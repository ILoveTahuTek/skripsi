#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Bangun SenseSIBI-v21-Audit-QA.xlsx: register audit + matriks uji QA (dapat diisi)
+ traceability + keputusan terbuka + changelog v20->v21."""
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from pathlib import Path

OUT = Path("/home/z/my-project/download/sensesibi-v10/SenseSIBI-v21-Audit-QA.xlsx")

HEAD_FILL = PatternFill("solid", fgColor="1F4E79")
HEAD_FONT = Font(color="FFFFFF", bold=True, size=10)
WRAP = Alignment(wrap_text=True, vertical="top")
THIN = Border(*[Side(style="thin", color="BFBFBF")] * 4)
STATUS_FILL = {"PASS": "C6EFCE", "CONDITIONAL": "FFEB9C", "FAIL": "FFC7CE", "NOT VERIFIED": "D9D9D9"}

def style_sheet(ws, widths, freeze="A2"):
    for i, w in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w
    for c in ws[1]:
        c.fill, c.font, c.alignment, c.border = HEAD_FILL, HEAD_FONT, WRAP, THIN
    for row in ws.iter_rows(min_row=2):
        for c in row:
            c.alignment, c.border = WRAP, THIN
            c.font = Font(size=9)
    ws.freeze_panes = freeze

wb = Workbook()

# ============ 1. REGISTER AUDIT ============
ws = wb.active
ws.title = "Register Audit"
ws.append(["ID", "Severity", "Status", "Temuan", "Bukti (lokasi)", "Dampak / Tindakan korektif", "Gerbang"])
REG = [
 ("AUD-01","KRITIS","FAIL","Injeksi NDP masih stub ADR-029 tanpa satu pun pemanggil; bingkai Null Data 24 byte hanya penampung; pengendali TX (controller PR) belum mendarat","csi_collector.c:940-982; rv_radio_ops_esp32.c:84-88; ADR-029 status Proposed","Mekanisme baseline diganti trafik OFDM self-ping + callback CSI promiscuous; narasi dikoreksi (2.3, 3.4, 3.5, Tabel 2.1/3.1, Gambar 3.3, G0); Tabel 3.7 no. 22","G0"),
 ("AUD-02","Tinggi","PASS","Sumber CSI aktual: self-ping gateway 10-50 Hz (baku 50), promiscuous MGMT+DATA pada papan tanpa layar, batas laju 50 Hz, LLTF dipaksa, power save mati","csi_collector.c:67-75,109-116,415-430,523-534,678-743","G0 tetap mengukur laju aktual; klaim 50 bingkai/dtk didukung","G0"),
 ("AUD-03","Sedang","CONDITIONAL","Bingkai ADR-018 baku tidak memuat MAC pengirim; tautan TX-RX butuh atribusi","patch kit ruview-v0.8.8-kit.patch; kit/server.py:5-8; NOTICE.md","Patch penandaan MAC pola kit [34] atau setara diaudit di T0 (QA-FW-04)","G0"),
 ("AUD-04","Sedang","PASS","UDP ADR-018 terverifikasi: magic 0xC5110001/0xC5110002, port 5005, sanitasi first_word_invalid (4 byte dinolkan + bendera), bit sinkronisasi","csi_collector.c:157-215,260-293; edge_processing.h:17-28; user-guide.md:379","Parser Rust diuji bolak-balik (QA-ACQ-07)","G0"),
 ("AUD-05","Rendah","PASS","ESP-NOW hanya sinkronisasi mesh lintas node (ADR-110 solusi D1), bukan jalur CSI","csi_collector.c:266-280; main.c:343-345","Konsisten Tabel 3.7 no. 21","G0"),
 ("AUD-06","Sedang","PASS / NOT VERIFIED","Mesh multistatik 3-6 node TDM = konfigurasi lanjutan yang menunjuk ADR-029/032 (usulan); dua node peran tetap belum terverifikasi pada perangkat nyata","docs/user-guide.md:85,440-460","Uji dua node nyata di G0 (QA-FW-03); risiko Tabel 3.8 no. 13","G0"),
 ("AUD-07","Sedang","CONDITIONAL","NUL-padding model.safetensors (isu #1522) telah diperbaiki 13 Okt 2026; header kini bersih, 17 tensor termuat utuh; klaim v20 basi","commit 98b29a35 'Fix NUL-padded safetensors header'; sha256 17c9acc1…11a1","Teks 2.4 diperbarui; T0 tetap memverifikasi pemuatan langsung","T0"),
 ("AUD-08","Sedang","CONDITIONAL","Dua keluarga berkas checkpoint bersaldo metadata beda: epoch 20 vs 60; tau 0,07 vs 0,1; jendela 1/10 s vs 2/30 s; LoRA rank 8 vs 4; model.rvf.jsonl tak terdokumentasi; '12 menit' vs 34,9 menit","config.json; training-metrics.json; node-1/2.json; README kartu","Pemilihan keluarga berkas direkonsiliasi di T0; Tabel 3.7 no. 6 diperluas","T0, G0b"),
 ("AUD-09","Rendah","PASS","Catatan SISO 56 subcarrier (isu #509) berada di README utama RuView, bukan kartu model (0 kemunculan)","README.md RuView:342-346","Kutipan 2.4 dikoreksi dari [10],[11] menjadi [10]","-"),
 ("AUD-10","Tinggi","PASS","Kontrak encoder: 8 fitur @1 Hz, embedding 128 L2, 9.280 parameter, triplet 82,3% (vs 66,4/69,6), EWC lupa 32,97% Fisher 2000, PIR+BME280, 60.630 sampel 2 node 8 jam, MIT","README kartu; csi-embed-v2.py; csi-embed-v2-metrics.json; training-metrics.json","Angka dikutip dengan cakupan aslinya","G0b"),
 ("AUD-11","Rendah","NOT VERIFIED","Varian kuantisasi q2/q4/q8 + int4 4,56 KB dengan standardizer FP16 tersedia (RMSE q2 0,3396; q4 0,0576; q8 0,0027); kinerja pada tugas SIBI belum teruji","berkas model-q*.bin; csi-embed-v2-int4.bin; metrics","Uji paritas kuantisasi (QA-EDGE-02/03)","G1, G3"),
 ("AUD-12","KRITIS","CONDITIONAL","write_label() menulis visibilitas konstan '2' untuk seluruh 21 keypoint; label tidak mencerminkan oklusi","convert_sibi_v2.py:286-297; DATASET_V2.md","Mask tidak diwarisi dari label: penanda langkah valid + saringan kualitas deteksi + verifikasi sampel (2.7, 2.9, Tabel 3.8 no. 14, QA-DS-02)","G0b, G1"),
 ("AUD-13","Sedang","PASS","flip_idx identitas terverifikasi empiris (n=16, konsistensi 0,91); koreksi atas permutasi COCO-WholeHand v1 yang salah untuk urutan MediaPipe","convert_sibi_v2.py:422-466; DATASET_V2.md butir 5","Urutan 21 keypoint MediaPipe dikunci","G1"),
 ("AUD-14","Tinggi","PASS","Dataset v2: 9.953 ditemukan; md5 -2.215; dHash -18; MediaPipe 7.210 OK / 510 gagal; 7.627 objek; split 6.231/650/329; split resmi Roboflow verbatim (0 bocor, 3.430 sumber); Kaggle hanya train; CC BY 4.0","DATASET_V2.md; convert_sibi_v2.py","Konsisten klaim 2.9","G1"),
 ("AUD-15","Tinggi","PASS","exp11_huruf24 dipetakan ulang ke 24 kelas huruf A-Y TANPA J dan Z; val 333 instance; mAP50 0,9580; mAP50-95 0,7235; box 0,9942/0,8918; conf 0,25: 325/333 (97,6%); 5 tertukar + 3 hilang","README WPC (evaluasi exp11); SUMMARY.json; folder eksperimen","Penanda [PERLU VALIDASI kelas J/Z] terjawab; supervisi J/Z dari lintasan + protokol","G1"),
 ("AUD-16","Sedang","NOT VERIFIED","Bobot exp11 belum diarsipkan di repo WPC; MANIFEST hanya exp00-exp10 + exp06b (sha256 073ccf71…, 50.532.034 byte)","pohon repo; weights/MANIFEST.json","Pemilik menerbitkan tag + hash exp11; penanda [PERLU DATA] rujukan [12] tetap","-"),
 ("AUD-17","Rendah","PASS","Pelatihan guru deterministik seed 42; ledger eksperimen lengkap exp00-exp11 dengan jejak ratchet 0,8445 -> 0,8944","README WPC; MANIFEST.json","Keterulangan pra-penelitian terdukung","G1"),
 ("AUD-18","Sedang","PASS","wifi-sensing-kit = kit orkestrasi di atas firmware RuView v0.8.8 + patch MAC; tanpa NDP; simetris pasif; ~50 Hz dibagi antar tautan; 52 subcarrier valid; hanya ESP32-S3; MIT","build.py:63; flash.py:21; NOTICE.md; server.py; how-it-works.md","Dipakai sebagai pola atribusi AUD-03 + opsi jalur pembanding pasif, bukan komponen inti","G0"),
 ("AUD-19","Sedang","CONDITIONAL","DensePose From WiFi pracetak tanpa telaah sejawat; 3x3 antena, 30 subcarrier, 100 Hz; IUV 24 wilayah tubuh + 17 keypoint tubuh; tanpa konten tangan; inkonsistensi internal tabel","ref-73 PDF (13 hlm); arxiv.org/abs/2301.00250","Dikutip sebagai latar penamaan lini dengan label pracetak [35], bukan dasar teknis encoder","-"),
 ("AUD-20","Rendah","PASS","Model MM-Fi terpisah: 17 keypoint tubuh, PCK@20 82,69%, lintas subjek zero-shot ~64%, CC BY-NC 4.0","kartu mmfi-pose; naskah 2.4 Tabel 2.2","Pemisahan tiga model konsisten","G0b"),
]
for r in REG:
    ws.append(r)
for row in ws.iter_rows(min_row=2, min_col=3, max_col=3):
    for c in row:
        status = str(c.value).split(" /")[0].strip()
        if status in STATUS_FILL:
            c.fill = PatternFill("solid", fgColor=STATUS_FILL[status])
style_sheet(ws, [9, 9, 16, 60, 38, 48, 10])

# ============ 2. MATRIKS UJI QA ============
ws2 = wb.create_sheet("Matriks Uji QA")
ws2.append(["ID", "Lapisan", "Komponen yang diuji", "Prasyarat", "Prosedur (ringkas)",
            "Hasil yang diharapkan", "Metrik dan ambang (usulan)", "Bukti yang disimpan",
            "Status hasil", "Tindakan jika gagal", "Gerbang"])
BELUM = "BELUM DIUJI"
def T(i, l, komp, pra, pros, hasil, metrik, bukti, gagal, g):
    ws2.append([i, l, komp, pra, pros, hasil, metrik, bukti, BELUM, gagal, g])

T("QA-FW-01","1 Firmware & HW","Pembangunan firmware dari komit terkunci","Docker ESP-IDF v5.4; SHA komit tercatat","Bangun firmware dari sumber pada komit terkunci; catat versi toolchain","Bangunan sukses dan terdokumentasi","Bangunan sukses; biner < 950 KB (ambang CI RuView)","Log bangunan + hash biner","Kunci ulang versi ESP-IDF; laporkan","G0")
T("QA-FW-02","1 Firmware & HW","Pemrograman dan provisioning dua node","QA-FW-01; AP tersedia","Flash kedua node; gabungkan ke AP satu kanal; verifikasi log boot","Kedua node aktif pada peran masing-masing","Kedua node bergabung; power save mati (log WIFI_PS_NONE)","Log boot kedua node","Perbaiki konfigurasi; jalur cadangan C","G0")
T("QA-FW-03","1 Firmware & HW","Konfigurasi dua node peran tetap tanpa ESP-NOW","QA-FW-02","Jalankan TX dan RX pada peran tetap; pastikan tidak ada dependensi ESP-NOW pada jalur akuisisi","CSI mengalir dari RX tanpa ESP-NOW","CSI mengalir; nol dependensi ESP-NOW","Log sesi + rekaman bingkai","Ikuti konfigurasi dokumentasi + laporkan penyimpangan","G0")
T("QA-FW-04","1 Firmware & HW","Patch penandaan MAC pengirim bingkai ADR-018","Patch ditinjau (pola kit [34])","Terapkan patch; pantau bingkai di server; pisahkan tautan TX-RX","Setiap bingkai membawa MAC pengirim; tautan terpisah","100% bingkai bertanda; tautan TX-RX teridentifikasi","Diff patch + keluaran parser","Alternatif atribusi yang setara; laporkan","G0")
T("QA-FW-05","1 Firmware & HW","Pipeline tepi tanpa perangkat (QEMU + mock CSI)","Docker; CONFIG_CSI_MOCK_ENABLED","Jalankan firmware di QEMU dengan pem bangkit CSI sintetis; ikuti alur pemrosesan tepi","Pipeline berjalan pada bingkai sintetis","Pipeline berjalan tanpa galat","Log QEMU","Tidak memblokir G0 (alat bantu saja)","G0")
T("QA-FW-06","1 Firmware & HW","Audit pinout antarmuka","Skema papan + Tabel 3.3","Periksa strapping GPIO 0/3/45/46, USB, ADC1, konflik I2C/I2S/SPI terhadap skema","Tidak ada konflik periferal","Nol konflik; revisi papan tercatat","Lembar audit pinout","Revisi pinout sebelum perakitan","G0")
T("QA-ACQ-01","2 Akuisisi & Transport","Laju CSI aktual node RX","QA-FW-03","Rekam CSI 60 menit; hitung bingkai per detik per sesi","Laju terukur dan stabil","≥ 25 bingkai/dtk; median + jitter dilaporkan","Log laju per sesi","Perbaikan penempatan satu kali; gagal lagi = henti jalur CSI","G0")
T("QA-ACQ-02","2 Akuisisi & Transport","Kehilangan paket UDP","QA-ACQ-01","Hitung bingkai dikirim lawan diterima selama sesi 60 menit","Kehilangan kecil","≤ 0,1%","Rekap paket","Mitigasi jaringan; ukur ulang","G0")
T("QA-ACQ-03","2 Akuisisi & Transport","Audit subcarrier valid N_valid","Parser ADR-018","Analisis LLTF 52 / HT-LTF 56, pilot, dan statistik sanitasi first_word_invalid","Daftar subcarrier valid terdokumentasi","Daftar + statistik sanitasi tercatat","Skrip audit + keluarannya","Sesuaikan pemrosesan; catat","G0")
T("QA-ACQ-04","2 Akuisisi & Transport","Keterpisahan gerak vs diam + pose statis (Delta-CSI)","Ruang terkalibrasi","Rekam ruang kosong, diam, bergerak, beberapa pose statis; hitung d(t) Persamaan 3.1 + varian 3.1b","Pola kondisi terpisah","Pola terpisah; keterpisahan awal pose teramati","Notebook analisis + grafik","G0 gagal: henti jalur CSI (Tabel 3.5)","G0")
T("QA-ACQ-05","2 Akuisisi & Transport","Sisa phase drift (Persamaan 2.5)","Data QA-ACQ-04","Estimasi drift fase pada subcarrier valid; rancang koreksi","Drift terestimasi dan terdokumentasi","Estimasi + koreksi tercatat","Laporan analisis","Tambahkan koreksi; laporkan","G0")
T("QA-ACQ-06","2 Akuisisi & Transport","Koeksistensi CSI + UDP + audio","Jalur audio aktif","Jalankan streaming audio sambil merekam CSI; bandingkan laju","Tidak ada degradasi melampaui ambang","Laju tetap memenuhi QA-ACQ-01","Log gabungan","Jalur cadangan C (modul ketiga / ponsel)","G0, G3")
T("QA-ACQ-07","2 Akuisisi & Transport","Parser biner ADR-018 server","Korpus bingkai uji","Uji unit parser terhadap bingkai sah dan rusak (fuzz ringan); verifikasi magic dan port","Parser benar dan tangguh","100% bingkai sah terparse; tak ada kegagalan server","Uji unit + fuzz","Perbaiki parser; uji ulang","G0")
T("QA-DS-01","3 Dataset & Anotasi","Kartu pemandu 26 huruf vs Kamus SIBI [3]","Validator menyetujui","Bandingkan 26 kartu terhadap bentuk baku; catat orientasi telapak","Kartu sesuai baku","26 kartu sesuai; orientasi tercatat","Lembar kartu + persetujuan","Revisi kartu","G0b")
T("QA-DS-02","3 Dataset & Anotasi","Kebijakan mask visibilitas (AUD-12)","Dataset CSI berpasangan","Verifikasi mask m* memakai penanda langkah valid + saringan kualitas; laporkan segmen terbuang","Mask tidak mewarisi label konstan","Mask efektif benar; tingkat segmen terbuang dilaporkan","Skrip + laporan anotasi","Perbaiki pipeline anotasi sebelum pelatihan","G1")
T("QA-DS-03","3 Dataset & Anotasi","Verifikasi sampel anotasi oleh validator","Sesi perekaman selesai","Sampel N segmen diperiksa manusia; catat ketidakcocokan label protokol vs guru","Ketidakcocokan terkendali","Ketidakcocokan tercatat; ambang saringan dari validasi","Formulir verifikasi","Naikkan saringan; laporkan","G1")
T("QA-DS-04","3 Dataset & Anotasi","Sinkronisasi penanda waktu kamera-CSI","Kalibrasi sebelum sesi","Uji offset dan jitter penanda waktu; verifikasi prosedur 3.6","Sinkron terjaga","Offset + jitter terukur dalam toleransi","Log sinkronisasi","Kalibrasi ulang; sesi ditunda","G0b")
T("QA-DS-05","3 Dataset & Anotasi","Anti-duplikasi & anti-kebocoran dataset CSI","Dataset terkumpul","Jalankan dedup md5 + leak-guard dHash lintas split; periksa purge gap","Dataset bersih","0 duplikat lintas split; purge gap ≥ W","Skrip audit","Bersihkan split; uji ulang","G1")
T("QA-DS-06","3 Dataset & Anotasi","Keseimbangan kelas & repetisi","Dataset terkumpul","Rekap repetisi per kelas per sesi; identifikasi kelas kurang","Repetisi terpenuhi","Tabel repetisi utuh","Tabel dataset","Sesi tambahan dijadwalkan","G1")
T("QA-MDL-01","4 Model & Pelatihan","Audit artefak checkpoint (AUD-07/08)","Checkpoint dipin SHA","Muat keluarga berkas terpilih; verifikasi standardizer; uji triplet kecil","Kontrak bentuk terpenuhi","(B,8) -> embedding 128 L2; triplet terukur","Skrip audit + log","Ganti keluarga berkas; laporkan","G0b")
T("QA-MDL-02","4 Model & Pelatihan","Determinisme pelatihan","Konfigurasi terkunci","Jalankan pelatihan dua kali seed sama; bandingkan metrik","Hasil identik","Metrik identik pada 2 jalan","Log pelatihan","Kunci versi pustaka; laporkan","G1")
T("QA-MDL-03","4 Model & Pelatihan","Kontrak dua kepala","Implementasi model","Uji bentuk keluaran 26 logit dan [T,21,2]; verifikasi mask m* pada kerugian","Bentuk dan mask benar","Bentuk cocok; padding tak masuk kerugian","Uji unit","Perbaiki implementasi","G1")
T("QA-MDL-04","4 Model & Pelatihan","Ablasi pada split + seed sama","Pelatihan selesai","Latih klasifikasi-saja, multitugas penuh, variasi lambda; pantau kosinis gradien (2.14a)","Selisih terlapor termasuk nihil","Tiga skema + kosinis gradien tercatat","Tabel ablasi","Penyeimbangan gradien / pelatihan bergantian","G1")
T("QA-MDL-05","4 Model & Pelatihan","Probe linear G0b + uji permutasi","Data pilot 97 menit","Probe 24 huruf, sekuensial, biner J-Z; permutasi label blok M=1.000","Skor melampaui acak secara signifikan (p_perm < 0,05)","F1 makro ≥ 0,30 & ≥ 3x acak; J-Z ≥ 70%; > persentil ke-95","Laporan G0b","Urutan jalur B1/B2 -> LoRA + Pembanding C","G0b")
T("QA-MDL-06","4 Model & Pelatihan","Paritas antarruntime","Model terpilih","Bandingkan keluaran PyTorch vs hasil ekspor pada himpunan uji","Keluaran identik","Identik dalam toleransi terdokumentasi","Uji paritas","Kunci satu runtime; laporkan","G1")
T("QA-EVL-01","5 Evaluasi & Anti-bocor","Split sebelum windowing + purge gap","Konfigurasi split","Audit pembagian: pastikan tak ada jendela melintasi batas; purge gap ≥ 1 s","Split bersih","0 jendela lintas batas","Skrip audit split","Perbaiki; evaluasi ulang","G1")
T("QA-EVL-02","5 Evaluasi & Anti-bocor","Pelaporan klasifikasi lengkap","Hasil uji 6 skema","Hitung akurasi, presisi, recall, F1 makro, confusion; bandingkan acak 3,8%","Pelaporan lengkap","Seluruh metrik + pembanding dilaporkan","Laporan evaluasi","-","G1")
T("QA-EVL-03","5 Evaluasi & Anti-bocor","Recall J/Z + confusion pasangan mirip","Hasil uji","Pisahkan recall J dan Z; rinci pasangan mirip","J/Z terlapor terpisah","Recall J/Z + pasangan mirip dirinci","Matriks kekeliruan","Pangkas himpunan sesuai aturan tanpa data uji","G1")
T("QA-EVL-04","5 Evaluasi & Anti-bocor","Pelaporan penolakan berpasangan","Mekanisme penolakan aktif","Ukur akurasi tanpa penolakan, cakupan diterima, akurasi selektif, laju terima/tolak palsu","Empat angka berpasangan","Keempat angka dilaporkan bersama","Laporan","Kalibrasi ambang dari validasi","G1")
T("QA-EVL-05","5 Evaluasi & Anti-bocor","MPJPE/PCK resolusi langkah","Kepala regresi aktif","Hitung MPJPE dan PCK dengan mask efektif; rinci galat per keypoint","Metrik pemantauan terlapor","MPJPE/PCK + galat per keypoint","Laporan","-","G1")
T("QA-EVL-06","5 Evaluasi & Anti-bocor","Disiplin pemangkasan himpunan huruf","Keputusan G1","Audit dasar pemangkasan: hanya data validasi, tercatat","Pemangkasan sah","Dasar dari validasi; tercatat","Notulat keputusan","Hentikan pemangkasan; laporkan","G1")
T("QA-SRV-01","6 Integrasi Rust","Latensi parsing UDP","Beban uji bingkai","Ukur waktu parsing per bingkai (p50) di bawah beban","Parsing cepat","p50 < 0,2 ms","Benchmark + log","Optimasi; ukur ulang","G3")
T("QA-SRV-02","6 Integrasi Rust","Memori server 60 menit","QA-SRV-01","Pantau pemakaian memori selama 60 menit beban","Memori stabil di bawah ambang","< 40 MB; tanpa tren naik","Log memori berkala","Optimasi; laporkan","G3")
T("QA-SRV-03","6 Integrasi Rust","Ketahanan parser bingkai rusak","Korpus bingkai rusak","Fuzz parser dengan bingkai tidak sah; pantau kegagalan","Server tetap hidup","Nol panic; bingkai rusak dibuang tercatat","Uji fuzz","Perbaiki; uji ulang","G3")
T("QA-SRV-04","6 Integrasi Rust","API + dasbor + klien Tauri","Integrasi penuh","Jalankan skenario daring/luring seluruh antarmuka","Seluruh alur berjalan","Semua alur lolos; transisi tercatat","Skenario uji tertulis","Perbaiki; jalur cadangan","G3")
T("QA-SRV-05","6 Integrasi Rust","Orkestrasi TTS/ASR server","Layanan ucapan terpasang","Uji pemanggilan, antrean, dan aliran audio end-to-end","Orkestrasi bekerja","Alur terverifikasi; kegagalan layanan tertangani","Log orkestrasi","Jalur cadangan D","G3")
T("QA-EDGE-01","7 Kuantisasi & Tepi","Dukungan operator runtime tepi","Graph ekspor tersedia","Verifikasi BatchNorm dan GELU pada ESP-DL / TFLM [23]","Operator didukung","Seluruh operator terverifikasi","Matriks operator","Ganti runtime; laporkan","G1")
T("QA-EDGE-02","7 Kuantisasi & Tepi","Kalibrasi kuantisasi affine int8","Data kalibrasi dari latih","Kalibrasi skala s dan titik nol (Persamaan 3.2); dokumentasikan distribusi","Kalibrasi terdokumentasi","Distribusi skala + titik nol tercatat","Laporan kalibrasi","Perluas data kalibrasi","G1")
T("QA-EDGE-03","7 Kuantisasi & Tepi","Paritas float vs int8","Model terkuantisasi","Bandingkan prediksi float vs int8 pada himpunan kecil","Prediksi konsisten","Kesesuaian ≥ 95% [usulan]; deviasi tercatat","Uji paritas","Evaluasi fp16/int4; fallback server","G1")
T("QA-EDGE-04","7 Kuantisasi & Tepi","Ukuran model + waktu inferensi","Modul nyata","Ukur ukuran model, RAM/PSRAM, inferensi per segmen p50/p95","Inferensi memenuhi target","p50 & p95 < 100 ms; memori terukur","Log inferensi","Klasifikasi pindah ke server (cadangan B)","G1, G3")
T("QA-EDGE-05","7 Kuantisasi & Tepi","Stabilitas + konsumsi arus","Purwarupa terpasang","Ukur arus pada beberapa kondisi kerja; estimasi baterai (3.4)","Arus terukur","Arus rata-rata tercatat; estimasi terlapor","Log arus","Sesuaikan target; laporkan","G3")
T("QA-EDGE-06","7 Kuantisasi & Tepi","Fallback inferensi server","Skenario gangguan","Simulasikan kegagalan tepi; verifikasi peralihan ke server","Peralihan bekerja","Transisi berhasil; durasi tercatat","Log skenario","Perbaiki; laporkan","G3")
T("QA-SPC-01","8 ASR/TTS & Komunikasi","ASR daring dan luring","Daftar frasa uji [PERLU DATA]","Rekam keluaran layanan awan dan faster-whisper; hitung WER + S/D/I/N + exact-match","WER terlapor tanpa 1-WER","WER + rincian + exact-match terlapor","Laporan ASR","Ganti layanan; laporkan","G3")
T("QA-SPC-02","8 ASR/TTS & Komunikasi","TTFA + durasi sintesis TTS","Mesin terpasang","Ukur TTFA dan durasi MMS-TTS-ind (utama) dan Kokoro (pembanding) pada frasa ≤ 5 kata","TTFA memenuhi target","TTFA p50 < 100 ms (kondisi terdokumentasi)","Log TTS","Pre-cache 26 klip dievaluasi; cadangan on-device/awan","G3")
T("QA-SPC-03","8 ASR/TTS & Komunikasi","Mutu sintesis Indonesia","Klip sampel per mesin","Minta penilaian manusia atas klip sintesis per mesin dan kondisi","Skor tercatat","Skor per mesin terlapor","Formulir penilaian","Keputusan mesin Tabel 3.7 no. 17","G3")
T("QA-SPC-04","8 ASR/TTS & Komunikasi","Pemutaran audio node RX","Aliran aktif","Putar audio via DAC I2S + penyangga cincin; hitung underrun","Pemutaran mulus","Underrun < 5% sesi [usulan]","Log pemutaran","Jalur cadangan C","G3")
T("QA-SPC-05","8 ASR/TTS & Komunikasi","Cakupan kamus + ejaan jari","Daftar kata uji","Hitung proporsi kata terwakili; verifikasi animasi J dan Z","Cakupan terukur; J/Z animasi benar","Proporsi terlapor; J/Z tampil beranimasi","Laporan cakupan","Batasi ke glos + ejaan (Tabel 3.8 no. 9)","G3")
T("QA-SPC-06","8 ASR/TTS & Komunikasi","Kondisi daring/luring/putus","Skenario gangguan","Jalankan skenario gangguan jaringan; catat transisi","Luring tetap berfungsi","Seluruh transisi tercatat","Log skenario","Perbaiki; laporkan","G3")
T("QA-UAT-01","9 Pengguna & Akses","Uji kegunaan 3-5 pengguna","Purwarupa terpasang; persetujuan tertulis","Jalankan skenario terbimbing; catat hambatan dan waktu","Hambatan terpetakan","Hambatan + waktu penyelesaian tercatat","Notulat uji","Perbaiki purwarupa; laporkan","G4")
T("QA-UAT-02","9 Pengguna & Akses","Kuesioner persepsi Likert [28]","QA-UAT-01 selesai","Tabulasi kuesioner; analisis deskriptif median/rentang","Skor memenuhi ambang usulan","Rata-rata ≥ 3,0/5 [usulan]","Rekap kuesioner","Hasil negatif tetap dilaporkan","G4")
T("QA-UAT-03","9 Pengguna & Akses","Penilaian validator kewajaran","Validator tunarungu berkefasihan","Bandingkan keluaran sistem vs penilaian validator dalam tabel silang","Kewajaran terverifikasi","Persetujuan tercatat; kasus keliru terpisah","Tabel silang","Sempitkan klaim; laporkan","G4")
T("QA-UAT-04","9 Pengguna & Akses","Kelengkapan etika & aksesibilitas","Protokol etika","Periksa persetujuan aksesibel, wali + persetujuan anak, retensi, re-identifikasi","Dokumen lengkap","Seluruh berkas etika lengkap","Berkas etika","Lengkapi sebelum sesi dimulai","G4")
T("QA-UAT-05","9 Pengguna & Akses","BOM dan biaya (Persamaan 3.5)","Pengadaan selesai","Isi BOM dari survei harga nyata; hitung total","BOM lengkap tanpa angka karangan","Seluruh sel terisi; total dinilai G4","Tabel BOM","Lengkapi survei; G4 ditunda","G4")
T("QA-UAT-06","9 Pengguna & Akses","Rubrik tiga pilar pakar","Rubrik disetujui (Tabel 3.7 no. 14)","Konsultasi pakar SIBI/RF/embedded AI; skor rubrik","Skor memenuhi ambang","Rata-rata per pilar ≥ 3/5; tanpa temuan blok","Formulir pakar","Perbaiki temuan; sempitkan klaim","G2")
style_sheet(ws2, [11, 18, 30, 26, 40, 30, 34, 24, 12, 30, 9])
for row in ws2.iter_rows(min_row=2, min_col=9, max_col=9):
    for c in row:
        c.fill = PatternFill("solid", fgColor="FFF2CC")  # kolom status diisi manual saat penelitian

# ============ 3. TRACEABILITY ============
ws3 = wb.create_sheet("Traceability")
ws3.append(["ID Kebutuhan", "Kebutuhan", "Desain (naskah)", "Implementasi / artefak (bukti audit)",
            "Uji", "Bukti uji", "Gerbang"])
TR = [
 ("R-01","Dua node ESP32-S3 satu kanal tanpa kamera pada inferensi akhir","2.3, 3.4, Tabel 3.1","RuView firmware v0.8.18 (3bae24a): STA + promiscuous + WIFI_PS_NONE (AUD-02)","QA-FW-02, QA-FW-03","Log boot + sesi","G0"),
 ("R-02","Akuisisi CSI dari trafik OFDM terjadwal (self-ping 10-50 Hz)","2.3, 3.7","csi_collector.c #954 self-ping + batas 50 Hz (AUD-02)","QA-ACQ-01, QA-ACQ-04","Log laju + analisis Delta-CSI","G0"),
 ("R-03","Transport UDP ADR-018 biner port 5005","2.3, 2.13","csi_collector.c ADR-018 + edge_processing (AUD-04)","QA-ACQ-07, QA-SRV-01","Uji parser + benchmark","G0, G3"),
 ("R-04","Atribusi bingkai ke tautan TX-RX (penandaan MAC)","2.3, 3.12 AUD-03","Pola patch kit wifi-sensing-kit (7fb77fc) di atas firmware sama (AUD-18)","QA-FW-04","Diff patch + keluaran parser","G0"),
 ("R-05","Encoder terpralatih beku dengan kontrak 8 fitur @1 Hz","2.4, 2.5","HF wifi-densepose-pretrained sha 98b29a35 (AUD-10); dua keluarga berkas (AUD-08)","QA-MDL-01","Skrip audit + log","G0b"),
 ("R-06","Guru visual YOLO26m-Pose 24 huruf statis","2.9, Tabel 2.2","WPC exp11_huruf24 (249a63d): mAP50 0,9580 (AUD-15)","QA-DS-02, QA-DS-03","Laporan anotasi + formulir verifikasi","G1"),
 ("R-07","Supervisi J/Z dari lintasan keypoint + label protokol","2.9, 3.7","AUD-15: exp11 tanpa kelas J/Z; kartu pemandu protokol","QA-EVL-03","Matriks kekeliruan","G1"),
 ("R-08","Dua kepala: 26 logit + regresi [T,21,2]","2.6-2.8, Persamaan 2.13/2.15","Rancangan naskah (tidak ada kode pelatihan murid pra-penelitian)","QA-MDL-03, QA-MDL-04","Uji unit + tabel ablasi","G1"),
 ("R-09","Mask efektif tanpa mewarisi visibilitas label","2.7, 2.9","AUD-12: write_label visibilitas konstan","QA-DS-02","Skrip + laporan anotasi","G1"),
 ("R-10","Pembagian data anti-kebocoran (split sebelum windowing, purge gap)","3.7, Tabel 3.4","Pola dedup/leak-guard WPC (AUD-14) diadopsi untuk dataset CSI","QA-EVL-01, QA-DS-05","Skrip audit split","G1"),
 ("R-11","Ablasi multitugas pada split + seed sama","3.7, 3.8.2","Rancangan naskah; resep deterministik WPC sebagai preseden (AUD-17)","QA-MDL-04","Tabel ablasi","G1"),
 ("R-12","Kompatibilitas representasi diuji sebelum pelatihan penuh (G0b)","3.7","Probe linear + uji permutasi (rancangan naskah)","QA-MDL-05","Laporan G0b","G0b"),
 ("R-13","Deployment Pilihan 1: graph terkuantisasi tanpa kepala regresi","3.7, Persamaan 3.2","Varian kuantisasi tersedia pada repo model (AUD-11); kinerja belum teruji","QA-EDGE-01..04","Matriks operator + log inferensi","G1, G3"),
 ("R-14","Fallback inferensi ke server saat tepi gagal","3.7, 3.11","Rancangan naskah (cadangan B)","QA-EDGE-06","Log skenario","G3"),
 ("R-15","Server Rust: orkestrasi, parsing, dasbor, klien","2.13","Rancangan naskah; target 0,2 ms / 40 MB diukur G3","QA-SRV-01..05","Benchmark + log","G3"),
 ("R-16","ASR Indonesia dengan WER + rincian S/D/I/N","2.14, Persamaan 2.23","Rancangan naskah; faster-whisper + layanan awan","QA-SPC-01","Laporan ASR","G3"),
 ("R-17","TTS Indonesia: MMS-TTS-ind utama + Kokoro pembanding, TTFA terukur","2.11, 3.5","Rujukan [24], [25]; keputusan Tabel 3.7 no. 17","QA-SPC-02, QA-SPC-03","Log TTS + formulir","G3"),
 ("R-18","Kamus kata SIBI + ejaan jari dengan animasi J/Z","2.12, 3.8.4","Kamus SIBI [3]; aset tampilan arah kedua","QA-SPC-05","Laporan cakupan","G3"),
 ("R-19","Uji kegunaan + validator kewajaran keluaran","3.8.5","Instrumen kuesioner [28] + validator","QA-UAT-01..03","Notulat + tabel silang","G4"),
 ("R-20","Etika: persetujuan aksesibel, wali, retensi, re-identifikasi","3.6","Protokol etika naskah","QA-UAT-04","Berkas etika","G4"),
 ("R-21","BOM + biaya dari survei nyata","3.4, Persamaan 3.5","Kerangka BOM 8 baris tanpa angka tebakan (v20)","QA-UAT-05","Tabel BOM","G4"),
 ("R-22","Rubrik tiga pilar pakar","3.8.6","Tabel 3.7 no. 14 (rubrik disetujui sebelum G2)","QA-UAT-06","Formulir pakar","G2"),
]
for r in TR:
    ws3.append(r)
style_sheet(ws3, [12, 44, 22, 44, 22, 24, 9])

# ============ 4. KEPUTUSAN TERBUKA ============
ws4 = wb.create_sheet("Keputusan Terbuka")
ws4.append(["No.", "Parameter / keputusan", "Waktu atau dasar penetapan", "Status", "Sumber"])
KP = [
 (1,"Finalisasi ambang seluruh gerbang G0-G4","Sebelum gerbang dinilai","PERLU DATA: finalisasi bersama pembimbing","Tabel 3.7 no. 1"),
 (2,"Ambang G1, tindakan gagal kedua, kriteria pemangkasan","Sebelum eksperimen","PERLU DATA","Tabel 3.7 no. 2"),
 (3,"Kriteria kualitas model guru","Sebelum pelatihan murid","PERLU DATA","Tabel 3.7 no. 3"),
 (4,"Pemilihan subcarrier, lintasan puncak, segmentasi huruf statis","Sebelum dipakai","PERLU DATA","Tabel 3.7 no. 4"),
 (5,"Pembagian data dan strategi Widar3.0","Sebelum dipakai","PERLU DATA","Tabel 3.7 no. 5"),
 (6,"Jalur masukan encoder + keluarga berkas checkpoint + T","Audit T0 dan G0b","PERLU VALIDASI (diperluas AUD-07/08)","Tabel 3.7 no. 6"),
 (7,"Sistem koordinat regresi, handedness, d_ref, alpha","Sebelum pelatihan","PERLU VALIDASI","Tabel 3.7 no. 7"),
 (8,"Modul temporal final (1D-CNN atau agregasi)","Dari hasil ablasi","PERLU DATA","Tabel 3.7 no. 8"),
 (9,"Bobot lambda_cls, lambda_reg, ambang keyakinan","Dari data validasi","PERLU DATA","Tabel 3.7 no. 9"),
 (10,"Peringkat LoRA r dan lapis disadap","Sebelum adaptasi","PERLU VALIDASI","Tabel 3.7 no. 10"),
 (11,"Perlakuan data uji","Sebelum dipakai","PERLU DATA","Tabel 3.7 no. 11"),
 (12,"Inklusi partisipan, sesi per ruang, token apresiasi","Sebelum dipakai","PERLU DATA","Tabel 3.7 no. 12"),
 (13,"Publikasi dataset dan persetujuan etik","Sebelum dipakai","PERLU DATA","Tabel 3.7 no. 13"),
 (14,"Rubrik tiga pilar pakar","Sebelum G2","PERLU DATA","Tabel 3.7 no. 14"),
 (15,"Indikator layak operasional + durasi pengamatan deteksi palsu","Sebelum G3","PERLU DATA","Tabel 3.7 no. 15"),
 (16,"Kanal, jarak antarmodul, zona, layar, audio, kapasitas baterai","T0 / sebelum T4","PERLU DATA","Tabel 3.7 no. 16"),
 (17,"Prioritas mesin TTS (MMS-TTS-ind kandidat utama; Kokoro pembanding)","Pada G3","PERLU KONFIRMASI","Tabel 3.7 no. 17"),
 (18,"Kuesioner, rubrik validator/pakar, asumsi biaya","Sebelum T4","PERLU DATA","Tabel 3.7 no. 18"),
 (19,"Model deployment (Pilihan 1 lawan Pilihan 2)","Hasil ablasi + konfirmasi","PERLU KONFIRMASI","Tabel 3.7 no. 19"),
 (20,"Akhiran judul (PEMROSESAN SERVER / CLOUD PROCESSING)","Kesesuaian arsitektur","PERLU DATA","Tabel 3.7 no. 20"),
 (21,"Peran ESP-NOW (dikeluarkan dari jalur inti)","Keputusan pemilik 14 Nov 2026","Ditetapkan","Tabel 3.7 no. 21"),
 (22,"Mekanisme akuisisi CSI baseline (self-ping + promiscuous; NDP stub tidak dipakai; atribusi MAC)","Audit kode 15 Nov 2026","Ditetapkan (baru, gelombang 21)","Tabel 3.7 no. 22; AUD-01..04"),
 (23,"Penerbitan tag rilis + hash bobot exp11","Menunggu pemilik","NOT VERIFIED (AUD-16)","Register AUD-16; rujukan [12]"),
 (24,"Identitas penulis, NIM, program studi, universitas, pembimbing, tahun","Sebelum pengumpulan","PERLU DATA (sampul)","Tabel identitas sampul"),
]
for r in KP:
    ws4.append(r)
style_sheet(ws4, [6, 56, 26, 26, 24])

# ============ 5. CHANGELOG ============
ws5 = wb.create_sheet("Changelog v20-v21")
ws5.append(["Aspek", "v20", "v21"])
CH = [
 ("Mekanisme akuisisi CSI (narasi)","TX menyuntikkan bingkai sounding NDP","TX penjana trafik OFDM self-ping 10-50 Hz + callback CSI promiscuous; NDP stub ADR-029 tidak dipakai (AUD-01); Tabel 3.7 no. 22 baru"),
 ("Atribusi bingkai TX-RX","Tidak dibahas","Penandaan MAC pengirim pola kit [34] diuji T0 (AUD-03; QA-FW-04)"),
 ("Klaim NUL-padding checkpoint","model.safetensors ditolak safetensors","Diperbaiki 13 Okt 2026 (komi 98b29a35); T0 tetap memverifikasi (AUD-07)"),
 ("Metadata kartu model","Dua keluarga berkas disebut singkat","Inkonsistensi lengkap dicatat + rekonsiliasi T0 (AUD-08); SISO dikutip ke [10] saja (AUD-09)"),
 ("Visibilitas label guru","Disebut sebagai mask dari guru","Label konstan '2' (AUD-12); mask = langkah valid + saringan kualitas + verifikasi sampel; Tabel 3.8 no. 14 baru"),
 ("Kelas J/Z pada guru","[PERLU VALIDASI] terbuka","Terjawab: exp11 = A-Y tanpa J/Z (AUD-15); fakta audit menggantikan penanda"),
 ("Bobot exp11","[PERLU DATA] terbuka","Tetap terbuka + bukti baru: bobot belum diarsipkan (AUD-16)"),
 ("Subbab baru","-","3.12 Brief Audit Teknis (Tabel 3.9-3.10); 3.13 Rencana Penjaminan Mutu (Tabel 3.11-3.20; 54 uji QA 9 lapis)"),
 ("Gerbang","G0-G4 + G0b","Tetap; QA terikat tanpa gerbang baru (Tabel 3.11)"),
 ("Daftar pustaka","33 entri","35 entri (+[34] wifi-sensing-kit, +[35] DensePose From WiFi pracetak)"),
 ("Tabel konten","13","25 (bertambah 12 tabel audit/QA)"),
 ("Heading","4 H1 + 34 H2 + 8 H3","4 H1 + 36 H2 + 22 H3"),
 ("Halaman PDF","68","84"),
 ("Ruang lingkup","26 huruf SIBI (24 statis + J/Z); dua kepala; Pilihan 1","Tidak berubah"),
 ("Berkas pendamping","-","Register-Audit-Teknis-v21.md + SenseSIBI-v21-Audit-QA.xlsx"),
]
for r in CH:
    ws5.append(r)
style_sheet(ws5, [30, 40, 66])

wb.save(OUT)
print("Tersimpan:", OUT)
import openpyxl
w = openpyxl.load_workbook(OUT)
for s in w.sheetnames:
    print(f"  {s}: {w[s].max_row-1} baris data, {w[s].max_column} kolom")
