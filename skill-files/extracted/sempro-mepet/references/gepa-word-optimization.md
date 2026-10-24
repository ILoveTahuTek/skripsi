# GEPA word-level optimization — static checklist + revision loop

Two passes adapted from the **GEPA** reflective-evolution pattern
(`gepa-optimize-anything`): a fast static checklist for every sentence, and an
evaluate→mutate→select loop for the sentences that decide the grade. GEPA's mental
model maps onto writing like this:

| GEPA concept | Here |
| --- | --- |
| candidate | a drafted sentence or short paragraph |
| evaluator `(candidate) → (score, feedback)` | the rubric below + written critique |
| reflection / mutation | rewrite 2–3 variants changing ONLY flagged words/phrases |
| Pareto frontier | keep the best variant per dimension; a variant that wins naturalness but breaks correctness is discarded |
| budget (`max_evals`) | max 2 rounds per sentence; loop only on critical sentences |
| saturated signal | a sentence with no flagged items needs no mutation — skip it |

## Part A — Static word-level checklist (every sentence, no loop)

Sweep the draft once, line by line. Each hit is either fixed immediately or, if it is a
meaning question, tagged for the loop.

<gepa-static-checklist>

**Correctness gates (K — a variant failing any of these is disqualified, regardless of score):**
- [ ] Subject exists (no `Dari hasil … menunjukkan`, no `Menurut X mengatakan`)
- [ ] No pleonasm (`adalah merupakan`, `agar supaya`, `sangat … sekali`, `data-data`)
- [ ] No calque connectors (`di mana`/`yang mana` as connectors, `memainkan peran`)
- [ ] Kata baku (analisa→analisis, praktek→praktik, sistim→sistem, …)
- [ ] di- attached to verbs, separated as preposition (`diuji` vs `di dalam`)
- [ ] No corpus-typical typos (`menggunakkan`, `di hadapi`, `di tunjukkan`)
- [ ] Punctuation spaces correct: none before `,` `.`; one after; `(` preceded by space
- [ ] Numbers/units: decimal comma, space before unit, no leading number in sentence

**Formality (register match, 0–10):**
- [ ] No colloquial words (`nungulin`, `bikin`, `ngasih tau`, `kayak`, `banget`)
- [ ] No casual contraction (`gak`, `udah`, `dll` in prose flow where a list belongs)
- [ ] Impersonal perspective maintained; `Penelitian ini` as actor
- [ ] No lecture voice (`Mari kita bahas`, `Perlu diingat`)

**Precision (0–10):**
- [ ] Claim strength matches evidence (`diduga` stays `diduga`)
- [ ] No inflated stacks (`sangat signifikan` without test, triple adjectives)
- [ ] Verb, not nominalization, where the verb is the point (`mengukur` > `melakukan
  pengukuran`)
- [ ] Numbers present where the claim is quantitative

**Naturalness (0–10):**
- [ ] No cosmic opener (`Di era digital ini`, `Seiring perkembangan zaman`)
- [ ] No empty assertive (`Tidak dapat dipungkiri`, `Sudah menjadi rahasia umum`)
- [ ] `hal ini` at most once per chapter; referent named elsewhere
- [ ] Ritual connectors not opening consecutive paragraphs
- [ ] Sentence length ≤ 35 words; lengths vary within the paragraph

</gepa-static-checklist>

## Part B — Revision loop (critical sentences only)

Run on: **each rumusan masalah item, each tujuan item, the closing paragraph of latar
belakang, the synthesis/gap paragraph of penelitian terdahulu, and each BAB II topic
sentence.** These are the sentences an examiner quotes back at you.

<gepa-loop>

1. **Evaluate (baseline).** Score the sentence 0–10 on the four rubric dimensions
   above and write a one-line critique naming the WEAKEST words: e.g. `formality 6:
   "ngasih tau" tidak baku; precision 5: klaim "sangat efektif" tanpa angka`.
2. **Check the failure signal (saturation guard).** If no dimension scores below 8 and
   no checklist item is flagged, skip the sentence entirely — mutation without a
   failure to reflect on is noise. (GEPA gotcha #9: reflection needs the seed's
   failures.)
3. **Mutate.** Write 2–3 variants. Each variant changes ONLY the flagged words and
   phrases — sentence structure moves only when the flagged item is structural
   (subject-missing, >35 words). Different variants may fix different flags.
4. **Score each variant** with the same rubric. Correctness is a gate: any K-fail
   discards the variant regardless of its other scores.
5. **Select on the Pareto rule:** keep the variant with the highest minimum across
   the four dimensions (the weakest-link winner), not the highest average — a 10/10/4/10
   loses to an 8/8/8/8. If two variants are Pareto-equal, keep the shorter one.
6. **Budget: max 2 rounds.** Stop early when no flagged item remains. If round 2
   produces no variant that beats round 1's minimum, keep round 1's text (do not
   thrash).

</gepa-loop>

**Anti-reward-hacking (GEPA gotcha #1 — the optimizer games the score, and so will you):**
the score rewards *fixing flagged issues*, not *adding formal words*. Padding a
sentence with extra baku vocabulary, longer connectors, or hedging stacks to look
"more academic" raises nothing — if a variant is longer than the previous one, it must
buy the extra words with a real fix. The rubric's weakest-link selection is chosen
precisely so that padding one dimension cannot mask a drop in another.

**Reporting (in Indonesian, in `catatan.md`):** for each optimized sentence, note the
final rubric mins and what changed: `rumusan #1: formality 5→9 ("ngasih tau" →
"menyampaikan"), precision 5→8 (ditambah angka target dari data pengguna)`.

## Worked micro-example (English annotation, Indonesian candidates)

Seed (from an informal user draft): `Alat ini ngasih tau pemilik kalo pakan udah
habis.`

- Evaluate: correctness 10, formality 2 (`ngasih tau`, `kalo`, `udah`), precision 6
  (no channel named), naturalness 7. Critique: `kolokial "ngasih tau/kalo/udah"; media
  notifikasi tidak disebut`.
- Mutate:
  - V1: `Alat ini memberikan notifikasi kepada pemilik ketika pakan telah habis.`
  - V2: `Alat ini memberi tahu pemilik apabila pakan habis.` (shorter, but `memberi
    tahu` still casual-adjacent for the corpus register)
  - V3: `Alat ini mengirimkan notifikasi kepada pemilik ketika sisa pakan mencapai
    batas minimum.` — needs the user's actual threshold: `[PERLU DATA: batas minimum
    sisa pakan]` if not given.
- Select: V3 (mins: formality 9, precision 9, correctness 10, naturalness 9) with the
  placeholder, or V1 (8/8/10/8) if the threshold is unknown and must not be invented.
- Round 2 on V1: no flags left → stop.

That is the whole loop: small, gated, word-level, twice at most.
