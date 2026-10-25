# T17-R3 — Riset Ulang: Pendekatan Teks/Ucapan Indonesia → Representasi Isyarat SIBI di Layar

- **Task ID**: T17-R3 (percobaan ke-2; percobaan pertama kehabisan waktu)
- **Tanggal riset**: 2026-10-25. Setiap klaim mencantumkan URL + tanggal akses + status.
- **Untuk**: penerjemah dua arah SIBI; **arah 2** = teks/suara Indonesia → representasi isyarat SIBI di layar SPI kecil modul ESP32-S3; pemrosesan bahasa (ASR/NLP) di server lokal laptop (RTX 3070). Kendala perangkat tampilan mengacu fakta T17-R2 (`T17-R2-esp32s3-csi.md`: modul umum 8 MB flash + 8 MB PSRAM; firmware RuView memakai ~943 KB flash; throughput Wi-Fi S3 ~20 Mbps TCP / 30 Mbps UDP).
- **Metode**: tanpa tool WebSearch/WebFetch; akses daring via `curl` ke API Crossref/OpenAlex dan halaman primer + unduhan PDF. Deposit sesi sebelumnya dimanfaatkan: metadata Crossref `13-sempro-docx/verifikasi-rujukan-2026-10-24/` (dibuat 2026-10-24) dan cache HTML `scripts/sempro-isi/web/` (unduhan 2026-10-24 14:23).
- **Label**: [DIVERIFIKASI] = dilihat/unduh langsung sesi ini (2026-10-25); [DIVERIFIKASI-CACHE-2026-10-24] = dari unduhan langsung sesi 2026-10-24; [CUPILIKAN] = hanya potongan pencarian (belum inspeksi penuh); [TIDAK DITEMUKAN] = dicari jujur tidak ada/gagal diakses; [ESTIMASI] = hitungan penulis, bukan klaim sumber.

---

## 1. Struktur SIBI (Pertanyaan 1)

### 1.1 Status resmi SIBI

- Dwijayanti dkk. 2021 (IJACSA 12(10), DOI `10.14569/ijacsa.2021.0121046`), teks PDF diunduh langsung 2026-10-25 dari `https://thesai.org/Downloads/Volume12No10/Paper_46-Indonesia_Sign_Language_Recognition.pdf` (1,4 MB): *"In 1994, SIBI became the language used in formal schools for students with impairments. However, the deaf prefer to use BISINDO instead of SIBI in their daily lives."* [DIVERIFIKASI]
- SK Mendikbud No. 0190/P/1994 (diluncurkan 2 Mei 1994) dan Surat 868/C/U/95: fakta bank proyek sesi sebelumnya (entri W4 di `11-bahan-dpj4/04-referensi-bahan.md`, status OFFICIAL-WEB saat itu). **Tidak diinspeksi ulang sesi ini** karena situs Kamus SIBI Digital terblokir (lihat §3.1) → label [CUPILIKAN dari bank proyek; WAJIB verifikasi ulang sebelum dikutip di naskah].

### 1.2 Jumlah kosakata dasar (±2600 kata) — [TIDAK DITEMUKAN]

- Dikurangi: DDG (`"SIBI" "26 huruf"`, `kamus SIBI 1994 ribu kata kosakata`), Bing, Crossref (`query=SIBI 2600 kosakata`, `query.bibliographic=isyarat jadian SIBI pembentukan`), OpenAlex search — tidak ada sumber yang menyatakan angka ±2600.
- **Kesimpulan disiplin**: angka "±2600 kosakata" TIDAK BOLEH dikutip sampai ada sumber layak. Kandidat verifikasi lanjutan: (a) halaman Kamus SIBI Digital (diblokir Cloudflare, §3.1); (b) buku *Kamus Sistem Isyarat Bahasa Indonesia* (Departemen P&K, 1994) — entri daftar pustaka proposal; (c) *Pedoman Umum Sistem Isyarat Bahasa Indonesia* (Pusat Bahasa).

### 1.3 Alfabet manual 26 huruf — [DIVERIFIKASI]

- **OpenSIBI 2022 (PDF penuh diunduh 2026-10-25 dari `https://ijc.ilearning.co/TM/article/download/1690/610`, 1,37 MB)**, bagian Material Collecting: *"Data tersebut antara lain 50 kosakata bahasa isyarat SIBI yang terdiri dari 9 angka yakni 1-9, **26 huruf yakni A-Z** dan 15 kata campuran yakni Gigi, Hidung, Kaki, Mata, Mulut, Pipi, Tangan, Telinga, Adik, Ayah, Ibu, Buku, Jam, Bola, Kakak."* → SIBI memuat alfabel manual **26 huruf A–Z** + **angka 1–9**, data "mengacu pada kurikulum SIBI". [DIVERIFIKASI]
- Rabit 2026 (DOI `10.36341/rabit.v11i2.8340`, abstrak via Crossref 2026-10-25): dataset Kaggle 7.582 citra alfabet SIBI, **"24 kelas alfabet SIBI, yaitu A sampai Y tanpa huruf J dan Z"**; akurasi MobileNetV2+augmentasi 97,10%. [DIVERIFIKASI]
- Soekarta dkk. 2024 (DOI `10.33506/insect.v10i2.4079`, abstrak via Crossref 2026-10-25): dataset **"24 kelas huruf abjad statis"**; MediaPipe; akurasi 90,85%. [DIVERIFIKASI]
- Sintesis (label [ESTIMASI] untuk penyebabnya): alfabet SIBI = 26 huruf, tetapi dataset riset citra **statis** hanya memuat 24 kelas (A–Y) tanpa J dan Z — konsisten dengan J dan Z merupakan isyarat **dinamis/bergerak**; alasan ini belum terbaca langsung dari sumber yang diakses → perlu konfirmasi dari buku/KSD. Konsekuensi desain: 2 huruf tidak terwakili gambar diam.

### 1.4 Pembentukan kata produktif (kata jadian/berimbuhan) — bukti tidak langsung

- **Rakun, Fanany, Wisesa, Tjandra (2015), "A heuristic Hidden Markov Model to recognize inflectional words in sign system for Indonesian language known as SIBI"**, TIME-E 2015 (IEEE), hlm. 53–58 — terbaca dari daftar pustaka Dwijayanti dkk. 2021 (PDF diunduh 2026-10-25, ref. [13]). Judulnya membuktikan adanya kajian **kata berinfleksi dalam SIBI** (kata jadian hasil afiksasi). [DIVERIFIKASI sebagai referensi di PDF Dwijayanti; keberadaan paper Rakun sendiri BELUM diverifikasi via Crossref/IEEE sesi ini — WAJIB sebelum dikutip di daftar pustaka]
- Mekanisme lengkap pembentukan kata SIBI (kata dasar + bentuk ejaan + modifikasi gerakan) **TIDAK DITEMUKAN** pada sumber yang diakses sesi ini; sumber primer yang tepat = buku Kamus SIBI 1994 / Pedoman Umum SIBI (belum bisa diakses daring). → Jangan tulis mekanisme detail di naskah tanpa membaca sumber primer.
- Indikasi pragmatis: OpenSIBI 2022 hanya memodelkan 50 item (angka + huruf + 15 kata) dan mengakui keterbatasan "begitu banyak kosakata" (lihat §2.2) — bukti bahwa cakupan kosakata kamus SIBI jauh melampaui yang praktis dianimasikan.

### 1.5 Tata bahasa SIBI vs Indonesia lisan; penanda non-manual

- Mursita (2015), *INKLUSI* 2(2), DOI `10.14421/ijds.2202`, abstrak via Crossref 2026-10-25: survei 100 responden tunarungu (16–50 th, Jawa–Bali): mayoritas **tidak mendukung SIBI untuk komunikasi sehari-hari** "because of its concept cause difficulties", **91% memakai BISINDO**. [DIVERIFIKASI]
- Satillah dkk. (2024), *AUDHI* 7(1), DOI `10.36722/jaudhi.v7i1.2876` (halaman OJS di-cache 2026-10-24, `scripts/sempro-isi/web/audhi_sib.html`): SIBI dominan **dalam pembelajaran formal di kelas**, isyarat lokal/BISINDO dipakai di interaksi sosial di luar kelas. [DIVERIFIKASI-CACHE-2026-10-24]
- Urutan kata SIBI, ekspresi wajah, mouthings dalam SIBI: **[TIDAK DITEMUKAN]** pada sumber terindeks yang diakses sesi ini (pencarian DDG/Bing/Crossref tidak menghasilkan paper linguistik SIBI yang bisa diinspeksi). Pemerkuat internasional bahwa non-manual (khususnya mouthing) adalah masalah desain avatar: Hakozaki dkk. 2025 (§4). → Pertanyaan tata bahasa SIBI harus dijawab dari buku/pakar (SLB/PUSBINDIKTURANEGARA), bukan dari literatur yang bisa saya akses sesi ini.

---

## 2. Sistem terdahulu teks/suara → SIBI (Pertanyaan 2)

### 2.1 KASIBI (2019) — kamus suara→isyarat, animasi 3D

- Zikky & Akbar (2019), *Jurnal Sains Terapan (JST)* 5(2), DOI `10.32487/jst.v5i2.732`. Abstrak via OpenAlex `https://api.openalex.org/works/doi:10.32487/jst.v5i2.732` (diakses 2026-10-25): pipeline = **suara → teks (speech-to-text) → pencarian kata di database → tampilan animasi peraga 3D**; diuji sebagai media pembelajaran "based on SIBI standard" dengan rata-rata **3,362 dari 4** skala. Kata kunci: Visualisasi. Jumlah kosakata tidak disebut di abstrak. [DIVERIFIKASI]
- Halaman jurnal `https://jurnal.poltekba.ac.id/index.php/jst/article/view/732` = terblokir Cloudflare sesi ini ("One moment, please…") → full text belum dibaca. [TIDAK DITEMUKAN: rincian kosakata]

### 2.2 OpenSIBI (2022) — suara → animasi 3D (sistem preseden TERKUAT untuk arah 2)

- Fatmawati, Asmara, Prayogi, Hakkun (2022), *Technomedia Journal* 7(1), 22–39, DOI `10.33050/tmj.v7i1.1690`. Abstrak Crossref + **PDF penuh 18 hlm. diunduh 2026-10-25** (`https://ijc.ilearning.co/TMJ/article/download/1690/610`; halaman artikel `https://ijc.ilearning.co/TMJ/en/article/view/1690`). [DIVERIFIKASI]
- **Mekanisme (dari PDF)**: aplikasi Android → tombol mikrofon → **Google Speech-to-Text API** menerjemahkan suara → teks dicocokkan ke **API OpenSIBI** yang menyimpan **dataset model 3D kosakata isyarat format Collada** → model di-render di Android sebagai **animasi 3D**; Java (aplikasi) + C#; database MySQL.
- **Skala**: 50 kosakata = 9 angka (1–9) + 26 huruf (A–Z) + 15 kata campuran (Gigi, Hidung, …, Kakak). Karakter avatar 3D hanya dimodelkan **dari pinggang sampai lutut** (bukan badan penuh).
- **Keterbatasan yang dilaporkan penulisnya**: tidak dapat memuat "kosakata bahasa isyarat secara mendetail dikarenakan begitu banyak kosakata dengan gerakan…"; saran pengembangan = menambah kosakata + memperbaiki karakter animasi. Uji: SUS (System Usability Scale).
- Ini BUKAN penerjemahan tata bahasa — pencocokan **kata-level** (kata → satu model 3D).

### 2.3 INTECOMS (2024) — aplikasi mobile pembelajaran dasar isyarat SIBI

- Rodhiyah & Wulandari (2024), *INTECOMS: J. Inf. Technol. Comput. Sci.* 7(1), 58–63, DOI `10.31539/intecoms.v7i1.8326`. Halaman OJS (`https://journal.ipm2kpe.or.id/index.php/INTECOM/article/view/8326`, di-cache 2026-10-24; abstrak juga via Crossref 2026-10-25). [DIVERIFIKASI-CACHE-2026-10-24 + DIVERIFIKASI]
- Isi: aplikasi mobile sebagai **media pembelajaran dasar** bahasa isyarat "dengan metode SIBI" bagi masyarakat umum. Arah = **manusia belajar isyarat** (bukan mesin menerjemahkan). Media tampilan per isyarat (video/gambar/avatar) tidak dirinci di abstrak; PDF (`.../download/8326/5333`) belum dibaca → rincian [TIDAK DITEMUKAN].

### 2.4 DBESTI (2026) — aplikasi pengenalan alfabet SIBI (arah KEBALIKAN dari arah 2)

- Maulana, Adriansyah, Imaduddin (2026), *DBESTI: J. Digital Business and Technology Innovation* 3(1), 78–85, DOI `10.54914/dbesti.v3i1.2081`. Halaman OJS `https://journal.nurulfikri.ac.id/index.php/DBESTI/article/view/2081` (di-cache 2026-10-24; abstrak via Crossref 2026-10-25). [DIVERIFIKASI-CACHE-2026-10-24 + DIVERIFIKASI]
- Isi: Android (Kotlin, Jetpack Compose, Clean Architecture) **mengenali huruf alfabet statis SIBI real-time** dengan TensorFlow Lite; metode RAD; uji Black Box; **UAT 91,3%**. Arah = isyarat→teks (pengenalan), cakupan = alfabet statis. Perlu dikutip HANYA sebagai bukti tren aplikasi SIBI Android, bukan sebagai penerjemah teks→isyarat.

### 2.5 Penerjemah teks→isyarat "berbasis aturan" — hampir semua yang berlabel "penerjemah" ternyata arah pengenalan

Hasil DDG 2026-10-25 (semua [CUPILIKAN] — hanya judul+snippet, belum inspeksi penuh):
1. "Sistem Penerjemah Sederhana Bisindo Menggunakan Mediapipe Holistic, LSTM, dan Rule-Based NLP" — `https://e-journal.umc.ac.id/index.php/INT/article/view/8450` (PDF snippet: mengenali gerakan → teks; rule-based NLP di sisi bahasa). Arah isyarat→teks, bahasa isyarat BISINDO.
2. "Rancang Bangun Sistem Penerjemah Bahasa Isyarat … (BISINDO WEB) … using a rule-based algorithm" — `https://openjurnal.unmuhpnk.ac.id/informatique/article/view/9205` (web, mengubah gestur BISINDO → teks & suara). Arah isyarat→teks.
3. "Model Penerjemah Bahasa Isyarat SIBI Statis Berbasis CNN (varian VGG)" — `https://ejournal2.unud.ac.id/index.php/jnatia/article/view/65`. Arah pengenalan SIBI statis.
4. Rakun dkk. 2015 (lihat §1.4) — pengenalan kata berinfleksi SIBI, arah isyarat→teks.
- **Kesimpulan**: sistem Indonesia arah teks/suara → isyarat yang terverifikasi hanyalah **kamus kata-level dengan animasi 3D** (KASIBI, OpenSIBI). **[TIDAK DITEMUKAN] sistem teks→SIBI dengan transfer tata bahasa (glossing + reorder + non-manual).** Judul "penerjemah" pada literatur Indonesia menyesatkan jika dibaca sebagai arah 2 — perlu dinyatakan eksplisit di naskah.

---

## 3. Opsi tampilan di layar SPI kecil (Pertanyaan 3)

### 3.1 Video isyarat prarekam

- **Aset Kamus SIBI Digital (KSD)**: situs `https://pkplk.kemendikdasmen.go.id/sibi` **terblokir Cloudflare** ("One moment, please…", uji ulang 2026-10-25); snapshot Wayback tersedia (`http://web.archive.org/web/20260507025618/https://pkplk.kemendikdasmen.go.id/sibi/`, via API `archive.org/wayback/available`, 2026-10-25) tetapi `web.archive.org` **timeout** dari lingkungan riset ini → **isi KSD (apakah ada video/gambar, jumlah kosakata, lisensi unduh) [TIDAK DIVERIFIKASI]**. Keberadaan KSD sendiri = fakta proyek W4 sesi sebelumnya.
- Analisis kelayakan ([ESTIMASI] dari fakta T17-R2): video per isyarat (mis. MJPEG 240×240, 1–2 s) ≈ 100 KB–1 MB per klip; 50 isyarat ≈ 5–50 MB → **tidak muat di flash 8 MB**, hanya mungkin di PSRAM 8 MB untuk buffer 1– beberapa klip. Pola realistis: **server lokal merender/mengirim, ESP32 menampilkan stream** (Wi-Fi S3 20–30 Mbps cukup untuk MJPEG kecil).

### 3.2 Avatar animasi 2D/3D

- Preseden: KASIBI & OpenSIBI pakai **animasi 3D per kosakata**; OpenSIBI menyimpan model **Collada** di server API dan hanya **50 kosakata** — bukti biaya pembuatan aset per isyarat sangat tinggi (paper-nya sendiri menyebut keterbatasan kosakata). [DIVERIFIKASI]
- On-device ESP32: render 3D real-time tidak realistis; animasi 2D sprite/skeletal ringan (mis. LVGL) mungkin untuk 26 huruf + N kata. [ESTIMASI]
- Pola paling masuk akal: **avatar 3D dirender di server laptop** (aset Collada ala OpenSIBI atau Blender) → dikirim sebagai video/MJPEG → layar ESP32 tinggal menampilkan. [ESTIMASI]

### 3.3 Rangkaian gambar diam

- 24 huruf statis terwakili gambar diam; J & Z (dinamis, §1.3) tidak. Ukuran: 26 PNG 100×100 → RGB565 ≈ 20 KB/gambar ≈ 520 KB total → **muat di flash 8 MB**. [ESTIMASI]
- Preseden tampilan simbol 2D SIBI ada di literatur: "Multimedia Interaktif Introduction of Simiotrics (CardGame) using SIBI Symbol – Sign Language 2D Based" (DOI `10.21070/ups.1552`, via pencarian Crossref 2026-10-25) [CUPILIKAN judul saja].

### 3.4 Glos teks + ejaan jari (fingerspelling) — opsi paling selaras SIBI

- Ejaan jari adalah bagian resmi sistem SIBI: OpenSIBI memakai **26 huruf A–Z** sebagai kosakata inti [DIVERIFIKASI]; riset SIBI secara luas menargetkan alfabet (Rabit 2026, Soekarta 2024, DBESTI 2026) [DIVERIFIKASI]. Kata di luar kamus dapat dieja — mekanisme kata jadian SIBI memakai ejaan (§1.4, detail mekanisme belum terverifikasi penuh).
- Di layar kecil: tampilkan teks Indonesia + glos SIBI + ikon/gambar konfigurasi tangan per huruf + jumlah N isyarat kata dasar. Kombinasi §3.3 + §3.4 = MVP paling murah aset.

### 3.5 SignWriting

- Tidak ditemukan penerapan SignWriting untuk SIBI pada sumber yang diakses sesi ini [TIDAK DITEMUKAN]. Notasi ini tidak akrab bagi awam → tidak direkomendasikan untuk MVP; hanya menarik sebagai notasi data di sisi server.

---

## 4. Internasional (Pertanyaan 4) — bukti keterbatasan teks→isyarat

- **Picron, Van Landuyt, Omardeen (2024). "(Towards) Sign Language Machine Translation in Practice."** dalam *Machine Translation: Technologies and Applications* (Springer), DOI `10.1007/978-3-031-47362-3_14` — via Crossref 2026-10-25. Bab-buku lain di koleksi yang sama (semua Crossref-verified 2026-10-25, konten bab belum dibaca): "The Pipeline of Sign Language Machine Translation" (`..._1`), "Sign Languages as Source Language for Machine Translation: Historical Overview and Challenges" (`..._7`), "Linguistic Processing for Sign Language Translation" (`..._8`). [DIVERIFIKASI metadata; isi bab = CUPILIKAN]
- **Hakozaki, Murakami, Uchida, Kaneko (2025). "Evaluation of Japanese Sign Language Avatar with Mouthing in News Content."** *Proc. 27th Int. ACM SIGACCESS (ASSETS)*, DOI `10.1145/3663547.3759693` — via Crossref 2026-10-25. Bukti bahwa **mouthing (penanda non-manual/bibir)** dievaluasi khusus pada avatar isyarat → non-manual adalah isu tampilan kelas satu, bukan aksesori. [DIVERIFIKASI metadata]
- Sagawa & Takeuchi (2002), sistem pengajaran JSL dengan pengenalan + **generation** isyarat, ACM Multimedia, DOI `10.1145/641007.641035` [DIVERIFIKASI-CACHE-2026-10-24].
- **Pernyataan umum "translasi teks→isyarat bukan substitusi kata; tata bahasa berbeda; non-manual penting"** untuk naskah harus dikutip dari teks bab Springer di atas (belum diakses) — sesi ini hanya memverifikasi keberadaan & topiknya. Jangan parafrase klaim isi sebelum baca babnya.

---

## 5. Batas MVP yang jujur (Pertanyaan 5)

**Yang defensible** (semua preseden terverifikasi):
1. Cakupan ala OpenSIBI: **angka (1–9) + alfabel manual (26 huruf A–Z) + N kata dasar** (OpenSIBI memakai N=15; proyek bisa ambil N serupa, mis. 15–100, dari kata yang benar-benar tersedia asetnya).
2. Pipeline arah 2 ala KASIBI/OpenSIBI: suara/teks Indonesia (di-*server*, mis. ASR Whisper) → normalisasi → **pencocokan kata-level ke kamus isyarat** → kata OOV jatuh ke **ejaan jari** → render tampilan.
3. Tampilan MVP: glos teks + gambar konfigurasi tangan/ejaan jari (muat di flash) ATAU stream MJPEG avatar/video dari server lokal (muat di bandwidth Wi-Fi, memori terbatas).
4. Metrik jujur: cakupan kamus (berapa % kata uji ter-cover), latensi, keberhasilan tampilan — **BUKAN** BLEU/WER penerjemahan kalimat.

**Yang mustahil diklaim MVP** (tanpa dukungan literatur):
- Penerjemahan kalimat penuh dengan tata bahasa isyarat + non-manual — tidak ada preseden Indonesia; avatar 3D saja sudah mahal (OpenSIBI: 50 kosakata, setengah badan).
- "Cakupan kamus SIBI penuh ±2600 kata" — angka belum terverifikasi + aset per isyarat belum ada (lihat §1.2, §3.2).
- Produksi isyarat kontinu/real-time natural — isu riset terbuka internasional (§4).
- Orientasi komunitas tuli sehari-hari: 91% penutur isyarat memakai BISINDO (Mursita 2015); SIBI hidup di **konteks pendidikan formal** (Satillah 2024; Dwijayanti 2021) → posisikan alat sebagai sarana pembelajaran/pendidikan SIBI, bukan alat komunikasi komunitas.

---

## 6. Kontradiksi & hal yang perlu dicek ulang

1. **Judul vs isi**: banyak paper Indonesia berjudul "penerjemah bahasa isyarat" padahal arahnya pengenalan (isyarat→teks) — termasuk DBESTI 2026, jnatia, BISINDO WEB. Jangan dikutip sebagai preseden arah 2.
2. **24 vs 26 huruf**: dataset statis = 24 kelas tanpa J/Z (Rabit 2026; Soekarta 2024) vs OpenSIBI = 26 huruf A–Z. Konsisten jika J/Z dinamis, tetapi penyebab "dinamis" belum terbaca dari sumber — konfirmasi dari buku Kamus SIBI/KSD.
3. **Angka kosakata kamus SIBI**: belum ada sumber layak — JANGAN tulis "±2600" di naskah apa pun sebelum KSD/buku diverifikasi.
4. Rakun 2015 belum diverifikasi keberadaannya lewat Crossref/IEEE (hanya terbaca sebagai referensi di Dwijayanti 2021).

## 7. Sumber yang gagal diakses sesi ini (untuk kejujuran metode)

- `https://pkplk.kemendikdasmen.go.id/sibi` — Cloudflare challenge (uji 2026-10-25).
- `https://jurnal.poltekba.ac.id/index.php/jst/article/view/732` (KASIBI) — Cloudflare challenge (2026-10-25).
- `web.archive.org` — connection timeout dari sandbox (2026-10-25), padahal snapshot KSD tersedia.
- Semantic Scholar API — HTTP 429 sepanjang sesi; r.jina.ai — 401 (IP reputation); Bing HTML — tak terurai.
- `https://journal.ipm2kpe.or.id/index.php/INTECOM/article/download/8326/5333` dan `https://journal.nurulfikri.ac.id/index.php/DBESTI/article/download/2081/486` (PDF INTECOMS/DBESTI) — belum sempat diunduh (prioritas waktu).

## 8. Tindak lanjut yang direkomendasikan

1. Verifikasi Rakun 2015 via Crossref/IEEE Xplore (`inflectional words SIBI Rakun`); verifikasi angka kosakata dari buku Kamus SIBI 1994 (perpustakaan) atau KSD lewat jaringan tanpa Cloudflare.
2. Unduh PDF INTECOMS & DBESTI (URL di §2.3–2.4) untuk rincian media tampilan.
3. Baca bab Springer 2024 (`10.1007/978-3-031-47362-3_14`, `_1`, `_7`, `_8`) untuk kutipan keterbatasan SLMT yang sahih.
4. Uji konsep cepat: render 26 huruf + 15 kata sebagai PNG RGB565 di layar SPI (hitung memori & FPS nyata) — angka §3.3 masih [ESTIMASI].

---

## Lampiran: log sumber (URL · status · tanggal akses)

| # | Sumber | URL | Status | Akses |
|---|---|---|---|---|
| 1 | Crossref API (KASIBI) | https://api.crossref.org/works/10.32487/jst.v5i2.732 | DIVERIFIKASI (metadata; abstrak kosong) | 2026-10-25 |
| 2 | OpenAlex (abstrak KASIBI) | https://api.openalex.org/works/doi:10.32487/jst.v5i2.732 | DIVERIFIKASI | 2026-10-25 |
| 3 | Halaman KASIBI JST | https://jurnal.poltekba.ac.id/index.php/jst/article/view/732 | TIDAK DITEMUKAN (Cloudflare) | 2026-10-25 |
| 4 | Crossref API (OpenSIBI, abstrak penuh) | https://api.crossref.org/works/10.33050/tmj.v7i1.1690 | DIVERIFIKASI | 2026-10-25 |
| 5 | PDF OpenSIBI (18 hlm.) | https://ijc.ilearning.co/TM/article/download/1690/610 | DIVERIFIKASI (diunduh, 1,37 MB) | 2026-10-25 |
| 6 | Halaman OpenSIBI | https://ijc.ilearning.co/TMJ/en/article/view/1690 | DIVERIFIKASI | 2026-10-25 |
| 7 | Halaman INTECOMS (cache) | https://journal.ipm2kpe.or.id/index.php/INTECOM/article/view/8326 | DIVERIFIKASI-CACHE-2026-10-24 | 2026-10-24 |
| 8 | Crossref API (INTECOMS) | https://api.crossref.org/works/10.31539/intecoms.v7i1.8326 | DIVERIFIKASI | 2026-10-25 |
| 9 | Halaman DBESTI (cache) | https://journal.nurulfikri.ac.id/index.php/DBESTI/article/view/2081 | DIVERIFIKASI-CACHE-2026-10-24 | 2026-10-24 |
| 10 | Crossref API (DBESTI) | https://api.crossref.org/works/10.54914/dbesti.v3i1.2081 | DIVERIFIKASI | 2026-10-25 |
| 11 | Crossref API (Rabit 2026) | https://api.crossref.org/works/10.36341/rabit.v11i2.8340 | DIVERIFIKASI | 2026-10-25 |
| 12 | Crossref API (Soekarta 2024) | https://api.crossref.org/works/10.33506/insect.v10i2.4079 | DIVERIFIKASI | 2026-10-25 |
| 13 | Crossref API (Mursita/INKLUSI 2015) | https://api.crossref.org/works/10.14421/ijds.2202 | DIVERIFIKASI | 2026-10-25 |
| 14 | Halaman AUDHI (cache) | https://doi.org/10.36722/jaudhi.v7i1.2876 → OJS UAI | DIVERIFIKASI-CACHE-2026-10-24 | 2026-10-24 |
| 15 | PDF Dwijayanti 2021 (IJACSA) | https://thesai.org/Downloads/Volume12No10/Paper_46-Indonesia_Sign_Language_Recognition.pdf | DIVERIFIKASI (diunduh, 1,4 MB) | 2026-10-25 |
| 16 | Crossref API (Picron dkk. 2024) | https://api.crossref.org/works/10.1007/978-3-031-47362-3_14 | DIVERIFIKASI (metadata) | 2026-10-25 |
| 17 | Crossref API (Hakozaki dkk. 2025) | https://api.crossref.org/works/10.1145/3663547.3759693 | DIVERIFIKASI (metadata) | 2026-10-25 |
| 18 | Sagawa & Takeuchi 2002 (metadata cache) | https://api.crossref.org/works/10.1145/641007.641035 (file `scripts/sempro-isi/crossref/sagawa2002_jsl_tutor.json`) | DIVERIFIKASI-CACHE-2026-10-24 | 2026-10-24 |
| 19 | KSD pkplk | https://pkplk.kemendikdasmen.go.id/sibi | TIDAK DIVERIFIKASI (Cloudflare) | uji 2026-10-25 |
| 20 | Wayback KSD snapshot | http://web.archive.org/web/20260507025618/https://pkplk.kemendikdasmen.go.id/sibi/ | ADA tapi timeout | 2026-10-25 |
| 21 | DDG: rule-based translators | e-journal.umc.ac.id/INT/8450; openjurnal.unmuhpnk.ac.id/informatique/9205; ejournal2.unud.ac.id/jnatia/65 | CUPILIKAN | 2026-10-25 |
| 22 | Crossref search: SIBI Symbol 2D | https://doi.org/10.21070/ups.1552 | CUPILIKAN (judul) | 2026-10-25 |

*Selesai T17-R3 — 2026-10-25. Dokumen bahan riset; bukan deliverable final proyek.*
