---
name: proposal-writing
description: >-
  Agent guide (panduan) for writing Indonesian thesis PROPOSALS — a proposal is
  BAB I-III of a skripsi (a skripsi without the results chapters and beyond) plus
  DAFTAR PUSTAKA. Language style is copied from the TRSE-UNM corpus (69 documents),
  format rules from the Universitas Bina Darma 2022 writing guideline; EYD-V polish
  via the naskah-id skill; word-by-word optimization via GEPA (optimize_anything);
  large jobs sliced with the to-tickets skill. Use when asked to membuat/menulis/
  merevisi/memeriksa/mentilis proposal skripsi, proposal tugas akhir, DPJ /
  pengajuan judul / usulan judul, BAB 1 sampai BAB 3, pendahuluan-tinjauan
  pustaka-metodologi — especially the WiFi-CSI ESP32/RuView line (broiler coop,
  SLB, SIBI sign language). Skill files are English for token economy; every
  delivered sentence is Indonesian (bahasa Indonesia baku, EYD V).
metadata:
  version: "5.0-en"
  sources:
    - "TRSE-UNM 69-doc corpus (Drive folder 1Dk8kygzZZkFQE9uc-Z2zPbltToQMz-lF)"
    - "Panduan Penulisan Laporan Penelitian, Teknik Informatika, Universitas Bina Darma, 2022 (33 pp)"
    - "naskah-id skill (github.com/nothinx/naskah-id)"
    - "gepa-optimize-anything skill (owner archive)"
    - "to-tickets skill (mattpocock/skills)"
version: "5.0-en"
---

# proposal-writing v5

Write or repair an Indonesian research proposal that reads like the corpus (korpus
TRSE Universitas Negeri Malang, 69 documents): canonical
BAB I–III structure, corpus sentence patterns, verified citations, campus-format
mechanics, claim discipline, and a GEPA polish loop. **You copy the language, never
the content.**

## The output-language contract (binds everything below)

1. Skill files = English (token economy). **Every sentence you deliver to the user =
   Indonesian** — proposal text, messages, change notes.
2. Indonesian template strings inside the references are output material: copy them,
   substitute `[...]`; never round-trip them through English.
3. Markers: `[PERLU DATA: …]` / `[PERLU RUJUKAN: …]` only. Never fabricate facts,
   names, numbers, or references.
Details: `references/00-output-language.md`.

## Process

### 1. Lock decisions before writing
Collect: target case/location, main title + 2 alternatives (Judul Alternatif), scope
stop-line, duration (default 1 semester ≈ 4.5 months), style profile (DPJ-UNM default;
BD-2022 only for Bina Darma), citation style (APA 7). Unknown facts become
`[PERLU DATA: …]`.
**Done when:** decisions listed or marked; zero invented facts. → `references/01-scope.md`

### 2. Slice big jobs with to-tickets
Full proposal / multi-document / skill-scale work → `/to-tickets`: tracer-bullet
tickets (each demoable), blockers first, native blocking edges, quiz before publish.
Single-section fixes skip this. → `references/09-workflow.md`
**Done when:** every ticket has a demo path + real blockers; none is a horizontal slice.

### 3. Build the verified reference set
≥10 entries per proposal; verify (verifikasi) every DOI via Crossref
(`api.crossref.org/works/<DOI>`) or naskah-id `openalex.py`; save JSON; no-DOI entries
need a second web check. Unverifiable → `[PERLU RUJUKAN: …]`, never cite.
**Done when:** JSON saved, 0 fictional. → `references/04-citations.md`

### 4. Draft BAB I–III from the canonical skeleton
BAB I: Latar Belakang (4-layer funnel closing `Berdasarkan uraian tersebut, penelitian
ini dilakukan untuk …` + `Tabel 1.1` judul) → Rumusan Masalah (opener "Berdasarkan latar
belakang …"; items `Bagaimana …?`) → Tujuan Penelitian (opener "Penelitian ini
bertujuan untuk …"; mirrored verbs `Merancang / Mengimplementasikan / Mengetahui`) →
Batasan Masalah (opener "ruang lingkup yang jelas"; last item `Penelitian ini tidak
membahas …` + claim-discipline paragraph) → Manfaat Penelitian (Manfaat Teoretis /
Manfaat Praktis, sub-item `Bagi Peneliti …`). BAB II KAJIAN PUSTAKA: 8–13 concept
subsections (discuss, don't define-dump) → `Penelitian Terdahulu` with `√/−`
comparison table + gap prose. BAB III METODE PENELITIAN: stage narrative ("Tahap
pertama adalah studi literatur …"), studi literatur, perancangan, pengujian, evaluasi,
Jadwal (semester table), Biaya (Rupiah), Risiko. Then DAFTAR PUSTAKA. Use the verbatim
corpus openers and templates; reporting verbs `menjelaskan / menunjukkan`.
**Done when:** outline complete, ≥150 words planned per section, opener patterns in
place. → `references/02-structure.md`, `references/03-language-patterns.md`

### 5. Apply format & mechanics per style profile
Profile switch (DPJ-UNM vs BD-2022): fonts, margins, numbering, captions
(`Tabel` above / `Gambar` below, chapter-scoped), page numbers, foreign-term italics
policy. PUEBI mechanics: `memengaruhi`, desimal koma, judul kapital, no first person,
acronym rules; paragraph depth (paragraf 3–8 kalimat).
**Done when:** profile applied konsisten; lint passes. → `references/05-format-mechanics.md`

### 6. Polish language through naskah-id
Load only the mapped naskah-id references (pola-ai, kalimat-efektif, ejaan-eyd-v,
kata-baku, istilah, singkatan, pertahankan). Run `periksa.py <file>` (K/AI sweep) and
`periksa.py --banding asli draf` (facts unchanged) **per chapter** for manuscripts
>≈3,000 words. Known recurring fixes: → `references/06-ejaan-naskah-id.md`
**Done when:** 0 hard lint findings; every remaining finding justified in the notes.

### 7. Enforce claim discipline (WiFi-CSI line)
Feasibility-study framing only (studi kelayakan); pose stub forbidden (PCK@20 ≈ 3% —
do correct paradigm = klasifikasi gestur dari pola CSI); physical Delta-CSI 2×ESP32
gate as go/no-go; risk rows with mitigasi; kombinational novelty only; SIBI-only
scope for the sign-language case (BISINDO cited as landscape evidence only). Insert
the discipline-statement template at 1.4.
**Done when:** statement present at 1.4; zero stub promises; schedule marks the gate.
→ `references/07-claim-discipline.md`

### 8. Optimize wording with GEPA (word-by-word)
Per section: candidate = section text; evaluator = rubric D1–D6 score + periksa
findings − reward-hacking gates (facts preserved, no term-dump, length sane);
`max_evals ≥ 15–20`, `stop_at_score=1.0`; reflection_lm as z-ai callable in this
environment. Token-constrained fallback: manual reflective sweep (≤3 rounds).
**Done when:** score ≥ 0.8 (target 1.0), diff reviewed, change list written.
→ `references/08-gepa-loop.md`

### 9. Render + QA + handover
DOCX via the academic renderer (three-line tables, hanging-indent references,
`- N -` footer, no cover page (tanpa halaman sampul), no mid-content page breaks);
`postcheck.py` 0 errors; PDF page-count check; evaluator `--doc ≥ 0.8`. Deliver in
Indonesian: file + placeholder inventory + before→after change notes; append worklog;
push backup repo.
**Done when:** gates in `references/09-workflow.md` §3 all green; handover complete.

## Reviewing an existing proposal (other mode)

Run `scripts/evaluator.py --doc <file>`; report per-dimension D1–D6 scores + failed
rule lines + specific fixes; then walk steps 5–8 as needed. Same thresholds.

## Rubric summary (details in scripts/evaluator.py; weights in repo rubric.json)

- **D1 Structure (0.20)** — BAB I–III + DAFTAR PUSTAKA only; mandatory BAB I
  subsections; comparison table; schedule/cost/risk inside BAB III; consistent naming.
- **D2 Language patterns (0.20)** — corpus openers; funnel; question↔goal mirror;
  `tidak membahas` closer.
- **D3 Citations (0.15)** — corpus verbs; APA 7 hanging indent + DOI; bidirectional
  match; all verified.
- **D4 Mechanics (0.15)** — caps title pattern; chapter-scoped numbering; PUEBI.
- **D5 Claim discipline (0.15)** — feasibility only; no stub promises; Delta-CSI gate;
  risks explicit.
- **D6 Completeness (0.15)** — 1 title + 2 alternatives; schedule; budget; scope
  bound; no cover; placeholders explicit.

## Reference files (load on demand)

| File | Load when |
|---|---|
| `references/00-output-language.md` | always (contract) |
| `references/01-scope.md` | step 1 |
| `references/02-structure.md` | step 4 skeleton |
| `references/03-language-patterns.md` | step 4 drafting |
| `references/04-citations.md` | step 3 + citation checks |
| `references/05-format-mechanics.md` | step 5 + rendering |
| `references/06-ejaan-naskah-id.md` | step 6 polish |
| `references/07-claim-discipline.md` | step 5/8 (WiFi-CSI line) |
| `references/08-gepa-loop.md` | step 8 optimization |
| `references/09-workflow.md` | step 2 slicing + gates |

## External skills this guide wires in

- **naskah-id** (github.com/nothinx/naskah-id) — EYD-V editing + verification ethics.
- **gepa-optimize-anything** — `optimize_anything` API for the polish loop.
- **to-tickets** (mattpocock) — ticket slicing with blocking edges.
