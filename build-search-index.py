#!/usr/bin/env python3
"""
build-search-index.py

Extracts text from all OSCE exam PDFs and builds search-index.json.
Each identified station becomes a searchable entry.

Usage:
    pip install pymupdf
    python build-search-index.py
"""

import json
import re
import sys
from pathlib import Path


def ensure_pymupdf():
    try:
        import fitz
        return fitz
    except ImportError:
        print("pymupdf not found, installing...")
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pymupdf"])
        import fitz
        return fitz


def extract_text(fitz, pdf_path: Path) -> str:
    try:
        doc = fitz.open(str(pdf_path))
        parts = []
        for page in doc:
            parts.append(page.get_text())
        doc.close()
        return "\n".join(parts)
    except Exception as e:
        print(f"  Warning: could not read {pdf_path.name}: {e}")
        return ""


def split_stations(text: str) -> dict:
    """
    Split text into stations keyed by station number.
    Returns {station_number: text_block}.
    If no station headers found, returns {0: full_text}.
    """
    pattern = re.compile(
        r'(?:^|\n)[ \t]*(?:STATION|Station|station)[ \t]*(\d+)',
        re.MULTILINE
    )
    matches = list(pattern.finditer(text))
    if not matches:
        return {0: text.strip()}

    stations = {}
    for i, m in enumerate(matches):
        num = int(m.group(1))
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        stations[num] = text[start:end].strip()
    return stations


def parse_filename(name: str) -> dict | None:
    """
    Parse filename like 'osce1_ord_ht25_dorr.pdf' into components.
    Returns None if unrecognised.
    """
    stem = name.replace('.pdf', '')
    parts = stem.split('_')
    if len(parts) < 4:
        return None

    level_map = {'osce1': 1, 'osce2': 2, 'osce3': 3}
    level = level_map.get(parts[0])
    if not level:
        return None

    exam_type = parts[1]  # ord | om
    semester = parts[2].upper()
    doctype = parts[3]    # dorr | bed | kombi

    cirkel = None
    variant = None
    if len(parts) >= 5:
        suffix = parts[4]
        if suffix.startswith('cirkel'):
            cirkel = suffix  # e.g. "cirkel-a"
        elif suffix == '6min':
            doctype = 'kombi_6min'
        # possible: parts[5] could also be cirkel after doctype

    return {
        'level': level,
        'type': exam_type,
        'semester': semester,
        'doctype': doctype,
        'cirkel': cirkel,
    }


def exam_id_from_info(info: dict) -> str:
    return f"osce{info['level']}_{info['type']}_{info['semester'].lower()}"


def semester_sort(semester: str) -> str:
    s = semester.upper()
    year = 2000 + int(s[2:])
    half = '2' if s.startswith('HT') else '1'
    return f"{year}-{half}"


def level_label(level: int) -> str:
    return ['OSCE I (T6)', 'OSCE II (T8)', 'OSCE III (T11)'][level - 1]


def build_index(base_dir: Path, fitz) -> list:
    # Group files by (exam_id, cirkel) → {doctype: path}
    groups: dict[tuple, dict] = {}

    for pdf in sorted(base_dir.rglob('*.pdf')):
        info = parse_filename(pdf.name)
        if not info:
            continue
        eid = exam_id_from_info(info)
        cirkel = info['cirkel'] or ''
        key = (eid, cirkel, info)
        # Use (eid, cirkel) as the group key, store info once
        gkey = (eid, cirkel)
        if gkey not in groups:
            groups[gkey] = {'_info': info, '_eid': eid}
        groups[gkey][info['doctype']] = pdf

    stations = []
    print(f"Found {len(groups)} file groups across all exams")

    for (eid, cirkel), files in sorted(groups.items()):
        info = files['_info']
        cirkel_suffix = f"_{cirkel}" if cirkel else ""
        cirkel_display = cirkel.replace('cirkel-', 'Cirkel ').upper() if cirkel else ''

        dorr_path = files.get('dorr')
        bed_path = files.get('bed')
        kombi_path = files.get('kombi') or files.get('kombi_6min')

        print(f"  Processing {eid}{cirkel_suffix}...")

        def rel(p: Path) -> str:
            return str(p.relative_to(base_dir.parent))

        if kombi_path:
            text = extract_text(fitz, kombi_path)
            station_texts = split_stations(text)
            for st_num, st_text in station_texts.items():
                sid = f"{eid}{cirkel_suffix}_st{st_num}" if st_num else f"{eid}{cirkel_suffix}_full"
                stations.append({
                    "id": sid,
                    "examId": eid,
                    "stationNumber": st_num,
                    "level": info['level'],
                    "levelLabel": level_label(info['level']),
                    "type": info['type'],
                    "semester": info['semester'],
                    "semesterSort": semester_sort(info['semester']),
                    "cirkel": cirkel_display,
                    "isKombi": True,
                    "dorrFile": rel(kombi_path),
                    "bedFile": rel(kombi_path),
                    "dorrText": st_text,
                    "bedText": st_text,
                    "searchableText": st_text,
                })
        else:
            dorr_texts = split_stations(extract_text(fitz, dorr_path)) if dorr_path else {}
            bed_texts = split_stations(extract_text(fitz, bed_path)) if bed_path else {}
            all_nums = sorted(set(list(dorr_texts) + list(bed_texts)))

            for st_num in all_nums:
                dt = dorr_texts.get(st_num, '')
                bt = bed_texts.get(st_num, '')
                combined = (dt + '\n' + bt).strip()
                sid = f"{eid}{cirkel_suffix}_st{st_num}" if st_num else f"{eid}{cirkel_suffix}_full"
                stations.append({
                    "id": sid,
                    "examId": eid,
                    "stationNumber": st_num,
                    "level": info['level'],
                    "levelLabel": level_label(info['level']),
                    "type": info['type'],
                    "semester": info['semester'],
                    "semesterSort": semester_sort(info['semester']),
                    "cirkel": cirkel_display,
                    "isKombi": False,
                    "dorrFile": rel(dorr_path) if dorr_path else '',
                    "bedFile": rel(bed_path) if bed_path else '',
                    "dorrText": dt,
                    "bedText": bt,
                    "searchableText": combined,
                })

    return stations


def main():
    base_dir = Path(__file__).parent / 'exams'
    if not base_dir.exists():
        print(f"Error: {base_dir} not found. Run from project root.")
        sys.exit(1)

    fitz = ensure_pymupdf()
    print(f"Building search index from {base_dir}...")
    stations = build_index(base_dir, fitz)

    import datetime
    output = {
        "generated": datetime.datetime.now().isoformat(),
        "stationCount": len(stations),
        "stations": stations,
    }

    out_path = Path(__file__).parent / 'search-index.json'
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"\n✓ Wrote {len(stations)} stations to {out_path}")


if __name__ == '__main__':
    main()
