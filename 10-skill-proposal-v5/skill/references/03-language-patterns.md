# 03 — Corpus Language Patterns (the "how it is written" layer)

Purpose: copy the **language**, never the content. All Indonesian strings below are
literal templates from the TRSE-UNM corpus (and previous QA-passed DPJs). Substitute
`[...]` with the research context. BD-2022's own language principle matches:
scientific Indonesian = *singkat, tepat, tidak multi tafsir*; EYD; no ambiguity.

## 1. Latar Belakang funnel — 4 layers, ±6–10 paragraphs

1. **General context** — field condition, one paragraph:
   > Perkembangan teknologi telah memengaruhi berbagai aktivitas [target], termasuk [domain]. Saat ini, [keadaan terkini].
2. **Specific problem** — current practice + its weakness:
   > Pada [sistem] konvensional, [praktik umum]. Kondisi tersebut menunjukkan bahwa [kelemahan], karena [penyebab].
3. **Enabling technology** — one paragraph per technology, each with a citation:
   > [Teknologi] merupakan [definisi]. Nama (Tahun) menjelaskan bahwa [klaim literatur]. Pada penelitian ini, [teknologi] digunakan untuk [fungsi].
4. **Funnel close**:
   > Berdasarkan uraian tersebut, penelitian ini dilakukan untuk [tujuan besar]. Sistem yang dikembangkan mengintegrasikan [komponen]. Pengembangan ini diharapkan dapat [dampak].

Anti-pattern (naskah-id pola-ai): never open with `Di era digital ini`,
`Seiring perkembangan zaman`, `Tidak dapat dipungkuri bahwa` — start from the
concrete problem. Layer 1 opens with the field, not with the universe.

## 2. Subsection openers of BAB I (verbatim corpus openers)

**Rumusan Masalah:**
> Berdasarkan latar belakang permasalahan yang telah diuraikan serta untuk menjawab permasalahan yang menjadi fokus dalam penelitian ini, maka dapat dirumuskan beberapa rumusan masalah yang akan dikaji lebih lanjut. Rumusan masalah pada penelitian ini sebagai berikut.

Then numbered questions: `1. Bagaimana [aspek perancangan] …?`

**Tujuan Penelitian:**
> Penelitian ini bertujuan untuk [tujuan umum]. Adapun tujuan dari penelitian ini adalah sebagai berikut.

Then numbered action-verb items mirroring 1.2 one-to-one:
`Merancang … / Mengimplementasikan … / Mengetahui hasil pengujian …`

**Batasan Masalah:**
> Agar penelitian ini memiliki ruang lingkup yang jelas dan terarah sesuai dengan tujuan yang telah ditetapkan, maka ditentukan batasan masalah guna membatasi pembahasan terhadap aspek-aspek yang relevan dengan topik penelitian. Adapun batasan masalah pada penelitian ini sebagai berikut.

Numbered items; **last item** always: `Penelitian ini tidak membahas [di luar lingkup].`
Then the claim-discipline paragraph (07 §3).

**Manfaat Penelitian:** short intro paragraph, then
`1.5.1 Manfaat Teoretis`:
> Penelitian ini diharapkan dapat menjadi referensi dalam pengembangan [bidang]. Selain itu, penelitian ini juga dapat menjadi acuan penerapan [teknologi-teknologi].

`1.5.2 Manfaat Praktis`: numbered `1. Bagi Peneliti … 2. Bagi [Pengembang/Guru/Peternak] … 3. Bagi Pengguna … 4. Bagi Praktisi Teknologi …`

## 3. Title pattern (BAB I opening block, ALL CAPS)

`RANCANG BANGUN | IMPLEMENTASI | PERANCANGAN | SISTEM … BERBASIS … PADA/UNTUK … : STUDI KELAYAKAN …`

## 4. Methodology stage-narrative (BAB III opener)

> Penelitian dalam [tugas akhir/proposal] ini dilaksanakan melalui beberapa tahapan yang tersusun secara sistematis sehingga membentuk suatu alur penelitian yang terstruktur. Tahap pertama adalah studi literatur, yaitu [uraian]. Tahap kedua adalah perancangan sistem, yang mencakup [uraian]. Tahap ketiga adalah implementasi … Tahap terakhir adalah pengujian dan evaluasi. Apabila dalam proses pengujian ditemukan kendala …, maka dilakukan evaluasi dan perbaikan secara berulang hingga sistem dapat bekerja secara optimal.

## 5. Gap statement (after the Penelitian Terdahulu table)

> Berdasarkan tabel perbandingan di atas, terlihat bahwa penelitian-penelitian sebelumnya [pola umum]. Belum banyak penelitian yang secara spesifik [celah], terdapat juga beberapa celah masalah (gap) yang belum terselesaikan secara simultan oleh peneliti sebelumnya. Penelitian ini mengisi celah tersebut dengan [langkah]: 1. … 2. … 3. …

Novelty claims are always **combinational** ("first on [language] via [platform] in
[context]"), never "first to discover X in general" (see 07 §5).

## 6. Discussion subsections (BAB II body)

Per-technology paragraph skeleton (BD: discuss, don't just define):
> [Teknologi] merupakan [definisi]. Nama (Tahun) menjelaskan bahwa [temuan/klaim]. Dalam konteks [penelitian ini/kasus], [mengapa konsep ini dipakai]. [Implikasi desain].

## 7. Abstract (only when requested — 01)

One paragraph ≤200 words: context & criticality → current state + weakness → technical
challenge → `Penelitian ini bertujuan untuk …` → method sketch → implication. Close
with `Kata Kunci: 3–5 frasa`.

## 8. Done-when

- Every BAB I subsection uses its corpus opener; every funnel layer present.
- No paragraph <3 sentences; no uncontextualized bullet list.
- Question items (1.2) ↔ goal items (1.3) mirror one-to-one.
