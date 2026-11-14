# Language core — the corpus register, inlined from naskah-id

Read this before writing any sentence. It defines HOW the target theses sound:
sentence mechanics, punctuation, word choice, and what never to write. All prose rules
are from **naskah-id** (EYD V, KBBI, *Tata Bahasa Baku*), inlined here so no external
dependency is needed. Example sentences are Indonesian; explanations are English.

## 1. Corpus register profile (measured)

Target voice, measured across 87 accepted proposal documents (~157k words):

| Property | Target | Notes |
| --- | --- | --- |
| Sentence length | mean ≈ 18–21 words, median ≈ 18, IQR ≈ 12–26 | >35 words: split. Vary length — short sentence for the key claim. |
| Paragraph | one governing idea, topic sentence first | 3–6 sentences typical for BAB I; procedure steps stay as numbered lists |
| Voice | impersonal: "Penelitian ini…" as subject | passive *di-* for procedures and design description; active only for findings/definitions |
| Perspective | impersonal throughout | never mix *penulis* + *peneliti* + impersonal in one document |
| Definitions | "X merupakan Y" / "X adalah Y" | *merupakan* before noun phrase, *adalah* before noun/adj/number — never both |
| Openers | vary: "Oleh karena itu,", "Dalam penelitian ini,", "Berdasarkan…", "Selanjutnya," | no more than one identical paragraph opener in a row |
| Punctuation | space BEFORE `(`? No: ` seperti ini (bukan begini)`. Never a space before `,` `.` `;` `:` | corpus often violates this — you must not |

Dominant connectors (use these, not their calques): **sehingga** (no comma before it),
**yaitu / yakni**, **adapun** (to introduce a list), **selain itu**, **selanjutnya**,
**oleh karena itu** (comma after), **namun** (comma before), **sedangkan** (comma before),
**berdasarkan**, **dengan adanya**, **sehubungan dengan**.

Reporting verbs for citations — pick the accurate one, not *mengatakan* everywhere:
*menyatakan, menjelaskan, mengukur, menemukan, mengusulkan, membandingkan, memperluas,
mengembangkan, menekankan, menyarankan, membantah*.

## 2. Marking levels (internal use)

When checking your own draft, tag issues at three levels — fix **K** always, **G** and
**AI** on any job wider than *Koreksi*:

- **K (kaidah)** — violates EYD V, KBBI, or grammar. Always fixed.
- **G (gaya)** — style recommendation. Fixed on sunting/tulis ulang.
- **AI (klise mesin)** — machine-translation/AI-typical pattern. Fixed on sunting/tulis
  ulang; a single occurrence is usually fine.

## 3. Sentence mechanics (KE rules)

### 3.1 Subject must exist

- ❌ `Dari hasil analisis menunjukkan bahwa …` → ✅ `Hasil analisis menunjukkan bahwa …`
- ❌ `Dalam penelitian ini membahas …` → ✅ `Penelitian ini membahas …` / `Dalam penelitian ini dibahas …`
- ❌ `Menurut Santoso mengatakan bahwa …` → ✅ `Menurut Santoso, …` / `Santoso mengatakan bahwa …`
- ❌ `Pada Gambar 3 memperlihatkan …` → ✅ `Gambar 3 memperlihatkan …`
- ❌ `Untuk mengukur suhu menggunakan sensor DHT22.` → ✅ `Suhu diukur dengan sensor DHT22.`

### 3.2 Connector table (memorize)

| Wrong / kaku | Baku | Level |
| --- | --- | --- |
| `berdasarkan pada hasil` | berdasarkan hasil | K |
| `antara A dengan B` | antara A dan B | K |
| `baik A ataupun B`, `baik A dan B` | baik A maupun B | K |
| `bukan A, tetapi B` (as correction) | bukan A, melainkan B; tidak A, tetapi B | K |
| `Meskipun …, tetapi …` | Meskipun …, (drop *tetapi*) | K |
| `Karena …, maka …` (double) | drop *maka* after *karena* | K |
| `Sehingga …` / `Sedangkan …` starting a sentence | join to previous sentence, or use `Akibatnya,` / `Adapun` | K |
| `lebih baik dari` | lebih baik daripada | K |
| `Dikarenakan …` | Karena … | G |
| `Namun demikian,` | Namun, / Meskipun demikian, | G |
| `dalam rangka meningkatkan` | untuk meningkatkan | G |
| koma before `sehingga` | no comma before *sehingga* (intrakalimat) | K |
| `terdiri dari` | terdiri atas (anjuran) — but *terdiri dari* is not an error | G |

Comma rules that matter: comma **after** sentence-initial connectors (*Oleh karena itu, …*),
**before** adversatives (*…, tetapi …; …, sedangkan …*), **after** a fronted subordinate
clause (*Karena sampel rusak, pengukuran diulang.*), **none** when the subordinate clause
follows (*Pengukuran diulang karena sampel rusak.*).

### 3.3 Nominalization — use the verb

| Kaku | Ringkas |
| --- | --- |
| `melakukan analisis terhadap data` | menganalisis data |
| `melakukan pengukuran` | mengukur |
| `melakukan perbandingan antara` | membandingkan |
| `mengalami peningkatan` | meningkat |
| `memberikan pengaruh terhadap` | memengaruhi |
| `Penelitian ini bertujuan untuk mengetahui` | Penelitian ini bertujuan mengukur / menguji / membandingkan |

Keep the noun only when it IS the topic: "Pengukuran dilakukan dua kali sehari" is fine in
a procedure paragraph about measurement.

### 3.4 Pleonasm — pick one

`adalah merupakan` → *adalah* / *merupakan* · `agar supaya` → *agar* · `sangat penting
sekali` → *sangat penting* · `data-data` → *data* · `berbagai macam metode` → *berbagai
metode* · `naik ke atas` → *naik* · `seperti: A, B, dan lain-lain` → *seperti A dan B* /
*antara lain A dan B* · `Dengan demikian dapat disimpulkan bahwa` → *Jadi, …*

### 3.5 Relative clauses

Calque-English `di mana` / `yang mana` as a connector is **K/G**: use *yang* (relative),
*tempat* (place), *saat/ketika* (time), or split the sentence. `di mana` stays legal
only as a question word.

- ❌ `Sistem ini bekerja di mana sensor membaca suhu …` → ✅ `Sistem ini bekerja dengan
  sensor yang membaca suhu …`
- ❌ `Pada 2020, di mana pandemi terjadi, kunjungan turun.` → ✅ `Pada 2020, saat pandemi
  terjadi, kunjungan turun.`

## 4. AI-typical patterns to keep OUT (top signals)

The corpus-published theses predate heavy AI, but user drafts are full of these — strip them:

1. **Cosmic openers** — `Di era digital ini`, `Seiring perkembangan zaman`, `Tidak dapat
   dipungkiri bahwa`. Start from the concrete problem instead. (If there is no concrete
   problem available: `[PERLU DATA: masalah konkret yang melatarbelakangi penelitian]`.)
2. **Empty assertives** — `Seperti yang kita ketahui bersama`, `Sudah menjadi rahasia umum`.
   Replace with the claim + reference, or delete.
3. **`Hal ini` chains** — max one *hal ini* per text; name the referent instead.
4. **Inflated claims** — `sangat signifikan` (without a test), `solusi yang inovatif`,
   `sangat krusial`, triple adjectives (`efektif, efisien, dan akurat`). Replace with the
   measurable fact, or delete.
5. **Lecture voice** — `Mari kita bahas`, `Perlu diingat bahwa`, `Penting untuk dipahami`.
   State the content directly.
6. **Ritual connectors every paragraph** — `Selain itu,` `Oleh karena itu,` at every
   opening. Drop the connector when the logic is already clear.
7. **Fillers** — `dalam hal ini`, `dalam konteks ini`, `faktor-faktor tertentu`,
   `berbagai aspek`. Name the thing or delete.

## 5. Spelling (EYD V essentials)

### di- / ke-

- Preposition, separated: *di dalam, di atas, ke luar* (direction), *di mana* (question).
- Prefix, attached: *diuji, dianalisis, dibangun*. Test: swap for *ke/dari* — if it still
  makes sense as a place, it's a preposition.
- ❌ `dimana`, `diatas`, `dianalisis` written as `di analisis`.

### Compound words (serangkai vs terpisah)

- Serangkai: *kerjasama* ❌ → *kerja sama*; *tanggungjawab* → *tanggung jawab*;
  *pertanggungjawaban* (with prefix+suffix, serangkai); *antarmuka, pascasarjana,
  nonlinier, multiguna, subbab*.
- Hyphen before capitalized/italic foreign word: *non-Indonesia, pasca-reshuffle*.

### Numbers and units

- Decimal comma: `0,5 V` not `0.5 V`; thousands point: `1.000 responden`; `Rp5.000,00`.
- One–two-word numbers in letters: *dilakukan tiga kali*; data/series stay numeric
  (`3 dari 12 sampel`).
- No number at sentence start — reorder or spell out: *Sebanyak 25 responden …*.
- Unit style: `10 V`, `5 kg`, `50 Hz`, `25 °C` (space, lowercase symbols, no trailing
  period). Percent: pick one of `5%` / `5 %` and be consistent.

### Corpus-typical typos to sweep (seen repeatedly)

`menggunakkan` → *menggunakan* · `di hadapi` → *dihadapi* · `di tunjukkan` →
*ditunjukkan* · `memnbuat` → *membuat* · `sekolah mengkat` → *tingkat* · missing space
before `(` and after `,`/`.` · space before `,` `.` — all are **K**, always fixed.

## 6. Kata baku quick table

| Not baku | Baku |
| --- | --- |
| analisa, sintesa, diagnosa | analisis, sintesis, diagnosis |
| praktek, tehnik, metoda, sistim | praktik, teknik, metode, sistem |
| resiko, kwalitas, frekwensi, prosentase | risiko, kualitas, frekuensi, persentase |
| obyek, subyek, projek | objek, subjek, proyek |
| aktifitas, efektifitas, produktifitas | aktivitas, efektivitas, produktivitas |
| standarisasi, ekstrim, katagori | standardisasi, ekstrem, kategori |
| teoritis, konkrit, respon | teoretis, konkret, respons |
| ijin, nasehat, jadual, hakekat | izin, nasihat, jadwal, hakikat |
| nampak, himbau, faham, pondasi | tampak, imbau, paham, fondasi |
| merubah, mengkonsumsi, mengkonfirmasi | mengubah, mengonsumsi, mengonfirmasi |
| apotik, atlit, kadaluarsa | apotek, atlet, kedaluwarsa |
| propinsi, Nopember | provinsi, November |

Luluh rule: *k/p/s/t* melts after *meng-/peng-* (mengubah, mengonsumsi) unless the base
starts with a consonant cluster (mengkritik, memproduksi, memtransfer).

## 7. Foreign terms — the decision ladder

Stop at the first step that answers:

1. **Never translated:** proper names, eponyms (*Kalman, Fourier*), algorithm/product
   names (YOLO, ResNet, Arduino, ESP32), standards (ISO 9001), unit symbols, code
   (`analogRead()`), taxonomic names.
2. **Campus/journal style wins** if the target guide names a form.
3. **Living-usage test** — prefer the form the field actually reads: *mikrokontroler,
   panel surya, kepuasan pelanggan* (padanan dominan) vs *machine learning, deep
   learning, framework, database, Internet of Things* (asing dominan). When unsure and
   the user's field is technical, keep the foreign term italic.
4. **Meaning test** — reject a padanan that means something else in context
   (*luaran* hibah vs *keluaran* sistem).
5. **Consistency** — one concept, one form, everywhere. Track it in the term list.

After choosing: padanan first with foreign in parentheses once — *catu daya (power
supply)* — then padanan only; foreign term italic every time; absorbed KBBI words
upright (*mikrokontroler*); Indonesian affix on foreign word takes a hyphen
(*di-upload*, better: *diunggah*).

## 8. Abbreviations

- First use: full form + `(AKRONIM)`: *Internet of Things (IoT)*; afterwards the short
  form only, never alternating.
- Non-name expansions lowercase: *usaha mikro, kecil, dan menengah (UMKM)*; institution
  names capitalized: *Badan Pusat Statistik (BPS)*.
- No plural doubling: *banyak UMKM*, not *UMKM-UMKM*.
- Do not guess expansions. If unknown: `[PERLU DATA: kepanjangan XYZ]`.
- Gelar: `S.T., M.T., Ph.D.` with periods; common 3-letter abbreviations: `dll., dsb., dst.`
  with final period.

## 9. Citations in prose

- Two legal shapes: narrative `Santoso (2021) mengukur …` and parenthetical `… (Santoso,
  2021)`. APA-style `(Nama, Tahun)` is the default in Indonesian theses; some programs
  use IEEE `[1]` — follow the brief, stay consistent.
- One source per claim it actually supports; group sources by finding, not by sentence.
- Never fabricate or "fix" a reference: unverifiable → `[PERLU RUJUKAN: …]`.
- *dkk.* for *et al.*, *hlm.* for page — unless the program template says otherwise.
- Do not write `Menurut X mengatakan` (pick one), and do not stack direct quotes where a
  paraphrase belongs — proposals paraphrase.

## 10. Pertahankan — legitimate conventions, do NOT "fix"

- Passive *di-* throughout BAB III procedures — that is the register, not an error.
- "Penelitian ini" as subject — impersonal style is the default here.
- Italic foreign terms that dominate the field (*machine learning*, *framework*).
- Honest hedging: *diduga, cenderung, kemungkinan* — keep, unless stacked.
- *terdiri dari* (only *terdiri atas* is a recommendation), *dipengaruhi*, *mengkritik*.
- The user's own consistent stylistic habits, when they gave a writing sample — the
  corpus register is the target for NEW prose, but a user's consistent voice wins for
  their edits.
