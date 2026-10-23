# BAHAN PENYUSUNAN PROPOSAL DPJ-4 — INDEX

**Scope**: DPJ-4 (SIBI-only, Wi-Fi CSI on ESP32, study of feasibility) — materials extracted for writing the proposal from a **human-centered angle**.

**Owner requirement (from user, paraphrased):**
1. The background must open from problems **outside technology** — social cases, education, etc. — not from "technology has developed…".
2. The device must be useful for **people who want to learn SIBI** (hearing learners first).
3. Using the device should help people **understand the perspective faced by deaf people** (empathy / perspective-taking).
4. The device must work as a **fast learning tool** (quick practice-feedback loop).
5. Collect **all** materials needed (bahan, metode, masalah, penyelesaian), written to markdown.

## File map

| File | What it contains | Use it for |
|---|---|---|
| `01-masalah-lapangan.md` | Field problems OUTSIDE technology: demography, family communication, education, healthcare, the SIBI-learning bottleneck, empathy gap | BAB I §1.1 latar belakang (layers 1–3), BAB II §2.4 domain SIBI |
| `02-solusi-konsep-alat.md` | Solution concept: learning-tool framing, 3 personas, learning loop, why Wi-Fi CSI fits, positioning vs existing tools, non-claims | BAB I §1.1 (layer 4) + §1.2–1.5, BAB II §2.3, BAB III §3.3 |
| `03-metode-bahan.md` | Research design materials: stages, Delta-CSI gate, vocabulary selection, data protocol, pipeline, metrics, optional learner-pilot, schedule/budget/risk updates | BAB III (all), §1.4 batasan |
| `04-referensi-bahan.md` | Reference bank: 22 existing verified DOIs + 8 NEW verified DOIs + official/web sources with exact figures; claim→reference mapping | BAB I–III citations, DAFTAR PUSTAKA |
| `05-kit-latar-belakang.md` | Writing kit for the NEW latar belakang: funnel plan, paragraph-by-paragraph template (Indonesian, ready to paste), anti-patterns, title options | BAB I §1.1 rewrite |
| `06-disiplin-klaim-sibi.md` | SIBI-only discipline + BRIN 77.7% BISINDO tension handling + updated claim statement + risk table | BAB I §1.4, BAB III §3.8, defense prep |

## Language policy (per user's standing instruction)

- File bodies are in **English** to save tokens.
- Sentences meant to be **pasted verbatim into the Indonesian proposal** are written in **Indonesian** and marked `ID-READY`.
- When an agent uses this folder to produce the proposal, **all deliverable text must be in Bahasa Indonesia** (following skill proposal-writing v5, ref `00-language-contract`).

## Source-status legend

| Tag | Meaning |
|---|---|
| `VERIFIED-DOI` | Crossref API confirmed; safe to cite immediately |
| `OFFICIAL-WEB` | Government/international-org page; cite as web/report source, quote exact figures |
| `NEEDS-VERIFY` | Useful but figure/page must be double-checked before final citation |

## One-paragraph summary of the new angle

The old DPJ-4 background opened with "Perkembangan teknologi…" and framed the device as a communication aid for deaf people. The **new** framing inverts it: open with the social/educational problem (hearing family members, teachers, and classmates of deaf people struggle and stay dependent; deaf people carry the whole communication burden), show that **learning SIBI is slow and feedback-poor** for hearing learners, then present Wi-Fi CSI on ESP32 as a **camera-free, private, always-available practice partner** that accelerates SIBI learning and builds empathy by making the learner step into the visual-manual world of signing. Technology stays in the last layer of the funnel, as the answer to a field problem.
