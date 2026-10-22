**PROPOSAL PENGAJUAN JUDUL SKRIPSI**

*Opsi Alat 1 dari 4 — Pemantauan Wi-Fi CSI pada Kandang Ayam Broiler*

**Judul Utama yang Diusulkan**

**ESTIMASI INDEKS AKTIVITAS KAWANAN BROILER BERBASIS WI-FI CHANNEL STATE INFORMATION PADA ESP32: STUDI KELAYAKAN PEMANTAUAN DINI KESEHATAN UNGGAS**

**Judul Alternatif 1:** Deteksi Perubahan Aktivitas Kawanan Ayam Berbasis Wi-Fi CSI untuk Sistem Peringatan Dini di Peternakan Rakyat

**Judul Alternatif 2:** Sistem Monitoring Perilaku Kawanan Unggas Device-Free Berbasis Wi-Fi CSI pada ESP32 dengan Dataset Publik

# **BAB I**

# **PENDAHULUAN**

## **1.1 Latar Belakang**

Perkembangan teknologi telah memengaruhi berbagai aktivitas peternakan, termasuk cara peternak memantau kondisi kawanan unggas yang dipeliharanya. Saat ini, peternakan skala kecil dan menengah dituntut meningkatkan efisiensi produksi di tengah keterbatasan tenaga kerja, sementara penyakit unggas masih sering terdeteksi terlambat. Keterlambatan deteksi menyebabkan penyebaran ke seluruh kawanan, kenaikan mortalitas, dan kerugian ekonomi yang berarti bagi peternak rakyat yang mengelola 10 hingga 50 ekor per siklus. Tinjauan sistematis He et al. (2022) menunjukkan bahwa peringatan dini penyakit ayam selama ini bertumpu pada pemantauan gejala klinis, dan seluruh moda pemantauan otomatis yang tersedia mengandalkan kamera atau sensor lekat yang mahal serta rumit bagi peternak kecil \[9\]. Kondisi tersebut menunjukkan bahwa dibutuhkan metode pemantauan yang murah, tanpa kamera saat operasi, dan tidak menuntut pemasangan perangkat pada tiap ekor.

Wi-Fi Channel State Information (CSI) merupakan jalur teknologi yang menawarkan alternatif atas moda tersebut. CSI adalah data per-subcarrier yang melaporkan bagaimana sinyal Wi-Fi termodulasi oleh lingkungan fisik, sehingga gerakan benda di antara pemancar dan penerima meninggalkan jejak yang terukur pada amplitudo dan fase sinyal. Ma et al. (2019) menjelaskan bahwa keluarga aplikasi sensing Wi-Fi telah mencakup pengenalan aktivitas, deteksi jatuh, dan estimasi respirasi manusia \[1\]. Hernandez dan Bulut (2020) menunjukkan bahwa sensing Wi-Fi berbasis CSI dapat dijalankan pada perangkat murah kelas Internet of Things, sehingga hambatan biaya perangkat keras semakin rendah \[2\]. Pada penelitian ini, CSI digunakan untuk membaca jejak gerak kolektif kawanan ayam broiler tanpa kamera dan tanpa perangkat lekat.

Pada hewan ternak besar, kemampuan CSI telah terbukti pada lingkungan kandang nyata. Hao et al. (2019) memantau respirasi babi menggunakan informasi kanal jaringan Wi-Fi \[3\], Lu et al. (2019) melanjutkan pemantauan frekuensi respirasi babi dengan teknologi wireless sensing \[4\], dan Hao et al. (2020) mengenali perilaku mounting sapi perlah dari sinyal Wi-Fi dengan ribuan sampel uji \[5\]. Ketiganya bekerja pada satu sampai dua hewan bermassa besar per area, sehingga masih membuka pertanyaan apakah pendekatan yang sama dapat bekerja pada kawanan unggas yang jauh lebih kecil massanya dan jauh lebih banyak jumlahnya. Pencarian literatur yang dilakukan sebelum penyusunan proposal ini tidak menemukan satu pun publikasi Wi-Fi CSI pada unggas, termasuk pada tinjauan peringatan dini penyakit ayam yang menyebut tiga moda utama tanpa menyebut Wi-Fi \[9\]. Pemantauan broiler hingga kini didominasi akselerometer lekat \[6\], computer vision \[7\] \[8\], sehingga penerapan CSI pada kawanan unggas merupakan wilayah yang belum dipetakan.

Rencana awal penelitian ini yang menjanjikan deteksi dini penyakit per-ekor telah direview secara kritis dan dinyatakan tidak defensibel. Ada tiga alasan struktural. Pertama, fisika sinyal: satu ayam sakit di kawanan 30 ekor hanya menyumbang sekitar 2 hingga 10 persen gangguan total, dan amplitudo Doppler skala dengan massa tubuh sehingga broiler dua kilogram menghasilkan gangguan puluhan kali lebih lemah daripada ternak besar. Kedua, tidak ada kelas positif: contoh ayam sakit terverifikasi tidak akan tersedia dalam satu semester, sehingga metrik klasifikasi seperti macro F1 tinggi tidak terdefinisi secara metodologis. Ketiga, atribusi individu tidak mungkin tanpa kamera pada setiap ekor. Konsekuensinya, unit analisis harus digeser dari individu ke kawanan, dan target pengukuran harus digeser dari deteksi penyakit ke estimasi indeks aktivitas kolektif.

Berdasarkan uraian tersebut, penelitian ini dilakukan untuk menguji kelayakan estimasi indeks aktivitas kawanan broiler menggunakan Wi-Fi CSI pada ESP32 sebagai dasar peringatan dini perubahan kondisi kawanan. Sistem yang dikembangkan mengintegrasikan firmware capture CSI pada ESP32, pengolahan sinyal pada server platform open-source RuView, indeks aktivitas kawanan, dan saluran peringatan melalui dashboard serta MQTT. Pengembangan ini diharapkan dapat memberikan alat bantu pemantauan berbiaya rendah bagi peternak rakyat sekaligus karakterisasi sinyal awal bagi penelitian sensing unggas berikutnya. Tabel 1.1 merangkum usulan judul utama beserta dua judul alternatif yang dipersiapkan untuk didiskusikan dengan pembimbing.

Tabel 1.1 Usulan judul penelitian

| **Kategori** | **Usulan Judul**                                                                                                                                | **Catatan Pemetaan**                                                                                                                                 |
|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| Utama        | Estimasi Indeks Aktivitas Kawanan Broiler Berbasis Wi-Fi Channel State Information pada ESP32: Studi Kelayakan Pemantauan Dini Kesehatan Unggas | Setiap kata terpetakan ke hasil yang dapat dibuktikan dalam satu semester; frasa studi kelayakan memberi ruang keluar yang elegan bila sinyal lemah. |
| Alternatif 1 | Deteksi Perubahan Aktivitas Kawanan Ayam Berbasis Wi-Fi CSI untuk Sistem Peringatan Dini di Peternakan Rakyat                                   | Dipilih bila pembimbing menuntut orientasi aplikasi; metrik alarm jujur ditetapkan sejak bab metode.                                                 |
| Alternatif 2 | Sistem Monitoring Perilaku Kawanan Unggas Device-Free Berbasis Wi-Fi CSI pada ESP32 dengan Dataset Publik                                       | Dipilih bila arah publikasi internasional dan jalur label proxy etis terkonfirmasi.                                                                  |

## **1.2 Rumusan Masalah**

Berdasarkan latar belakang permasalahan yang telah diuraikan serta untuk menjawab permasalahan yang menjadi fokus dalam penelitian ini, maka dapat dirumuskan beberapa rumusan masalah yang akan dikaji lebih lanjut. Rumusan masalah pada penelitian ini sebagai berikut.

1. Bagaimana rancangan uji fisik Delta-CSI dua node ESP32 menghasilkan kontras sinyal yang dapat diandalkan antara kondisi kandang kosong, satu ekor bergerak, dan kawanan penuh bergerak terhadap noise floor?

2. Bagaimana indeks aktivitas kawanan dibangun dari energi motion-band amplitudo CSI window 60 detik dan seberapa konsisten hasilnya terhadap referensi aktivitas dari kamera sinkron pada tiap window pengamatan?

3. Bagaimana efektivitas control chart berbasis z-score adaptif pada indeks aktivitas dalam memberi peringatan perubahan pola kawanan dengan tingkat alarm palsu paling banyak satu per 24 jam dan precision@k minimal 0,5 terhadap audit kamera retrospektif?

## **1.3 Tujuan Penelitian**

Penelitian ini bertujuan untuk menguji kelayakan estimasi indeks aktivitas kawanan broiler berbasis Wi-Fi CSI pada ESP32 sebagai dasar peringatan dini perubahan kondisi kawanan. Adapun tujuan dari penelitian ini adalah sebagai berikut.

1. Merancang uji fisik Delta-CSI tiga skenario (kandang kosong, satu ekor bergerak, kawanan penuh) di lokasi nyata pada minggu awal sebagai gerbang go/no-go kelayakan fisik sinyal.

2. Mengimplementasikan indeks aktivitas kawanan kontinyu dari energi motion-band amplitudo CSI dengan window 60 detik dan memvalidasinya terhadap referensi kamera sinkron.

3. Mengetahui hasil pengujian control chart z-score adaptif dalam mendeteksi perubahan pola kawanan melalui metrik alarm palsu per 24 jam dan precision@k, serta menyusun protokol pengukuran dan dataset awal yang terdokumentasi untuk penelitian lanjutan.

## **1.4 Batasan Masalah**

Agar penelitian ini memiliki ruang lingkup yang jelas dan terarah sesuai dengan tujuan yang telah ditetapkan, maka ditentukan batasan masalah guna membatasi pembahasan terhadap aspek-aspek yang relevan dengan topik penelitian. Adapun batasan masalah pada penelitian ini sebagai berikut.

1. Unit analisis adalah kawanan 10 hingga 15 ekor broiler dalam satu kandang mitra 【lokasi kandang】 dengan siklus pemeliharaan normal, bukan ayam per-ekor.

2. Tidak ada kelas positif penyakit terverifikasi dalam satu semester; evaluasi utama memakai metrik yang jujur untuk kondisi tanpa label, dan jalur sekunder hanya berjalan bila event proxy etis berlabel tersedia dari vaksinasi atau pembatasan pakan terkontrol.

3. Kamera hanya dipakai pada fase pelabelan dan audit; saat operasi harian sistem berjalan tanpa kamera.

4. Objek terbatas pada satu kandang mitra, sehingga desain evaluasi memakai split blok-waktu (latih pada hari A sampai B, uji pada hari C) untuk mengelola risiko pseudoreplikasi.

5. Sistem diposisikan sebagai alat bantu peringatan dini untuk peternak, bukan alat diagnosis medis hewan.

6. Penelitian ini tidak membahas identifikasi ayam per-ekor, diagnosis penyakit, pengukuran fisiologi per-ekor seperti denyut jantung unggas, maupun perluasan ke kandang skala industri.

## **1.5 Manfaat Penelitian**

Penerapan sensing Wi-Fi pada kawanan unggas kecil-kecil banyak merupakan wilayah yang belum terpetakan sehingga hasil penelitian ini berpotensi menjadi rujukan bagi kajian lanjutan. Proses pengujian yang bergerbang juga memberi contoh tata kelola risiko dan kejujuran metrik pada penelitian tugas akhir. Manfaat penelitian ini diuraikan sebagai berikut.

# **BAB II**

# **KAJIAN PUSTAKA**

## **2.1 Wi-Fi Channel State Information**

Wi-Fi Channel State Information (CSI) merupakan informasi per-subcarrier yang menggambarkan bagaimana sinyal Wi-Fi merambat dari pemancar ke penerima, mencakup amplitudo dan fase pada tiap subcarrier. Ketika orang, hewan, atau benda bergerak di antara kedua node, jalur pantulan sinyal berubah sehingga pola CSI ikut berubah; perubahan inilah yang dimanfaatkan sebagai sumber data sensing. Ma et al. (2019) menjelaskan bahwa keluarga aplikasi sensing Wi-Fi berbasis CSI mencakup pengenalan aktivitas, deteksi jatuh, estimasi respirasi, dan lokalisasi, dengan tantangan umum berupa sensitivitas lingkungan dan kebutuhan kalibrasi \[1\]. Karakteristik tersebut menempatkan CSI sebagai sensor tidak kasatmata yang tidak memerlukan kamera maupun perangkat yang dikenakan pada objek, sehingga sesuai untuk kandang yang padat dan lembap seperti pada penelitian ini.

## **2.2 Mikrokontroler ESP32**

ESP32 merupakan mikrokontroler murah dengan konektivitas Wi-Fi bawaan yang menyediakan akses CSI pada firmware khusus. Hernandez dan Bulut (2020) menunjukkan bahwa sensing Wi-Fi mandiri dapat berjalan penuh pada perangkat kelas IoT tanpa laptop atau kartu jaringan kelas riset, sehingga biaya per node sensing menjadi sangat rendah \[2\]. Kemampuan ini menjadi dasar pemilihan ESP32 sebagai perangkat capture pada penelitian ini: tiga node (satu access point, dua station) dapat dipasang mengapit area kawanan dengan anggaran yang masih terjangkau bagi mahasiswa. Dengan perangkat murah tersebut, replikasi protokol pengukuran oleh peneliti lain atau peternak lain juga menjadi lebih realistis.

## **2.3 Platform RuView**

Penelitian ini tidak membangun rantai pengambilan sinyal dari nol. Sistem dibangun di atas RuView, sebuah proyek open-source (github.com/ruvnet/RuView) yang menyediakan firmware ESP32 untuk penangkapan CSI, server pengolahan sinyal berbasis Rust, dashboard web, serta saluran alert melalui MQTT dan Home Assistant. Posisi RuView pada penelitian ini adalah infrastruktur capture, pipeline DSP dasar, dan alert; logika khusus unggas tetap menjadi tanggung jawab penelitian. RuView juga menyediakan modul ternak ind_livestock_monitor yang memuat desain alert stillness, escape, dan labored breathing untuk unggas; modul ini dipakai sebagai acuan desain, bukan dijalankan langsung pada skenario kandang broiler.

Tabel 2.1 memetakan fitur RuView yang dipakai beserta status keterujinya, agar janji teknis proposal ini selalu berada di atas fitur yang benar-benar terukur. Dua hal jujur perlu dicatat sejak awal. Pertama, filter bandpass napas dan jantung pada RuView memiliki rentang yang dikodekan permanen untuk manusia pada semua lapisan; bila penelitian melanjutkan ke estimasi napas unggas, konstanta filter wajib diubah di firmware dan server, dan denyut jantung ayam (250 hingga 330 denyut per menit) tidak mungkin diukur tanpa desain ulang filter. Kedua, fitur pose on-device pada RuView berstatus stub dengan kualitas terukur yang sangat rendah (PCK@20 sekitar 3 persen), sehingga tidak dijanjikan sama sekali dalam proposal ini.

Tabel 2.1 Pemetaan fitur RuView untuk alat kandang broiler

| **Fitur RuView**                                                   | **Peran pada Penelitian**                          | **Status**                                              |
|--------------------------------------------------------------------|----------------------------------------------------|---------------------------------------------------------|
| Capture CSI ESP32 + streaming UDP (format frame ADR-018)           | Sumber data utama seluruh eksperimen               | Terukur (MEASURED)                                      |
| Presence heuristik (varians fase, kalibrasi ambient 60 detik)      | Deteksi ada tidaknya aktivitas kawanan             | Terukur; risiko alarm palsu pada kipas ventilasi        |
| Motion-band power + akselerasi fase                                | Bahan baku indeks aktivitas kawanan (inti skripsi) | Terukur                                                 |
| Kalibrasi ruang kosong minimal 600 frame                           | Baseline kandang kosong sebelum eksperimen         | Terukur                                                 |
| Recording JSONL + adaptive classifier (latih di bawah 1 detik)     | Dataset percontohan dan klasifikator baseline      | Terukur                                                 |
| Dashboard web + MQTT + notifikasi                                  | Saluran peringatan ke peternak                     | Terukur                                                 |
| Modul ind_livestock_monitor (stillness, escape, labored breathing) | Acuan desain alert kesehatan kawanan               | DSP nyata; validasi hewan nol                           |
| Bandpass napas 0,1-0,5 Hz                                          | Estimasi napas unggas bila dilanjutkan             | Konstanta wajib diubah di semua lapisan                 |
| Pose 17-keypoint on-device                                         | Tidak dipakai                                      | Stub terukur (PCK@20 3,0 persen) — terlarang dijanjikan |

## **2.4 Pemantauan Perilaku Unggas**

Pemantauan broiler yang ada kini memakai moda lain di luar CSI. Yang et al. (2021) mengklasifikasi perilaku broiler dari akselerometer triaksial dengan machine learning \[6\]; Campbell et al. (2024) memantau aktivitas broiler komersial melalui clustering trajektori berbasis kamera \[7\]; dan Okinda et al. (2019) membangun sistem machine vision untuk deteksi dini burung sakit pada model broiler \[8\]. Ketiga moda ini menuntut biaya perangkat, pemeliharaan, atau kamera yang sulit bagi peternak kecil, dan ketiganya juga menegaskan bahwa indikator perilaku mendahului gejala klinis. Review He et al. (2022) merangkum kemajuan peringatan dini penyakit ayam dari gejala klinis dan menempatkan pemantauan otomatis sebagai arah penting \[9\]. Posisi penelitian ini adalah melengkapi moda tersebut dengan sensor yang tidak lekat dan tidak berkamera, dengan imbalan resolusi informasi yang lebih kasar pada tingkat kawanan.

## **2.5 Deteksi Anomali Tanpa Label**

Kondisi penelitian ini tidak menyediakan contoh kegagalan yang berlabel, sehingga pendekatan evaluasi harus jujur terhadap keterbatasan tersebut. Antonini et al. (2023) membuktikan bahwa deteksi anomali tanpa supervisi dapat berjalan pada lingkungan industri ekstrem dengan sistem TinyML adaptif \[10\]. Pola pendekatan ini sejalan dengan kebutuhan penelitian ini: control chart dan z-score adaptif pada indeks aktivitas yang tidak memerlukan contoh kegagalan, dengan audit retrospektif kamera sebagai penilaian kualitas alarm. Strategi semacam ini umum dipakai pada pemantauan proses industri dan dapat ditransfer ke pemantauan aktivitas kawanan tanpa mengubah prinsip kerjanya.

## **2.6 Penelitian Terdahulu**

Berdasarkan tabel perbandingan di atas, terlihat bahwa penelitian-penelitian sebelumnya terpisah pada dua kelompok: sensing CSI yang matang pada ternak besar per-individu, serta pemantauan unggas yang seluruhnya memakai sensor lekat atau kamera. Belum banyak penelitian yang secara spesifik menerapkan sensing CSI pada kawanan unggas kecil-kecil banyak dengan perangkat murah, terdapat juga beberapa celah masalah (gap) yang belum terselesaikan secara simultan oleh peneliti sebelumnya. Penelitian ini mengisi celah tersebut dengan langkah-langkah berikut.

1. Memindahkan unit analisis sensing CSI unggas dari individu ke kawanan sehingga keterbatasan fisika sinyal pada broiler bermassa kecil tetap dijawab secara jujur.

2. Memakai perangkat murah ESP32 dan platform open-source RuView agar seluruh rantai capture hingga alert dapat direplikasi peternak dan peneliti lain.

3. Menempatkan luaran sebagai studi kelayakan bergerbang dengan dataset awal dan protokol pengukuran sebagai artefak yang tetap bernilai.

Tabel 2.2 Perbandingan penelitian terdahulu

| **Peneliti (Tahun) dan Judul Singkat**                           | **Sinyal CSI** | **Target Unggas** | **Bebas Perangkat Lekat** | **Perangkat Murah** |
|------------------------------------------------------------------|----------------|-------------------|---------------------------|---------------------|
| Hao et al. (2019) — monitoring respirasi babi via CSI            | √              | −                 | √                         | −                   |
| Lu et al. (2019) — frekuensi respirasi babi, wireless sensing    | √              | −                 | √                         | −                   |
| Hao et al. (2020) — perilaku mounting sapi perah via Wi-Fi       | √              | −                 | √                         | −                   |
| Yang et al. (2021) — klasifikasi perilaku broiler akselerometer  | −              | √                 | −                         | −                   |
| Campbell et al. (2024) — aktivitas broiler via kamera            | −              | √                 | √                         | −                   |
| Okinda et al. (2019) — deteksi dini burung sakit, machine vision | −              | √                 | √                         | −                   |
| Penelitian Ini                                                   | √              | √                 | √                         | √                   |

# **BAB III**

# **METODE PENELITIAN**

## **3.1 Tahapan Penelitian**

Penelitian dalam proposal ini dilaksanakan melalui beberapa tahapan yang tersusun secara sistematis sehingga membentuk suatu alur penelitian yang terstruktur. Tahap pertama adalah studi literatur, yaitu pemetaan sensing CSI pada ternak, pemantauan perilaku unggas, dan metode evaluasi tanpa label, yang berujung pada penetapan metrik dan target yang jujur. Tahap kedua adalah perancangan sistem, mencakup arsitektur node, penempatan antena mengapit zona Fresnel area kawanan, dan protokol pengumpulan data. Tahap ketiga adalah implementasi, yaitu pemasangan perangkat, uji fisik Delta-CSI, pengumpulan dataset, dan pembangunan indeks aktivitas kawanan. Tahap terakhir adalah pengujian dan evaluasi, yaitu pengujian control chart terhadap audit kamera retrospektif dan penyusunan laporan kelayakan. Apabila dalam proses pengujian ditemukan kendala seperti alarm palsu berulang atau kontras sinyal yang lemah, maka dilakukan evaluasi dan perbaikan secara berulang hingga sistem dapat bekerja secara optimal.

Setiap tahap dirancang menghasilkan artefak tetap, mulai dari karakterisasi sinyal, protokol pengukuran, dataset awal, hingga laporan evaluasi, sehingga penelitian tetap bernilai sekalipun berhenti pada salah satu gerbang. Desain penelitian yang dipakai adalah studi kelayakan kuantitatif dengan gerbang go/no-go pada minggu ketiga; keputusan lanjut atau pivot diambil sebelum pipeline besar dibangun mengikuti prinsip bahwa biaya menemukan kelemahan di awal jauh lebih murah daripada di akhir.

## **3.2 Studi Literatur**

Studi literatur dilakukan terhadap tiga kelompok sumber, yaitu sensing Wi-Fi berbasis CSI pada manusia dan ternak, pemantauan perilaku unggas, serta metode deteksi anomali tanpa label. Sumber diutamakan dari jurnal dan prosiding terindeks (ACM, IEEE, Elsevier, MDPI, Sensors) pada rentang 2014 hingga 2024. Setiap referensi yang dikutip diverifikasi keasliannya melalui API Crossref dengan mencocokkan judul, penulis, tahun, dan venue terhadap DOI yang terdaftar, sehingga tidak ada satu pun referensi fiktif dalam dokumen ini. Hasil studi literatur dikonsolidasikan pada Bab II dan menjadi dasar pemilihan metrik serta penetapan celah penelitian pada subbab 2.6.

## **3.3 Perancangan Arsitektur Sistem**

Arsitektur sistem terdiri atas tiga lapisan. Lapisan sensing berisi tiga ESP32 (satu access point, dua station) yang dipasang TX-RX mengapit area kawanan agar geometri antena memotong zona Fresnel area bergerak; ketiganya mengirim frame CSI melalui UDP sesuai format frame ADR-018 milik RuView. Lapisan pengolahan berisi server Rust RuView pada single board computer yang melakukan dekoding frame, kalibrasi, ekstraksi motion-band power, dan agregasi indeks aktivitas per window 60 detik. Lapisan penyajian berisi dashboard web dan saluran alert MQTT ke perangkat peternak. Pemisahan tiga lapisan ini menjaga agar penggantian komponen pada satu lapisan tidak merombak lapisan lain.

## **3.4 Perancangan Perangkat Keras**

Perangkat keras utama adalah empat unit ESP32-S3 (tiga terpasang, satu cadangan) dengan housing tertutup, pigtail antena berkualitas, dan grounding untuk menghadapi amonia serta kelembapan kandang. Daya diberikan melalui adaptor dengan backup sederhana agar rekaman blok hari tidak terputus. Server pengolahan berjalan pada single board computer (Orange Pi atau Raspberry Pi) dengan kartu memori berkapasitas cukup untuk rekaman JSONL selama beberapa blok hari. Kamera sinkron dipasang hanya pada fase pelabelan dan audit, diposisikan sehingga tidak menambah beban operasional harian peternak.

## **3.5 Perancangan Perangkat Lunak dan Dataset**

Perangkat lunak penelitian terdiri atas tiga bagian. Bagian pertama adalah capture dan kalibrasi: baseline kandang kosong direkam minimal 600 frame mengikuti protokol RuView sebelum eksperimen dimulai. Bagian kedua adalah ekstraksi fitur: fitur per window 60 detik diambil dari amplitudo CSI saja karena fase ESP32 satu antena berderau tinggi; fitur meliputi energi motion-band, varians amplitudo, dan statistik akselerasi fase, dan keputusan membuang fase dinyatakan sejak desain fitur. Bagian ketiga adalah model: z-score adaptif terhadap baseline hari-hari sebelumnya dipadukan satu klasifikator SVM RBF yang dieksekusi di laptop; komponen CNN dan TFLite dinyatakan sebagai pekerjaan lanjutan dan tidak dijanjikan dalam lingkup skripsi ini.

Dataset disusun dalam blok hari berturut-turut dengan kamera sinkron untuk ground truth dan log kejadian harian (jadwal pakan, cahaya, suhu, kelembapan litter, panen) sebagai kovariat. Evaluasi memakai split blok-waktu, yaitu latih pada hari A sampai B dan uji pada hari C, karena split acak pada data time-series membocorkan informasi dan membuat hasil terlalu optimistis. Seluruh dataset, log, dan kode analisis disimpan terdokumentasi agar dapat dirilis sebagai dataset awal sensing kawanan unggas bila pembimbing menyetujui.

## **3.6 Objek, Lokasi, dan Kesejahteraan Hewan**

Objek penelitian adalah kawanan broiler 10 hingga 15 ekor pada kandang mitra 【lokasi kandang】 dengan siklus pemeliharaan normal. Penelitian bersifat observasional terhadap hewan, namun tetap memerlukan persetujuan kesejahteraan hewan; dokumen persetujuan disiapkan sebelum pengambilan data. Jalur kelas positif dikoordinasikan dengan puskeswan atau fakultas kedokteran hewan sejak awal untuk event proxy etis berlabel seperti vaksinasi, heat stress ringan, atau pembatasan pakan terkontrol. Seluruh prosedur penanganan hewan mengikuti praktik pemeliharaan normal, tanpa perlakuan yang menambah stres di luar praktik kandang standar.

## **3.7 Rencana Pengujian**

Rencana pengujian terdiri atas tiga kelompok yang berurutan. Pengujian pertama adalah uji fisik Delta-CSI pada minggu pertama hingga ketiga: dua ESP32 diposisikan mengapit kandang, lalu amplitudo CSI direkam window 60 detik untuk tiga skenario kandang kosong, satu ayam bergerak, dan kawanan penuh bergerak, ketiganya dibandingkan terhadap noise floor. Pengujian kedua adalah uji indeks aktivitas: energi motion-band diagregasi menjadi indeks per window dan dibandingkan dengan referensi intensitas gerak dari kamera sinkron pada tiap window. Pengujian ketiga adalah uji peringatan: control chart z-score adaptif dijalankan pada data blok hari, dan setiap alarm diaudit terhadap rekaman kamera retrospektif untuk menilai benar-salahnya. Setiap kelompok pengujian menghasilkan tabel hasil dan catatan kejadian yang melekat pada dataset.

## **3.8 Evaluasi dan Kriteria Keberhasilan**

Evaluasi memakai dua jalur yang jujur terhadap kondisi tanpa kelas positif. Jalur utama, yang selalu berjalan, memakai control chart pada indeks aktivitas dengan dua metrik: alarm palsu per 24 jam dengan target paling banyak satu per hari, dan precision@k minimal 0,5 berdasarkan audit kamera retrospektif pada k event teratas. Jalur sekunder hanya berjalan bila event proxy etis berlabel tersedia, memakai F1 minimal 0,70 pada level kawanan dengan split blok-waktu. Target macro F1 di atas 0,80 sengaja tidak dijanjikan karena secara metodologis tidak terdefinisi tanpa minimal 50 event anomali.

Minggu ketiga ditetapkan sebagai gerbang keputusan go/no-go. Bila aktivitas kawanan penuh tidak terlihat dari derau pada uji Delta-CSI, judul, metrik, dan arsitektur dipivot sebelum satu baris pipeline besar ditulis, dan kegagalan ini dicatat sebagai temuan studi kelayakan, bukan kegagalan skripsi. Bila kontras sinyal memadai, penelitian lanjut ke pengumpulan dataset dan evaluasi sesuai rencana. Kriteria kontras minimum ditetapkan bersama pembimbing pada pertemuan penjajakan judul sehingga keputusan go/no-go bersifat objektif.

## **3.9 Rencana Kegiatan dan Jadwal Penelitian**

Jadwal disusun untuk satu semester (sekitar 4,5 bulan efektif) dengan gerbang keputusan dini pada minggu ketiga dan eksperimen yang dipadatkan setelah gerbang lolos, sebagaimana Tabel 3.1. Baris pertama memuat gerbang go/no-go yang menentukan lanjut atau pivot seluruh rencana.

Tabel 3.1 Jadwal penelitian satu semester

| **Periode**  | **Aktivitas**                                                                                                                                                              | **Keluaran**                                    |
|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| Minggu 1-3   | Pembelian alat; pemasangan 3 ESP32; uji Delta-CSI tiga skenario (kosong, satu ekor, kawanan) — GERBANG GO/NO-GO; dokumen kesejahteraan hewan; kalibrasi baseline 600 frame | Keputusan go/no-go; baseline kandang; izin etik |
| Minggu 4-7   | Pengumpulan dataset blok hari A-B; kamera sinkron untuk ground truth; log kejadian harian; identifikasi event proxy etis bersama puskeswan                                 | Dataset mentah berlabel proxy + log kovariat    |
| Minggu 8-11  | Ekstraksi fitur amplitudo-only window 60 detik; z-score adaptif + SVM RBF; split blok-waktu (latih A-B, uji C); control chart dan precision@k                              | Model baseline + metrik dua jalur               |
| Minggu 12-15 | Analisis hasil; penyetelan ambang; audit kamera retrospektif; penyusunan dataset rilis (opsional, dengan DOI) bila pembimbing menyetujui                                   | Hasil evaluasi utuh + catatan rilis dataset     |
| Minggu 16-18 | Penulisan naskah skripsi; finalisasi bab metode dan hasil; persiapan sidang                                                                                                | Naskah skripsi siap sidang                      |

## **3.10 Rencana Biaya Penelitian**

Tabel 3.2 merangkum rencana biaya perangkat dan operasional dalam Rupiah. Nilai bersifat estimasi pasar saat penyusunan proposal dan akan disesuaikan saat rekap belanja; platform RuView tidak menimbulkan biaya lisensi karena open-source.

Tabel 3.2 Rencana biaya penelitian

| **Komponen**                                                       | **Jumlah** | **Estimasi Biaya (Rp)** |
|--------------------------------------------------------------------|------------|-------------------------|
| ESP32-S3 (satu access point, dua station, plus satu cadangan)      | 4 unit     | 800.000                 |
| Single board computer (Orange Pi atau Raspberry Pi) + kartu memori | 1 set      | 750.000                 |
| Housing tertutup, pigtail antena, grounding (anti korosi amonia)   | 1 set      | 150.000                 |
| Kamera/WebCam sinkron untuk ground truth pelabelan                 | 1 unit     | 250.000                 |
| Adaptor, kabel, power backup, komponen kecil                       | 1 set      | 200.000                 |
| Operasional mitra kandang dan dokumen kesejahteraan hewan          | —          | 150.000                 |
| Total                                                              | —          | 2.300.000               |

## **3.11 Analisis Risiko dan Rencana Cadangan**

Tabel 3.3 merangkum risiko utama beserta mitigasinya. Setiap risiko dipasangkan dengan rencana cadangan yang menjaga penelitian tetap menghasilkan temuan, sehingga tidak ada satu pun skenario kegagalan yang mengosongkan skripsi.

Tabel 3.3 Risiko utama dan rencana cadangan

| **Risiko**                                                                     | **Dampak Bila Terjadi**                                 | **Mitigasi / Fallback**                                                                                                                             |
|--------------------------------------------------------------------------------|---------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| Kontras Delta-CSI lemah (fisika sinyal kawanan kecil)                          | Sinyal kawanan tidak terbedakan dari noise floor        | Pivot desain pada minggu 3 sebelum pipeline besar dibangun; studi kelayakan tetap menghasilkan karakterisasi sinyal dan protokol uji sebagai temuan |
| Alarm palsu dari konfound terjadwal (pakan, panen, cahaya) dan kipas ventilasi | Control chart salah alarm berulang                      | Log kejadian harian sebagai kovariat; definisi alarm palsu per 24 jam; pengecualian jendela kejadian terjadwal                                      |
| Pseudoreplikasi satu kandang satu kawanan                                      | Hasil terlalu optimistis dan tidak dapat digeneralisasi | Split blok-waktu dengan validasi antar-hari; klaim dibatasi pada studi kelayakan pada satu konteks                                                  |
| Konfound siklus hidup broiler (bobot tumbuh 40 gram menjadi 2 kilogram)        | Baseline bergeser dan z-score adaptif salah alarm       | Mencatat usia awal saat eksperimen dimulai; baseline adaptif per blok; laporan sensitivitas per minggu usia                                         |
| Korosi perangkat akibat amonia dan kelembapan                                  | Node mati di tengah pengumpulan data                    | Housing tertutup, pigtail berkualitas, grounding; spare node minimal satu                                                                           |

# **DAFTAR PUSTAKA**

\[1\] Ma, Y., Zhou, G., & Wang, S. (2019). WiFi sensing with channel state information: A survey. ACM Computing Surveys, 52(3), 1–36. https://doi.org/10.1145/3310194

\[2\] Hernandez, S. M., & Bulut, E. (2020). Lightweight and standalone IoT based WiFi sensing for active repositioning and mobility. Proceedings of the IEEE International Conference on WoWMoM 2020. https://doi.org/10.1109/WoWMoM49955.2020.00056

\[3\] Hao, Q., Li, K., Wang, Z., & Lin, F. (2019). An animal respiration monitoring system based on channel state information of Wi-Fi network. Proceedings of the ACM ICIT 2019, 283–289. https://doi.org/10.1145/3377170.3377196

\[4\] Lu, M., Li, K., Hao, Q., & Lin, F. (2019). Monitoring pig respiration frequency using Wi-Fi wireless sensing technology. Transactions of the Chinese Society of Agricultural Engineering, 35(24), 183–190. https://doi.org/10.11975/j.issn.1002-6819.2019.24.022

\[5\] Hao, Q., Lin, F., Wang, Z., Guo, X., & Lu, M. (2020). Recognition of mounting behavior of dairy cows based on Wi-Fi wireless sensing. Transactions of the Chinese Society of Agricultural Engineering, 36(19), 168–176. https://doi.org/10.11975/j.issn.1002-6819.2020.19.019

\[6\] Yang, X., Zhao, Y., Street, G. M., Huang, Y., Filip To, S. D., & Purswell, J. L. (2021). Classification of broiler behaviours using triaxial accelerometer and machine learning. Animal, 15(7), 100269. https://doi.org/10.1016/j.animal.2021.100269

\[7\] Campbell, J., Miller, L., Diaz-Chito, K., Hong, J., McLaughlin, N., Parvinzamir, S., Martinez Del Rincon, J., & O’Connell, N. (2024). A computer vision approach to monitor activity in commercial broiler chickens using trajectory-based clustering analysis. Computers and Electronics in Agriculture. https://doi.org/10.1016/j.compag.2023.108591

\[8\] Okinda, C., Lu, M., Liu, L., Nyalala, I., Muneri, C., Wang, C., Zhang, M., & Shen, M. (2019). A machine vision system for early detection and prediction of sick birds: A broiler chicken model. Biosystems Engineering, 188, 229–242. https://doi.org/10.1016/j.biosystemseng.2019.09.015

\[9\] He, G., Chen, S., Yu, X., Hayat, M. M., He, J., Pan, J., & Lin, H. (2022). Research progress in the early warning of chicken diseases by monitoring clinical symptoms. Applied Sciences, 12(11), 5601. https://doi.org/10.3390/app12115601

\[10\] Antonini, M., Pincheira, M., Vecchio, M., & Antonelli, F. (2023). An adaptable and unsupervised TinyML anomaly detection system for extreme industrial environments. Sensors, 23(4), 2344. https://doi.org/10.3390/s23042344
