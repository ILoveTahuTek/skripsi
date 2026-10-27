# Laporan Audit dan Rencana Redesain Diagram — Proposal Penerjemah Dua Arah SIBI

**Dokumen sasaran:** `Proposal-Penerjemah-Dua-Arah-SIBI-CSI-ESP32S3.docx` (66 halaman, BAB I–III + Daftar Pustaka)
**Pemicu:** dua gambar contoh dari pemilik (Gambar 3.1 dan 3.2) sebagai contoh masalah keterbacaan dan kepadatan informasi; audit diperluas ke seluruh diagram dalam dokumen.
**Disusun:** 27 Oktober 2026 · Metode pengukuran: render SVG per sumber (mmdc 12.0.0), parse `viewBox` + `font-size`, konversi ke ukuran cetak pada lebar konten 14 cm (= 396,85 pt), dengan pemangkasan tinggi tampil 20,6 cm yang berlaku di generator DOCX.

---

## 1. Hasil pengukuran kondisi eksisting (fakta terukur)

Seluruh angka = ukuran cetak sebenarnya ketika gambar disematkan selebar konten 14 cm (margin 4-3-3-3). huruf "min" = label sisi; "maks" = teks simpul.

| Gambar | Isi | Kanvas (px logis) | Aspek | Huruf cetak | Vonis terhadap target 9–11 pt |
|---|---|---|---|---|---|
| 3.1 | Tahapan T0–T5 + gerbang (varian 3 kolom, 21 simpul) | 1260×2163 | 1,72 | **3,2–4,8 pt**; tinggi 24,9 cm → terpangkas, lebar tampil tinggal 12,0 cm | GAGAL — terburuk |
| 3.2 | Alur guru–murid (2 kolom, 13 simpul) | 1104×1540 | 1,39 | **4,3–5,8 pt** | GAGAL |
| 3.3 | Arsitektur akhir (3 subgraf, 16 simpul) | 1360×1324 | 0,97 | **3,5–4,7 pt** | GAGAL |
| 3.4 | Topologi jaringan (10 simpul) | 986×1067 | 1,08 | **4,8–6,4 pt** | GAGAL |
| 3.5 | Inferensi tepi (9 simpul + catatan) | 744×810 | 1,09 | **6,4–8,5 pt** | GAGAL (terbaik, masih di bawah target) |
| 3.6 | Dataset–pelatihan–evaluasi (3 kolom, 12 simpul) | 898×904 | 1,01 | **5,3–7,1 pt** | GAGAL |

**Diagnosis akar masalah.** (1) Keenam diagram memuat terlalu banyak simpul dan keputusan untuk satu figur sehingga skala turun jauh di bawah 9 pt; (2) uraian panjang (2–3 baris, 30–40 karakter per baris) ditempatkan di dalam simpul; (3) memperbesar huruf tanpa mengubah struktur tidak menolong karena kanvas ikut membesar secara proporsional — ukuran cetak efektif hampir konstan per struktur. Solusinya wajib struktural: memecah pada batas logis, memendek teks simpul, dan menaikkan huruf sumber pada konfigurasi bersama.

## 2. Daftar audit per figur (Tahap A)

### Gambar 3.1 — "Tahapan penelitian T0–T5 dengan gerbang keputusan G0–G4"
1. **Lokasi:** BAB III, Subbab 3.2 (hlm. 31 pada PDF pratinjau).
2. **Tujuan komunikasi:** memetakan kronologi enam tahap penelitian (T0–T5) dan lima gerbang keputusan (G0–G4) sebagai kerangka metodologi bergerbang.
3. **Informasi inti:** urutan T0→T5 dengan bulan (M1–M14); posisi dan kriteria tiap gerbang; jalur lolos; jalur gagal: tindakan korektif (P0–P4), uji ulang (G0U/G1U), dan terminal (S0, S1, kembali ke T5).
4. **Masalah:** 21 simpul + 20 sisi dalam satu figur; kriteria gerbang 3 baris menumpuk di dalam belah ketupat; dua tujuan komunikasi berbeda (kronologi tahapan vs logika remediasi kegagalan) dipaksakan menjadi satu; aspek 1,72 memicu pemangkasan tinggi sehingga lebar tampil menyusut.
5. **Kompleksitas:** tinggi (21 simpul, 5 jalur remediasi).
6. **Rekomendasi:** **pecah** pada batas "jalur keberhasilan utama" vs "jalur gagal dan remediasi" (master prompt §7 butir 1–4).
7. **Nomor/judul baru:** 3.1 "Tahapan penelitian T0–T5 dan gerbang keputusan G0–G4 (jalur utama)"; 3.2 (baru) "Jalur gagal dan remediasi gerbang keputusan G0–G4".

### Gambar 3.2 — "Alur pelatihan guru–murid dari perekaman tersinkron hingga deployment"
1. **Lokasi:** BAB III, Subbab 3.2.3 (hlm. 34).
2. **Tujuan komunikasi:** menjelaskan metodologi utama distilasi guru–murid dari perekaman tersinkron hingga model terpasang di modul.
3. **Informasi inti:** perekaman video+CSI+label satu penanda waktu; pelatihan lanjutan guru YOLO26-Pose di Kaggle dengan loop kualitas *keypoint*; ekstraksi deret *keypoint* (17 COCO); penyandingan berbasis waktu; loop cakupan data; *dataset* murid (jendela CSI + label + pose guru); pelatihan murid 1D-CNN dengan suku supervisi guru; dua pembanding (SVM, murid ablasi); gerbang kinerja G2/G3 dengan loop tindakan Tabel 3.4; kuantisasi int8; deployment ke modul penerima; perangkat akhir tanpa kamera.
4. **Masalah:** 13 simpul + 3 siklus umpan balik bertingkat dalam satu figur; teks simpul 3 baris; dua tujuan komunikasi (akuisisi-penyandingan data vs pelatihan-optimasi-deployment) bercampur; saling silang sisi loop memaksa kanvas lebar.
5. **Kompleksitas:** tinggi (13 simpul, 3 loop, 1 cabang pembanding).
6. **Rekomendasi:** **pecah** pada batas keluaran gerbang kualitas data ("ya" pada DQ) — sesuai opsi pemisahan master prompt §7 (akuisisi & penyandingan multimodal vs pelatihan murid & deployment).
7. **Nomor/judul baru:** 3.3 "Distilasi guru–murid (I): perekaman tersinkron, model guru, dan penyandingan waktu"; 3.4 "Distilasi guru–murid (II): pelatihan murid CSI, pembanding, dan deployment".

### Gambar 3.3 — "Arsitektur produk akhir tanpa kamera"
1. **Lokasi:** BAB III, Subbab 3.5.1 (hlm. 39).
2. **Tujuan komunikasi:** menunjukkan dua jalur operasional dua arah (isyarat→teks/suara; ucapan→representasi SIBI) plus jalur guru dan cadangan lokal.
3. **Informasi inti:** seluruh 16 simpul dan 11 sisi (termasuk 2 sisi putus-putus cadangan lokal) — tidak ada yang boleh hilang.
4. **Masalah:** struktur sudah sehat (aspek 0,97; tanpa tumpang tindih) tetapi teks simpul panjang (3 baris) sehingga huruf cetak hanya 3,5–4,7 pt.
5. **Kompleksitas:** sedang.
6. **Rekomendasi:** **rapikan + susun ulang**: susun tiga subgraf sebagai tiga kolom vertikal sejajar (arah 1 | arah 2 | guru) dengan server lokal di bawah; teks simpul dipadatkan 1–2 baris tanpa menghilangkan istilah teknis (rincian sudah utuh di prosa §3.5.1); huruf sumber 24–26 px.
7. **Nomor/judul baru:** 3.5 (judul tetap).

### Gambar 3.4 — "Topologi perangkat, komunikasi antarmodul, layanan awan, dan server"
1. **Lokasi:** BAB III, Subbab 3.5.2 (hlm. 40).
2. **Tujuan komunikasi:** penempatan jaringan: 2–3 modul, AP satu kanal berinternet, layanan awan (utama), server lokal (riset/cadangan).
3. **Informasi inti:** seluruh 10 simpul, 4 kelompok, 7 sisi (termasuk sisi putus-putus riset/cadangan).
4. **Masalah:** struktur TB sudah tepat; teks simpul terlalu panjang; huruf 4,8–6,4 pt.
5. **Kompleksitas:** rendah–sedang.
6. **Rekomendasi:** **rapikan** (struktur dipertahankan; teks dipadatkan; huruf sumber 24 px).
7. **Nomor/judul baru:** 3.6 (judul tetap).

### Gambar 3.5 — "Inferensi langsung pada ESP32-S3"
1. **Lokasi:** BAB III, Subbab 3.7.8 (hlm. 47).
2. **Tujuan komunikasi:** alur inferensi perangkat: callback CSI → penyangga geser → segmentasi → fitur → model int8 → ambang penolakan → UDP.
3. **Informasi inti:** 8 simpul alur + cabang ya/tidak ambang; batas perangkat pada simpul NOTE **sudah terdokumentasi penuh di BAB II dengan sitasi [29]** (SRAM 512 KB, PSRAM hingga 8 MB, LX7 240 MHz, 1T1R) sehingga NOTE merupakan duplikasi; kewajiban satu kanal + WIFI_PS_NONE belum ada di prosa dan akan dipindah ke §3.7.8 dengan sitasi [28].
4. **Masalah:** simpul NOTE 5 baris menggembungkan baris kedua; huruf 6,4–8,5 pt.
5. **Kompleksitas:** rendah.
6. **Rekomendasi:** **rapikan**: hapus NOTE (info pindah ke prosa + sitasi), pola ular 2 baris dipertahankan, huruf sumber 26 px.
7. **Nomor/judul baru:** 3.7 (judul tetap).

### Gambar 3.6 — "Alur dataset, pelatihan guru–murid, evaluasi, dan deployment"
1. **Lokasi:** BAB III, Subbab 3.8 (hlm. 48).
2. **Tujuan komunikasi:** rantai evaluasi: dari data terlatih hingga artefak akhir.
3. **Informasi inti:** 12 simpul: perekaman→penyaringan→guru→dataset murid→murid+pembanding (rantai ini **duplikat** Gambar 3.2/skema distilasi) lalu 5 skema pembagian, metrik, deployment, uji operasional, cakupan kamus arah 2, uji kegunaan, artefak.
4. **Masalah:** separuh kiri mengulang konten Gambar 3.2 (dua sumber kebenaran untuk proses yang sama dalam satu bab); varian 3 kolom juga menggabungkan dua sisi (DEP→OP dan DEP→COVER) menjadi satu sisi klaster — generalisasi yang sebelumnya didokumentasikan sebagai pengecualian.
5. **Kompleksitas:** sedang–tinggi.
6. **Rekomendasi:** **gabungkan secara logis + susun ulang**: fokuskan figur pada rantai evaluasi (mulai dari "model guru, murid, dan pembanding terlatih (Gambar 3.4)"); rantai perekaman–pelatihan tidak dihapus dari dokumen karena sudah diwakili Gambar 3.3–3.4; akibatnya sisi DEP→OP/DEP→COVER dapat digambar utuh sebagai sisi simpul (tanpa generalisasi klaster).
7. **Nomor/judul baru:** 3.8 "Alur evaluasi: pembagian data, metrik, uji operasional, uji kegunaan, dan artefak".

### Visual di luar naskah (inventaris lengkap, tidak diubah)
- `G1.1-peta-masalah`, `G1.2-visi-purwarupa`, `G2.1-taksonomi`, `G2.2-alur-arah1`, `G2.3-alur-arah2` — berkas konteks bacaan di `translator-sibi-draft/diagram/`, sengaja tidak dimuat di naskah (keputusan pemilik, revisi sesi 1). Status: **dipertahankan apa adanya**.
- `Peta-Literatur-Titik-Temu` (translator-sibi-literatur) — dokumen pendamping mandiri, bukan bagian naskah. Status: di luar lingkup.
- Proposal DPJ-4 lama (alat pembelajaran, `sempro-dpj4-sibi-csi`) — dokumen lain dengan 2 gambar yang sudah direvisi putaran ketiga. Status: di luar lingkup audit ini.

## 3. Rencana arsitektur figur baru (Tahap B)

Hierarki: L1 = peta besar; L2 = proses/subsistem; L3 = detail teknis.

| Baru | Level | Tujuan tunggal (paham 5–10 detik) | Isi (semua simpul/sisi sumber terwakili) | Keterkaitan |
|---|---|---|---|---|
| 3.1 Tahapan T0–T5 dan gerbang G0–G4 (jalur utama) | L1 | Kronologi 6 tahap + posisi 5 gerbang, jalur lolos | 12 simpul (T0–T5, T2B, G0–G4), sisi "lolos"; kriteria gerbang diringkas 2–3 baris | Gagal → ke 3.2; detail tiap tahap = §3.2.1–3.2.5 |
| 3.2 Jalur gagal dan remediasi gerbang G0–G4 (BARU) | L3 | Apa yang terjadi bila gerbang gagal: aksi, uji ulang, terminal | 5 baris remediasi: P0–P4, G0U, G1U, S0, S1, T2B/T4/T5 sebagai keluaran berlabel | Rujuk balik 3.1; tindakan = Tabel 3.6 |
| 3.3 Distilasi (I): perekaman, guru, penyandingan (BARU) | L2 | Data multimodal tersinkron + pemeriksaan kualitas guru | REC, TT, TQ (loop), Y26, PAIR, DQ (loop) | "ya" → 3.4; detail = §3.6, §3.7.4 |
| 3.4 Distilasi (II): pelatihan murid hingga deployment (BARU) | L2 | Murid 1D-CNN + pembanding + gerbang kinerja → modul | SD, STU, BASE, EQ (loop), OPT, DEP, DEV | Datanya dari 3.3; DEV → 3.5 |
| 3.5 Arsitektur produk akhir tanpa kamera | L2 | Dua jalur operasional + jalur guru + cadangan lokal | 16 simpul, 11 sisi (utuh) | Murid int8 dari 3.4; kabel jaringan = 3.6 |
| 3.6 Topologi modul dan jaringan | L2 | Siapa tersambung ke apa, lewat mana | 10 simpul, 4 kelompok, 7 sisi (utuh) | Peran tiap jalur = 3.5 |
| 3.7 Inferensi langsung pada ESP32-S3 | L3 | Alur inferensi per segmen + ambang penolakan | 8 simpul alur (NOTE pindah ke prosa) | Model dari 3.4; batas perangkat = §2.2 [29] |
| 3.8 Alur evaluasi hingga artefak | L2 | Dari model terpilih ke laporan kelayakan | 9 simpul evaluasi (rantai pelatihan dirujuk ke 3.3–3.4) | Metrik = §3.8.1–3.8.4; gerbang = 3.1–3.2 |

**Sistem desain bersama (satu untuk semua figur):**
- Sumber: Mermaid `flowchart` (dapat diedit, tervalidasi mmdc 12.0.0); satu berkas `.mmd` per figur di `translator-sibi-draft/diagram/` — **sumber tunggal** untuk naskah markdown dan DOCX (menghapus lapisan varian docx sebelumnya).
- Huruf: `themeVariables.fontSize` 22–26 px per kebutuhan figur; label sisi dinaikkan lewat `themeCSS` agar ≥ 9 pt cetak; keluarga huruf Arial/Helvetica (sans-serif netral, konsisten antarfigur, aman grayscale).
- Tema: `neutral` (abu-abu netral — lulus cetak grayscale; status tidak bergantung warna saja; bentuk bermakna: persegi = proses, belah ketupat = keputusan, putus-putus = jalur cadangan/pengecualian).
- Arah alur: atas-ke-bawah untuk tahapan/keputusan; kiri-ke-kanan untuk alur data per baris; pola ular dua baris untuk rantai panjang.
- Target terukur: huruf efektif ≥ 9 pt (ideal 9–11 pt) pada 14 cm; aspek ≤ 1,45 agar tidak terpangkas; seluruh simpul/sisi sumber terverifikasi terwakili (pemeriksa integritas otomatis).
- Label keputusan eksplisit: "lolos/gagal", "ya/tidak", "belum" — dipertahankan dari sumber.

**Integritas ilmiah (wajib):** tidak ada simpul, cabang, kondisi gerbang, loop umpan balik, pembanding, atau terminologi yang dihapus; pemisahan/penggabungan hanya memindahkan lokasi informasi dan dicatat satu per satu pada Bagian 6. Nilai, ambang, nama model (YOLO26-Pose, 1D-CNN, SVM, TFLM/ESP-DL), sitasi Subbab, dan nomor Tabel dipertahankan verbatim.

## 4. Catatan kesesuaian diagram ↔ prosa (temuan audit)
1. **Duplikasi konten Gambar 3.6 vs 3.2** (rantai perekaman–pelatihan muncul dua kali) — diselesaikan dengan fokus evaluasi + rujukan silang eksplisit. *Dokumentasikan ke pembimbing: perubahan penyajian, bukan perubahan metode.*
2. **Simpul S1 pada 3.1 lama adalah simpul terminal tanpa sisi keluar** (sesuai sumber Mermaid asli sejak Task 15) — dipertahankan sebagai terminal pada 3.2 baru; bila pembimbing menghendaki kelanjutan S1 (mis. lanjut T2 dengan cakupan kurang), itu keputusan metodologi baru di luar kewenangan redesain.
3. **Node DEV pada distilasi merujuk "(Gambar 3.3)"** — nomor diperbarui mengikuti penomoran baru.
4. Tidak ditemukan kontradiksi logika lain antara diagram dan uraian §3.2, §3.5, §3.7, §3.8.

---

## 5. Hasil akhir redesain (realisasi 27 Oktober 2026)

Seluruh rencana Bagian 3 terealisasi. Sumber tunggal `translator-sibi-draft/diagram/G3.1–G3.8-*.mmd` (Mermaid); sumber lama diarsip `diagram/lama-20261026/` (termasuk nama-nama lama). Konfigurasi desain bersama `scripts/translator-sibi-docx/diagram-docx/config-24.json`.

| Gambar | Kanvas (px logis) | Aspek | Huruf cetak | Sebelum | Vonis |
|---|---|---|---|---|---|
| 3.1 Tahapan (jalur lolos) | 924×950 | 1,03 | **10,3 pt** | 3,2–4,8 pt | lolos |
| 3.2 Remediasi gerbang (baru) | 997×1334 | 1,34 | **9,5 pt** | — | lolos |
| 3.3 Distilasi I (data & guru) | 1039×886 | 0,85 | **9,2 pt** | 4,3–5,8 pt | lolos |
| 3.4 Distilasi II (murid & deployment) | 987×1230 | 1,25 | **9,6 pt** | — | lolos |
| 3.5 Arsitektur akhir | 1016×1136 | 1,12 | **9,4 pt** | 3,5–4,7 pt | lolos |
| 3.6 Topologi jaringan | 1035×1356 | 1,31 | **9,2 pt** | 4,8–6,4 pt | lolos |
| 3.7 Inferensi tepi | 930×690 | 0,74 | **10,2 pt** | 6,4–8,5 pt | lolos |
| 3.8 Alur evaluasi | 809×1072 | 1,32 | **11,8 pt** | 5,3–7,1 pt | lolos |

**Validasi tumpuan (semua lolos):**
- `cek_integritas.py` — 76 simpul & 64 sisi keenam sumber lama seluruhnya terwakili di figur baru atau terdokumentasi transformasinya (kompresi notasi uji-ulang → label sisi; pemindahan S0/S1/NOTE → prosa/caption).
- `bangun_diagram.py` — huruf efektif ≥ 9,2 pt dan aspek ≤ 1,34 pada seluruh 8 figur (bebas pemangkasan 20,6 cm).
- `rakit_draft.py` — LOLOS 13 OK / 0 galat (8 blok mermaid, 8 caption urut, semua gambar dirujuk prosa, 80 rujukan utuh).
- `qa_ekspor.py` pada PDF ekspor — 8 gambar di hlm. 31, 32, 34, 35, 40, 42, 49, 50; semuanya 14,0 cm selebar konten; 16 pemeriksaan caption/rujukan silang/teks-lama-hilang: semua OK.
- `postcheck.py` (skill docx) — 0 galat; 1 peringatan lama yang sudah diterima (spasi sel tabel).

**Catatan keputusan akhir:**
1. Gerbang pada 3.1 digambar sudut-membulat (bukan belah ketupat) karena pada figur ini gerbang belum bercabang — seluruh percabangan lolos/gagal dirinci 3.2; makna keputusan tetap tegas lewat label.
2. Lingkaran keluaran pada 3.2: kosong = lanjut ke tahap tujuan (label sisi); "temuan" = penelitian berlanjut dengan hasil dilaporkan. Rincian S0/S1 dipindah ke prosa §3.2.
3. Kesesuaian diagram↔prosa Bagian 4 butir 1–3 terselesaikan; butir 2 (S1 terminal tanpa keluaran) dipertahankan sesuai sumber dan kini tercatat eksplisit pada caption/prosa.
