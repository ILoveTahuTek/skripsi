# BAB II KAJIAN PUSTAKA

## 2.1 Bahasa Isyarat, SIBI, dan Kebutuhan Komunikasi Dua Arah

Bahasa isyarat menyampaikan makna lewat gerak tangan, lengan, tubuh, dan ekspresi wajah. Satu isyarat tersusun atas bentuk tangan, lokasi, gerak, serta orientasi telapak; cukup satu jari berubah bentuk, maknanya bisa ikut berubah. Susunan inilah yang menjadi acuan penelitian dalam memisahkan bagian isyarat yang bisa dinilai mesin dari bagian yang tetap memerlukan penilaian manusia [3]. SIBI ialah sistem isyarat baku pendidikan formal yang didokumentasikan kamus pemerintah [3], sedangkan BISINDO tumbuh alami di komunitas tunarungu. Survei terhadap 100 responden tunarungu di Jawa dan Bali menemukan 91% memakai BISINDO, sementara SIBI menempel pada konteks sekolah [4]. Penelitian ini tetap memilih SIBI karena sasarannya alat bantu pembelajaran di sekolah, bukan karena jumlah penuturnya lebih besar.

Bicara antara pengguna isyarat dan orang pendengar menuntut dua arah. Keluarga dan guru berada di barisan paling depan untuk merasakan kesenjangan ini, sementara jumlah juru bahasa masih jauh dari cukup [1]; alat bantu yang dibangun karena itu harus dua arah, bukan sekadar kamus satu arah. Sistem satu arah yang mengubah ucapan menjadi animasi isyarat sudah lebih dulu hadir di Indonesia, tetapi untuk arah isyarat menjadi teks riset dalam negeri bertumpu pada kamera, misalnya CNN untuk huruf BISINDO [5]. Masalahnya, kamera menuntut pencahayaan dan garis pandang yang baik, dan kamera yang terus menyala membuat pengguna merasa diawasi. Dua kendala inilah yang mendorong pencarian jalur penginderaan tanpa kamera dan tanpa perangkat yang dikenakan.

## 2.2 Wi-Fi Channel State Information

*Channel State Information* (CSI) memuat informasi amplitudo dan fase pada setiap *subcarrier* sinyal Wi-Fi, yang bersama-sama menggambarkan kondisi jalur propagasi [6]. Tubuh yang bergerak di antara pemancar dan penerima mengubah panjang jalur pantulan; amplitudo dan fase tiap *subcarrier* pun ikut bergeser. Geseran inilah yang dipakai untuk mengenali gerak tanpa sensor yang dikenakan. Karena tiap *subcarrier* menempati frekuensi berbeda, satu pasang perangkat sekaligus menyediakan banyak kanal pengamatan [6].

Pemodelan CSI sendiri berpijak pada zona Fresnel [12]. Artikulasi jari menggeser jalur pantulan pada orde sentimeter sampai milimeter, dan tiap bentuk huruf meninggalkan pola perubahan *subcarrier* yang khas. Masalahnya, fase mentah tercemar derau osilator lokal; teknik CSI-ratio membersihkannya lewat rasio atau perkalian konjugat tanpa perangkat tambahan [12], dan prinsip yang sama diterapkan penelitian ini pada modul penerima sebagai rasio terhadap rekam acuan kalibrasi ruang (Subbab 3.7). Gerak tubuh juga melahirkan komponen Doppler [6]; untuk menangkapnya, pita analisis 1–60 Hz menuntut laju pencuplikan sekurang-kurangnya 120 Hz menurut kaidah Nyquist, padahal *firmware* RuView membatasi laju paling sering 50 bingkai per detik [10]. Jika laju terukur lebih rendah, pita yang dianalisis menyempit, dan hal itu dilaporkan apa adanya.

Dari ketukan tombol sampai gerakan jari, bukti kepekaan CSI terhadap gerak halus cukup banyak [6]; akan tetapi, bukti-bukti itu lahir dari kondisi terkendali sehingga bagi penelitian ini statusnya sebatas hipotesis kerja. Model CSI juga mudah *overfitting* terhadap orang dan ruang, dan Widar3.0 menjawab masalah itu dengan profil kecepatan Doppler untuk pengenalan lintas domain [13]. Resolusi spasial ikut terbatasi panjang gelombang 2,4 GHz yang hanya sekitar 12,5 cm, sementara sebagian besar preseden memakai perangkat berantena banyak. Kelayakan satu tautan dua modul berantena tunggal untuk membedakan 26 bentuk tangan SIBI karenanya diperlakukan sebagai pertanyaan penelitian, bukan asumsi; uji Delta-CSI dan gerbang G1 yang mengujinya. Jika beberapa huruf terbukti tidak terpisahkan, himpunan huruf dipangkas (Tabel 3.7).

## 2.3 Modul ESP32-S3, Platform RuView, dan Koeksistensi Radio

ESP32-S3 ialah mikrokontroler Wi-Fi 802.11 b/g/n 2,4 GHz berantena tunggal dengan inti ganda 240 MHz, SRAM 512 KB, dan PSRAM hingga 8 MB [8]. Dukungan CSI tersedia resmi lewat repositori esp-csi; pada kanal 20 MHz, CSI memuat 56 *subcarrier* [9]. RuView merekomendasikan ESP32-S3 sebagai modul penangkap CSI sekaligus menyediakan rantai akuisisi lengkap [10] yang dipetakan pada Tabel 2.1. Repositori yang sama menerbitkan keluarga model WiFi-DensePose yang memetakan sinyal Wi-Fi ke permukaan tubuh dengan jaringan visi sebagai guru; model terpralatihnya berkuantisasi int8 dan dipakai sebagai *backbone* murid (Subbab 3.7).

Fakta paling menentukan justru koeksistensi radio pada satu *chip*. *Firmware* RuView mampu menangkap CSI sambil memelihara koneksi *station* UDP serta sinkronisasi ESP-NOW secara serentak. Dua syaratnya: seluruh perangkat berada pada satu kanal dan mode hemat daya dimatikan [10]. Purwarupa karenanya tidak memerlukan modul gerbang khusus, tetapi ada satu catatan penting: RuView belum melalui telaah sejawat, jadi fungsinya diverifikasi sendiri pada gerbang G0.

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

Estimasi pose memperkirakan posisi titik tubuh manusia dari citra; YOLO26 dari Ultralytics menyediakannya lengkap dengan *dataset* *hand-keypoints* beranotasi 21 titik per tangan [14]. Pada penelitian ini, YOLO26m-Pose mengambil peran guru: membaca isyarat lewat kamera saat data direkam, lalu mengeluarkan deret 21 titik beserta label huruf yang menjadi acuan pelatihan model Wi-Fi. Pola guru-murid semacam ini mengikuti keluarga model WiFi-DensePose pada RuView [10].

Kemampuan guru tersebut sudah teruji pada tahap pra-penelitian. Model juara mencatat *pose* mAP50 0,8944 pada 49 kelas isyarat, serta mAP50 0,9580 dan akurasi huruf 97,6% pada 24 huruf statis. Pembedaan pasangan V dan U serta lintasan J dan Z ikut teruji di dalamnya. Dari angka itu terbaca bahwa 21 titik artikulasi jari memuat informasi cukup untuk gestur mikro SIBI. Pertanyaan penelitian ini tinggal satu: apakah CSI sanggup mereplikasinya tanpa kamera? Setelah murid ter-*deploy*, seluruh jalur operasional berjalan tanpa kamera dan tanpa citra (Subbab 3.7).

## 2.5 Pengenalan Isyarat dan Gestur Berbasis CSI serta Inferensi pada Perangkat

Riset pengenalan bahasa isyarat dari CSI sudah berjalan di beberapa negara. SignFi mengenali 276 isyarat ASL dengan akurasi hingga 99,8% di laboratorium, walau turun menjadi 86,66% ketika diuji pada lima pengguna baru [7]; namun, jalur ini belum menyentuh SIBI. Kebaruan penelitian ini ada pada penerapan CSI untuk alfabet SIBI serta penyatuan dua arah bersama pemrosesan bahasa Indonesia (Subbab 2.10).

Rancangan fiturnya mengikuti praktik yang terbukti: amplitudo dan fase *subcarrier* terpilih serta spektrum Doppler [6], [13]. SVM dijadikan pembanding dasar karena kuat pada *dataset* kecil [15], sedangkan model utamanya murid dua bagian: *backbone* WiFi-DensePose int8 [10] dengan kepala 1D-CNN ringan untuk deret waktu. Klasifikator himpunan tertutup selalu memilih satu kelas, sehingga keluarannya perlu dilengkapi skor keyakinan dan mekanisme penolakan [16]; keyakinan yang rendah memunculkan pesan "isyarat tidak dikenali" alih-alih menebak salah. Inferensi sendiri dirancang berjalan langsung di modul. ESP-DL membuktikan hal itu mungkin dengan contoh pengenalan gestur tangan int8 69,2 ms pada keluarga ESP32 [17]; TensorFlow Lite Micro menjadi alternatifnya. Tolok ukur CSI-isyarat pada ESP32-S3 sendiri belum ada, jadi waktu inferensi aktual diukur sendiri (Subbab 3.7).

## 2.6 TTS dan ASR Bahasa Indonesia

Purwarupa membutuhkan mesin sintesis ucapan (*text-to-speech*, TTS) dan pengenalan ucapan (*automatic speech recognition*, ASR). Tiga kriteria menyeleksi keduanya: dukungan bahasa Indonesia terverifikasi, jalur *on-device* dan lokal tersedia, serta biaya berkelanjutan yang masuk akal bagi sekolah. Mesin TTS *on-device* yang direncanakan ialah Kokoro-82M ONNX bersama sekitar 82 juta parameter [18], berjalan luring di ponsel melalui ONNX Runtime. *Model card* resminya mencantumkan delapan bahasa tanpa bahasa Indonesia, sehingga ketersediaan suara Indonesia perlu diverifikasi pada gerbang G3; jika memang belum tersedia, jalur beralih ke MMS-TTS-ind, model TTS Indonesia dari Meta [19]. Layanan TTS dan ASR awan hadir sebagai pembanding latensi dan mutu, dan pilihan finalnya ditetapkan setelah uji banding (Tabel 3.7).

Pada sisi ASR, Whisper dilatih dengan lima juta jam audio dan mendukung lebih dari 100 bahasa, termasuk Indonesia [20]. Ketika internet terputus, server lokal mengambil alih dengan implementasi faster-whisper sebagai cadangan. Galat kata Whisper untuk percakapan bahasa Indonesia belum terverifikasi dari sumber primer, jadi akurasinya diukur sendiri pada skenario pengujian (Subbab 3.8).

## 2.7 Pemetaan Teks ke Representasi SIBI di Layar

Terjemahan teks menjadi isyarat tidak mungkin dilakukan kata demi kata karena bahasa isyarat memiliki tata bahasa sendiri. Arah kedua karenanya dirancang pada tingkat kamus kata dengan ejaan jari sebagai cadangan. Struktur SIBI mendukung rancangan ini sebab alfabet manualnya lengkap: 26 huruf dan 9 angka [3].

Tampilan pada arah kedua disusun atas dua lapis. Lapis utama memunculkan glos dan gambar bentuk tangan untuk kata yang tersedia di kamus; ukuran gambarnya sekitar dua puluh sampai tiga puluh kilobita sehingga muat di penyimpanan modul. Lapis kedua berupa animasi yang dialirkan dari server, jika waktu pengembangan memungkinkan. Kata di luar kamus dialihkan ke ejaan jari. Sebagai metrik utama arah ini, cakupan kamus, yaitu proporsi kata uji yang terwakili, diukur dan dilaporkan (Subbab 3.8).

## 2.8 Komunikasi Modul, Server, dan Topologi Jaringan

Seluruh perangkat, dari kedua modul penginderaan sampai ponsel, berbagi satu kanal Wi-Fi yang sama sehingga penangkapan CSI berjalan serentak dengan komunikasi data [10]. Peran jembatan jaringan sekaligus penjangkar kanal dipegang *access point*, yang bentuknya bisa *router* sekolah maupun *hotspot* ponsel. Sinkronisasi antarmodul memakai ESP-NOW, sedangkan aliran data ke server memakai UDP [10].

Perangkat lunak server ditulis seluruhnya dalam Rust: konkurensi ditangani Tokio, Axum menyediakan HTTP dan WebSocket, Leptos membangun dasbor yang dikompilasi ke WASM, dan Tauri menjadi aplikasi klien ponsel. Alasannya praktis. Tanpa pengumpul sampah, pemrosesan bingkai UDP tetap cepat; binernya hemat memori; dan satu sistem tipe mendeteksi perubahan format bingkai saat kompilasi. Target *parsing* di bawah 0,2 ms dan memori server di bawah 40 MB adalah target rancangan yang baru diukur pada gerbang G3, bukan hasil yang dijanjikan. Server lokal pada laptop menjalankan server RuView, server Rust, faster-whisper, dan TTS MMS sebagai jalur cadangan tanpa internet.

## 2.9 Evaluasi Kelayakan

Penilaian kelayakan berjalan bertahap lewat lima gerbang G0 sampai G4 (BAB III), dan tiap tahap menghasilkan artefak tetap sehingga kegagalan pun tetap terdokumentasi. Rekomendasi akhirnya menyatakan posisi purwarupa pada skala kesiapterapan teknologi (TKT) yang mengikuti kerangka *technology readiness level* [21]. Kinerja klasifikasi diukur dengan akurasi, presisi, *recall*, skor F1 makro, serta *confusion matrix* per isyarat, selalu dibandingkan terhadap peluang acak (satu dibagi jumlah kelas). Pembagian acak di dalam satu sesi tidak dipakai sebab repetisi berurutan bisa membocorkan informasi latih ke uji. Empat dimensi tambahan menilai kelayakan alat komunikasinya: latensi ujung ke ujung, cakupan kamus, keandalan operasional, dan biaya. Persepsi pengguna diukur dengan kuesioner skala Likert [22] lalu dianalisis secara deskriptif, sedangkan kewajaran keluaran dinilai validator penutur tunarungu.

## 2.10 Penelitian Terdahulu

Penelitian terdahulu yang paling relevan dibandingkan pada Tabel 2.2, mencakup pengenalan isyarat dan gestur dari sinyal Wi-Fi serta pengenalan isyarat berbasis kamera di Indonesia.

Tabel 2.2 Perbandingan penelitian terdahulu

| No. | Peneliti (Tahun) | Modalitas dan arah | Bahasa isyarat | Bebas kamera | Fokus |
|---|---|---|---|---|---|
| 1 | Ma dkk. (2018) [7] | CSI; isyarat menjadi teks | ASL, 276 isyarat | Ya | Pengenalan berskala besar |
| 2 | Zhang dkk. (2022) [13] | CSI; gestur lintas domain | Gestur umum | Ya | Generalisasi lintas orang dan ruang |
| 3 | Dwijayanti dkk. (2021) [5] | Citra; isyarat menjadi teks | BISINDO | Tidak | CNN pengenalan citra |
| 4 | Penelitian ini | CSI sepasang ESP32-S3, inferensi tepi, dua arah, TTS *on-device* | SIBI, alfabet 26 huruf | Ya | Purwarupa penerjemah dua arah |

Dua kelompok penelitian bisa dibaca dari Tabel 2.2. Pengenalan isyarat dan gestur dari Wi-Fi [7], [13] berjalan tanpa kamera tetapi belum menjangkau SIBI, sedangkan riset Indonesia berbasis kamera [5] membuktikan tingginya minat namun tetap terikat pencahayaan dan garis pandang. Dalam batas penelusuran, publikasi pengenalan isyarat SIBI dari CSI maupun purwarupa dua arah yang memadukannya dengan TTS dan ASR bahasa Indonesia pada ESP32-S3 belum ditemukan. Kebaruan penelitian ini karenanya bersifat kombinatif: CSI satu tautan pada sepasang ESP32-S3 untuk alfabet SIBI, distilasi guru-murid, inferensi tepi, dan integrasi dua arah dengan pemrosesan bahasa Indonesia. Di luar itu, kebaruan tidak diklaim untuk pengenalan kontinu maupun penerjemahan kalimat penuh.

## 2.11 Matriks Justifikasi Pemilihan Komponen

Tabel 2.3 merangkum jawaban atas pertanyaan "mengapa X dan bukan Y" untuk tujuh keputusan arsitektur. Seluruh target kinerja di dalamnya adalah target rancangan yang baru diukur pada gerbang BAB III, bukan hasil yang dijanjikan.

Tabel 2.3 Matriks justifikasi pemilihan komponen (Mengapa X dan Bukan Y?)

| No. | Keputusan | Komponen dipilih | Alternatif ditinggalkan | Justifikasi |
|---|---|---|---|---|
| 1 | Tumpukan UI dan server | Seluruhnya Rust: Tokio/Axum, Leptos (WASM), Tauri | Node.js, Streamlit, Electron, React/JS | *Parsing* UDP di bawah 0,2 ms; memori di bawah 40 MB; satu sistem tipe (Subbab 2.8) |
| 2 | Mesin TTS | Kokoro TTS ONNX *on-device*; prasyarat suara Indonesia pada G3; alternatif MMS-TTS-ind [18], [19] | TTS awan, VITS/Tacotron penuh | Model 82 juta parameter diinferensikan luring pada ponsel (Subbab 2.6) |
| 3 | Node penginderaan | ESP32-S3 [8] | ESP32 biasa, C3/C6, Arduino Uno | Instruksi vektor int8; PSRAM penyangga CSI dan model; API CSI resmi (Subbab 2.3) |
| 4 | Penginderaan radio | CSI-Ratio 2,4 GHz kanal 20 MHz [12] | RSSI, radar khusus, *time of flight* | RSSI terlalu kasar; CSI-ratio membersihkan derau fase tanpa perangkat tambahan (Subbab 2.2) |
| 5 | Model guru visi | YOLO26m-Pose 21 *keypoint* [14] | YOLOv8-pose, MediaPipe, UNet | 21 titik artikulasi vital untuk membedakan V/U dan lintasan J/Z; akurasi 97,6% pada pra-penelitian (Subbab 2.4) |
| 6 | Model murid tepi | WiFi-DensePose int8 + 1D-CNN [10] | SVM utama, MLP berat | Int8 berjalan pada modul, target di bawah 100 ms; SVM pembanding (Subbab 2.5) |
| 7 | Metode distilasi | Distilasi visual-ke-Wi-Fi [11] | Pelatihan Wi-Fi murni | CSI abstrak memerlukan supervisi spasial guru; manfaatnya diuji lewat ablasi (Subbab 3.7) |
