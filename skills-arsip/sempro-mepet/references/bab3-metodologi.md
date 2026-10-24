# BAB III — Metodologi Penelitian

BAB III tells the examiner the research is *executable as written*. It is the most
formulaic chapter and the most passive: procedures are written with *di-* passive or
me- prefixed steps, components are named exactly, and everything is referenced to a
numbered figure or table. Chapter name varies (Metodologi Penelitian, Metode Penelitian,
Perancangan dan Implementasi) — follow the campus guide.

## Chapter skeleton (engineering/applied default)

1. **Gambaran umum / diagram alur penelitian** — 1 paragraph + flowchart:
   `Tahapan penelitian secara umum ditunjukkan pada Gambar 3.1.` then walk the flow:
   `Penelitian dimulai dari [tahap awal] kemudian [tahap] … hingga [tahap akhir].`
2. **Metode pengumpulan data / kebutuhan sistem** — `Teknik pengumpulan data pada
   penelitian ini dilakukan dengan studi literatur, observasi, dan [wawancara/kuesioner
   bila ada].` Order by weight, name each source of data.
3. **Alat dan bahan** — table: `Tabel 3.1 Alat` / `Tabel 3.2 Bahan`, columns
   `No. | Nama | Spesifikasi | Jumlah | Keterangan`. Intro sentence:
   `Pada proses perancangan [sistem] membutuhkan alat dan bahan sebagai berikut:`
4. **Perancangan** (per subsystem, 3.x.2 …) — design diagram + walkthrough:
   - Diagram reference: `Desain rangkaian ditunjukkan pada Gambar 3.x.`
   - Walkthrough: `Pada skema tersebut, [komponen A] terhubung dengan [komponen B]
     melalui [jalur], [fungsi].` — one sentence per interconnection, in signal/data
     flow order.
   - Software design if any: `Perancangan perangkat lunak menggunakan [metode/bahasa],
     dengan alur …`
5. **Prosedur pengujian** — numbered imperative steps + what is measured:
   `Pengujian dilakukan untuk mengetahui [parameter] dengan [metrik].`
6. **Jadwal penelitian** (if the template requires): table of stages vs months.

## The procedural register (distinct from BAB I/II)

Procedures use **me- prefixed imperative steps** (instructions) or **di- passive**
(descriptions of what happens). Corpus pattern for a testing procedure:

```
Adapun prosedur pengujian [komponen] adalah sebagai berikut.
1. Menyiapkan peralatan yang digunakan.
2. Merangkai [komponen] sesuai dengan Gambar 3.x.
3. Menghubungkan [perangkat] dengan [host/perangkat lain].
4. Membuat program pada [IDE] sesuai kebutuhan.
5. Mengunggah program tersebut.
6. Menjalankan program.
7. Mengamati, mencatat, dan menganalisis hasil pengujian [parameter].
```

Note the register details: `Menyiapkan/Merangkai/Menghubungkan` (me- form, not
bare imperative `Siapkan` — some campuses use the bare form; the me- form is the safer
corpus default), the final triple `mengamati, mencatat, dan menganalisis`, and the
figure reference inside step 2. If the campus guide shows bare imperatives
(`Siapkan peralatan…`), mirror that instead — consistency with the guide beats
corpus default.

## Figure and table referencing (memorize these three shapes)

- `… ditunjukkan pada Gambar 3.x.` / `… ditunjukkan pada Tabel 3.x.`
- `Gambar 3.x menunjukkan [isi].` / `Tabel 3.x menyajikan [isi].`
- `… dapat dilihat pada Gambar 3.x.` / `… seperti pada Tabel 3.x.`

Caption placement: table title ABOVE the table (`Tabel 3.1 Alat dan bahan pengujian`),
figure title BELOW the figure (`Gambar 3.2 Rangkaian sensor`). Numbering =
`<bab>.<urutan>` (restart per chapter). Never reference a figure as "gambar di bawah
ini" — always by number.

## Walkthrough sentence pattern (for design diagrams)

For each interconnection, one sentence in this skeleton:

`[Komponen A] terhubung dengan [komponen B] melalui [medium/port], yang berfungsi
untuk [fungsi data/sinyal].`

Then the power/energy note if relevant: `Rangkaian dijalankan menggunakan [sumber
daya] dengan [tegangan], dan [konversi tegangan bila ada] agar [kebutuhan komponen].`

## Method-selection paragraphs (when a method is chosen)

Three sentences, in this order:

1. Name + citation: `Metode [X] merupakan [definisi ringkas] ([Nama], [tahun]).`
2. Why it fits: `Metode ini dipilih karena [alasan yang dikaitkan dengan karakteristik
   masalah/batasan].`
3. What it does here: `Dalam penelitian ini, metode [X] diterapkan untuk [fungsi]
   pada [bagian sistem].`

Common development methods named in the corpus (pick ONE and keep it): *waterfall,
prototyping, iterative, agile/scrum, RAD* — the choice must appear again in the
perancangan steps.

## Rules

- No results. "Hasil pengujian menunjukkan…" is BAB IV language — forbidden here.
  The procedure ends at `menganalisis hasil pengujian`, not at the findings.
- Every tool named exactly as used (user's fact, verbatim): `NodeMCU ESP8266`,
  `Arduino IDE`, `sensor ultrasonik HC-SR04` — brand/case preserved, in the term list.
- Every physical quantity with unit and space (`12 V`, `25 °C`, `60 cm × 40 cm × 30 cm`).
- Sample/prototype dimensions go in both batasan (BAB I) and alat-bahan/perancangan
  here — identical numbers, no drift.
- If a step needs data the user has not provided (exact components, tools, quantities),
  stop and ask once, or write `[PERLU DATA: …]` — never invent a plausible component
  list; the examiner checks prices and datasheets.
