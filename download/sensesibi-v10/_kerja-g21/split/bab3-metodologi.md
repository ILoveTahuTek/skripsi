# BAB III METODE PENELITIAN

## 3.1 Desain Penelitian

Penelitian ini berbentuk studi kelayakan kuantitatif bergerbang. Sisi kuantitatifnya mengukur tiga hal: kemampuan CSI dari satu tautan antarmodul ESP32-S3 membedakan 26 huruf alfabet manual SIBI, kemampuan model terkuantisasi berjalan di modul, dan kinerja kedua jalur penerjemahan. Komponen yang lulus uji dikemas menjadi purwarupa, lalu dinilai lewat uji operasional, uji kegunaan skala kecil, dan penilaian validator penutur tunarungu. Mengapa bergerbang? Belum ada yang membuktikan CSI mampu membedakan isyarat SIBI, dan kemampuan semacam itu tidak boleh diperlakukan sebagai asumsi; setiap tahap menghasilkan artefak tetap, kegagalan gerbang dicatat sebagai temuan, dan kriteria akurasi dirumuskan relatif terhadap peluang acak (Subbab 2.14). Inti pelatihannya adalah supervisi lintas modalitas berpandu guru (Subbab 3.7): label kelas dari protokol perekaman serta deret 21 *keypoint* dari guru kamera YOLO26m-Pose mengawasi pelatihan adapter masukan (jika digunakan), modul temporal, dan kedua kepala tugas di atas *encoder* CSI terpralatih yang dibekukan pada baseline. Model terpilihnya lalu dijalankan langsung di modul. Rumusan pertama dijawab pada replikasi platform hingga perancangan model, kedua pada uji klasifikasi, regresi, dan *deployment*, ketiga pada uji operasional, kegunaan, dan penilaian validator.

## 3.2 Tahapan Penelitian

Empat belas minggu (M1 sampai M14) dibagi ke dalam enam tahap: replikasi platform dan karakterisasi (T0), kurasi isyarat dan protokol (T1), perekaman *dataset* serta pelatihan dua kepala (T2), uji generalisasi (T3), pengemasan purwarupa dan uji penerimaan (T4), serta analisis dan penulisan (T5). Lima gerbang keputusan menutup rangkaian itu, ditambah sub-gerbang G0b yang mengaudit kompatibilitas representasi *encoder* atas data pilot sebelum pelatihan penuh; kriteria dan tindakan jika gagal dirinci pada Tabel 3.5; penerimaan pengguna dan biaya dinilai G4, yang kemudian menyusun rekomendasi posisi TKT/TRL 3–4 [27]. Alur lolosnya dirangkum pada Gambar 3.1. Jika G0 gagal dua kali, jalur CSI dihentikan dan dilaporkan sebagai temuan; kriteria seluruh gerbang difinalkan bersama pembimbing sebelum dinilai (Tabel 3.7).

```mermaid
flowchart LR
    accTitle: Tahapan penelitian T0 sampai T5 dengan gerbang G0 sampai G4 dan sub-gerbang G0b
    accDescr: Diagram dua fase. Fase data, audit representasi, dan model (M1 sampai M8) berisi T0 replikasi platform, penguncian versi firmware RuView, audit subcarrier valid dan first_word_invalid, uji Delta-CSI, koeksistensi audio-CSI, audit artefak RuView; gerbang G0 baseline; T1 kurasi, kalibrasi, protokol, etika, pilot G0b; sub-gerbang G0b uji permutasi probe untuk memilih Jalur A, B, atau Pembanding C; T2 perekaman dataset, split anti-kebocoran, pelatihan dua kepala, ablasi, kuantisasi, uji deployment Pilihan 1; gerbang G1 dengan cakupan diterima dan akurasi selektif. Fase pengujian dan penulisan (M8 sampai M14) berisi T3 uji generalisasi enam skema; G2 konsultasi tiga pilar; T4 pengemasan dua arah, TTS lokal utama MMS-TTS-ind, uji latensi; G3 latensi per arah dan TTFA; G4 sintesis kelayakan dan rekomendasi TKT 3-4 Permenristekdikti 42/2016; T5 analisis dan penulisan.

    subgraph KA["Fase data, audit, dan model (M1-M8)"]
        direction TB
    T0["T0 Replikasi platform, audit<br/>subcarrier valid, Delta-CSI,<br/>koeksistensi, artefak (M1-M2)"]
    G0("G0 akhir M2: laju ≥ 25 fps,<br/>paket hilang ≤ 0,1%,<br/>gerak terpisah")
    T1["T1 Kurasi 26 huruf, kalibrasi,<br/>protokol, etika,<br/>pilot G0b (M2-M4)"]
    G0b("G0b awal T2 (M4): probe linear +<br/>uji permutasi (p < 0,05);<br/>pilih jalur masukan")
    T2["T2 Perekaman dataset, split anti-<br/>leakage, pelatihan dua kepala,<br/>kuantisasi, uji deployment (M4-M8)"]
    G1("G1 akhir M8: akurasi ≥ 50%,<br/>F1 ≥ 0,45, cakupan +<br/>akurasi selektif, < 100 ms")
    T0 --> G0
    G0 -- "lolos" --> T1
    T1 --> G0b
    G0b -- "lolos" --> T2
    T2 --> G1
    end
    subgraph KB["Fase pengujian dan penulisan (M8-M14)"]
        direction TB
    T3["T3 Uji generalisasi enam skema:<br/>sesi, LOSO, LORO, pengguna<br/>baru, posisi (M8-M10)"]
    G2("G2 akhir M10: 3 pilar pakar<br/>tanpa temuan blok kritis")
    T4["T4 Pengemasan dua arah, Rust,<br/>TTS lokal MMS-TTS-ind, uji<br/>latensi, biaya (M10-M12)"]
    G3("G3 M11: Arah 1 ≤ 2 s, Arah 2 ≤ 3 s (p50/p95);<br/>TTFA < 100 ms; UDP < 0,2 ms; RAM < 40 MB")
    G4("G4 akhir M12: Likert, validator,<br/>BOM biaya, TKT 3-4<br/>(Permenristekdikti 42/2016)")
    T5["T5 Analisis dan penulisan<br/>laporan akhir (M12-M14)"]
    T3 --> G2
    G2 -- "lolos" --> T4
    T4 --> G3
    G3 -- "lolos" --> G4
    G4 -- "lolos" --> T5
    end
    KA -- "G1 lolos" --> KB
```

Gambar 3.1 Tahapan penelitian T0–T5, gerbang keputusan G0–G4, dan sub-gerbang G0b (jalur lolos; kuantisasi dan uji deployment berada pada T2; tindakan jika gagal merujuk Tabel 3.5)

Tahap T0 sampai T2 lebih dulu membangun dasar data. T0 menyiapkan dua modul dengan *firmware* `esp32-csi-node` RuView [10], lalu menjalankan empat uji tanpa partisipan. Uji itu mencakup verifikasi himpunan *subcarrier* valid N~valid~ (pemeriksaan LLTF atau HT-LTF, *pilot*, dan `first_word_invalid`) stabil pada jarak baku 1 meter, audit sisa *phase drift* Persamaan (2.5), uji pilot keterpisahan awal beberapa pose tangan statis dengan konfigurasi jari dan orientasi telapak berbeda, termasuk percobaan awal huruf dinamis J dan Z, di samping pemisahan gerak dan diam, uji Delta-CSI (Subbab 3.8.1), koeksistensi radio dengan *streaming* audio aktif, serta pengukuran laju pencuplikan, laju paket hilang, panjang buffer CSI, RSSI dan *noise floor*, dan penanganan fase pada *callback*. T0 juga mengaudit *checkpoint encoder* [11]: bentuk masukan, parameter normalisasi masukan, jumlah parameter, normalisasi L2, dukungan ekspor, dan kompatibilitas LoRA (Subbab 3.7). T1 meliputi kurasi 26 huruf bersama validator, kalibrasi ruang, protokol dan etika, serta perizinan (Subbab 3.6); pasangan huruf paling mirip juga ditetapkan di sini sebagai bahan gerbang G1.

Pada T2, *dataset* kurang lebih 30 repetisi per isyarat per sesi direkam disertai video yang tersinkron (Subbab 3.6). Alur pelatihannya berbentuk supervisi berpandu guru: segmen disaring lewat *keypoint* guru, jendela CSI disandingkan dengan label guru berdasarkan penanda waktu, lalu kedua kepala dilatih di atas *encoder* yang dibekukan dengan kerugian gabungan. Model terpilih selanjutnya dikuantisasi dan diuji di modul (Subbab 3.7). T2 melahirkan *dataset* berlabel, model terlatih, dan laporan *deployment*. G1 menilai hasilnya; jika gagal, cakupan dipangkas menjadi himpunan huruf dengan pembeda CSI terkuat (Tabel 3.7).

Tahap T3 sampai T5 berisi pengujian dan pelaporan. Generalisasi lintas sesi, partisipan, ruang, serta posisi berdiri-duduk diuji pada T3, termasuk pada satu pengguna baru tanpa pelatihan ulang (Subbab 3.7) dengan acuan Widar3.0 [14]. Jika ketahanan lintas pengguna rendah, cakupan berubah menjadi personalisasi per pengguna dan dilaporkan sebagai temuan. T4 mengemas model menjadi purwarupa dua arah (Subbab 3.5), menjalankan uji operasional dan jalur ucapan (Subbab 3.8) yang dinilai G3. Rangkaian itu ditutup uji penerimaan, penilaian validator, dan analisis biaya yang dinilai G4. Pada T5, seluruh artefak dianalisis dan laporan kelayakan disusun lengkap dengan rekomendasi TKT/TRL 3–4 [27] beserta keterbatasan eksplisitnya (Subbab 1.4).

## 3.3 Waktu dan Lokasi Penelitian

Pelaksanaan penelitian jatuh pada [PERLU DATA: bulan dan tahun pelaksanaan penelitian] di Jawa Timur. Penelitian ini tidak bersandar pada mitra lembaga; partisipan direkrut langsung oleh peneliti, sedangkan perekaman dan pengujian berlangsung di sedikitnya dua ruang berbeda, misalnya ruang kelas dan ruang kerja, sebagai jumlah minimum skema *leave-one-room-out*. Tiap ruang dikalibrasi lebih dulu sebelum perekaman (Subbab 3.5).

## 3.4 Alat dan Bahan

Tabel 3.1 dan Tabel 3.2 menyajikan perangkat keras dan perangkat lunak penelitian. Node penginderaan dipegang sepasang modul ESP32-S3: TX menjana trafik OFDM terjadwal (*self-ping* ke *gateway*) sebagai sumber bingkai, sedangkan RX menangkap CSI 56 *subcarrier* pada 2,4 GHz kanal 20 MHz melalui *callback* CSI mode *promiscuous* sekaligus memuat antarmuka. Supaya eksperimen bisa diulang, versi atau komit *firmware* RuView serta perangkat lunak lain dicatat bersama log pelatihan. Bahan penelitiannya meliputi *checkpoint encoder* terpralatih [11], *dataset* CSI berpasangan yang direkam sendiri, dataset citra WPC beserta model guru YOLO26m-Pose dari repositori peneliti, lembar definisi huruf, aset tampilan arah kedua, formulir persetujuan, instrumen uji, dan kuesioner persepsi. Perekaman dilakukan sendiri karena pengenalan isyarat SIBI dari CSI memang belum ditemukan dalam penelusuran (Subbab 2.15).

Tabel 3.1 Perangkat keras penelitian

| No. | Nama | Spesifikasi | Jumlah | Keterangan |
|---|---|---|---|---|
| 1 | Modul ESP32-S3 | PSRAM 8 MB; 2,4 GHz 802.11b/g/n, kanal 20 MHz (56 *subcarrier*), 1T1R; varian yang direkomendasikan RuView [10] | 2 unit | Node TX (penjana trafik OFDM *self-ping*) dan node RX (penerima CSI dan antarmuka) |
| 2 | Layar modul | OLED 0,96 inci I2C (128×64) atau TFT 1,3 inci SPI (240×240) [PERLU DATA: model final] | 1 unit | Tampilan huruf, baterai, kanal, mode kerja |
| 3 | *Rotary encoder* EC11 dan tombol tekan | Putar 360 derajat, 20 detak per putaran, tombol terintegrasi; sakelar sesaat *pull-up* internal | 1–2 unit | Navigasi menu, sensitivitas, tekan-untuk-bicara, reset |
| 4 | Pengeras suara dengan DAC I2S | Mini 8 Ohm 3 W, penguat kelas D MAX98357A | 1 set | Pemutaran suara TTS hasil sintesis server yang dialirkan ke modul (keputusan D3 pada Tabel 3.7); *speaker* ponsel sebagai cadangan |
| 5 | Mikrofon I2S | INMP441, MEMS omnidireksional, SNR 61 dBA | 1 unit | Pintu suara arah kedua |
| 6 | Baterai Li-Po, BMS 1S, pengisi TP4056 | Li-Po 3,7 V [PERLU DATA: kapasitas final ditetapkan dari uji arus T0 dan G3]; proteksi; pengisi 1 A USB-C | 1–2 set | Daya portabel, proteksi, dan pengisian |
| 7 | Laptop | ASUS TUF Dash F15 FX516PR: i7-11370H, RTX 3070 Laptop 8 GB VRAM, RAM 16 GB | 1 unit | Server Rust (penelan CSI, orkestrasi, ASR lokal cadangan, TTS lokal utama, dasbor); akuisisi jalur guru; pelatihan dua kepala; evaluasi |
| 8 | Ponsel pintar | Poco F4 5G: Snapdragon 870, RAM 6 GB, Android | 1 unit | Klien Tauri (tampilan teks dan representasi SIBI), mesin TTS *on-device* sebagai cadangan, *hotspot* cadangan |
| 9 | *Access point* | *Router* Wi-Fi 2,4 GHz dengan internet [PERLU DATA: pilihan final] | 1 unit | Jembatan jaringan dan penjangkar kanal, bukan penginderaan |
| 10 | *Webcam* | Bawaan laptop | 1 unit | Hanya untuk jalur guru |

Rencana daftar komponen (*bill of materials*, BOM) pengadaan disusun dari baris Tabel 3.1 dan diisi hasil survei harga sebelum pembelian tanpa mengarang angka; sel berisi [PERLU DATA] dilengkapi dari survei harga, dan totalnya dinilai pada G4 (Persamaan 3.5) dengan memisahkan harga pasangan modul inti dari total node antarmuka lengkap:

| No. | Komponen | Jumlah | Harga Satuan (Rp) | Subtotal (Rp) | Sumber Rujukan Harga |
|---|---|---|---|---|---|
| 1 | Modul ESP32-S3 (TX dan RX) | 2 unit | [PERLU DATA] | [PERLU DATA] | [PERLU DATA] |
| 2 | Layar modul final (OLED 0,96 inci atau TFT 1,3 inci) | 1 unit | [PERLU DATA] | [PERLU DATA] | [PERLU DATA] |
| 3 | *Rotary encoder* EC11 dan tombol PTT/reset | 1–2 set | [PERLU DATA] | [PERLU DATA] | [PERLU DATA] |
| 4 | Mikrofon I2S INMP441 | 1 unit | [PERLU DATA] | [PERLU DATA] | [PERLU DATA] |
| 5 | DAC I2S MAX98357A dan pengeras suara 8 Ω 3 W | 1 set | [PERLU DATA] | [PERLU DATA] | [PERLU DATA] |
| 6 | Baterai Li-Po kapasitas final, BMS 1S, TP4056, komponen pasif, dan pembagi tegangan | 1–2 set | [PERLU DATA] | [PERLU DATA] | [PERLU DATA] |
| 7 | *Enclosure* cetak tiga dimensi, kabel, header, dan PCB | 2 set | [PERLU DATA] | [PERLU DATA] | [PERLU DATA] |
| Total | Sepasang node antarmuka lengkap (di luar laptop, ponsel, dan *access point*) | - | - | [PERLU DATA] | - |

Foto pada Gambar 3.2 memudahkan mengenali bentuk sembilan perangkat pada Tabel 3.1; webcam memakai bawaan laptop sehingga tidak difoto terpisah. Foto produk hanya menjadi pengenal bentuk, bukan acuan merek maupun spesifikasi, dan rujukan spesifikasinya tetap Tabel 3.1 [PERLU ILUSTRASI: foto dokumentasi sendiri setelah seluruh perangkat dibeli].

```gambar
Sumber skrip: scripts/sensesibi-v10/gambar_g15_alatbahan.py (grid foto hasil pencarian gambar daring) -> assets-v16/gambar-3.2.png
```

Gambar 3.2 Perangkat keras penelitian; huruf pada tiap foto mengikuti baris Tabel 3.1 (foto produk sebagai ilustrasi pengenal bentuk sementara sebelum perangkat dirakit, bukan acuan merek)

Tabel 3.2 Perangkat lunak penelitian

| No. | Nama | Fungsi dalam penelitian |
|---|---|---|
| 1 | *Firmware* dan *server* RuView [10] | Menangkap CSI, mengirim UDP, kalibrasi ruang, segmentasi |
| 2 | *Checkpoint* encoder CSI terpralatih `ruvnet/wifi-densepose-pretrained` beserta adapter LoRA ruangannya [11] | *Encoder* murid yang dibekukan pada baseline; kandidat adaptasi LoRA |
| 3 | `scripts/collect-ground-truth.py` (diadaptasi) | Sinkron kamera-CSI; estimator memakai YOLO26m-Pose |
| 4 | Model guru YOLO26m-Pose dan repositori alur kerja YOLO26 peneliti [12] | Ekstraksi *keypoint*; konversi *dataset*, pelatihan deterministik, pencatatan eksperimen (Subbab 3.7) |
| 5 | Layanan GPU Kaggle | Pelatihan lanjutan guru dan pembanding adaptasi *encoder* jika GPU lokal tidak cukup |
| 6 | Python dan PyTorch | Pelatihan dua kepala, LoRA, pelatihan lanjutan, evaluasi; kompatibel dengan *checkpoint* dan mendukung autograd |
| 7 | ESP-DL dengan akselerasi ESP-NN (alternatif: TensorFlow Lite Micro) [23] | Menjalankan model terkuantisasi pada node RX |
| 8 | faster-whisper, MMS-TTS-ind ONNX (kandidat utama), Kokoro ONNX (pembanding) [26], [25], [24]; layanan ucapan awan [PERLU DATA: layanan final hasil uji banding] | ASR cadangan lokal (faster-whisper); TTS utama operasional di server lokal (MMS-TTS-ind); TTS pembanding (Kokoro); ASR utama saat daring |
| 9 | Rust, Tokio, Axum, Leptos, Tauri | Server seluruhnya Rust, dasbor WASM, aplikasi klien ponsel |
| 10 | ONNX Runtime dan Kokoro TTS ONNX [24] | *Runtime* evaluasi TTS di server lokal dan ponsel (Tauri); Kokoro diuji sebagai pembanding jika suara Indonesia tersedia sebelum G3 |
| 11 | Kamus label-teks dan teks-isyarat | Dikembangkan sendiri; kamus label-teks dimuat pada modul |

## 3.5 Perancangan Sistem

Gambar 3.3 memperlihatkan keseluruhan sistem: dua jalur operasional tanpa kamera ditambah satu jalur guru yang hanya aktif saat akuisisi dan pelatihan. Pada arah pertama, bingkai OFDM trafik *self-ping* yang dipancarkan node TX melintasi zona isyarat, gerak pengisyarat mengubah deret CSI yang ditangkap node penerima, dan model berkepala klasifikasi yang terkuantisasi dijalankan langsung di modul menghasilkan label beserta skor keyakinan. Label dikirim melalui UDP ke server Rust sebagai telemetri, dipetakan menjadi teks Indonesia, lalu teks itu tampil di layar modul dan aplikasi Tauri sekaligus disintesis mesin TTS di server lokal; audio hasil sintesis dialirkan kembali ke modul dan diputar pada *speaker* DAC I2S. Jika aliran audio ke modul tidak stabil atau server tidak tersedia, sintesis beralih ke mesin *on-device* pada ponsel dan pemutaran memakai *speaker* ponsel; peralihan itu dicatat. Dengan keputusan *deployment* Pilihan 1 (Tabel 3.7), kepala regresi berperan sebagai supervisi tambahan saat pelatihan dan dilepas pada *deployment* sehingga keluaran perangkat ialah label huruf beserta skor keyakinan.

Pada arah kedua, tombol tekan-untuk-bicara mengaktifkan mikrofon I2S pada node penerima; audio ditangkap di modul lalu dialirkan ke server Rust, yang meneruskannya ke layanan ASR awan saat daring atau memprosesnya sendiri dengan faster-whisper. Teks hasil pengenalan dipetakan ke representasi SIBI dari aset modul dan tampil pada aplikasi Tauri, dengan indikator opsional di layar modul. Saat internet terputus, kedua arah tetap berjalan karena ASR dan TTS beralih ke server lokal; kebutuhan pemrosesan audio di node penerima sebatas penangkapan dan pengaliran, bukan pengenalan. Jalur guru, yang memakai *webcam* dan YOLO26m-Pose untuk mengekstrak deret *keypoint* sebagai supervisi pelatihan, bukan bagian produk akhir.

```mermaid
flowchart TD
    accTitle: Arsitektur produk akhir tanpa kamera dengan cadangan TTS on-device pada Arah 1
    accDescr: Jalur guru hanya aktif saat akuisisi dan pelatihan; webcam dan YOLO26m-Pose menghasilkan 21 keypoint untuk supervisi dua kepala. Arah 1 mengalir dari bingkai OFDM trafik self-ping node TX melalui zona isyarat ke node RX yang menjalankan model klasifikasi terkuantisasi Pilihan 1; label dan skor dikirim via UDP ke server Rust, teks tampil di layar dan aplikasi Tauri, TTS server lokal menyintesis suara yang dialirkan ke speaker DAC I2S node RX; garis putus-putus adalah cadangan TTS on-device ponsel untuk Arah 1. Arah 2 mengalir dari tombol PTT dan mikrofon I2S ke server, dikenali ASR awan saat daring atau faster-whisper saat luring, dipetakan ke kamus kata SIBI dengan ejaan jari termasuk animasi J dan Z, lalu tampil di aplikasi Tauri.

    subgraph GURU["Jalur guru (akuisisi dan pelatihan saja)"]
        direction TB
    WC["Webcam laptop"]
    YP["YOLO26m-Pose:<br/>21 keypoint tangan"]
    SUP["Supervisi pelatihan<br/>(Subbab 3.7)"]
    WC --> YP
    YP --> SUP
    end
    subgraph A1["Arah 1: isyarat menjadi teks dan suara"]
        direction TB
    TX["Node TX: penjana trafik OFDM"]
    ZN["Zona isyarat"]
    RX["Node RX: CSI + model klasifikasi<br/>terkuantisasi (Pilihan 1)"]
    MAPL["Kamus label-teks di modul"]
    DSP1["Layar modul + Tauri:<br/>teks hasil + skor"]
    SPK["Speaker DAC I2S (node RX)"]
    TTSP["TTS on-device ponsel<br/>(cadangan Arah 1)"]
    TX --> ZN
    ZN --> RX
    RX --> MAPL
    MAPL --> DSP1
    end
    SRV["Server Rust (laptop):<br/>TTS MMS-TTS-ind utama +<br/>ASR faster-whisper"]
    subgraph A2["Arah 2: ucapan menjadi representasi SIBI"]
        direction TB
    PTT["Tombol tekan-untuk-bicara"]
    MIC["Mikrofon I2S (INMP441)"]
    ASR["ASR: awan (daring) /<br/>faster-whisper (luring)"]
    ASET["Kamus kata SIBI + ejaan jari<br/>(animasi J dan Z)"]
    TAU["Aplikasi Tauri:<br/>teks + representasi SIBI"]
    PTT --> MIC
    MIC -- "audio PCM via UDP/WS" --> SRV
    ASR -- "teks" --> ASET
    ASET --> TAU
    end
    RX -- "label + skor via UDP" --> SRV
    SRV -- "audio TTS dialirkan" --> SPK
    SRV -. "cadangan" .-> TTSP
    SRV -- "audio" --> ASR
```

Gambar 3.3 Arsitektur produk akhir tanpa kamera. Subgraf Arah 1 = isyarat menjadi teks dan suara, dengan cadangan TTS *on-device* ponsel untuk Arah 1; subgraf Arah 2 = ucapan menjadi representasi SIBI; subgraf jalur guru hanya aktif saat akuisisi dan pelatihan; garis putus-putus = jalur cadangan.

Topologi jaringannya menyatukan seluruh perangkat pada satu *access point* dan satu kanal, sehingga penangkapan CSI berjalan serentak dengan komunikasi data (Subbab 2.3). Node TX menjana trafik OFDM terjadwal sebagai sumber bingkai CSI, sedangkan node penerima mengirim bingkai CSI mentah saat akuisisi serta label dan skor saat *deployment* melalui UDP kepada server Rust sebagai telemetri riset. Server lokal menjalankan server RuView, server Rust, faster-whisper sebagai ASR cadangan, serta TTS MMS-TTS-ind sebagai jalur utama sintesis luring. Untuk menjamin aliran audio dua arah tidak melumpuhkan penangkapan CSI 50 bingkai per detik pada kanal Wi-Fi yang sama, protokol komunikasi dan audio ditetapkan serta diuji secara empiris pada T0 dan gerbang G3 dengan cakupan: (a) verifikasi koeksistensi *firmware* yang menjalankan *callback* CSI, koneksi *station*, dan pengiriman UDP secara serentak; (b) penetapan format audio, *codec*, laju pencuplikan, mekanisme *streaming* dan penyangga untuk aliran mikrofon (INMP441 I2S) maupun pengeras suara (MAX98357A I2S), beserta penanganan *packet loss*, batas waktu, dan pengulangan [PERLU DATA: spesifikasi protokol audio hasil audit T0]; (c) sinkronisasi penanda waktu antarmodul dan server; serta (d) dampak beban lalu lintas audio terhadap laju aktual CSI dan kestabilan jaringan. Sebagai kerangka kerja awal, cuplikan mikrofon dialirkan dalam paket bernomor urut melalui UDP berpenyangga atau *WebSocket* saat tombol PTT ditekan, dan aliran pengeras suara Arah 1 masuk ke penyangga cincin (*ring buffer*) di PSRAM modul RX guna mencegah *underrun* akibat jitter Wi-Fi; pemilihan format dan laju pencuplikan final mengikuti hasil uji T0, bukan asumsi di muka. Apabila koeksistensi pada satu modul RX menimbulkan degradasi CSI melampaui ambang G0, jalur cadangan C (memisahkan antarmuka audio ke modul ketiga atau pemutaran di ponsel) diaktifkan dan dilaporkan.

Kedua modul dipasang setinggi dada dan saling mengapit zona isyarat; uji Delta-CSI memeriksa kesesuaiannya. Zona hanya ditempati satu pengisyarat per sesi, sistem tidak mengidentifikasi individu, dan jarak antarmodul (baku 1 meter) ditetapkan pada T0 lalu dicatat dalam metadata sesi (Tabel 3.7). Karena CSI peka terhadap perubahan ruang [10], [14], setiap sesi diawali kalibrasi ruang bawaan RuView selama kurang lebih empat menit dengan 600 bingkai dan 8 *anchor*. Posisi perabot, pendingin ruangan, serta orang yang lewat dicatat sebagai kovariat analisis.

*Enclosure* cetak tiga dimensi bahan PLA atau ABS menampung papan, baterai, BMS, TP4056, serta seluruh antarmuka node penerima. Layar, pengeras suara, dan mikrofon berada pada muka depan atau atas, *rotary encoder* dan tombol pada samping, port USB-C pada bawah. Node pemancar dikemas serupa tanpa antarmuka. Pemetaan pin GPIO pada Tabel 3.3 dipilih agar tidak menabrak pin *strapping* (GPIO 0, 3, 45, 46) maupun kanal USB bawaan papan [8], lalu diverifikasi ulang pada unit papan fisik saat T0 dengan cakupan yang dirinci pada catatan Tabel 3.3. Rantai dayanya tersusun atas baterai, BMS 1S, TP4056, dan regulator 3,3 volt papan; tegangan baterai diukur lewat pembagi tegangan sehingga persentase baterai bisa tampil di layar. Pada rantai daya itu, kecukupan arus puncak regulator 3,3 V saat Wi-Fi TX dan penguat kelas D MAX98357A aktif bersama *speaker*, sekaligus keamanan pengisian daya pada modul TP4056 (*load-sharing* atau larangan operasi aktif saat pengisian jika modul tanpa *power-path*), diverifikasi pada uji bangku T0 dan G3 [PERLU DATA: profil arus puncak terukur, regulasi beban saat pengisian, dan kapasitas regulator terpilih]; nilai kapasitas arus tidak diasumsikan di muka. Estimasi ketahanan baterai (Persamaan 3.4) didasarkan pada pengukuran arus aktual I~rata~ dalam kondisi diam, inferensi aktif, *streaming* audio, dan pemutaran *speaker*. [PERLU DATA: berkas model enclosure final] [PERLU ILUSTRASI: foto atau render enclosure dan tata letak komponennya]

Skema tiga dimensi pada Gambar 3.4 merangkum penempatan seluruh komponen node penerima di dalam enclosure; pemetaan pinnya mengikuti Tabel 3.3 dan dimensinya difinalkan setelah uji T0.

```gambar
Sumber skrip: scripts/sensesibi-v10/gambar_g15_rxnode.py (matplotlib mplot3d) -> assets-v16/gambar-3.4.png
```

Gambar 3.4 Skema penempatan komponen node penerima di dalam enclosure (ilustrasi tiga dimensi, tidak berskala)

Tabel 3.3 Matriks pinout wiring GPIO node penerima

| No. | Subsistem | Pin modul | GPIO ESP32-S3 | Fungsi |
|---|---|---|---|---|
| 1 | Layar I2C (OLED) | SDA / SCL | GPIO 8 / GPIO 9 | Jalur data dan *clock* bus I2C |
| 2 | *Rotary encoder* EC11 | CLK (A) / DT (B) / SW | GPIO 10 / GPIO 11 / GPIO 12 | Detak, arah putaran, tombol |
| 3 | Tombol tekan | OUT | GPIO 13 | Tekan-untuk-bicara dan reset; *pull-up* internal |
| 4 | Mikrofon INMP441 | SCK / WS / SD | GPIO 14 / GPIO 15 / GPIO 16 | *Clock*, *word select*, data I2S penerima |
| 5 | DAC MAX98357A | BCLK / LRC / DIN | GPIO 17 / GPIO 18 / GPIO 21 | *Clock*, penanda kiri-kanan, data I2S pengirim |
| 6 | Pemantau tegangan baterai | ADC | GPIO 1 (ADC1_CH0) | Keluaran pembagi tegangan baterai |

Seluruh baris Tabel 3.3 wajib diverifikasi ulang pada unit papan fisik yang dibeli saat T0; verifikasi mencakup pin *strapping* (GPIO 0, 3, 45, 46), jalur USB, kemampuan kanal ADC1, potensi konflik periferal I2C/I2S/SPI, dan revisi papan, dengan penyesuaian pemetaan yang dicatat dan dilaporkan.

Seluruh perangkat lunak server dan klien ditulis dalam Rust (Subbab 2.13): pendengar UDP bingkai CSI berjalan di atas Tokio, sementara Axum menyediakan HTTP dan WebSocket bagi dasbor Leptos WASM. Aplikasi Tauri pada ponsel menerima teks hasil isyarat sekaligus menjadi klien antarmuka dua arah. Target *parsing* bingkai di bawah 0,2 ms serta memori server di bawah 40 MB baru diukur pada G3 (Subbab 3.8.3). Mesin sintesis utama di server lokal memakai `facebook/mms-tts-ind` (dikonversi ke ONNX untuk evaluasi luring; sekitar 36,3 juta parameter) karena verifikasi resmi `hexgrad/Kokoro-82M` (`VOICES.md`, 14 November 2026) memastikan tidak tersedianya suara bahasa Indonesia pada rilis v1.0 [24], [25]; Kokoro-82M ONNX tetap disiapkan sebagai pembanding apabila rilis atau adapter bahasa Indonesia terverifikasi sebelum G3. Untuk menjaga konsistensi pengukuran, target waktu menuju audio pertama (*time-to-first-audio*, TTFA) di bawah 100 ms pada frasa uji hingga lima kata didefinisikan terpisah dari durasi sintesis total dan diukur pada kondisi terdokumentasi: perangkat keras laptop uji (CPU i7-11370H dan GPU RTX 3070), *execution provider* ONNX Runtime (CPU atau CUDA), presisi model (FP32, FP16, atau INT8), serta ukuran *chunk* penyangga audio pertama, dengan pelaporan persentil p50 dan p95. Untuk keluaran huruf tunggal pada Arah 1, opsi pra-penyimpanan (*pre-cache*) klip audio 26 huruf dievaluasi pada G3 sebagai salah satu cara menjaga pemutaran tetap instan [PERLU DATA: keputusan opsi *pre-cache* dan hasil uji bandingnya terhadap sintesis langsung].

## 3.6 Protokol Perekaman Dataset, Partisipan, dan Etika

Partisipan terdiri atas 3–4 pengisyarat kompeten, sedikitnya satu validator penutur tunarungu, serta 3–5 pengguna uji dari kelompok sasaran, yaitu guru, siswa tunarungu, dan wali murid. Agar skema lintas sesi bisa dijalankan, setiap pengisyarat direkam dalam sedikitnya dua sesi. Kurasi isyarat mengacu pada *Kamus SIBI* [3]: lembar definisi memuat konfigurasi tangan-jari serta lintasan J dan Z, lalu validator menyetujuinya. Pasangan huruf paling mirip ditetapkan sebagai bahan G1, sedangkan kosakata tampilan arah kedua meliputi 26 huruf dan 9 angka [3] serta kata terpilih. Perekaman memakai *elisitasi* terisolasi, satu huruf per segmen dengan jeda antarrepetisi: huruf statis diperagakan sebagai pose yang ditahan sejenak, J dan Z sebagai lintasan gerak. Prosedur perekaman setiap sesi adalah sebagai berikut.

1. Menyiapkan seluruh peralatan yang dipakai.
2. Memasang kedua modul, pemancar dan penerima, lalu menghubungkan seluruh perangkat ke *access point* pada satu kanal.
3. Menjalankan kalibrasi ruang seraya mencatat metadata sesi: tanggal, ruang, kode pengisyarat, posisi modul, dan kondisi latar.
4. Menjalankan `scripts/collect-ground-truth.py` menggunakan sumber penanda waktu monotonik tunggal pada laptop sebagai acuan penyelarasan *timestamp* bingkai kamera (target sekitar 30 fps) dan bingkai CSI (sekitar 50 fps). Kualitas sinkronisasi diverifikasi melalui uji ketukan tangan di awal dan akhir setiap sesi dengan batas galat selisih waktu maksimum [PERLU DATA: toleransi sinkronisasi akhir, misalnya 20 ms atau satu bingkai CSI; metode penyelarasan dan resampling *keypoint* ke pusat jendela CSI]. Bingkai kamera yang hilang (*frame drop*) dicatat; jika jeda melebihi toleransi, segmen ditandai tidak valid untuk target regresi tanpa interpolasi paksa gerakan yang hilang.
5. Memunculkan kartu pemandu huruf target dengan urutan huruf yang diacak di dalam setiap blok guna mencegah efek urutan (*order effect*) dan akumulasi kelelahan pada kelas huruf tertentu, merekam satu repetisi, memberi jeda antarrepetisi, hingga tiap huruf mencapai sekitar 30 repetisi per sesi.
6. Membuang segmen yang gagal deteksi tangan oleh model guru, mengalami *jitter* *keypoint* melampaui ambang, atau terpotong, serta melakukan audit kualitas *keypoint* khusus lintasan dinamis J dan Z (melaporkan *detection rate*, laju *frame drop*, dan konsistensi kelancaran lintasan selama gerak cepat, karena kinerja `exp11_huruf24` pada 24 huruf statis tidak otomatis menjamin keandalan *keypoint* pada gerakan J/Z); tingkat segmen terbuang, skor kualitas anotasi tiap segmen, serta jumlah dan proporsi repetisi yang benar-benar dipakai per kelas dan per sesi setelah pembuangan dicatat dan dilaporkan.
7. Meminta validator penutur tunarungu memeriksa sampel acak terstratifikasi sebesar [PERLU DATA: proporsi sampel, misalnya sekurang-kurangnya 10% segmen per kelas atau minimal 3 repetisi per huruf per pengisyarat] dan menjalankan uji reliabilitas kesepakatan jika penilai lebih dari satu orang; label keluaran guru berstatus *pseudo-label* sampai audit validator selesai. Rujukan teknis model guru merujuk dokumentasi Ultralytics [12] serta artefak repositori WPC peneliti [PERLU DATA: tag rilis/commit dan hash *checkpoint* exp11_huruf24].

Beban perekaman dihitung agar protokolnya realistis dan etis. Dengan 26 huruf dan kurang lebih 30 repetisi, satu sesi memuat sekitar 780 repetisi; pada asumsi lima detik per repetisi, perekaman murninya sekitar 65 menit, dan dengan jeda blok, kalibrasi, serta persiapan, satu sesi memakan waktu sekitar 97 menit. Setiap sesi dibagi blok sekitar sepuluh menit dengan jeda wajib sekurang-kurangnya tiga menit di antaranya; paling banyak dua sesi per hari untuk satu pengisyarat; pengisyarat boleh menghentikan repetisi kapan saja tanpa konsekuensi. Tingkat kelelahan diamati dari penurunan mutu segmen pada blok akhir dan dilaporkan bersama tingkat segmen terbuang.

Baru setelah persetujuan etik dari [PERLU DATA: lembaga atau komisi pemberi persetujuan etik] serta persetujuan tertulis (*informed consent*) yang disajikan dalam format bahasa Indonesia yang jelas dan aksesibel bagi partisipan Tuli (didampingi juru bahasa isyarat atau panduan visual jika diperlukan) diperoleh, perekaman dimulai; partisipan berhak mengundurkan diri kapan saja. Apabila uji kegunaan (T4) melibatkan siswa di bawah usia 18 tahun, penelitian wajib memperoleh persetujuan tertulis orang tua atau wali sekaligus persetujuan sukarela anak (*child assent*); jika tidak, partisipan dibatasi pada kelompok dewasa (sedikitnya 18 tahun). Formulir persetujuan menerangkan batas ruang lingkup kamera (hanya saat akuisisi pelatihan), mode privasi RuView aktif, serta pengiriman audio Arah 2 ke layanan awan saat mode daring. Video mentah hanya disimpan pada media terenkripsi dengan akses terbatas peneliti untuk keperluan verifikasi batas segmen, penyaringan kualitas, dan peninjauan validator, lalu dihapus secara permanen dalam batas waktu [PERLU DATA: misalnya maksimal 30 hari] setelah seluruh validasi anotasi selesai. *Dataset* yang dibagikan tidak mencantumkan nama atau identitas langsung, namun penelitian mengakui bahwa pola kinematika tangan, audio, atau metadata sesi tetap berpotensi memiliki risiko identifikasi ulang sehingga tidak diklaim sepenuhnya anonim tanpa batas, dan tata kelolanya tunduk pada perjanjian akses terbatas.

## 3.7 Pengolahan Sinyal, Pelatihan Dua Kepala, dan Deployment

Bingkai CSI dibatasi *firmware* RuView paling sering setiap 20 ms atau 50 bingkai per detik [10]; laju aktualnya diukur pada T0, dan jika terukur lebih rendah, pita Doppler yang dianalisis dipangkas hingga setengah laju aktual. Deret CSI dipotong menjadi segmen huruf dengan segmentasi energi gerak memakai Delta-CSI, yaitu rata-rata besar perubahan koefisien kanal kompleks antarbingkai pada himpunan *subcarrier* valid N~valid~ hasil audit T0 (Subbab 2.2):

```rumus
d( t ) = ( 1 / |N~valid~| ) · Σ~n~ | h~n~(t) − h~n~( t − 1 ) | , n ∈ N~valid~ (3.1)
```

Segmentasi tidak mengandalkan ambang energi gerak τ semata karena huruf statis memperagakan pose yang ditahan diam, saat nilai energi gerak d(t) justru turun mendekati kondisi tenang. Alur segmentasi memisahkan tiga fase: (1) deteksi awal gerak (*onset*) saat d(t) melampaui ambang τ~onset~; (2) untuk 24 huruf statis, pencuplikan jendela tahan pose (*pose-hold window*) berdurasi L~hold~ sesudah *onset* mereda atau stabil, yang ambang dan durasinya ditala dari data validasi (bukan data uji); serta (3) untuk huruf dinamis J dan Z, penangkapan jendela lintasan penuh selama energi gerak melampaui ambang τ~dinamis~ hingga kembali tenang. Fitur tiap segmen, yaitu amplitudo dan fase *subcarrier* terpilih serta spektrum Doppler [6], [14], diringkas menjadi masukan *encoder*. Sebagai pembanding sensitivitas pada uji Delta-CSI (Subbab 3.8.1), varian berbasis amplitudo saja juga dihitung dan dilaporkan berdampingan:

```rumus
d~|H|~( t ) = ( 1 / |N~valid~| ) · Σ~n~ | |h~n~(t)| − |h~n~( t − 1 )| | , n ∈ N~valid~
```

Langkah berikutnya menutup temuan audit Subbab 2.4: bentuk masukan *checkpoint* harus disesuaikan sebelum dipakai. Kartu model mencatat masukan delapan fitur turunan pada laju 1 Hz [11], sedangkan jalur akuisisi menghasilkan 56 *subcarrier* pada 50 bingkai per detik [9], [10]. Empat rute evaluasi karenanya disiapkan sesuai Subbab 2.4: Jalur A (menghitung ulang delapan fitur turunan bawaan RuView beserta *standardizer*-nya), Jalur B1 (adapter rekonstruksi fitur), Jalur B2 (adapter terpandu tugas), serta Pembanding C (*baseline* CSI temporal lebih kaya tanpa penyempitan delapan fitur) [PERLU VALIDASI: bentuk masukan *checkpoint* dan rancangan adapter]. Setelah bentuk masukan pasti, alur fitur dibakukan pada tiga tingkat: bingkai CSI (56 *subcarrier*, hingga 50 bingkai per detik), jendela fitur sepanjang W = 1 detik yang diringkas menjadi satu vektor delapan fitur, dan langkah *embedding*, yaitu satu keluaran *encoder* per jendela. Jalur pertama menghitung ulang delapan fitur turunan bawaan RuView dari bingkai CSI; jalur kedua melatih adapter masukan kecil berbasis konvolusi satu dimensi yang memetakan jendela CSI mentah ke vektor masukan *encoder* sehingga informasi *subcarrier* tidak diringkas lebih dulu oleh rumus tetap. Pada kedua jalur, *encoder* diterapkan per jendela, bukan per bingkai, sesuai kontrak laju 1 Hz kartu model [11].

Pada rute *encoder* RuView (Jalur A dan Jalur B), setiap vektor masukan merangkum jendela sepanjang W = 1 detik dengan pergeseran (*hop*) H = 0,25 detik (usulan; dikalibrasi pada T2), menghasilkan tumpang tindih (*overlap*) sebesar 75%. Laju empat langkah per detik (1/H = 4 Hz) merupakan laju lompatan jendela yang saling tumpang tindih, bukan empat pengamatan temporal independen, karena setiap *embedding* tetap mengagregasi konteks satu detik. Untuk J dan Z, kelas tidak dibaca dari satu jendela: barisan langkah diproses modul temporal secara berurutan dan klasifikasinya diambil dari ringkasan barisan tersebut; lintasan gerak J dan Z karena itu tetap tersedia tanpa melanggar kontrak masukan *encoder*. Karena agregasi W = 1 detik berisiko mengaburkan lintasan cepat J dan Z, eksperimen wajib membandingkan konfigurasi (W = 1,0 s, H = 0,25 s) terhadap jendela lebih pendek (W = 0,5 s dengan H = 0,10 sampai 0,25 s) dan terhadap Pembanding C (*baseline* CSI temporal langsung pada W = 0,2 s atau laju bingkai asli tanpa penyempitan delapan fitur). Kandidat modul temporal ialah 1D-CNN ringan dari rancangan lama yang memelihara urutan waktu per langkah; agregasi statistik hanya menjadi kandidat bagi jalur klasifikasi, dan pilihan di antara keduanya diambil dari hasil ablasi pada data yang sama (Subbab 2.8).

Kompatibilitas representasi diuji pada gerbang G0b sebagai eksperimen sungguh-sungguh, bukan asumsi. Gerbang G0b dinilai setelah G0 atas data pilot satu pengisyarat satu sesi (sekitar 97 menit) yang direkam lebih dulu atau diambil dari sesi pertama T2. Alat ujinya *probe* linear, yaitu pengklasifikasi linear sederhana di atas *embedding* beku; cara ini baku untuk membaca seberapa informatif sebuah representasi tanpa melatih model penuh. Rangkaiannya: *probe* 24 huruf statis pada skema blok temporal, *probe* sekuensial atas gabungan langkah tiap segmen, *probe* biner J terhadap Z, serta perbandingan langsung terhadap Pembanding C (fitur CSI mentah atau lebih kaya). Untuk memvalidasi signifikansi statistik secara benar, dilakukan uji permutasi (*permutation test*): label kelas diacak pada level blok atau repetisi independen (bukan per *window* tumpang tindih) sebanyak M = 1.000 iterasi untuk membentuk distribusi *null* acak; pengujian dinyatakan signifikan apabila skor F1 makro *probe* berlabel asli melampaui persentil ke-95 distribusi *null* (p~perm~ < 0,05), sementara skor pada label teracak tetap berada di sekitar peluang acak. Ambang usulannya: F1 makro *probe* sekurang-kurangnya 0,30 dan sekurang-kurangnya tiga kali peluang acak; *probe* J–Z sekurang-kurangnya 70%; seluruhnya difinalkan bersama pembimbing sebelum gerbang dinilai. Jalur A dipakai jika lulus; jika gagal, diuji Jalur B1 (rekonstruksi) dan Jalur B2 (adapter terpandu tugas); jika seluruh jalur masukan delapan fitur tetap gagal, skema adaptasi LoRA dan pelatihan lanjutan (Subbab 2.5) diuji secara berdampingan dengan Pembanding C (CSI lebih kaya tanpa penyempitan delapan fitur), karena adaptasi bobot *encoder* tidak dapat memulihkan informasi jari yang hilang sebelum masuk *encoder*; seluruh hasilnya dilaporkan sebagai temuan.

*Dataset* murid terbentuk dengan menyelaraskan tiga deret menurut penanda waktu: jendela CSI hasil segmentasi, label huruf dari kartu pemandu protokol, dan deret *keypoint* guru. Guru memakai model juara pra-penelitian dari repositori peneliti [12]. Label kelas tiap segmen diambil dari kartu pemandu protokol; keluaran kelas guru hanya dipakai sebagai salinan pembanding untuk penyaringan kualitas, bukan sebagai label kebenaran. Ketidakcocokan antara label protokol dan kelas guru dicatat sebagai temuan kualitas anotasi dan dilaporkan bersama tingkat segmen terbuang. Jika rekaman baru memperlihatkan pergeseran domain yang menurunkan kualitas deteksi, guru menjalani pelatihan lanjutan di layanan GPU Kaggle dengan alur kerja yang sudah teruji itu sebelum labelnya dipakai. Seluruh pasangan direkam dalam struktur *dataset* berpasangan Subbab 2.17, lengkap dengan mask visibilitas, metadata sesi, dan skor kualitas anotasi.

Deret *keypoint* guru dipasangkan ke titik pusat waktu tiap jendela CSI dengan laju yang sama dengan keluaran modul temporal. Untuk mengevaluasi galat lintasan J dan Z secara jujur, metrik MPJPE dan PCK@α dilaporkan secara utama pada resolusi langkah model (dengan mask efektif m∗~itj~ sesuai Persamaan 2.13a agar langkah *padding* tidak terhitung). Apabila dilakukan interpolasi ke laju kamera untuk perbandingan visual bingkai demi bingkai dengan acuan guru, ditegaskan bahwa interpolasi tidak menciptakan informasi temporal baru yang tidak diamati dan hasilnya hanya berstatus pelaporan sekunder; metode interpolasinya dinyatakan pada laporan. Panjang T ditetapkan 16 langkah per segmen (usulan; difinalkan dari distribusi durasi segmen pada data pilot T2 tanpa memakai data uji); pada lompatan H = 0,25 detik, selisih pusat jendela pertama ke langkah ke-16 adalah (16 − 1) × 0,25 = 3,75 detik, sedangkan rentang sinyal mentah yang tercakup dari awal jendela pertama hingga akhir jendela ke-16 mencapai 4,75 detik untuk segmen valid penuh. Segmen lebih pendek diberi *padding* nol dengan mask valid, dan kerugian regresi dinormalisasi oleh jumlah langkah valid; mask visibilitas Persamaan 2.13 diperluas satu dimensi waktu. Resampling ke panjang tetap tidak dipakai untuk pelatihan J dan Z karena menyeragamkan durasi dan menghapus petunjuk kecepatan yang justru membedakan kedua huruf itu.

Enam skema pada Tabel 3.4 mengukur kinerja; untuk skema dalam sesi, pembagiannya temporal per blok dan tidak acak. Untuk mencegah kebocoran data (*data leakage*) akibat tumpang tindih jendela sebesar 75%, seluruh pembagian data latih, validasi, dan uji pada keenam skema wajib dilakukan pada level rekaman mentah, sesi, atau blok/grup repetisi sebelum pembentukan jendela bergulir (*sliding windows*), disertai celah pemisah (*purge gap*) sekurang-kurangnya sepanjang W (satu detik) pada perbatasan blok agar tidak ada jendela yang memotong batas set latih dan uji. Data validasi hanya berasal dari data latih, sehingga data uji tidak pernah dipakai untuk memilih *subcarrier*, menormalkan fitur, menetapkan ambang, ataupun menala bobot kerugian (Tabel 3.7).

Tabel 3.4 Skema pembagian data

| No. | Skema | Data latih | Data uji | Aspek yang diukur |
|---|---|---|---|---|
| 1 | Dalam sesi (blok temporal) | Blok awal satu sesi | Blok akhir sesi yang sama | Separabilitas orang, ruang, sesi sama |
| 2 | Lintas sesi | Sebagian sesi pengisyarat di satu ruang | Sesi lain, ruang sama | Ketahanan antarsesi |
| 3 | Lintas partisipan (*leave-one-subject-out*) | Semua pengisyarat kecuali satu | Pengisyarat yang ditinggalkan, bergiliran | Ketahanan pergantian orang |
| 4 | Lintas ruang (*leave-one-room-out*) | Semua ruang kecuali satu | Ruang yang ditinggalkan, bergiliran | Ketahanan pergantian ruang |
| 5 | Pengguna baru | Seluruh pengisyarat | Satu pengguna baru tanpa pelatihan ulang | Kesiapan orang baru |
| 6 | Lintas posisi | Posisi berdiri (atau sebaliknya) | Posisi duduk | Ketahanan pergeseran posisi |

Pelatihan berjalan di komputer dengan Python dan PyTorch karena keduanya kompatibel dengan *checkpoint* dan mendukung autograd serta pengoptimal; layanan GPU Kaggle dipakai jika kapasitas GPU lokal tidak cukup. Baseline dilatih dengan urutan yang eksplisit. *Encoder* dimuat lalu dibekukan, dan geometri *embedding*-nya diverifikasi lewat uji triplet kecil pada data sendiri. Setelah itu, kedua kepala beserta modul temporal dilatih serentak dengan kerugian gabungan Persamaan (2.14) dan (2.15), memakai *seed* tetap dan *early stopping* pada data validasi. Ablasi dijalankan sebagai rangkaian pembanding pada data dan seed yang sama: kepala klasifikasi saja tanpa kepala regresi, multitugas penuh, dan variasi bobot λ~reg~; manfaat supervisi *keypoint* dibaca dari selisih ketiganya, termasuk jika manfaatnya nihil. Sebagai pembanding lanjutan jika waktu dan data mencukupi, adaptasi LoRA (Persamaan 2.7) [17] dan pelatihan lanjutan sebagian atau seluruhnya dijalankan pada pembagian yang sama. Seluruh hasilnya dilaporkan berdampingan, bukan hanya yang terbaik.

Keluaran klasifikator dilengkapi skor keyakinan dan mekanisme penolakan [18]. Segmen di bawah ambang berujung status penolakan pada kedua arah: *speaker* tidak mengucapkan apa pun dan layar memunculkan pesan isyarat tidak dikenali. Menolak lebih aman daripada menebak kelas yang salah; ambangnya ditetapkan dari data validasi, dan kecukupannya diperiksa lewat laju deteksi palsu serta penilaian validator (Subbab 3.8).

Setelah terpilih, model *deployment* disusun menurut Pilihan 1: *encoder*, adapter (jika dipakai), modul temporal, dan kepala klasifikasi digabung menjadi satu *graph* inferensi lalu dikuantisasi; kepala regresi dilepas setelah pelatihan karena perannya supervisi tambahan. Kepala regresi ikut dijalankan pada *deployment* (Pilihan 2) hanya jika keputusan pada Tabel 3.7 menyatakannya, dengan tambahan biaya memori, komputasi, dan kuantisasi yang diukur serta dilaporkan. Skema kuantisasinya affine 8-bit [23]: nilai x dipetakan ke bilangan bulat q lewat skala s dan titik nol z~0~

```rumus
q = round( x / s ) + z~0~, dengan s = ( x~maks~ − x~min~ ) / 255 (3.2)
```

dengan parameter s dan z~0~ dihitung dari data kalibrasi; varian float16, int8, dan int4 dievaluasi masing-masing sesuai dukungan operator pada *runtime*. Jalur ekspornya dinyatakan realistis dan bertahap. Format bobot *checkpoint* diperiksa lebih dulu, lalu operator BatchNorm dan GELU diverifikasi pada *runtime* kandidat di ESP32-S3, baik lewat ESP-DL dengan akselerasi ESP-NN maupun TensorFlow Lite Micro [23]. Klaim dukungan operator tidak dibuat sebelum terverifikasi [PERLU VALIDASI: dukungan operator runtime tepi]. Radio tetap terikat satu kanal bersama *access point* dengan *power save* dimatikan [10]. Alur inferensi pada perangkat tampak pada Gambar 3.5. Bingkai hasil *callback* CSI masuk ke penyangga geser, segmen terdeteksi dari energi gerak, dan masukan *encoder* disiapkan sesuai hasil audit. Model terkuantisasi menghasilkan kelas dan skor, lalu keluaran di atas ambang dikirim melalui UDP. Waktu inferensi per segmen, pemakaian memori, serta pengaruhnya pada laju pemrosesan diukur lalu dilaporkan; jika model terbukti terlalu berat, klasifikasi pindah ke server menurut jalur cadangan (Subbab 3.11).

```mermaid
flowchart LR
    accTitle: Alur inferensi langsung pada ESP32-S3 menurut deployment Pilihan 1
    accDescr: Bingkai hasil callback CSI masuk ke penyangga geser di PSRAM dengan pemeriksaan subcarrier valid dan first_word_invalid; segmentasi perangkat memisahkan onset Delta-CSI, jendela tahan pose untuk huruf statis, dan jendela lintasan untuk J dan Z; masukan diekstraksi sesuai rute hasil audit; model terkuantisasi berisi encoder, modul temporal, dan kepala klasifikasi saja karena kepala regresi dilepas sesuai Pilihan 1; keluaran di atas ambang ditampilkan dan dikirim via UDP ke server Rust, keluaran di bawah ambang ditolak tanpa memicu suara.

    subgraph R1["Akuisisi dan segmentasi"]
        direction TB
    CSI["Callback CSI promiscuous<br/>(subcarrier valid, filter MAC)"]
    BUF["Penyangga geser<br/>CSI di PSRAM"]
    SEG["Segmentasi: onset,<br/>tahan pose / lintasan"]
    FT["Masukan teraudit<br/>(Jalur A / B / C)"]
    CSI --> BUF
    BUF --> SEG
    SEG --> FT
    end
    subgraph R2["Inferensi Pilihan 1"]
        direction TB
    MOD["Model int8/fp16: encoder +<br/>temporal + klasifikasi"]
    DEC{"Keyakinan di<br/>atas ambang?"}
    OUT["Tampil + UDP label/skor<br/>ke server Rust"]
    RJ["Tolak: tidak dikenali<br/>(tanpa suara)"]
    MOD --> DEC
    DEC -- "ya" --> OUT
    DEC -- "tidak" --> RJ
    end
    R1 --> R2
```

Gambar 3.5 Alur inferensi langsung pada ESP32-S3 menurut rancangan *deployment* Pilihan 1 tanpa kepala regresi (aktivasi kepala regresi Pilihan 2 menunggu konfirmasi Tabel 3.7 no. 19), dengan segmentasi tiga fase dan mekanisme tolak; seluruh latensi dan memori diukur langsung pada perangkat, bukan dijanjikan

## 3.8 Skenario Pengujian dan Metrik Evaluasi

G0 berdiri di atas uji Delta-CSI dan koeksistensi, G1 di atas uji model pada Subbab 3.8.2, G2 di atas konsultasi tiga pilar, G3 di atas uji operasional dan jalur ucapan, serta G4 di atas uji kegunaan, penilaian validator, dan analisis biaya. Satu uji lagi, cakupan kamus, melengkapi analisis tanpa menjadi syarat gerbang. Seluruh hasil klasifikasi, regresi, dan operasional dilaporkan sebagai bukti awal pada populasi terbatas 3–4 pengisyarat, sedikitnya dua ruang, dan satu konfigurasi perangkat; skema *leave-one-subject-out*, pengguna baru, dan *leave-one-room-out* dibaca sebagai indikasi ketahanan awal, bukan bukti generalisasi populasi (Subbab 1.4). Rincian prasyarat, metrik, ambang, dan bukti setiap uji dirinci pada Rencana Penjaminan Mutu Subbab 3.13, sedangkan temuan audit atas sumber implementasi yang mendasari rancangan ini dirangkum pada Subbab 3.12.

### 3.8.1 Uji Delta-CSI dan Koeksistensi

Satu pertanyaan dijawab uji Delta-CSI: apakah gerak tubuh menghasilkan perubahan CSI yang terpisah jelas dari kondisi tanpa gerak (ukuran keterpisahannya pada Tabel 3.7). Prosedurnya sebagai berikut.

1. Memasang kedua modul pada posisi awal sehingga mengapit zona isyarat.
2. Merekam CSI dalam tiga kondisi dasar (ruang kosong, pengisyarat diam, dan pengisyarat bergerak) ditambah uji pilot beberapa konfigurasi tangan statis yang berbeda, orientasi telapak yang berbeda, serta percobaan awal huruf J dan Z.
3. Menjalankan modul penerima dengan CSI, koneksi *station*, dan UDP secara serentak, termasuk saat *streaming* audio, serta mencatat laju CSI aktual dan paket yang hilang.
4. Membandingkan pola antarkondisi, lalu mencatat dan menganalisis hasilnya sebagai bahan G0.

### 3.8.2 Uji Klasifikasi, Regresi, dan Ablasi

Keenam skema Tabel 3.4 diuji dengan metrik Subbab 2.14, selalu dibandingkan terhadap peluang acak sekitar 3,8% untuk 26 kelas; angka acak itu dihitung ulang jika cakupan dipangkas. Akurasi dilaporkan dalam dua versi, yaitu tanpa penolakan pada seluruh segmen uji dan dengan penolakan pada segmen yang diterima. *Recall* tiap kelas dilaporkan, dengan *recall* J dan Z terpisah beserta *confusion* terhadap huruf paling mirip. Kinerja kepala regresi dilaporkan dengan MPJPE, NME, PCK@α, dan galat per *keypoint* (Subbab 2.14), dan galat itu dirinci untuk pasangan huruf paling mirip serta lintasan J dan Z. Pembanding ablasi dilaporkan berdampingan: kepala klasifikasi saja, multitugas penuh, dan variasi bobot λ~reg~; manfaat supervisi *keypoint* dinyatakan dari selisihnya, termasuk jika manfaatnya nihil. Evaluasi klasifikasi juga memisahkan dua taraf penilaian: (a) kelayakan ilmiah awal (*scientific feasibility*), yakni bukti adanya daya pisah sinyal CSI jauh di atas peluang acak maupun pembanding tunggal, dan (b) kegunaan operasional (*operational usability*) untuk komunikasi nyata di kelas. Untuk mekanisme penolakan [18], setiap eksperimen wajib melaporkan bersama-sama akurasi keseluruhan tanpa penolakan, cakupan diterima (*accepted coverage*), akurasi selektif (*selective accuracy*) pada segmen yang lolos ambang keyakinan, laju terima palsu (*false accept*), laju tolak palsu (*false reject*), serta waktu inferensi persentil p50 dan p95.

### 3.8.3 Uji Operasional

Tiga hal diukur pada uji operasional: deteksi palsu per jam tanpa peragaan, latensi ujung ke ujung tiap arah, dan konsumsi arus modul. Prosedurnya sebagai berikut.

1. Menjalankan purwarupa di ruang yang sudah terkalibrasi.
2. Merekam kondisi tanpa peragaan, termasuk ketika orang lewat dan kipas menyala, lalu mencatat isyarat yang terdeteksi.
3. Meminta pengisyarat memperagakan isyarat target, lalu mencatat waktu selesainya isyarat dan terdengarnya suara; pada arah kedua, mengucapkan frasa uji dan mencatat waktu representasi tampil.
4. Mengukur arus modul pada beberapa kondisi kerja, kemudian menghitung estimasi ketahanan baterai.
5. Menghitung biaya purwarupa dari harga komponen serta perkiraan biaya layanan ucapan per jam pemakaian.
6. Menganalisis deteksi palsu, latensi pada kedua arah, dan ketahanan baterai terhadap indikator layak yang ditetapkan kemudian (Tabel 3.7).

Tiga perhitungan penunjang dirumuskan lebih dulu agar hasilnya bisa diperiksa ulang. Latensi ujung ke ujung dirumuskan terpisah untuk masing-masing arah karena perbedaan komponennya, dan keduanya diukur pada mode daring serta luring dengan pelaporan persentil p50 dan p95:

```rumus
T~1~ = t~CSI-buf~ + t~seg~ + t~inf-tepi~ + t~tel~ + t~peta~ + t~TTS~ + t~audio-dl~ + t~putar~ (3.3a)
T~2~ = t~rekam~ + t~audio-ul~ + t~ASR~ + t~kamus~ + t~tampil~ (3.3b)
```

dengan T~1~ mencakup latensi pasca-akhir segmen isyarat hingga awal pemutaran suara (termasuk varian klip ter-*cache* 26 huruf maupun sintesis langsung) dan T~2~ mencakup akhir ujaran PTT hingga tampilnya representasi SIBI di aplikasi Tauri; anggaran per tahap dan ambang totalnya diuji pada G3 (Tabel 3.5). Biaya purwarupa dihitung dari tabel BOM riil seluruh komponen dengan memisahkan harga pasangan modul ESP32-S3 inti dari total komponen antarmuka lengkap (Persamaan 3.5). Ketahanan baterai diestimasi dari kapasitas baterai C~baterai~ dan arus rata-rata terukur I~rata~:

```rumus
T~baterai~ ≈ 0,8 · C~baterai~ / I~rata~ (3.4)
```

Faktor 0,8 menampung efisiensi konverter dan penuaan baterai. Sebagai ilustrasi angka, baterai 2.500 mAh pada arus rata-rata 250 mA bertahan kira-kira delapan jam; angka arus sebenarnya diukur pada langkah keempat, bukan diasumsikan. Biaya total purwarupa menjumlahkan harga seluruh komponen b~j~ dan biaya layanan ucapan per jam:

```rumus
B~total~ = Σ~j~ b~j~ + b~layanan~ · t~pakai~ (3.5)
```

dengan t~pakai~ jam pemakaian layanan selama uji.

### 3.8.4 Uji Jalur Ucapan dan Cakupan Kamus

Komponen bahasa pada kedua arah dinilai lewat uji jalur ucapan, yang membandingkan jalur *on-device*, awan, dan server lokal disertai cakupan kamus arah kedua. Prosedurnya sebagai berikut.

1. Menyiapkan daftar frasa uji pendek berbahasa Indonesia [PERLU DATA: daftar frasa uji dan jumlah penutur] yang memuat kata di dalam dan di luar kamus.
2. Merekam teks keluaran layanan ASR awan (daring) dan `faster-whisper` (luring) pada frasa uji bahasa Indonesia, lalu melaporkan WER beserta rincian (S, D, I, N) (Persamaan 2.23) dan *exact-match rate* tanpa memakai rumus 1 − WER.
3. Mengukur waktu pengenalan, pemetaan, waktu menuju audio pertama (TTFA) sintesis TTS, serta total ujung ke ujung pada kedua arah.
4. Mengulang pengukuran pada kandidat mesin (MMS-TTS-ind ONNX sebagai kandidat utama dan Kokoro ONNX sebagai pembanding) di server lokal maupun *on-device* ponsel serta jalur pembanding awan, lalu menimbang mutu dan latensinya.
5. Memverifikasi prasyarat suara Indonesia sambil mengukur *parsing* UDP dan memori server Rust (Subbab 2.13).
6. Mencatat proporsi kata uji yang tampil sebagai representasi isyarat, ejaan jari, dan gagal tampil, kemudian menganalisis mutu, latensi, serta ketergantungan internet sebagai bahan keputusan G3 (Tabel 3.7).

### 3.8.5 Uji Kegunaan dan Penilaian Validator

Uji kegunaan diposisikan sebagai uji kelayakan skala kecil: hasilnya dianalisis secara deskriptif untuk menemukan hambatan pemakaian dan mengarahkan perbaikan purwarupa, bukan sebagai bukti efektivitas pada populasi pengguna; rumusan ini selaras dengan Batasan no. 9. Keterpakaian purwarupa ditelaah lewat uji kegunaan bersama 3–5 pengguna kelompok sasaran pada skenario tugas terbimbing, yaitu saling menyampaikan pesan pendek melalui ejaan huruf dan kosakata tampilan. Tiap pengguna menjalani langkah berikut.

1. Menjelaskan tujuan uji, batas kosakata, kenyataan bahwa kamera tidak menyala, dan hak mundur, lalu meminta persetujuan tertulis.
2. Memberi waktu berlatih singkat bersama kamus tampilan.
3. Menjalankan tugas komunikasi dua arah sambil mencatat keberhasilan, waktu penyelesaian, dan keluaran yang menyesatkan.
4. Meminta pengguna mengisi kuesioner skala Likert [28] mengenai kegunaan, kejelasan, dan keinginan memakai ulang.
5. Merekapitulasi hasil, lalu menganalisisnya secara deskriptif tanpa klaim kausal.

Kewajaran keluaran kedua arah dinilai validator penutur tunarungu; keluaran sistem dan penilaian independennya dicatat dalam tabel silang, sedangkan kasus yang dinilai keliru dilaporkan tersendiri. Sebagai analisis sekunder, kesalahan klasifikator dikaitkan luring dengan kemiripan pose pada deret *keypoint* guru agar kesalahan konfigurasi mirip dapat dibedakan dari kesalahan sinyal lemah.

### 3.8.6 Kriteria Gerbang Keputusan

Tabel 3.5 menyajikan kriteria tiap gerbang beserta tindakan jika gagal. Kelayakan pada rumusan ketiga ditinjau per dimensi, bukan semata dari lolosnya G4, dan ambang kuantitatifnya difinalkan bersama pembimbing sebelum gerbang dinilai.

Tabel 3.5 Kriteria gerbang keputusan

| Gerbang | Nama dan waktu | Kriteria lolos (ambang usulan) | Tindakan jika gagal |
|---|---|---|---|
| G0 | Baseline CSI dan jaringan, akhir M2 | Versi atau komit *firmware* RuView dikunci dan tercatat; konfigurasi dua node peran tetap terverifikasi berjalan tanpa implementasi ESP-NOW tambahan; akuisisi *subcarrier* valid N~valid~ (LLTF/HT-LTF, *pilot*, `first_word_invalid` diaudit) pada jarak 1 m ke UDP Rust terbaca stabil saat trafik OFDM terjadwal dan pengiriman UDP berjalan bersamaan; atribusi bingkai CSI ke tautan TX-RX terverifikasi lewat penandaan atau penyaringan MAC pengirim; laju sekurang-kurangnya 25 bingkai per detik; paket hilang tidak melampaui 0,1%; pola bergerak terpisah dari diam; keterpisahan awal beberapa pose tangan statis teramati; audit sisa *phase drift* Persamaan (2.5) dan audit artefak *encoder* (pemilihan berkas v1/v2, *standardizer*) selesai | Perbaikan penempatan satu kali; gagal lagi berarti jalur CSI dihentikan dan dilaporkan |
| G0b | Audit kompatibilitas representasi *encoder*, setelah G0 atas data pilot (awal T2) | *Probe* linear 24 huruf statis dan *probe* sekuensial di atas *embedding* beku: F1 makro sekurang-kurangnya 0,30 dan sekurang-kurangnya tiga kali peluang acak; *probe* biner J–Z sekurang-kurangnya 70% [usulan]; skor label asli melampaui persentil ke-95 distribusi *null* uji permutasi blok/repetisi (p~perm~ < 0,05); perbandingan langsung terhadap Pembanding C tercatat; keputusan jalur masukan tercatat | Jalur A gagal maka Jalur B1/B2 diuji; seluruh jalur delapan fitur gagal maka LoRA/pelatihan lanjutan dijalankan berdampingan dengan Pembanding C (CSI lebih kaya tanpa *bottleneck* 8 fitur) dan hasilnya dilaporkan sebagai temuan |
| G1 | Model tepi terkuantisasi dan dua kepala, akhir M8 | Akurasi dalam sesi sekurang-kurangnya 50% (sekitar 13 kali acak 3,8%) sebagai ambang kelayakan ilmiah awal, bukan klaim siap pakai operasional; F1 makro sekurang-kurangnya 0,45 [usulan]; tidak ada kelas dengan *recall* nol pada himpunan huruf terpilih; melampaui pembanding ablasi kepala tunggal dengan manfaat multitugas dilaporkan; cakupan diterima dan akurasi selektif dilaporkan berpasangan; *recall* J dan Z dilaporkan terpisah beserta *confusion* terhadap huruf paling mirip; MPJPE pada resolusi langkah model dilaporkan sebagai pemantauan; inferensi terkuantisasi di bawah 100 ms; pemangkasan himpunan huruf dilarang memakai informasi data uji; seluruh ambang difinalkan bersama pembimbing sebelum G1 dinilai | Pangkas himpunan huruf pembeda terkuat berbasis data validasi, lalu nilai ulang |
| G2 | Tiga pilar pakar, akhir M10 | Penilaian tertulis pakar SIBI-aksesibilitas, RF-*wireless sensing*, dan *embedded AI* masuk semua; tanpa temuan blok kritis; skor rata-rata per pilar sekurang-kurangnya 3 dari 5 | Perbaiki temuan blok atau sempitkan klaim, lalu nilai ulang |
| G3 | Integrasi Rust dan mesin ucapan, M11 | Latensi Persamaan (3.3a) Arah 1 tidak melampaui 2 detik dan Persamaan (3.3b) Arah 2 tidak melampaui 3 detik pada jalur utama server lokal (5 detik untuk jalur cadangan *on-device*), diukur daring dan luring dengan pelaporan p50 dan p95; TTFA di bawah 100 ms pada frasa uji paling banyak lima kata pada kondisi terdokumentasi; *parsing* UDP di bawah 0,2 ms; memori server di bawah 40 MB; konfigurasi TTS Indonesia mengikuti keputusan Tabel 3.7 no. 17 (kandidat default MMS-TTS-ind ONNX dengan opsi *pre-cache* 26 huruf tunggal) kecuali Kokoro mendukung bahasa Indonesia sebelum G3 | Beralih ke mesin alternatif, lalu jalur *on-device* ponsel atau awan; melampaui berarti temuan |
| G4 | Sintesis kelayakan, akhir M12 | Skor persepsi rata-rata sekurang-kurangnya 3,0 dari 5 (dianalisis deskriptif: median, rentang, per partisipan); validator menyetujui kewajaran; BOM biaya lengkap; rekomendasi TKT 3–4 tertulis mengacu pada Permenristekdikti Nomor 42 Tahun 2016 [31] beserta indikator capaian Perdirjen Penguatan Risbang 603/E1.2/2016 | Hasil negatif tetap dilaporkan; rekomendasi menyatakan posisi lebih rendah beserta alasan |

## 3.9 Jadwal Penelitian

Tabel 3.6 memuat jadwal empat belas minggu; tanda ■ menandai minggu pelaksanaan.

Tabel 3.6 Jadwal penelitian

| No. | Kegiatan | M1 | M2 | M3 | M4 | M5 | M6 | M7 | M8 | M9 | M10 | M11 | M12 | M13 | M14 | Gerbang |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | T0 Replikasi platform, audit *checkpoint*, uji Delta-CSI, dan koeksistensi | ■ | ■ | | | | | | | | | | | | | G0 (akhir M2) |
| 2 | T1 Kurasi alfabet SIBI dan kosakata, kalibrasi ruang, protokol, perizinan, perekaman pilot G0b | | ■ | ■ | ■ | | | | | | | | | | | G0b (awal T2 / M4) |
| 3 | T2 Perekaman *dataset*, pelatihan dua kepala, kuantisasi, uji *deployment* | | | | ■ | ■ | ■ | ■ | ■ | | | | | | | G1 (akhir M8) |
| 4 | T3 Uji lintas sesi, partisipan, ruang, dan pengguna baru | | | | | | | | ■ | ■ | ■ | | | | | G2 (akhir M10) |
| 5 | T4 Pengemasan dua arah, Rust, TTS server lokal, uji operasional, jalur ucapan, kamus, kegunaan, validator | | | | | | | | | | ■ | ■ | ■ | | | G3 (M11), G4 (akhir M12) |
| 6 | T5 Analisis dan penulisan | | | | | | | | | | | | ■ | ■ | ■ | — |

## 3.10 Parameter Rancangan yang Ditetapkan Kemudian

Sebagian parameter bergantung pada kesepakatan pembimbing, hasil tahap sebelumnya, atau data validasi. Parameter semacam itu dihimpun pada Tabel 3.7 dan ditetapkan lebih dulu sebelum dipakai menilai data uji maupun gerbang terkait. Untuk memperjelas batas keputusan, Tabel 3.7 terbagi dua kelompok: baris 1, 13, 14, 16, 17, 19, dan 20 merupakan keputusan desain dan administratif inti yang memerlukan konfirmasi pembimbing, sedangkan baris 2 sampai 12, 15, 18, serta 21 sampai 22 merupakan parameter teknis dan *hyperparameter* yang penetapannya berbasis hasil audit atau data validasi.

Tabel 3.7 Parameter rancangan yang ditetapkan kemudian

| No. | Parameter | Waktu atau dasar penetapan | Status |
|---|---|---|---|
| 1 | Finalisasi ambang seluruh gerbang G0–G4 | Sebelum gerbang dinilai | [PERLU DATA: finalisasi ambang usulan Tabel 3.5 bersama pembimbing] |
| 2 | Ambang G1, tindakan gagal kedua, dan kriteria pemangkasan himpunan huruf | Sebelum eksperimen | [PERLU DATA: ambang, tindakan, dan kriteria pemangkasan tanpa data uji] |
| 3 | Kriteria kualitas model guru | Sebelum pelatihan murid | [PERLU DATA: ambang deteksi tangan, batas jitter, prosedur sampel] |
| 4 | Pemilihan *subcarrier*, lintasan puncak, dan segmentasi huruf statis | Sebelum dipakai | [PERLU DATA: kriteria, definisi operasional, ambang dan jendela tahan pose] |
| 5 | Pembagian data dan strategi Widar3.0 | Sebelum dipakai | [PERLU DATA: blok, proporsi latih-validasi-uji, komponen strategi, repetisi uji] |
| 6 | Pilihan jalur masukan *encoder* (fitur turunan atau adapter), parameter normalisasi masukan, panjang barisan T, serta pemilihan keluarga berkas *checkpoint* (`model.safetensors` lawan `csi-embed-v2`) beserta rekonsiliasi metadata kartu model (AUD-07, AUD-08) | Hasil audit T0 dan gerbang G0b | [PERLU VALIDASI: parameter normalisasi masukan checkpoint; pemilihan keluarga berkas; keputusan jalur G0b; finalisasi T dari data pilot] |
| 7 | Sistem koordinat target regresi, konvensi *handedness*, skala acuan d~ref~, dan ambang α | Sebelum pelatihan | [PERLU VALIDASI: sistem koordinat, *handedness*, dan ambang PCK] |
| 8 | Status modul temporal final (1D-CNN atau agregasi statistik) | Dari hasil ablasi | [PERLU DATA: keputusan modul temporal beserta bukti ablasi] |
| 9 | Bobot λ~cls~, λ~reg~, normalisasi skala kerugian, dan ambang keyakinan | Dari data validasi | [PERLU DATA: nilai bobot, skema normalisasi, dan ambang] |
| 10 | Peringkat LoRA r dan lapis yang disadap | Sebelum adaptasi dijalankan | [PERLU VALIDASI: kompatibilitas LoRA dengan alur ekspor dan pilihan r] |
| 11 | Perlakuan data uji | Sebelum dipakai | [PERLU DATA: segmen tersaring kamera atau segmentasi tanpa koreksi] |
| 12 | Inklusi partisipan, sesi per ruang, dan token apresiasi | Sebelum dipakai | [PERLU DATA: kriteria kompetensi, kefasihan validator, pengguna uji, token] |
| 13 | Publikasi *dataset* dan persetujuan etik | Sebelum dipakai | [PERLU DATA: izin, repositori, lisensi, lembaga persetujuan etik] |
| 14 | Rubrik tiga pilar pakar dan personalisasi jika G2 gagal | Sebelum G2 dinilai | [PERLU DATA: rubrik, ambang skor, prosedur data latih pengguna] |
| 15 | Indikator layak operasional dan durasi pengamatan deteksi palsu | Sebelum G3 dinilai | [PERLU DATA: anggaran latensi, batas deteksi palsu, baterai minimum, durasi] |
| 16 | Kanal, jarak antarmodul, zona, model layar, audio, dan kapasitas baterai | Pada T0 atau sebelum T4 | [PERLU DATA: penetapan, model layar final, kapasitas dari uji arus] |
| 17 | Prioritas mesin TTS operasional (verifikasi primer: Kokoro v1.0 tanpa suara Indonesia; kandidat utama MMS-TTS-ind ONNX dengan opsi *pre-cache* 26 huruf), lokasi sintesis D3, layanan ASR, dan frasa uji | Pada G3 | [PERLU KONFIRMASI: pergeseran default ke MMS-TTS-ind menunggu persetujuan; keputusan final mesin, lokasi, layanan, dan daftar frasa dari uji banding G3] |
| 18 | Kuesioner, rubrik validator dan pakar, serta asumsi biaya G4 | Sebelum T4 | [PERLU DATA: butir kuesioner, rubrik, batas kesesuaian, harga dan asumsi] |
| 19 | Model *deployment* (Pilihan 1: klasifikator saja, kepala regresi dilepas setelah pelatihan; Pilihan 2: dua kepala aktif) | Tujuan eksperimen dan hasil ablasi manfaat regresi | [PERLU KONFIRMASI: teks Subbab 3.5 dan 3.7 mengarah ke Pilihan 1 (klasifikator saja); penguncian final menunggu konfirmasi pembimbing dan hasil ablasi] |
| 20 | Akhiran judul (PEMROSESAN SERVER atau CLOUD PROCESSING) | Kesesuaian dengan arsitektur aktual yang berpusat di server | [PERLU DATA: keputusan akhiran judul bersama pembimbing] |
| 21 | Peran ESP-NOW dan konfigurasi node akuisisi CSI (ESP-NOW dikeluarkan dari jalur inti; dua node peran tetap diverifikasi tanpa implementasi ESP-NOW tambahan; sinkronisasi *mesh* hanya jika diperlukan) | Keputusan pemilik 14 Nov 2026 atas audit dokumentasi *firmware* RuView [32], [33] | Ditetapkan; ESP-NOW diaktifkan kembali hanya jika konfigurasi *mesh* TDM memerlukannya dan penggunaannya dilaporkan |
| 22 | Mekanisme akuisisi CSI *baseline* (trafik OFDM terjadwal *self-ping* 10–50 Hz ke *gateway*, *callback* CSI mode *promiscuous*, transport UDP ADR-018; injeksi NDP masih *stub* ADR-029 sehingga tidak dipakai; atribusi bingkai ke tautan TX-RX lewat penandaan MAC pengirim) | Audit kode *firmware* 15 Nov 2026 (Subbab 3.12, AUD-01 sampai AUD-04) | Ditetapkan; injeksi NDP dievaluasi ulang hanya jika *controller PR* RuView mendarat sebelum T2 dan perubahannya dilaporkan |

## 3.11 Risiko dan Alternatif Cadangan

Tabel 3.8 merangkum risiko utama beserta mitigasinya. Cadangan disusun bertingkat mengikuti titik kegagalan, sehingga kegagalan komponen hanya mempersempit klaim tanpa menghentikan penelitian; setiap pemakaian cadangan tercatat dalam laporan akhir.

Tabel 3.8 Risiko dan mitigasi

| No. | Risiko | Dampak | Mitigasi dan cadangan |
|---|---|---|---|
| 1 | Pola CSI isyarat tidak terpisah pada konfigurasi dua modul | G0 gagal; jalur CSI tidak layak | Perbaikan penempatan satu kali; gagal lagi berarti dihentikan dan dilaporkan |
| 2 | Bentuk masukan *checkpoint* tidak sesuai jendela CSI (delapan fitur turunan lawan 56 *subcarrier*) | *Encoder* tidak bisa dipakai langsung | Hitung fitur turunan bawaan RuView atau latih adapter masukan; hasil audit T0 dilaporkan |
| 3 | *Embedding* *encoder* beku tidak memisahkan kelas huruf | Kepala tidak dapat belajar | Uji Jalur B2 (adapter terpandu tugas), LoRA/pelatihan lanjutan, dan Pembanding C (*baseline* CSI temporal lebih kaya tanpa *bottleneck* 8 fitur) secara berdampingan untuk membedakan kegagalan representasi masukan dari kegagalan bobot *encoder*; hasilnya dilaporkan apa adanya |
| 4 | Konflik gradien antartugas multitugas | Salah satu tugas terhambat | Penyeimbangan gradien atau pelatihan bergantian; kepala tunggal pembanding |
| 5 | Akurasi lintas partisipan, ruang, atau posisi rendah (G2 gagal) | Klaim pengguna baru tak dapat dibuat | Personalisasi per pengguna (cadangan A); dilaporkan |
| 6 | Model terkuantisasi terlalu berat atau lambat di modul | Inferensi tepi tidak tercapai | Klasifikasi dipindah ke server, modul kirim fitur (cadangan B) |
| 7 | Beban radio gabungan CSI, UDP, dan audio bermasalah | Purwarupa tidak stabil | Modul ketiga khusus antarmuka (cadangan C) |
| 8 | Layanan ucapan tidak memadai; Kokoro-82M v1.0 terkonfirmasi tanpa suara Indonesia [24] | Jalur ucapan terganggu | MMS-TTS-ind ONNX dengan opsi *pre-cache* audio 26 huruf tunggal sebagai kandidat konfigurasi utama menunggu konfirmasi, lalu cadangan server lokal, ponsel, atau awan (cadangan D) |
| 9 | Aset representasi isyarat mahal | Cakupan arah kedua sempit | Batasi ke glos dan gambar plus ejaan jari |
| 10 | Ketahanan baterai di bawah target | Klaim portabilitas melemah | Ukur arus, sesuaikan target, laporkan apa adanya |
| 11 | Rekrutmen, etika, atau kuota GPU terlambat | Jadwal mundur | Dua ruang dan pengisyarat cadangan; pelatihan terkompresi; minggu transisi |
| 12 | Huruf sangat mirip tak terpisahkan CSI | Himpunan kelas menyempit | Pangkas himpunan pada G1 sesuai Tabel 3.7; laporkan pasangan gagal |
| 13 | Mekanisme akuisisi dua node tidak berjalan seperti dirancang: injeksi NDP masih *stub* (AUD-01), bingkai baku belum memuat MAC pengirim (AUD-03), dan dokumentasi standarnya memakai *mesh* multistatik 3–6 node dengan TDM [33] | G0 tidak dapat dinilai atau CSI tidak stabil | Jalankan *baseline* trafik OFDM *self-ping* dengan tangkapan *promiscuous*; tambahkan penandaan MAC pengirim menurut pola *kit* [34] atau tambahan minimal setara yang diaudit; jika tetap bermasalah, ikuti konfigurasi node pada dokumentasi *firmware* termasuk pengaturan TDM, lalu laporkan sebagai penyimpangan rancangan yang disengaja |
| 14 | Visibilitas label guru bernilai konstan untuk seluruh *keypoint* sehingga tidak mencerminkan oklusi nyata (AUD-12) | Supervisi regresi mengandung derau titik terhalang | Mask visibilitas tidak diwarisi dari label; saringan kualitas deteksi, verifikasi sampel validator, dan laporan tingkat segmen terbuang dijalankan (QA-DS-02, QA-DS-03); perbaikan pipeline anotasi guru didokumentasikan sebelum label dipakai |
## 3.12 Brief Audit Teknis

Subbab ini merangkum audit kesesuaian antara klaim naskah dan implementasi nyata pada enam sumber yang dipakai penelitian. Audit dilakukan pada 15 November 2026 dengan membuka kode sumber, kartu model, artefak eksperimen, dan dokumen rancangan langsung pada komit yang dikunci; hasilnya direkam sebagai register temuan AUD-01 sampai AUD-20 dengan status *PASS*, *CONDITIONAL*, *FAIL*, atau *NOT VERIFIED*. Klaim naskah yang terbukti bertentangan dengan kode dikoreksi pada revisi ini; yang belum terbukti tetap diberi penanda terbuka. Register lengkap beserta kutipan bukti per temuan tersimpan sebagai berkas pendamping Register-Audit-Teknis-v21.md di repositori penelitian agar setiap barisnya dapat diperiksa ulang.

### 3.12.1 Ruang Lingkup dan Artefak yang Diaudit

Tabel 3.9 memuat keenam sumber beserta versi yang diaudit. Penguncian komit dan *hash* bertujuan agar audit dapat direproduksi: pembaca dapat membuka berkas pada komit yang sama dan memperoleh bukti yang sama.

Tabel 3.9 Artefak yang diaudit dan versi yang dikunci

| Sumber | Versi atau identitas yang dikunci | Perubahan terakhir | Metode audit |
|---|---|---|---|
| RuView (ruvnet/RuView) | Komit `3bae24a1231e0d9809e84eb35edba7231b8d1913`; *firmware* `esp32-csi-node` v0.8.18 | 13 Nov 2026 | Baca kode `csi_collector.c`, `rv_radio_ops_esp32.c`, `edge_processing.c`, README *firmware*, panduan pengguna, dokumen ADR-018/029/110, panduan kalibrasi |
| *Checkpoint* `ruvnet/wifi-densepose-pretrained` | *Repo* Hugging Face pada `sha` `98b29a35f962996d6e8207e4f46818dedb5764d5`; `model.safetensors` sha256 `17c9acc1…11a1`; `csi-embed-v2.safetensors` sha256 `183c988b…ed72` | 13 Okt 2026 | Baca kartu model, seluruh berkas metadata, unduh dan urai *header* dua berkas bobot |
| WPC (ILoveTahuTek/WPC) | Komit `249a63dff4a7` pada cabang utama | 2 Nov 2026 | Baca `scripts/convert_sibi_v2.py`, `docs/DATASET_V2.md`, `weights/MANIFEST.json`, ringkasan eksperimen `exp11_huruf24` |
| *wifi-sensing-kit* (andrisgauracs) | Komit `7fb77fc0c0adb98bcf0a102d68fa8718b2f98625`; dasar *firmware* RuView tag v0.8.8-esp32 (`e04f269f`) | 11 Okt 2026 | Kloning dangkal; baca *patch* kit, skrip bangun dan *flash*, pustaka penerima, dokumentasi |
| *DensePose From WiFi* (arXiv) | arXiv:2301.00250v1, 31 Des 2022, DOI 10.48550/arXiv.2301.00250 | Tidak berubah sejak terbit | Baca teks lengkap 13 halaman; verifikasi metadata versi pada halaman abstrak |
| Naskah proposal v20 | Komit repositori skripsi `a0f2d7a` | 14 Nov 2026 | Telusur seluruh klaim mekanisme, angka, dan penanda terbuka terhadap lima sumber di atas |

Dua catatan menyertai tabel ini. Pertama, jalur ringkas naskah (komi `35c1ade`) tetap terdokumentasi terpisah dan tidak memengaruhi jalur utama; pemilik memutuskan untuk mempertahankan v20 sebagai dasar revisi ini. Kedua, seluruh tanggal pada tabel ialah tanggal komit terakhir artefak, bukan tanggal audit; seluruh audit dilakukan serentak pada 15 November 2026.

### 3.12.2 Ringkasan Temuan

Audit menemukan dua temuan berat, satu klaim basi, satu penanda terbuka yang terjawab, dan selebihnya temuan yang memperkuat atau membatasi rancangan. Temuan berat pertama menyangkut mekanisme akuisisi CSI. Fungsi injeksi NDP pada *firmware* RuView masih berstatus *stub* tanpa satu pun pemanggil, sementara sumber CSI yang benar-benar berjalan ialah trafik *self-ping* OFDM yang ditangkap secara *promiscuous* (AUD-01). Narasi naskah karenanya dikoreksi pada Subbab 2.3, 3.4, 3.5, Tabel 2.1, Tabel 3.1, Gambar 3.3, dan kriteria G0. Temuan berat kedua menyangkut kualitas anotasi guru: label visibilitas pada dataset WPC bernilai konstan untuk seluruh *keypoint* sehingga tidak dapat diperlakukan sebagai kebenaran oklusi (AUD-12); kebijakan mask efektif pada Subbab 2.7 dan 2.9 karenanya diperjelas. Tabel 3.10 merangkum keseluruhan register.

Tabel 3.10 Register audit ringkas (bukti lengkap pada berkas pendamping)

| ID | Temuan | Status | Tindakan korektif | Gerbang |
|---|---|---|---|---|
| AUD-01 | Injeksi NDP masih *stub* ADR-029 tanpa pemanggil; bingkai Null Data 24 byte hanya penampung; pengendali TX belum mendarat | FAIL (klaim lama) | Mekanisme *baseline* diganti trafik OFDM *self-ping* + *callback* CSI *promiscuous*; NDP dicatat rancangan masa depan; Tabel 3.7 no. 22 | G0 |
| AUD-02 | Sumber CSI aktual terverifikasi: *self-ping* gateway 10–50 Hz (baku 50), pembatasan laju 50 Hz, mode *promiscuous* MGMT+DATA pada papan tanpa layar | PASS | G0 tetap mengukur laju aktual | G0 |
| AUD-03 | Bingkai ADR-018 baku tidak memuat MAC pengirim; atribusi tautan TX-RX memerlukan penandaan MAC | CONDITIONAL | Patch penandaan MAC pola *kit* [34] atau tambahan minimal setara diaudit di T0; QA-FW-04 | G0 |
| AUD-04 | Format UDP ADR-018 terverifikasi: magic 0xC5110001/0xC5110002, port 5005, sanitasi `first_word_invalid`, LLTF dipaksa aktif | PASS | Parser Rust diuji bolak-balik; QA-ACQ-07 | G0 |
| AUD-05 | ESP-NOW hanya sinkronisasi *mesh* (ADR-110), bukan jalur CSI | PASS | Konsisten Tabel 3.7 no. 21 | G0 |
| AUD-06 | *Mesh* multistatik 3–6 node TDM terdokumentasi sebagai konfigurasi lanjutan yang menunjuk ADR-029/032 (masih usulan); konfigurasi dasar tiap node mengalirkan UDP mandiri | PASS (dokumentasi), NOT VERIFIED (dua node) | Uji konfigurasi dua node pada perangkat nyata di G0 | G0 |
| AUD-07 | Cacat *NUL-padding* `model.safetensors` (isu #1522) telah diperbaiki 13 Okt 2026; verifikasi ulang menunjukkan *header* bersih dan 17 tensor termuat utuh | CONDITIONAL (klaim naskah basi) | Teks 2.4 diperbarui; audit T0 tetap memverifikasi pemuatan langsung | T0 |
| AUD-08 | Dua keluarga berkas *checkpoint* bersaldo metadata berbeda (epoch 20 lawan 60, temperatur 0,07 lawan 0,1, jendela temporal, peringkat LoRA 4 lawan 8, `model.rvf.jsonl` tak terdokumentasi) | CONDITIONAL | Pemilihan keluarga berkas direkonsiliasi eksplisit di T0; Tabel 3.7 no. 6 diperluas | T0, G0b |
| AUD-09 | Catatan SISO 56 *subcarrier* berada pada README utama RuView (isu #509), bukan kartu model | PASS | Kutipan 2.4 dikoreksi ke [10] saja | - |
| AUD-10 | Kontrak *encoder* terverifikasi: 8 fitur @ 1 Hz, *embedding* 128 ternormalisasi L2, 9.280 parameter, triplet-temporal 82,3% (pembanding 66,4% dan 69,6%), EWC lupa 32,97%, lisensi MIT | PASS | Angka dikutip dengan cakupan aslinya | G0b |
| AUD-11 | Varian kuantisasi q2/q4/q8 serta int4 4,56 KB dengan *standardizer* FP16 tersedia; kinerjanya pada tugas SIBI belum teruji | NOT VERIFIED (kinerja tugas) | Uji paritas kuantisasi; QA-EDGE-02 dan QA-EDGE-03 | G1, G3 |
| AUD-12 | `write_label()` WPC menulis visibilitas konstan 2 untuk seluruh 21 *keypoint*; label tidak mencerminkan oklusi nyata | CONDITIONAL | Mask visibilitas tidak diwarisi dari label; diganti saringan kualitas deteksi + verifikasi sampel; Tabel 3.8 no. 14; QA-DS-02 | G0b, G1 |
| AUD-13 | `flip_idx` identitas terverifikasi empiris (n = 16, konsistensi 0,91); koreksi atas permutasi COCO-WholeHand v1 yang salah untuk urutan MediaPipe | PASS | Urutan 21 *keypoint* MediaPipe dikunci sebagai konvensi | G1 |
| AUD-14 | Dataset v2 terverifikasi: 9.953 ditemukan, dedup md5 −2.215, *leak-guard* dHash −18, MediaPipe 7.210 sukses dan 510 gagal, 7.627 objek, split terkunci 6.231/650/329, split resmi Roboflow dipakai apa adanya, Kaggle hanya latih, Roboflow CC BY 4.0 | PASS | Angka 2.9 konsisten | G1 |
| AUD-15 | `exp11_huruf24` dipetakan ulang saat pelatihan ke 24 kelas huruf A sampai Y tanpa J dan Z; validasi 333 instance huruf; mAP50 0,9580, mAP50-95 0,7235; conf 0,25 membaca 325/333 (97,6%) dengan 5 pertukaran dan 3 deteksi hilang | PASS (menjawab penanda terbuka) | Penanda [PERLU VALIDASI kelas J/Z] diselesaikan; supervisi J/Z tetap dari lintasan dan protokol | G1 |
| AUD-16 | Bobot `exp11` belum diarsipkan di repositori WPC; MANIFEST hanya memuat exp00 sampai exp10 dan exp06b (sha256 `073ccf71…3ea0`) | NOT VERIFIED (artefak) | Pemilik diminta menerbitkan tag rilis dan *hash* bobot exp11 sebelum angka guru diaudit pihak lain | - |
| AUD-17 | Pelatihan guru deterministik (seed 42) dengan buku besar eksperimen lengkap dan resep diulang pada exp11 | PASS | Keterulangan pra-penelitian terdukung | G1 |
| AUD-18 | *wifi-sensing-kit* ialah kit orkestrasi di atas *firmware* RuView v0.8.8 dengan patch MAC; tanpa NDP (stub sama), tanpa peran TX/RX tetap, laju sekitar 50 Hz dibagi antar tautan, hanya ESP32-S3, lisensi MIT | PASS (sebagai pola) | Dipakai sebagai pola atribusi AUD-03 dan opsi jalur pembanding pasif, bukan komponen inti | G0 |
| AUD-19 | *DensePose From WiFi* berstatus pracetak tanpa telaah sejawat; setup 3 antena TX × 3 RX, 30 *subcarrier*, 100 Hz, keluaran IUV 24 wilayah tubuh + 17 *keypoint* tubuh, tanpa konten tangan; terdapat inkonsistensi internal tabel | CONDITIONAL | Dikutip sebagai latar penamaan lini riset dengan label pracetak [35], bukan dasar teknis *encoder* | - |
| AUD-20 | Model pose MM-Fi [15] terpisah: 17 *keypoint* tubuh, PCK@20 82,69%, lisensi CC BY-NC 4.0, lintas subjek *zero-shot* sekitar 64% | PASS | Pemisahan tiga model pada Tabel 2.2 konsisten | G0b |

### 3.12.3 Bukti dan Penelusuran

Setiap temuan dapat ditelusuri ke berkas dan baris kode pada komit yang dikunci pada Tabel 3.9. Untuk AUD-01, fungsi `csi_inject_ndp_frame()` pada `firmware/esp32-csi-node/main/csi_collector.c` baris 940 sampai 982 memuat komentar ADR-029 yang menyebut bingkai Null Data itu hanya penampung. Penelusuran seluruh pohon kode tidak menemukan satu pun pemanggil fungsi tersebut. Berkas `rv_radio_ops_esp32.c` baris 84 sampai 88 menyatakan perilaku TX baru berjalan setelah *controller PR* pengendali mendarat. Untuk AUD-12, fungsi `write_label()` pada `scripts/convert_sibi_v2.py` baris 286 sampai 297 menuliskan angka visibilitas tetap untuk setiap *keypoint* tanpa memeriksa keadaan oklusi. Untuk AUD-15, dokumen evaluasi `exp11_huruf24` menyatakan label dipetakan ulang ke 24 kelas huruf A sampai Y tanpa J dan Z pada saat pelatihan. Kutipan lengkap ketiganya beserta bukti temuan lain tersimpan pada berkas pendamping register; seluruh tautan sumber juga dicatat di sana.

### 3.12.4 Dampak terhadap Rancangan

Koreksi pada revisi ini bersifat naratif dan kebijakan, bukan perubahan arah penelitian. Mekanisme akuisisi CSI dinyatakan ulang sesuai bukti kode agar klaim naskah tidak melampaui implementasi yang tersedia. Kebijakan mask visibilitas diketatkan supaya supervisi regresi tidak mewarisi label yang tidak informatif. Klaim *NUL-padding* yang telah usang diperbarui, dan satu penanda terbuka tentang kelas J/Z terjawab dengan fakta audit. Ruang lingkup penelitian tidak berubah: objek tetap 26 huruf SIBI satu tangan, guru tetap YOLO26m-Pose dengan supervisi lintasan untuk J dan Z, gerbang tetap G0 sampai G4 dengan sub-gerbang G0b, dan deployment tetap mengikuti Pilihan 1 pada Tabel 3.7. Tidak ada hasil pengujian yang dikarang; seluruh uji pada Subbab 3.13 berstatus belum diuji sampai penelitian berjalan.

### 3.12.5 Tindakan Korektif dan Keputusan yang Ditimbulkan

Tiga keputusan lahir dari audit ini dan dicatat pada Tabel 3.7. Pertama, mekanisme akuisisi baseline ditetapkan pada baris 22: trafik OFDM terjadwal dengan *callback* CSI *promiscuous*, tanpa injeksi NDP, dengan atribusi bingkai lewat penandaan MAC pengirim. Kedua, pemilihan keluarga berkas *checkpoint* beserta rekonsiliasi metadata kartu model ditambahkan ke lingkup audit T0 pada baris 6. Ketiga, permintaan penerbitan bobot dan *hash* `exp11` (AUD-16) menjadi prasyarat agar angka pra-penelitian guru dapat diaudit pihak lain; sampai artefak itu tersedia, penanda [PERLU DATA] pada rujukan [12] tetap berlaku. Seluruh keputusan lain yang menunggu pembimbing atau data eksperimen tetap tidak diputuskan sepihak.

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
