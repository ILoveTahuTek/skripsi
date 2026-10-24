# 02 — Canonical Structure BAB I–III + Mandatory Tables

Sources: 12-document TRSE-UNM corpus (8/8 consistent) merged with BD-2022 guideline
§2.1–2.2. Chapter names stay consistent across the whole document (pick ONE variant
per bracketed pair and keep it).

## Document order

```
Title block (caps) + Judul Alternatif 1/2
BAB I PENDAHULUAN
BAB II KAJIAN PUSTAKA | TINJAUAN PUSTAKA
BAB III METODE PENELITIAN | METODOLOGI PENELITIAN
DAFTAR PUSTAKA
```

## BAB I PENDAHULUAN — mandatory subsections, in order

| # | Subsection | Content contract |
|---|---|---|
| 1.1 | Latar Belakang | 4-layer funnel (03) + Table `Tabel 1.1` of proposed titles (main + alternatives) |
| 1.2 | Rumusan Masalah | 2–4 numbered questions `Bagaimana …?` (corpus pattern; BD allows statements — default to questions) |
| 1.3 | Tujuan Penelitian | mirrors 1.2 one-to-one, action-verb phrases |
| 1.4 | Batasan Masalah | numbered; last item `Penelitian ini tidak membahas …`; ends with claim-discipline paragraph (07) |
| 1.5 | Manfaat Penelitian | `1.5.1 Manfaat Teoretis`, `1.5.2 Manfaat Praktis` (sub-items `Bagi …`) |

BD-2022 wording of the same five (sanity check, §2.2a): Latarbelakang = gap between
real and ideal state + why the research matters; Perumusan Masalah = questions/utterances
pinning the focus; Tujuan = what is achieved when research ends; Ruang Lingkup dan
Batasan = what is solved + assumptions; Manfaat = impact when goals are met.

## BAB II KAJIAN PUSTAKA — 8–13 subsections

- One subsection per concept/technology, ordered system → components
  (e.g., 2.1 Wi-Fi CSI; 2.2 ESP32; 2.3 RuView platform (+`Tabel 2.1` feature map);
  2.4 domain concept; 2.5 …; last subsection `2.n Penelitian Terdahulu`).
- **Discussion, not a definition dump** (BD §2.2b): every subsection must argue why
  the concept matters to THIS design, not merely define it.
- `2.n Penelitian Terdahulu` **must** end with the comparison table + gap prose
  (template in 03 §4). Table: researchers(+year, short title) as rows/first column,
  feature columns, `√`/`−` cells, final row `Penelitian Ini`.

## BAB III METODE PENELITIAN — all plans consolidated here

| # | Subsection | Contract |
|---|---|---|
| 3.1 | Alur Penelitian / Tahapan Penelitian | stage-narrative (03 §3), not a bullet dump |
| 3.2 | Studi Literatur | sources + DOI/Crossref verification method |
| 3.3–3.5 | Perancangan … | architecture, hardware, software/dataset; location/participants/ethics where relevant |
| 3.6 | Rencana Pengujian | one block per feature group: plan + metric |
| 3.7 | Evaluasi | success criteria + go/no-go gate decision |
| 3.8 | Rencana Kegiatan dan Jadwal Penelitian | semester schedule table; physical Delta-CSI gate marked |
| 3.9 | Rencana Biaya Penelitian | cost table in Rupiah |
| 3.10 | Analisis Risiko dan Rencana Cadangan | risk + mitigation + fallback per row |

## DAFTAR PUSTAKA

APA 7, alphabetical ascending, hanging indent, DOI URLs. Bidirectional match with
in-text citations (04).

## Mandatory tables (all three required)

1. `Tabel 1.1` proposed titles (in 1.1)
2. `Tabel 2.n` Penelitian Terdahulu comparison (last subsection of BAB II)
3. `Tabel 3.1/3.2/3.3` schedule / cost / risk (in 3.8–3.10)

## Institution profile switch

- Profile **DPJ-UNM** (default): the exact skeleton above; no front matter.
- Profile **BD-2022**: same BAB I–III core; if the deliverable is a full report
  (not proposal) add BD front matter (01); chapter numbering switches to
  `1. Sub Bab / 2.1.1.` style per `05-format-mechanics.md`.

> Done when: outline complete; every planned section has ≥150 words of content plan;
> chapter naming internally consistent.
