# QC checklist — before delivery

Run per chapter, then once across the whole proposal. Everything here is checkable;
anything failing either gets fixed or gets reported in `catatan.md`. Report the results
to the user in Bahasa Indonesia.

## Per chapter

- [ ] All sections the campus template requires exist (BAB I: latar belakang, rumusan
      masalah, tujuan, batasan, manfaat, sistematika; BAB II: teori + penelitian
      terdahulu; BAB III: alat-bahan, perancangan, prosedur pengujian).
- [ ] Rumusan ↔ tujuan mirror 1:1 (same count, same order, same objects).
- [ ] Batasan facts = BAB III facts (dimensions, tools, platforms — identical numbers).
- [ ] No bullet lists inside argumentative prose (lists only for procedures, batasan
      items, rumusan/tujuan items — as the campus template allows).
- [ ] Figure/table numbering `<bab>.<urutan>` sequential; captions above tables,
      below figures; every figure/table referenced from prose by number exactly once
      minimum.
- [ ] Every abbreviation expanded on first use in THAT chapter's first occurrence in
      the full document; term list consistent.
- [ ] No BAB IV language: no `hasil pengujian menunjukkan`, no findings, no `kesimpulan`
      content beyond the sistematika's one-liner.

## Whole document

- [ ] One perspective throughout (impersonal default; no *penulis*/*peneliti* mixing).
- [ ] One citation style throughout (APA `(Nama, Tahun)` or IEEE `[n]`) — including
      daftar pustaka format.
- [ ] Every `[PERLU DATA: …]` and `[PERLU RUJUKAN: …]` listed in `catatan.md` with a
      suggestion of who can supply it (user, pembimbing, lab data).
- [ ] Kata baku sweep: run the Part A static checklist over any sentence written or
      edited in this session (at minimum the critical sentences from the GEPA pass).
- [ ] Numbers: decimal commas, thousand points, units with space, no digits at
      sentence start, quantities inside batasan vs BAB III identical.
- [ ] Claim-strength audit: search for `terbukti`, `sangat`, `signifikan`, `krusial`,
      `inovatif`, `solusi` — each must survive the evidence test or be downgraded/removed.
- [ ] AI-pattern scan (search strings): `Di era`, `Seiring`, `Tidak dapat dipungkiri`,
      `Perlu diingat`, `Mari kita`, `hal ini`, `di mana`, `yang mana`, `memainkan
      peran` — each hit judged; one weak hit is acceptable, clusters are not.
- [ ] Titles and proper nouns spelled exactly as the user wrote them (institution,
      product, supervisor names — never "corrected" from memory).

## Delivery package

```
sempro/<slug>/
├── bab1-pendahuluan.md
├── bab2-kajian-pustaka.md
├── bab3-metodologi.md
├── daftar-pustaka.md        # only verified entries + placeholders
└── catatan.md               # job type per chapter, changes, markers,
                            # GEPA round notes, term list
```

`catatan.md` must state, per chapter: the job performed (koreksi/sunting/tulis ulang/
tulis), the important changes (before → after for the top ones), remaining markers,
and one line on what the user should verify with their pembimbing (e.g. citation
style, sistematika chapter count). This mirrors naskah-id's delivery contract and
keeps the AI-assistance disclosure honest.
