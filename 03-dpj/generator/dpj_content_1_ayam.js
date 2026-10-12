// dpj_content_1_ayam.js — DPJ 1: Kandang Ayam Broiler (garis unggas, reformulasi dewan)
"use strict";

module.exports = {
  fileName: "DPJ-1_Proposal_Judul_Kandang_Ayam_Broiler.docx",
  docLabel: "PROPOSAL PENGAJUAN JUDUL SKRIPSI",
  subjectLine: "Opsi Alat 1 dari 3 \u2014 Pemantauan WiFi CSI pada Kandang Ayam Broiler",
  headerTitle: "Proposal Pengajuan Judul Skripsi \u2014 Kandang Ayam Broiler (WiFi CSI pada ESP32)",
  judulUtama: "Estimasi Indeks Aktivitas Kawanan Broiler Berbasis Wi-Fi Channel State Information pada ESP32: Studi Kelayakan Pemantauan Dini Kesehatan Unggas",
  alternatif: [
    { kategori: "Alternatif 1", judul: "Deteksi Perubahan Aktivitas Kawanan Ayam Berbasis Wi-Fi CSI untuk Sistem Peringatan Dini di Peternakan Rakyat", catatan: "Orientasi aplikasi peternakan rakyat; metrik alarm yang jujur (alarm palsu per 24 jam, precision@k) harus ditetapkan sejak bab metode." },
    { kategori: "Alternatif 2", judul: "Sistem Monitoring Perilaku Kawanan Unggas Device-Free Berbasis Wi-Fi CSI pada ESP32 dengan Dataset Publik", catatan: "Arah publikasi internasional; hanya dipakai bila jalur label proxy etis terkonfirmasi berjalan dan dataset dapat dirilis dengan DOI." },
  ],
  chapters: [
    {
      h1: "1. Latar Belakang",
      paras: [
        "Penyakit unggas pada peternakan skala kecil dan menengah masih sering terdeteksi terlambat. Keterlambatan deteksi menyebabkan penyebaran ke seluruh kawanan, kenaikan mortalitas, dan kerugian ekonomi yang berarti bagi peternak rakyat yang mengelola 10 hingga 50 ekor per siklus. Tinjauan sistematis He dan kawan-kawan menunjukkan bahwa peringatan dini penyakit ayam selama ini bertumpu pada pemantauan gejala klinis, dan seluruh moda pemantauan otomatis yang tersedia mengandalkan kamera atau sensor lekat yang mahal serta rumit bagi peternak kecil [9]. Kondisi ini membuka kebutuhan akan metode pemantauan yang murah, tanpa kamera saat operasi, dan tidak menuntut pemasangan perangkat pada tiap ekor.",
        "Wi-Fi Channel State Information (CSI) menawarkan jalur alternatif yang menarik. CSI adalah data per-subcarrier yang melaporkan bagaimana sinyal Wi-Fi termodulasi oleh lingkungan fisik, sehingga gerakan benda di antara pemancar dan penerima meninggalkan jejak yang terukur pada amplitudo dan fase sinyal. Survei Ma dan kawan-kawan mengkatalogkan kemampuan moda ini untuk manusia, mulai dari pengenalan aktivitas, deteksi jatuh, hingga estimasi respirasi [1]. Pada ternak besar, CSI telah terbukti memantau respirasi babi dengan akurasi tinggi di kandang nyata [3] [4] dan mengenali perilaku estrus sapi perlah [5]. Sementara itu, Hernandez dan Bulut membuktikan bahwa sensing Wi-Fi berbasis CSI dapat dijalankan pada perangkat murah kelas Internet of Things, sehingga hambatan biaya perangkat keras semakin rendah [2].",
        "Meskipun demikian, pencarian literatur yang dilakukan sebelum penyusunan proposal ini tidak menemukan satu pun publikasi Wi-Fi CSI pada unggas, termasuk pada tinjauan peringatan dini penyakit ayam yang menyebut tiga moda utama tanpa menyebut Wi-Fi [9]. Pemantauan broiler hingga kini didominasi akselerometer lekat [6] dan computer vision [7] [8]. Dengan demikian, penerapan CSI pada kawanan unggas kecil-kecil banyak merupakan wilayah yang belum dipetakan. Klaim kebaruan yang jujur adalah sensing kolektif device-free pada kawanan kecil, bukan klaim pertama untuk hewan secara umum, karena babi dan sapi telah mendahului [3] [4] [5].",
        "Rencana awal penelitian ini yang menjanjikan deteksi dini penyakit per-ekor telah direview secara kritis dan dinyatakan tidak defensibel. Ada tiga alasan struktural. Pertama, fisika sinyal: satu ayam sakit di kawanan 30 ekor hanya menyumbang sekitar 2 hingga 10 persen gangguan total, dan amplitudo Doppler skala dengan massa tubuh sehingga broiler dua kilogram menghasilkan gangguan puluhan kali lebih lemah daripada ternak besar. Kedua, tidak ada kelas positif: contoh ayam sakit terverifikasi tidak akan tersedia dalam satu semester, sehingga metrik klasifikasi seperti macro F1 tinggi tidak terdefinisi secara metodologis. Ketiga, atribusi individu tidak mungkin tanpa kamera pada setiap ekor. Konsekuensinya, unit analisis harus digeser dari individu ke kawanan, dan target pengukuran harus digeser dari deteksi penyakit ke estimasi indeks aktivitas kolektif.",
        "Berdasarkan reformulasi tersebut, proposal ini menawarkan studi kelayakan estimasi indeks aktivitas kawanan broiler menggunakan Wi-Fi CSI pada ESP32. Sistem memantau tingkat aktivitas kolektif kawanan secara kontinyu; bila indeks menyimpang dari pola baseline hari-hari sebelumnya, sistem mengirim peringatan kepada peternak; sistem tidak dan tidak akan mengidentifikasi ayam mana yang sakit. Dengan posisi sebagai studi kelayakan, penelitian ini tetap menghasilkan temuan berharga berupa karakteristik sinyal, protokol pengukuran, dan dataset awal, sekalipun kontras sinyal terbukti lemah. Tabel 1 merangkum usulan judul utama beserta dua alternatif yang dipersiapkan untuk didiskusikan dengan pembimbing.",
      ],
      tables: [{
        caption: "Tabel N Usulan judul penelitian",
        widths: [16, 50, 34],
        headers: ["Kategori", "Usulan Judul", "Catatan Pemetaan"],
        rows: [
          ["Utama", "Estimasi Indeks Aktivitas Kawanan Broiler Berbasis Wi-Fi Channel State Information pada ESP32: Studi Kelayakan Pemantauan Dini Kesehatan Unggas", "Setiap kata terpetakan ke hasil yang dapat dibuktikan dalam satu semester; frasa studi kelayakan memberi ruang keluar yang elegan bila sinyal lemah."],
          ["Alternatif 1", "Deteksi Perubahan Aktivitas Kawanan Ayam Berbasis Wi-Fi CSI untuk Sistem Peringatan Dini di Peternakan Rakyat", "Dipilih bila pembimbing menuntut orientasi aplikasi; metrik alarm jujur ditetapkan sejak bab metode."],
          ["Alternatif 2", "Sistem Monitoring Perilaku Kawanan Unggas Device-Free Berbasis Wi-Fi CSI pada ESP32 dengan Dataset Publik", "Dipilih bila arah publikasi internasional dan jalur label proxy etis terkonfirmasi."],
        ],
      }],
    },
    {
      h1: "2. Rumusan Masalah dan Batasan",
      subs: [
        {
          h2: "2.1 Rumusan Masalah",
          paras: ["Tiga pertanyaan penelitian berikut dirumuskan agar setiap jawabannya dapat dipetakan langsung ke protokol pengukuran yang tersedia dalam satu semester."],
          numbered: [
            "Sejauh mana sinyal Wi-Fi CSI yang ditangkap ESP32 menghasilkan kontras yang dapat diandalkan antara kondisi kandang kosong, satu ekor bergerak, dan kawanan penuh bergerak terhadap noise floor (uji Delta-CSI)?",
            "Seberapa konsisten indeks aktivitas kawanan hasil agregasi energi motion-band CSI terhadap referensi aktivitas dari kamera sinkron pada tiap window pengamatan?",
            "Seberapa efektif control chart berbasis z-score adaptif pada indeks aktivitas mendeteksi perubahan pola kawanan dengan tingkat alarm palsu paling banyak satu per 24 jam dan precision@k minimal 0,5 terhadap audit kamera retrospektif?",
          ],
        },
        {
          h2: "2.2 Batasan Masalah",
          paras: ["Batasan berikut disusun agar janji penelitian tetap berada di dalam wilayah yang dapat dibuktikan, sesuai hasil review kritis terhadap rencana awal."],
          bullets: [
            "Unit analisis adalah kawanan 10 hingga 15 ekor broiler dalam satu kandang, bukan ayam per-ekor; atribusi individu dinyatakan di luar lingkup.",
            "Tidak ada kelas positif penyakit terverifikasi; evaluasi utama memakai metrik yang jujur untuk kondisi tanpa label, dan jalur sekunder hanya berjalan bila event proxy etis berlabel tersedia.",
            "Kamera hanya dipakai pada fase pelabelan dan audit; saat operasi harian sistem berjalan tanpa kamera.",
            "Objek terbatas pada satu kandang mitra 【lokasi kandang】, sehingga desain evaluasi memakai split blok-waktu untuk mengelola risiko pseudoreplikasi.",
            "Sistem diposisikan sebagai alat bantu peringatan dini untuk peternak, bukan alat diagnosis medis hewan.",
          ],
        },
      ],
    },
    {
      h1: "3. Tujuan dan Manfaat",
      subs: [
        {
          h2: "3.1 Tujuan Penelitian",
          numbered: [
            "Mengukur kelayakan fisik sinyal Wi-Fi CSI pada ESP32 untuk sensing kawanan broiler melalui uji Delta-CSI tiga skenario di kandang nyata sebagai gerbang go/no-go.",
            "Membangun indeks aktivitas kawanan kontinyu dari energi motion-band amplitudo CSI dengan window 60 detik, dan memvalidasinya terhadap referensi kamera sinkron.",
            "Mengevaluasi kemampuan control chart z-score adaptif memberi peringatan perubahan pola kawanan dengan metrik alarm palsu per 24 jam dan precision@k.",
            "Menyusun protokol pengukuran, log kejadian harian, dan dataset awal CSI kawanan unggas yang terdokumentasi untuk penelitian lanjutan.",
          ],
        },
        {
          h2: "3.2 Manfaat Penelitian",
          paras: [
            "Bagi peternakan rakyat, penelitian ini menguji kemungkinan alat peringatan dini berbiaya rendah yang tidak menuntut kamera di kandang dan tidak memasang sensor pada tiap ekor, sehingga dapat dipelihara peternak skala 10 hingga 50 ekor. Bagi komunitas ilmiah, penelitian ini mengisi celah literatur sensing kolektif device-free pada kawanan unggas kecil-kecil banyak yang belum dipetakan siapa pun, dan menyediakan karakteristik sinyal serta protokol evaluasi yang dapat direplikasi. Bagi mahasiswa, penelitian ini melatih kemampuan eksperimen fisik, pengolahan sinyal, evaluasi model time-series, dan tata kelola klaim yang jujur terhadap keterbatasan data.",
          ],
        },
      ],
    },
    {
      h1: "4. Tinjauan Pustaka",
      paras: [
        "Fondasi teknis sensing Wi-Fi berbasis CSI telah matang pada manusia. Survei Ma dan kawan-kawan mengkatalogkan pengenalan aktivitas, deteksi jatuh, estimasi respirasi, dan lokalisasi sebagai keluarga aplikasi utama, beserta tantangan sinyal seperti sensitivitas lingkungan dan kebutuhan kalibrasi [1]. Baru-baru ini perangkat murah turut dibuktikan memadai: Hernandez dan Bulut menunjukkan sensing Wi-Fi mandiri berbasis mikrokontroler kelas IoT untuk deteksi mobilitas aktif [2], yang menjadi dasar pemilihan ESP32 sebagai perangkat capture pada penelitian ini.",
        "Pada ternak, CSI telah dieksplorasi untuk hewan besar per-individu. Hao dan kawan-kawan memantau respirasi babi menggunakan informasi kanal jaringan Wi-Fi di lingkungan kandang nyata [3], Lu dan kawan-kawan melanjutkan pemantauan frekuensi respirasi babi dengan teknologi wireless sensing [4], dan Hao serta kawan-kawan mengenali perilaku mounting sapi perah dari sinyal Wi-Fi dengan ribuan sampel uji [5]. Ketiganya memakai satu sampai dua hewan besar per area dan perangkat riset kelas atas, sehingga hasilnya belum tentu berlaku untuk kawanan unggas kecil dengan perangkat murah satu antena.",
        "Pemantauan broiler yang ada kini memakai moda lain. Yang dan kawan-kawan mengklasifikasi perilaku broiler dari akselerometer triaksial dengan machine learning [6]; Campbell dan kawan-kawan memantau aktivitas broiler komersial melalui clustering trajektori berbasis kamera [7]; Okinda dan kawan-kawan membangun sistem machine vision untuk deteksi dini burung sakit pada model broiler [8]. Ketiga moda ini menuntut biaya perangkat, pemeliharaan, atau kamera yang sulit bagi peternak kecil, dan ketiganya juga menegaskan bahwa indikator perilaku mendahului gejala klinis. Review He dan kawan-kawan merangkum kemajuan peringatan dini penyakit ayam dari gejala klinis dan menempatkan pemantauan otomatis sebagai arah penting [9].",
        "Untuk pengolahan sinyal tanpa label, pendekatan anomali tanpa supervisi telah dibuktikan layak pada lingkungan industri ekstrem oleh Antonini dan kawan-kawan dengan sistem TinyML adaptif [10]. Pola pendekatan ini sejalan dengan kebutuhan penelitian ini: control chart dan z-score adaptif pada indeks aktivitas yang tidak memerlukan contoh kegagalan, dengan audit retrospektif sebagai penilaian kualitas alarm.",
        "Dari pemetaan tersebut, celah penelitian teridentifikasi dengan jelas: tidak ditemukan satu pun publikasi Wi-Fi CSI pada unggas, dan literatur CSI ternak belum pernah menghadapi kawanan kecil-kecil banyak. Klaim kebaruan penelitian ini dibatasi secara disiplin: studi kelayakan pertama sensing kolektif device-free Wi-Fi CSI pada kawanan broiler menggunakan mikrokontroler murah pada rentang literatur yang berhasil dicari. Klaim pertama untuk hewan secara umum gugur karena babi dan sapi telah mendahului [3] [4] [5], dan klaim kebaruan geografis tidak dipakai.",
      ],
    },
    {
      h1: "5. Basis Teknologi: Platform RuView",
      paras: [
        "Penelitian ini tidak membangun rantai pengambilan sinyal dari nol. Sistem dibangun di atas RuView, sebuah proyek open-source (github.com/ruvnet/RuView) yang menyediakan firmware ESP32 untuk penangkapan CSI, server pengolahan sinyal berbasis Rust, dashboard web, serta saluran alert melalui MQTT dan Home Assistant. Posisi RuView pada penelitian ini adalah infrastruktur capture, pipeline DSP dasar, dan alert; logika khusus unggas tetap menjadi tanggung jawab penelitian. RuView juga menyediakan modul ternak ind_livestock_monitor yang memuat desain alert stillness, escape, dan labored breathing untuk unggas; modul ini dipakai sebagai acuan desain, bukan dijalankan langsung pada skenario kandang broiler.",
        "Tabel 2 memetakan fitur RuView yang dipakai beserta status keterujinya, agar janji teknis proposal ini selalu berada di atas fitur yang benar-benar terukur. Dua hal jujur perlu dicatat sejak awal. Pertama, filter bandpass napas dan jantung pada RuView memiliki rentang yang dikodekan permanen untuk manusia pada semua lapisan; bila penelitian melanjutkan ke estimasi napas unggas, konstanta filter wajib diubah di firmware dan server, dan denyut jantung ayam (250 hingga 330 denyut per menit) tidak mungkin diukur tanpa desain ulang filter. Kedua, fitur pose on-device pada RuView berstatus stub dengan kualitas terukur yang sangat rendah, sehingga tidak dijanjikan sama sekali dalam proposal ini.",
      ],
      tables: [{
        caption: "Tabel N Pemetaan fitur RuView untuk alat kandang broiler",
        widths: [30, 42, 28],
        headers: ["Fitur RuView", "Peran pada Penelitian", "Status"],
        rows: [
          ["Capture CSI ESP32 + streaming UDP (format frame ADR-018)", "Sumber data utama seluruh eksperimen", "Terukur (MEASURED)"],
          ["Presence heuristik (varians fase, kalibrasi ambient 60 detik)", "Deteksi ada tidaknya aktivitas kawanan", "Terukur; risiko alarm palsu pada kipas ventilasi"],
          ["Motion-band power + akselerasi fase", "Bahan baku indeks aktivitas kawanan (inti skripsi)", "Terukur"],
          ["Kalibrasi ruang kosong minimal 600 frame", "Baseline kandang kosong sebelum eksperimen", "Terukur"],
          ["Recording JSONL + adaptive classifier (latih di bawah 1 detik)", "Dataset percontohan dan klasifikator baseline", "Terukur"],
          ["Dashboard web + MQTT + notifikasi", "Saluran peringatan ke peternak", "Terukur"],
          ["Modul ind_livestock_monitor (stillness, escape, labored breathing)", "Acuan desain alert kesehatan kawanan", "DSP nyata; validasi hewan nol"],
          ["Bandpass napas 0,1-0,5 Hz", "Estimasi napas unggas bila dilanjutkan", "Konstanta wajib diubah di semua lapisan"],
          ["Pose 17-keypoint on-device", "Tidak dipakai", "Stub terukur (PCK@20 3,0 persen) \u2014 terlarang dijanjikan"],
        ],
      }],
    },
    {
      h1: "6. Metodologi Penelitian",
      subs: [
        {
          h2: "6.1 Desain Penelitian",
          paras: [
            "Penelitian ini adalah studi kelayakan kuantitatif dengan desain pre-eksperimental satu kelompok dan gerbang go/no-go pada minggu ketiga. Desain dipilih agar keputusan lanjut atau pivot terjadi sebelum pipeline besar dibangun, mengikuti prinsip bahwa biaya menemukan kelemahan di awal jauh lebih murah daripada di akhir. Seluruh keputusan teknis diikat pada hasil terukur, bukan pada preferensi, dan setiap tahap menghasilkan artefak yang tetap bernilai sekalipun penelitian dihentikan pada gerbang tersebut.",
          ],
        },
        {
          h2: "6.2 Objek, Lokasi, dan Kesejahteraan Hewan",
          paras: [
            "Objek penelitian adalah kawanan broiler 10 hingga 15 ekor pada kandang mitra 【lokasi kandang】 dengan siklus pemeliharaan normal. Tiga ESP32 (satu access point, dua station) dipasang TX-RX mengapit area kawanan agar geometri antena memotong zona Fresnel area bergerak. Penelitian bersifat observasional terhadap hewan, namun tetap memerlukan persetujuan kesejahteraan hewan; dokumen persetujuan disiapkan sebelum pengambilan data, dan jalur kelas positif dikoordinasikan dengan puskeswan atau fakultas kedokteran hewan sejak awal untuk event proxy etis berlabel seperti vaksinasi, heat stress ringan, atau pembatasan pakan terkontrol.",
          ],
        },
        {
          h2: "6.3 Protokol Pengumpulan Data dan Kalibrasi",
          paras: [
            "Gerbang pertama adalah uji Delta-CSI fisik pada minggu pertama hingga ketiga. Dua ESP32 diposisikan mengapit kandang, lalu amplitudo CSI direkam window 60 detik untuk tiga skenario: kandang kosong, satu ayam bergerak, dan kawanan penuh bergerak; ketiganya dibandingkan terhadap noise floor. Setelah gerbang lolos, kalibrasi baseline kandang kosong direkam minimal 600 frame mengikuti protokol RuView, kemudian data eksperimen dikumpulkan dalam blok hari berturut-turut dengan kamera sinkron untuk ground truth dan log kejadian harian (jadwal pakan, cahaya, suhu, kelembapan litter, panen) sebagai kovariat. Evaluasi memakai split blok-waktu, yaitu latih pada hari A sampai B dan uji pada hari C, karena split acak pada data time-series membocorkan informasi dan membuat hasil terlalu optimistis.",
          ],
        },
        {
          h2: "6.4 Ekstraksi Fitur dan Model",
          paras: [
            "Fitur diekstraksi dari amplitudo CSI saja karena fase ESP32 satu antena berderau tinggi; fase dibuang dan keputusan ini dinyatakan sejak desain fitur. Fitur per window 60 detik meliputi energi motion-band, varians amplitudo, dan statistik akselerasi fase. Model utama adalah z-score adaptif terhadap baseline hari-hari sebelumnya, dipadukan satu klasifikator SVM RBF yang dieksekusi di laptop; komponen CNN dan TFLite dinyatakan sebagai pekerjaan lanjutan dan tidak dijanjikan dalam lingkup skripsi ini. Pemilihan model sederhana disengaja: target penelitian adalah kelayakan sinyal dan kejujuran metrik, bukan prestasi klasifikasi.",
          ],
        },
        {
          h2: "6.5 Metrik Evaluasi",
          paras: [
            "Evaluasi memakai dua jalur yang jujur terhadap kondisi tanpa kelas positif. Jalur utama, yang selalu berjalan, memakai control chart pada indeks aktivitas dengan dua metrik: alarm palsu per 24 jam dengan target paling banyak satu per hari, dan precision@k minimal 0,5 berdasarkan audit kamera retrospektif pada k event teratas. Jalur sekunder hanya berjalan bila event proxy etis berlabel tersedia, memakai F1 minimal 0,70 pada level kawanan dengan split blok-waktu. Target macro F1 di atas 0,80 sengaja tidak dijanjikan karena secara metodologis tidak terdefinisi tanpa minimal 50 event anomali.",
          ],
        },
        {
          h2: "6.6 Gerbang Go/No-Go",
          paras: [
            "Minggu ketiga ditetapkan sebagai gerbang keputusan. Bila aktivitas kawanan penuh tidak terlihat dari derau pada uji Delta-CSI, judul, metrik, dan arsitektur dipivot sebelum satu baris pipeline besar ditulis, dan kegagalan ini dicatat sebagai temuan studi kelayakan, bukan kegagalan skripsi. Bila kontras sinyal memadai, penelitian lanjut ke pengumpulan dataset dan evaluasi sesuai rencana. Kriteria kontras minimum ditetapkan bersama pembimbing pada pertemuan penjajakan judul sehingga keputusan go/no-go bersifat objektif.",
          ],
        },
      ],
    },
    {
      h1: "7. Manajemen Risiko dan Rencana Fallback",
      paras: ["Tabel 3 merangkum risiko utama beserta mitigasinya. Setiap risiko dipasangkan dengan rencana fallback yang menjaga penelitian tetap menghasilkan temuan, sehingga tidak ada satu pun skenario kegagalan yang mengosongkan skripsi."],
      tables: [{
        caption: "Tabel N Risiko utama dan mitigasi",
        widths: [30, 30, 40],
        headers: ["Risiko", "Dampak Bila Terjadi", "Mitigasi / Fallback"],
        rows: [
          ["Kontras Delta-CSI lemah (fisika sinyal kawanan kecil)", "Sinyal kawanan tidak terbedakan dari noise floor", "Pivot desain pada minggu 3 sebelum pipeline besar dibangun; studi kelayakan tetap menghasilkan karakterisasi sinyal dan protokol uji sebagai temuan"],
          ["Alarm palsu dari konfound terjadwal (pakan, panen, cahaya) dan kipas ventilasi", "Control chart salah alarm berulang", "Log kejadian harian sebagai kovariat; definisi alarm palsu per 24 jam; pengecualian jendela kejadian terjadwal"],
          ["Pseudoreplikasi satu kandang satu kawanan", "Hasil terlalu optimistis dan tidak dapat digeneralisasi", "Split blok-waktu dengan validasi antar-hari; klaim dibatasi pada studi kelayakan pada satu konteks"],
          ["Konfound siklus hidup broiler (bobot tumbuh 40 gram menjadi 2 kilogram)", "Baseline bergeser dan z-score adaptif salah alarm", "Mencatat usia awal saat eksperimen dimulai; baseline adaptif per blok; laporan sensitivitas per minggu usia"],
          ["Korosi perangkat akibat amonia dan kelembapan", "Node mati di tengah pengumpulan data", "Housing tertutup, pigtail berkualitas, grounding; spare node minimal satu"],
        ],
      }],
    },
    {
      h1: "8. Jadwal Penelitian",
      paras: ["Jadwal disusun untuk satu semester (sekitar 4,5 bulan) dengan gerbang keputusan dini pada minggu ketiga dan eksperimen yang dipadatkan setelah gerbang lolos, sebagaimana Tabel 4."],
      tables: [{
        caption: "Tabel N Jadwal penelitian satu semester",
        widths: [22, 46, 32],
        headers: ["Periode", "Aktivitas", "Keluaran"],
        rows: [
          ["Minggu 1-3", "Pembelian alat; pemasangan 3 ESP32; uji Delta-CSI tiga skenario (kosong, satu ekor, kawanan); dokumen kesejahteraan hewan; kalibrasi baseline 600 frame", "Keputusan go/no-go; baseline kandang; izin etik"],
          ["Minggu 4-7", "Pengumpulan dataset blok hari A-B; kamera sinkron untuk ground truth; log kejadian harian; identifikasi event proxy etis bersama puskeswan", "Dataset mentah berlabel proxy + log kovariat"],
          ["Minggu 8-11", "Ekstraksi fitur amplitudo-only window 60 detik; z-score adaptif + SVM RBF; split blok-waktu (latih A-B, uji C); control chart dan precision@k", "Model baseline + metrik dua jalur"],
          ["Minggu 12-15", "Analisis hasil; penyetelan ambang; audit kamera retrospektif; penyusunan dataset rilis (opsional, dengan DOI) bila pembimbing menyetujui", "Hasil evaluasi utuh + catatan rilis dataset"],
          ["Minggu 16-18", "Penulisan naskah skripsi; finalisasi bab metode dan hasil; persiapan sidang", "Naskah skripsi siap sidang"],
        ],
      }],
    },
    {
      h1: "9. Estimasi Anggaran",
      paras: ["Tabel 5 merangkum estimasi anggaran perangkat dan operasional. Nilai bersifat estimasi pasar saat penyusunan proposal dan akan disesuaikan saat rekap belanja."],
      tables: [{
        caption: "Tabel N Estimasi anggaran perangkat dan operasional",
        widths: [44, 26, 30],
        headers: ["Komponen", "Jumlah", "Estimasi Biaya"],
        rows: [
          ["ESP32-S3 (satu access point, dua station, plus satu cadangan)", "4 unit", "Rp 800.000"],
          ["Single board computer (Orange Pi atau Raspberry Pi) + kartu memori", "1 set", "Rp 750.000"],
          ["Housing tertutup, pigtail antena, grounding (anti korosi amonia)", "1 set", "Rp 150.000"],
          ["Kamera/WebCam sinkron untuk ground truth pelabelan", "1 unit", "Rp 250.000"],
          ["Adaptor, kabel, power backup, komponen kecil", "1 set", "Rp 200.000"],
          ["Operasional mitra kandang dan dokumen kesejahteraan hewan", "\u2014", "Rp 150.000"],
          ["Total", "\u2014", "Rp 2.300.000"],
        ],
      }],
    },
    {
      h1: "10. Daftar Referensi",
      refs: [
        "[1] Ma, Y., Zhou, G., & Wang, S. (2019). WiFi sensing with channel state information: A survey. ACM Computing Surveys, 52(3), 1\u201336. https://doi.org/10.1145/3310194",
        "[2] Hernandez, S. M., & Bulut, E. (2020). Lightweight and standalone IoT based WiFi sensing for active repositioning and mobility. Proceedings of the IEEE International Conference on WoWMoM 2020. https://doi.org/10.1109/WoWMoM49955.2020.00056",
        "[3] Hao, Q., Li, K., Wang, Z., & Lin, F. (2019). An animal respiration monitoring system based on channel state information of Wi-Fi network. Proceedings of the ACM ICIT 2019, 283\u2013289. https://doi.org/10.1145/3377170.3377196",
        "[4] Lu, M., Li, K., Hao, Q., & Lin, F. (2019). Monitoring pig respiration frequency using Wi-Fi wireless sensing technology. Transactions of the Chinese Society of Agricultural Engineering, 35(24), 183\u2013190. https://doi.org/10.11975/j.issn.1002-6819.2019.24.022",
        "[5] Hao, Q., Lin, F., Wang, Z., Guo, X., & Lu, M. (2020). Recognition of mounting behavior of dairy cows based on Wi-Fi wireless sensing. Transactions of the Chinese Society of Agricultural Engineering, 36(19), 168\u2013176. https://doi.org/10.11975/j.issn.1002-6819.2020.19.019",
        "[6] Yang, X., Zhao, Y., Street, G. M., Huang, Y., Filip To, S. D., & Purswell, J. L. (2021). Classification of broiler behaviours using triaxial accelerometer and machine learning. Animal, 15(7), 100269. https://doi.org/10.1016/j.animal.2021.100269",
        "[7] Campbell, J., Miller, L., Diaz-Chito, K., Hong, J., McLaughlin, N., Parvinzamir, S., Martinez Del Rincon, J., & O\u2019Connell, N. (2024). A computer vision approach to monitor activity in commercial broiler chickens using trajectory-based clustering analysis. Computers and Electronics in Agriculture. https://doi.org/10.1016/j.compag.2023.108591",
        "[8] Okinda, C., Lu, M., Liu, L., Nyalala, I., Muneri, C., Wang, C., Zhang, M., & Shen, M. (2019). A machine vision system for early detection and prediction of sick birds: A broiler chicken model. Biosystems Engineering, 188, 229\u2013242. https://doi.org/10.1016/j.biosystemseng.2019.09.015",
        "[9] He, G., Chen, S., Yu, X., Hayat, M. M., He, J., Pan, J., & Lin, H. (2022). Research progress in the early warning of chicken diseases by monitoring clinical symptoms. Applied Sciences, 12(11), 5601. https://doi.org/10.3390/app12115601",
        "[10] Antonini, M., Pincheira, M., Vecchio, M., & Antonelli, F. (2023). An adaptable and unsupervised TinyML anomaly detection system for extreme industrial environments. Sensors, 23(4), 2344. https://doi.org/10.3390/s23042344",
      ],
    },
  ],
};
