# 08 — GEPA Loop: Word-by-Word Optimization of the Draft

Source: `gepa-optimize-anything` skill (owner-provided archive) + the real run
precedent (Task 4: seed 0.7196 → curated v3 at 1.0; reward-hacking lesson captured).

## 0. When to run

After structural drafting (03) and the manual language sweep (06 §5) — GEPA is the
last, most expensive pass. Run it on **one section at a time** (candidate = section
text), BAB I first (highest language-rule density), then BAB II/III + abstract.

Without the package (token-constrained sessions): run the manual reflective sweep —
score the section against the rubric D1–D6 + lint findings, rewrite the worst-scoring
rules, repeat ≤3 rounds. That is "GEPA by hand" and is acceptable.

## 1. Contract (what GEPA needs)

```python
from gepa.optimize_anything import optimize_anything, OptimizeAnythingConfig

def evaluate(section_text: str, example) -> tuple[float, dict]:
    # score = weighted rubric compliance of THIS section, 0..1
    d = rubric_scores(section_text)            # reuse scripts/evaluator.py logic
    lint = periksa_findings(section_text)      # naskah-id periksa.py, K/AI findings
    score = 0.7 * d["dimension_score"] - 0.03 * lint["hard_count"] - 0.01 * lint["soft_count"]
    if not sanity(section_text):               # anti reward-hacking gates:
        score = 0.0                            #   min length, no term-dump, facts preserved
    return score, {
        "score": score,
        "failed_rules": d["failed_rules"],     # concrete rule IDs -> actionable feedback
        "lint_lines": lint["lines"],           # periksa.py report lines
        "note": "keep Indonesian; preserve numbers/citations/claim bounds",
    }

result = optimize_anything(
    seed_candidate=example["section"],
    evaluator=evaluate,
    objective="Maximize rubric+language compliance of this Indonesian proposal section.",
    background="Proposal = BAB I-III. Output-language contract: Indonesian text; EYD V; no fabricated facts.",
    config=OptimizeAnythingConfig(
        engine="gepa", name=f"polish_{example['section_id']}",
        max_evals=30,                    # single-task: 15-20 proposals floor
        stop_at_score=1.0,               # hard ceiling -> stop early
        run_dir="runs/polish", output_dir="outputs/polish",
        engine_config={"reflection": {"reflection_lm": REFLECTION_LM}},
    ),
)
```

## 2. Hard-won rules (from the real run — do not re-learn these)

- **Reward hacking is the default failure.** The Task-4 evaluator initially accepted a
  term-dump (stuffing every rubric keyword into a paragraph). Fix: score gates —
  sanity() must check (a) min/max word count, (b) facts/numbers/citations unchanged vs
  seed, (c) no `Bagaimana|Merancang|Delta-CSI|go/no-go`-style keyword stuffing measured
  as term-frequency vs seed ratio, (d) claim-bound sentences intact.
- **Metrics bug ≠ content bug.** In Task 5 all documents scored 0.585 because the
  skill-dir evaluator had an old regex (escaped alternation `|` killed every
  multi-term rule). Sync `scripts/evaluator.py` from `scripts/` before scoring anything.
- **reflection_lm**: `openai/gpt-5.1` default needs a key; in this environment pass a
  **callable** implementing GEPA's LM protocol (precedent: z-ai chat completion,
  glm-4-plus, Task 4). Validate with a 1-call test before a long run.
- **Budget**: single-task mode ⇒ `max_evals ≥ 15–20`; always set `stop_at_score=1.0`;
  wall-clock `timeout 1200 python run.py` backstop.
- Keep the accepted-candidate lineage (`run_dir/`) and record seed→final scores in the
  worklog; curate any candidate that improved score by degrading readability.

## 3. What "word-by-word" means here

GEPA mutates the section text toward the evaluator; the evaluator encodes the corpus
language rules (03), EYD mechanics (05/06), citation rules (04), claim bounds (07).
So the optimizer's "word-by-word optimization" = iterative reflection on concrete
failed rules + lint lines, not free-style rewriting. Facts, numbers, citations and
placeholder markers must survive every mutation (checked in sanity()).

## 4. Post-loop

Diff seed vs best (word-level), run `periksa.py --banding` once more, then hand the
user a before→after change list (naskah-id handover format). Log scores in worklog.
