#!/usr/bin/env python3
"""
build-search-index.py

Extracts text from all OSCE exam PDFs page-by-page and builds search-index.json.
Each page of each PDF becomes one searchable entry with its page number.

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


def parse_filename(name: str) -> dict | None:
    stem = name.replace('.pdf', '')
    parts = stem.split('_')
    if len(parts) < 4:
        return None

    level_map = {'osce1': 1, 'osce2': 2, 'osce3': 3}
    level = level_map.get(parts[0])
    if not level:
        return None

    exam_type = parts[1]
    semester = parts[2].upper()
    doctype = parts[3]

    cirkel = ''
    for p in parts[4:]:
        if p.startswith('cirkel'):
            cirkel = p
        elif p == '6min':
            doctype = 'kombi'

    return {
        'level': level,
        'type': exam_type,
        'semester': semester,
        'doctype': doctype,
        'cirkel': cirkel,
    }


def exam_id_from_info(info: dict) -> str:
    if info['doctype'] == 'kombi' and info.get('_6min'):
        return f"osce{info['level']}_om_{info['semester'].lower()}"
    return f"osce{info['level']}_{info['type']}_{info['semester'].lower()}"


def build_index(base_dir: Path, fitz) -> list:
    entries = []

    for pdf in sorted(base_dir.rglob('*.pdf')):
        info = parse_filename(pdf.name)
        if not info:
            print(f"  Skipping unrecognised: {pdf.name}")
            continue

        eid = exam_id_from_info(info)
        rel_path = str(pdf.relative_to(base_dir.parent))
        cirkel_display = info['cirkel'].replace('cirkel-', '').upper() if info['cirkel'] else ''

        print(f"  {rel_path} ({len(list(range(0)))} pages)...", end='')
        try:
            doc = fitz.open(str(pdf))
            page_count = len(doc)
            print(f" {page_count} pages")
            for page_idx in range(page_count):
                page = doc[page_idx]
                text = page.get_text().strip()
                if len(text) < 10:
                    continue
                entries.append({
                    "examId": eid,
                    "file": rel_path,
                    "fileType": info['doctype'],
                    "page": page_idx + 1,
                    "level": info['level'],
                    "type": info['type'],
                    "semester": info['semester'],
                    "cirkel": cirkel_display,
                    "text": text,
                })
            doc.close()
        except Exception as e:
            print(f" ERROR: {e}")

    return entries


def main():
    base_dir = Path(__file__).parent / 'exams'
    if not base_dir.exists():
        print(f"Error: {base_dir} not found. Run from project root.")
        sys.exit(1)

    fitz = ensure_pymupdf()
    print(f"Building page-level search index from {base_dir}...")
    entries = build_index(base_dir, fitz)

    import datetime
    output = {
        "generated": datetime.datetime.now().isoformat(),
        "pageCount": len(entries),
        "pages": entries,
    }

    out_path = Path(__file__).parent / 'search-index.json'
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"\nWrote {len(entries)} page entries to {out_path}")


if __name__ == '__main__':
    main()
