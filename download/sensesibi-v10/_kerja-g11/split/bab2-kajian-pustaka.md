# BAB II KAJIAN PUSTAKA

## 2.1 Bahasa Isyarat, SIBI, dan Kebutuhan Komunikasi Dua Arah

Bahasa isyarat menyampaikan makna lewat gerak tangan, lengan, tubuh, dan ekspresi wajah. Sebuah isyarat tersusun atas bentuk tangan, lokasi, gerak, dan orientasi telapak; perbedaan satu bentuk jari saja dapat mengubah maknanya. Susunan itu menjadi acuan penelitian ini dalam memisahkan bagian isyarat yang dapat dinilai mesin dari bagian yang memerlukan penilaian manusia [3]. SIBI adalah sistem isyarat baku untuk pendidikan formal yang bentuknya didokumentasikan dalam kamus pemerintah [3], sedangkan BISINDO tumbuh secara alami di komunitas tunarungu [7]. Keduanya tidak bersaing untuk menggantikan satu sama lain; masing-masing hidup di ranah berbeda [8], [5]. Survei pada 100 responden tunarungu di Jawa dan Bali menemukan 91% lebih banyak memakai BISINDO, sementara pemakaian SIBI menempel pada konteks sekolah [8]. Penelitian ini memilih SIBI karena sasarannya adalah alat bantu pembelajaran di sekolah, bukan karena jumlah penuturnya lebih banyak.

Komunikasi antara pengguna isyarat dan orang pendengar menuntut dua arah. Keluarga dan guru berada di barisan pertama yang merasakan kesenjangan itu, sedangkan juru bahasa masih jauh dari cukup [1]. Karena itu, alat bantu yang dibangun harus dua arah, bukan kamus satu arah. Sistem terdahulu di Indonesia hanya menutup satu arah. KASIBI mengubah ucapan menjadi teks, lalu menampilkan animasi tangan tiga dimensi, dan memperoleh rata-rata skor 3,362 dari 4 dalam penilaiannya [9]. OpenSIBI menganimasikan model tiga dimensi untuk 50 kosakata, yaitu 9 angka, 26 huruf, dan 15 kata [10]. Pada arah isyarat menjadi teks, riset dalam negeri bertumpu pada kamera: CNN untuk huruf BISINDO [11], tinjauan sistematis pengenalan BISINDO berbasis citra [23], aplikasi MediaPipe untuk 24 huruf statis SIBI [12], aplikasi Android berbasis *deep learning* [13], dan *dataset* video BISINDO tingkat kata [24]. Kamera menuntut pencahayaan dan garis pandang yang baik, sedangkan kamera yang terus menyala membuat pengguna merasa diawasi. Dua kendala itulah yang mendorong penelitian ini mencari penginderaan tanpa kamera dan tanpa perangkat yang dikenakan.

## 2.2 Wi-Fi Channel State Information

*Channel State Information* (CSI) adalah informasi amplitudo dan fase pada setiap *subcarrier* sinyal Wi-Fi yang menggambarkan kondisi jalur propagasi [14]. Ketika tubuh bergerak di antara pemancar dan penerima, panjang jalur pantulan berubah, dan amplitudo serta fase tiap *subcarrier* ikut berubah. Perubahan itulah yang dipakai untuk mengenali gerak tanpa sensor yang dikenakan. Tiap *subcarrier* menempati frekuensi berbeda sehingga satu pasang perangkat sudah menyediakan banyak kanal pengamatan sekaligus [14].

Dasar pemodelannya adalah zona Fresnel [25]. Artikulasi jari menggeser jalur pantulan pada orde sentimeter hingga milimeter, dan setiap bentuk huruf meninggalkan pola perubahan *subcarrier* yang khas. Fase mentah tercemar derau osilator lokal; teknik CSI-ratio membersihkannya lewat rasio atau perkalian konjugat tanpa perangkat tambahan [25], dan Widar2.0 menerapkan teknik serupa untuk pelacakan manusia [26]. Penelitian ini menerapkan prinsip yang sama pada modul penerima sebagai rasio terhadap rekam acuan kalibrasi ruang (Subbab 3.7). Gerak tubuh juga menghasilkan komponen Doppler [14]; pita analisis 1–60 Hz menuntut laju pencuplikan sekurang-kurangnya 120 Hz mengikuti kaidah Nyquist, sedangkan *firmware* RuView membatasi laju paling sering 50 bingkai per detik [20]. Bila laju terukur lebih rendah, pita yang dianalisis menyempit dan hal itu dilaporkan apa adanya.

CSI terbukti peka terhadap gerak halus, dari ketukan tombol hingga gerakan jari [14]. Namun, bukti-bukti itu diperoleh pada kondisi terkendali sehingga bagi penelitian ini statusnya hanya hipotesis kerja. Model CSI juga mudah *overfitting* terhadap orang dan ruang; Widar3.0 menjawabnya dengan profil kecepatan Doppler untuk pengenalan lintas domain [27]. Panjang gelombang 2,4 GHz sekitar 12,5 cm juga membatasi resolusi spasial, dan sebagian besar preseden memakai perangkat berantena banyak. Kelayakan satu tautan dua modul berantena tunggal membedakan 26 bentuk tangan SIBI karena itu diperlakukan sebagai pertanyaan penelitian, bukan asumsi. Uji Delta-CSI dan gerbang G1 mengujinya, dan bila beberapa huruf tidak terpisahkan, himpunan huruf dipangkas (Tabel 3.7).

## 2.3 Modul ESP32-S3, Platform RuView, dan Koeksistensi Radio

ESP32-S3 adalah mikrokontroler Wi-Fi 802.11 b/g/n 2,4 GHz berantena tunggal dengan inti ganda 240 MHz, SRAM 512 KB, dan PSRAM hingga 8 MB [18]. Dukungan CSI tersedia resmi lewat repositori esp-csi; pada kanal 20 MHz, CSI mencakup 56 *subcarrier* [19]. RuView merekomendasikan ESP32-S3 sebagai modul penangkap CSI dan menyediakan rantai akuisisi lengkap [20], yang dipetakan pada Tabel 2.1. Repositori yang sama menerbitkan keluarga model WiFi-DensePose, mengikuti DensePose from WiFi yang memetakan sinyal Wi-Fi ke permukaan tubuh dengan jaringan visi sebagai guru [28]; model terpralatihnya berkuantisasi int8 dan dipakai sebagai *backbone* murid (Subbab 3.7).

Fakta yang paling menentukan adalah koeksistensi radio pada satu *chip*. *Firmware* RuView menjalankan penangkapan CSI, koneksi *station* UDP, dan sinkronisasi ESP-NOW secara serentak dengan syarat satu kanal dan mode hemat daya dimatikan [20]. Dengan demikian, purwarupa tidak memerlukan modul gerbang khusus. Karena RuView tidak melalui telaah sejawat, fungsinya diverifikasi sendiri pada gerbang G0.

Tabel 2.1 Pemetaan fitur RuView terhadap peran dalam penelitian ini

| Fitur RuView | Peran dalam penelitian ini |
|---|---|
| *Firmware* penangkap CSI (UDP) | Mengalirkan CSI dan label ke server |
| Station + UDP + CSI *promiscuous* + ESP-NOW pada satu *chip* | Dasar topologi satu kanal (Subbab 3.5) |
| Kalibrasi ruang 600 bingkai + 8 *anchor* | Kalibrasi tiap sesi; pemotongan segmen isyarat |
| Mode privasi | Membuang fitur biometrik selama penelitian |
| Akuisisi tersinkron kamera–CSI | Jalur guru; estimator diganti YOLO26m-Pose |
| Model WiFi-DensePose terpralatih int8 | Inisialisasi *backbone* murid |

## 2.4 Estimasi Pose Berbasis Visi sebagai Model Guru Kamera

Estimasi pose memperkirakan posisi titik tubuh manusia dari citra, dan YOLO26 dari Ultralytics menyediakannya bersama *dataset* *hand-keypoints* beranotasi 21 titik per tangan [29]. Dalam penelitian ini, YOLO26m-Pose menjadi model guru: ia membaca isyarat lewat kamera pada saat data direkam, lalu keluarannya berupa deret 21 titik dan label huruf menjadi acuan pelatihan model Wi-Fi. Pola pelatihan semacam ini punya preseden pada DensePose from WiFi [28].

Kemampuan guru sudah terbukti pada tahap pra-penelitian. Model juara mencatat *pose* mAP50 0,8944 pada 49 kelas isyarat, serta mAP50 0,9580 dan akurasi huruf 97,6% pada 24 huruf statis, termasuk membedakan V dan U serta mengikuti lintasan J dan Z. Bukti itu menegaskan bahwa 21 titik artikulasi jari memuat informasi yang cukup untuk gestur mikro SIBI. Pertanyaan penelitian ini tinggal satu: apakah CSI mampu mereplikasinya tanpa kamera. Setelah murid ter-*deploy*, seluruh jalur operasional berjalan tanpa kamera dan tanpa citra (Subbab 3.7).

## 2.5 Pengenalan Isyarat dan Gestur Berbasis CSI serta Inferensi pada Perangkat

Pengenalan bahasa isyarat dari CSI telah diteliti di beberapa negara. SignFi mengenali 276 isyarat ASL dengan akurasi hingga 99,8% di laboratorium, tetapi turun menjadi 86,66% pada lima pengguna baru [15]. DF-WiSLR mengenali 49 gestur tanpa perangkat dikenakan [16], dan WiSign mengenali kalimat ASL kontinu dari perangkat komersial [17]. Belum ada yang menyentuh SIBI. Kebaruan penelitian ini karena itu bukan pada pengenalan kontinu, melainkan pada penerapan CSI untuk alfabet SIBI dan penyatuan dua arah dengan pemrosesan bahasa Indonesia (Subbab 2.10).

Rancangan fitur mengikuti praktik yang terbukti: amplitudo dan fase *subcarrier* terpilih serta spektrum Doppler [14], [27]. SVM menjadi pembanding dasar karena kuat pada *dataset* kecil [30]. Model utamanya murid dua bagian, yaitu *backbone* WiFi-DensePose int8 [20] dengan kepala 1D-CNN ringan untuk deret waktu. Klasifikator himpunan tertutup selalu memilih satu kelas; karena itu, keluaran dilengkapi skor keyakinan dan mekanisme penolakan [31]. Keluaran dengan keyakinan rendah menampilkan pesan "isyarat tidak dikenali" daripada menebak salah. Inferensi dirancang berjalan langsung di modul. ESP-NN mempercepat model pendeteksi orang dari 2.300 ms menjadi 54 ms pada ESP32-S3 [32], dan ESP-DL menyediakan contoh pengenalan gestur tangan int8 69,2 ms [33], dengan TensorFlow Lite Micro sebagai alternatif [34]. Belum ada tolok ukur CSI-isyarat pada ESP32-S3 sehingga waktu inferensi aktual diukur sendiri (Subbab 3.7).

## 2.6 TTS dan ASR Bahasa Indonesia

Purwarupa memerlukan mesin sintesis ucapan (*text-to-speech*, TTS) dan pengenalan ucapan (*automatic speech recognition*, ASR). Kriteria pemilihannya tiga: dukungan bahasa Indonesia terverifikasi, tersedia jalur *on-device* dan lokal, serta biaya berkelanjutan yang masuk akal untuk sekolah. Mesin TTS *on-device* yang direncanakan adalah Kokoro-82M ONNX dengan sekitar 82 juta parameter [35], yang berjalan luring di ponsel melalui ONNX Runtime [36], [37]. *Model card* resminya mencantumkan delapan bahasa tanpa bahasa Indonesia sehingga ketersediaan suara Indonesia diverifikasi pada gerbang G3. Bila belum tersedia, jalur beralih ke MMS-TTS-ind, model TTS Indonesia dari Meta [38]. Layanan TTS dan ASR awan menjadi pembanding latensi dan mutu; pilihan finalnya ditetapkan setelah uji banding (Tabel 3.7).

Untuk ASR, Whisper dilatih pada lima juta jam audio dan mendukung lebih dari 100 bahasa termasuk Indonesia [39]. Implementasi faster-whisper menyelesaikan 13 menit audio dalam 59 detik pada GPU 8 GB, sekitar tiga belas kali lebih cepat dari waktu nyata [40]. Server lokal menjalankan faster-whisper sebagai cadangan bila internet terputus. Karena galat kata Whisper untuk percakapan bahasa Indonesia belum terverifikasi dari sumber primer, akurasinya diukur sendiri pada skenario pengujian (Subbab 3.8).

## 2.7 Pemetaan Teks ke Representasi SIBI di Layar

Menerjemahkan teks menjadi isyarat tidak bisa dilakukan kata demi kata. Bahasa isyarat punya tata bahasa sendiri, dan penerjemahan tingkat kalimat masih menjadi masalah terbuka [22]. Arah kedua karena itu dirancang pada tingkat kamus kata dengan ejaan jari sebagai cadangan, mengikuti preseden KASIBI dan OpenSIBI [9], [10]. Struktur SIBI mendukung rancangan ini karena alfabet manualnya lengkap, yaitu 26 huruf dan 9 angka [3].

Tampilan arah kedua dirancang dua lapis. Lapis utama menampilkan glos dan gambar bentuk tangan untuk kata yang tersedia di kamus; gambar berukuran sekitar dua puluh hingga tiga puluh kilobita sehingga muat di penyimpanan modul. Lapis kedua berupa animasi yang dialirkan dari server bila waktu pengembangan memungkinkan. Kata di luar kamus dialihkan ke ejaan jari. Cakupan kamus, yaitu proporsi kata uji yang terwakili, diukur dan dilaporkan sebagai metrik utama arah ini (Subbab 3.8).

## 2.8 Komunikasi Modul, Server, dan Topologi Jaringan

Seluruh perangkat terhubung pada satu kanal Wi-Fi yang sama sehingga penangkapan CSI dan komunikasi data berjalan serentak [20]. *Access point* berfungsi sebagai jembatan jaringan dan penjangkar kanal; perannya dapat dipegang *router* sekolah atau *hotspot* ponsel. Sinkronisasi antarmodul memakai ESP-NOW, dan aliran data ke server memakai UDP [20].

Perangkat lunak server ditulis purna Rust: Tokio menjalankan konkurensi [41], Axum menyediakan HTTP dan WebSocket [42], Leptos membangun dasbor yang dikompilasi ke WASM [43], dan Tauri menjadi aplikasi klien ponsel [44]. Alasannya praktis: tanpa pengumpul sampah, pemrosesan bingkai UDP tetap cepat; biner hemat memori; dan satu sistem tipe mendeteksi perubahan format bingkai saat kompilasi. Target *parsing* di bawah 0,2 ms dan memori server di bawah 40 MB adalah target rancangan yang diukur pada gerbang G3, bukan hasil yang dijanjikan. Server lokal laptop menjalankan server RuView, server Rust, faster-whisper, dan TTS MMS sebagai jalur cadangan tanpa internet.

## 2.9 Evaluasi Kelayakan

Kelayakan dinilai bertahap melalui lima gerbang G0–G4 (BAB III). Setiap tahap menghasilkan artefak tetap sehingga kegagalan tetap terdokumentasi dan dilaporkan. Rekomendasi akhir menyatakan posisi purwarupa pada skala kesiapterapan teknologi (TKT) yang mengikuti kerangka *technology readiness level* [45]. Kinerja klasifikasi diukur dengan akurasi, presisi, *recall*, skor F1 makro, dan *confusion matrix* per isyarat, selalu dibandingkan dengan peluang acak (satu dibagi jumlah kelas). Pembagian acak di dalam satu sesi tidak dipakai karena repetisi berurutan dapat membocorkan informasi latih ke uji. Kelayakan alat komunikasi dinilai dari empat dimensi tambahan: latensi ujung ke ujung, cakupan kamus, keandalan operasional, dan biaya. Persepsi pengguna diukur dengan kuesioner skala Likert [46] dan dianalisis secara deskriptif; kewajaran keluaran dinilai validator penutur tunarungu.

## 2.10 Penelitian Terdahulu

Penelitian ini mempertimbangkan penelitian terdahulu pada empat topik: pengenalan bahasa isyarat dari sinyal Wi-Fi, transfer visi ke Wi-Fi, pengenalan isyarat berbasis kamera di Indonesia, dan sistem SIBI satu arah. Tabel 2.2 membandingkan yang paling relevan.

Tabel 2.2 Perbandingan penelitian terdahulu

| No. | Peneliti (Tahun) | Modalitas dan arah | Bahasa isyarat | Bebas kamera | Fokus |
|---|---|---|---|---|---|
| 1 | Ma dkk. (2018) [15] | CSI; isyarat menjadi teks | ASL, 276 isyarat | Ya | Pengenalan berskala besar |
| 2 | Zhang dkk. (2020) [17] | CSI; isyarat menjadi teks | ASL, kalimat kontinu | Ya | Pengenalan kontinu |
| 3 | Ahmed dkk. (2020) [16] | CSI; isyarat menjadi teks | 49 gestur | Ya | Tanpa perangkat dikenakan |
| 4 | Geng dkk. (2023) [28] | Wi-Fi dengan guru visi | Bukan bahasa isyarat | Ya | Pose padat tubuh |
| 5 | Dwijayanti dkk. (2021) [11] | Citra; isyarat menjadi teks | BISINDO | Tidak | CNN pengenalan citra |
| 6 | Soekarta dkk. (2024) [12] | Citra; isyarat menjadi teks | SIBI, 24 huruf statis | Tidak | Aplikasi MediaPipe |
| 7 | Zikky dan Akbar (2019) [9]; Fatmawati dkk. (2022) [10] | Suara menjadi animasi 3D | SIBI | Ya | Kamus suara-isyarat; OpenSIBI 50 kosakata |
| 8 | Penelitian ini | CSI sepasang ESP32-S3, inferensi tepi, dua arah, TTS *on-device* | SIBI, alfabet 26 huruf | Ya | Purwarupa penerjemah dua arah |

Tabel 2.2 memperlihatkan empat kelompok. Pengenalan isyarat dari Wi-Fi [15], [17], [16] berjalan tanpa kamera tetapi tidak menjangkau SIBI. Transfer visi ke Wi-Fi [28] menjadi preseden pelatihan guru–murid. Riset Indonesia berbasis kamera [11], [12] membuktikan minat yang tinggi tetapi terikat pencahayaan dan garis pandang. Kamus suara-animasi [9], [10] menutup satu arah dengan kosakata terbatas. Dalam batas penelusuran, belum ditemukan publikasi pengenalan isyarat SIBI dari CSI maupun purwarupa dua arah yang memadukannya dengan TTS dan ASR bahasa Indonesia pada ESP32-S3. Kebaruan penelitian ini karena itu bersifat kombinatif: CSI satu tautan pada sepasang ESP32-S3 untuk alfabet SIBI, distilasi guru–murid, inferensi tepi, dan integrasi dua arah dengan pemrosesan bahasa Indonesia. Kebaruan tidak diklaim pada pengenalan kontinu maupun penerjemahan kalimat penuh.

## 2.11 Matriks Justifikasi Pemilihan Komponen

Tabel 2.3 merangkum jawaban atas pertanyaan "mengapa X dan bukan Y" untuk tujuh keputusan arsitektur. Seluruh target kinerja adalah target rancangan yang diukur pada gerbang BAB III, bukan hasil yang dijanjikan.

Tabel 2.3 Matriks justifikasi pemilihan komponen (Mengapa X dan Bukan Y?)

| No. | Keputusan | Komponen dipilih | Alternatif ditinggalkan | Justifikasi |
|---|---|---|---|---|
| 1 | Tumpukan UI dan server | Purna Rust: Tokio/Axum, Leptos (WASM), Tauri [41], [42], [43], [44] | Node.js, Streamlit, Electron, React/JS | *Parsing* UDP di bawah 0,2 ms; memori di bawah 40 MB; satu sistem tipe (Subbab 2.8) |
| 2 | Mesin TTS | Kokoro TTS ONNX *on-device*; prasyarat suara Indonesia pada G3; alternatif MMS-TTS-ind [36], [35], [38] | TTS awan, VITS/Tacotron penuh | Model 82 juta parameter diinferensikan luring pada ponsel (Subbab 2.6) |
| 3 | Node penginderaan | ESP32-S3 [18] | ESP32 biasa, C3/C6, Arduino Uno | Instruksi vektor int8; PSRAM penyangga CSI dan model; API CSI resmi (Subbab 2.3) |
| 4 | Penginderaan radio | CSI-Ratio 2,4 GHz kanal 20 MHz [25] | RSSI, radar khusus, *time of flight* | RSSI terlalu kasar; CSI-ratio membersihkan derau fase tanpa perangkat tambahan [26] (Subbab 2.2) |
| 5 | Model guru visi | YOLO26m-Pose 21 *keypoint* [29] | YOLOv8-pose, MediaPipe, UNet | 21 titik artikulasi vital untuk membedakan V/U dan lintasan J/Z; akurasi 97,6% pada pra-penelitian (Subbab 2.4) |
| 6 | Model murid tepi | WiFi-DensePose int8 + 1D-CNN [20], [28] | SVM utama, MLP berat | Int8 berjalan pada modul, target di bawah 100 ms; SVM pembanding (Subbab 2.5) |
| 7 | Metode distilasi | Distilasi visual-ke-Wi-Fi [21], [28] | Pelatihan Wi-Fi murni | CSI abstrak memerlukan supervisi spasial guru; manfaatnya diuji lewat ablasi (Subbab 3.7) |
