## 3.13 Rencana Penjaminan Mutu

Subbab ini menetapkan rencana penjaminan mutu (*quality assurance*, QA) berlapis yang mengikat seluruh komponen penelitian pada gerbang keputusan yang sudah ada. Setiap uji memiliki pengenal, komponen yang diuji, prasyarat, prosedur, hasil yang diharapkan, metrik beserta ambang, bukti yang disimpan, status hasil, dan tindakan jika gagal; kesembilan butir itu tercantum lengkap pada matriks uji berkas pendamping SenseSIBI-v21-Audit-QA.xlsx yang disusun agar dapat dijalankan dan diisi hasilnya selama penelitian berlangsung. Naskah ini memuat katalog ringkasnya berupa tabel per lapisan, sementara prosedur rinci per uji tetap berada pada matriks dan berkas kerja tahap terkait. Seluruh ambang pada subbab ini berstatus usulan sampai difinalkan bersama pembimbing (Tabel 3.7 no. 1), dan status seluruh uji pada saat penyusunan proposal ialah belum diuji karena pengujian baru berjalan ketika penelitian dimulai; tidak ada kelulusan yang dinyatakan di muka.

Tabel 3.11 Pemetaan lapisan penjaminan mutu terhadap gerbang keputusan

| Lapisan | Fokus | Gerbang utama | Jumlah uji |
|---|---|---|---|
| 1. Firmware dan perangkat keras (QA-FW) | Pembangunan, pemrograman modul, konfigurasi radio, audit pinout | G0 | 6 |
| 2. Akuisisi dan transport CSI (QA-ACQ) | Laju, kehilangan paket, subcarrier valid, koeksistensi radio | G0 | 7 |
| 3. Dataset dan anotasi (QA-DS) | Protokol perekaman, kualitas label guru, anti-kebocoran | G0b, G1 | 6 |
| 4. Arsitektur model dan pelatihan (QA-MDL) | Kontrak checkpoint, determinisme, dua kepala, ablasi | G0b, G1 | 6 |
| 5. Evaluasi dan anti-kebocoran (QA-EVL) | Split, pelaporan metrik, penolakan, pemangkasan | G1 | 6 |
| 6. Integrasi Rust dan server (QA-SRV) | Parsing, memori, ketahanan, orkestrasi layanan | G3 | 5 |
| 7. Kuantisasi dan deployment tepi (QA-EDGE) | Operator, kalibrasi, paritas, latensi, daya | G1, G3 | 6 |
| 8. ASR/TTS dan komunikasi dua arah (QA-SPC) | WER, TTFA, mutu sintesis, kamus, kondisi jaringan | G3 | 6 |
| 9. Penerimaan pengguna dan aksesibilitas (QA-UAT) | Uji kegunaan, validator, etika, biaya | G2, G4 | 6 |

Pemetaan pada Tabel 3.11 tidak menambah gerbang baru. Bukti uji menjadi bahan penilaian gerbang, gerbang menjadi titik tanda tangan lanjut atau berhenti, dan hasil negatif tetap dilaporkan sebagai temuan sebagaimana dirancang pada Subbab 2.14. Bukti setiap uji disimpan dalam struktur folder riset berupa log, skrip, keluaran program, tabel pengukuran, atau foto; setiap berkas bukti menyertakan tanggal, komit perangkat lunak, dan kondisi uji agar dapat diperiksa ulang.

### 3.13.1 Lapisan 1: Firmware dan Perangkat Keras

Prasyarat lapisan ini ialah komit firmware dan versi ESP-IDF yang dikunci (Tabel 3.7 no. 22) serta perangkat keras Tabel 3.1 yang telah diperiksa pinout-nya. Prosedurnya membangun firmware dari sumber pada komit terkunci memakai Docker ESP-IDF versi yang ditentukan dokumentasi, memprogram kedua node, lalu menjalankan verifikasi konfigurasi pada perangkat nyata; uji pipeline tanpa perangkat memakai mode QEMU dengan pembangkit CSI sintetis disiapkan sebagai alat bantu. Jika gagal, versi perangkat lunak dikunci ulang, konfigurasi diperbaiki, dan kegagalan berulang eskalasinya mengikuti Tabel 3.8 no. 13.

Tabel 3.12 Uji lapisan firmware dan perangkat keras

| ID | Komponen yang diuji | Prasyarat | Metrik dan ambang (usulan) | Bukti | Gerbang |
|---|---|---|---|---|---|
| QA-FW-01 | Pembangunan firmware dari komit terkunci | Docker ESP-IDF v5.4; SHA komit tercatat | Bangunan sukses; ukuran biner di bawah ambang CI RuView 950 KB | Log bangunan + hash biner | G0 |
| QA-FW-02 | Pemrograman dan provisioning dua node (TX, RX) | Bangunan QA-FW-01 | Kedua node bergabung ke AP pada satu kanal; power save mati sesuai log firmware | Log boot kedua node | G0 |
| QA-FW-03 | Konfigurasi dua node peran tetap tanpa ESP-NOW tambahan | QA-FW-02 | CSI mengalir dari RX; tidak ada dependensi ESP-NOW pada jalur akuisisi | Log sesi + rekaman bingkai | G0 |
| QA-FW-04 | Patch penandaan MAC pengirim pada bingkai ADR-018 (pola kit [34], AUD-03) | Patch ditinjau dan dicatat sebagai penyimpangan terdokumentasi | Setiap bingkai membawa MAC pengirim; server memisahkan tautan TX-RX | Diff patch + keluaran parser | G0 |
| QA-FW-05 | Pipeline tepi tanpa perangkat (QEMU, pembangkit CSI sintetis) | Docker; konfigurasi pembangkit aktif | Pipeline pemrosesan tepi berjalan pada bingkai sintetis tanpa galat | Log QEMU | G0 |
| QA-FW-06 | Audit pinout antarmuka (strapping GPIO 0/3/45/46, USB, ADC1, konflik I2C/I2S/SPI) | Skema papan dan Tabel 3.3 | Tidak ada konflik periferal; revisi papan tercatat | Lembar audit pinout | G0 |

### 3.13.2 Lapisan 2: Akuisisi dan Transport CSI

Prasyarat lapisan ini ialah lapisan 1 lulus dan ruang uji terpasang sesuai Gambar 3.1. Prosedurnya merekam CSI pada kondisi dasar (ruang kosong, pengisyarat diam, pengisyarat bergerak) selama sesi berdurasi cukup, memverifikasi format bingkai hingga parser server, dan mengukur laju serta kehilangan paket pada kondisi normal maupun saat audio mengalir. Jika gagal, urutan tindakannya mengikuti Tabel 3.5 G0: perbaikan penempatan satu kali, lalu jalur CSI dihentikan dan dilaporkan jika gagal lagi.

Tabel 3.13 Uji lapisan akuisisi dan transport CSI

| ID | Komponen yang diuji | Prasyarat | Metrik dan ambang (usulan) | Bukti | Gerbang |
|---|---|---|---|---|---|
| QA-ACQ-01 | Laju CSI aktual node RX | QA-FW-03 | Sekurang-kurangnya 25 bingkai per detik; median dan jitter dilaporkan | Log laju per sesi | G0 |
| QA-ACQ-02 | Kehilangan paket UDP selama sesi | QA-ACQ-01 | Tidak melampaui 0,1% pada sesi 60 menit | Rekap paket | G0 |
| QA-ACQ-03 | Audit subcarrier valid N_valid (LLTF 52, HT-LTF 56, pilot, sanitasi first_word_invalid) | Parser ADR-018 | Daftar subcarrier valid dan statistik sanitasi terdokumentasi | Skrip audit + keluarannya | G0 |
| QA-ACQ-04 | Keterpisahan pola gerak lawan diam dan beberapa pose statis (Delta-CSI Persamaan 3.1 serta varian amplitudo) | Ruang terkalibrasi | Pola kondisi terpisah; keterpisahan awal pose tangan teramati | Notebook analisis + grafik | G0 |
| QA-ACQ-05 | Audit sisa phase drift (Persamaan 2.5) | Data QA-ACQ-04 | Besaran drift terestimasi dan koreksinya terdokumentasi | Laporan analisis | G0 |
| QA-ACQ-06 | Koeksistensi CSI, UDP, dan streaming audio serentak | Jalur audio aktif | Laju CSI tetap memenuhi QA-ACQ-01; degradasi tercatat | Log gabungan | G0, G3 |
| QA-ACQ-07 | Parser biner ADR-018 pada server (magic 0xC5110001/0xC5110002, port 5005) | Korpus bingkai uji | Seluruh bingkai sah terparse; bingkai rusak ditolak tanpa menghentikan server | Uji unit + fuzz ringan | G0 |

### 3.13.3 Lapisan 3: Dataset dan Anotasi

Prasyarat lapisan ini ialah protokol perekaman Subbab 3.6 disetujui dan kartu pemandu 26 huruf tervalidasi. Prosedurnya memverifikasi kartu terhadap Kamus SIBI, mengaudit kualitas label guru pada sampel yang diperiksa manusia, mengukur sinkronisasi penanda waktu kamera dan CSI, serta menjalankan pemeriksaan duplikasi dan kebocoran split. Temuan AUD-12 menjadi dasar kebijakan mask: nilai visibilitas label tidak diwarisi; kualitas anotasi dicalangkan dari skor deteksi dan verifikasi sampel. Jika gagal, pipeline anotasi diperbaiki dan didokumentasikan sebelum label dipakai pelatihan.

Tabel 3.14 Uji lapisan dataset dan anotasi

| ID | Komponen yang diuji | Prasyarat | Metrik dan ambang (usulan) | Bukti | Gerbang |
|---|---|---|---|---|---|
| QA-DS-01 | Kartu pemandu protokol 26 huruf terhadap Kamus SIBI [3] | Validator menyetujui bentuk baku | 26 kartu sesuai baku; orientasi telapak tercatat | Lembar kartu + persetujuan validator | G0b |
| QA-DS-02 | Kebijakan mask visibilitas pasca AUD-12 (label konstan tidak diwarisi) | Dataset CSI berpasangan | Mask efektif memakai penanda langkah valid + saringan kualitas deteksi; tingkat segmen terbuang dilaporkan | Skrip + laporan anotasi | G1 |
| QA-DS-03 | Verifikasi sampel anotasi oleh validator | Sesi perekaman selesai | Ketidakcocokan label protokol lawan guru tercatat; ambang saringan ditetapkan dari validasi | Formulir verifikasi | G1 |
| QA-DS-04 | Sinkronisasi penanda waktu kamera dan CSI | Kalibrasi sebelum sesi | Offset dan jitter terukur; prosedur selaras Subbab 3.6 | Log sinkronisasi | G0b |
| QA-DS-05 | Anti-duplikasi dan anti-kebocoran dataset CSI (md5 dan dHash, pola WPC) | Dataset terkumpul | Nol duplikat lintas split; purge gap sekurang-kurangnya W | Skrip audit | G1 |
| QA-DS-06 | Keseimbangan kelas dan pencatatan repetisi per kelas per sesi | Dataset terkumpul | Tabel repetisi utuh; kelas kurang terisi dijadwalkan ulang | Tabel dataset | G1 |

### 3.13.4 Lapisan 4: Arsitektur Model dan Pelatihan

Prasyarat lapisan ini ialah artefak checkpoint yang dipilih pada audit T0 (Tabel 3.7 no. 6) dan data pilot G0b. Prosedurnya memuat checkpoint lalu memverifikasi kontrak bentuk masukan dan keluaran, menjalankan pelatihan dengan seed tetap dan early stopping pada data validasi, lalu menjalankan probe linear G0b beserta uji permutasi sebelum pelatihan penuh; ablasi dijalankan pada pembagian dan seed yang sama. Jika kontrak bentuk gagal, keluarga berkas checkpoint diganti dan hasilnya dilaporkan; jika G0b gagal, urutan jalur cadangan mengikuti Tabel 3.5 G0b.

Tabel 3.15 Uji lapisan arsitektur model dan pelatihan

| ID | Komponen yang diuji | Prasyarat | Metrik dan ambang (usulan) | Bukti | Gerbang |
|---|---|---|---|---|---|
| QA-MDL-01 | Audit artefak checkpoint: pemuatan keluarga berkas terpilih, verifikasi standardizer, uji triplet kecil (AUD-07, AUD-08) | Checkpoint dipin pada SHA | Masukan (B, 8) menghasilkan embedding 128 ternormalisasi L2; metrik triplet terukur | Skrip audit + log | G0b |
| QA-MDL-02 | Determinisme pelatihan (seed tetap, early stopping) | Konfigurasi terkunci | Dua jalan dengan seed sama menghasilkan metrik identik | Log pelatihan | G1 |
| QA-MDL-03 | Kontrak dua kepala: 26 logit klasifikasi; regresi berbentuk [T, 21, 2]; padding tidak masuk kerugian (mask m∗ Persamaan 2.13a) | Implementasi model | Bentuk keluaran cocok; kerugian hanya menghitung langkah valid | Uji unit | G1 |
| QA-MDL-04 | Ablasi pada split dan seed sama (klasifikasi saja, multitugas penuh, variasi bobot kerugian) dengan pemantauan konflik gradien (Persamaan 2.14a) | Pelatihan selesai | Selisih ketiganya dilaporkan termasuk jika nihil; kosinis gradien tercatat | Tabel ablasi | G1 |
| QA-MDL-05 | Probe linear G0b: 24 huruf statis, probe sekuensial, probe biner J–Z, uji permutasi blok M = 1.000 | Data pilot 97 menit | F1 makro sekurang-kurangnya 0,30 dan tiga kali acak; J–Z sekurang-kurangnya 70%; skor asli melampaui persentil ke-95 sebaran nol (p_perm < 0,05) | Laporan G0b | G0b |
| QA-MDL-06 | Paritas antarruntime jika lebih dari satu dipakai (PyTorch lawan hasil ekspor) | Model terpilih | Keluaran identik dalam toleransi terdokumentasi | Uji paritas | G1 |

### 3.13.5 Lapisan 5: Evaluasi dan Anti-Kebocoran

Prasyarat lapisan ini ialah model terlatih dan pembagian data yang telah diaudit. Prosedurnya menjalankan evaluasi pada keenam skema Tabel 3.4 dengan pelaporan lengkap terhadap peluang acak, memisahkan pelaporan klasifikasi dan regresi, serta mencatat mekanisme penolakan secara berpasangan. Kegagalan pada lapisan ini tidak ditambal dengan mengubah data uji; pemangkasan himpunan huruf hanya boleh memakai data validasi dan keputusannya dicatat.

Tabel 3.16 Uji lapisan evaluasi dan anti-kebocoran

| ID | Komponen yang diuji | Prasyarat | Metrik dan ambang (usulan) | Bukti | Gerbang |
|---|---|---|---|---|---|
| QA-EVL-01 | Pembagian data sebelum pembentukan jendela; purge gap sekurang-kurangnya W | Konfigurasi split | Tidak ada jendela yang melintasi batas latih dan uji | Skrip audit split | G1 |
| QA-EVL-02 | Pelaporan klasifikasi lengkap terhadap peluang acak 3,8% (akurasi, presisi, recall, F1 makro, confusion) | Hasil uji keenam skema | Seluruh metrik dan pembanding dilaporkan berdampingan | Laporan evaluasi | G1 |
| QA-EVL-03 | Recall J dan Z terpisah beserta confusion pasangan huruf mirip | Hasil uji | Recall J/Z dan pasangan mirip dirinci | Matriks kekeliruan | G1 |
| QA-EVL-04 | Pelaporan berpasangan penolakan: akurasi tanpa penolakan, cakupan diterima, akurasi selektif, laju terima dan tolak palsu | Mekanisme penolakan aktif | Keempat angka dilaporkan bersama pada tiap eksperimen | Laporan | G1 |
| QA-EVL-05 | MPJPE dan PCK pada resolusi langkah dengan mask efektif | Kepala regresi aktif | Metrik pemantauan terlaporkan beserta galat per keypoint | Laporan | G1 |
| QA-EVL-06 | Disiplin pemangkasan himpunan huruf tanpa informasi data uji | Keputusan G1 | Dasar pemangkasan berasal dari data validasi dan tercatat | Notulat keputusan | G1 |

### 3.13.6 Lapisan 6: Integrasi Rust dan Server

Prasyarat lapisan ini ialah server Rust terpasang sesuai Subbab 2.13 dengan seluruh dependensi terkunci. Prosedurnya menjalankan server di bawah beban bingkai uji, mengukur latensi parsing dan memori, menguji ketahanan terhadap bingkai rusak, lalu menjalankan skenario integrasi penuh termasuk kondisi daring dan luring. Angka target parsing dan memori ialah target rancangan yang diukur, bukan hasil; jika gagal, optimasi dijalankan lalu pengukuran diulang sebelum G3 dinilai.

Tabel 3.17 Uji lapisan integrasi Rust dan server

| ID | Komponen yang diuji | Prasyarat | Metrik dan ambang (usulan) | Bukti | Gerbang |
|---|---|---|---|---|---|
| QA-SRV-01 | Latensi parsing UDP per bingkai | Beban uji bingkai | p50 di bawah 0,2 ms | Benchmark + log | G3 |
| QA-SRV-02 | Memori server pada beban 60 menit | QA-SRV-01 | Pemakaian di bawah 40 MB; tanpa tren naik (bocor) | Log memori berkala | G3 |
| QA-SRV-03 | Ketahanan parser terhadap bingkai rusak | Korpus bingkai rusak | Tidak ada panic; bingkai rusak dibuang dan tercatat | Uji fuzz | G3 |
| QA-SRV-04 | API, dasbor WASM, dan klien Tauri pada kondisi daring dan luring | Integrasi penuh | Seluruh alur berjalan; transisi kondisi tercatat | Skenario uji tertulis | G3 |
| QA-SRV-05 | Orkestrasi TTS dan ASR oleh server (pemanggilan, antrean, aliran audio) | Layanan ucapan terpasang | Alur ujung ke ujung terverifikasi; kegagalan layanan tertangani | Log orkestrasi | G3 |

### 3.13.7 Lapisan 7: Kuantisasi dan Deployment Tepi

Prasyarat lapisan ini ialah model terpilih hasil G1 dan alat ekspor yang diaudit. Prosedurnya mengekspor graph deployment Pilihan 1, memverifikasi dukungan operator pada runtime kandidat, mengalibrasi kuantisasi dari data latih, lalu mengukur ukuran model, waktu inferensi, dan konsumsi arus pada modul nyata. Jika model terbukti terlalu berat atau lambat, klasifikasi pindah ke server menurut jalur cadangan B (Tabel 3.8 no. 6) dan pelaporannya tetap dilakukan.

Tabel 3.18 Uji lapisan kuantisasi dan deployment tepi

| ID | Komponen yang diuji | Prasyarat | Metrik dan ambang (usulan) | Bukti | Gerbang |
|---|---|---|---|---|---|
| QA-EDGE-01 | Dukungan operator (BatchNorm, GELU) pada runtime kandidat ESP-DL atau TFLM [23] | Graph ekspor tersedia | Seluruh operator terverifikasi; klaim dukungan tanpa bukti tidak dipakai [PERLU VALIDASI: dukungan operator runtime tepi] | Matriks operator | G1 |
| QA-EDGE-02 | Kalibrasi kuantisasi affine int8 (Persamaan 3.2) | Data kalibrasi dari latih | Distribusi skala dan titik nol terdokumentasi | Laporan kalibrasi | G1 |
| QA-EDGE-03 | Paritas keluaran float lawan int8 | Model terkuantisasi | Kesesuaian prediksi sekurang-kurangnya 95% pada himpunan kecil [usulan]; deviasi tercatat | Uji paritas | G1 |
| QA-EDGE-04 | Ukuran model, RAM dan PSRAM, serta waktu inferensi per segmen | Modul nyata | Inferensi p50 dan p95 di bawah 100 ms; pemakaian memori terukur | Log inferensi | G1, G3 |
| QA-EDGE-05 | Stabilitas jangka pendek dan konsumsi arus pada beberapa kondisi kerja | Purwarupa terpasang | Arus rata-rata terukur; estimasi ketahanan baterai Persamaan 3.4 | Log arus | G3 |
| QA-EDGE-06 | Peralihan inferensi ke server saat tepi gagal | Skenario gangguan | Peralihan bekerja dan tercatat; durasi gangguan dilaporkan | Log skenario | G3 |

### 3.13.8 Lapisan 8: ASR/TTS dan Komunikasi Dua Arah

Prasyarat lapisan ini ialah daftar frasa uji berbahasa Indonesia yang telah disusun (Tabel 3.7 no. 17) dan mesin ucapan terpasang. Prosedurnya merekam keluaran ASR pada jalur awan dan luring, mengukur TTFA serta durasi sintesis pada kedua kandidat TTS, memverifikasi pemutaran audio pada node RX, lalu menghitung cakupan kamus dan memeriksa ejaan jari termasuk animasi J dan Z. Jika mutu atau latensi tidak memadai, keputusan mesin mengikuti Tabel 3.7 no. 17 dan jalur cadangan D diaktifkan.

Tabel 3.19 Uji lapisan ASR/TTS dan komunikasi dua arah

| ID | Komponen yang diuji | Prasyarat | Metrik dan ambang (usulan) | Bukti | Gerbang |
|---|---|---|---|---|---|
| QA-SPC-01 | ASR daring (layanan awan) dan luring (faster-whisper) pada frasa uji | Daftar frasa uji [PERLU DATA] | WER dilaporkan beserta rincian S, D, I, N tanpa rumus 1−WER; exact-match dilaporkan terpisah | Laporan ASR | G3 |
| QA-SPC-02 | TTFA dan durasi sintesis MMS-TTS-ind (kandidat utama) dan Kokoro (pembanding) | Mesin terpasang | TTFA p50 di bawah 100 ms pada frasa paling banyak lima kata pada kondisi terdokumentasi | Log TTS | G3 |
| QA-SPC-03 | Mutu sintesis bahasa Indonesia (penilaian manusia) | Klip sampel per mesin | Skor penilaian tercatat per mesin dan kondisi | Formulir penilaian | G3 |
| QA-SPC-04 | Pemutaran audio pada node RX (DAC I2S, penyangga cincin PSRAM) | Aliran aktif | Tanpa underrun pada sekurang-kurangnya 95% sesi [usulan] | Log pemutaran | G3 |
| QA-SPC-05 | Cakupan kamus arah kedua dan ejaan jari (animasi J dan Z wajib) | Daftar kata uji | Proporsi kata terwakili terukur; J dan Z tampil beranimasi | Laporan cakupan | G3 |
| QA-SPC-06 | Kondisi daring, luring, dan putus koneksi | Skenario gangguan terdefinisi | Seluruh transisi tercatat; jalur luring tetap berfungsi | Log skenario | G3 |

### 3.13.9 Lapisan 9: Penerimaan Pengguna dan Aksesibilitas

Prasyarat lapisan ini ialah purwarupa terpasang, instrumen uji disetujui, dan seluruh kelengkapan etika terpenuhi. Prosedurnya menjalankan uji kegunaan skala kecil bersama kelompok sasaran pada skenario terbimbing, merekap kuesioner persepsi, meminta penilaian kewajaran keluaran oleh validator penutur tunarungu, serta merangkum biaya dari BOM nyata. Hasil dianalisis secara deskriptif tanpa klaim kausal; hasil negatif tetap dilaporkan sesuai kriteria G4.

Tabel 3.20 Uji lapisan penerimaan pengguna dan aksesibilitas

| ID | Komponen yang diuji | Prasyarat | Metrik dan ambang (usulan) | Bukti | Gerbang |
|---|---|---|---|---|---|
| QA-UAT-01 | Uji kegunaan 3–5 pengguna kelompok sasaran pada skenario terbimbing | Purwarupa terpasang; persetujuan tertulis | Hambatan pemakaian tercatat; waktu penyelesaian tugas diukur | Notulat uji | G4 |
| QA-UAT-02 | Kuesioner persepsi skala Likert [28] dianalisis deskriptif | QA-UAT-01 selesai | Skor rata-rata sekurang-kurangnya 3,0 dari 5 [usulan]; median dan rentang dilaporkan | Rekap kuesioner | G4 |
| QA-UAT-03 | Penilaian validator kewajaran keluaran dua arah (tabel silang) | Validator tunarungu berkefasihan | Persetujuan tercatat; kasus dinilai keliru dilaporkan tersendiri | Tabel silang | G4 |
| QA-UAT-04 | Kelengkapan etika dan aksesibilitas instrumen (persetujuan aksesibel, wali dan persetujuan anak, retensi, re-identifikasi) | Protokol etika | Seluruh dokumen etika lengkap sebelum sesi dimulai | Berkas etika | G4 |
| QA-UAT-05 | BOM dan biaya purwarupa (Persamaan 3.5) dari survei harga nyata | Pengadaan selesai | Seluruh sel harga terisi tanpa angka karangan; total dinilai pada G4 | Tabel BOM | G4 |
| QA-UAT-06 | Rubrik penilaian tiga pilar pakar | Rubrik disetujui (Tabel 3.7 no. 14) | Skor rata-rata per pilar sekurang-kurangnya 3 dari 5; tanpa temuan blok | Formulir pakar | G2 |
