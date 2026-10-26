# Catatan Pengemasan Dokumen Terstruktur DPJ-4 SIBI-CSI

Dibuat 24 Oktober 2026. Pekerjaan: **pengemasan/kompilasi** — menyusun materi
`sempro/dpj4-sibi-csi` (23 Oktober 2026) menjadi satu dokumen terstruktur dalam dua format.
**Tidak ada satu kata pun teks bab yang diubah**; seluruh isi disalin verbatim dari materi
(kesetiaan diverifikasi otomatis, lihat bagian Verifikasi).

## 1. Berkas keluaran

| Berkas | Isi |
|---|---|
| `Proposal-Sempro-DPJ4-SIBI-CSI.docx` | Dokumen utuh: sampul → daftar isi (romawi kecil i–iii) → BAB I–III + Daftar Pustaka (arab mulai 1); 49 halaman A4 |
| `Proposal-Sempro-DPJ4-SIBI-CSI.md` | Markdown terpadu: blok identitas + BAB I–III + Daftar Pustaka, konten identik verbatim dengan DOCX |
| `assets/gambar-3.1.png`, `assets/gambar-3.2.png` | Kedua diagram BAB III siap cetak (hasil gambar ulang, struktur dan teks simpul sama dengan kode Mermaid sumber). Revisi 26 Okt: gambar dikecilkan (12,8 cm & 8,9 cm) dengan font diperbesar (lihat bagian 9) |
| `catatan-pengemasan.md` | Berkas ini |

## 2. Keputusan pengemasan (docx)

- **Gaya**: skripsi Indonesia — Times New Roman 12pt, spasi 1,5, margin kiri 4 cm atas/kanan/bawah 3 cm, rata kiri-kanan dengan indentasi baris pertama 1,25 cm.
- **Sampul**: resep akademik R5 (Clean White): label "PROPOSAL PENELITIAN", judul kapital tiga baris, tabel identitas bergaris bawah. Seluruh nilai identitas berupa penanda `[PERLU DATA: …]` tersorot kuning karena belum tersedia di materi.
- **Daftar isi**: bidang TOC otomatis kedalaman BAB–subbab–anak subbab (55 entri). Nomor halaman pada berkas masih **estimasi placeholder** — di Word klik kanan daftar isi → *Update Field* → *Update entire table* agar mutakhir.
- **Nomor halaman**: sampul tanpa nomor; daftar isi romawi kecil (i, ii, iii) rata tengah; isi arab mulai 1 rata kanan.
- **Tabel** (8 buah): tiga-garis akademik — keterangan di atas rata kiri (nomor tebal), kepala 9pt tebal tengah, isi 9pt; baris tidak terpotong halaman, kepala berulang lintas halaman.
- **Gambar** (2 buah): dua jalur tata letak ulang dari kode Mermaid (perataan otomatis Mermaid menghasilkan rasio 1:7,7 yang tak muat halaman; sesuai catatan materi, "untuk Word, gambar ulang … dengan struktur yang sama"). Simpul, teks, jalur, dan label lolos/gagal/pelatihan identik. Revisi 26 Oktober 2026: gambar dikecilkan menjadi 14×12,8 cm dan 14×8,9 cm dengan teks cetak 7,1–8,1 pt (rincian di bagian 9).
- **Penanda** `[PERLU DATA: …]`: 38 kemunculan (semua keputusan pembimbing/data pribadi/parameter rancangan), **tersorot kuning** agar mudah dicari (Ctrl+F "PERLU"). Seluruh 60 kemunculan lain telah diisi dari sumber terverifikasi pada 24 Oktober 2026 (lihat bagian 6).
- **Sitasi IEEE `[n]`** dan **daftar pustaka 62 entri** (indentasi gantung) apa adanya; 28 rujukan baru ditambahkan pada putaran kedua dengan DOI terverifikasi Crossref.

## 3. Hasil verifikasi otomatis

- Sinkron konten sumber → DOCX: **568/568 unit teks ditemukan** (pemeriksaan pandoc round-trip).
- postcheck.py (skill docx): **0 error**; 1 peringatan spasi = desain tabel 9pt (pola yang sama dengan DPJ terdahulu yang lolos).
- Inspeksi visual halaman kunci (sampul, daftar isi, awal BAB I, Tabel 2.2, Gambar 3.1, Tabel 3.5, Daftar Pustaka): lolos tanpa cacat.
- Jumlah penanda: 38 kemunculan (4 BAB I, 2 BAB II, 33 BAB III, 0 Daftar Pustaka) — cocok dengan `laporan-penanda.md` materi. Putaran kedua (24 Okt): 596/596 unit teks, 53 halaman PDF, postcheck 0 error.

## 4. Temuan lint bahasa (dilaporkan, TIDAK diubah)

Menjalankan `periksa.py` (skill naskah-id) pada 12.043 kata menghasilkan 8 temuan:

- **1 temuan kaidah genuin**: koma sebelum "sehingga" pada kalimat "…bentuk jari yang tepat**, sehingga** peragaan…" (Subbab 3.7.6). EYD V tidak memakai koma sebelum *sehingga* bila anak kalimat mengikuti induk. Siap diperbaiki satu hapusan koma bila pemilik setuju.
- 2 positif palsu: "di **antara** 5–8 kelas" (preposisi, bukan konjungsi antara…dan) dan "skor F1 **makro**" (kata mandiri, bukan bentuk terikat).
- 5 catatan gaya (AI-17): penghubung "Oleh karena itu" muncul 5 kali — berjauhan, bukan gerombolan; boleh dibiarkan.

## 5. Yang perlu dilakukan pemilik

1. Isi identitas sampul (nama, NIM, program studi, universitas, pembimbing, tahun) — semua tersorot kuning.
2. Di Word: perbarui bidang daftar isi setelah pengisian selesai.
3. Isi 38 penanda `[PERLU …]` yang tersisa sesuai prioritas `laporan-penanda.md` — seluruhnya keputusan bersama pembimbing, data pribadi/mitra, atau parameter rancangan Tabel 3.6. Penanda Daftar Pustaka (URL Kemenko PMK, tanggal akses BRIN, terbitan *Kamus SIBI*, commit RuView) SUDAH terisi.
4. Bawa ke bimbingan 8 keputusan terbuka pada `catatan.md` materi (Subbab 6), khususnya redaksi rumusan masalah no. 3 dan istilah "separabilitas fisik".

## 6. Putaran kedua — pengisian penanda dari sumber terverifikasi (24 Oktober 2026)

Atas perintah pemilik, 60 kemunculan penanda diisi/dijawab dan 28 rujukan baru ditambahkan; dokumen dibangun ulang penuh (53 halaman PDF, 596/596 unit sinkron, postcheck 0 error).

**Diisi dengan data nyata (semua DOI diverifikasi Crossref/OpenAlex; fakta RuView dicocokkan langsung ke repositori commit fefb0f9):**
- Teori klasik: Stokoe 2005; Ong-Ranganath 2005; Nyquist 1928 + Shannon 1949; Likert 1932; Cortes-Vapnik 1995; Kiranyaz dkk. 2021; Chow 1970; Bowen dkk. 2009; Sokolova-Lapalme 2009; Mountrakis dkk. 2011; Zheng dkk. 2023; Sigrist dkk. 2013; Zajonc 1965; Bailenson 2021.
- Konteks pembelajaran isyarat: Hassan dkk. 2026 (CHI); Sagawa-Takeuchi 2002 (sistem tutor isyarat Jepang); Daniel dkk. 2024 (umpan balik waktu nyata).
- Indonesia: AUDHI 2024 (SIBI di SLB N Ogan Ilir); Nugraheni dkk. 2023 (SIBI vs BISINDO); Malika-Berlianti 2025; aplikasi SIBI (INTECOMS 2024; Technomedia 2022; Zikky-Akbar 2019; DBESTI 2026); Soekarta dkk. 2024 (deteksi SIBI MediaPipe-Android).
- Laman resmi: Kamus SIBI Digital (SK Mendikbud 0190/P/1994; Surat 868/C/U/95 mewajibkan SLB memakai sistem isyarat baku); rilis Kemenko PMK (URL lengkap).
- Teknis RuView: ADR = *architecture decision record*; ESP32-S3 varian yang direkomendasikan; firmware membatasi 20 ms/frame (maks. 50 fps); mode privasi menekan HR/BR/pose.
- Sistem pembanding (Tabel 2.2 + Subbab 2.3): SignFi (Intel 5300, 3 antena), Wi-SL (Atheros 2TXx3RX, 40 MHz, 400 Hz), HandFi (Intel 5300), WiSign (TP-Link + 2 laptop, tanpa bahasa tertentu), DF-WiSLR (49 gestur), Dwijayanti 2021 = BISINDO (26 huruf + 10 angka).

**Dijawab jujur (tidak ada di literatur — dinyatakan eksplisit, tanpa fabrikasi):** proporsi Indonesia anak tunarungu dari orang tua pendengar; proporsi kosakata Kamus SIBI berbasis lintasan gerak + jumlah kandidat (ditetapkan saat kurasi T1); studi khusus kebutuhan pembelajar pendengar SIBI; orientasi pembelajaran pada kelompok WiFi-SLR; kursus SIBI bagi keluarga. Klaim batas resolusi spasial CSI ditata ulang: fakta perangkat multi-antena + asumsi eksplisit yang diperiksa lewat uji Delta-CSI.

**Rincian lengkap:** `catatan.md` materi bagian 5b; arsip verifikasi JSON di `13-sempro-docx/verifikasi-rujukan-2026-10-24/`.

## 7. Revisi gambar — perbesaran kejelasan (25 Oktober 2026)

Atas perintah pemilik ("terlalu kecil jika dilihat dari dokumen"), kedua diagram dirender ulang dengan tata letak yang sama tetapi lebih padat dan font lebih besar:

| Aspek | Sebelum | Sesudah |
|---|---|---|
| Font teks simpul | 13,5–14 px (±3,2–3,4 pt saat cetak) | 20–26 px (±5,5–7,9 pt saat cetak) |
| Gambar 3.1 | 1560×1420 px kanvas, tinggi cetak 12,7 cm | 1440×2085 px kanvas, tinggi cetak 20,3 cm (memanfaatkan tinggi halaman) |
| Gambar 3.2 | 1660×1060 px, tinggi cetak 8,9 cm | 1300×1480 px, tinggi cetak 15,9 cm |

- Simpul, teks, jalur panah, dan label *gagal/lolos/pelatihan* tetap identik dengan kode Mermaid sumber (`generator/gambar-3.1.mmd`, `gambar-3.2.mmd`).
- **Koreksi kecil kesetiaan sumber:** rel kanan kini hanya mengalir dari S0 ke T5, sesuai kode Mermaid (`S0 --> T5`); versi sebelumnya ikut menggambar sambungan S1 ke rel tersebut padahal `S1` tidak memiliki keluaran di sumber.
- Generator kini memasang pengaman tinggi tampil maksimum 20,6 cm (`MAXH_PX`) agar gambar + keterangan selalu muat satu halaman.
- QA: pemeriksaan overflow otomatis via Playwright (`generator/check_overflow.js`) = 0 overflow pada kedua figur (tiga kotak sempit ditinggikan setelah terdeteksi); inspeksi VLM halaman PDF 29 (G3.1) dan 34 (G3.2) = tampil utuh satu halaman, teks terbaca jelas, keterangan tepat di bawah gambar; postcheck 0 error; sinkron pandoc 596/596 unit; PDF 55 halaman.

## 8. Putaran ketiga — ralat MediaPipe → YOLO26 pose + perbaikan tumpang tindih gambar (25 Oktober 2026)

Atas perintah pemilik ("ralat, aku tidak menggunakan mediapipe tapi yolo26 pose model. revisi gambar dan teks. blok pada gambar terjadi tumpang tindih tolong perbaiki lagi"), dua pekerjaan dilakukan sekaligus. Rincian keputusan isi ada di `catatan.md` materi bagian 5c.

**A. Ralat teks MediaPipe → model pose YOLO26 (11 lokasi di bab, semuanya disunting di `_berkunci/` lalu dinomori ulang):**

| Aspek | Sebelum | Sesudah |
|---|---|---|
| Estimator jalur pelabelan | MediaPipe (Pose, Hands), 33 *landmark* tubuh + 21 per tangan | Model pose YOLO26 terlatih, 17 *keypoint* tubuh format COCO, tanpa *keypoint* jari |
| Rujukan terpakai | [33] MediaPipe, [50] BlazePose, [51] MediaPipe Hands, [52] Kim dkk. | [33] Jocher dkk. 2026 (arXiv:2606.03748, resmi Ultralytics), [51] dok. Ultralytics *Pose*, [52] Sapkota dkk. 2025 (arXiv:2509.25164); MediaPipe tetap [49] hanya sebagai fakta skrip RuView |
| Posisi RuView | "MediaPipe sudah terintegrasi ADR-079 sehingga dipakai yang tersedia" | "Pola ADR-079 diikuti dengan estimator diganti YOLO26; keluaran format sama (17 *keypoint* COCO)" |
| Tabel 3.2 | Baris 3 "...dengan MediaPipe PoseLandmarker"; baris 4 "MediaPipe (Pose, Hands)" | Baris 3 "`collect-ground-truth.py` (ADR-079, diadaptasi)"; baris 4 "Model pose YOLO26 (Ultralytics)" |
| Gambar 3.2 (node) | `MediaPipe` | `Model pose YOLO26` |

- Sebutan MediaPipe yang **sengaja dipertahankan**: fakta repositori RuView (Subbab 2.4, dengan rujukan [49]) dan karya pihak lain (Soekarta dkk. [61] pada Tabel 2.2 + Subbab 2.8). Kalimat *landmark* tangan dihapus karena keluaran YOLO26-pose hanya mencakup tubuh — justru kini selaras dengan batasan cakupan pengenalan (lintasan lengan/tubuh atas/kepala, Subbab 2.3).
- Arsip verifikasi ketiga rujukan baru: `verifikasi-rujukan-2026-10-24/yolo26/`.

**B. Perbaikan tumpang tindih blok pada kedua gambar.** Akar masalah G3.1: *diamond* gerbang dibuat dengan rotasi CSS 45° atas persegi panjang 280×340 sehingga *bounding box* sebenarnya 440×440 — puncak diamond menabrak kotak T/P (±39 px), *diamond* GU menabrak P dan S, dan label "gagal/lolos" jatuh di dalam *diamond*. Perbaikan: *diamond* kini persegi (rotasi = belah ketupat simetris; AABB terkontrol 354 px untuk G, 212 px untuk GU), seluruh kolom/jalur/label disusun ulang di kanvas 1550×2200 (G3.1) dan 1300×1480 (G3.2); pada G3.2 node kolom B digeser agar tidak menempel border panel, koridor putus-putus diberi lajur terpisah, label "pelatihan" dipindah dari atas border panel ke sisi kiri garis.

**QA putaran ini:** pemeriksa geometri deterministik baru `generator/check_layout.js` (luapan teks + irisan blok termasuk *diamond* rotasi + garis menembus blok + batas kanvas + node menempel border panel) = **BERSIH keduanya**; postcheck 0 error; sinkron pandoc 596/596 unit; PDF 55 halaman; spot-check pdftotext: 13 kemunculan YOLO26, 0 kemunculan BlazePose/MediaPipe Hands/humanoid, gambar terpasang benar di halaman 29 (G3.1, rasio 1:1,42) dan 34 (G3.2, 1:1,14). Catatan: inspeksi visual VLM halaman tidak dapat dijalankan putaran ini (layanan visi menjawab 401) — penggantinya, pemeriksaan geometri deterministik atas DOM sumber, justru lebih ketat karena menghitung koordinat pasti dan bukan persepsi gambar.

## 9. Revisi gambar putaran ketiga — gambar dikecilkan, teks diperbesar (26 Oktober 2026)

Atas perintah pemilik ("gambar terlalu besar, teks pada gambar tidak terlihat"), kedua diagram dirender ulang dengan pendekatan berbeda dari putaran 1–2: bukan sekadar menaikkan font, tetapi **mengubah tata letak agar rasio font-terhadap-ukuran-cetak naik drastis**. Akar masalah: kanvas tinggi (2200 px / 1480 px) yang saat dipaskan ke lebar halaman 14 cm menghasilkan teks cetak hanya 5,6–7,9 pt — dan gambar hampir memenuhi satu halaman penuh (19,9 cm / 15,9 cm).

| Aspek | Sebelum (25 Okt) | Sesudah (26 Okt) |
|---|---|---|
| Gambar 3.1 (cetak) | 14×19,9 cm — nyaris 1 halaman penuh | **14×12,8 cm** (−36%) |
| Gambar 3.2 (cetak) | 14×15,9 cm | **14×8,9 cm** (−44%) |
| Teks simpul utama | 26 px → ±6,7 pt | 32 px → **±8,1 pt** |
| Teks gerbang | 20–22 px → ±5,6 pt | 28–32 px → **±7,1–8,1 pt** |
| Teks sekunder (P/S/label) | 21–25 px → ±5,9 pt | 28–30 px → **±7,1–7,6 pt** |

Keputusan desain:

- **Gerbang digambar heksagon datar, bukan belah ketupat** (G0–G4, G0U, G1U). Belah ketupat membuang ±50% kotaknya untuk teks, sehingga kriteria gerbang yang panjang (74 karakter) memaksa kanvas sangat tinggi. Heksagon (bentuk baku "gerbang/persiapan" pada bagan alur) menyisakan ±84% kotak untuk teks — kanvas langsung memendek. Pembeda visual gerbang vs proses tetap terjaga (heksagon abu-abu vs kotak putih; simpul temuan abu-abu tua; T5 final bercetak tebal).
- **Gambar 3.2 disusun alur ular (snake) dua kolom per panel**: kolom 1 turun (TX→ZI→RX→CSI), kolom 2 naik dari dasar (SEG→FIT→KLS→UB) sehingga panel menjadi lebar-rendah; panel pelabelan serupa (KP→LBL→DS dan CAM→YOLO26→KEY→VER, dasar DS sejajar VER). DIAG pindah ke kiri-bawah, SYN kanan-bawah, dekat node yang bersambungan dengannya.
- Simpul, teks, jalur, dan label *lolos/gagal/pelatihan* **tetap identik** dengan kode Mermaid sumber; ralat YOLO26 dipertahankan; rel kanan tetap hanya S0→T5.
- Tautan bantu putus-putus diberi lajur tetap (x14, x385, x650, x745, x790, x1025, x1552). Dua **persilangan bersih 90° antartautan bantu** (SEG→DS dan DS→KLS masing-masing × KEY→DIAG di y406) tidak terhindarkan secara topologis pada kanvas ringkas — keduanya garis bantu bergaya sama dan tetap terbaca.

**QA putaran ini:** pemeriksa geometri deterministik `check_layout.js` diperluas (dukungan heksagon `clip-path`) = **BERSIH keduanya** (0 luapan, 0 irisan, 0 garis menembus, 0 di luar kanvas); postcheck 0 error; sinkron pandoc 596/596 unit; PDF 52 halaman (turun dari 55); gambar terpasang 14,0×12,8 cm (hlm 28) dan 14,0×8,9 cm (hlm 32); inspeksi visual VLM kedua halaman = teks terbaca jelas, tidak ada tumpang tindih, ukuran proporsional tidak memenuhi halaman.
