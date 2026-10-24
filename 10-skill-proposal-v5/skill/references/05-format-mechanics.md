# 05 — Format Mechanics: Two Style Profiles + PUEBI Mechanics

Source: BD-2022 §3.1–3.5 (page setup, styles, punctuation, numbering, captions)
+ DPJ/TRSE renderer conventions (previous QA-passed DOCX lineage).

## 0. Style profile switch (decide once per document)

| Aspect | Profile **DPJ-UNM** (default) | Profile **BD-2022** |
|---|---|---|
| Paper / font | A4, Times New Roman 12 pt | A4, Cambria 12 pt, min 25 sheets excl. references |
| Margins | (as approved DOCX lineage) | left 4 cm; top/right/bottom 3 cm |
| Body paragraphs | line ~1.5, justified-first-line conventions of lineage | Normal: justify, single; `_bernomor` lists: 1.5; quote: 1.5, indent left 3,25 cm |
| Headings | `BAB I` (two lines: BAB I / PENDAHULUAN), subsections `1.1` | `1. Sub Bab`, `2.1.1. Sub Sub bab`, then `a., b., c.`; H1 bold |
| Page numbers | footer `- N -` | front matter: roman lowercase bottom-center; body: arabic bottom-right |
| Table caption | per-bab numbering, above table | **above** table, left-aligned: `Tabel 3.3. Desain tabel pelanggan` (number bold, title normal) |
| Figure caption | per-bab numbering, below | **below** figure, centered: `Gambar 4.1. Tampilan Home` |
| Table styles | three-line tables | header 9 pt bold centered; body 9 pt; caption 12 pt |
| Code/script | 10 pt monospace-ish block | `Script` 10 pt single-spaced |
| Foreign terms | unitalicized (consistency decision) | **italicize** all unabsorbed foreign terms |
| Page breaks | only after title block | front matter / body transitions |

Both profiles: table/figure numbers are **chapter-scoped** (`Tabel 2.1`, `Gambar 3.1`),
every table and figure introduced by a sentence, no floating captions.

## 1. PUEBI/EYD-V mechanics (hard rules, both profiles)

- `memengaruhi`, never `mempengaruhi`.
- Decimal comma (`0,9967`); percent without space (`99%`); `2×ESP32` allowed.
- No first person. Subjects: `penelitian ini`, `sistem`, `alat`.
- `antar-`/`lintas-` compounds hyphenated when the second element is a phrase,
  solid when lexicalized (`antarsesi`); stay consistent per document.
- `per-` as prefix attached (`perkecil`), as preposition separate (`per bulan`).
- Acronyms without dots (`SIM`, not `S.I.M.`).
- Capitalize `Doppler`; `entropi` not `entropy`; `ambang` not `threshold` (measure
  with openalex `istilah` when unsure — 06).
- Foreign-term italics: profile-dependent (see table above + 00).

## 2. Punctuation (BD §3.3 condensed — apply literally)

- **Titik (.)** ends non-exclamatory sentences; no dot after `?`/`!`; no dots in acronyms.
- **Koma (,)**: between enumerated elements (`keyboard, mouse, dan scanner`); before
  contrast conjunctions (*tetapi, melainkan*); around appositive insertions
  (`Kondisi seperti di atas, yaitu suhu 25 °C, …`).
- **Titik koma (;)**: between enumeration elements that already contain commas
  (multi-source citations — 04 §2).
- **Titik dua (:)** ends a complete statement followed by detail (specs lists,
  ≥40-word quote intros).
- **Petik (" ")**: direct quotes incl. literal translations.
- **Hubung (-)**: syllable wraps; reduplicated words; `se-`+proper noun, `ke-`+number,
  number+`-an`, ID element + foreign element (`se-Indonesia`, `ujicoba ke-2`,
  `tahun 90-an`, `di-print`).
- **Pisah (– en dash)**: ranges (`tanggal 5–10 April`). **(— em dash)**: emphatic
  insertion (`Findability—yang meliputi …—merupakan …`).
- **Kurung (( ))**: supplementary explanation. **Elipsis (…)**: omitted text.

## 3. Rendering pipeline (DOCX deliverables)

- Reuse the academic renderer (`dpj_common.js` lineage): TNR/Cambria per profile,
  three-line tables, `[n]`-free author–year citations, hanging-indent reference list,
  `- N -` footer (DPJ), no mid-content page breaks, no cover.
- After render: `postcheck.py` (docx skill) must report 0 errors; convert to PDF and
  check page count + visual spot-check of title block, one table, numbered list.

> Done when: profile chosen and applied consistently; periksa lint passes (06);
> postcheck 0 errors.
