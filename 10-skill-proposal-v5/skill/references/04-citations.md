# 04 — Citations: In-Text Rules, Reference List, Verification

Sources: BD-2022 §3.4.3–3.4.6 (in-text citation mechanics), TRSE corpus convention,
naskah-id `sitasi.md` + `alat-riset.md`. Default style: **APA 7 (author–year)**.
BD allows APA or Harvard — APA 7 unless the user says otherwise.

## 1. In-text: two correct forms

**Signal phrase** (author is part of the sentence):
> Luthfi (2004) berargumentasi bahwa …
> Sistem yang dikembangkan oleh Alman & Syakti (2005) mengungkapkan …
> Di sisi lain, Iskandar dkk (1999) melaporkan …

**Parenthetical** (author not part of the sentence):
> Penelitian (Luthfie, 2004) menemukan kenyataan …
> Telah terbukti bahwa AI sangat efektif (Febriansyah et al, 2000) dalam …

**Forbidden** (identity must fuse with the sentence — BD's explicit warning):
> ✗ Penelitian oleh (Oemar, 2004) menemukan …
> ✗ Menurut (Syamsuar, 2004) bahwa …
> ✓ Penelitian oleh Oemar (2004) menemukan …
> ✓ Menurut Syamsuar (2004) …

Corpus reporting verbs: *menjelaskan, menunjukkan, menyoroti*; extend with *menemukan,
mengusulkan, mengukur, melaporkan, membantah, memperluas* as fit — never *mengatakan*
for every source (naskah-id).

## 2. Edge cases (BD rules, keep exactly)

| Case | Form |
|---|---|
| Multiple sources in one bracket | separated by `;` → `(Jogianto, 1995, 2004; Fathoni & Febriansyah, 2003; Syamsuar, 2003, 2005)` |
| Same author, several years | `(Jogianto, 1995, 1997, 2004)` |
| Two authors | `&` in parentheses, `dan/&` in signal phrases per house style |
| 3+ authors | one name + `dkk` (or `et al.` — pick one, consistent per document) |
| Ambiguous same author+year | suffix letters `(Jones, 1983a, 1983b)` |
| Page needed (direct quote) | `(Zuhri, 2003, h. 30-35)` / `(Wijaya, 1980, h. 12)` |
| Quote ≥40 words | signal phrase ending with `:` + block quote indented ±1,25 cm + `(h. N)` at the end |
| Secondary source | `Martin dan Odell (1999, dalam Hariyanto, 2004) mengemukakan …` — the reference list contains ONLY the source actually read (Hariyanto) |

## 3. Reference list (APA 7)

> Nama, A., & Nama, B. (Tahun). Judul artikel. *Venue*, vol(issue), halaman. https://doi.org/…

- Alphabetical ascending A–Z, hanging indent 1,25 cm (BD profile: hanging 1,25 cm).
- Every in-text citation appears in the list **and vice versa** (bidirectional match —
  D3 rule; automated count lives in `scripts/evaluator.py`).
- DOI as `https://doi.org/...` URL, never bare `doi:` prefix.

## 4. Verification pipeline (non-negotiable — no fabricated references)

1. Prefer literature with a DOI. Verify each via Crossref:
   `curl -s https://api.crossref.org/works/<DOI>` — check title/authors/year/venue
   against the claimed entry.
2. Or OpenAlex via the naskah-id tool:
   `python .../naskah-id/scripts/openalex.py cek "judul" --penulis "..." --tahun ...`
   and `rujukan <DOI> --gaya apa` for a paste-ready entry.
3. Save the verified set as JSON in the working repo (precedent:
   `04-referensi-slb/verified_refs.json`, `06-referensi-isyarat/verified_refs.json`).
4. Unverifiable source → do NOT cite it; write `[PERLU RUJUKAN: claim]` instead.
   Web-only (no DOI) entries need a second web check (venue+year+authors) and get
   status `verified-web-only`.
5. Minimum 10 verified references per proposal (D6/QA gate).

**Done when:** JSON of verified refs saved; zero fictional entries; bidirectional
match passes.
