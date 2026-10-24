# 06 — Language Polish Bridge: naskah-id Integration

The heavy EYD-V / kata-baku / anti-AI-pattern rules live in the **naskah-id** skill
(github.com/nothinx/naskah-id). This skill does NOT duplicate them — it wires them in
at the right workflow points (09) and carries the recurring fixes discovered while
editing the four DPJ proposals (Task 7, ~62 rule pairs).

## 1. What naskah-id enforces (summary of its contract)

1. Numbers, results, quotes, data only from the user → else `[PERLU DATA: …]`.
2. Only traceable references → else `[PERLU RUJUKAN: …]`; never assemble a reference
   list from memory.
3. When editing: numbers, results, names, citations unchanged to the letter.
4. Changes never exceed the requested work level: **koreksi < sunting < tulis ulang < tulis**.
5. No plagiarism laundering, no AI-detector evasion.

Its three tag levels: **K** (EYD-V/KBBI violation — always fix), **G** (style — fix on
sunting+), **AI** (machine cliché — fix on sunting+; a single occurrence is tolerable).

## 2. Load-when map (from naskah-id, load only on demand)

| Problem in draft | File |
|---|---|
| AI patterns / English-calque prose | `references/pola-ai.md` |
| Missing subject, pleonasm, nominalization, fake connectors | `references/kalimat-efektif.md` |
| Spelling, prepositions, word joins, numbers, units, punctuation | `references/ejaan-eyd-v.md` |
| Non-standard words | `references/kata-baku.md` |
| Foreign term: translate / absorb / keep | `references/istilah.md` |
| Abbreviations, acronyms, institution names | `references/singkatan.md` |
| Citation & reference formatting | `references/sitasi.md` |
| What looks like an error but is legitimate convention | `references/pertahankan.md` |
| Section-specific conventions (abstract, intro, method…) | `references/bagian-naskah.md` |

Strongest AI tells (fix first, from naskah-id SKILL.md): cosmic openers; preposition-
swallowed subjects (`Dari hasil pengujian menunjukkan…`); English-fake connectors
(`di mana`/`yang mana` as connectors, `memainkan peran`, `mengambil tempat`); ritual
`Hal ini`/`Selain itu`/`Oleh karena itu` at every paragraph head; inflated claims
(`sangat signifikan`, `solusi inovatif`, triple-adjective stacking).

## 3. Lint commands (run per section, per chapter — not once at the end)

```bash
# fact-preservation diff (numbers/citations/quotes unchanged)
python .../naskah-id/scripts/periksa.py --banding asli.md draf.md
# K/AI pattern sweep
python .../naskah-id/scripts/periksa.py draf.md
```

Long-manuscript rule (>≈3,000 words): work per bab; build a term+viewpoint list
(*filter Kalman*, *responden*, impersonal) before the first chapter and hold it
constant; run `--banding` per bab.

## 4. Recurring fixes observed in the DPJ corpus (quick table)

| Before → After | Class |
|---|---|
| `et al.` in Indonesian prose → `dkk` (keep `et al.` inside reference entries) | G |
| `di mana` as connector → restructure with `yang`/`tempat`/`saat` | AI |
| `, sehingga` splice on >35-word sentences → split sentence | G |
| `kontinyu` → `berkelanjutan`/`terus-menerus` | K |
| `mempengaruhi` → `memengaruhi` | K |
| `multi-` compounds: `multi-person` → `lintas-person`/`antar-orang` per context | G |
| `antar-sesi` → `antarsesi`; `lintas-person` stays hyphenated (phrase) | K |
| `entropy` → `entropi`; `threshold` → `ambang`; `milidetik` → `ms` (consistency) | G |
| English calques: `contact-less` → `bebas-kontak`; `update` → `ter-update` forms per naskah-id | G |
| `Mengetahui hasil pengujian` as a goal verb → `Menguji` (action, not passive knowing) | G |
| Verbal nouns: `melakukan pengukuran` → `mengukur` | G |

Full pair list with rationale: repo `08-markdown-dpj/CATATAN-PERUBAHAN.md` +
`scripts/fix_bahasa_dpj.py` (62 pairs).

## 5. When polishing (order)

1. Structural pass (patterns 03) → 2. K-level sweep (periksa.py) → 3. G/AI sweep
(naskah-id references) → 4. fact-check `--banding` → 5. GEPA loop (08) for
word-by-word scoring-driven refinement.
