# LEMBAR FAKTA BERSAMA — Proposal DPJ-4 (SIBI-only)

Dokumen ini adalah SATU-SATUNYA sumber fakta untuk BAB I, II, dan III. Semua angka, nama alat, nama metode, dan klaim harus berasal dari sini. Fakta yang tidak ada di sini ditulis sebagai `[PERLU DATA: …]` atau `[PERLU RUJUKAN: …]`.

## A. Keputusan yang sudah dikunci pemilik

- Cakupan **SIBI saja** (BISINDO hanya disebut sebagai konteks dan kerja lanjutan).
- Framing: **alat pembelajaran/latihan isyarat SIBI tanpa kamera bagi pembelajar pendengar**. Latar belakang berangkat dari masalah sosial/pendidikan, BUKAN dari teknologi. Teknologi hanya alat.
- Format **sempro standar, 3 BAB**: tanpa tabel usulan judul, tanpa rencana biaya, tanpa tabel risiko. BAB III berisi metodologi + jadwal.
- Sitasi **IEEE numerik**. Agen menulis kunci `[@kunci]` (lihat §F). Penomoran [1], [2], … dikerjakan belakangan oleh koordinator. Contoh: `… dari sinyal Wi-Fi [@signfi2018].` atau `Ma dkk. [@signfi2018] mengusulkan …`. Beberapa sumber: `[@ma2019survey], [@chen2023]`.
- Perspektif **impersonal** ("Penelitian ini …"), tidak memakai "penulis/peneliti/saya".
- Bahasa Indonesia baku (EYD V, KBBI).

## B. Judul

**ALAT PEMBELAJARAN ISYARAT SIBI TANPA KAMERA BERBASIS WI-FI CHANNEL STATE INFORMATION PADA ESP32: STUDI KELAYAKAN UMPAN BALIK LATIHAN BAGI PEMBELAJAR PENDENGAR**

## C. Fakta lapangan (boleh dikutip, sumber tertera)

| ID | Fakta | Kunci |
|---|---|---|
| F1 | Lebih dari 430 juta orang (±5% populasi dunia) memerlukan rehabilitasi pendengaran; diproyeksikan ±700 juta pada 2050 (laporan dunia WHO tentang pendengaran, 2021) | `[@chadha2021]` |
| F2 | Mayoritas besar anak tuli/kurang dengar lahir dari orang tua pendengar (data AS; mitos "10% orang tua tuli" dibantah); kisaran yang lazim dikutip 90–95% | `[@mitchell2004]`, `[@mitchell2005]` |
| F3 | Orang tua pendengar yang belajar bahasa isyarat bersama anak tunarungunya membutuhkan akses kurikulum dan dukungan belajar terstruktur (survei metode campuran, ASL) | `[@lieberman2022]` |
| F4 | Orang tua pendengar menghadapi hambatan praktis dalam menavigasi pembelajaran bahasa isyarat | `[@ritmeester2025]` |
| F5 | Indonesia memiliki ±500 juru bahasa isyarat (JBI) untuk ±1,92 juta penyandang tuli (rasio ±1 : 3.840) | `[@kemenkopmk2025]` |
| F6 | Survei ekosistem bahasa isyarat (daring, *purposive*, 26 provinsi, BUKAN sampel nasional): BISINDO 77,7%; SIBI 1,9%; campuran 14,9%; lainnya 5,6%. SIBI berkembang di pendidikan formal | `[@brin2026]` |
| F7 | UU No. 8/2016 tentang Penyandang Disabilitas mengakui bahasa isyarat dan mewajibkan aksesibilitas komunikasi | `[@uu8_2016]` |
| F8 | Riset pengenalan bahasa isyarat Indonesia yang ditinjau berbasis pengolahan citra/*deep learning* (kamera). PERHATIAN: tinjauan Sanjaya dkk. berjudul "… Deep Learning Techniques for Image Processing" — JANGAN mengklaim tinjauan itu "mencatat belum adanya pendekatan nirkabel". Klaim celah nirkabel ditulis sebagai hasil penelusuran literatur penelitian ini sendiri (diberi kata "belum ditemukan"). | `[@sanjaya2023]` |
| F9 | Tinjauan sistematis manfaat dan perkembangan teknologi bantu komunikasi bagi tunarungu | `[@rodriguez2023]` |

**Cara jujur memakai F6:** angka 1,9% dibuka sendiri di BAB I. Pembelaan: komunitas tunarungu sehari-hari memakai BISINDO, sedangkan SIBI adalah sistem yang diajarkan di pendidikan formal; alat ini menyasar pembelajar pendengar yang masuk lewat jalur formal (keluarga siswa, calon guru, mahasiswa). Rancangan sistem bersifat bahasa-agnostik sehingga perluasan ke BISINDO cukup mengganti *dataset* dan validasi penutur. Sebutkan juga keterbatasan survei (purposive, bukan nasional).

**Justifikasi bebas kamera (non-teknis, sebagai HIPOTESIS yang diuji, bukan klaim):** latihan yang tidak terasa diawasi diduga lebih mudah dijadikan kebiasaan harian; kamera juga menuntut pencahayaan dan sudut tertentu. Hipotesis ini diuji melalui kuesioner persepsi (lihat §E.8).

## D. Fakta teknis

- **Wi-Fi CSI**: informasi amplitudo dan fase per *subcarrier* yang berubah ketika gerak tubuh mengganggu jalur propagasi. Gerak lengan menghasilkan komponen Doppler yang dapat diukur.
- **Batas fisika**: panjang gelombang Wi-Fi 2,4/5 GHz ±6–12 cm; dengan dua node ESP32, konfigurasi jari dan ekspresi wajah TIDAK dapat dibedakan. Cakupan pengenalan: **lintasan lengan, tubuh atas, dan kepala**.
- **ESP32**: mikrokontroler murah dengan radio Wi-Fi yang dapat mengekspor CSI; basis akuisisi CSI pada ESP32 dikembangkan oleh Hernandez dan Bulut `[@hernandez2020]`. Varian papan: `[PERLU DATA: varian ESP32 yang dipakai, misalnya ESP32 DevKit atau ESP32-S3]`.
- **Laju sampling CSI**: `[PERLU DATA: laju sampling CSI node ESP32 pada konfigurasi RuView]`; agar pita Doppler gerak 1–60 Hz terwakili, laju sampling minimal ±120 Hz (kriteria Nyquist).
- **Platform RuView** `[@ruview]` (proyek sumber terbuka, github.com/ruvnet/RuView): firmware ESP32 penangkap CSI (format frame ADR-018, streaming UDP), server pengolahan sinyal, kalibrasi ruang bawaan (600 *frame* + 8 *anchor*, ±4 menit), segmentasi berbasis energi gerak, *dashboard* web, mode privasi yang membuang fitur biometrik, dan *pipeline* akuisisi tersinkron kamera–CSI `scripts/collect-ground-truth.py` (ADR-079) yang memakai MediaPipe PoseLandmarker. Modul estimasi pose *on-device* RuView TIDAK dipakai. Jangan menulis angka PCK apa pun.
- **MediaPipe** `[@mediapipe2019]`: kerangka kerja *pipeline* persepsi; BlazePose `[@blazepose2020]` menghasilkan 33 *landmark* tubuh; MediaPipe Hands `[@mphands2020]` menghasilkan 21 *landmark* per tangan; contoh penerapan jurnal `[@kim2023]`.
- **Transfer visi→Wi-Fi (preseden konsep "guru visi, murid CSI")**: Person-in-WiFi `[@personinwifi2019]` (persepsi tubuh dari Wi-Fi dengan supervisi kamera); DensePose From WiFi `[@densepose2023]` (memetakan sinyal Wi-Fi ke koordinat permukaan tubuh tingkat region, dilatih dengan guru visi). Keduanya bekerja pada tingkat tubuh, bukan jari.
- **PERAN KAMERA YANG JUJUR**: label kelas isyarat diketahui dari protokol elisitasi (kartu pemandu ditampilkan sebelum tiap repetisi). MediaPipe TIDAK "mencetak label kelas"; MediaPipe memberi deret *keypoint* yang dipakai untuk (1) memverifikasi batas awal–akhir segmen isyarat, (2) menyaring segmen buruk (orang tidak terdeteksi, *jitter*), dan (3) diagnosis kesalahan klasifikator (apakah salah karena lintasan mirip atau sinyal lemah). Distilasi pose penuh CSI→pose→kelas adalah kerja lanjutan, bukan janji.
- **Fitur**: amplitudo dan fase *subcarrier* terpilih, spektrum Doppler pita 1–60 Hz, statistik ringkas (energi, entropi, lintasan puncak) `[@ma2019survey]`, `[@widar2021]`, `[@sruthi2024]`, `[@cai2024]`.
- **Klasifikator**: *Support Vector Machine* (SVM) sebagai *baseline* dan *1D Convolutional Neural Network* (1D-CNN) kecil. Rujukan teori SVM/CNN tidak tersedia → `[PERLU RUJUKAN: …]`.
- **Umpan balik**: keluaran klasifikator + skor keyakinan. Skor di bawah ambang → "isyarat tidak dikenali, ulangi" (penolakan). Skor di atas ambang → ditampilkan isyarat yang terdeteksi dan kecocokannya dengan isyarat target. "Benar" berarti **lintasan gerak lengan/tubuh atas sesuai**, BUKAN bentuk jari benar — ditulis eksplisit sebagai keterbatasan. Umpan balik ditampilkan di *dashboard* pada laptop. Nilai ambang `[PERLU DATA: ambang skor keyakinan, ditetapkan dari data validasi]`.
- **Generalisasi**: CSI mudah *overfit* pada orang dan ruang `[@chen2023]`; strategi lintas domain Widar3.0 `[@widar2021]` dipakai sebagai sumber strategi, bukan janji hasil.

## E. Desain penelitian (BAB III mengikuti ini; BAB I memakai rumusan/tujuan/batasan persis)

### E.1 Rumusan masalah (dipakai persis di BAB I; BAB III merujuk)

1. Bagaimana merancang sistem akuisisi Wi-Fi CSI dua node ESP32 berbasis platform RuView beserta protokol perekaman *dataset* isyarat SIBI terisolasi yang kosakatanya divalidasi penutur tunarungu?
2. Bagaimana kinerja klasifikasi 5–8 isyarat SIBI terisolasi dari fitur amplitudo, fase, dan Doppler CSI pada skenario dalam sesi, lintas partisipan, dan lintas ruang?
3. Bagaimana kelayakan sistem sebagai sarana latihan SIBI tanpa kamera bagi pembelajar pendengar ditinjau dari umpan balik latihan, latensi, persepsi kenyamanan pengguna, dan penilaian validator tunarungu?

### E.2 Tujuan (cermin 1:1)

1. Merancang sistem akuisisi Wi-Fi CSI dua node ESP32 berbasis platform RuView beserta protokol perekaman *dataset* isyarat SIBI terisolasi yang kosakatanya divalidasi penutur tunarungu.
2. Mengukur kinerja klasifikasi 5–8 isyarat SIBI terisolasi dari fitur amplitudo, fase, dan Doppler CSI pada skenario dalam sesi, lintas partisipan, dan lintas ruang.
3. Menguji kelayakan sistem sebagai sarana latihan SIBI tanpa kamera bagi pembelajar pendengar berdasarkan umpan balik latihan, latensi, persepsi kenyamanan pengguna, dan penilaian validator tunarungu.

(Agen BAB I boleh merapikan diksi asalkan objek, jumlah, dan urutan tetap sama; laporkan perubahan.)

### E.3 Batasan masalah

1. Objek: 5–8 isyarat SIBI terisolasi, dipilih melalui dua saringan: (a) separabilitas fisik — dibedakan oleh lintasan lengan, tubuh atas, atau kepala, bukan bentuk jari; (b) validitas pedagogis — disetujui validator penutur tunarungu dan dicocokkan dengan Kamus SIBI `[@kamussibi]`. Bukan penerjemah kalimat dan bukan pengenalan isyarat kontinu.
2. Konfigurasi jari dan ekspresi wajah tidak dikenali; umpan balik "benar" berarti lintasan gerak sesuai.
3. Satu pengisyarat per sesi di zona akuisisi; sistem tidak mengidentifikasi individu.
4. Perangkat: dua node ESP32 (pemancar dan penerima) + laptop; kamera hanya menyala saat perekaman *dataset* dan pada satu kondisi uji persepsi; mode latihan berjalan tanpa kamera.
5. Pengujian dilakukan di sedikitnya dua ruang mitra yang dikalibrasi oleh peneliti; penyiapan mandiri oleh pengguna di rumah berada di luar cakupan.
6. Uji pengguna berskala kecil (3–5 pembelajar pemula) dan dianalisis secara deskriptif; empati tidak diukur secara psikometrik.

### E.4 Tahapan (enam tahap, minggu M1–M14)

| Tahap | Minggu | Isi | Gerbang |
|---|---|---|---|
| T0 Replikasi | M1–M2 | Menyiapkan 2 ESP32 + firmware RuView, menjalankan *pipeline* akuisisi tersinkron ADR-079, uji Delta-CSI (ruang kosong vs pengisyarat diam vs pengisyarat bergerak) | **G0** akhir M2: akuisisi tersinkron stabil dan pola CSI saat bergerak terpisah jelas dari kondisi diam/kosong. Gagal → perbaiki penempatan node satu kali; gagal lagi → jalur CSI dihentikan, dilaporkan sebagai temuan karakterisasi |
| T1 Kurasi & protokol | M2–M4 | Kurasi 5–8 isyarat (dua saringan, bersama validator), kalibrasi ruang mitra, protokol perekaman & etika, perizinan | **G1** M3: separabilitas awal 2–3 isyarat — repetisi isyarat yang sama lebih dekat satu sama lain daripada ke isyarat lain (uji *nearest-centroid* sederhana). Gagal → ubah penempatan/orientasi node satu kali |
| T2 Perekaman & klasifikasi | M4–M8 | Perekaman *dataset* (±30 repetisi/isyarat/sesi, kamera tersinkron), penyaringan segmen, ekstraksi fitur, pelatihan SVM + 1D-CNN | **G2** M6–M7: akurasi dalam partisipan pada *split* temporal berada jauh di atas peluang acak (1/jumlah kelas); ambang numerik `[PERLU DATA: ambang G2 yang disepakati bersama pembimbing sebelum eksperimen]`. Gagal → pangkas ke 3–5 isyarat yang paling dominan lintasan |
| T3 Generalisasi | M8–M10 | Uji lintas sesi, lintas partisipan (*leave-one-subject-out*), lintas ruang (*leave-one-room-out*), satu pengguna baru tanpa pelatihan ulang | **G3** M10: kinerja lintas partisipan/ruang di atas peluang acak; ambang `[PERLU DATA: ambang G3 dari pembimbing]`. Runtuh → cakupan menjadi personalisasi per pengguna, ditulis sebagai temuan |
| T4 Kemasan & uji kegunaan | M10–M12 | Mode latihan umpan balik di *dashboard*, uji 3–5 pemula, kuesioner persepsi, penilaian validator | **G4** M12: tiga syarat — skor pre/post tercatat, persepsi tercatat, validator menyetujui kewajaran umpan balik. Hasil negatif tetap dilaporkan sebagai temuan kelayakan |
| T5 Penulisan | M12–M14 | Analisis, keterbatasan, rekomendasi | — |

Prinsip: ini studi kelayakan; setiap tahap menghasilkan artefak tetap (laporan karakterisasi sinyal, protokol, *dataset* berlabel, model, laporan kelayakan) sehingga penelitian tetap bernilai walau berhenti di salah satu gerbang. JANGAN menulis target akurasi sebagai janji.

### E.5 Alat dan bahan

Perangkat keras: ESP32 2 unit (+1 cadangan) `[PERLU DATA: varian]`; aksesori (kabel, adaptor daya, dudukan setinggi dada pengisyarat); laptop pribadi sebagai server RuView, mesin pelatihan, dan tampilan umpan balik `[PERLU DATA: spesifikasi laptop]`; *webcam* bawaan laptop (hanya saat pelabelan dan satu kondisi uji persepsi).
Perangkat lunak: firmware dan server RuView; `scripts/collect-ground-truth.py` (ADR-079); MediaPipe (Pose/Holistic, Hands); Python; scikit-learn; PyTorch; *dashboard* RuView.
Bahan: *dataset* CSI isyarat SIBI hasil perekaman sendiri; lembar definisi isyarat; formulir persetujuan; instrumen pre/post dan kuesioner persepsi.

### E.6 Arsitektur dua jalur (untuk diagram BAB III)

- **Jalur operasional (bebas kamera):** ESP32 TX — zona isyarat — ESP32 RX → deret CSI (amplitudo, fase, Doppler 1–60 Hz) → segmentasi berbasis energi gerak → ekstraksi fitur → klasifikator 5–8 kelas (SVM, 1D-CNN) + skor keyakinan → umpan balik di *dashboard* (isyarat terdeteksi, cocok/tidak cocok, atau "tidak dikenali").
- **Jalur pelabelan (hanya saat perekaman dataset):** kartu pemandu → label kelas; *webcam* → MediaPipe → deret *keypoint* → verifikasi batas segmen, penyaringan kualitas, diagnosis. Sinkronisasi waktu kamera–CSI melalui `collect-ground-truth.py` (ADR-079).

### E.7 Protokol perekaman, partisipan, etika

- Setiap sesi: kalibrasi ruang (600 *frame* + 8 *anchor*), pencatatan kondisi latar (posisi perabot, kipas/AC, orang lewat) sebagai kovariat.
- Elisitasi terisolasi: kartu pemandu ditampilkan, satu isyarat per segmen, jeda antar-repetisi, ±30 repetisi per isyarat per sesi.
- Metadata: tanggal, ruang, kode pengisyarat, posisi node, kondisi latar.
- Aturan buang-segmen: orang tidak terdeteksi MediaPipe, *jitter* *keypoint* ekstrem, segmen terpotong. Tingkat segmen terbuang dicatat.
- Validator mengambil sampel segmen untuk memeriksa kebenaran bentuk isyarat.
- Lokasi: `[PERLU DATA: nama sekolah/lembaga mitra]`, sedikitnya dua ruang.
- Partisipan: 3–4 pengisyarat kompeten (guru/pembina SIBI, dapat penutur tunarungu) untuk *dataset*; minimal 1 validator penutur tunarungu (wajib); 3–5 pembelajar pendengar pemula untuk uji kegunaan.
- Etika: persetujuan institusi, persetujuan tertulis subjek, hak mundur tanpa konsekuensi, kamera hanya pada sesi pelabelan dan satu kondisi uji persepsi (dinyatakan tertulis), mode privasi RuView aktif. Video hanya dipakai untuk pelabelan, disimpan terbatas, tidak dipublikasikan; *dataset* publik hanya memuat CSI, label, dan *keypoint* tanpa identitas. Token apresiasi validator `[PERLU DATA: dikonfirmasi pembimbing]`.

### E.8 Pengujian dan metrik

1. Uji Delta-CSI (G0).
2. Uji klasifikasi: akurasi, presisi/*recall*/F1 makro, *confusion matrix* per isyarat pada skenario (i) dalam sesi dengan *split* temporal per blok (BUKAN acak, untuk mencegah kebocoran antar-repetisi berurutan), (ii) lintas sesi, (iii) lintas partisipan, (iv) *leave-one-room-out*, (v) satu pengguna baru. Selalu dilaporkan bersama peluang acak (1/jumlah kelas) dan tingkat penolakan.
3. Uji operasional: laju deteksi palsu per jam saat tidak ada isyarat (orang lewat, kipas, perabot bergeser); latensi ujung-ke-ujung dari selesainya isyarat hingga umpan balik tampil.
4. Uji kegunaan (3–5 pemula): sebelum dan sesudah sesi latihan, peserta memperagakan isyarat target; ketepatan dinilai validator dengan rubrik (independen dari sistem CSI). Kuesioner persepsi skala Likert (±5 butir: kenyamanan, rasa diawasi, kemauan berlatih lagi) diberikan setelah peserta berlatih pada dua kondisi — kamera menyala dan kamera mati — dengan urutan diacak (*within-subject*). Analisis deskriptif; tidak ada klaim kausal atau statistik inferensial.
5. Penilaian validator atas kewajaran umpan balik.
6. Diagnosis (sekunder): mengaitkan kesalahan klasifikator dengan kemiripan lintasan tubuh dari *keypoint* MediaPipe.

## F. Kunci rujukan (HANYA kunci ini yang boleh dipakai)

Konten sumber sudah diverifikasi metadata-nya (DOI). Klaim tentang isi sumber harus sesuai deskripsi singkat di bawah; JANGAN menambah angka hasil (akurasi, dll.) dari ingatan.

| Kunci | Ringkas isi | Tahun |
|---|---|---|
| rodriguez2023 | Tinjauan sistematis manfaat & perkembangan teknologi bantu komunikasi tunarungu | 2023 |
| sanjaya2023 | Tinjauan sistematis pengenalan BISINDO dengan teknik *deep learning* untuk pengolahan citra | 2023 |
| dwijayanti2021 | Pengenalan bahasa isyarat Indonesia dengan CNN (citra) | 2021 |
| kindy2025 | *Dataset* video BISINDO tingkat kata + metode *baseline* | 2025 |
| wiguna2025 | Pengenalan kalimat BISINDO dengan 3D CNN-LSTM dan 3D CNN-BiLSTM (video) | 2025 |
| sebastian2025 | Pengenalan BISINDO dengan pengenalan gestur tubuh sadar-spasial (visi) | 2025 |
| ma2019survey | Survei *sensing* Wi-Fi berbasis CSI (dasar fisika, taksonomi, tantangan) | 2019 |
| chen2023 | Survei *sensing* Wi-Fi CSI lintas domain (strategi generalisasi) | 2023 |
| hernandez2020 | *Sensing* Wi-Fi mandiri ringan berbasis IoT (ESP32) — basis alat akuisisi CSI ESP32 | 2020 |
| signfi2018 | SignFi: pengenalan 276 isyarat ASL dari CSI Wi-Fi | 2018 |
| shang2017 | Sistem pengenalan bahasa isyarat tangguh dengan beberapa perangkat Wi-Fi | 2017 |
| ahmed2020 | DF-WiSLR: pengenalan bahasa isyarat berbasis Wi-Fi bebas perangkat | 2020 |
| ahmed2021 | Pengenalan bahasa isyarat dari CSI Wi-Fi dengan jaringan LSTM | 2021 |
| baldeo2024 | Pengenalan Filipino Sign Language dari CSI Wi-Fi | 2024 |
| widar2021 | Widar3.0: pengenalan gestur lintas domain tanpa pelatihan ulang, berbasis profil kecepatan dari Doppler | 2022 (terbit cetak) |
| hao2020 | Wi-SL: pengenalan gestur (isyarat) halus tanpa kontak dari CSI | 2020 |
| sruthi2024 | HandFi: pengenalan gestur tangan dari CSI | 2024 |
| cai2024 | Pengenalan gestur dengan informasi amplitudo dan fase CSI yang saling melengkapi | 2024 |
| qin2023 | WiASL: pengenalan tulisan ASL dengan perangkat Wi-Fi komersial | 2023 |
| personinwifi2019 | Person-in-WiFi: persepsi tubuh halus dari Wi-Fi dengan supervisi kamera | 2019 |
| densepose2023 | DensePose From WiFi: transfer jaringan visi ke Wi-Fi untuk pose padat tingkat region tubuh | 2023 |
| mediapipe2019 | MediaPipe: kerangka kerja *pipeline* persepsi | 2019 |
| blazepose2020 | BlazePose: pelacakan pose tubuh *real-time* di perangkat (33 *landmark*) | 2020 |
| mphands2020 | MediaPipe Hands: pelacakan tangan *real-time* (21 *landmark*) | 2020 |
| kim2023 | Estimasi pose manusia dengan MediaPipe Pose dan optimasi model humanoid | 2023 |
| chadha2021 | Laporan dunia WHO tentang pendengaran 2021 | 2021 |
| mitchell2004 | Status pendengaran orang tua siswa tuli di AS (membantah mitos 10%) | 2004 |
| mitchell2005 | Status pendengaran orang tua dan penggunaan isyarat siswa tuli | 2005 |
| lieberman2022 | Orang tua pendengar belajar ASL bersama anak tuli (survei metode campuran) | 2022 |
| ritmeester2025 | Pengalaman orang tua pendengar menavigasi pembelajaran bahasa isyarat | 2025 |
| ruview | Repositori RuView (GitHub) | — |
| brin2026 | Berita BRIN: survei ekosistem bahasa isyarat (F6) | 2026 |
| kemenkopmk2025 | Rilis Kemenko PMK tentang jumlah JBI (F5) | 2025 |
| uu8_2016 | UU No. 8 Tahun 2016 tentang Penyandang Disabilitas | 2016 |
| kamussibi | Kamus Sistem Isyarat Bahasa Indonesia (resmi) | — |

## G. Daftar istilah (pakai persis, konsisten)

| Konsep | Bentuk yang dipakai |
|---|---|
| Wi-Fi CSI | pertama: Wi-Fi *Channel State Information* (CSI); selanjutnya: CSI |
| SIBI | pertama: Sistem Isyarat Bahasa Indonesia (SIBI) |
| BISINDO | pertama: Bahasa Isyarat Indonesia (BISINDO) |
| orang tuli | tunarungu (konsisten); "komunitas tunarungu" |
| *signer* | pengisyarat (BUKAN "penandatangan") |
| *hearing learner* | pembelajar pendengar |
| validator | validator penutur tunarungu |
| *isolated sign* | isyarat terisolasi |
| *feedback* | umpan balik |
| *dataset* | *dataset* (miring) |
| *subcarrier* | *subcarrier* (miring) |
| *pose estimation* | estimasi pose |
| *keypoint/landmark* | *keypoint* (miring); *landmark* hanya saat menyebut keluaran MediaPipe |
| *ground truth* | label acuan |
| *classifier* | klasifikator |
| SVM | pertama: *Support Vector Machine* (SVM) |
| 1D-CNN | pertama: *one-dimensional Convolutional Neural Network* (1D-CNN) |
| *go/no-go gate* | gerbang keputusan |
| TX/RX | node pemancar (TX) / node penerima (RX) |
| *dashboard* | *dashboard* (miring) |
| *open source* | sumber terbuka |
| *leave-one-room-out* | *leave-one-room-out* (miring, dijelaskan sekali) |
| *leave-one-subject-out* | *leave-one-subject-out* (miring, dijelaskan sekali) |
| *split* temporal | pembagian data temporal |
