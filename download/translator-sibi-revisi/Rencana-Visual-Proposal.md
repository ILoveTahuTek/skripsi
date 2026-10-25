# Rencana Visual Proposal — Purwarupa Penerjemah Dua Arah SIBI Berbasis Wi-Fi CSI

Dokumen ini merencanakan penyebaran ilustrasi ilmiah pada proposal revisi (`Proposal-Revisi-Translator-SIBI.md`). Rencana disusun agar visual tersebar proporsional ke seluruh bab, tidak menumpuk pada satu bab sebagaimana pada proposal lama yang menempatkan seluruh diagram hanya di BAB III.

## 1. Prinsip perencanaan visual

Setiap visual harus memenuhi lima syarat berikut. Pertama, dirujuk di dalam teks dengan nomor gambar (misalnya "seperti ditunjukkan pada Gambar 3.2") sebelum atau sesudah gambar muncul. Kedua, memiliki keterangan gambar (caption) di bawah gambar dengan penomoran `<bab>.<urutan>` yang dimulai ulang pada setiap bab. Ketiga, isi diagram konsisten dengan arsitektur yang dipakai di seluruh proposal: modul ESP32-S3 tanpa kamera untuk produk akhir, kamera dan YOLO26-Pose hanya pada jalur pelabelan riset. Keempat, klaim teknis di dalam diagram (jumlah subcarrier, laju CSI, ukuran memori, dukungan bahasa) berasal dari sumber yang sama dengan klaim di teks dan tercantum pada `Matriks-Literatur-dan-Bukti.md`. Kelima, sumber diagram disediakan dalam format sunting (editable) Mermaid sehingga dapat diubah tanpa menggambar ulang.

## 2. Alokasi visual per bab

| No. | Kode | Judul | Lokasi (bab.subbab) | Tipe diagram | Isi ringkas | Sumber klaim utama |
|---|---|---|---|---|---|---|
| 1 | G1.1 | Peta masalah dan kesenjangan penelitian | 1.1 | Diagram alur 3 lapis | Masalah komunikasi dua arah tunarungu-pendengar bercabang menjadi empat kesenjangan, lalu bertemu pada posisi penelitian | Klaim 1.1 (jumlah juru bahasa, keterbatasan aplikasi, keterbatasan kamera, celah CSI-SIBI) |
| 2 | G1.2 | Visi purwarupa penerjemah dua arah tanpa kamera | 1.1 (paragraf penutup corong) | Skema dua arah | Modul TX, zona isyarat, modul RX berinferensi, server lokal (TTS/ASR/pemetaan), speaker/mikrofon/layar | Arsitektur yang dirancang (Subbab 3.5) |
| 3 | G2.1 | Taksonomi pengenalan isyarat dan translasi SIBI | 2.2 | Pohon taksonomi | Tiga kelompok pengenalan (sensor terpasang, visi, Wi-Fi CSI termasuk ESP32) dan tiga tingkat translasi balik (kamus kata-level, ejaan jari, SLMT penuh) | Subbab 2.2 dan 2.8 |
| 4 | G2.2 | Alur arah pertama: SIBI menjadi teks dan suara | 2.7 | Pipa proses (pipeline) | ESP-NOW → CSI 56 subcarrier HT20 ≤ 50 fps → segmentasi energi → fitur → inferensi int8 → label → UDP → kamus label → TTS → speaker | Subbab 2.4, 2.6, 2.7; T17-R2 |
| 5 | G2.3 | Alur arah kedua: teks/ucapan menjadi representasi SIBI | 2.8 | Diagram alur bercabang | Dua pintu masuk (teks, suara), ASR faster-whisper, normalisasi, kamus isyarat, cabang tampil versus ejaan jari | Subbab 2.7, 2.8; T17-R3 |
| 6 | G3.1 | Alur pelatihan CSI dengan YOLO26-Pose sebagai alat bantu | 3.2 | Diagram alur bergerbang | T0-T5 dengan gerbang G0-G4; T2 memuat kartu pemandu + webcam + YOLO26 17 keypoint COCO yang disinkronkan dengan CSI; kuantisasi dan uji deploy | Subbab 3.2; evolusi Gambar 3.1 lama |
| 7 | G3.2 | Arsitektur produk akhir tanpa kamera | 3.5.1 | Diagram arsitektur dua subgraf + jalur pelabelan putus-putus | Dua arah resmi pada modul dan server; jalur kamera-YOLO26 digambar terpisah dan hanya aktif saat riset | Subbab 3.5.1; evolusi Gambar 3.2 lama |
| 8 | G3.3 | Topologi perangkat, komunikasi antarmodul, dan server | 3.5.2 | Diagram topologi jaringan | Modul A/B/C, AP satu kanal (router/hotspot laptop), server lokal (RuView + ASR + TTS + kamus), cloud jarak jauh sebagai alternatif putus-putus | T17-R2 (koeksistensi radio); Subbab 3.5.2 |
| 9 | G3.4 | Inferensi langsung pada ESP32-S3 | 3.7.7 | Pipa proses tepi (edge) | Callback CSI promiscuous → penyangga PSRAM → segmentasi → fitur → model int8 TFLM/ESP-DL → ambang keyakinan → label; catatan batas perangkat | T17-R2 (datasheet, ESP-NN, ESP-DL) |
| 10 | G3.5 | Alur dataset, eksperimen, evaluasi, dan deployment | 3.8 | Rantai artefak | Perekaman → penyaringan segmen → dataset → 5 skema pembagian → metrik → kuantisasi/deployment → uji operasional + cakupan kamus → uji kegunaan → laporan | Subbab 3.6-3.8 |

Sebaran akhir: BAB I memuat dua gambar (G1.1, G1.2), BAB II memuat tiga gambar (G2.1, G2.2, G2.3), dan BAB III memuat lima gambar (G3.1-G3.5). Rasio ini sepadan dengan bobot tiap bab: BAB III memang bab metode yang paling padat rancangan, tetapi BAB I dan II kini ikut membawa beban visual alih-alih kosong sebagaimana proposal lama.

## 3. Konvensi penomoran dan keterangan

Penomoran gambar mengikuti pola `<bab>.<urutan>` dan dimulai ulang pada setiap bab. Keterangan gambar ditulis di bawah gambar dengan pola `Gambar X.Y Judul ringkat`, sedangkan keterangan tabel berada di atas tabel dengan pola `Tabel X.Y Judul ringkat`. Setiap gambar dirujuk sekurang-kurangnya satu kali dari teks dengan pola korpus: "seperti ditunjukkan pada Gambar X.Y", "Gambar X.Y memperlihatkan ...", atau "... dapat dilihat pada Gambar X.Y". Tidak ada gambar yang dirujuk dengan frasa "gambar di bawah ini".

## 4. Konvensi diagram Mermaid

Seluruh sumber diagram disimpan sebagai berkas `.mmd` pada folder `diagram/` dengan penamaan `G<bab>.<urutan>-<slug>.mmd`. Konvensi yang dipakai: arah alur proses memakai `flowchart LR` (kiri ke kanan) dan struktur bertingkat memakai `flowchart TD` (atas ke bawah); setiap simpul diberi pengenal singkat dan label berbahasa Indonesia dengan pemisah baris `<br/>`; jalur resmi produk digambar dengan garis penuh, sedangkan jalur pelabelan riset dan alternatif (cloud jarak jauh, distilasi) digambar dengan garis putus-putus agar perbedaan perannya terbaca sekilas. Keputusan memakai garis putus-putus untuk jalur riset penting karena kesalahpahaman "kamera masih dipakai produk akhir" adalah risiko komunikasi utama proposal ini.

## 5. Cara menyunting dan merender

Diagram dapat disunting langsung pada berkas `.mmd` atau melalui penyunting daring Mermaid Live Editor (mermaid.live). Untuk merender menjadi SVG dari baris perintah, gunakan `mmdc -i <berkas>.mmd -o <keluaran>.svg`; seluruh sepuluh berkas telah lolos validasi sintaks dengan `mmdc` pada 25 Oktober 2026. Apabila kelak diagram perlu dilekatkan ke dokumen DOCX cetak, pelajaran sesi sebelumnya pada proyek ini berlaku: keluaran `mmdc` arah TD cenderung terlalu tinggi untuk satu halaman (rasio lebar:tinggi tidak sesuai halaman A4), sehingga tahap pengemasan DOCX sebaiknya menggambar ulang figur dengan HTML/CSS dan Playwright pada rasio halaman, dengan isi simpul, jalur, dan label yang identik dengan sumber `.mmd`; berkas `.mmd` tetap menjadi sumber kebenaran yang dapat diaudit.

## 6. Daftar berkas sumber

```
diagram/
├── G1.1-peta-masalah.mmd
├── G1.2-visi-purwarupa.mmd
├── G2.1-taksonomi.mmd
├── G2.2-alur-arah1.mmd
├── G2.3-alur-arah2.mmd
├── G3.1-alur-pelatihan.mmd
├── G3.2-arsitektur-akhir.mmd
├── G3.3-topologi-jaringan.mmd
├── G3.4-inferensi-tepi.mmd
└── G3.5-alur-dataset-evaluasi.mmd
```

## 7. Visual yang sengaja tidak dibuat

Tiga kandidat visual sengaja tidak dibuat agar jumlah tetap pada rentang sasaran 8-10 dan agar setiap gambar benar-benar memikul beban argumen. Pertama, tangkapan layar produk cloud (misalnya konsol Google Cloud atau Azure) tidak dibuat karena prototipe memakai server lokal dan penampilan antarmuka pihak ketiga dapat berubah. Kedua, diagram alur data latih-versi-uji terperinci per lapisan jaringan saraf tidak dibuat karena arsitektur model masih menjadi parameter rancangan yang ditetapkan pada T2 (Tabel 3.6). Ketiga, gambar teknis dimensi fisik modul (ukuran baterai, penempatan layar) tidak dibuat karena dimensi fisik merupakan keputusan perangkat keras yang belum ditetapkan pemilik penelitian; menetapkannya sekarang berisiko fabrikasi spesifikasi.
