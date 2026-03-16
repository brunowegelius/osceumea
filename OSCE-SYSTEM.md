# OSCE Studieportal — Systemdesign

## 1. Standardiserat filnamnssystem

### Format
```
{nivå}_{typ}_{termin}_{doktyp}[_{variant}].pdf
```

| Del | Värden | Beskrivning |
|-----|--------|-------------|
| `nivå` | `osce1`, `osce2`, `osce3` | OSCE I (T6), OSCE II (T8), OSCE III (T11) |
| `typ` | `ord`, `om` | Ordinarie eller omexamination |
| `termin` | `vt22`, `ht22`, `vt23`, … `ht25` | Termin + år |
| `doktyp` | `dorr`, `bed`, `kombi` | Dörrinformation, bedömningsmall, eller kombinerad |
| `variant` | `cirkel-a`, `cirkel-b`, `cirkel-c`, `6min` | Valfritt — cirkel/variant |

### Komplett filnamnsmappning

#### OSCE I (T6)

| Nuvarande filnamn | Nytt filnamn |
|---|---|
| `OSCE I HT25 - DÖRRINFORMATION.pdf` | `osce1_ord_ht25_dorr.pdf` |
| `OSCE I HT25 - BEDÖMNINGSMALLAR.pdf` | `osce1_ord_ht25_bed.pdf` |
| `OSCE I VT25 - DÖRRINFORMATION.pdf` | `osce1_ord_vt25_dorr.pdf` |
| `OSCE I VT25 - BEDÖMNINGSMALLAR.pdf` | `osce1_ord_vt25_bed.pdf` |
| `OSCE I HT24 - DÖRRINFORMATION.pdf` | `osce1_ord_ht24_dorr.pdf` |
| `OSCE I HT24 - BEDÖMNINGSMALLAR.pdf` | `osce1_ord_ht24_bed.pdf` |
| `OSCE I VT24 - DÖRRINFORMATION.pdf` | `osce1_ord_vt24_dorr.pdf` |
| `OSCE I VT24 - BEDÖMNINGSMALLAR.pdf` | `osce1_ord_vt24_bed.pdf` |
| `1. Dörrinformation OSCE I HT23.pdf` | `osce1_ord_ht23_dorr.pdf` |
| `2. Bedömningsmallar OSCE I HT23.pdf` | `osce1_ord_ht23_bed.pdf` |
| `1. Dörrinformation OSCE I VT23.pdf` | `osce1_ord_vt23_dorr.pdf` |
| `2. Bedömningsmallar OSCE I VT23.pdf` | `osce1_ord_vt23_bed.pdf` |
| `1. Dörrinformation OSCE I VT22.pdf` | `osce1_ord_vt22_dorr.pdf` |
| `2. Bedömningsmallar OSCE I VT22.pdf` | `osce1_ord_vt22_bed.pdf` |
| `5. Dörrinformation OSCE I HT22.pdf` | `osce1_ord_ht22_dorr.pdf` |
| `6. Bedömningsmallar OSCE I HT22.pdf` | `osce1_ord_ht22_bed.pdf` |
| `OMOSCE I VT25 - DÖRRINFORMATION.pdf` | `osce1_om_vt25_dorr.pdf` |
| `OMOSCE I VT25 - BEDÖMNINGSMALLAR.pdf` | `osce1_om_vt25_bed.pdf` |
| `Dörrinformation OmOSCE I HT24_reviderad.pdf` | `osce1_om_ht24_dorr.pdf` |
| `ALLA bedömarmallar omOSCE I HT24.pdf` | `osce1_om_ht24_bed.pdf` |
| `OMOSCE I VT24 CIRKEL 1 och 2 - DÖRRINFORMATION.pdf` | `osce1_om_vt24_dorr.pdf` |
| `OMOSCE I VT24 BEDÖMNINGSMALLAR CIRKEL 1.pdf` | `osce1_om_vt24_bed_cirkel-1.pdf` |
| `OMOSCE I VT24 BEDÖMNINGSMALLAR CIRKEL 2.pdf` | `osce1_om_vt24_bed_cirkel-2.pdf` |
| `OMOSCE I HT23 - DÖRRINFORMATION.pdf` | `osce1_om_ht23_dorr.pdf` |
| `4. Bedömningsmallar OMOSCE I HT23.pdf` | `osce1_om_ht23_bed.pdf` |
| `3. Dörrinformation omOSCE I VT23.pdf` | `osce1_om_vt23_dorr.pdf` |
| `4. Bedömningsmallar omOSCE I VT23 cirkel 1.pdf` | `osce1_om_vt23_bed_cirkel-1.pdf` |
| `4. Bedömningsmallar omOSCE I VT23 cirkel 2.pdf` | `osce1_om_vt23_bed_cirkel-2.pdf` |
| `3. Dörrinformation omOSCE I VT22.pdf` | `osce1_om_vt22_dorr.pdf` |
| `4. Bedömningsmallar omOSCE I VT22-2.pdf` | `osce1_om_vt22_bed.pdf` |
| `7. Dörrinformation omOSCE HT22.pdf` | `osce1_om_ht22_dorr.pdf` |
| `8. Bedömningsmallar omOSCE I HT22.pdf` | `osce1_om_ht22_bed.pdf` |

#### OSCE II (T8)

| Nuvarande filnamn | Nytt filnamn |
|---|---|
| `OSCE II VT25 Dörrinformation.pdf` | `osce2_ord_vt25_dorr.pdf` |
| `OSCE II VT25 Bedömningsunderlag.pdf` | `osce2_ord_vt25_bed.pdf` |
| `Dörrinfo alla stationer OSCE II HT25.pdf` | `osce2_ord_ht25_dorr.pdf` |
| `OSCE II HT25 Bedömningsunderlag.pdf` | `osce2_ord_ht25_bed.pdf` |
| `Dörrinfo alla stationer OSCE II HT24.pdf` | `osce2_ord_ht24_dorr.pdf` |
| `Bedömingsmallar OSCE II HT24.pdf` | `osce2_ord_ht24_bed.pdf` |
| `Dörrinformation OSCE II VT24.pdf` | `osce2_ord_vt24_dorr.pdf` |
| `Bedömningsmallar OSCE II VT24.pdf` | `osce2_ord_vt24_bed.pdf` |
| `OSCE II HT23 Dörrinformation.pdf` | `osce2_ord_ht23_dorr.pdf` |
| `OSCE II HT23 Bedömningsunderlag.pdf` | `osce2_ord_ht23_bed.pdf` |
| `OSCE II VT23 Dörrinformation.pdf` | `osce2_ord_vt23_dorr.pdf` |
| `OSCE II VT23 Bedömningsunderlag.pdf` | `osce2_ord_vt23_bed.pdf` |
| `OSCE II VT22 Dörrinformation.pdf` | `osce2_ord_vt22_dorr.pdf` |
| `OSCE II VT 22 Bedömningsunderlag.pdf` | `osce2_ord_vt22_bed.pdf` |
| `OSCE II HT22 Dörrinformation.pdf` | `osce2_ord_ht22_dorr.pdf` |
| `OSCE II HT22 Bedömningsunderlag.pdf` | `osce2_ord_ht22_bed.pdf` |
| `om-OSCE II HT25 Dörrinformation.pdf` | `osce2_om_ht25_dorr.pdf` |
| `om-OSCE II HT25 Bedömningsunderlag.pdf` | `osce2_om_ht25_bed.pdf` |
| `Bedömningsmallar om-OSCE II VT25.pdf` | `osce2_om_vt25_bed.pdf` |
| `Dörrinfo om-OSCE II HT24 Cirkel A.pdf` | `osce2_om_ht24_dorr_cirkel-a.pdf` |
| `Dörrinfo om-OSCE II HT24 Cirkel B.pdf` | `osce2_om_ht24_dorr_cirkel-b.pdf` |
| `Bedömningsunderlag om-OSCE II HT24 Cirkel A.pdf` | `osce2_om_ht24_bed_cirkel-a.pdf` |
| `Bedömningsunderlag om-OSCE II HT24 Cirkel B.pdf` | `osce2_om_ht24_bed_cirkel-b.pdf` |
| `Dörrinfo alla stationer om-OSCE II VT24.pdf` | `osce2_om_vt24_dorr.pdf` |
| `om-OSCE II VT24 Cirkel A Bedömningsmall.pdf` | `osce2_om_vt24_bed_cirkel-a.pdf` |
| `om-OSCE II VT24 Cirkel B Bedömningsmall.pdf` | `osce2_om_vt24_bed_cirkel-b.pdf` |
| `om-OSCE II VT24 Cirkel C Bedömningsmall.pdf` | `osce2_om_vt24_bed_cirkel-c.pdf` |
| `Dörrinfo alla stationer om-OSCE II HT23.pdf` | `osce2_om_ht23_dorr.pdf` |
| `Bedömningsmall alla stationer om-OSCE II HT23.pdf` | `osce2_om_ht23_bed.pdf` |
| `Dörrinformation OM OSCE II VT23.pdf` | `osce2_om_vt23_dorr.pdf` |
| `om-OSCE II VT23 Bedömningsunderlag.pdf` | `osce2_om_vt23_bed.pdf` |
| `om-OSCE II VT22 Dörrinformation.pdf` | `osce2_om_vt22_dorr.pdf` |
| `Bedömningsmall om-OSCE II VT22 Cirkel A.pdf` | `osce2_om_vt22_bed_cirkel-a.pdf` |
| `Bedömningsmall om-OSCE II VT22 Cirkel B.pdf` | `osce2_om_vt22_bed_cirkel-b.pdf` |
| `om-OSCE II HT22 Dörrinformation.pdf` | `osce2_om_ht22_dorr.pdf` |
| `om-OSCE II HT22 Cirkel A Bedömningsunderlag.pdf` | `osce2_om_ht22_bed_cirkel-a.pdf` |
| `om-OSCE II HT22 Cirkel B Bedömningsunderlag.pdf` | `osce2_om_ht22_bed_cirkel-b.pdf` |

#### OSCE III (T11)

| Nuvarande filnamn | Nytt filnamn |
|---|---|
| `OSCE III HT25 Dörrinstruktioner och bedömningsunderlag.pdf` | `osce3_ord_ht25_kombi.pdf` |
| `OSCE III VT25 Dörrinstruktioner och bedömningsunderlag.pdf` | `osce3_ord_vt25_kombi.pdf` |
| `OSCE III HT24 Dörrinstruktioner och bedömningsunderlag.pdf` | `osce3_ord_ht24_kombi.pdf` |
| `OSCE III VT24 Dörrinstruktioner och bedömningsunderlag.pdf` | `osce3_ord_vt24_kombi.pdf` |
| `OSCE III HT23 Dörrinstruktioner och bedömningsunderlag.pdf` | `osce3_ord_ht23_kombi.pdf` |
| `OSCE III VT23 Dörrinstruktioner och bedömningsunderlag.pdf` | `osce3_ord_vt23_kombi.pdf` |
| `OSCE III VT22 Dörrinstruktioner.pdf` | `osce3_ord_vt22_dorr.pdf` |
| `OSCE III VT22 Bedömningsunderlag.pdf` | `osce3_ord_vt22_bed.pdf` |
| `OSCE III HT22 Dörrinstruktioner och bedömningsunderlag.pdf` | `osce3_ord_ht22_kombi.pdf` |
| `250507 Dörrinfo och bedömning 6 min.pdf` | `osce3_ord_vt25_kombi_6min.pdf` |
| `2024-11-13 6 min Dörrinfo och bedömnin.pdf` | `osce3_ord_ht24_kombi_6min.pdf` |
| `240424 6 minutersstationer Dörrinfo och bedömnin.pdf` | `osce3_ord_vt24_kombi_6min.pdf` |
| `om-OSCE III HT25 Dörrinstruktioner och bedömningsunderlag.pdf` | `osce3_om_ht25_kombi.pdf` |
| `om-OSCE III HT23 Dörrinstruktioner och bedömningsunderlag.pdf` | `osce3_om_ht23_kombi.pdf` |
| `om-OSCE III VT23 Dörrinstruktioner och bedömningsunderlag.pdf` | `osce3_om_vt23_kombi.pdf` |
| `om-OSCE III VT22 Dörrinstruktioner och bedömningsunderlag.pdf` | `osce3_om_vt22_kombi.pdf` |
| `om-OSCE III HT22 Dörrinstruktioner och bedömningsunderlag.pdf` | `osce3_om_ht22_kombi.pdf` |

---

## 2. System för kategorisering och visning

### Datastruktur: `exams.json`

Alla filer registreras i en central JSON-fil som hemsidan läser. Varje examination blir ett objekt med metadata som gör filtrering och sökning trivialt.

```json
{
  "exams": [
    {
      "id": "osce1_ord_ht25",
      "level": 1,
      "levelLabel": "OSCE I (T6)",
      "type": "ord",
      "typeLabel": "Ordinarie",
      "semester": "HT25",
      "semesterSort": "2025-2",
      "files": {
        "dorr": "exams/osce1/osce1_ord_ht25_dorr.pdf",
        "bed": "exams/osce1/osce1_ord_ht25_bed.pdf"
      },
      "tags": ["kirurgi", "internmedicin", "neurologi"]
    },
    {
      "id": "osce3_ord_ht25",
      "level": 3,
      "levelLabel": "OSCE III (T11)",
      "type": "ord",
      "typeLabel": "Ordinarie",
      "semester": "HT25",
      "semesterSort": "2025-2",
      "files": {
        "kombi": "exams/osce3/osce3_ord_ht25_kombi.pdf"
      },
      "tags": ["akutmedicin", "pediatrik"]
    },
    {
      "id": "osce2_om_ht24",
      "level": 2,
      "levelLabel": "OSCE II (T8)",
      "type": "om",
      "typeLabel": "Omexamination",
      "semester": "HT24",
      "semesterSort": "2024-2",
      "files": {
        "dorr_cirkel-a": "exams/osce2/osce2_om_ht24_dorr_cirkel-a.pdf",
        "dorr_cirkel-b": "exams/osce2/osce2_om_ht24_dorr_cirkel-b.pdf",
        "bed_cirkel-a": "exams/osce2/osce2_om_ht24_bed_cirkel-a.pdf",
        "bed_cirkel-b": "exams/osce2/osce2_om_ht24_bed_cirkel-b.pdf"
      },
      "tags": ["psykiatri", "ortopedi"]
    }
  ]
}
```

### Mappstruktur i GitHub-repot

```
osce-umea/
├── index.html              ← Hela appen (single-page app)
├── exams.json              ← Central metadata-fil
├── exams/
│   ├── osce1/
│   │   ├── osce1_ord_ht25_dorr.pdf
│   │   ├── osce1_ord_ht25_bed.pdf
│   │   ├── osce1_om_vt24_bed_cirkel-1.pdf
│   │   └── ...
│   ├── osce2/
│   │   └── ...
│   └── osce3/
│       └── ...
└── README.md
```

### Visningskoncept på hemsidan

**Huvudvy — "Examinationer"**
- Filtrera på: OSCE-nivå (I/II/III), typ (ord/om), termin
- Varje examination visas som ett kort med: termin, typ, badge för antal filer
- Klicka → öppnar en "studievy"

**Studievy (per examination)**
- Delad skärm (split-view): dörrinfo till vänster, bedömningsmall till höger
- Båda PDF:erna inbäddade via `<iframe>` eller PDF.js
- Om filen är `kombi` → visa enbart den i helskärm
- Om det finns cirklar → dropdown för att välja cirkel

**Checkoff-system**
- Varje examination har en checkbox "Klar ✓"
- Sparas i `localStorage` i webbläsaren (kräver ingen backend)
- Progressbar per OSCE-nivå som visar "12/16 klara"
- Eventuellt även per station om stationerna extraheras ur PDF:erna

**Ämnesvy — "Filtrera på ämne"**
- `tags`-fältet i `exams.json` gör det möjligt att filtrera per ämnesområde
- Visar alla examinationer som innehåller t.ex. "kirurgi"
- **OBS:** Taggarna behöver fyllas i manuellt efter att du/ni läst igenom PDF:erna och identifierat vilka ämnen varje station täcker. Alternativt kan Claude Code hjälpa till att extrahera text ur PDF:erna och föreslå taggar.

---

## 3. Claude Code-prompt

Kopiera och klistra in detta i Claude Code (VS Code) efter att du har:
1. Skapat GitHub-repot
2. Döpt om alla filer enligt mappningen ovan
3. Lagt dem i `exams/osce1/`, `exams/osce2/`, `exams/osce3/`
4. Skapat `exams.json` med alla examinationer

---

### Prompt att kopiera:

```
Jag bygger en studieportal för OSCE-examinationer (läkarprogrammet, Umeå Universitet). Repot innehåller redan alla PDF-filer och en exams.json. Skapa en komplett single-page webapp (index.html med inbäddad CSS/JS, inga ramverk) som gör följande:

## Datamodell
Läs exams.json som innehåller alla examinationer. Varje examination har:
- id, level (1/2/3), levelLabel, type (ord/om), typeLabel, semester, semesterSort
- files: objekt med nycklar som "dorr", "bed", "kombi", eller varianter som "dorr_cirkel-a", "bed_cirkel-a"
- tags: array med ämnesområden (t.ex. ["kirurgi", "internmedicin"])

## Sidor/vyer (SPA med hash-routing)

### 1. Startsida (#/)
- Rubrik "OSCE Studieportal — Umeå Universitet"
- Tre kort för OSCE I (T6), OSCE II (T8), OSCE III (T11) med progressbar som visar hur många examinationer användaren markerat som klara
- Knapp "Filtrera på ämne" som leder till ämnesvyn

### 2. Examinationslista (#/osce/1, #/osce/2, #/osce/3)
- Visa alla examinationer för vald OSCE-nivå
- Filtreringsknappar: Ordinarie / Omexamination / Alla
- Sortera kronologiskt (nyast först)
- Varje examination som ett kort med:
  - Termin + typ (t.ex. "HT25 — Ordinarie")
  - Badge som visar antal filer
  - Checkbox "Klar" som sparar till localStorage
  - Klickbar → öppnar studievyn

### 3. Studievy (#/exam/{id})
- Om filen är "kombi": visa PDF:en i helskärm med inbäddad PDF-viewer
- Om separata dorr + bed: delad skärm (split-view) med dörrinfo till vänster (50%) och bedömningsmall till höger (50%)
- Om det finns cirkelvarianter: dropdown högst upp för att välja cirkel
- Använd <iframe> med PDF-sökvägen för att visa PDF:erna
- Knapp "Markera som klar" + knapp "Tillbaka"

### 4. Ämnesvy (#/tags)
- Visa alla unika tags från exams.json som klickbara knappar/chips
- Klicka på en tag → filtrera fram alla examinationer med den taggen
- Samma kort-layout som examinationslistan

## Design
- Modernt, rent, mobilanpassat (responsive)
- Färgschema: vitt med blåa accenter (Umeå-känsla)
- Typsnitt: system-font-stack
- Inga externa beroenden förutom eventuellt PDF.js om <iframe> inte räcker

## Checkoff-system
- Använd localStorage för att spara vilka examinationer som är klara
- Nyckelmönster: "osce_done_{id}" = true/false
- Progressbars på startsidan som uppdateras live

## Viktigt
- Appen ska fungera helt statiskt (inga servrar, bara GitHub Pages)
- Alla PDF-sökvägar är relativa till index.html
- Appen ska kunna hostas via GitHub Pages direkt
- Testa att hash-routing fungerar korrekt
- Se till att split-view fungerar bra på både desktop och mobil (stacka vertikalt på mobil)
```

---

## Nästa steg

1. **Skapa GitHub-repot** — t.ex. `osce-umea`
2. **Döp om filerna** — använd mappningen ovan (kan göras med ett enkelt bash-script)
3. **Lägg filerna i rätt mappar** — `exams/osce1/`, `exams/osce2/`, `exams/osce3/`
4. **Skapa exams.json** — fyll i alla examinationer med metadata. Tags kan läggas till efterhand.
5. **Kör Claude Code-prompten** — i VS Code, klistra in prompten ovan
6. **Deploya till GitHub Pages** — Settings → Pages → Deploy from main branch
7. **Fyll i ämnestaggar** — gå igenom PDF:erna och tagga varje examination med ämnesområden

### Bash-script för att döpa om filerna

Om du vill kan jag generera ett komplett bash-script som automatiskt döper om alla filer enligt mappningen. Säg bara till!
