# 09 — Workflow: to-tickets Pipeline + Integration Map

The writing job is executed like an engineering change: sliced into tracer-bullet
tickets (to-tickets), each one demoable, with blocking edges. Precedents: issues
#6–#14 (skill build), #15–#21 (4-proposal remake) in github.com/ILoveTahuTek/skripsi.

## 0. Pipeline

```
lock decisions (01)
   │
   ├─ big job? ── /to-tickets ── publish tickets (blockers first, native edges)
   ▼
verified reference set (04)                 [JSON, Crossref/OpenAlex]
   ▼
structure skeleton (02)                     [outline + ≥150 words/section plan]
   ▼
draft per chapter  ─  for each section:  draft (03) → lint (06) → GEPA (08)
   ▼
citation bidirectional check (04) + claim-bound check (07)
   ▼
render DOCX/PDF per style profile (05) + postcheck + visual spot-check
   ▼
deliver: file + placeholder inventory + change notes; worklog + push
```

## 1. to-tickets specifics for proposal writing

- Invoke `/to-tickets` when the job spans more than one context window (a full
  proposal remake, a 4-document batch, a skill build). Single-section fixes go
  straight to execution.
- **Tracer bullets, not layers**: a ticket = one finished, demoable unit
  ("BAB I of DPJ-4 SIBI-only passes evaluator ≥0.8 + periksa clean"), never
  "all of BAB I for all documents" (horizontal slice → rework).
- **Blocking edges are the artifact**: publish blockers first, wire native edges
  (`gh issue create --blocked-by` / REST dependencies API), frontier = tickets with
  zero open blockers. Local fallback: `.scratch/<feature>/issues/<NN>-<slug>.md`.
- **Wide-refactor exception → expand–contract**: renaming a term across all chapters
  (e.g., removing BISINDO from a DPJ) = expand (new form beside old) → migrate
  (per chapter batch) → contract (delete old form).
- **Quiz step before publishing**: check granularity (merge/split), verify each
  acceptance criterion can actually fail before the work starts.
- Tickets are agent-ready by construction — do not re-triage them.

## 2. Integration map (which skill does what)

| Stage | Skill/source | Loaded refs |
|---|---|---|
| Slice work | **to-tickets** (mattpocock `skills/`) | its SKILL.md |
| Draft Indonesian prose | **naskah-id** | 06 load-when map |
| Optimize wording | **gepa-optimize-anything** | 08 |
| Structure/language/format/claims | this skill | 01–07 |

## 3. Quality gates

| Gate | Tool | Threshold |
|---|---|---|
| Structure+language+claims | `scripts/evaluator.py --doc` (D1–D6) | ≥ 0.8, target 1.0 |
| EYD/AI lint | naskah-id `periksa.py` | 0 hard findings; justified soft |
| Facts preserved | `periksa.py --banding` | every reported line explainable |
| References | Crossref/OpenAlex JSON | 0 fictional; ≥10 verified entries |
| DOCX render | docx skill `postcheck.py` | 0 errors; PDF page count sane |
| Skill self-check | `scripts/evaluator.py --skill` | ≥ 0.8 |

## 4. Handover (delivery) format

Indonesian, per naskah-id "Serahkan": the text, a concise before→after change list,
remaining markers, and the placeholder inventory (01). State whether the work was
language-only editing or substance drafting. Append the worklog entry (Task ID) and
push the repo backup.
