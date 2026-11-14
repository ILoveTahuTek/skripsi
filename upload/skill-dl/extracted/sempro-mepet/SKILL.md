---
name: sempro-mepet
description: >-
  Write or restyle an Indonesian undergraduate thesis PROPOSAL (seminar-proposal document =
  BAB I Pendahuluan through BAB III Metodologi, plus Daftar Pustaka) in the formal academic
  register of Indonesian university theses. Covers drafting each chapter from a brief,
  converting informal notes into baku academic prose, fixing citation language, running
  word-level GEPA optimization, and QC before submission. All generated prose is delivered
  in Bahasa Indonesia; use when the user mentions sempro, proposal skripsi/TA, BAB 1-3,
  sidang/seminar proposal preparation, latar belakang, rumusan masalah, kajian pustaka, or
  asks to "make my proposal sound like a real skripsi".
---

# Sempro-Mepet

Draft an Indonesian thesis proposal — **BAB I (Pendahuluan) through BAB III (Metodologi)** —
whose *language* reads like the accepted theses of an Indonesian university: formal, baku
(EYD V / KBBI), impersonal, procedurally passive, and free of machine-translation and
AI-typical patterns. The register targeted here was measured from a corpus of accepted
applied-engineering theses, but the style rules are **discipline-generic**: substitute the
domain vocabulary, keep the sentence mechanics.

**Language contract (non-negotiable):** these instruction files are English for token
economy, but EVERYTHING you deliver to the user — proposal prose, chapter files, change
notes, chat replies while this skill is active — is in **Bahasa Indonesia**.

A proposal is complete when a reader can answer: *what problem, why it matters, what
others did, what you will build/do, how, and with what tools*. It contains no results,
no findings, no conclusions beyond BAB III.

<scope-rules>

- Scope = BAB I, BAB II, BAB III (+ Daftar Pustaka, optional front-matter list). If the
  user asks for BAB IV/hasil, that is outside this skill: say so and stop at BAB III.
- Never invent: numbers, measurements, prior research, references, tools the user did not
  mention. Missing facts become `[PERLU DATA: …]`; unverified references become
  `[PERLU RUJUKAN: …]`. These two markers only — no variants.
- The style being copied is *how the corpus writes*, never *what it says*: never reuse a
  sentence's content from a sample thesis; reuse only its sentence mechanics.
- One consistent perspective per document: prefer impersonal ("Penelitian ini…") unless
  the campus guide says otherwise. Never mix *penulis*, *peneliti*, and impersonal.

</scope-rules>

## Process

### 1. Gather the brief (ask once, in Indonesian)

Ask only what is missing, then stop asking:

- judul (atau draf judul), program studi, and target style if known (campus writing guide?)
- what already exists: topic notes, data, references, a rough draft, or nothing
- citation style of the program (APA (Nama, Tahun) or IEEE [1]); never guess it
- deadline/urgency — with "mepet" users, offer the fastest complete path first

### 2. Classify the job (batas perubahan)

Pick the narrowest interpretation of the request, and tell the user which job you are doing:

| Job | User says | You may change |
| --- | --- | --- |
| **Koreksi** | "cek ejaan saja" | spelling, punctuation, kata baku, capitals, numbers/units only |
| **Sunting** | "rapikan bahasanya" | + sentence structure, connectors, pleonasm, AI patterns |
| **Tulis ulang** | "tulis ulang paragraf ini" | + paragraph order and idea flow |
| **Tulis** | "buatkan BAB 1" | compose new text from the user's material only |

### 3. Draft chapter by chapter (vertical slices)

Draft in **proposal order** and deliver each chapter as its own file so the user can review
while you continue. Load the matching reference file per section as you work — do not load
everything up front:

| Writing this… | Load |
| --- | --- |
| Any sentence, first (always) | `references/language-core.md` |
| BAB I sub-sections (latar belakang → sistematika) | `references/bab1-pendahuluan.md` |
| BAB II (kajian pustaka, penelitian terdahulu) | `references/bab2-kajian-pustaka.md` |
| BAB III (metodologi, alat-bahan, prosedur) | `references/bab3-metodologi.md` |
| Word-level polish on critical sentences | `references/gepa-word-optimization.md` |
| Before delivery | `references/qc-checklist.md` + `references/examples-parallel.md` |

<chapter-rules>

- Each chapter is a complete vertical slice: a reader can review it standalone.
- First draft of each section is written at corpus register from the start
  (see `language-core.md`), then optimized — do not write sloppy-then-fix-everything-later.
- Keep terminology consistent across chapters: build a term list (Indonesian + italic
  foreign term + abbreviation) as you draft BAB I and reuse it; ask the user when two
  terms compete for one concept.
- Match user-supplied facts exactly: dimensions, tool names, method names, institution
  names are copied verbatim into the draft, never paraphrased into "better" ones.

</chapter-rules>

### 4. GEPA word-level optimization (critical sections)

Run the loop from `references/gepa-word-optimization.md` on the sentences that decide the
grade: **rumusan masalah, tujuan penelitian, the closing paragraph of latar belakang, and
each topic sentence of BAB II theory blocks**. Routine sentences get the static checklist
only. Never optimize a sentence into meaninglessness: correctness gates everything.

### 5. Quiz the user (before final delivery)

Present a compact per-chapter summary: what was written, which facts are placeholders
(`[PERLU DATA: …]` / `[PERLU RUJUKAN: …]`), term list decisions, and 2–3 alternative
phrasings for the rumusan masalah if any were generated. Ask:

- Apakah granularitas tiap subbab sudah pas?
- Apakah penanda `[PERLU DATA]`/`[PERLU RUJUKAN]` mau diisi sekarang atau dibiarkan?
- Apakah ada istilah yang harus diganti?

Iterate until approved. Do not silently fill placeholders with guesses.

### 6. Deliver

Write one markdown file per chapter to the user's chosen folder (default
`./sempro/<slug>/`), using the section-file template below. Deliver in Indonesian:

- `bab1-pendahuluan.md`, `bab2-kajian-pustaka.md`, `bab3-metodologi.md`, `daftar-pustaka.md`
- a `catatan.md` change-log: job type per chapter, important changes, remaining markers

<section-file-template>

# BAB I PENDAHULUAN

## 1.1 Latar Belakang
<prose — paragraphs only, no bullet lists in body text>

## 1.2 Rumusan Masalah
Berdasarkan latar belakang yang telah dipaparkan, maka masalah yang dikaji
dalam penelitian ini dapat dirumuskan sebagai berikut:
1. Bagaimana … ?
2. Bagaimana … ?

## 1.3 Tujuan Penelitian
Berdasarkan rumusan masalah tersebut, tujuan penelitian ini adalah:
1. <verb-first item mirroring item 1 above>
2. <…>

## 1.4 Batasan Masalah
Batasan masalah pada penelitian ini yaitu:
1. <concrete scope fence — object, dimensions, platform, method>

## 1.5 Manfaat Penelitian
<teoretis + praktis, per beneficiary>

## 1.6 Sistematika Penulisan
<BAB I…BAB V one line each>

</section-file-template>

Avoid embedding volatile details (page numbers, exact figure/table counts) in the
delivery notes; they go stale after the user edits in Word.

## Honesty contract (from naskah-id, binding)

1. Numbers, results, quotes, and data come only from the user; otherwise write
   `[PERLU DATA: …]`.
2. Only traceable references enter the text; otherwise write `[PERLU RUJUKAN: …]`.
   Never assemble a bibliography from memory.
3. When editing, never alter numbers, results, names, or citations.
4. Never exceed the requested job scope (see step 2).
5. Claim strength must match evidence: *diduga* never becomes *terbukti*;
   *signifikan* only with a statistical test attached.
6. This skill helps with language and structure — it does not fabricate research,
   and it is not a plagiarism-detection-evasion tool. If asked to disguise AI text,
   offer legitimate help instead (structure guidance, editing the user's own text).
