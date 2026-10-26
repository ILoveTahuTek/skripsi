# -*- coding: utf-8 -*-
"""Bagian tetap dossier bahan Translator SIBI (tidak dimutasi GEPA).

Seluruh angka dan klaim di sini disalin dari deliverable Task 17
(Matriks-Literatur-dan-Bukti.md, Proposal-Revisi-Translator-SIBI.md,
Audit-Arsitektur-Translator-SIBI.md) dan dossier lama DPJ-4 yang masih
relevan. Nomor [n] mengikuti Daftar Pustaka Proposal-Revisi (79 entri).
"""

HEADER = """# Dossier Bahan Penyusunan Proposal — Purwarupa Penerjemah Dua Arah SIBI (Topik Diperbarui)

**Dokumen kerja internal pengumpul bahan** — penerus `DPJ-4_Bahan-Proposal-SIBI.md` (23 Oktober 2026) yang masih mengacu topik lama (alat latihan satu arah bagi pembelajar pendengar).
Disusun: 26 Oktober 2026 · Basis: `Proposal-Revisi-Translator-SIBI.md` + `Audit-Arsitektur-Translator-SIBI.md` + `Matriks-Literatur-dan-Bukti.md` + catatan riset `riset-translator-sibi/` (Task 17, 24–25 Oktober 2026).

> **Status keputusan pemilik yang tercatat (visi produk terbaru):**
> 1. Produk berupa purwarupa penerjemah dua arah yang portabel berbasis 2–3 modul ESP32-S3; setiap modul direncanakan memiliki layar kecil, baterai, *speaker*, dan mikrofon.
> 2. Arah pertama: Sistem Isyarat Bahasa Indonesia (SIBI) menjadi teks dan suara Bahasa Indonesia — pengenalan isyarat lewat Wi-Fi *channel state information* (CSI) dengan inferensi berjalan langsung pada modul, hasil dikirim ke server untuk dijadikan teks dan disuarakan sintesis ucapan (*text-to-speech*, TTS).
> 3. Arah kedua: ucapan atau teks Indonesia menjadi representasi SIBI pada layar modul — ucapan dikenali pengenal ucapan otomatis (*automatic speech recognition*, ASR) di server, teks dipetakan ke kamus kata-level dengan *fallback* ejaan jari.
> 4. Model pose YOLO26 hanya dipakai pada tahap riset (pelabelan, ekstraksi informasi gerakan, pembentukan *ground truth*); produk akhir tidak memakai kamera maupun citra, dan modul tidak menjalankan model visi.
> 5. Laptop ASUS TUF Dash F15 FX516PR (Intel Core i7-11370H, RTX 3070 Laptop 8 GB VRAM, RAM 16 GB) menjadi mesin pengembangan, pelatihan, dan server lokal prototipe; layanan *cloud* jarak jauh dibedakan tegas dan tidak diuji pada prototipe.
> 6. Draf `Proposal-Revisi-Translator-SIBI.md` **tidak ditulis ulang** — dossier ini adalah bahan kerja bagi pemilik untuk menulis, menyesuaikan, atau membela naskahnya sendiri.

---

"""

BANK_FAKTA = """
## 3. Bank Fakta Siap Kutip

Nomor dalam kurung siku merujuk Daftar Pustaka `Proposal-Revisi-Translator-SIBI.md`. Status **DV** = terverifikasi (sumber dilihat langsung, 24–25 Oktober 2026, jejak pada `Matriks-Literatur-dan-Bukti.md`); **EST** = estimasi internal yang selalu dilabeli demikian bila dipakai; **XT** = tidak layak kutip (jangan dipakai).

| Kunci | Inti siap tulis | Sumber | Status |
|---|---|---|---|
| F1 orang-tua-pendengar | 90–95% anak tunarungu lahir dari orang tua pendengar (data siswa AS); mengbantah mitos "10% orang tua tuli". Angka Indonesia belum ditemukan pada penelusuran hingga Okt 2026 — ditulis terbuka di naskah | [1], [2] | DV |
| F2 dukungan-belajar | Orang tua pendengar yang belajar isyarat membutuhkan dukungan terstruktur | [3] | DV |
| F3 hambatan-praktis | Orang tua DHH menghadapi hambatan praktis navigasi belajar isyarat | [4] | DV |
| F4 juru-bahasa | Sekitar 500 juru bahasa isyarat untuk sekitar 1,92 juta penyandang tunarungu (±1 : 3.840) | [5] | DV |
| F5 landasan-hukum | UU No. 8/2016 mengakui bahasa isyarat dan mewajibkan aksesibilitas komunikasi | [6] | DV |
| F6 peta-BRIN | BISINDO 77,7%; SIBI 1,9%; campuran 14,9%; lainnya 5,6% — survei daring purposive 26 provinsi (bukan nasional); keterbatasan sampel wajib disebut saat angka dipakai | [8] | DV |
| F7 survei-Mursita | 91% dari 100 responden tunarungu (Jawa–Bali) memakai BISINDO sehari-hari; konsep SIBI dianggap sulit | [9] | DV |
| F8 baku-SIBI | Kamus SIBI 1994 (SK 0190/P/1994); Surat 868/C/U/95 mewajibkan sistem isyarat baku pada SLB komunikasi total; Kamus SIBI Digital tersedia daring (asetnya tak terverifikasi sesi ini — halaman terblokir) | [10], [45] | DV |
| F9 SIBI-di-SLB | Murid SLB N Ogan Ilir memakai SIBI dalam pembelajaran harian | [11] | DV |
| F10 KASIBI | Suara → pengenal ucapan → basis data → animasi peraga 3D; uji kelayakan 3,362 dari 4 | [12] | DV |
| F11 OpenSIBI | Google Speech-to-Text → API model 3D Collada → animasi Android; hanya 50 kosakata (9 angka, 26 huruf, 15 kata); keterbatasan kosakata diakui penulisnya | [13] | DV (PDF penuh) |
| F12 kamera-moda-utama | Riset isyarat Indonesia bertumpu kamera: SLR BISINDO [14]; CNN 26 huruf + 10 angka [15]; 24 huruf statis SIBI MediaPipe 90,85% [16]; TFLite alfabet statis [17]; keberhasilan bergantung pencahayaan dan garis pandang [18] | [14]–[18] | DV |
| F13 kamera-kelelahan | Paparan kamera yang terus menyala dikaitkan dengan kelelahan nonverbal | [19] | DV |
| F14 dasar-CSI | CSI memuat amplitudo dan fase tiap subcarrier yang berubah saat gerak tubuh mengganggu jalur pantulan; gerak menghasilkan komponen Doppler | [20] | DV |
| F15 SignFi | 276 isyarat ASL dari CSI Intel 5300 (3 antena penerima); dalam sesi 98,01% (lab), 98,91% (rumah), 94,81% (campuran) — dikutip untuk konteks multi-antena, bukan proyeksi ESP32 | [21] | DV |
| F16 DF-WiSLR | 49 gestur dikenali tanpa perangkat yang dikenakan | [22] | DV |
| F17 Filipino-SL | Pengenalan Filipino Sign Language dari CSI (preseden bahasa nasional lain) | [23] | DV |
| F18 WiSign | Kalimat ASL kontinu dikenali dari CSI perangkat komersial (segmentasi kepadatan spektrum) — membatasi klaim kebaruan kontinu | [24] | DV |
| F19 WiKey | Ketukan tombol (gerak jari skala sentimeter): deteksi >97,5%, klasifikasi kunci tunggal 96,4% pada kondisi terkendali | [25] | DV |
| F20 napas | Pola pernapasan (gerak dada milimeter) 99,54%; laju napas 98,69% pada kanal cukup baik | [26] | DV |
| F21 esp-csi | CSI didukung resmi seluruh seri ESP32 termasuk S3; kanal HT20 802.11n memuat 56 subcarrier (52 data + 4 pilot) | [27] | DV |
| F22 RuView | Firmware CSI format ADR-018 via UDP; batas kirim 20 ms → maksimum 50 bingkai/detik; kalibrasi ruang 600 bingkai + 8 anchor ±4 menit; segmentasi energi gerak; dashboard web; mode privasi; pipeline kamera–CSI `collect-ground-truth.py` (ADR-079); koeksistensi STA + CSI promiscuous + ESP-NOW pada satu chip (terbukti di firmware, "works on both S3 and C6") dengan tiga syarat: satu kanal, filter paket MGMT, `WIFI_PS_NONE`; ESP-NOW memuat hingga 250 bita per paket | [28] | DV (kode dibaca) |
| F23 datasheet-S3 | Dual-core LX7 240 MHz (instruksi vektor); SRAM 512 KB; ROM 384 KB; PSRAM terpasang s.d. 8 MB oktal; Wi-Fi b/g/n 2,4 GHz tautan tunggal SISO 1T1R | [29] | DV |
| F24 ESP-NN | Person detection 2.300 ms → 54 ms pada S3 (model 293,5 KB, arena 100 KB) | [30] | DV |
| F25 ESP-DL | Model int8 contoh pada S3: hand-gesture 69,2 ms; MobileNetV2 437,9 ms | [31] | DV |
| F26 TFLM | Contoh micro_speech 18,4 KB berjalan penyangga terkendali | [72] | DV |
| F27 Whisper | 100+ bahasa termasuk Indonesia; large-v3 1,55 miliar parameter; turbo 809 juta (±6 GB) | [32] | DV |
| F28 faster-whisper | Tolok ukur RTX 3070 Ti 8 GB: large-v3 int8 ±2,9 GB VRAM; 13 menit audio selesai 59 detik (±13× waktu nyata) | [33] | DV |
| F29 MMS-TTS-ind | Checkpoint TTS Indonesia (VITS), lisensi CC-BY-NC 4.0, dapat dijalankan lokal | [34], [35] | DV |
| F30 Google-TTS | Suara id-ID Standard dan Premium; Standard ±US$4 per juta karakter setelah jatah gratis bulanan | [36] | DV |
| F31 Azure | Suara id-ID-GadisNeural dan id-ID-ArdiNeural | [37] | DV |
| F32 Kokoro | Model card resmi: 8 bahasa dan 54 suara — Bahasa Indonesia tidak termasuk (bukti kehati-hatian pemilihan teknologi) | [38] | DV |
| F33 YOLO26 | Keluarga model visi waktu nyata multi-tugas; model pose terlatih COCO menghasilkan 17 keypoint tubuh per orang tanpa keypoint jari | [41], [42] | DV |
| F34 supervisi-visi | Person-in-WiFi dan DensePose from WiFi = preseden pengetahuan visi untuk model Wi-Fi (kamera aktif hanya saat pelatihan) | [63], [64] | DV |
| F35 parameter-isyarat | Isyarat tersusun atas bentuk tangan, lokasi, gerak, orientasi telapak, dan komponen nonmanual (perbedaan satu parameter mengubah makna) | [46], [47] | DV |
| F36 kata-infleksi | Kata jadian SIBI dikenali dengan HMM; komponen gesturnya diurai karya lanjutan | [74], [75] | DV |
| F37 SLMT-terbuka | Penerjemahan mesin bahasa isyarat tingkat kalimat masih masalah terbuka; mouthing adalah isu kelas satu keterbacaan avatar | [43], [44] | DV |
| F38 ejaan-jari | Alfabet manual: 26 huruf + 9 angka [13]; dataset citra statis riset hanya 24 kelas tanpa J dan Z (keduanya melibatkan gerakan) — 7.582 citra, MobileNetV2 97,10% | [13], [16], [73] | DV |
| F39 angka-2600 | Angka "±2.600 kosakata kamus SIBI" tidak ditemukan sumber layak kutip (DDG, Bing, Crossref, OpenAlex) — jangan dipakai | — | XT |
| F40 Sagawa | Preseden internasional sistem pembelajaran isyarat dengan pengenalan + pembangkitan | [76] | DV |
| F41 lintas-domain | Model CSI mudah overfitting terhadap orang dan ruang; strategi generalisasi dirangkum; Widar3.0 memakai profil kecepatan Doppler | [39], [40] | DV |
| F42 Nyquist | Pita Doppler 1–60 Hz terwakili bila laju pencuplikan ≥ 120 Hz; firmware maksimum 50 bingkai/detik → pita menyempit setengah laju aktual dan dilaporkan | [55], [56], [28] | DV |
| F43 kelayakan-metrik | Desain studi kelayakan bertahap; metrik klasifikasi (akurasi, presisi, recall, F1 makro, confusion matrix); kuesioner skala Likert | [77]–[79] | DV |
| F44 Vosk | Vosk resmi tidak menyediakan model Bahasa Indonesia | riset T17-R1 | DV |
| F45 arus-S3 | Datasheet: arus penerimaan 88–91 mA; pemancaran puncak 283–340 mA — basis estimasi baterai; arus modul lengkap (radio + layar + audio) belum terukur, diukur pada T4 | [29] | DV |

Cara pemakaian: setiap fakta dipakai **tidak melebihi sumbernya**. Angka SignFi/Wi-SL tidak diproyeksikan ke perangkat satu antena; angka WiKey/Mosleh dikutip sebagai bukti kepekaan pada kondisi terkendali, bukan jaminan; survei BRIN dan Mursita selalu disertai keterbatasan sampelnya.
"""

BANK_RUJUKAN = """
## 4. Bank Rujukan per Kelompok (peta ke Daftar Pustaka Proposal-Revisi)

| Kelompok | Nomor [n] | Peran di naskah |
|---|---|---|
| A — konteks tunarungu, SIBI, hukum | [1]–[11], [45]–[49] | Latar belakang BAB I §1.1–1.2; kajian BAB II §2.1–2.2 |
| B — pengenalan isyarat dari CSI | [20]–[24], [57], [58], [65]–[67] | BAB II §2.3, §2.6; tabel penelitian terdahulu |
| C — sensitivitas gerak halus & lintas domain | [25], [26], [39], [40] | BAB II §2.3 (kepekaan), §2.6 (strategi fitur) |
| D — supervisi visi untuk Wi-Fi | [63], [64] | BAB II §2.5 (preseden peran kamera hanya saat pelatihan) |
| E — visi isyarat Indonesia + pose | [14]–[17], [51]–[53], [60]–[62], [73] | BAB II §2.2, §2.5; pembanding moda kamera |
| F — arah balik teks/suara → isyarat | [12], [13], [19], [43], [44], [50], [74]–[76] | BAB II §2.2, §2.8 (desain arah kedua) |
| G — TTS dan ASR Indonesia | [32]–[38] | BAB II §2.7 (audit teknologi ucapan) |
| H — platform ESP32-S3/RuView + metode + evaluasi | [27]–[31], [54]–[56], [68]–[72], [77]–[79] | BAB II §2.4, §2.6, §2.10; BAB III §3.4, §3.7 |

Dua puluh rujukan baru ditambahkan pada revisi (WiSign, WiKey, Mosleh, Mursita, Picron, Hakozaki, Safrida/Rabit, Rakun, Anggraini, Whisper, MMS, mms-tts-ind, Kokoro, faster-whisper, Google TTS, Azure, datasheet S3, esp-csi, esp-dl, tflite-micro-esp, esp-nn) dan enam rujukan lama dikeluarkan karena melekat pada uji persepsi kamera yang sudah dihapus (Sigrist 2013; Zajonc 1965; Daniel 2024; Hassan 2026; dua entri pendukung). Metadata verifikasi: `scripts/translator-sibi/meta_rujukan_baru.json`.
"""

PERANGKAT = """
## 5. Perangkat, Aset, dan Peta Diagram

### 5.1 Perangkat keras (selaras Tabel 3.1 proposal revisi)

| No. | Nama | Spesifikasi | Jumlah | Keterangan |
|---|---|---|---|---|
| 1 | Modul ESP32-S3 | Papan pengembangan S3 dengan PSRAM, varian yang direkomendasikan RuView | 3 unit | Modul TX, modul RX, modul pengguna (bergilir dengan cadangan) |
| 2 | Layar modul | SPI/TFT 1,8–2,8 inci [PERLU DATA: model final] | 1–2 unit | Tampilan representasi SIBI |
| 3 | Antarmuka audio | Mikrofon I2S + speaker dengan penguat I2S (contoh umum: INMP441, MAX98357A) [PERLU DATA: model final] | 1 set | Pintu suara arah kedua dan pemutaran TTS |
| 4 | Baterai modul | Li-ion/Li-Po dengan regulator daya [PERLU DATA: kapasitas berdasar uji arus] | 1–2 set | Ketahanan diukur pada uji operasional |
| 5 | Laptop | ASUS TUF Dash F15 FX516PR: i7-11370H, RTX 3070 Laptop 8 GB VRAM, RAM 16 GB | 1 unit | Pelatihan, server lokal, jalur pelabelan |
| 6 | Access point | Router 2,4 GHz atau hotspot laptop [PERLU DATA: pilihan final] | 1 unit | Seluruh perangkat satu kanal |
| 7 | Webcam | Bawaan laptop | 1 unit | Hanya menyala pada jalur pelabelan dataset riset |

### 5.2 Perangkat lunak (selaras Tabel 3.2 proposal revisi)

Firmware dan server RuView; `scripts/collect-ground-truth.py` (ADR-079, estimator diganti pose YOLO26); model pose YOLO26; Python + scikit-learn + PyTorch; TensorFlow Lite Micro dan ESP-DL; faster-whisper (ASR); MMS-TTS-ind (TTS); layanan TTS awan (opsional pembanding); kamus label-teks dan teks-isyarat (dikembangan sendiri). Versi dicatat bersama log konfigurasi agar eksperimen dapat diulang.

### 5.3 Aset RuView yang dipakai (selaras Tabel 2.1 proposal revisi)

Firmware penangkap CSI (ADR-018, streaming UDP) → aliran CSI dan label; koeksistensi STA + UDP + CSI + ESP-NOW pada satu chip → dasar topologi satu kanal; kalibrasi ruang 600 bingkai + 8 anchor → awal setiap sesi; segmentasi energi gerak → memotong segmen terisolasi; dashboard web → pemantauan sesi riset; mode privasi → membuang fitur biometrik; pipeline ADR-079 → jalur pelabelan dengan estimator diganti YOLO26; modul estimasi pose on-device RuView → **tidak dipakai**. Fungsi yang dipakai diverifikasi ulang pada G0 sebelum perekaman karena RuView tidak melalui telaah sejawat.

### 5.4 Peta diagram (sepuluh visual `diagram/*.mmd`, lolos validasi mmdc)

| Kode | Judul | Lokasi | Tugas argumen |
|---|---|---|---|
| G1.1 | Peta masalah dan kesenjangan | 1.1 | Masalah inti bercabang empat kesenjangan → posisi penelitian |
| G1.2 | Visi purwarupa dua arah tanpa kamera | 1.1 | Modul TX/RX, server lokal, speaker/mikrofon/layar |
| G2.1 | Taksonomi pengenalan dan translasi | 2.2 | Tiga moda pengenalan; tiga tingkat translasi balik |
| G2.2 | Alur arah pertama | 2.7 | ESP-NOW → CSI → segmen → fitur → int8 → label → TTS |
| G2.3 | Alur arah kedua | 2.8 | Dua pintu masuk → ASR → kamus → tampil/ejaan jari |
| G3.1 | Alur pelatihan bergerbang | 3.2 | T0–T5 + G0–G4; YOLO26 hanya di T2 |
| G3.2 | Arsitektur produk akhir tanpa kamera | 3.5.1 | Dua arah resmi; jalur pelabelan putus-putus |
| G3.3 | Topologi jaringan | 3.5.2 | Modul A/B/C, AP satu kanal, server, cloud alternatif |
| G3.4 | Inferensi langsung pada S3 | 3.7.7 | Callback CSI → penyangga PSRAM → int8 → ambang |
| G3.5 | Alur dataset–evaluasi–deployment | 3.8 | Perekaman → penyaringan → 5 skema → metrik → uji |

### 5.5 Tabel gerbang keputusan (selaras Tabel 3.4 proposal revisi)

| Gerbang | Waktu | Ukuran | Kriteria lolos | Tindakan bila gagal |
|---|---|---|---|---|
| G0 | Akhir M2 | Uji Delta-CSI dan koeksistensi | Pola CSI bergerak terpisah dari diam dan kosong; CSI + STA + UDP serentak, kehilangan paket terkendali | Perbaiki penempatan satu kali; gagal lagi → jalur CSI dihentikan, dilaporkan sebagai temuan karakterisasi |
| G1 | M3 | Separabilitas awal 2–3 isyarat (nearest-centroid) | Repetisi isyarat sama lebih rapat sesamanya daripada ke isyarat lain | Ubah penempatan/orientasi satu kali; gagal lagi → tindakan sesuai Tabel 3.6 |
| G2 | M6–M7 | Akurasi skema dalam sesi | Jauh di atas peluang acak (ambang pada Tabel 3.6) | Pangkas ke 3–5 isyarat yang bertumpu lintasan |
| G3 | M10 | Kinerja lintas partisipan dan ruang | Di atas peluang acak | Cakupan menjadi personalisasi per pengguna, ditulis sebagai temuan |
| G4 | M12 | Kelengkapan uji dan persetujuan validator | Data uji operasional, jalur ucapan, cakupan kamus, kegunaan tercatat; validator menyetujui kewajaran keluaran | Hasil negatif tetap dilaporkan sebagai temuan kelayakan |

### 5.6 Risiko dan alternatif cadangan (selaras Tabel 3.7 proposal revisi)

| No. | Risiko | Mitigasi / cadangan |
|---|---|---|
| 1 | Pola CSI isyarat tidak terpisah pada konfigurasi dua modul | Perbaikan penempatan satu kali; bila tetap gagal → dihentikan, dilaporkan sebagai temuan |
| 2 | Akurasi lintas partisipan/ruang rendah | Personalisasi per pengguna (cadangan A) |
| 3 | Model int8 terlalu berat di modul | Klasifikasi dipindah ke server, modul kirim fitur (cadangan B); klaim inferensi tepi jadi hasil uji banding |
| 4 | Beban radio gabungan CSI + UDP + audio bermasalah | Pemisahan peran modul: modul CSI khusus dan modul pengguna khusus (cadangan C) |
| 5 | TTS/ASR lokal terlalu lambat untuk frasa pendek | Turunkan ukuran model ASR atau uji layanan awan sebagai pembanding (cadangan D) |
| 6 | Aset representasi mahal dibuat | Batasi ke glos + gambar konfigurasi + ejaan jari; animasi jadi pengayaan |
| 7 | Ketahanan baterai di bawah target | Ukur arus tiap kondisi, sesuaikan target, laporkan apa adanya |
| 8 | Rekrutmen/etika terlambat | Dua ruang dan pengisyarat cadangan di T1; transisi satu minggu |
"""

LAMPIRAN = """
## 13. Lampiran — Jejak Riset dan Cara Memakai Dossier

**Jejak bukti.** Matriks rujukan dan status verifikasi per klaim: `download/translator-sibi-revisi/Matriks-Literatur-dan-Bukti.md`. Vonis kelayakan komponen: `Audit-Arsitektur-Translator-SIBI.md`. Catatan riset teknis: `riset-translator-sibi/T17-R1-tts-asr-indonesia.md`, `T17-R2-esp32s3-csi.md`, `T17-R3-representasi-sibi.md`. Metadata Crossref rujukan baru: `scripts/translator-sibi/meta_rujukan_baru.json`. Arsip verifikasi rujukan lama: `13-sempro-docx/verifikasi-rujukan-2026-10-24/`. Dossier pendahulu (topik lama, masih berguna untuk kontras): `12-council-alur-dpj4/DPJ-4_Bahan-Proposal-SIBI.md` beserta transkrip dewan.

**Konvensi penanda.** `[PERLU DATA: ...]` = keputusan yang menunggu pemilik, pembimbing, atau hasil tahap sebelumnya; `[PERLU RUJUKAN: ...]` = klaim yang belum punya rujukan terverifikasi (dossier ini tidak memuatnya). Frasa ID-READY = kalimat bahasa Indonesia siap disalin lalu disesuaikan ke naskah.

**Optimisasi GEPA.** Dossier ini disusun sebagai kandidat benih dan disempurnakan lewat `optimize_anything` (paket gepa 0.1.4, backend gepa) dengan evaluator hibrida: cek objektif (jangkar fakta, klaim terlarang, penanda, panjang) × rubrik juri LLM lima dimensi. Log iterasi tersimpan pada `scripts/translator-sibi-bahan/runs/`; laporan ringkas pada `catatan.md` paket pengiriman.
"""

# Urutan perakitan dokumen final: (jenis, kunci, judul seksi sebelum komponen)
SUSUNAN = [
    ("tetap", "HEADER", None),
    ("mut", "ringkasan", "## 0. Ringkasan Eksekutif"),
    ("mut", "arah_latar", "## 1. Arah Latar Belakang"),
    ("mut", "peta_masalah", "## 2. Masalah yang Dijawab"),
    ("tetap", "BANK_FAKTA", None),
    ("tetap", "BANK_RUJUKAN", None),
    ("tetap", "PERANGKAT", None),
    ("mut", "konsep_alat", "## 8. Konsep Penyelesaian: Pemetaan, Skenario, Disiplin Klaim"),
    ("mut", "kit_bab1", "## 9. Kit Penulisan BAB I (kalimat ID-READY)"),
    ("mut", "kit_bab23", "## 10. Kit Penulisan BAB II dan BAB III"),
    ("mut", "sidang", "## 11. Antisipasi Sidang: Pertanyaan dan Jawaban Siap Pakai"),
    ("mut", "keputusan", "## 12. Keputusan Terbuka dan Langkah Pertama"),
    ("tetap", "LAMPIRAN", None),
]


def rakit(komponen: dict) -> str:
    """Rakit dokumen final dari komponen mudah-mutasi + bagian tetap."""
    bagian = []
    for jenis, kunci, judul in SUSUNAN:
        if jenis == "tetap":
            bagian.append(globals()[kunci])
        else:
            isi = komponen.get(kunci, "").strip()
            bagian.append("\n" + judul + "\n\n" + isi + "\n")
    teks = "".join(bagian)
    import re as _re
    return _re.sub(r"\n{4,}", "\n\n\n", teks)
