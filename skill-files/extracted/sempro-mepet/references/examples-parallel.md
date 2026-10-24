# Parallel examples — bad → good, by pattern

Rich pairs for calibration. Left side = what actually shows up in user drafts and in
corpus theses; right side = the same content at target register. Annotations name the
rule (KE/AI/EJ/KB codes from `language-core.md`). All names, numbers, and citations in
these examples are illustrative placeholders — never copy them into real prose.

## 1. Informal → formal register (word level)

| Draft (informal) | Proposal (baku) | Why |
| --- | --- | --- |
| alat ini ngasih tau pemilik | alat ini memberikan notifikasi kepada pemilik | KB + register |
| bannya udah abis | baterai telah habis | KB |
| bikin sistem biar gampang | membangun sistem agar mempermudah | KB |
| kayaknya susah dipake | diduga sulit digunakan | KB + hedging |
| pakenya ESP32 | menggunakan ESP32 | KB |
| nyari data | mengumpulkan data | KB |
| ngecek suhu | memeriksa suhu | KB |
| ditaro di dalam box | diletakkan di dalam wadah | KB |
| doang | saja | KB |
| jarang banget | jarang | KB |
| gampangin kerjaan petugas | mempermudah tugas petugas | KB |
| banyak orang yang ngerti | masyarakat memahami | KB |

## 2. Calque / AI pattern → natural academic (phrase level)

| Draft (calque/AI) | Proposal | Code |
| --- | --- | --- |
| sistem di mana sensor membaca suhu | sistem dengan sensor yang membaca suhu | AI-14 |
| metode yang mana dipakai untuk klasifikasi | metode yang digunakan untuk klasifikasi | AI-13 |
| IoT memainkan peran penting | IoT berperan penting | AI-05 |
| teknologi ini mengambil tempat dalam … | teknologi ini digunakan dalam … | AI-08 |
| Hal ini menunjukkan bahwa … (3rd time) | Penurunan tegangan tersebut menunjukkan bahwa … | AI-15 |
| Dalam hal ini, sistem mengirim data. | Sistem mengirim data. | filler |
| Perlu diingat bahwa sampel terbatas. | Sampel penelitian terbatas. | AI-11 |
| sangat signifikan sekali | signifikan (*p* < 0,05) atau hapus | AI-12/KE-04 |
| solusi yang inovatif, efektif, dan efisien | [ganti dengan angka/fakta konkret] | AI-07/09 |
| Di era digital ini, teknologi berkembang pesat. | [hapus — mulai dari masalah konkret] | AI-01 |
| Tidak dapat dipungkiri bahwa kebutuhan meningkat. | Kebutuhan meningkat (BPS, 2023). | AI-03 |
| melakukan analisis terhadap data | menganalisis data | NM-01 |
| Penelitian ini bertujuan untuk mengetahui … | Penelitian ini bertujuan mengukur / merancang / membandingkan … | NM-01 |

## 3. Corpus-typical mechanical errors (K level, always fix)

| Seen in corpus | Correct |
| --- | --- |
| menggunakan, menggunakkan, menggunakkan | menggunakan |
| di hadapi, di tunjukkan, di buat | dihadapi, ditunjukkan, dibuat |
| memnbuat, menambhakan | membuat, menambahkan |
| `masakan ,karena` / `karena ,` (space before comma) | karena, |
| `seperti ini(yang salah)` (no space before parenthesis) | seperti ini (yang benar) |
| `di atas , kemudian` (space before comma) | di atas, kemudian |
| `12V`, `25derajat` , `5 kg` vs `5kg` mixed | 12 V, 25 °C, 5 kg — satu bentuk konsisten |
| `0.5` decimal | 0,5 |
| `praktek`, `sistim`, `analisa`, `aktifitas` | praktik, sistem, analisis, aktivitas |
| `internet of things`, `Internet Of Things` (plain, inconsistent) | *Internet of Things* (IoT) — miring, sekali didefinisikan |

## 4. Paragraph rewrites (before → after)

### 4.1 Latar belakang opening

> **Before:** Di era digital ini, tidak dapat dipungkiri bahwa teknologi IoT
> berkembang sangat pesat dan memainkan peran penting dalam berbagai macam bidang
> kehidupan. Oleh karena itu, dalam penelitian ini membahas rancang bangun sistem
> parkir cerdas.

> **After:** Lahan parkir gedung X memiliki 120 slot, tetapi pengunjung menghabiskan
> rata-rata 15 menit untuk mencari slot kosong [PERLU DATA: sumber angka observasi].
> Pendataan kendaraan masih mengandalkan pengamatan visual petugas sehingga sering
> terjadi kesalahan pencatatan. Oleh karena itu, penelitian ini merancang bangun
> sistem parkir cerdas berbasis *Internet of Things* (IoT) untuk menampilkan
> ketersediaan slot secara langsung.

Changed: cosmic opener + empty assertive deleted (AI-01, AI-03); concrete problem and
numbers first; subject restored (`dalam penelitian ini membahas` → `penelitian ini
merancang`, KE-01); foreign term italic with first-use expansion; closing move names
the expected capability.

### 4.2 Rumusan masalah

> **Before:** Masalahnya adalah alat ini gimana cara deteksi pakan abis gak dan
> gimana ngirim ke HP pemilik, serta apakah bagus gak akurasinya.

> **After:** Berdasarkan latar belakang yang telah dipaparkan, maka masalah yang
> dikaji dalam penelitian ini dapat dirumuskan sebagai berikut.
> 1. Bagaimana merancang bangun dispenser pakan otomatis berbasis IoT untuk kucing?
> 2. Bagaimana sistem memberikan notifikasi kepada pemilik ketika pakan habis?
> 3. Bagaimana kinerja sistem ditinjau dari kecepatan notifikasi dan akurasi pembacaan
>    sisa pakan?

Changed: colloquial register (KB) converted; one lead-in sentence in corpus form; three
parallel `Bagaimana` items covering design, function, testing (mirrors the corpus triad);
each item answerable and later mirrored 1:1 in tujuan.

### 4.3 Tujuan penelitian

> **Before:** 1. Untuk mengetahui tentang alat ini. 2. Supaya bisa membantu orang.
> 3. Untuk mempelajari lebih lanjut.

> **After:** Berdasarkan rumusan masalah yang telah diuraikan, tujuan penelitian ini
> adalah sebagai berikut.
> 1. Merancang bangun dispenser pakan otomatis berbasis IoT.
> 2. Menerapkan notifikasi otomatis kepada pemilik ketika pakan habis.
> 3. Menguji kinerja sistem ditinjau dari kecepatan notifikasi dan akurasi pembacaan
>    sisa pakan.

Changed: vague verbs (`mengetahui tentang`, `mempelajari lebih lanjut`) replaced with
verifiable ones (merancang bangun / menerapkan / menguji); each item mirrors a rumusan
item; no benefit-statement leakage (`supaya bisa membantu orang` belongs to manfaat).

### 4.4 Theory block (BAB II)

> **Before:** Sensor DHT22 adalah sensor yang mana bisa mengukur suhu dan kelembaban.
> Menurut Widodo (2020) mengatakan bahwa sensor DHT22 memiliki akurasi tinggi. Selain
> itu, menurut Putri (2019) juga mengatakan bahwa DHT22 murah. Selain itu, DHT22
> mudah digunakan.

> **After:** DHT22 merupakan sensor yang mengukur suhu dan kelembaban udara
> sekaligus. Sensor ini dipilih karena akurasinya tinggi (Widodo, 2020) dan harganya
> terjangkau (Putri, 2019). Dalam penelitian ini, DHT22 digunakan sebagai masukan
> utama pada subsistem pemantauan karena keluarannya sudah terkalibrasi dalam bentuk
> digital.

Changed: `yang mana` relative calque (AI-13); `Menurut X mengatakan` doubled subject
(KE-01); sources grouped by finding instead of one-sentence-per-source; mandatory
relevance sentence added (`Dalam penelitian ini …`); *merupakan* before noun phrase.

### 4.5 Penelitian terdahulu synthesis

> **Before:** Penelitian A membuat sistem parkir. Penelitian B juga membuat sistem
> parkir tapi pakai kamera. Penelitian C pakai sensor. Jadi penelitian ini beda.

> **After:** Pengembangan sistem parkir cerdas telah banyak dilakukan. Penelitian A
> (2021) menerapkan kamera untuk mengenali plat nomor, sedangkan Penelitian B (2022)
> menggunakan sensor ultrasonik pada tiap slot. Namun, keduanya belum menerapkan
> pemetaan rute menuju slot kosong. Oleh karena itu, penelitian ini menggabungkan
> sensor ultrasonik dengan aplikasi peta untuk mengarahkan pengguna ke slot terdekat.

Changed: one-sentence-per-source listing replaced by grouped synthesis; contrast
connector `sedangkan` (comma before); the gap stated positively and specifically;
final sentence commits to the combination that defines this research.

### 4.6 Procedure (BAB III)

> **Before:** Pertama-tama yang dilakukan adalah pembuatan rangkaian yang dapat
> menjadi inputan mikrokontroler. Setelah itu dilakukan pengujian terhadap rangkaian
> oleh peneliti. Hasil dari pengujian tersebut kemudian dicatat.

> **After:** Adapun prosedur pengujian sensor adalah sebagai berikut.
> 1. Menyiapkan peralatan yang digunakan.
> 2. Merangkai sensor sesuai dengan Gambar 3.2.
> 3. Menghubungkan rangkaian dengan komputer melalui IDE Arduino.
> 4. Mengunggah program pengujian.
> 5. Mengamati, mencatat, dan menganalisis hasil pembacaan sensor.

Changed: nominalized narrative (`pembuatan rangkaian … dilakukan`) converted to the
corpus me- imperative list; passive agent `oleh peneliti` dropped (actor is irrelevant
in procedures); figure reference inserted; standard closing triple.

### 4.7 Batasan masalah

> **Before:** Batasannya cuma untuk ayam aja, ukurannya tidak terlalu besar, dan
> pakai teknologi yang ada sekarang.

> **After:** Adapun batasan masalah pada penelitian ini adalah:
> 1. Objek penelitian adalah ayam kampung umur 8–12 minggu.
> 2. Sistem dibuat sebagai purwarupa dengan ukuran 1300 mm × 800 mm × 950 mm.
> 3. Pengujian dilakukan pada kandang semi tertutup.
> 4. Pengukuran mencakup suhu, kadar amonia, serta pemberian pakan otomatis.

Changed: colloquial register (cuma, aja) converted; each fence is a checkable
declarative (object+age, dimensions with units and × separators, environment,
parameter list) — the four fence types from `bab1-pendahuluan.md`.

## 5. Full move-bank quick copy (corpus register)

For drafting speed, the highest-frequency corpus frames:

```
Berdasarkan latar belakang yang telah dipaparkan, maka masalah yang dikaji dalam
penelitian ini dapat dirumuskan sebagai berikut: …
Berdasarkan rumusan masalah yang telah diuraikan, tujuan penelitian ini adalah: …
Adapun batasan masalah pada penelitian ini adalah: …
Dengan adanya permasalahan tersebut, maka dirancang bangun [X] berbasis [Y] yang
menggunakan [Z].
Dengan adanya sistem tersebut diharapkan dapat membantu [pihak] dalam [tindakan]
sehingga [dampak].
… ditunjukkan pada Gambar 3.x.
Pada skema tersebut, [A] terhubung dengan [B] melalui [jalur], yang berfungsi untuk
[fungsi].
Dalam penelitian ini, [X] digunakan sebagai [peran] karena [alasan].
Pengujian dilakukan untuk mengetahui [parameter] dengan [metrik].
Adapun prosedur pengujian [X] adalah sebagai berikut. …
```

These frames are furniture, not content: every bracket needs the user's verified facts,
and no frame may appear twice within one section.
