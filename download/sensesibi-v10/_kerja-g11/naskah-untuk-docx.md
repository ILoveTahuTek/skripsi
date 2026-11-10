# STUDI KELAYAKAN PURWARUPA SenseSIBI: SISTEM PENERJEMAHAN DUA ARAH HURUF SIBI BERBASIS WI-FI CSI DENGAN INFERENSI ESP32-S3 DAN PEMROSESAN SERVER

**PROPOSAL PENELITIAN**

| Identitas | Keterangan |
|---|---|
| Judul | STUDI KELAYAKAN PURWARUPA SenseSIBI: SISTEM PENERJEMAHAN DUA ARAH HURUF SIBI BERBASIS WI-FI CSI DENGAN INFERENSI ESP32-S3 DAN PEMROSESAN SERVER |
| Jenis dokumen | Proposal penelitian (seminar proposal), BAB I–III + Daftar Pustaka — versi ringkas ±40 halaman |
| Disusun oleh | [PERLU DATA: nama penulis] |
| NIM | [PERLU DATA: NIM penulis] |
| Program studi | [PERLU DATA: program studi] |
| Universitas | [PERLU DATA: nama universitas] |
| Pembimbing | [PERLU DATA: nama pembimbing, bila sudah ditentukan] |
| Tahun | [PERLU DATA: tahun penyusunan] |

> Catatan penyusunan: versi ini menyunting naskah ringkas gelombang 10 mengikuti masukan dosen pembimbing, yaitu register diturunkan ke level mahasiswa D4/S1 dengan kalimat pendek dan emosi manusiawi, konteks masalah ditanamkan di Indonesia tepatnya Jawa Timur, sumber data diutamakan dari Indonesia, daftar pustaka dipangkas dari 93 menjadi 46 entri dengan prioritas sumber Indonesia, dan istilah asing tidak dipaksakan diterjemahkan (misalnya *sandbox*, *on-device*, *fallback* tetap ditulis asing). Kaidah bahasa mengikuti naskah-id (EYD V), gaya memakai humanizer-id (Mode Akademik Ketat) dan sempro-mepet (register korpus sempro). Sitasi ditulis dengan kunci semantik lalu dinomori ulang urut kemunculan sehingga kesalahan pemetaan nomor-sumber yang lolos pada gelombang 10 (antara lain sitasi BRIN/Mursita dan *Kamus SIBI*) ikut terkoreksi. Struktur, tabel, gambar, angka pra-penelitian, dan penanda `[PERLU DATA: ...]` dipertahankan; perencanaan tetap distilasi guru–murid YOLO26m-Pose ke murid CSI untuk inferensi tepi pada ESP32-S3.

---

# BAB I PENDAHULUAN

## 1.1 Latar Belakang

Anak tunarungu umumnya lahir dari orang tua yang mendengar. Sejak hari-hari pertama, komunikasi di rumah menuntut dua arah, tetapi kedua pihak tidak berbagi bahasa: orang tua berbicara dengan suara, anak menjawab dengan isyarat. Orang tua harus mempelajari bahasa isyarat dari nol, sementara kesempatan belajarnya terbatas. Indonesia memiliki sekitar 1,92 juta penyandang tunarungu, sedangkan jumlah juru bahasa isyarat hanya sekitar 500 orang [1]. Artinya, satu juru bahasa harus melayani hampir 4.000 orang. Menunggu juru bahasa jelas bukan pilihan untuk kebutuhan sehari-hari: menceritakan sakit, mengikuti pelajaran, atau sekadar bertanya pada penjual di pasar. Undang-Undang Nomor 8 Tahun 2016 sudah menjamin hak setiap penyandang disabilitas untuk berkomunikasi [2], tetapi jaminan itu berjalan lambat tanpa alat bantu yang benar-benar terjangkau.

Kesenjangan itu paling terasa di ruang kelas. Guru menjelaskan dengan suara; siswa tunarungu menangkap sebagian, menebak sisanya, dan sering kehilangan alur pelajaran. Pada pendidikan formal, pembelajaran memakai SIBI, yaitu sistem isyarat yang bentuknya dibakukan pemerintah dalam *Kamus Sistem Isyarat Bahasa Indonesia* [3]. Penelitian di SLB Negeri Ogan Ilir menunjukkan siswa memakai SIBI dalam pembelajaran, meskipun di luar kelas mereka lebih akrab dengan BISINDO [4]. Temuan serupa dilaporkan Nugraheni dkk. [5] serta Malika dan Berlianti [6]: SIBI hidup di sekolah, sedangkan BISINDO hidup di komunitas. Survei BRIN mencatat 77,7% responden tunarungu memakai BISINDO dan hanya 1,9% memakai SIBI [7]; survei 100 responden tunarungu di Jawa dan Bali melaporkan 91% memakai BISINDO [8]. Kedua survei itu justru menegaskan tempat SIBI berada, yaitu sekolah. Karena tujuan penelitian ini adalah alat bantu pembelajaran, sistem yang dipilih adalah SIBI. Penelitian dilaksanakan bekerja sama dengan sekolah mitra di Jawa Timur [PERLU DATA: nama SLB atau lembaga mitra di Jawa Timur].

Alat bantu komunikasi dua arah memang pernah dicoba, tetapi jalurnya masih setengah jalan. KASIBI mengubah ucapan menjadi teks, lalu menampilkan animasi tangan tiga dimensi [9]. OpenSIBI menganimasikan 50 kosakata SIBI dari teks [10]. Keduanya hanya melayani satu arah: orang pendengar berbicara, sistem menampilkan isyarat. Arah sebaliknya, yaitu isyarat siswa dibaca mesin, belum tersedia sebagai alat yang siap dipakai. Sementara itu, riset pengenalan isyarat di Indonesia bergerak di jalur kamera: pengenalan huruf BISINDO dari citra [11], aplikasi deteksi 24 huruf statis SIBI dengan MediaPipe [12], dan aplikasi Android berbasis *deep learning* [13]. Pendekatan kamera punya dua kendala praktis. Pertama, kamera menuntut pencahayaan dan posisi yang tepat; sedikit saja cahaya berubah, akurasi ikut jatuh. Kedua, kamera yang terus menyala membuat penggunanya merasa diawasi, dan tidak nyaman dipakai sepanjang hari di kelas.

Sinyal Wi-Fi menawarkan jalan lain tanpa kamera. Sinyal Wi-Fi membawa informasi kanal yang disebut *Channel State Information* (CSI) [14]. Ketika tangan bergerak di antara pemancar dan penerima, jalur pantulan sinyal bergeser, dan CSI berubah mengikuti pola gerakan itu. Perubahan itulah yang dibaca untuk mengenali gerak tanpa sensor yang dikenakan di tubuh. Kemampuan ini telah terbukti: SignFi mengenali 276 isyarat *American Sign Language* (ASL) dari CSI [15], DF-WiSLR mengenali 49 gestur tanpa perangkat dikenakan [16], dan WiSign mengenali kalimat ASL dari perangkat Wi-Fi komersial [17]. CSI juga terbukti peka terhadap gerak halus, sampai ke gerakan jari [14]. Namun, penelusuran pada Google Scholar, Crossref, dan OpenAlex hingga Oktober 2026 belum menemukan satu pun penerapan CSI untuk isyarat SIBI.

Alatnya juga sederhana dan murah. Modul ESP32-S3 adalah mikrokontroler sekitar Rp150.000 yang memiliki radio Wi-Fi 2,4 GHz dengan dukungan CSI resmi [18], [19]. Dua modul cukup: satu memancarkan sinyal, satu menangkapnya, dan zona isyarat berada di antara keduanya. Platform terbuka RuView sudah menyediakan *firmware* penangkap CSI yang teruji untuk modul ini [20]. Sepasang node lengkap diperkirakan berbiaya di bawah Rp350.000, jauh lebih murah daripada kamera ditambah komputer pengolah citra. Murah bukan sekadar angka; harga yang terjangkau membuat sekolah berani memasang alat ini di lebih dari satu ruang.

Penelitian ini merancang purwarupa penerjemah dua arah bernama SenseSIBI, singkatan dari *Sensing & Translation of SIBI*. Pada arah pertama, siswa mengisyaratkan huruf; modul menangkap pola CSI, model yang berjalan langsung di modul mengenalinya, teks tampil di layar, lalu dibunyikan sebagai suara. Pada arah kedua, guru menekan tombol dan berbicara; ucapan dikenali menjadi teks, teks tampil di layar, dan bentuk isyaratnya ditampilkan. Model tidak dilatih dari nol. Sebuah model penglihatan bernama YOLO26m-Pose yang sudah terlatih pada data citra SIBI berperan sebagai "guru", sedangkan model Wi-Fi menjadi "murid" yang belajar menirunya melalui distilasi pengetahuan [21]. Guru melihat isyarat lewat kamera hanya saat data direkam; setelah murid lulus, seluruh sistem bekerja tanpa kamera.

Sebagai studi kelayakan, penelitian ini sengaja membatasi klaimnya. Objek pengenalan adalah alfabet manual SIBI satu tangan 26 huruf, yaitu 24 huruf statis ditambah dua huruf gerak J dan Z, bukan penerjemahan kalimat penuh. Penerjemahan bahasa isyarat tingkat kalimat masih menjadi masalah terbuka [22]. Kemampuan membedakan huruf diuji terlebih dahulu sebelum klaim lebih jauh dibuat. Setiap tahap ditutup gerbang keputusan, dan kegagalan tetap dilaporkan sebagai temuan. Dengan batas itu, penelitian ini menjawab pertanyaan yang sederhana dan jujur: apakah sepasang modul Wi-Fi murah benar-benar dapat menjadi jembatan komunikasi dua arah antara siswa tunarungu dan gurunya di kelas.

## 1.2 Rumusan Masalah

Berdasarkan latar belakang yang telah dipaparkan, masalah yang dikaji dalam penelitian ini dirumuskan sebagai berikut.

1. Bagaimana merancang purwarupa penerjemah dua arah yang menghubungkan SIBI dengan teks dan suara bahasa Indonesia berbasis sepasang modul ESP32-S3 yang bekerja tanpa kamera?
2. Bagaimana kinerja pengenalan alfabet manual SIBI dari sinyal CSI serta kinerja kedua jalur penerjemahan pada skenario dalam sesi, lintas partisipan, dan lintas ruang?
3. Bagaimana kelayakan purwarupa sebagai alat bantu komunikasi ditinjau dari latensi, cakupan kosakata, keandalan operasional, penerimaan pengguna, dan biaya?

## 1.3 Tujuan Penelitian

Berdasarkan rumusan masalah tersebut, tujuan penelitian ini adalah:

1. Merancang purwarupa penerjemah dua arah yang menghubungkan SIBI dengan teks dan suara bahasa Indonesia berbasis sepasang modul ESP32-S3 yang bekerja tanpa kamera.
2. Mengukur kinerja pengenalan alfabet manual SIBI dari sinyal CSI serta kinerja kedua jalur penerjemahan pada skenario dalam sesi, lintas partisipan, dan lintas ruang.
3. Menganalisis kelayakan purwarupa sebagai alat bantu komunikasi ditinjau dari latensi, cakupan kosakata, keandalan operasional, penerimaan pengguna, dan biaya.

## 1.4 Batasan Masalah

Ruang lingkup penelitian ini dibatasi sebagai berikut.

1. Objek pengenalan adalah alfabet manual SIBI satu tangan 26 huruf (24 statis serta huruf gerak J dan Z) dengan bentuk baku yang dicocokkan dengan *Kamus SIBI* [3] dan disetujui validator penutur tunarungu; sistem bukan penerjemah kalimat.
2. Bentuk tangan dan jari menjadi pembeda utama; ekspresi wajah dan penanda nonmanual tidak dikenali.
3. Penginderaan memakai sepasang modul ESP32-S3 (satu pemancar dan satu penerima, 2,4 GHz, kanal 20 MHz) dengan layar, baterai, *speaker*, dan mikrofon pada node penerima; kamera hanya dipakai saat perekaman data pelatihan.
4. Model penglihatan YOLO26m-Pose hanya menjadi guru saat akuisisi dan pelatihan; produk akhir bebas kamera dan bebas citra.
5. Sintesis ucapan berjalan *on-device* di ponsel; pengenalan ucapan memakai layanan awan dengan mesin lokal sebagai cadangan; pilihan final ditetapkan pada gerbang G3.
6. Arah kedua dibatasi pada kamus tingkat kata dengan *fallback* ejaan jari; cakupan kamus diukur dan dilaporkan.
7. Setiap sesi melibatkan satu pengisyarat; sistem tidak mengidentifikasi individu; pengujian dilakukan di sedikitnya dua ruang mitra di Jawa Timur yang dikalibrasi.
8. Uji pengguna berskala kecil (3–5 pengguna) dan dianalisis secara deskriptif tanpa statistik inferensial.
9. Penelitian ini tidak membahas isyarat kontinu, tata bahasa isyarat penuh, BISINDO, dan klasifikasi gerakan otomatis dari video.

## 1.5 Manfaat Penelitian

Manfaat penelitian ini dibedakan menjadi manfaat teoretis dan manfaat praktis.

### 1.5.1 Manfaat Teoretis

Penelitian ini memberikan bukti awal apakah CSI dari satu tautan antarmodul ESP32-S3 mampu membedakan alfabet manual SIBI. Bukti itu terikat pada alfabet manual dan belum tentu berlaku untuk isyarat kata maupun kontinu. Penelitian ini juga meninggalkan *dataset* CSI berlabel beserta protokol perekamannya, yang dapat dipakai penelitian berikutnya untuk bahasa isyarat lain, termasuk perluasan ke BISINDO.

### 1.5.2 Manfaat Praktis

Bagi sekolah mitra, penelitian ini memberikan gambaran nyata tentang kelayakan alat bantu komunikasi dua arah berbahasa SIBI, lengkap dengan biaya perangkatnya. Bila seluruh tahap berhasil, dihasilkan purwarupa yang menampilkan teks, menyuarakan isyarat, dan menampilkan bentuk isyarat bagi lawan bicara. Bila berhenti lebih awal, laporan karakterisasi, protokol, dan *dataset* berlabel tetap menjadi warisan penelitian. Bagi keluarga siswa, kosakata yang tervalidasi memastikan isyarat yang tampil benar bentuknya. Bagi komunitas riset, rancangan yang tidak terikat pada satu bahasa isyarat memudahkan replikasi di tempat lain.

## 1.6 Sistematika Penulisan

Proposal ini terdiri atas tiga bab. **BAB I Pendahuluan** memuat latar belakang, rumusan masalah, tujuan, batasan, manfaat, dan sistematika. **BAB II Kajian Pustaka** memuat teori dan penelitian terdahulu yang menjadi dasar perancangan. **BAB III Metode Penelitian** memuat desain, tahapan, waktu dan lokasi, alat dan bahan, perancangan sistem, protokol perekaman, pengolahan sinyal dan pelatihan, skenario pengujian, jadwal, parameter yang ditetapkan kemudian, serta risiko dan cadangan.

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

# BAB III METODE PENELITIAN

## 3.1 Desain Penelitian

Penelitian ini adalah studi kelayakan kuantitatif bergerbang. Bagian kuantitatif mengukur tiga hal: kemampuan CSI dari satu tautan antarmodul ESP32-S3 membedakan 26 huruf alfabet manual SIBI, kemampuan model terkuantisasi berjalan di modul, dan kinerja kedua jalur penerjemahan. Setelah komponen teruji, purwarupa dikemas lalu dinilai melalui uji operasional, uji kegunaan skala kecil, dan penilaian validator penutur tunarungu. Struktur bergerbang dipilih karena satu alasan jujur: belum ada yang membuktikan CSI mampu membedakan isyarat SIBI, jadi kemampuan itu tidak boleh diperlakukan sebagai asumsi. Setiap tahap menghasilkan artefak tetap, kegagalan gerbang dicatat sebagai temuan, dan kriteria akurasi dirumuskan relatif terhadap peluang acak (Subbab 2.9). Inti pelatihannya adalah distilasi guru–murid: keluaran guru kamera YOLO26m-Pose berupa deret 21 *keypoint* dan label menjadi *ground truth* yang mengawasi pelatihan murid ber-*backbone* WiFi-DensePose int8 berkepala 1D-CNN yang berjalan langsung di modul (Subbab 3.7). Rumusan masalah pertama dijawab pada tahap replikasi platform hingga distilasi, kedua pada uji klasifikasi dan *deployment*, ketiga pada uji operasional, kegunaan, dan penilaian validator.

## 3.2 Tahapan Penelitian

Penelitian berlangsung empat belas minggu (M1–M14) dalam enam tahap: replikasi platform dan karakterisasi (T0), kurasi isyarat dan protokol (T1), perekaman *dataset* dan pelatihan guru–murid (T2), uji generalisasi (T3), pengemasan purwarupa dan uji penerimaan (T4), serta analisis dan penulisan (T5). Lima gerbang keputusan menutup rangkaian itu dengan kriteria, ukuran, dan tindakan bila gagal yang dirinci pada Tabel 3.5. G4 menilai penerimaan pengguna dan biaya, lalu menyusun rekomendasi posisi TKT/TRL 3–4 [45]. Jalur lolos dirangkum pada Gambar 3.1. Bila G0 gagal dua kali, jalur CSI dihentikan dan dilaporkan sebagai temuan; kriteria seluruh gerbang difinalkan bersama pembimbing sebelum dinilai dan dihimpun pada Tabel 3.7.

```mermaid
flowchart LR
    subgraph KA[" "]
        direction TB
        T0["T0 Replikasi platform, verifikasi<br/>CSI 56 subcarrier pada 1 m,<br/>uji Delta-CSI, koeksistensi (M1–M2)"]
        G0("G0 akhir M2: baseline CSI-jaringan:<br/>UDP Rust tanpa kehilangan paket,<br/>akuisisi stabil, gerak terpisah")
        T1["T1 Kurasi isyarat, kalibrasi ruang,<br/>protokol, etika, rintisan separabilitas<br/>pasangan huruf mirip (M2–M4)"]
        T2["T2 Perekaman dataset dan<br/>pelatihan guru–murid<br/>(M4–M8)"]
        T0 --> G0
        G0 -- "lolos" --> T1
        T1 --> T2
    end
    subgraph KB[" "]
        direction TB
        T2B["Kuantisasi int8 dan uji<br/>deployment murid ke<br/>modul ESP32-S3"]
        G1("G1 akhir M8: model tepi int8:<br/>akurasi skema dan inferensi<br/>di bawah 100 ms")
        T3["T3 Uji generalisasi: lintas sesi,<br/>partisipan, ruang, posisi<br/>berdiri/duduk (M8–M10)"]
        G2("G2 akhir M10: konsultasi 3 pilar<br/>pakar SIBI, RF, embedded AI<br/>tanpa temuan blok kritis")
        T4["T4 Pengemasan dua arah, full-stack<br/>Rust, TTS on-device, uji penerimaan<br/>dan biaya (M10–M12)"]
        G3("G3 M11: integrasi Rust dan mesin<br/>ucapan on-device dalam<br/>anggaran latensi")
        G4("G4 akhir M12: sintesis kelayakan,<br/>penerimaan dan biaya layak,<br/>rekomendasi TKT/TRL 3–4")
        T5["T5 Analisis dan penulisan<br/>(M12–M14)"]
        T2B --> G1
        G1 -- "lolos" --> T3
        T3 --> G2
        G2 -- "lolos" --> T4
        T4 --> G3
        G3 -- "lolos" --> G4
        G4 -- "lolos" --> T5
    end
    KA --> KB
```

Gambar 3.1 Tahapan penelitian T0–T5 dan gerbang keputusan G0–G4 (jalur lolos; tindakan bila gagal pada Tabel 3.5)

Tahap T0–T2 membangun dasar data. T0 menyiapkan dua modul dengan *firmware* `esp32-csi-node` RuView [20] dan menjalankan empat uji tanpa partisipan: verifikasi 56 *subcarrier* terbaca stabil pada jarak baku 1 meter, uji Delta-CSI (Subbab 3.8.1) untuk memisahkan pola CSI saat bergerak dari saat diam, uji koeksistensi radio dengan *streaming* audio aktif, dan pengukuran laju pencuplikan. T1 mencakup kurasi 26 huruf bersama validator, kalibrasi ruang, protokol dan etika, serta perizinan (Subbab 3.6); pasangan huruf paling mirip ditetapkan di sini sebagai bahan gerbang G1.

T2 merekam *dataset* kurang lebih 30 repetisi per isyarat per sesi disertai video tersinkron (Subbab 3.6). Alur pelatihannya berbentuk distilasi: segmen disaring lewat *keypoint* guru, guru menjalani pelatihan lanjutan pada data visual SIBI di GPU Kaggle, jendela CSI disandingkan dengan *ground truth* guru berdasarkan penanda waktu, murid dilatih dengan supervisi label dan deret pose guru, lalu model terpilih dikuantisasi int8 dan di-*deploy* (Subbab 3.7). Keluaran T2 adalah *dataset* berlabel, model terlatih, dan laporan *deployment*; G1 menilai hasilnya, dan bila gagal, cakupan dipangkas menjadi himpunan huruf dengan pembeda CSI terkuat (Tabel 3.7).

Tahap T3–T5 menguji dan melaporkan. T3 menguji generalisasi lintas sesi, partisipan, ruang, dan posisi berdiri-duduk, termasuk satu pengguna baru tanpa pelatihan ulang (Subbab 3.7) dengan acuan Widar3.0 [27]; bila ketahanan lintas pengguna rendah, cakupan menjadi personalisasi per pengguna dan dilaporkan sebagai temuan. T4 mengemas model menjadi purwarupa dua arah (Subbab 3.5), menjalankan uji operasional dan jalur ucapan (Subbab 3.8) yang dinilai G3, lalu ditutup uji penerimaan, penilaian validator, dan analisis biaya yang dinilai G4. T5 menganalisis seluruh artefak dan menyusun laporan kelayakan dengan rekomendasi TKT/TRL 3–4 [45] beserta keterbatasan eksplisit (Subbab 1.4).

## 3.3 Waktu dan Lokasi Penelitian

Penelitian dilaksanakan pada [PERLU DATA: bulan dan tahun pelaksanaan penelitian] di Jawa Timur, bekerja sama dengan [PERLU DATA: nama SLB atau lembaga mitra di Jawa Timur]. Perekaman dan pengujian dilakukan di sedikitnya dua ruang, jumlah minimum skema *leave-one-room-out*, dan setiap ruang dikalibrasi sebelum perekaman (Subbab 3.5).

## 3.4 Alat dan Bahan

Perangkat keras dan perangkat lunak penelitian disajikan pada Tabel 3.1 dan Tabel 3.2. Sepasang modul ESP32-S3 menjadi node penginderaan: TX memancarkan *beacon* ESP-NOW, sedangkan RX mengekstrak CSI 56 *subcarrier* pada 2,4 GHz kanal 20 MHz sekaligus memuat antarmuka. Versi perangkat lunak dicatat bersama log pelatihan agar eksperimen dapat diulang. Bahan penelitian meliputi *dataset* CSI beserta deret pose guru hasil perekaman sendiri, kode dan data pelatihan model guru dari repositori peneliti, lembar definisi huruf, aset tampilan arah kedua, formulir persetujuan, instrumen uji, dan kuesioner persepsi. *Dataset* direkam sendiri karena pengenalan isyarat SIBI dari CSI belum ditemukan dalam penelusuran (Subbab 2.10).

Tabel 3.1 Perangkat keras penelitian

| No. | Nama | Spesifikasi | Jumlah | Keterangan |
|---|---|---|---|---|
| 1 | Modul ESP32-S3 | PSRAM 8 MB; 2,4 GHz 802.11b/g/n, kanal 20 MHz (56 *subcarrier*), 1T1R; varian yang direkomendasikan RuView [20] | 2 unit | Node TX (pemancar *beacon*) dan node RX (penerima CSI dan antarmuka) |
| 2 | Layar modul | OLED 0,96 inci I2C (128×64) atau TFT 1,3 inci SPI (240×240) [PERLU DATA: model final] | 1 unit | Tampilan huruf, baterai, kanal, mode kerja |
| 3 | *Rotary encoder* EC11 dan tombol tekan | Putar 360 derajat, 20 detak per putaran, tombol terintegrasi; sakelar sesaat *pull-up* internal | 1–2 unit | Navigasi menu, sensitivitas, tekan-untuk-bicara, reset |
| 4 | Pengeras suara dengan DAC I2S | Mini 8 Ohm 3 W, penguat kelas D MAX98357A | 1 set | Pemutaran suara TTS dari modul |
| 5 | Mikrofon I2S | INMP441, MEMS omnidireksional, SNR 61 dBA | 1 unit | Pintu suara arah kedua |
| 6 | Baterai Li-Po, BMS 1S, pengisi TP4056 | Li-Po 3,7 V 2.500–3.000 mAh [PERLU DATA: kapasitas final berdasarkan uji arus]; proteksi; pengisi 1 A USB-C | 1–2 set | Daya portabel, proteksi, dan pengisian |
| 7 | Laptop | ASUS TUF Dash F15 FX516PR: i7-11370H, RTX 3070 Laptop 8 GB VRAM, RAM 16 GB | 1 unit | Akuisisi jalur guru, pengembangan, pelatihan, server cadangan |
| 8 | Ponsel pintar | Poco F4 5G: Snapdragon 870, RAM 6 GB, Android | 1 unit | *Hotspot* portabel, klien Tauri, mesin TTS *on-device* |
| 9 | *Access point* | *Router* Wi-Fi 2,4 GHz dengan internet [PERLU DATA: pilihan final] | 1 unit | Jembatan jaringan dan penjangkar kanal, bukan penginderaan |
| 10 | *Webcam* | Bawaan laptop | 1 unit | Hanya untuk jalur guru |

Tabel 3.2 Perangkat lunak penelitian

| No. | Nama | Fungsi dalam penelitian |
|---|---|---|
| 1 | *Firmware* dan *server* RuView [20] | Menangkap CSI, mengirim UDP, kalibrasi ruang, segmentasi |
| 2 | `scripts/collect-ground-truth.py` (diadaptasi) | Sinkron kamera–CSI; estimator diganti YOLO26m-Pose |
| 3 | Model guru YOLO26m-Pose dan repositori alur kerja YOLO26 peneliti [29] | Ekstraksi *keypoint*; konversi *dataset*, pelatihan deterministik, pencatatan eksperimen (Subbab 3.7) |
| 4 | Layanan GPU Kaggle dan model WiFi-DensePose terpralatih [20] | Pelatihan guru dan murid; inisialisasi *backbone* murid |
| 5 | Python, scikit-learn, PyTorch | Ekstraksi fitur, pelatihan SVM dan murid, evaluasi |
| 6 | ESP-DL dengan akselerasi ESP-NN (alternatif: TensorFlow Lite Micro) [33], [32], [34] | Menjalankan murid int8 pada node RX |
| 7 | faster-whisper dan MMS-TTS-ind [40], [38]; layanan ucapan awan [PERLU DATA: layanan final hasil uji banding] | ASR dan TTS cadangan lokal; jalur utama pengenalan ucapan |
| 8 | Rust, Tokio, Axum, Leptos, Tauri [41], [42], [43], [44] | Server purna Rust, dasbor WASM, aplikasi klien ponsel |
| 9 | Kokoro TTS ONNX dan ONNX Runtime [36], [37] | Mesin TTS *on-device*; prasyarat suara Indonesia pada G3 |
| 10 | Kamus label-teks dan teks-isyarat | Dikembangkan sendiri; kamus label-teks dimuat pada modul |

## 3.5 Perancangan Sistem

Sistem bekerja dalam dua jalur operasional tanpa kamera dan satu jalur guru yang hanya aktif saat akuisisi dan pelatihan, seperti ditunjukkan pada Gambar 3.2. Pada arah pertama, *beacon* ESP-NOW dari node pemancar melewati zona isyarat; gerak pengisyarat mengubah deret CSI yang ditangkap node penerima; model murid int8 menghasilkan label beserta skor keyakinan; label dipetakan menjadi teks Indonesia, tampil di layar, lalu dikirim ke aplikasi Tauri pada ponsel yang menyuarakannya lewat Kokoro TTS ONNX secara luring. Pada arah kedua, tombol tekan-untuk-bicara mengaktifkan mikrofon; ucapan dikenali layanan ASR, teks tampil di layar, lalu dipetakan ke representasi SIBI dari aset modul (Subbab 2.7). Saat internet terputus, sintesis tetap berjalan *on-device* dan ASR beralih ke server lokal faster-whisper. Jalur guru memakai *webcam* dan YOLO26m-Pose untuk mengekstrak deret *keypoint* sebagai supervisi pelatihan; jalur ini bukan bagian produk akhir.

```mermaid
flowchart TD
    TX["Node TX: beacon<br/>ESP-NOW"]
    ZN["Zona isyarat<br/>(satu pengisyarat)"]
    RX["Node RX: CSI promiscuous +<br/>inferensi murid int8 +<br/>antarmuka pengguna"]
    MAPL["Kamus label–teks<br/>di modul"]
    DSP1["Layar modul:<br/>teks hasil"]
    TTS["Mesin TTS on-device:<br/>Kokoro ONNX di aplikasi<br/>Tauri (Poco F4 5G)"]
    SPK["Speaker +<br/>rotary encoder"]
    TX --> ZN
    ZN --> RX
    RX --> MAPL
    MAPL --> DSP1
    MAPL -- "teks via Wi-Fi" --> TTS
    TTS -- "audio" --> SPK

    BTN["Tombol<br/>tekan-untuk-bicara"]
    MIC["Mikrofon<br/>I2S"]
    STT["Layanan<br/>ASR awan"]
    DSP2["Layar modul: teks lalu<br/>representasi SIBI"]
    AST["Aset SIBI: glos,<br/>gambar, ejaan jari<br/>(Subbab 2.7)"]
    BTN --> MIC
    MIC -- "audio via Wi-Fi" --> STT
    STT -- "teks" --> DSP2
    AST --> DSP2

    CAM["Webcam laptop"]
    Y26P["YOLO26m-Pose:<br/>21 keypoint pose tangan"]
    SUP["Supervisi pelatihan<br/>murid (Subbab 3.7)"]
    CAM --> Y26P
    Y26P --> SUP

    LOK["Server lokal (cadangan):<br/>ASR faster-whisper,<br/>TTS MMS, server RuView,<br/>server Rust"]
    TTS -. "TTS lokal" .-> LOK
    STT -. "ASR lokal" .-> LOK
```

Gambar 3.2 Arsitektur produk akhir tanpa kamera. Rantai kiri = arah 1 (isyarat menjadi teks dan suara); rantai tengah = arah 2 (ucapan menjadi representasi SIBI); rantai kanan = jalur guru yang hanya aktif saat akuisisi dan pelatihan; garis putus-putus = beralih ke server lokal ketika internet tidak tersedia.

Pada topologi jaringan, seluruh perangkat terhubung ke satu *access point* pada kanal yang sama sehingga penangkapan CSI dan komunikasi data berjalan serentak (Subbab 2.3). Node pemancar memancarkan *beacon* sebagai sumber bingkai CSI; node penerima mengirim bingkai, label, dan skor melalui UDP kepada server Rust sebagai telemetri riset; server lokal menjalankan server RuView, server Rust, faster-whisper, dan MMS-TTS-ind sebagai jalur cadangan.

Kedua modul dipasang setinggi dada dan mengapit zona isyarat; kesesuaiannya diperiksa lewat uji Delta-CSI. Zona hanya ditempati satu pengisyarat per sesi, sistem tidak mengidentifikasi individu, dan jarak antarmodul (baku 1 meter) ditetapkan pada T0 serta dicatat dalam metadata sesi (Tabel 3.7). Setiap sesi diawali kalibrasi ruang bawaan RuView selama kurang lebih empat menit dengan 600 bingkai dan 8 *anchor* karena CSI peka terhadap perubahan ruang [20], [27]; posisi perabot, pendingin ruangan, dan orang yang lewat dicatat sebagai kovariat analisis.

Node penerima dikemas dalam *enclosure* cetak tiga dimensi bahan PLA atau ABS yang menampung papan, baterai, BMS, TP4056, dan seluruh antarmuka: layar, pengeras suara, dan mikrofon pada muka depan atau atas, *rotary encoder* dan tombol pada samping, port USB-C pada bawah; node pemancar dikemas serupa tanpa antarmuka. Pemetaan pin GPIO pada Tabel 3.3 dipilih agar tidak menabrak pin *strapping* (GPIO 0, 3, 45, 46) maupun kanal USB bawaan papan [18]; penetapan pin diverifikasi ulang pada T0. Rantai daya terdiri atas baterai, BMS 1S, TP4056, dan regulator 3,3 volt papan; tegangan baterai diukur melalui pembagi tegangan sehingga persentase baterai tampil di layar. [PERLU DATA: berkas model enclosure final] [PERLU ILUSTRASI: foto atau render enclosure dan tata letak komponennya]

Tabel 3.3 Matriks pinout wiring GPIO node penerima

| No. | Subsistem | Pin modul | GPIO ESP32-S3 | Fungsi |
|---|---|---|---|---|
| 1 | Layar I2C (OLED) | SDA / SCL | GPIO 8 / GPIO 9 | Jalur data dan *clock* bus I2C |
| 2 | *Rotary encoder* EC11 | CLK (A) / DT (B) / SW | GPIO 10 / GPIO 11 / GPIO 12 | Detak, arah putaran, tombol |
| 3 | Tombol tekan | OUT | GPIO 13 | Tekan-untuk-bicara dan reset; *pull-up* internal |
| 4 | Mikrofon INMP441 | SCK / WS / SD | GPIO 14 / GPIO 15 / GPIO 16 | *Clock*, *word select*, data I2S penerima |
| 5 | DAC MAX98357A | BCLK / LRC / DIN | GPIO 17 / GPIO 18 / GPIO 21 | *Clock*, penanda kiri-kanan, data I2S pengirim |
| 6 | Pemantau tegangan baterai | ADC | GPIO 1 (ADC1_CH0) | Keluaran pembagi tegangan baterai |

Perangkat lunak ditulis purna Rust (Subbab 2.8): Tokio menjalankan pendengar UDP bingkai CSI [41], Axum menyediakan HTTP dan WebSocket bagi dasbor Leptos WASM [42], [43], dan aplikasi Tauri pada ponsel menerima teks hasil isyarat serta menjalankan Kokoro TTS ONNX [44], [36]. Target *parsing* bingkai di bawah 0,2 ms dan memori server di bawah 40 MB diukur pada G3 (Subbab 3.8.3). Mesin sintesis berjalan sepenuhnya di ponsel: Kokoro-82M ONNX diinferensikan luring lewat ONNX Runtime di dalam Tauri [35], [37], dengan target inferensi frasa pendek di bawah 100 ms pada Snapdragon 870. Prasyaratnya satu, yaitu suara bahasa Indonesia pada Kokoro; bila belum tersedia, mesin *on-device* beralih ke MMS-TTS-ind [38] dan peralihan itu dilaporkan.

## 3.6 Protokol Perekaman Dataset, Partisipan, dan Etika

Partisipan terdiri atas 3–4 pengisyarat kompeten, sedikitnya satu validator penutur tunarungu, serta 3–5 pengguna uji dari kelompok sasaran (guru, siswa tunarungu, wali murid). Setiap pengisyarat direkam dalam sedikitnya dua sesi agar skema lintas sesi dapat dijalankan. Kurasi isyarat mengacu pada *Kamus SIBI* [3]: lembar definisi memuat konfigurasi tangan-jari serta lintasan J dan Z, validator menyetujuinya, dan pasangan huruf paling mirip ditetapkan sebagai bahan G1; kosakata tampilan arah kedua mencakup 26 huruf, 9 angka, serta kata terpilih [10]. Perekaman memakai *elisitasi* terisolasi, satu huruf per segmen dengan jeda antarrepetisi: huruf statis diperagakan sebagai pose yang ditahan sejenak, sedangkan J dan Z diperagakan sebagai lintasan gerak. Prosedur perekaman setiap sesi adalah sebagai berikut.

1. Menyiapkan peralatan yang digunakan.
2. Memasang modul pemancar dan penerima, lalu menghubungkan seluruh perangkat ke *access point* pada satu kanal.
3. Menjalankan kalibrasi ruang dan mencatat metadata sesi, yaitu tanggal, ruang, kode pengisyarat, posisi modul, dan kondisi latar.
4. Menjalankan `scripts/collect-ground-truth.py` agar perekaman CSI dan *webcam* sinkron.
5. Menampilkan kartu pemandu huruf target, merekam satu repetisi, memberi jeda, dan mengulanginya hingga setiap huruf mencapai kurang lebih 30 repetisi.
6. Membuang segmen bila tangan tidak terdeteksi model guru, terjadi *jitter* *keypoint* ekstrem, atau segmen terpotong, lalu mencatat tingkat segmen terbuang.
7. Meminta validator mengambil sampel segmen untuk memeriksa kebenaran bentuk isyarat.

Perekaman dimulai setelah persetujuan lembaga mitra dan persetujuan tertulis setiap partisipan diperoleh [PERLU DATA: lembaga atau komisi pemberi persetujuan etik]; partisipan berhak mengundurkan diri kapan saja. Formulir persetujuan menyatakan bahwa kamera hanya menyala pada sesi akuisisi jalur guru, produk akhir bebas kamera, dan mode privasi RuView aktif. Video hanya dipakai untuk verifikasi batas segmen, penyaringan kualitas, dan diagnosis; disimpan terbatas dan tidak dipublikasikan. Audio arah kedua dikirim ke layanan awan sehingga tujuannya diungkapkan pada formulir dan kebijakan penyimpanan layanan diperiksa sebelum dipakai. *Dataset* publik hanya memuat CSI, label, dan *keypoint* tanpa identitas.

## 3.7 Pengolahan Sinyal, Ekstraksi Fitur, Pelatihan Guru–Murid, dan Deployment

*Firmware* RuView membatasi bingkai CSI paling sering setiap 20 ms atau 50 bingkai per detik [20]; laju aktual diukur pada T0, dan pita Doppler yang dianalisis dibatasi hingga setengah laju aktual bila terukur lebih rendah. Deret CSI dipotong menjadi segmen huruf dengan segmentasi energi gerak RuView [20]; J dan Z terpotong jelas dari energinya, sedangkan huruf statis memakai jendela tahan pose yang ambang dan panjangnya ditetapkan pada Tabel 3.7. Fitur tiap segmen terdiri atas amplitudo dan fase *subcarrier* terpilih serta spektrum Doppler [14], [27]; fitur diringkas menjadi vektor untuk SVM dan deret waktu untuk 1D-CNN.

Model guru YOLO26m-Pose menjalani pelatihan lanjutan pada data visual SIBI hasil T2 di layanan server GPU Kaggle. Pelatihan tidak dibangun dari nol karena repositori peneliti (Tabel 3.2) memuat alur kerja YOLO26 lengkap yang teruji [29]. Sembilan eksperimen tercatat menghasilkan model juara *pose* mAP50 0,8944 pada 49 kelas (25 huruf dan 24 kata), dan eksperimen lanjutan pada 24 huruf statis mencapai mAP50 0,9580 dengan akurasi huruf 97,6%. Sebelum dipakai, kualitas guru dievaluasi dari proporsi bingkai tangan terdeteksi, *jitter* *keypoint*, dan pemeriksaan sampel (Tabel 3.7); selama akuisisi, kartu pemandu protokol menentukan huruf per repetisi sehingga label guru dapat dicocokkan dengan perintah protokol.

*Dataset* murid dibentuk dengan menyelaraskan tiga deret berdasarkan penanda waktu: jendela CSI hasil segmentasi, label huruf guru, dan deret pose guru. Murid ber-*backbone* WiFi-DensePose int8 yang diinisialisasi dari model terpralatih RuView [20], [28] dengan kepala 1D-CNN dilatih pada GPU Kaggle memakai kerugian gabungan: kerugian klasifikasi ditambah suku supervisi guru. Suku itu mengikat representasi murid pada deret pose guru [21]. Dua pembanding dilatih pada data yang sama, yaitu SVM atas fitur ringkas [30] dan murid ablasi tanpa suku supervisi guru sehingga manfaat supervisi dinilai langsung dari data. Setelah pelatihan, murid memprediksi kelas dari jendela CSI saja, tanpa kamera.

Kinerja diukur dengan enam skema pada Tabel 3.4; skema dalam sesi memakai pembagian temporal per blok tanpa pembagian acak. Data validasi hanya berasal dari data latih sehingga data uji tidak pernah dipakai memilih *subcarrier*, menormalkan fitur, atau menetapkan ambang (Tabel 3.7).

Tabel 3.4 Skema pembagian data

| No. | Skema | Data latih | Data uji | Aspek yang diukur |
|---|---|---|---|---|
| 1 | Dalam sesi (blok temporal) | Blok awal satu sesi | Blok akhir sesi yang sama | Separabilitas orang, ruang, sesi sama |
| 2 | Lintas sesi | Sebagian sesi pengisyarat di satu ruang | Sesi lain, ruang sama | Ketahanan antarsesi |
| 3 | Lintas partisipan (*leave-one-subject-out*) | Semua pengisyarat kecuali satu | Pengisyarat yang ditinggalkan, bergiliran | Ketahanan pergantian orang |
| 4 | Lintas ruang (*leave-one-room-out*) | Semua ruang kecuali satu | Ruang yang ditinggalkan, bergiliran | Ketahanan pergantian ruang |
| 5 | Pengguna baru | Seluruh pengisyarat | Satu pengguna baru tanpa pelatihan ulang | Kesiapan orang baru |
| 6 | Lintas posisi | Posisi berdiri (atau sebaliknya) | Posisi duduk | Ketahanan pergeseran posisi |

Keluaran klasifikator dilengkapi skor keyakinan dan mekanisme penolakan [31]; segmen di bawah ambang menghasilkan status penolakan pada kedua arah, yaitu *speaker* tidak mengucapkan apa pun dan layar menampilkan pesan isyarat tidak dikenali. Penolakan lebih aman daripada menebak kelas salah; ambangnya ditetapkan dari data validasi dan kecukupannya diperiksa melalui laju deteksi palsu serta penilaian validator (Subbab 3.8).

Model terpilih dikuantisasi int8 lalu dijalankan pada modul penerima melalui ESP-DL dengan akselerasi ESP-NN dan penyangga PSRAM [33], [32]; TensorFlow Lite Micro menjadi alternatif [34], dan radio terikat satu kanal bersama *access point* dengan *power save* dimatikan [20]. Alur inferensi pada perangkat ditunjukkan pada Gambar 3.3: bingkai *promiscuous* masuk ke penyangga geser, segmen terdeteksi dari energi gerak, fitur dihitung, model int8 menghasilkan kelas dan skor, dan keluaran di atas ambang dikirim melalui UDP. Waktu inferensi per segmen, pemakaian memori, dan pengaruhnya pada laju pemrosesan diukur dan dilaporkan; bila model terlalu berat, klasifikasi dipindahkan ke server sesuai jalur cadangan (Subbab 3.11).

```mermaid
flowchart LR
    subgraph R1[" "]
        direction TB
        CSI["Callback CSI,<br/>mode promiscuous,<br/>filter MGMT"]
        BUF["Penyangga geser<br/>CSI di PSRAM"]
        SEG["Segmentasi energi<br/>gerak (perangkat)"]
        FT["Fitur ringkas:<br/>Doppler, amplitudo/fase"]
        CSI --> BUF
        BUF --> SEG
        SEG --> FT
    end
    subgraph R2[" "]
        direction TB
        MOD["Model murid int8:<br/>backbone WiFi-DensePose +<br/>kepala 1D-CNN, 26 kelas"]
        DEC{"Skor keyakinan<br/>di atas ambang?"}
        OUT["Label + skor<br/>dikirim via UDP"]
        RJ["Label ditolak:<br/>isyarat tidak dikenali"]
        MOD --> DEC
        DEC -- "ya" --> OUT
        DEC -- "tidak" --> RJ
    end
    R1 --> R2
```

Gambar 3.3 Inferensi langsung pada ESP32-S3

## 3.8 Skenario Pengujian dan Metrik Evaluasi

Uji Delta-CSI dan koeksistensi mendasari G0, uji klasifikasi dan *deployment* mendasari G1, konsultasi tiga pilar mendasari G2, uji operasional dan jalur ucapan mendasari G3, serta uji kegunaan, penilaian validator, dan analisis biaya mendasari G4. Uji cakupan kamus melengkapi analisis tanpa menjadi syarat gerbang.

### 3.8.1 Uji Delta-CSI dan Koeksistensi

Uji Delta-CSI menjawab satu pertanyaan: apakah gerak tubuh menghasilkan perubahan CSI yang terpisah jelas dari kondisi tanpa gerak (ukuran keterpisahan pada Tabel 3.7). Prosedurnya adalah sebagai berikut.

1. Memasang kedua modul pada posisi awal yang mengapit zona isyarat.
2. Merekam CSI pada kondisi ruang kosong, pengisyarat diam, dan pengisyarat bergerak.
3. Menjalankan modul penerima dengan CSI, koneksi *station*, dan UDP serentak, termasuk saat *streaming* audio, lalu mencatat laju CSI aktual dan paket hilang.
4. Membandingkan pola antarkondisi, lalu mencatat dan menganalisis hasilnya sebagai bahan G0.

### 3.8.2 Uji Klasifikasi

Uji klasifikasi pada keenam skema memakai metrik Subbab 2.9, selalu dibandingkan dengan peluang acak sekitar 3,8% untuk 26 kelas dan dihitung ulang bila cakupan dipangkas. Akurasi dilaporkan tanpa penolakan (seluruh segmen uji) dan dengan penolakan (segmen diterima); murid ablasi dilaporkan berdampingan dengan murid utama dan SVM.

### 3.8.3 Uji Operasional

Uji operasional mengukur deteksi palsu per jam tanpa peragaan, latensi ujung ke ujung tiap arah, dan konsumsi arus modul. Prosedurnya adalah sebagai berikut.

1. Menjalankan purwarupa di ruang terkalibrasi.
2. Merekam kondisi tanpa peragaan, termasuk saat orang lewat dan kipas menyala, lalu mencatat isyarat yang terdeteksi.
3. Meminta pengisyarat memperagakan isyarat target dan mencatat waktu selesainya isyarat serta suara terdengar; pada arah kedua, mengucapkan frasa uji dan mencatat waktu representasi tampil.
4. Mengukur arus modul pada beberapa kondisi kerja, lalu menghitung estimasi ketahanan baterai.
5. Menghitung biaya purwarupa dari harga komponen dan perkiraan biaya layanan ucapan per jam pemakaian.
6. Menganalisis deteksi palsu, latensi kedua arah, dan ketahanan baterai terhadap indikator layak (Tabel 3.7).

### 3.8.4 Uji Jalur Ucapan dan Cakupan Kamus

Uji jalur ucapan menilai komponen bahasa kedua arah dengan membandingkan jalur *on-device*, awan, dan server lokal, disertai cakupan kamus arah kedua. Prosedurnya adalah sebagai berikut.

1. Menyiapkan daftar frasa uji pendek berbahasa Indonesia [PERLU DATA: daftar frasa uji dan jumlah penutur] yang mencakup kata dalam dan di luar kamus.
2. Merekam teks hasil layanan ASR awan, lalu menghitung akurasi kata terhadap teks acuan.
3. Mengukur waktu pengenalan, pemetaan, inferensi TTS *on-device*, dan total ujung ke ujung kedua arah.
4. Mengulang pengukuran pada kedua kandidat mesin *on-device* (Kokoro ONNX dan MMS-TTS-ind) serta jalur pembanding awan dan server lokal, lalu membandingkan mutu dan latensi.
5. Memverifikasi prasyarat suara Indonesia serta mengukur *parsing* UDP dan memori server Rust (Subbab 2.8).
6. Mencatat proporsi kata uji yang tampil sebagai representasi isyarat, ejaan jari, dan gagal tampil, lalu menganalisis mutu, latensi, dan ketergantungan internet sebagai bahan keputusan G3 (Tabel 3.7).

### 3.8.5 Uji Kegunaan dan Penilaian Validator

Uji kegunaan dengan 3–5 pengguna kelompok sasaran menelaah keterpakaian purwarupa pada skenario tugas terbimbing, yaitu saling menyampaikan pesan pendek melalui ejaan huruf dan kosakata tampilan. Langkah uji tiap pengguna adalah sebagai berikut.

1. Menjelaskan tujuan uji, batas kosakata, kondisi kamera tidak menyala, dan hak mundur, lalu meminta persetujuan tertulis.
2. Memberi waktu berlatih singkat dengan kamus tampilan.
3. Menjalankan tugas komunikasi dua arah, mencatat keberhasilan, waktu penyelesaian, dan keluaran menyesatkan.
4. Meminta pengguna mengisi kuesioner skala Likert [46] tentang kegunaan, kejelasan, dan keinginan memakai ulang.
5. Merekapitulasi hasil, lalu menganalisis secara deskriptif tanpa klaim kausal.

Validator penutur tunarungu menilai kewajaran keluaran kedua arah; keluaran sistem dan penilaian independen dicatat dalam tabel silang, dan kasus yang dinilai keliru dilaporkan tersendiri. Sebagai analisis sekunder, kesalahan klasifikator dikaitkan luring dengan kemiripan pose pada deret *keypoint* guru untuk membedakan kesalahan konfigurasi mirip dari kesalahan sinyal lemah.

### 3.8.6 Kriteria Gerbang Keputusan

Kriteria tiap gerbang dan tindakan bila gagal disajikan pada Tabel 3.5. Kelayakan pada rumusan ketiga ditinjau per dimensi, bukan dari lolosnya G4 semata, dan ambang kuantitatif difinalkan bersama pembimbing sebelum gerbang dinilai.

Tabel 3.5 Kriteria gerbang keputusan

| Gerbang | Nama dan waktu | Kriteria lolos (ambang usulan) | Tindakan bila gagal |
|---|---|---|---|
| G0 | Baseline CSI dan jaringan, akhir M2 | Akuisisi 56 *subcarrier* 1 m ke UDP Rust terbaca stabil; laju sekurang-kurangnya 25 bingkai per detik; paket hilang tidak melampaui 0,1%; pola bergerak terpisah dari diam | Perbaikan penempatan satu kali; gagal lagi berarti jalur CSI dihentikan dan dilaporkan |
| G1 | Model tepi int8 dan distilasi, akhir M8 | Akurasi dalam sesi sekurang-kurangnya 50% (sekitar 13 kali acak 3,8%) dan melampaui SVM; inferensi int8 di bawah 100 ms; pembanding ablasi dilaporkan | Pangkas himpunan huruf pembeda terkuat, lalu nilai ulang |
| G2 | Tiga pilar pakar, akhir M10 | Penilaian tertulis pakar SIBI-aksesibilitas, RF-*wireless sensing*, dan *embedded AI* masuk semua; tanpa temuan blok kritis; skor rata-rata per pilar sekurang-kurangnya 3 dari 5 | Perbaiki temuan blok atau sempitkan klaim, lalu nilai ulang |
| G3 | Integrasi Rust dan mesin ucapan, M11 | Latensi arah 1 tidak melampaui 2 detik dan arah 2 tidak melampaui 3 detik pada jalur *on-device* (5 detik cadangan); TTS di bawah 100 ms; *parsing* UDP di bawah 0,2 ms; memori server di bawah 40 MB; suara Indonesia tersedia atau peralihan dilaporkan | Beralih ke mesin *on-device* alternatif, lalu server lokal atau awan; melampaui berarti temuan |
| G4 | Sintesis kelayakan, akhir M12 | Skor persepsi rata-rata sekurang-kurangnya 3,0 dari 5; validator menyetujui kewajaran; biaya lengkap; rekomendasi TKT/TRL 3–4 tertulis | Hasil negatif tetap dilaporkan; rekomendasi menyatakan posisi lebih rendah beserta alasan |

## 3.9 Jadwal Penelitian

Jadwal empat belas minggu disajikan pada Tabel 3.6; tanda ■ menunjukkan minggu pelaksanaan.

Tabel 3.6 Jadwal penelitian

| No. | Kegiatan | M1 | M2 | M3 | M4 | M5 | M6 | M7 | M8 | M9 | M10 | M11 | M12 | M13 | M14 | Gerbang |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | T0 Replikasi platform, uji Delta-CSI, dan koeksistensi | ■ | ■ | | | | | | | | | | | | | G0 (akhir M2) |
| 2 | T1 Kurasi alfabet SIBI dan kosakata, kalibrasi ruang, protokol, perizinan | | ■ | ■ | ■ | | | | | | | | | | | — |
| 3 | T2 Perekaman *dataset*, pelatihan guru–murid, kuantisasi, uji *deployment* | | | | ■ | ■ | ■ | ■ | ■ | | | | | | | G1 (akhir M8) |
| 4 | T3 Uji lintas sesi, partisipan, ruang, dan pengguna baru | | | | | | | | ■ | ■ | ■ | | | | | G2 (akhir M10) |
| 5 | T4 Pengemasan dua arah, Rust, TTS *on-device*, uji operasional, jalur ucapan, kamus, kegunaan, validator | | | | | | | | | | ■ | ■ | ■ | | | G3 (M11), G4 (akhir M12) |
| 6 | T5 Analisis dan penulisan | | | | | | | | | | | | ■ | ■ | ■ | — |

## 3.10 Parameter Rancangan yang Ditetapkan Kemudian

Parameter yang bergantung pada kesepakatan pembimbing, hasil tahap sebelumnya, atau data validasi dihimpun pada Tabel 3.7 dan ditetapkan sebelum dipakai menilai data uji atau gerbang terkait.

Tabel 3.7 Parameter rancangan yang ditetapkan kemudian

| No. | Parameter | Waktu atau dasar penetapan | Status |
|---|---|---|---|
| 1 | Finalisasi ambang seluruh gerbang G0–G4 | Sebelum gerbang dinilai | [PERLU DATA: finalisasi ambang usulan Tabel 3.5 bersama pembimbing] |
| 2 | Ambang G1, tindakan gagal kedua, dan kriteria pemangkasan himpunan huruf | Sebelum eksperimen | [PERLU DATA: ambang, tindakan, dan kriteria pemangkasan tanpa data uji] |
| 3 | Kriteria kualitas model guru | Sebelum pelatihan murid | [PERLU DATA: ambang deteksi tangan, batas jitter, prosedur sampel] |
| 4 | Pemilihan *subcarrier*, lintasan puncak, dan segmentasi huruf statis | Sebelum dipakai | [PERLU DATA: kriteria, definisi operasional, ambang dan jendela tahan pose] |
| 5 | Pembagian data dan strategi Widar3.0 | Sebelum dipakai | [PERLU DATA: blok, proporsi latih-validasi-uji, komponen strategi, repetisi uji] |
| 6 | Suku supervisi guru dan ambang keyakinan | Dari data validasi | [PERLU DATA: bentuk suku distilasi, bobot, dan ambang] |
| 7 | Perlakuan data uji | Sebelum dipakai | [PERLU DATA: segmen tersaring kamera atau segmentasi tanpa koreksi] |
| 8 | Inklusi partisipan, sesi per ruang, dan token apresiasi | Sebelum dipakai | [PERLU DATA: kriteria kompetensi, kefasihan validator, pengguna uji, token] |
| 9 | Publikasi *dataset* dan persetujuan etik | Sebelum dipakai | [PERLU DATA: izin, repositori, lisensi, lembaga persetujuan etik] |
| 10 | Rubrik tiga pilar pakar dan personalisasi bila G2 gagal | Sebelum G2 dinilai | [PERLU DATA: rubrik, ambang skor, prosedur data latih pengguna] |
| 11 | Indikator layak operasional dan durasi pengamatan deteksi palsu | Sebelum G3 dinilai | [PERLU DATA: anggaran latensi, batas deteksi palsu, baterai minimum, durasi] |
| 12 | Kanal, jarak antarmodul, zona, model layar, audio, dan kapasitas baterai | Pada T0 atau sebelum T4 | [PERLU DATA: penetapan, model layar final, kapasitas dari uji arus] |
| 13 | Mesin TTS *on-device* final, layanan ASR, dan frasa uji | Pada G3 | [PERLU DATA: keputusan mesin, layanan, dan daftar frasa dari uji banding] |
| 14 | Kuesioner, rubrik validator dan pakar, serta asumsi biaya G4 | Sebelum T4 | [PERLU DATA: butir kuesioner, rubrik, batas kesesuaian, harga dan asumsi] |

## 3.11 Risiko dan Alternatif Cadangan

Risiko utama dan mitigasinya dirangkum pada Tabel 3.8. Cadangan disusun bertingkat sesuai titik kegagalan sehingga kegagalan komponen tidak menghentikan penelitian, tetapi mempersempit klaimnya; setiap pemakaian cadangan dicatat dalam laporan akhir.

Tabel 3.8 Risiko dan mitigasi

| No. | Risiko | Dampak | Mitigasi dan cadangan |
|---|---|---|---|
| 1 | Pola CSI isyarat tidak terpisah pada konfigurasi dua modul | G0 gagal; jalur CSI tidak layak | Perbaikan penempatan satu kali; gagal lagi berarti dihentikan dan dilaporkan |
| 2 | Akurasi lintas partisipan, ruang, atau posisi rendah (G2 gagal) | Klaim pengguna baru tak dapat dibuat | Personalisasi per pengguna (cadangan A); dilaporkan |
| 3 | Model int8 terlalu berat atau lambat di modul | Inferensi tepi tidak tercapai | Klasifikasi dipindah ke server, modul kirim fitur (cadangan B) |
| 4 | Beban radio gabungan CSI, UDP, dan audio bermasalah | Purwarupa tidak stabil | Modul ketiga khusus antarmuka (cadangan C) |
| 5 | Layanan ucapan tidak memadai, termasuk suara Kokoro belum tersedia | Jalur ucapan terganggu | Beralih ke MMS-TTS-ind ONNX, lalu server lokal atau awan (cadangan D) |
| 6 | Aset representasi isyarat mahal | Cakupan arah kedua sempit | Batasi ke glos dan gambar plus ejaan jari |
| 7 | Ketahanan baterai di bawah target | Klaim portabilitas melemah | Ukur arus, sesuaikan target, laporkan apa adanya |
| 8 | Rekrutmen, etika, atau kuota GPU terlambat | Jadwal mundur | Dua ruang dan pengisyarat cadangan; pelatihan terkompresi; minggu transisi |
| 9 | Huruf sangat mirip tak terpisahkan CSI | Himpunan kelas menyempit | Pangkas himpunan pada G1 sesuai Tabel 3.7; laporkan pasangan gagal |

# DAFTAR PUSTAKA

[1] Kementerian Koordinator Bidang Pembangunan Manusia dan Kebudayaan, "Kemenko PMK bergerak bersama wujudkan selaras bahasa isyarat," 3 Okt. 2025. [Online]. Available: https://www.kemenkopmk.go.id/kemenko-pmk-bergerak-bersama-wujudkan-selaras-bahasa-isyarat, diakses 24 Okt. 2026.

[2] Republik Indonesia, *Undang-Undang Nomor 8 Tahun 2016 tentang Penyandang Disabilitas*. Jakarta, Indonesia, 2016.

[3] Departemen Pendidikan dan Kebudayaan, *Kamus Sistem Isyarat Bahasa Indonesia* (edisi pertama). Jakarta, Indonesia: Departemen Pendidikan dan Kebudayaan, 1994.

[4] S. As Satillah, K. Khotimah, N. N. Muslihah, R. Rahmayanti, W. Mirip, Y. D. Suryani, and L. D. A. Pagarwati, "Ragam bahasa anak tunarungu dengan SIBI di SLB N Ogan Ilir," *Jurnal Anak Usia Dini Holistik Integratif (AUDHI)*, vol. 7, no. 1, pp. 31–43, 2024, doi: 10.36722/jaudhi.v7i1.2876.

[5] A. S. Nugraheni, A. P. Husain, and H. Unayah, "Optimalisasi penggunaan bahasa isyarat dengan SIBI dan BISINDO pada mahasiswa difabel tunarungu di Prodi PGMI UIN Sunan Kalijaga," *Jurnal Holistika*, vol. 5, no. 1, pp. 28–33, 2023, doi: 10.24853/holistika.5.1.28-33.

[6] M. Malika and Berlianti, "Penggunaan bahasa isyarat SIBI dan BISINDO untuk siswa tuli di Sekolah Luar Biasa Negeri Pembina Medan," *Concept: Journal of Social Humanities and Education*, vol. 4, no. 3, pp. 78–87, 2025, doi: 10.55606/concept.v4i3.2178.

[7] Badan Riset dan Inovasi Nasional, "BRIN dorong penguatan ekosistem bahasa isyarat, BISINDO dominan digunakan penyandang tuli," 26 Agu. 2026. [Online]. Available: https://brin.go.id/news/130095, diakses 24 Okt. 2026.

[8] R. A. Mursita, "Respon tunarungu terhadap penggunaan Sistem Bahasa Isyarat Indonesia (SIBI) dan Bahasa Isyarat Indonesia (BISINDO) dalam komunikasi," *INKLUSI*, vol. 2, no. 2, p. 221, 2015, doi: 10.14421/ijds.2202.

[9] M. Zikky and Z. F. Akbar, "Kamus sistem isyarat bahasa Indonesia (KASIBI) dengan voice recognition sebagai pendukung belajar bahasa isyarat berbasis Android," *Jurnal Sains Terapan*, vol. 5, no. 2, 2019, doi: 10.32487/jst.v5i2.732.

[10] R. Fatmawati, R. Asmara, Y. R. Prayogi, and R. Y. Hakkun, "Aplikasi pembelajaran sistem isyarat bahasa Indonesia (SIBI) berbasis voice menggunakan OpenSIBI," *Technomedia Journal*, vol. 7, no. 1, pp. 22–39, 2022, doi: 10.33050/tmj.v7i1.1690.

[11] S. Dwijayanti, Hermawati, S. I. Taqiyyah, H. Hikmarika, and B. Y. Suprapto, "Indonesia sign language recognition using convolutional neural network," *International Journal of Advanced Computer Science and Applications*, vol. 12, no. 10, 2021, doi: 10.14569/IJACSA.2021.0121046.

[12] R. Soekarta, S. Aras, R. Rezki, and N. K. D. P. Ainun, "Sistem deteksi simbol isyarat pada SIBI (Sistem Isyarat Bahasa Indonesia) menggunakan Mediapipe berbasis Android," *Insect (Informatics and Security): Jurnal Teknik Informatika*, vol. 10, no. 2, pp. 90–100, 2024, doi: 10.33506/insect.v10i2.4079.

[13] R. A. Maulana, A. R. Adriansyah, and Z. Imaduddin, "Integrasi model deep learning pada pengembangan aplikasi Android pendeteksi bahasa isyarat SIBI menggunakan Jetpack Compose," *DBESTI: Journal of Digital Business and Technology Innovation*, vol. 3, no. 1, pp. 78–85, 2026, doi: 10.54914/dbesti.v3i1.2081.

[14] Y. Ma, G. Zhou, and S. Wang, "WiFi sensing with channel state information: A survey," *ACM Computing Surveys*, vol. 52, no. 3, pp. 1–36, 2019, doi: 10.1145/3310194.

[15] Y. Ma, G. Zhou, S. Wang, H. Zhao, and W. Jung, "SignFi: Sign language recognition using WiFi," *Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies*, vol. 2, no. 1, pp. 1–21, 2018, doi: 10.1145/3191755.

[16] H. F. Thariq Ahmed, H. Ahmad, K. Narasingamurthi, H. Harkat, and S. K. Phang, "DF-WiSLR: Device-free Wi-Fi-based sign language recognition," *Pervasive and Mobile Computing*, vol. 69, Art. no. 101289, 2020, doi: 10.1016/j.pmcj.2020.101289.

[17] L. Zhang, Y. Zhang, and X. Zheng, "WiSign: Ubiquitous American Sign Language recognition using commercial Wi-Fi devices," *ACM Transactions on Intelligent Systems and Technology*, vol. 11, no. 3, pp. 1–24, 2020, doi: 10.1145/3377553.

[18] Espressif Systems, *ESP32-S3 Series Datasheet*, versi 2.2, 2026. [Online]. Available: https://www.espressif.com/sites/default/files/documentation/esp32-s3_datasheet_en.pdf, diakses 25 Okt. 2026.

[19] Espressif Systems, "esp-csi: Wi-Fi channel state information based sensing," repositori GitHub. [Online]. Available: https://github.com/espressif/esp-csi, diakses 25 Okt. 2026.

[20] ruvnet, "RuView," repositori GitHub. [Online]. Available: https://github.com/ruvnet/RuView, commit fefb0f9, diakses 24 Okt. 2026.

[21] G. Hinton, O. Vinyals, and J. Dean, "Distilling the knowledge in a neural network," arXiv:1503.02531, 2015, doi: 10.48550/arXiv.1503.02531.

[22] F. Picron, D. Van Landuyt, and R. Omardeen, "(Towards) Sign language machine translation in practice," in *Machine Translation: Technologies and Applications*. Cham, Switzerland: Springer, 2024, pp. 327–343, doi: 10.1007/978-3-031-47362-3_14.

[23] S. A. Sanjaya and H. F. Ilone, "BISINDO sign language recognition: A systematic literature review of deep learning techniques for image processing," *Indonesian Journal of Computer Science*, vol. 12, no. 6, 2023, doi: 10.33022/ijcs.v12i6.3539.

[24] G. O. Kindy, G. Leonali, and H. Lucky, "Word-level BISINDO: A novel video Indonesian sign language dataset and baseline methods," *Procedia Computer Science*, vol. 269, pp. 249–258, 2025, doi: 10.1016/j.procs.2025.08.277.

[25] D. Wu, Y. Zeng, F. Zhang, and D. Zhang, “WiFi CSI-based device-free sensing: From Fresnel zone model to CSI-ratio model,” *CCF Transactions on Pervasive Computing and Interaction*, vol. 4, no. 1, pp. 88–102, 2022, doi: 10.1007/s42486-021-00077-z.

[26] K. Qian, C. Wu, Y. Zhang, G. Zhang, Z. Yang, and Y. Liu, “Widar2.0: Passive human tracking with a single Wi-Fi link,” in *Proc. 16th Annual Int. Conf. Mobile Systems, Applications, and Services (MobiSys)*, 2018, pp. 350–361, doi: 10.1145/3210240.3210314.

[27] Y. Zhang, Y. Zheng, K. Qian, G. Zhang, Y. Liu, C. Wu, and Z. Yang, "Widar3.0: Zero-effort cross-domain gesture recognition with Wi-Fi," *IEEE Transactions on Pattern Analysis and Machine Intelligence*, vol. 44, no. 11, pp. 8671–8685, 2022, doi: 10.1109/TPAMI.2021.3105387.

[28] J. Geng, D. Huang, and F. De la Torre, "DensePose from WiFi," arXiv:2301.00250, 2023, doi: 10.48550/arXiv.2301.00250.

[29] Ultralytics, "Pose estimation" dan "Hand Keypoints Pose Estimation Dataset," Ultralytics YOLO Docs. [Online]. Available: https://docs.ultralytics.com/tasks/pose/ dan https://docs.ultralytics.com/datasets/pose/hand-keypoints/, diakses 8 Nov. 2026.

[30] C. Cortes and V. Vapnik, "Support-vector networks," *Machine Learning*, vol. 20, no. 3, pp. 273–297, 1995, doi: 10.1007/BF00994018.

[31] C. K. Chow, "On optimum recognition error and reject tradeoff," *IEEE Transactions on Information Theory*, vol. 16, no. 1, pp. 41–46, 1970, doi: 10.1109/TIT.1970.1054406.

[32] Espressif Systems, "esp-nn: Neural network kernel library for Espressif chips," repositori GitHub. [Online]. Available: https://github.com/espressif/esp-nn, diakses 25 Okt. 2026.

[33] Espressif Systems, "esp-dl: Espressif deep-learning library for ESP32-S3," repositori GitHub. [Online]. Available: https://github.com/espressif/esp-dl, diakses 25 Okt. 2026.

[34] Espressif Systems, "tflite-micro-esp-examples," repositori GitHub. [Online]. Available: https://github.com/espressif/tflite-micro-esp-examples, diakses 25 Okt. 2026.

[35] hexgrad, "Kokoro-82M," model card Hugging Face. [Online]. Available: https://huggingface.co/hexgrad/Kokoro-82M dan https://doi.org/10.57967/hf/4329, diakses 25 Okt. 2026.

[36] thewh1teagle, "kokoro-onnx: ONNX versions of the Kokoro TTS model," repositori GitHub. [Online]. Available: https://github.com/thewh1teagle/kokoro-onnx, diakses 9 Nov. 2026.

[37] Microsoft, "onnxruntime: Cross-platform, high performance ML inference and training accelerator," repositori GitHub. [Online]. Available: https://github.com/microsoft/onnxruntime, diakses 9 Nov. 2026.

[38] Meta AI, "Massively Multilingual Speech (MMS): Indonesian text-to-speech," model card Hugging Face facebook/mms-tts-ind. [Online]. Available: https://huggingface.co/facebook/mms-tts-ind, diakses 25 Okt. 2026.

[39] A. Radford *et al.*, "Robust speech recognition via large-scale weak supervision," arXiv:2212.04356, 2022, doi: 10.48550/arXiv.2212.04356.

[40] SYSTRAN, "faster-whisper: Whisper transcription with CTranslate2," repositori GitHub. [Online]. Available: https://github.com/SYSTRAN/faster-whisper, diakses 25 Okt. 2026.

[41] Tokio, "tokio: A runtime for writing reliable asynchronous applications with Rust," repositori GitHub. [Online]. Available: https://github.com/tokio-rs/tokio, diakses 9 Nov. 2026.

[42] tokio-rs, "axum: Ergonomic and modular web framework built with Tokio," repositori GitHub. [Online]. Available: https://github.com/tokio-rs/axum, diakses 9 Nov. 2026.

[43] leptos-rs, "leptos: Build fast full-stack web apps in Rust," repositori GitHub. [Online]. Available: https://github.com/leptos-rs/leptos, diakses 9 Nov. 2026.

[44] Tauri, "tauri: Build smaller, faster, and more secure desktop and mobile applications," repositori GitHub. [Online]. Available: https://github.com/tauri-apps/tauri, diakses 9 Nov. 2026.

[45] J. C. Mankins, "Technology readiness assessments: A retrospective," *Acta Astronautica*, vol. 65, no. 9-10, pp. 1216-1223, 2009, doi: 10.1016/j.actaastro.2009.03.058.

[46] R. Likert, "A technique for the measurement of attitudes," *Archives of Psychology*, no. 140, pp. 5–55, 1932.
