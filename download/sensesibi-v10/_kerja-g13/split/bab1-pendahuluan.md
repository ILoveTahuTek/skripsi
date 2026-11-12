# BAB I PENDAHULUAN

## 1.1 Latar Belakang

Anak tunarungu hampir selalu lahir dari orang tua yang bisa mendengar. Sejak hari-hari pertama, komunikasi di rumah berjalan dengan dua bahasa yang tidak saling mengerti: orang tua berbicara dengan suara, anak menjawab dengan isyarat. Orang tua lalu harus mempelajari bahasa isyarat dari nol, padahal waktu dan kesempatan berlatih serba terbatas. Angkanya memang timpang. Di Indonesia ada sekitar 1,92 juta penyandang tunarungu, sementara juru bahasa isyarat hanya sekitar 500 orang [1], sehingga satu juru bahasa harus melayani hampir 4.000 orang. Untuk kebutuhan harian seperti menceritakan sakit atau bertanya kepada penjual di pasar, menunggu juru bahasa jelas bukan jalan keluar. Undang-Undang Nomor 8 Tahun 2016 sudah menjamin hak setiap penyandang disabilitas untuk berkomunikasi [2], tetapi tanpa alat bantu yang benar-benar terjangkau, jaminan itu berjalan lambat.

Kesenjangan seperti itu paling terasa di ruang kelas. Guru menjelaskan dengan suara; siswa tunarungu menangkap sebagian, menebak sisanya, lalu mudah kehilangan alur pelajaran. SIBI menjadi bahasa pengantar pada pendidikan formal; bentuk isyaratnya dibakukan pemerintah dalam *Kamus Sistem Isyarat Bahasa Indonesia* [3]. Penelitian di SLB Negeri Ogan Ilir memperlihatkan siswa yang memakai SIBI dalam pembelajaran meskipun di luar kelas mereka lebih akrab dengan BISINDO [4]. Nugraheni dkk. [5] serta Malika dan Berlianti [6] melaporkan temuan serupa: SIBI hidup di sekolah, BISINDO hidup di komunitas. Survei BRIN mencatat 77,7% responden tunarungu memakai BISINDO dan hanya 1,9% memakai SIBI [7], sedangkan survei terhadap 100 responden tunarungu di Jawa dan Bali melaporkan angka 91% untuk BISINDO [8]. Kedua survei itu justru menunjukkan tempat SIBI: sekolah. Karena penelitian ini menyasar alat bantu pembelajaran di sekolah, SIBI yang dipilih. Seluruh pelaksanaannya direncanakan di Jawa Timur tanpa mengikat kerja sama dengan lembaga tertentu.

Upaya membangun alat bantu komunikasi dua arah sebenarnya sudah ada, tetapi jalurnya baru setengah jalan. KASIBI mengubah ucapan menjadi teks lalu memunculkan animasi tangan tiga dimensi [9], sedangkan OpenSIBI menganimasikan 50 kosakata SIBI dari teks [10]; keduanya sama-sama hanya melayani satu arah, yaitu orang pendengar berbicara dan sistem mengisyaratkan. Arah sebaliknya, isyarat siswa yang dibaca mesin, belum tersedia sebagai alat yang siap dipakai. Riset pengenalan isyarat di Indonesia masih berkutat di jalur kamera: pengenalan huruf BISINDO dari citra [11], aplikasi deteksi 24 huruf statis SIBI dengan MediaPipe [12], dan aplikasi Android berbasis *deep learning* [13]. Kendala kamera itu ada dua dan keduanya praktis. Kamera menuntut pencahayaan serta posisi yang tepat, dan begitu cahaya sedikit berubah, akurasi ikut jatuh; kamera yang terus menyala juga membuat penggunanya merasa diawasi, tidak nyaman dipakai sepanjang hari di kelas.

Untuk menghindari dua kendala itu, sinyal Wi-Fi membuka jalan lain tanpa kamera. Sinyal ini membawa informasi kanal bernama *Channel State Information* (CSI) [14]. Begitu tangan bergerak di antara pemancar dan penerima, jalur pantulan sinyal bergeser dan CSI berubah mengikuti pola gerakannya; perubahan itulah yang dibaca untuk mengenali gerak tanpa sensor yang dikenakan di tubuh. Kemampuan semacam ini sudah terbukti di sejumlah penelitian: SignFi mengenali 276 isyarat *American Sign Language* (ASL) dari CSI [15], DF-WiSLR mengenali 49 gestur tanpa perangkat yang dikenakan [16], dan WiSign membaca kalimat ASL dari perangkat Wi-Fi komersial [17]. CSI bahkan peka terhadap gerak halus sampai ke gerakan jari [14]. Penelusuran pada Google Scholar, Crossref, dan OpenAlex hingga Oktober 2026 belum menemukan satu pun penerapan CSI untuk isyarat SIBI.

Perangkat yang dibutuhkan pun sederhana dan murah. Modul ESP32-S3, mikrokontroler seharga sekitar Rp150.000, sudah memiliki radio Wi-Fi 2,4 GHz dengan dukungan CSI resmi [18], [19]. Dua modul cukup untuk satu pasang: yang satu memancarkan sinyal, yang lain menangkapnya, dan zona isyarat berada di antara keduanya. *Firmware* penangkap CSI yang teruji untuk modul ini tersedia pada platform terbuka RuView [20]. Biaya sepasang node lengkap diperkirakan di bawah Rp350.000, jauh lebih ringan daripada kamera ditambah komputer pengolah citra. Murah bukan sekadar soal angka; harga yang terjangkau mengundang sekolah berani memasang alat ini di lebih dari satu ruang.

Jawabannya, penelitian ini merancang purwarupa bernama SenseSIBI, singkatan dari *Sensing & Translation of SIBI*. Arah pertamanya berjalan dari siswa: ia mengisyaratkan huruf, modul menangkap pola CSI, model yang berjalan langsung di modul mengenalinya, teks muncul di layar, lalu dibunyikan sebagai suara. Arah kedua berjalan dari guru: ia menekan tombol lalu berbicara; ucapannya dikenali menjadi teks, lalu bentuk isyaratnya ikut tampil di layar. Model Wi-Fi-nya sendiri tidak dilatih dari nol. Model penglihatan YOLO26m-Pose yang sudah terlatih pada data citra SIBI berperan sebagai "guru", sedangkan model Wi-Fi menjadi "murid" yang belajar menirunya lewat distilasi pengetahuan [21]. Kamera hanya dipakai guru saat data direkam; setelah murid lulus, seluruh sistem bekerja tanpa kamera.

Sebagai studi kelayakan, penelitian ini sengaja membatasi klaimnya. Objek pengenalan dibatasi pada alfabet manual SIBI satu tangan sebanyak 26 huruf, yaitu 24 huruf statis ditambah dua huruf gerak J dan Z, bukan penerjemahan kalimat penuh; penerjemahan bahasa isyarat tingkat kalimat sampai sekarang masih menjadi masalah terbuka [22]. Kemampuan membedakan huruf diuji lebih dahulu sebelum klaim yang lebih jauh dibuat; tiap tahap ditutup gerbang keputusan, dan kegagalan tetap dilaporkan sebagai temuan. Dalam batas itulah penelitian ini mencoba menjawab pertanyaan yang sederhana sekaligus jujur: apakah sepasang modul Wi-Fi murah sungguh bisa menjadi jembatan komunikasi dua arah antara siswa tunarungu dan gurunya di kelas?

## 1.2 Rumusan Masalah

Dari latar belakang yang telah dipaparkan, masalah yang dikaji dalam penelitian ini dirumuskan sebagai berikut.

1. Bagaimana merancang purwarupa penerjemah dua arah, yang menghubungkan SIBI dengan teks dan suara bahasa Indonesia, dengan sepasang modul ESP32-S3 yang bekerja tanpa kamera?
2. Seberapa baik alfabet manual SIBI dikenali dari sinyal CSI, dan bagaimana kinerja kedua jalur penerjemahan pada skenario dalam sesi, lintas partisipan, serta lintas ruang?
3. Seberapa layak purwarupa menjadi alat bantu komunikasi jika ditinjau dari latensi, cakupan kosakata, keandalan operasional, penerimaan pengguna, dan biaya?

## 1.3 Tujuan Penelitian

Tujuan penelitian ini adalah sebagai berikut.

1. Merancang purwarupa penerjemah dua arah, yang menghubungkan SIBI dengan teks dan suara bahasa Indonesia, dengan sepasang modul ESP32-S3 yang bekerja tanpa kamera.
2. Mengukur seberapa baik alfabet manual SIBI dikenali dari sinyal CSI serta kinerja kedua jalur penerjemahan pada skenario dalam sesi, lintas partisipan, dan lintas ruang.
3. Menganalisis kelayakan purwarupa sebagai alat bantu komunikasi ditinjau dari latensi, cakupan kosakata, keandalan operasional, penerimaan pengguna, dan biaya.

## 1.4 Batasan Masalah

Agar fokus, ruang lingkup penelitian ini dibatasi sebagai berikut.

1. Objek pengenalan ialah alfabet manual SIBI satu tangan 26 huruf (24 statis serta huruf gerak J dan Z); bentuk bakunya dicocokkan dengan *Kamus SIBI* [3] dan disetujui validator penutur tunarungu; sistem ini bukan penerjemah kalimat.
2. Pembeda utamanya adalah bentuk tangan dan jari; ekspresi wajah serta penanda nonmanual tidak dikenali.
3. Penginderaan memakai sepasang modul ESP32-S3 (satu pemancar, satu penerima; 2,4 GHz, kanal 20 MHz) dengan layar, baterai, *speaker*, dan mikrofon pada node penerima; kamera hanya menyala saat perekaman data pelatihan.
4. YOLO26m-Pose berperan sebagai guru hanya pada saat akuisisi dan pelatihan; produk akhirnya bebas kamera dan bebas citra.
5. Sintesis ucapan berjalan *on-device* di ponsel, sedangkan pengenalan ucapan memakai layanan awan dengan mesin lokal sebagai cadangan; pilihan finalnya ditetapkan pada gerbang G3.
6. Arah kedua terbatas pada kamus tingkat kata dengan *fallback* ejaan jari; cakupan kamusnya diukur lalu dilaporkan.
7. Satu sesi hanya melibatkan satu pengisyarat dan sistem tidak mengidentifikasi individu; pengujian berlangsung di sedikitnya dua ruang berbeda di Jawa Timur yang sudah dikalibrasi.
8. Uji pengguna berskala kecil (3–5 pengguna) dan dianalisis secara deskriptif, tanpa statistik inferensial.
9. Isyarat kontinu, tata bahasa isyarat penuh, BISINDO, serta klasifikasi gerakan otomatis dari video berada di luar pembahasan.

## 1.5 Manfaat Penelitian

Manfaat penelitian ini terbagi atas manfaat teoretis dan manfaat praktis.

### 1.5.1 Manfaat Teoretis

Secara teoretis, penelitian ini menyumbang bukti awal: apakah CSI dari satu tautan antarmodul ESP32-S3 sanggup membedakan alfabet manual SIBI. Bukti semacam itu terikat pada alfabet manual dan belum tentu berlaku untuk isyarat kata maupun isyarat kontinu. Penelitian ini juga meninggalkan *dataset* CSI berlabel beserta protokol perekamannya, sehingga peneliti berikutnya bisa memakainya untuk bahasa isyarat lain, termasuk perluasan ke BISINDO.

### 1.5.2 Manfaat Praktis

Bagi sekolah yang kelak memakainya, penelitian ini memberi gambaran nyata tentang kelayakan alat bantu komunikasi dua arah berbahasa SIBI, lengkap dengan biaya perangkatnya. Purwarupa yang memunculkan teks, menyuarakan isyarat, dan memperagakan bentuk isyarat bagi lawan bicara akan lahir jika seluruh tahap berhasil; jika berhenti lebih awal, laporan karakterisasi, protokol, dan *dataset* berlabel tetap menjadi warisan penelitian. Bagi keluarga siswa, kosakata yang tervalidasi memastikan isyarat yang muncul di layar benar bentuknya. Bagi komunitas riset, rancangan yang tidak terikat pada satu bahasa isyarat memudahkan replikasi di tempat lain.

## 1.6 Sistematika Penulisan

Secara ringkas, proposal ini disusun atas tiga bab. **BAB I Pendahuluan** memuat latar belakang, rumusan masalah, tujuan, batasan, manfaat, dan sistematika penulisan. **BAB II Kajian Pustaka** menghimpun teori dan penelitian terdahulu yang menjadi dasar perancangan. Adapun **BAB III Metode Penelitian** memuat desain, tahapan, waktu dan lokasi, alat dan bahan, perancangan sistem, protokol perekaman, pengolahan sinyal dan pelatihan, skenario pengujian, jadwal, parameter yang ditetapkan kemudian, serta risiko dan cadangannya.
