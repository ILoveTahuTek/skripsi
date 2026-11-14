#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Revisi v17 -> v18 (gelombang 18): paket perbaikan reviewer + ESP-NOW turun ke fitur opsional
+ pemadatan menyeluruh + 4 rujukan baru ([29] Permenristekdikti, [30] DensePose From WiFi,
[31] DF-WiSLR, [32] Wi-SignFi). BAB II dirakit ulang 17 -> 12 subbab (bab2_v18.txt)."""
import re, sys
from pathlib import Path

V10 = Path("/home/z/my-project/download/sensesibi-v10")
SCR = Path("/home/z/my-project/scripts/sensesibi-v10")
src = (V10 / "Proposal-SenseSIBI-v17.md").read_text(encoding="utf-8")
bab2 = (SCR / "bab2_v18.txt").read_text(encoding="utf-8").strip() + "\n"

MARK = "<!-- ===== AKHIR NASKAH"

# ---------- 1) ganti seluruh BAB II ----------
i2 = src.index("# BAB II KAJIAN PUSTAKA")
i3 = src.index("# BAB III METODE PENELITIAN")
pre = src[:i2]                      # header identitas + BAB I
post = src[i3:]                     # BAB III + DP + log
tubuh = pre + bab2 + "\n" + post
naskah, log = tubuh[:tubuh.index(MARK)], tubuh[tubuh.index(MARK):]

# ---------- 2) penomoran ulang (HANYA BAB I [pre] dan BAB III+DP [post];
# BAB II baru sudah memakai penomoran final sehingga tidak boleh tersentuh) ----------
MAP_SUBBAB = {"1":"1","2":"2","3":"2","4":"3","5":"3","6":"4","7":"4","8":"4","9":"5",
              "10":"6","11":"7","12":"7","13":"8","14":"9","15":"10","16":"11","17":"12"}
def sub_sub(m):
    return "Subbab 2." + MAP_SUBBAB[m.group(1)]

# Tabel BAB III bergeser karena BOM baru menjadi Tabel 3.2 (satu kali, injektif)
MAP_TABEL = {"2":"3","3":"4","4":"5","5":"6","6":"7","7":"8","8":"9"}
def sub_tabel(m):
    return "Tabel 3." + MAP_TABEL[m.group(1)]

# log historis di bawah penanda AKHIR NASKAH tidak boleh ikut dinomori ulang
mark_pos = post.index(MARK)
post_body, post_log = post[:mark_pos], post[mark_pos:]

# Gambar 2.2 (arsitektur model) menjadi Gambar 2.1 (Gambar 2.1 fresnel dihapus)
pre = re.sub(r"Subbab 2\.(\d+)(?=[\s.,;:)\]]|$)", sub_sub, pre)
pre = re.sub(r"Tabel 3\.([2-8])(?=[\s.,;:#)\]]|$)", sub_tabel, pre)
pre = pre.replace("Gambar 2.2", "Gambar 2.1")
post_body = re.sub(r"Subbab 2\.(\d+)(?=[\s.,;:)\]]|$)", sub_sub, post_body)
post_body = re.sub(r"Tabel 3\.([2-8])(?=[\s.,;:#)\]]|$)", sub_tabel, post_body)
post_body = post_body.replace("Gambar 2.2", "Gambar 2.1")

naskah = pre + bab2 + "\n" + post_body
log = post_log

EDITS = []
def G(old, new, n=1):
    EDITS.append((old, new, n))

# ---------- 3) BAB I ----------
G("Anak tunarungu hampir selalu lahir dari orang tua yang bisa mendengar. Sejak hari-hari pertama, komunikasi di rumah berjalan dengan dua bahasa yang tidak saling mengerti: orang tua berbicara dengan suara, anak menjawab dengan isyarat. Orang tua lalu harus mempelajari bahasa isyarat dari nol, padahal waktu dan kesempatan berlatih serba terbatas.",
  "Sebagian besar anak tunarungu tumbuh di dalam keluarga penutur dengar yang belum menguasai bahasa isyarat sejak awal. Sejak hari-hari pertama, komunikasi di rumah kerap berjalan dalam dua saluran bahasa yang belum saling menjembatani: orang tua berbicara dengan suara, anak menjawab dengan isyarat, sementara waktu dan kesempatan belajar bahasa isyarat serba terbatas.")
G("Penelusuran pada Google Scholar, Crossref, dan OpenAlex hingga Oktober 2026 belum menemukan satu pun penerapan CSI untuk isyarat SIBI.",
  "Penelusuran pada Google Scholar, Crossref, dan OpenAlex hingga Oktober 2026 belum menemukan satu pun penerapan CSI untuk isyarat SIBI maupun purwarupa dua arah sejenis; ketiadaan itu dicatat sebagai batas penelusuran basis data terkait (Subbab 2.10).")
G("Perangkat yang dibutuhkan pun sederhana dan murah. Modul ESP32-S3, mikrokontroler seharga sekitar Rp150.000, sudah memiliki radio Wi-Fi 2,4 GHz dengan dukungan CSI resmi [8], [9]. Dua modul cukup untuk satu pasang: yang satu memancarkan sinyal, yang lain menangkapnya. Zona isyarat berada di antara keduanya. *Firmware* penangkap CSI yang teruji untuk modul ini tersedia pada platform terbuka RuView [10]. Biaya sepasang node lengkap diperkirakan di bawah Rp350.000, jauh lebih ringan daripada kamera ditambah komputer pengolah citra. Murah di sini bukan soal angka semata; harga yang terjangkau mengundang sekolah berani memasang alat ini di lebih dari satu ruang.",
  "Perangkat yang dibutuhkan pun sederhana. Modul ESP32-S3, mikrokontroler seharga sekitar Rp150.000, sudah memiliki radio Wi-Fi 2,4 GHz dengan dukungan CSI resmi [8], [9]. Dua modul cukup untuk satu pasang: yang satu menyediakan lalu lintas Wi-Fi sebagai sumber bingkai CSI, yang lain menangkapnya dalam mode *promiscuous*; zona isyarat berada di antara keduanya. *Firmware* penangkap CSI yang teruji untuk modul ini tersedia pada platform terbuka RuView [10]. Sepasang modul inti diperkirakan sekitar Rp300.000, lebih ringan daripada kamera ditambah komputer pengolah citra; total biaya node lengkap dengan layar, audio, baterai, dan *enclosure* disusun lewat daftar komponen (BOM) yang diisi dari survei dan dinilai pada gerbang G4 [PERLU DATA: total BOM purwarupa lengkap] (Tabel 3.2), bukan diklaim murah sebelum rinciannya ada. Harga yang terjangkau mengundang sekolah berani memasang alat ini di lebih dari satu ruang.")
G("Representasinya dibekukan, lalu dua kepala tugas dilatih di atasnya: satu kepala mengenali 26 kelas huruf, satu lagi memperkirakan 21 titik jari tangan.",
  "Representasinya dibekukan, lalu adapter masukan (jika dipakai), modul temporal, dan dua kepala tugas dilatih di atasnya: satu kepala mengenali 26 kelas huruf, satu lagi memperkirakan 21 titik jari tangan.")
G("apakah *embedding* hasil pretraining kontrastif pada CSI masih informatif untuk gestur jari jika hanya dua kepala tugasnya yang dilatih.",
  "apakah *embedding* hasil pretraining kontrastif pada CSI masih informatif untuk gestur jari apabila *encoder* dibekukan dan hanya adapter masukan (jika dipakai), modul temporal, serta kedua kepala tugasnya yang dilatih.")

# ---------- 4) BAB III : 3.1, 3.2 ----------
G("kriteria akurasi dirumuskan relatif terhadap peluang acak (Subbab 2.9). Inti pelatihannya adalah supervisi lintas modalitas berpandu guru (Subbab 3.7): label kelas dari protokol perekaman serta deret 21 *keypoint* dari guru kamera YOLO26m-Pose mengawasi pelatihan dua kepala tugas di atas *encoder* CSI terpralatih yang dibekukan.",
  "kriteria akurasi dirumuskan relatif terhadap peluang acak (Subbab 2.9). Inti pelatihannya adalah supervisi lintas modalitas berpandu guru (Subbab 3.7): label kelas dari protokol perekaman serta deret 21 *keypoint* dari guru kamera YOLO26m-Pose mengawasi pelatihan adapter masukan (jika dipakai), modul temporal, dan dua kepala tugas di atas *encoder* CSI terpralatih yang dibekukan.")
G("penerimaan pengguna dan biaya dinilai G4, yang kemudian menyusun rekomendasi posisi TKT/TRL 3–4 [27].",
  "penerimaan pengguna dan biaya dinilai G4, yang kemudian menyusun rekomendasi posisi TKT/TRL 3–4 [27], [29].")
G("Tahap T0 sampai T2 lebih dulu membangun dasar data. T0 menyiapkan dua modul dengan *firmware* `esp32-csi-node` RuView [10], lalu menjalankan empat uji tanpa partisipan. Uji itu mencakup verifikasi 56 *subcarrier* stabil pada jarak baku 1 meter, uji Delta-CSI (Subbab 3.8.1), koeksistensi radio dengan *streaming* audio aktif, dan pengukuran laju pencuplikan. T0 juga mengaudit *checkpoint encoder* [11]: bentuk masukan, parameter normalisasi masukan, jumlah parameter, normalisasi L2, dukungan ekspor, dan kompatibilitas LoRA (Subbab 3.7). T1 meliputi kurasi 26 huruf bersama validator, kalibrasi ruang, protokol dan etika, serta perizinan (Subbab 3.6); pasangan huruf paling mirip juga ditetapkan di sini sebagai bahan gerbang G1.",
  "Tahap T0 sampai T2 lebih dulu membangun dasar data. T0 menyiapkan dua modul dengan *firmware* `esp32-csi-node` RuView [10] lalu menjalankan empat uji tanpa partisipan: verifikasi N~valid~ *subcarrier* stabil pada jarak baku 1 meter, uji Delta-CSI (Subbab 3.8.1), koeksistensi radio dengan *streaming* audio aktif [PERLU DATA: format audio, laju cuplik, mekanisme pengaliran, dan penanganan paket hilang], serta pengukuran laju pencuplikan. T0 juga mengaudit *checkpoint encoder* [11]: bentuk masukan, parameter normalisasi masukan, jumlah parameter, normalisasi L2, dukungan ekspor, kompatibilitas LoRA, kedua set berkas *checkpoint* (model.* dan csi-embed-v2.*), jenis bingkai yang menjadi sumber CSI, serta versi dan *commit* RuView yang dipakai [PERLU DATA: versi dan commit RuView] (Subbab 3.7). T1 meliputi kurasi 26 huruf bersama validator, kalibrasi ruang, protokol dan etika, perizinan, serta penentuan pasangan huruf paling mirip sebagai bahan gerbang G1 (Subbab 3.6).")
G("Tahap T3 sampai T5 berisi pengujian dan pelaporan. Generalisasi lintas sesi, partisipan, ruang, serta posisi berdiri-duduk diuji pada T3, termasuk pada satu pengguna baru tanpa pelatihan ulang (Subbab 3.7) dengan acuan Widar3.0 [14]. Jika ketahanan lintas pengguna rendah, cakupan berubah menjadi personalisasi per pengguna dan dilaporkan sebagai temuan. T4 mengemas model menjadi purwarupa dua arah (Subbab 3.5), menjalankan uji operasional dan jalur ucapan (Subbab 3.8) yang dinilai G3. Rangkaian itu ditutup uji penerimaan, penilaian validator, dan analisis biaya yang dinilai G4. Pada T5, seluruh artefak dianalisis dan laporan kelayakan disusun lengkap dengan rekomendasi TKT/TRL 3–4 [27] beserta keterbatasan eksplisitnya (Subbab 1.4).",
  "Tahap T3 sampai T5 berisi pengujian dan pelaporan. Generalisasi lintas sesi, partisipan, ruang, serta posisi berdiri-duduk diuji pada T3, termasuk pada satu pengguna baru tanpa pelatihan ulang dengan acuan Widar3.0 [14]; jika ketahanan lintas pengguna rendah, cakupan berubah menjadi personalisasi per pengguna dan dilaporkan sebagai temuan. T4 mengemas model menjadi purwarupa dua arah (Subbab 3.5) lalu menjalankan uji operasional dan jalur ucapan (Subbab 3.8) yang dinilai G3; rangkaian ditutup uji penerimaan, penilaian validator, dan analisis biaya yang dinilai G4. Pada T5, seluruh artefak dianalisis dan laporan kelayakan disusun lengkap dengan rekomendasi TKT/TRL 3–4 [27], [29] beserta keterbatasan eksplisitnya (Subbab 1.4).")

# ---------- 5) BAB III : 3.4 (alat bahan + BOM + ESP-NOW) ----------
G("Tabel 3.1 dan Tabel 3.3 menyajikan perangkat keras dan perangkat lunak penelitian. Node penginderaan dipegang sepasang modul ESP32-S3: TX memancarkan *beacon* ESP-NOW, sedangkan RX mengekstrak CSI 56 *subcarrier* pada 2,4 GHz kanal 20 MHz sekaligus memuat antarmuka.",
  "Tabel 3.1 dan Tabel 3.3 menyajikan perangkat keras dan perangkat lunak penelitian. Node penginderaan dipegang sepasang modul ESP32-S3: TX menyediakan lalu lintas Wi-Fi baku sebagai sumber bingkai CSI, sedangkan RX mengekstrak CSI N~valid~ *subcarrier* pada 2,4 GHz kanal 20 MHz sekaligus memuat antarmuka; ESP-NOW hanya kandidat fitur sinkronisasi opsional (Subbab 2.2).")
G("| 1 | Modul ESP32-S3 | PSRAM 8 MB; 2,4 GHz 802.11b/g/n, kanal 20 MHz (56 *subcarrier*), 1T1R; varian yang direkomendasikan RuView [10] | 2 unit | Node TX (pemancar *beacon*) dan node RX (penerima CSI dan antarmuka) |",
  "| 1 | Modul ESP32-S3 | PSRAM 8 MB; 2,4 GHz 802.11b/g/n, kanal 20 MHz (56 *subcarrier*), 1T1R; varian yang direkomendasikan RuView [10] | 2 unit | Node TX (sumber lalu lintas Wi-Fi) dan node RX (penerima CSI dan antarmuka) |")
G("Foto pada Gambar 3.2 memudahkan mengenali bentuk sembilan perangkat pada Tabel 3.1;",
  "Harga komponen dirangkum pada Tabel 3.2 sebagai kerangka daftar komponen (BOM) rencana; seluruh harga diisi dari survei pemasok sebelum gerbang G4 dan tidak ditebak lebih dahulu [PERLU DATA: harga satuan komponen dan sumber rujukan].\n\nTabel 3.2 Kerangka BOM rencana sepasang node lengkap\n\n| No. | Komponen | Jumlah | Harga satuan (Rp) | Subtotal (Rp) | Sumber harga |\n|---|---|---|---|---|---|\n| 1 | Modul ESP32-S3 (TX dan RX) | 2 unit | [PERLU DATA] | [PERLU DATA] | [PERLU DATA] |\n| 2 | Layar modul final (OLED 0,96 inci atau TFT 1,3 inci) | 1 unit | [PERLU DATA] | [PERLU DATA] | [PERLU DATA] |\n| 3 | *Rotary encoder* EC11 dan tombol PTT/reset | 1–2 set | [PERLU DATA] | [PERLU DATA] | [PERLU DATA] |\n| 4 | Mikrofon I2S INMP441 | 1 unit | [PERLU DATA] | [PERLU DATA] | [PERLU DATA] |\n| 5 | DAC I2S MAX98357A dan *speaker* 8 Ohm 3 W | 1 set | [PERLU DATA] | [PERLU DATA] | [PERLU DATA] |\n| 6 | Baterai Li-Po (kapasitas final), BMS 1S, TP4056, dan komponen pasif | 1–2 set | [PERLU DATA] | [PERLU DATA] | [PERLU DATA] |\n| 7 | *Enclosure* cetak 3D serta kabel, *header*, dan PCB | 2 set | [PERLU DATA] | [PERLU DATA] | [PERLU DATA] |\n| — | Total sepasang node lengkap (di luar laptop, ponsel, dan AP) | — | — | [PERLU DATA] | — |\n\nFoto pada Gambar 3.2 memudahkan mengenali bentuk sembilan perangkat pada Tabel 3.1;")
G("Gambar 3.2 Perangkat keras penelitian; huruf pada tiap foto mengikuti baris Tabel 3.1 (foto produk sebagai pengenal bentuk, bukan acuan merek)",
  "Gambar 3.2 Perangkat keras penelitian; huruf pada tiap foto mengikuti baris Tabel 3.1 (foto produk hanya ilustrasi pengenal bentuk sebelum pengadaan dan perakitan, bukan acuan merek)")
G("| 8 | faster-whisper dan MMS-TTS-ind [26], [25]; layanan ucapan awan [PERLU DATA: layanan final hasil uji banding] | ASR cadangan lokal (faster-whisper); alternatif TTS lokal (MMS-TTS-ind); ASR utama saat daring |",
  "| 8 | faster-whisper [26]; MMS-TTS-ind [25]; layanan ASR awan [PERLU DATA: layanan final hasil uji banding] | ASR luring (faster-whisper); kandidat utama TTS Indonesia (MMS-TTS-ind); ASR utama saat daring |")
G("| 10 | Kokoro TTS ONNX dan ONNX Runtime [24] | Mesin TTS utama di server lokal dan cadangan *on-device* di ponsel; prasyarat suara Indonesia pada G3 |",
  "| 10 | Kokoro TTS ONNX dan ONNX Runtime [24] | Kokoro terverifikasi tanpa bahasa Indonesia (14 Nov. 2026), diuji ulang bila rilis berikutnya menyediakannya [PERLU KONFIRMASI: Tabel 3.8 #17]; ONNX Runtime menjalankan TTS *on-device* di ponsel |")

# ---------- 6) BAB III : 3.5 ----------
G("Pada arah pertama, *beacon* ESP-NOW node pemancar melintasi zona isyarat, gerak pengisyarat mengubah deret CSI yang ditangkap node penerima,",
  "Pada arah pertama, lalu lintas Wi-Fi node pemancar melintasi zona isyarat, gerak pengisyarat mengubah deret CSI yang ditangkap node penerima,")
G("Node pemancar memancarkan *beacon* sebagai sumber bingkai CSI, sedangkan node penerima mengirim bingkai, label, dan skor melalui UDP kepada server Rust sebagai telemetri riset. Server lokal menjalankan server RuView, server Rust, faster-whisper sebagai ASR cadangan, serta TTS Kokoro/MMS sebagai jalur utama sintesis luring.",
  "Node pemancar menyediakan lalu lintas Wi-Fi baku sebagai sumber bingkai CSI, sedangkan node penerima mengirim bingkai, label, dan skor melalui UDP kepada server Rust sebagai telemetri riset; sinkronisasi antarmodul, bila diperlukan, memakai ESP-NOW sebagai fitur opsional (Subbab 2.2). Server lokal menjalankan server RuView, server Rust, faster-whisper sebagai ASR luring, serta mesin TTS dengan MMS-TTS-ind sebagai kandidat utama dan Kokoro bila suara Indonesia tersedia.")
G("Pemetaan pin GPIO pada Tabel 3.4 dipilih agar tidak menabrak pin *strapping* (GPIO 0, 3, 45, 46) maupun kanal USB bawaan papan [8], dan diverifikasi ulang pada T0.",
  "Pemetaan pin GPIO pada Tabel 3.4 dipilih agar tidak menabrak pin *strapping* (GPIO 0, 3, 45, 46) maupun kanal USB bawaan papan [8], dan diverifikasi ulang pada unit papan fisik saat T0, mencakup jalur USB, kanal ADC1, potensi konflik periferal I2C/I2S/SPI, serta revisi papan [PERLU DATA: revisi papan final].")
G("Rantai dayanya tersusun atas baterai, BMS 1S, TP4056, dan regulator 3,3 volt papan; tegangan baterai diukur lewat pembagi tegangan sehingga persentase baterai bisa tampil di layar. [PERLU DATA: berkas model enclosure final]",
  "Rantai dayanya tersusun atas baterai, BMS 1S, TP4056, dan regulator 3,3 volt papan; tegangan baterai diukur lewat pembagi tegangan sehingga persentase baterai bisa tampil di layar. Kecukupan arus puncak saat Wi-Fi dan *speaker* aktif serta keamanan pengisian daya sambil beroperasi diverifikasi pada uji bangku T0/G3 [PERLU DATA: profil arus puncak, regulasi beban saat pengisian, dan kapasitas baterai final]. [PERLU DATA: berkas model enclosure final]")
G("Mesin sintesis utamanya berjalan di server lokal dengan Kokoro-82M ONNX yang diinferensikan luring [24], sementara jalur cadangan *on-device* berjalan di ponsel lewat ONNX Runtime di dalam Tauri. Target latensinya didefinisikan sebagai waktu menuju audio pertama (*time-to-first-audio*, TTFA) di bawah 100 ms pada frasa uji paling banyak lima kata; durasi sintesis keseluruhan dilaporkan terpisah. Prasyaratnya hanya satu, yaitu tersedia suara bahasa Indonesia pada Kokoro; jika belum, jalur beralih ke MMS-TTS-ind [25] dan peralihan itu dilaporkan.",
  "Mesin sintesis utamanya berjalan di server lokal dengan MMS-TTS-ind sebagai kandidat utama operasional [25], setelah verifikasi 14 November 2026 membuktikan Kokoro-82M v1.0 tanpa suara bahasa Indonesia [24]; Kokoro diuji ulang bila rilis berikutnya menyediakannya [PERLU KONFIRMASI: Tabel 3.8 #17]. Jalur cadangan *on-device* berjalan di ponsel lewat ONNX Runtime di dalam Tauri. Target latensinya didefinisikan sebagai waktu menuju audio pertama (*time-to-first-audio*, TTFA) di bawah 100 ms pada frasa uji paling banyak lima kata, dilaporkan menurut persentil p50 dan p95 pada lingkungan uji terdokumentasi [PERLU DATA: konfigurasi CPU/GPU, runtime, presisi model, dan opsi pre-cache audio huruf tunggal]; durasi sintesis keseluruhan dilaporkan terpisah.")

# ---------- 7) BAB III : 3.6 protokol ----------
G("4. Menjalankan `scripts/collect-ground-truth.py` supaya perekaman CSI dan *webcam* berjalan sinkron dengan penanda waktu bersama, lalu memverifikasi ulang kualitas sinkronisasi lewat uji kejadian di awal sesi, misalnya satu ketukan tangan yang terbaca kedua sensor [PERLU DATA: toleransi sinkronisasi yang diterima].",
  "4. Menjalankan `scripts/collect-ground-truth.py` dengan sumber penanda waktu tunggal supaya perekaman CSI dan *webcam* berjalan sinkron, lalu memverifikasi ulang kualitas sinkronisasi lewat uji kejadian di awal sesi, misalnya satu ketukan tangan yang terbaca kedua sensor [PERLU DATA: sumber clock final, resolusi waktu, toleransi sinkronisasi, metode penyelarasan dan pensampelan ulang keypoint ke pusat jendela, serta penanganan bingkai hilang].")
G("5. Memunculkan kartu pemandu huruf target, merekam satu repetisi, memberi jeda, lalu mengulanginya sampai setiap huruf mencapai kurang lebih 30 repetisi.",
  "5. Memunculkan kartu pemandu huruf target dengan urutan huruf yang diacak di dalam setiap blok, merekam satu repetisi, memberi jeda, lalu mengulanginya sampai setiap huruf mencapai kurang lebih 30 repetisi; jumlah repetisi yang benar-benar terpakai per kelas dan per sesi dicatat setelah pembuangan segmen bermasalah.")
G("6. Membuang segmen yang tangan tidak terdeteksi model guru, yang mengalami *jitter* *keypoint* ekstrem, atau yang terpotong, lalu mencatat tingkat segmen terbuang dan skor kualitas anotasi tiap segmen.",
  "6. Membuang segmen yang tangan tidak terdeteksi model guru, yang mengalami *jitter* *keypoint* ekstrem, atau yang terpotong, lalu mencatat tingkat segmen terbuang dan skor kualitas anotasi tiap segmen; kualitas deteksi *keypoint* pada gerakan dinamis J dan Z dievaluasi khusus (laju deteksi berhasil, *jitter*, bingkai hilang, dan validitas lintasan) karena performa exp11_huruf24 hanya terukur pada 24 pose statis [PERLU DATA: ambang batas jitter dan laju deteksi minimum].")
G("7. Meminta validator mengambil sampel segmen untuk memeriksa kebenaran bentuk isyarat; label guru berstatus *pseudo-label* sampai pemeriksaan ini selesai.",
  "7. Meminta validator mengambil sampel segmen untuk memeriksa kebenaran bentuk isyarat [PERLU DATA: proporsi sampel dan jumlah penilai]; label guru berstatus *pseudo-label* sampai pemeriksaan ini selesai.")
G("Video semata-mata dipakai untuk verifikasi batas segmen, penyaringan kualitas, dan diagnosis; penyimpanannya terbatas dan tidak dipublikasikan.",
  "Video semata-mata dipakai untuk verifikasi batas segmen, penyaringan kualitas, dan diagnosis; penyimpanannya terbatas, tidak dipublikasikan, dan dihapus permanen setelah verifikasi serta ekstraksi selesai [PERLU DATA: durasi retensi, batas kontrol akses berkas, dan prosedur penghapusan]. Formulir persetujuan disajikan dalam format yang mudah diakses dan dipahami partisipan tunarungu; bila ada partisipan di bawah umur, persetujuan orang tua atau wali beserta *assent* anak wajib disertakan, atau partisipan dibatasi pada kelompok dewasa. Potensi risiko identifikasi ulang dari metadata, pola kinematika, dan suara diakui secara terbuka tanpa klaim anonimitas mutlak.")

# ---------- 8) BAB III : 3.7 ----------
G("Deret CSI dipotong menjadi segmen huruf dengan segmentasi energi gerak memakai Delta-CSI, yaitu rata-rata besar perubahan koefisien kanal kompleks antarbingkai pada seluruh 56 *subcarrier*:",
  "Deret CSI dipotong menjadi segmen huruf dengan segmentasi energi gerak memakai Delta-CSI, yaitu rata-rata besar perubahan koefisien kanal kompleks antarbingkai pada seluruh *subcarrier* valid n ∈ N~valid~ (himpunan *subcarrier* data efektif hasil audit T0; Subbab 2.2):")
G("d( t ) = ( 1 / 56 ) · Σ~n~ | h~n~(t) − h~n~( t − 1 ) | (3.1)",
  "d( t ) = ( 1 / |N~valid~| ) · Σ~n∈Nvalid~ | h~n~(t) − h~n~( t − 1 ) | (3.1)")
G("d~|H|~( t ) = ( 1 / 56 ) · Σ~n~ | |h~n~(t)| − |h~n~( t − 1 )| |",
  "d~|H|~( t ) = ( 1 / |N~valid~| ) · Σ~n∈Nvalid~ | |h~n~(t)| − |h~n~( t − 1 )| |")
G("Segmen dianggap memuat gerak jika d(t) melampaui ambang τ selama sekurang-kurangnya panjang jendela minimum; J dan Z terpotong jelas dari energinya, sedangkan huruf statis memakai jendela tahan pose yang ambang dan panjangnya ditetapkan dari data validasi, bukan dari data uji (Tabel 3.8). Fitur tiap segmen, yaitu amplitudo dan fase *subcarrier* terpilih serta spektrum Doppler [6], [14], diringkas menjadi masukan *encoder*.",
  "Segmentasi memisahkan dua fase: deteksi *onset* gerak dari Delta-CSI (d(t) melampaui ambang τ), lalu untuk 24 huruf statis jendela penahanan pose (*pose-hold*) selama durasi observasi tetap untuk klasifikasi statis, sedangkan untuk J dan Z jendela lintasan penuh dari *onset* sampai *offset* gerak; seluruh ambang dan durasi ditetapkan dari data validasi, bukan dari data uji (Tabel 3.8) [PERLU VALIDASI: ambang onset, durasi pose-hold, dan offset].")
G("Langkah berikutnya menutup temuan audit Subbab 2.3: bentuk masukan *checkpoint* harus disesuaikan sebelum dipakai. Kartu model mencatat masukan delapan fitur turunan pada laju 1 Hz [11], sedangkan jalur akuisisi menghasilkan 56 *subcarrier* pada 50 bingkai per detik [9], [10]. Dua jalur penyelesaian karenanya disiapkan: menghitung ulang delapan fitur turunan bawaan RuView dari bingkai CSI, atau melatih adapter masukan kecil yang memetakan jendela CSI ke ruang masukan *encoder* [PERLU VALIDASI: bentuk masukan checkpoint dan rancangan adapter]. Setelah bentuk masukan pasti, alur fitur dibakukan pada tiga tingkat: bingkai CSI (56 *subcarrier*, hingga 50 bingkai per detik), jendela fitur sepanjang W = 1 detik yang diringkas menjadi satu vektor delapan fitur, dan langkah *embedding*, yaitu satu keluaran *encoder* per jendela. Jalur pertama menghitung ulang delapan fitur turunan bawaan RuView dari bingkai CSI; jalur kedua melatih adapter masukan kecil berbasis konvolusi satu dimensi yang memetakan jendela CSI mentah ke vektor masukan *encoder* sehingga informasi *subcarrier* tidak diringkas lebih dulu oleh rumus tetap. Pada kedua jalur, *encoder* diterapkan per jendela, bukan per bingkai, sesuai kontrak laju 1 Hz kartu model [11].",
  "Bentuk masukan *checkpoint* harus disesuaikan sebelum dipakai (Subbab 2.3): masukan kartu model delapan fitur turunan pada laju 1 Hz [11] berhadapan dengan N~valid~ *subcarrier* hingga 50 bingkai per detik [9], [10]. Tiga rute karenanya disiapkan, yaitu Jalur A yang menghitung ulang delapan fitur turunan RuView, Jalur B1/B2 yang melatih adapter konvolusi satu dimensi (rekonstruksi atau tugas), dan Pembanding C yang memakai spektrum CSI tanpa penyempitan delapan fitur; keputusan rutenya diambil pada G0b [PERLU VALIDASI: bentuk masukan checkpoint dan rancangan adapter]. Alur fitur dibakukan pada tiga tingkat: bingkai CSI (N~valid~ *subcarrier*, hingga 50 bingkai per detik), jendela fitur sepanjang W = 1 detik yang diringkas menjadi satu vektor masukan, dan langkah *embedding*, yaitu satu keluaran *encoder* per jendela; *encoder* diterapkan per jendela, bukan per bingkai, sesuai kontrak laju 1 Hz kartu model [11].")
G("Resolusi temporal dijaga dengan jendela bergulir berlompatan H = 0,25 detik (usulan; dikalibrasi pada T2) sehingga satu segmen huruf menghasilkan satu sampai sekitar tiga belas langkah *embedding* tergantung durasinya. Untuk J dan Z, kelas tidak dibaca dari satu jendela: barisan langkah diproses modul temporal secara berurutan dan klasifikasinya diambil dari ringkasan barisan tersebut. Dengan itu lintasan gerak J dan Z tetap tersedia pada laju empat langkah per detik, cukup untuk lintasan sekitar satu detik, tanpa melanggar kontrak masukan *encoder*. Kandidat modul temporal ialah 1D-CNN ringan dari rancangan lama yang memelihara urutan waktu per langkah; agregasi statistik hanya menjadi kandidat bagi jalur klasifikasi, dan pilihan di antara keduanya diambil dari hasil ablasi pada data yang sama (Subbab 2.4).",
  "Resolusi temporal dijaga dengan jendela bergulir sepanjang W = 1 detik berlompatan H = 0,25 detik (usulan; dikalibrasi pada T2). Empat langkah per detik itu adalah laju awal jendela dengan tumpang-tindih 75%, bukan empat observasi independen; satu segmen huruf menghasilkan satu sampai sekitar tiga belas langkah *embedding* tergantung durasinya. Untuk J dan Z, kelas tidak dibaca dari satu jendela: barisan langkah diproses modul temporal secara berurutan dan klasifikasinya diambil dari ringkasan barisan tersebut, sehingga lintasan gerak tetap terbaca tanpa melanggar kontrak masukan *encoder*. Konfigurasi (W, H) yang lebih pendek khusus J dan Z dibandingkan pada data pilot [PERLU VALIDASI: finalisasi W, H, dan T dari data pilot]. Kandidat modul temporal ialah 1D-CNN ringan yang memelihara urutan waktu per langkah; agregasi statistik hanya kandidat bagi jalur klasifikasi, dan pilihan di antara keduanya diambil dari hasil ablasi pada data yang sama (Subbab 2.4).")
G("Alat ujinya *probe* linear, yaitu pengklasifikasi linear sederhana di atas *embedding* beku; cara ini baku untuk membaca seberapa informatif sebuah representasi tanpa melatih model penuh. Rangkaiannya: *probe* 24 huruf statis pada skema blok temporal, *probe* sekuensial atas gabungan langkah tiap segmen, *probe* biner J terhadap Z, serta dua kontrol, yaitu *probe* pada fitur mentah ringkas dan kontrol label-acak (p < 0,05), agar hasilnya tidak menipu.",
  "Alat ujinya *probe* linear, yaitu pengklasifikasi linear sederhana di atas *embedding* beku. Rangkaiannya: *probe* 24 huruf statis pada skema blok temporal, *probe* sekuensial atas gabungan langkah tiap segmen, *probe* biner J terhadap Z, serta dua kontrol, yaitu *probe* pada fitur mentah ringkas dan uji permutasi label pada unit blok repetisi (p_perm < 0,05, skor label asli melampaui distribusi nol hasil permutasi), agar hasilnya tidak menipu.")
G("Ambang usulannya: F1 makro *probe* sekurang-kurangnya 0,30 dan sekurang-kurangnya tiga kali peluang acak; *probe* J–Z sekurang-kurangnya 70%; seluruhnya difinalkan bersama pembimbing sebelum gerbang dinilai. Jalur fitur turunan dipakai jika lulus; jika gagal tetapi adapter lulus, adapter yang dipilih; jika keduanya gagal, *encoder* beku ditinggalkan menuju skema adaptasi LoRA dan pelatihan lanjutan (Subbab 2.3) dan hasilnya dilaporkan sebagai temuan.",
  "Ambang usulannya: F1 makro *probe* sekurang-kurangnya 0,30 dan sekurang-kurangnya tiga kali peluang acak; *probe* J–Z sekurang-kurangnya 70%; seluruhnya difinalkan bersama pembimbing sebelum gerbang dinilai. Jalur fitur turunan dipakai jika lulus; jika gagal tetapi adapter lulus, adapter yang dipilih; jika keduanya gagal, Pembanding C dijalankan berdampingan dengan skema adaptasi LoRA dan pelatihan lanjutan (Subbab 2.3), dan hasilnya dilaporkan sebagai temuan.")
G("Untuk pelaporan galat lintasan J dan Z, deret prediksi diinterpolasi kembali ke laju kamera agar dapat dibandingkan bingkai demi bingkai dengan acuan guru, dan metode interpolasinya dinyatakan pada laporan. Panjang T ditetapkan 16 langkah per segmen (usulan; difinalkan dari distribusi durasi segmen pada data pilot T2), menutup segmen hingga sekitar empat detik pada lompatan 0,25 detik. Segmen lebih pendek diberi *padding* nol dengan mask valid, dan kerugian regresi dinormalisasi oleh jumlah langkah valid; mask visibilitas Persamaan 2.13 diperluas satu dimensi waktu.",
  "Metrik galat lintasan J dan Z dilaporkan pada resolusi langkah model sebagai metrik utama; interpolasi prediksi ke laju kamera hanya pembanding sekunder karena tidak menambah informasi temporal yang belum teramati, dan metodenya dinyatakan pada laporan. Panjang T ditetapkan 16 langkah per segmen (usulan; difinalkan dari distribusi durasi segmen pada data pilot T2): pada lompatan 0,25 detik, jarak jendela awal ke akhir 3,75 detik dan cakupan data mentah gabungannya sampai sekitar 4,75 detik. Segmen lebih pendek diberi *padding* nol dengan mask valid m^valid^ (Persamaan 2.13a), dan kerugian regresi dinormalisasi oleh jumlah langkah valid.")
G("Enam skema pada Tabel 3.5 mengukur kinerja; untuk skema dalam sesi, pembagiannya temporal per blok dan tidak acak. Data validasi hanya berasal dari data latih,",
  "Enam skema pada Tabel 3.5 mengukur kinerja. Pembagian latih-validasi-uji dilakukan pada level rekaman mentah, sesi, atau blok repetisi sebelum jendela bergulir dibentuk, disertai jeda pembersih (*purge gap*) sekurang-kurangnya selebar W antarbagian, sehingga tumpang-tindih 75% tidak membocorkan data latih ke data uji. Data validasi hanya berasal dari data latih,")
G("Menolak lebih aman daripada menebak kelas yang salah; ambangnya ditetapkan dari data validasi, dan kecukupannya diperiksa lewat laju deteksi palsu serta penilaian validator (Subbab 3.8).",
  "Menolak lebih aman daripada menebak kelas yang salah; ambangnya ditetapkan dari data validasi, dan pelaporannya mencakup *accepted coverage*, akurasi pada segmen diterima, akurasi keseluruhan, serta laju terima-salah dan tolak-salah yang diperiksa lewat uji operasional serta penilaian validator (Subbab 3.8).")
G("Setelah terpilih, model *deployment* disusun menurut Pilihan 1: *encoder*, adapter (jika dipakai), modul temporal, dan kepala klasifikasi digabung menjadi satu *graph* inferensi lalu dikuantisasi; kepala regresi dilepas setelah pelatihan karena perannya supervisi tambahan. Kepala regresi ikut dijalankan pada *deployment* (Pilihan 2) hanya jika keputusan pada Tabel 3.8 menyatakannya, dengan tambahan biaya memori, komputasi, dan kuantisasi yang diukur serta dilaporkan.",
  "Setelah terpilih, model *deployment* disusun menurut Pilihan 1 sebagai rancangan utama naskah ini: *encoder*, adapter (jika dipakai), modul temporal, dan kepala klasifikasi digabung menjadi satu *graph* inferensi lalu dikuantisasi; kepala regresi dilepas setelah pelatihan karena perannya supervisi tambahan. Keputusan finalnya menunggu hasil ablasi dan konfirmasi (Tabel 3.8 #19) [PERLU DATA: keputusan deployment final]. Kepala regresi ikut dijalankan pada *deployment* (Pilihan 2) hanya jika keputusan itu menyatakannya, dengan tambahan biaya memori, komputasi, dan kuantisasi yang diukur serta dilaporkan.")

# ---------- 9) BAB III : G3.5 mermaid + caption ----------
G("accDescr: Bingkai promiscuous masuk ke penyangga geser di PSRAM, segmen terdeteksi dari energi gerak, masukan encoder disiapkan sesuai audit bentuk masukan, model terkuantisasi berupa encoder terpralatih, modul temporal, dan dua kepala menghasilkan kelas beserta skor dan keypoint opsional, keluaran di atas ambang dikirim via UDP, dan keluaran di bawah ambang ditolak sebagai isyarat tidak dikenali.",
  "accDescr: Bingkai promiscuous diperiksa filter MAC, penanda first_word_invalid, dan himpunan subcarrier valid lalu masuk ke penyangga geser di PSRAM. Segmentasi memisahkan onset gerak Delta-CSI, jendela penahanan pose untuk huruf statis, dan jendela lintasan untuk J dan Z, kemudian masukan encoder diekstraksi menurut rute terpilih Jalur A, B, atau Pembanding C. Model terkuantisasi menjalankan encoder, modul temporal, dan kepala klasifikasi; keluaran di atas ambang keyakinan ditampilkan dan dikirim via UDP, keluaran di bawah ambang ditolak sebagai isyarat tidak dikenali. Kepala regresi dilepas pada Pilihan 1 dan hanya aktif bila Pilihan 2 ditetapkan pada Tabel 3.8.")
G("""    subgraph R1["Akuisisi dan segmentasi"]
        direction TB
    CSI["Callback CSI,<br/>mode promiscuous,<br/>filter MGMT"]
    BUF["Penyangga geser<br/>CSI di PSRAM"]
    SEG["Segmentasi energi<br/>gerak (perangkat)"]
    FT["Masukan encoder sesuai<br/>audit bentuk masukan"]
    CSI --> BUF
    BUF --> SEG
    SEG --> FT
    end
    subgraph R2["Model dan keluaran"]
        direction TB
    MOD["Model terkuantisasi:<br/>encoder terpralatih +<br/>modul temporal + dua kepala"]
    DEC{"Skor keyakinan<br/>di atas ambang?"}
    OUT["Label + skor (+ keypoint<br/>opsional) dikirim via UDP"]
    RJ["Label ditolak:<br/>isyarat tidak dikenali"]
    MOD --> DEC
    DEC -- "ya" --> OUT
    DEC -- "tidak" --> RJ
    end
    R1 --> R2""",
  """    subgraph ACQ["Akuisisi, validasi bingkai, dan segmentasi di node RX"]
        direction TB
    CB["Callback CSI mode promiscuous:<br/>filter MAC/MGMT, cek first_word_invalid<br/>dan N_valid"]
    BUF["Penyangga geser<br/>CSI di PSRAM"]
    SEG["Segmentasi: onset Delta-CSI;<br/>pose-hold (24 huruf statis) /<br/>lintasan (J, Z)"]
    INP["Ekstraksi masukan teraudit<br/>(Jalur A / B / Pembanding C)"]
    CB --> BUF
    BUF --> SEG
    SEG --> INP
    end
    subgraph INF["Inferensi tepi terkuantisasi (Pilihan 1: klasifikator saja)"]
        direction TB
    MOD["Model terkuantisasi: encoder +<br/>modul temporal + kepala klasifikasi<br/>(regresi dilepas; Pilihan 2 menunggu<br/>keputusan Tabel 3.8)"]
    DEC{"Skor keyakinan<br/>di atas ambang?"}
    OUT["Tampil di layar; label + skor<br/>dikirim via UDP"]
    RJ["Label ditolak:<br/>isyarat tidak dikenali"]
    MOD --> DEC
    DEC -- "ya" --> OUT
    DEC -- "tidak" --> RJ
    end
    INP --> MOD""")
G("Gambar 3.5 Inferensi langsung pada ESP32-S3 dengan model gabungan encoder, modul temporal, dan dua kepala; seluruh waktunya diukur, bukan dijanjikan",
  "Gambar 3.5 Inferensi langsung pada ESP32-S3 menurut Pilihan 1 (klasifikator saja; aktivasi kepala regresi menunggu keputusan Tabel 3.8); seluruh waktunya diukur, bukan dijanjikan")

print("total suntingan terdaftar:", len(EDITS))
gagal = []
for old, new, n in EDITS:
    c = naskah.count(old)
    if c != n:
        gagal.append((old[:90], c, n))
    else:
        naskah = naskah.replace(old, new)
if gagal:
    for g_, c, n in gagal:
        print(f"GAGAL (ditemukan {c}, harapan {n}): {g_}...")
    sys.exit(1)
print("seluruh suntingan diterapkan:", len(EDITS))
(V10 / "_v18 Intermediate.md").write_text(naskah + log, encoding="utf-8")
print("disimpan sementara -> _v18 Intermediate.md (lanjut di revisi_g18_b.py)")
