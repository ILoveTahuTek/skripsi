# BAB II KAJIAN PUSTAKA

## 2.1 Bahasa Isyarat, SIBI, dan Kebutuhan Komunikasi Dua Arah

Bahasa isyarat menyampaikan makna lewat gerak tangan, lengan, tubuh, dan ekspresi wajah. Satu isyarat tersusun atas bentuk tangan, lokasi, gerak, serta orientasi telapak; cukup satu jari berubah bentuk, maknanya bisa ikut berubah. Susunan inilah yang menjadi acuan penelitian dalam memisahkan bagian isyarat yang bisa dinilai mesin dari bagian yang tetap memerlukan penilaian manusia [3]. SIBI ialah sistem isyarat baku pendidikan formal yang didokumentasikan kamus pemerintah [3]; BISINDO tumbuh alami di komunitas tunarungu [7]. Keduanya tidak bersaing menggantikan satu sama lain karena masing-masing hidup di ranah berbeda [8], [5]. Survei terhadap 100 responden tunarungu di Jawa dan Bali menemukan 91% lebih banyak memakai BISINDO, sementara SIBI menempel pada konteks sekolah [8]. Penelitian ini tetap memilih SIBI karena sasarannya alat bantu pembelajaran di sekolah, bukan karena jumlah penuturnya lebih besar.

Bicara antara pengguna isyarat dan orang pendengar menuntut dua arah. Keluarga dan guru berada di barisan paling depan untuk merasakan kesenjangan ini, sementara jumlah juru bahasa masih jauh dari cukup [1]; alat bantu yang dibangun karena itu harus dua arah, bukan sekadar kamus satu arah. Sistem terdahulu di Indonesia baru menutup satu arah saja. KASIBI mengubah ucapan menjadi teks lalu memunculkan animasi tangan tiga dimensi, dengan rata-rata skor 3,362 dari 4 pada penilaiannya [9]; OpenSIBI menganimasikan model tiga dimensi untuk 50 kosakata yang terdiri atas 9 angka, 26 huruf, dan 15 kata [10]. Untuk arah isyarat menjadi teks, riset dalam negeri bertumpu pada kamera. Contohnya CNN untuk huruf BISINDO [11], tinjauan sistematis pengenalan BISINDO berbasis citra [23], aplikasi MediaPipe untuk 24 huruf statis SIBI [12], aplikasi Android berbasis *deep learning* [13], dan *dataset* video BISINDO tingkat kata [24]. Masalahnya, kamera menuntut pencahayaan dan garis pandang yang baik, dan kamera yang terus menyala membuat pengguna merasa diawasi. Dua kendala inilah yang mendorong pencarian jalur penginderaan tanpa kamera dan tanpa perangkat yang dikenakan.

## 2.2 Wi-Fi Channel State Information

*Channel State Information* (CSI) memuat informasi amplitudo dan fase pada setiap *subcarrier* sinyal Wi-Fi, yang bersama-sama menggambarkan kondisi jalur propagasi [14]. Tubuh yang bergerak di antara pemancar dan penerima mengubah panjang jalur pantulan; amplitudo dan fase tiap *subcarrier* pun ikut bergeser. Geseran inilah yang dipakai untuk mengenali gerak tanpa sensor yang dikenakan. Karena tiap *subcarrier* menempati frekuensi berbeda, satu pasang perangkat sekaligus menyediakan banyak kanal pengamatan [14].

Pemodelan CSI sendiri berpijak pada zona Fresnel [25]. Artikulasi jari menggeser jalur pantulan pada orde sentimeter sampai milimeter, dan tiap bentuk huruf meninggalkan pola perubahan *subcarrier* yang khas. Masalahnya, fase mentah tercemar derau osilator lokal; teknik CSI-ratio membersihkannya lewat rasio atau perkalian konjugat tanpa perangkat tambahan [25], dan Widar2.0 memakai teknik serupa untuk pelacakan manusia [26]. Prinsip yang sama diterapkan penelitian ini pada modul penerima sebagai rasio terhadap rekam acuan kalibrasi ruang (Subbab 3.7). Gerak tubuh juga melahirkan komponen Doppler [14]; untuk menangkapnya, pita analisis 1–60 Hz menuntut laju pencuplikan sekurang-kurangnya 120 Hz menurut kaidah Nyquist. Padahal *firmware* RuView membatasi laju paling sering 50 bingkai per detik [20]. Jika laju terukur lebih rendah, pita yang dianalisis menyempit, dan hal itu dilaporkan apa adanya.

Dari ketukan tombol sampai gerakan jari, bukti kepekaan CSI terhadap gerak halus cukup banyak [14]; akan tetapi, bukti-bukti itu lahir dari kondisi terkendali sehingga bagi penelitian ini statusnya sebatas hipotesis kerja. Model CSI juga mudah *overfitting* terhadap orang dan ruang, dan Widar3.0 menjawab masalah itu dengan profil kecepatan Doppler untuk pengenalan lintas domain [27]. Resolusi spasial ikut terbatasi panjang gelombang 2,4 GHz yang hanya sekitar 12,5 cm, sementara sebagian besar preseden memakai perangkat berantena banyak. Kelayakan satu tautan dua modul berantena tunggal untuk membedakan 26 bentuk tangan SIBI karenanya diperlakukan sebagai pertanyaan penelitian, bukan asumsi; uji Delta-CSI dan gerbang G1 yang mengujinya. Jika beberapa huruf terbukti tidak terpisahkan, himpunan huruf dipangkas (Tabel 3.7).

## 2.3 Modul ESP32-S3, Platform RuView, dan Koeksistensi Radio

ESP32-S3 ialah mikrokontroler Wi-Fi 802.11 b/g/n 2,4 GHz berantena tunggal dengan inti ganda 240 MHz, SRAM 512 KB, dan PSRAM hingga 8 MB [18]. Dukungan CSI tersedia resmi lewat repositori esp-csi; pada kanal 20 MHz, CSI memuat 56 *subcarrier* [19]. RuView merekomendasikan ESP32-S3 sebagai modul penangkap CSI sekaligus menyediakan rantai akuisisi lengkap [20] yang dipetakan pada Tabel 2.1. Repositori yang sama menerbitkan keluarga model WiFi-DensePose menuruti jejak DensePose from WiFi, yang memetakan sinyal Wi-Fi ke permukaan tubuh dengan jaringan visi sebagai guru [28]; model terpralatihnya berkuantisasi int8 dan dipakai sebagai *backbone* murid (Subbab 3.7).

Fakta paling menentukan justru koeksistensi radio pada satu *chip*. *Firmware* RuView mampu menangkap CSI sambil memelihara koneksi *station* UDP serta sinkronisasi ESP-NOW secara serentak. Dua syaratnya: seluruh perangkat berada pada satu kanal dan mode hemat daya dimatikan [20]. Purwarupa karenanya tidak memerlukan modul gerbang khusus, tetapi ada satu catatan penting: RuView belum melalui telaah sejawat, jadi fungsinya diverifikasi sendiri pada gerbang G0.

Tabel 2.1 Pemetaan fitur RuView terhadap peran dalam penelitian ini

| Fitur RuView | Peran dalam penelitian ini |
|---|---|
| *Firmware* penangkap CSI (UDP) | Mengalirkan CSI dan label ke server |
| Station + UDP + CSI *promiscuous* + ESP-NOW pada satu *chip* | Dasar topologi satu kanal (Subbab 3.5) |
| Kalibrasi ruang 600 bingkai + 8 *anchor* | Kalibrasi tiap sesi; pemotongan segmen isyarat |
| Mode privasi | Membuang fitur biometrik selama penelitian |
| Akuisisi tersinkron kamera-CSI | Jalur guru; estimator diganti YOLO26m-Pose |
| Model WiFi-DensePose terpralatih int8 | Inisialisasi *backbone* murid |

## 2.4 Estimasi Pose Berbasis Visi sebagai Model Guru Kamera

Estimasi pose memperkirakan posisi titik tubuh manusia dari citra; YOLO26 dari Ultralytics menyediakannya lengkap dengan *dataset* *hand-keypoints* beranotasi 21 titik per tangan [29]. Pada penelitian ini, YOLO26m-Pose mengambil peran guru: membaca isyarat lewat kamera saat data direkam, lalu mengeluarkan deret 21 titik beserta label huruf yang menjadi acuan pelatihan model Wi-Fi. Pola pelatihan seperti ini punya preseden pada DensePose from WiFi [28].

Kemampuan guru tersebut sudah teruji pada tahap pra-penelitian. Model juara mencatat *pose* mAP50 0,8944 pada 49 kelas isyarat, serta mAP50 0,9580 dan akurasi huruf 97,6% pada 24 huruf statis. Pembedaan pasangan V dan U serta lintasan J dan Z ikut teruji di dalamnya. Dari angka itu terbaca bahwa 21 titik artikulasi jari memuat informasi cukup untuk gestur mikro SIBI. Pertanyaan penelitian ini tinggal satu: apakah CSI sanggup mereplikasinya tanpa kamera? Setelah murid ter-*deploy*, seluruh jalur operasional berjalan tanpa kamera dan tanpa citra (Subbab 3.7).

## 2.5 Pengenalan Isyarat dan Gestur Berbasis CSI serta Inferensi pada Perangkat

Riset pengenalan bahasa isyarat dari CSI sudah berjalan di beberapa negara. SignFi mengenali 276 isyarat ASL dengan akurasi hingga 99,8% di laboratorium, walau turun menjadi 86,66% ketika diuji pada lima pengguna baru [15]. DF-WiSLR mengenali 49 gestur tanpa perangkat yang dikenakan [16], dan WiSign membaca kalimat ASL kontinu dari perangkat komersial [17]. Namun, belum satu pun dari sana menyentuh SIBI. Kebaruan penelitian ini ada pada penerapan CSI untuk alfabet SIBI serta penyatuan dua arah bersama pemrosesan bahasa Indonesia (Subbab 2.10).

Rancangan fiturnya mengikuti praktik yang terbukti: amplitudo dan fase *subcarrier* terpilih serta spektrum Doppler [14], [27]. SVM dijadikan pembanding dasar karena kuat pada *dataset* kecil [30], sedangkan model utamanya murid dua bagian: *backbone* WiFi-DensePose int8 [20] dengan kepala 1D-CNN ringan untuk deret waktu. Klasifikator himpunan tertutup selalu memilih satu kelas, sehingga keluarannya perlu dilengkapi skor keyakinan dan mekanisme penolakan [31]; keyakinan yang rendah memunculkan pesan "isyarat tidak dikenali" alih-alih menebak salah. Inferensi sendiri dirancang berjalan langsung di modul. ESP-NN membuktikan hal itu mungkin: model pendeteksi orang terpicu dari 2.300 ms menjadi 54 ms pada ESP32-S3 [32], dan ESP-DL menyediakan contoh pengenalan gestur tangan int8 69,2 ms [33], dengan TensorFlow Lite Micro sebagai alternatif [34]. Tolok ukur CSI-isyarat pada ESP32-S3 sendiri belum ada, jadi waktu inferensi aktual diukur sendiri (Subbab 3.7).

## 2.6 TTS dan ASR Bahasa Indonesia

Purwarupa membutuhkan mesin sintesis ucapan (*text-to-speech*, TTS) dan pengenalan ucapan (*automatic speech recognition*, ASR). Tiga kriteria menyeleksi keduanya: dukungan bahasa Indonesia terverifikasi, jalur *on-device* dan lokal tersedia, serta biaya berkelanjutan yang masuk akal bagi sekolah. Mesin TTS *on-device* yang direncanakan ialah Kokoro-82M ONNX bersama sekitar 82 juta parameter [35], berjalan luring di ponsel melalui ONNX Runtime [36], [37]. *Model card* resminya mencantumkan delapan bahasa tanpa bahasa Indonesia, sehingga ketersediaan suara Indonesia perlu diverifikasi pada gerbang G3; jika memang belum tersedia, jalur beralih ke MMS-TTS-ind, model TTS Indonesia dari Meta [38]. Layanan TTS dan ASR awan hadir sebagai pembanding latensi dan mutu, dan pilihan finalnya ditetapkan setelah uji banding (Tabel 3.7).

Pada sisi ASR, Whisper dilatih dengan lima juta jam audio dan mendukung lebih dari 100 bahasa, termasuk Indonesia [39]. Implementasi faster-whisper tercatat menuntaskan 13 menit audio dalam 59 detik pada GPU 8 GB, kira-kira tiga belas kali lipat kecepatan waktu nyata [40]. Ketika internet terputus, server lokal mengambil alih dengan faster-whisper sebagai cadangan. Galat kata Whisper untuk percakapan bahasa Indonesia belum terverifikasi dari sumber primer, jadi akurasinya diukur sendiri pada skenario pengujian (Subbab 3.8).

## 2.7 Pemetaan Teks ke Representasi SIBI di Layar

Terjemahan teks menjadi isyarat tidak mungkin dilakukan kata demi kata. Bahasa isyarat memiliki tata bahasa sendiri, dan penerjemahan tingkat kalimat sampai kini masih menjadi masalah terbuka [22]. Arah kedua karenanya dirancang pada tingkat kamus kata dengan ejaan jari sebagai cadangan, menelusuri preseden KASIBI dan OpenSIBI [9], [10]. Struktur SIBI mendukung rancangan ini sebab alfabet manualnya lengkap: 26 huruf dan 9 angka [3].

Tampilan pada arah kedua disusun atas dua lapis. Lapis utama memunculkan glos dan gambar bentuk tangan untuk kata yang tersedia di kamus; ukuran gambarnya sekitar dua puluh sampai tiga puluh kilobita sehingga muat di penyimpanan modul. Lapis kedua berupa animasi yang dialirkan dari server, jika waktu pengembangan memungkinkan. Kata di luar kamus dialihkan ke ejaan jari. Sebagai metrik utama arah ini, cakupan kamus, yaitu proporsi kata uji yang terwakili, diukur dan dilaporkan (Subbab 3.8).

## 2.8 Komunikasi Modul, Server, dan Topologi Jaringan

Seluruh perangkat, dari kedua modul penginderaan sampai ponsel, berbagi satu kanal Wi-Fi yang sama sehingga penangkapan CSI berjalan serentak dengan komunikasi data [20]. Peran jembatan jaringan sekaligus penjangkar kanal dipegang *access point*, yang bentuknya bisa *router* sekolah maupun *hotspot* ponsel. Sinkronisasi antarmodul memakai ESP-NOW, sedangkan aliran data ke server memakai UDP [20].

Perangkat lunak server ditulis seluruhnya dalam Rust: konkurensi ditangani Tokio [41], Axum menyediakan HTTP dan WebSocket [42], Leptos membangun dasbor yang dikompilasi ke WASM [43], dan Tauri menjadi aplikasi klien ponsel [44]. Alasannya praktis. Tanpa pengumpul sampah, pemrosesan bingkai UDP tetap cepat; binernya hemat memori; dan satu sistem tipe mendeteksi perubahan format bingkai saat kompilasi. Target *parsing* di bawah 0,2 ms dan memori server di bawah 40 MB adalah target rancangan yang baru diukur pada gerbang G3, bukan hasil yang dijanjikan. Server lokal pada laptop menjalankan server RuView, server Rust, faster-whisper, dan TTS MMS sebagai jalur cadangan tanpa internet.

## 2.9 Evaluasi Kelayakan

Penilaian kelayakan berjalan bertahap lewat lima gerbang G0 sampai G4 (BAB III), dan tiap tahap menghasilkan artefak tetap sehingga kegagalan pun tetap terdokumentasi. Rekomendasi akhirnya menyatakan posisi purwarupa pada skala kesiapterapan teknologi (TKT) yang mengikuti kerangka *technology readiness level* [45]. Kinerja klasifikasi diukur dengan akurasi, presisi, *recall*, skor F1 makro, serta *confusion matrix* per isyarat, selalu dibandingkan terhadap peluang acak (satu dibagi jumlah kelas). Pembagian acak di dalam satu sesi tidak dipakai sebab repetisi berurutan bisa membocorkan informasi latih ke uji. Empat dimensi tambahan menilai kelayakan alat komunikasinya: latensi ujung ke ujung, cakupan kamus, keandalan operasional, dan biaya. Persepsi pengguna diukur dengan kuesioner skala Likert [46] lalu dianalisis secara deskriptif, sedangkan kewajaran keluaran dinilai validator penutur tunarungu.

## 2.10 Penelitian Terdahulu

Empat topik penelitian terdahulu dipertimbangkan: pengenalan bahasa isyarat dari sinyal Wi-Fi, transfer visi ke Wi-Fi, pengenalan isyarat berbasis kamera di Indonesia, dan sistem SIBI satu arah. Tabel 2.2 membandingkan yang paling relevan di antaranya.

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

Empat kelompok penelitian bisa dibaca dari Tabel 2.2. Pengenalan isyarat dari Wi-Fi [15], [17], [16] berjalan tanpa kamera tetapi belum menjangkau SIBI; transfer visi ke Wi-Fi [28] menjadi preseden pelatihan guru-murid. Riset Indonesia berbasis kamera [11], [12] membuktikan tingginya minat namun tetap terikat pencahayaan dan garis pandang; kamus suara-animasi [9], [10] menutup satu arah dengan kosakata terbatas. Dalam batas penelusuran, publikasi pengenalan isyarat SIBI dari CSI maupun purwarupa dua arah yang memadukannya dengan TTS dan ASR bahasa Indonesia pada ESP32-S3 belum ditemukan. Kebaruan penelitian ini karenanya bersifat kombinatif: CSI satu tautan pada sepasang ESP32-S3 untuk alfabet SIBI, distilasi guru-murid, inferensi tepi, dan integrasi dua arah dengan pemrosesan bahasa Indonesia. Di luar itu, kebaruan tidak diklaim untuk pengenalan kontinu maupun penerjemahan kalimat penuh.

## 2.11 Matriks Justifikasi Pemilihan Komponen

Tabel 2.3 merangkum jawaban atas pertanyaan "mengapa X dan bukan Y" untuk tujuh keputusan arsitektur. Seluruh target kinerja di dalamnya adalah target rancangan yang baru diukur pada gerbang BAB III, bukan hasil yang dijanjikan.

Tabel 2.3 Matriks justifikasi pemilihan komponen (Mengapa X dan Bukan Y?)

| No. | Keputusan | Komponen dipilih | Alternatif ditinggalkan | Justifikasi |
|---|---|---|---|---|
| 1 | Tumpukan UI dan server | Seluruhnya Rust: Tokio/Axum, Leptos (WASM), Tauri [41], [42], [43], [44] | Node.js, Streamlit, Electron, React/JS | *Parsing* UDP di bawah 0,2 ms; memori di bawah 40 MB; satu sistem tipe (Subbab 2.8) |
| 2 | Mesin TTS | Kokoro TTS ONNX *on-device*; prasyarat suara Indonesia pada G3; alternatif MMS-TTS-ind [36], [35], [38] | TTS awan, VITS/Tacotron penuh | Model 82 juta parameter diinferensikan luring pada ponsel (Subbab 2.6) |
| 3 | Node penginderaan | ESP32-S3 [18] | ESP32 biasa, C3/C6, Arduino Uno | Instruksi vektor int8; PSRAM penyangga CSI dan model; API CSI resmi (Subbab 2.3) |
| 4 | Penginderaan radio | CSI-Ratio 2,4 GHz kanal 20 MHz [25] | RSSI, radar khusus, *time of flight* | RSSI terlalu kasar; CSI-ratio membersihkan derau fase tanpa perangkat tambahan [26] (Subbab 2.2) |
| 5 | Model guru visi | YOLO26m-Pose 21 *keypoint* [29] | YOLOv8-pose, MediaPipe, UNet | 21 titik artikulasi vital untuk membedakan V/U dan lintasan J/Z; akurasi 97,6% pada pra-penelitian (Subbab 2.4) |
| 6 | Model murid tepi | WiFi-DensePose int8 + 1D-CNN [20], [28] | SVM utama, MLP berat | Int8 berjalan pada modul, target di bawah 100 ms; SVM pembanding (Subbab 2.5) |
| 7 | Metode distilasi | Distilasi visual-ke-Wi-Fi [21], [28] | Pelatihan Wi-Fi murni | CSI abstrak memerlukan supervisi spasial guru; manfaatnya diuji lewat ablasi (Subbab 3.7) |
