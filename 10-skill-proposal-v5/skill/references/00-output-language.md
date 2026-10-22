# 00 — Output-Language Contract (read FIRST, always)

Source of this rule: owner's instruction (token economy). Skill files are written in
English so an agent spends fewer tokens learning them; the **deliverable** is not.

## The contract

1. **All text you produce for the user = Indonesian** (bahasa Indonesia baku, EYD V).
   This covers every sentence of the proposal, every comment to the user, every
   changelog you hand back. Never deliver English prose inside the proposal document.
2. **Skill internals stay English.** Do not translate these files back into your
   replies. Summarize process state in English to yourself (thinking), Indonesian to
   the user (messages).
3. **Indonesian template strings in these reference files are output material.** They
   are quoted verbatim in Indonesian on purpose. Copy them as templates — do NOT
   translate them into English and then back. Placeholders inside `[...]` get the
   research context substituted.
4. **Chat replies to the user: Indonesian.** Worklog entries and commit messages may
   follow repo convention (Indonesian).

## What stays non-Indonesian in the delivered text

| Keep as-is | Examples |
|---|---|
| Established technical terms (Latin script) | *computer vision, real-time, embedded system, channel state information (CSI), ESP32, dataset, deep learning* |
| Product/tool/platform names | RuView, Wi-Fi, IEEE, MATLAB |
| Titles of cited works, DOIs, URLs | https://doi.org/... |
| Code, identifiers, column names | `no_ktp`, `Varchar` |
| Units per style profile | `2×ESP32`, `0,9967` (decimal comma) |

Rule for absorbed loanwords: if the Indonesian equivalent is dominant in Indonesian
scholarship, prefer it (*mikrokontroler*, *panel surya*); if the English term is
idiomatic in the field, keep it (*deep learning*, *stakeholder*). Measure with
`python scripts/openalex.py istilah "padanan" "asing" --bidang ...` (from the
naskah-id skill) when uncertain; see `06-ejaan-naskah-id.md`.

## Foreign-term italics (institution-dependent)

- Bina Darma 2022 guideline **mandates italics** for foreign terms that have not been
  absorbed into Indonesian. Apply when style profile = BD (see `05-format-mechanics.md`).
- The DPJ/TRSE-UNM profile keeps foreign terms unitalicized (previous QA decision:
  consistency beats partial italics until the campus guideline is confirmed).
- Decide once per document; never mix within one file.

## Markers (only these two)

- `[PERLU DATA: what is missing]` — any fact the user did not provide.
- `[PERLU RUJUKAN: claim needing a source]` — any claim without a verified source.
Never invent facts, names, numbers, or references. Legacy marker `【...】` from older
DPJ files is acceptable when the user's document already uses it.

## Sentence-level defaults (deliverable)

- No first person (*saya/kami*); subjects: *penelitian ini*, *sistem*, *alat*, *penelitian terdahulu*.
- Paragraphs 3–8 sentences; every list/table introduced by a sentence.
- No artificial end-of-document markers.
- Reporting verbs for citations: *menjelaskan, menunjukkan, menyoroti, menemukan,
  mengusulkan, mengukur* — never *mengatakan* for everything (see `04-citations.md`).
