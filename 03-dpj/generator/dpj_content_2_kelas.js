// dpj_content_2_kelas.js — DPJ 2: Ruang Kelas SLB — REMAKE struktur BAB I-III
// Mengikuti skill proposal-writing (korpus TRSE UNM): proposal hanya BAB I-III + DAFTAR PUSTAKA.
"use strict";

module.exports = {
  fileName: "DPJ-2_Proposal_Judul_Ruang_Kelas_SLB.docx",
  docLabel: "PROPOSAL PENGAJUAN JUDUL SKRIPSI",
  subjectLine: "Opsi Alat 2 dari 4 \u2014 Pemantauan Wi-Fi CSI pada Ruang Kelas SLB",
  headerTitle: "Proposal Pengajuan Judul Skripsi \u2014 Ruang Kelas SLB (Wi-Fi CSI pada ESP32)",
  judulUtama: "Sistem Pemantauan Aktivitas dan Keselamatan Siswa Kelas SLB Berbasis Wi-Fi Channel State Information pada ESP32: Studi Kelayakan Tanpa Kamera",
  alternatif: [
    { kategori: "Judul Alternatif 1", judul: "Deteksi Jatuh dan Anomali Aktivitas Siswa Berkebutuhan Khusus Berbasis Wi-Fi CSI pada Ruang Kelas: Studi Kelayakan Pemantauan Privasi-Preservasi" },
    { kategori: "Judul Alternatif 2", judul: "Kalibrasi Parameter Wi-Fi Sensing untuk Pemantauan Aktivitas Anak Berkebutuhan Khusus pada Ruang Kelas SLB Berbasis ESP32" },
  ],
  chapters: [
    // ================= BAB I =================
    {
      h1: "BAB I", h1b: "PENDAHULUAN",
      subs: [
        {
          h2: "1.1 Latar Belakang",
          paras: [
            "Perkembangan teknologi telah memengaruhi berbagai bidang layanan pendidikan, termasuk cara sekolah menjaga keselamatan dan kenyamanan peserta didiknya di dalam kelas. Pada Sekolah Luar Biasa (SLB), tuntutan tersebut lebih besar karena sekolah melayani siswa dengan kebutuhan pendampingan yang lebih intens daripada sekolah umum. Guru dan pendamping perlu mengawasi aktivitas, keselamatan, dan kondisi siswa di ruang kelas secara terus-menerus, sementara rasio pendamping terhadap siswa sering kali terbatas. Kejadian seperti anak jatuh, pingsan, atau tidak bergerak terlalu lama di pojok kelas tidak selalu segera terlihat, terutama pada jam pembelajaran individual di mana perhatian guru terbagi. Kondisi tersebut menunjukkan bahwa kebutuhan akan alat bantu peringatan dini di ruang kelas nyata dan spesifik pada konteks ini.",
            "Solusi pemantauan yang paling umum adalah kamera, tetapi pemasangan kamera di ruang kelas anak berkebutuhan khusus menimbulkan beban etis yang berat: kepekaan terhadap identitas, penyimpanan rekaman, potensi penyalahgunaan, serta kekhawatiran orang tua. Wi-Fi Channel State Information (CSI) merupakan alternatif yang secara prinsip tidak merekam wajah dan tidak membedakan identitas individu, sekaligus mampu melaporkan ada tidaknya orang, intensitas gerakan, hingga kejadian jatuh dari modulasi sinyal antara pemancar dan penerima. Ma et al. (2019) menjelaskan bahwa keluarga kemampuan sensing Wi-Fi pada manusia telah mencakup pengenalan aktivitas dan deteksi jatuh [1], dan Jiang et al. (2018) menempatkannya di dalam ekosistem smart home yang menuntut privasi [3]. Pada penelitian ini, CSI digunakan untuk memantau kondisi ruang kelas secara agregat tanpa menyentuh identitas siapa pun.",
            "Kemampuan deteksi jatuh dengan CSI telah terbukti pada perangkat Wi-Fi umum sejak lama. Wang et al. (2017) membangun RT-Fall, sistem deteksi jatuh real-time tanpa kontak pada perangkat Wi-Fi komoditas [6], sementara Zhou et al. (2024) menunjukkan bahwa tantangan utama deteksi jatuh CSI kini bergeser ke generalisasi antar-individu (cross-individual) [7]. Temuan terakhir ini justru relevan bagi penelitian ini: sistem perlu dikalibrasi ulang pada populasi yang berbeda dari populasi dewasa neurotipikal pada umumnya data latih, dan itulah yang terjadi bila sistem dirancang untuk anak SLB. Sebaliknya, penghitungan jumlah orang dari CSI terbatas; Brena et al. (2021) menunjukkan penurunan kualitas penghitungan kerumunan saat jumlah subjek meningkat [8], sehingga klaim penghitungan harus dikelola hati-hati.",
            "Argumen privasi CSI perlu dinyatakan secara proporsional, bukan berlebihan. Mosharaf et al. (2024) merangkum bahwa sinyal Wi-Fi pada prinsipnya masih dapat dipakai untuk pengenalan identitas pada skenario tertentu [10]. Namun pada arsitektur sensing yang dipakai penelitian ini, sistem ditempatkan sebagai pelaporan kondisi ruangan tanpa penyimpanan biometrik, mode privasi aktif membuang fitur biometrik sebelum data keluar dari node, dan tata kelola akses mengikuti persetujuan sekolah serta orang tua. Dengan desain semacam ini, keunggulan etis tanpa kamera menjadi argumen utama proposal, bukan sekadar bonus.",
            "Pada level literatur, aplikasi CSI untuk ruang kelas umum telah ada pada tema kehadiran dan penghitungan, namun pencarian awal yang dilakukan pada penyusunan proposal ini belum menemukan penerapan CSI pada ruang kelas pendidikan inklusi atau SLB, sehingga celah ini berlabel terbatas-pencarian (search-limited) dan akan diverifikasi ulang bersama pembimbing. Berdasarkan uraian tersebut, penelitian ini dilakukan untuk menguji kelayakan sistem pemantauan aktivitas dan keselamatan siswa kelas SLB tanpa kamera pada ESP32, dengan kalibrasi ulang parameter sensing dari populasi dewasa ke populasi anak sebagai kontribusi eksplisit. Tabel 1.1 merangkum usulan judul utama dan dua judul alternatifnya.",
          ],
          tables: [{
            caption: "Tabel 1.1 Usulan judul penelitian",
            widths: [16, 50, 34],
            headers: ["Kategori", "Usulan Judul", "Catatan Pemetaan"],
            rows: [
              ["Utama", "Sistem Pemantauan Aktivitas dan Keselamatan Siswa Kelas SLB Berbasis Wi-Fi Channel State Information pada ESP32: Studi Kelayakan Tanpa Kamera", "Setiap kata terpetakan ke fitur yang terukur (presence, motion, fall, anomali inaktivitas) dan ke protokol izin yang realistis dalam satu semester."],
              ["Alternatif 1", "Deteksi Jatuh dan Anomali Aktivitas Siswa Berkebutuhan Khusus Berbasis Wi-Fi CSI pada Ruang Kelas: Studi Kelayakan Pemantauan Privasi-Preservasi", "Dipilih bila fokus keselamatan diutamakan; jatuh dievaluasi lewat simulasi etis di matras."],
              ["Alternatif 2", "Kalibrasi Parameter Wi-Fi Sensing untuk Pemantauan Aktivitas Anak Berkebutuhan Khusus pada Ruang Kelas SLB Berbasis ESP32", "Dipilih bila kalibrasi dewasa-ke-anak dijadikan kontribusi utama; cocok untuk arah publikasi metode."],
            ],
          }],
        },
        {
          h2: "1.2 Rumusan Masalah",
          paras: [
            "Berdasarkan latar belakang permasalahan yang telah diuraikan serta untuk menjawab permasalahan yang menjadi fokus dalam penelitian ini, maka dapat dirumuskan beberapa rumusan masalah yang akan dikaji lebih lanjut. Rumusan masalah pada penelitian ini sebagai berikut.",
          ],
          numbered: [
            "Bagaimana rancangan uji Delta-CSI pada ruang kelas SLB menghasilkan deteksi kehadiran dan intensitas aktivitas yang andal pada kondisi kelas kosong, kelas terisi sesi pembelajaran, dan transisi di antaranya?",
            "Bagaimana kinerja deteksi jatuh simulasi dan anomali inaktivitas pada populasi anak setelah ambang sistem yang dirancang untuk dewasa disetel ulang, dilihat dari sensitivitas dan jumlah alarm palsu per jam?",
            "Bagaimana selisih parameter sensing antara populasi dewasa dan populasi anak SLB didokumentasikan sehingga menghasilkan rekomendasi kalibrasi yang dapat dipakai ulang oleh sekolah lain?",
          ],
        },
        {
          h2: "1.3 Tujuan Penelitian",
          paras: [
            "Penelitian ini bertujuan untuk menguji kelayakan sistem pemantauan aktivitas dan keselamatan siswa kelas SLB berbasis Wi-Fi CSI tanpa kamera pada ESP32. Adapun tujuan dari penelitian ini adalah sebagai berikut.",
          ],
          numbered: [
            "Merancang uji Delta-CSI kondisi kelas kosong, kelas terisi, dan transisi pada ruang kelas SLB sebagai gerbang go/no-go kelayakan fisik sinyal.",
            "Mengevaluasi deteksi kehadiran, intensitas aktivitas, deteksi jatuh simulasi, dan anomali inaktivitas pada populasi anak dengan ambang yang disetel ulang dari nilai dewasa.",
            "Mendokumentasikan selisih parameter sensing dewasa terhadap populasi anak SLB dan menyusun rekomendasi kalibrasi serta protokol izin berjenjang yang dapat direplikasi sekolah lain.",
          ],
        },
        {
          h2: "1.4 Batasan Masalah",
          paras: [
            "Agar penelitian ini memiliki ruang lingkup yang jelas dan terarah sesuai dengan tujuan yang telah ditetapkan, maka ditentukan batasan masalah guna membatasi pembahasan terhadap aspek-aspek yang relevan dengan topik penelitian. Adapun batasan masalah pada penelitian ini sebagai berikut.",
          ],
          numbered: [
            "Lingkup terbatas pada satu ruang kelas mitra di \u3010Nama SLB\u3011 dengan maksimal 10 siswa hadir per sesi eksperimen.",
            "Sistem tidak mengidentifikasi individu; seluruh keluaran berupa status ruangan dan peristiwa, bukan profil perilaku tiap anak.",
            "Deteksi jatuh dievaluasi melalui simulasi etis yang dilakukan pendamping dewasa di atas matras, bukan eksperimen pada anak.",
            "Sistem diposisikan sebagai alat bantu pendamping dan peringatan dini, bukan alat diagnosis atau alat medis.",
            "Ambang sistem bawaan dirancang untuk orang dewasa dan perlu disetel ulang; proses penyetelan itulah yang menjadi bagian dari temuan, bukan kelemahan tersembunyi.",
            "Penelitian ini tidak membahas penghitungan jumlah siswa secara teliti, identifikasi individu, penilaian perilaku klinis, maupun penggunaan kamera pada saat sistem beroperasi.",
          ],
        },
        {
          h2: "1.5 Manfaat Penelitian",
          paras: [
            "Pengukuran parameter sensing pada populasi anak masih jarang dipublikasikan, sehingga hasil penelitian ini berkontribusi pada literatur sekaligus pada praktik sekolah. Proses pengukuran yang bergerbang dan tata kelola izin yang tertulis memberi contoh penelitian lapangan yang aman pada lingkungan sensitif. Manfaat penelitian ini diuraikan sebagai berikut.",
          ],
          subs: [
            {
              h3: "1.5.1 Manfaat Teoretis",
              paras: [
                "Penelitian ini diharapkan dapat menjadi referensi dalam pengembangan pemantauan aktivitas berbasis Wi-Fi CSI pada populasi anak, yang literaturnya selama ini didominasi populasi dewasa [1] [6] [7]. Selain itu, penelitian ini juga dapat menjadi acuan penerapan kalibrasi ulang parameter sensing, evaluasi deteksi jatuh simulasi yang etis, dan tata kelola privasi pada penelitian sensing di ruang pendidikan.",
              ],
            },
            {
              h3: "1.5.2 Manfaat Praktis",
              paras: [
                "Manfaat praktis penelitian ini mencakup empat kelompok penerima manfaat sebagai berikut.",
              ],
              numbered: [
                "Bagi Peneliti: pengalaman eksperimen lapangan pada lingkungan sensitif, manajemen risiko etis, dan pengukuran sistem nyata dari ujung ke ujung.",
                "Bagi Sekolah SLB dan Guru: alat peringatan dini yang menambah mata kedua bagi pendamping tanpa memasang kamera di ruang kelas, dengan tata kelola persetujuan yang jelas bagi orang tua.",
                "Bagi Orang Tua/Wali: dokumen tata kelola data dan hak menarik diri yang transparan sebagai dasar kepercayaan.",
                "Bagi Praktisi Teknologi: tabel parameter kalibrasi dewasa-ke-anak dan protokol izin yang dapat dipakai ulang pada pengembangan sensing untuk populasi rentan.",
              ],
            },
          ],
        },
      ],
    },
    // ================= BAB II =================
    {
      h1: "BAB II", h1b: "KAJIAN PUSTAKA",
      subs: [
        {
          h2: "2.1 Wi-Fi Channel State Information",
          paras: [
            "Wi-Fi Channel State Information (CSI) merupakan informasi per-subcarrier yang melaporkan kondisi kanal propagasi sinyal Wi-Fi, mencakup amplitudo dan fase pada tiap subcarrier. Gerakan manusia di antara pemancar dan penerima mengubah jalur pantulan sinyal sehingga meninggalkan pola yang terukur pada CSI, dan pola itulah yang dipakai sebagai sumber data sensing tanpa kamera. Ma et al. (2019) mengkatalogkan pengenalan aktivitas, deteksi jatuh, dan lokalisasi sebagai keluarga aplikasi utama beserta tantangan kalibrasi dan sensitivitas lingkungan [1]. Jiang et al. (2018) menempatkan sensing Wi-Fi sebagai lapisan persepsi smart home dengan aplikasi kesehatan dan keselamatan [3], sementara Al-qaness (2019) membuktikan pengenalan mikro-aktivitas manusia tanpa perangkat dari sinyal Wi-Fi [5] dan Zou et al. (2019) memperlihatkan kombinasi Wi-Fi dan visi untuk pengenalan aktivitas yang lebih akurat [4]. Kumpulan kemampuan tersebut menunjukkan granularitas fitur yang tersedia dari CSI untuk konteks ruang kelas pada penelitian ini.",
          ],
        },
        {
          h2: "2.2 Mikrokontroler ESP32",
          paras: [
            "ESP32 adalah mikrokontroler murah dengan radio Wi-Fi bawaan yang mampu mengekspor CSI melalui firmware khusus. Hernandez dan Bulut (2020) menunjukkan bahwa sensing Wi-Fi mandiri dapat berjalan pada perangkat kelas Internet of Things untuk deteksi mobilitas aktif tanpa perangkat kelas riset yang mahal [2]. Untuk penelitian ini, kemampuan tersebut berarti dua node ESP32 dapat dipasang di ruang kelas dengan biaya yang masih terjangkau, mudah dipindahkan antar-ruang, dan tidak mengubah aktivitas pembelajaran. Karakteristik perangkat murah ini juga menuntut disiplin kalibrasi karena kualitas antena dan derau lingkungan lebih bervariasi daripada kartu jaringan kelas riset.",
          ],
        },
        {
          h2: "2.3 Platform RuView",
          paras: [
            "Sistem dibangun di atas RuView, proyek open-source (github.com/ruvnet/RuView) yang menyediakan firmware ESP32 untuk penangkapan CSI, server pengolahan berbasis Rust, mesin status semantik untuk status ruangan, dashboard web, serta alert melalui MQTT dan Home Assistant. Fitur deteksi jatuh RuView bekerja dari akselerasi fase dengan debouncing di bawah 200 milidetik, sedangkan anomali inaktivitas dipantau melalui mesin status no_movement. Mode privasi bawaan membuang fitur biometrik sebelum data keluar dari node dan diaktifkan penuh pada penelitian ini karena objek penelitian adalah anak-anak.",
            "Tabel 2.1 memetakan fitur RuView yang dipakai beserta status keterujinya. Dua catatan jujur perlu dinyatakan sejak awal. Pertama, ambang mesin status (durasi inaktivitas, deteksi tidur, distress) dikalibrasi pada orang dewasa, sehingga penyetelan ulang untuk populasi anak adalah bagian dari penelitian, bukan asumsi bahwa sistem langsung cocok. Kedua, fitur penghitungan orang pada RuView bersifat heuristik dan menurun kualitasnya pada lebih dari dua sampai tiga subjek, sehingga tidak dijanjikan sebagai keluaran utama.",
          ],
          tables: [{
            caption: "Tabel 2.1 Pemetaan fitur RuView untuk alat ruang kelas SLB",
            widths: [30, 42, 28],
            headers: ["Fitur RuView", "Peran pada Penelitian", "Status"],
            rows: [
              ["Capture CSI ESP32 + streaming UDP (format frame ADR-018)", "Sumber data utama", "Terukur (MEASURED)"],
              ["Presence + motion level/energy", "Kehadiran dan intensitas aktivitas kelas", "Terukur"],
              ["Mesin status room_active", "Status kelas aktif atau tidak", "Terukur"],
              ["Deteksi jatuh (akselerasi fase + debounce di bawah 200 ms)", "Peringatan kejadian jatuh (simulasi etis)", "Terukur"],
              ["No_movement (30 menit) + sec_panic_motion + possible-distress", "Anomali inaktivitas dan gerakan panik", "Ambang dewasa, wajib disetel ulang untuk anak"],
              ["Privacy mode (strip fitur biometrik)", "Kepatuhan etika untuk ruang kelas anak", "Terukur, diaktifkan penuh"],
              ["MQTT ke Home Assistant + notifikasi", "Penerusan alert ke perangkat guru", "Terukur"],
              ["Kalibrasi 600 frame + enrollment 8 anchor per kelas", "Kalibrasi ruangan sekitar 4 menit per kelas", "Terukur"],
              ["Person counting heuristik", "Tidak dijanjikan sebagai keluaran utama", "Lemah pada lebih dari 2-3 subjek"],
              ["Pose 17-keypoint on-device", "Tidak dipakai", "Stub terukur (PCK@20 3,0 persen) \u2014 terlarang dijanjikan"],
            ],
          }],
        },
        {
          h2: "2.4 Deteksi Jatuh dan Anomali Aktivitas",
          paras: [
            "Deteksi jatuh adalah kemampuan sensing Wi-Fi yang paling matang untuk konteks keselamatan kelas. Wang et al. (2017) membangun RT-Fall pada perangkat Wi-Fi komoditas dengan latensi real-time [6], dan Zhou et al. (2024) kemudian menyoroti persoalan cross-individual pada deteksi jatuh CSI serta menawarkan metode time-continuous untuk memperbaiki generalisasi [7]. Untuk konteks penelitian ini, ada dua pelajaran penting: kemampuan deteksi jatuh realistis untuk dijanjikan pada skenario simulasi etis, dan penyesuaian pada populasi berbeda adalah persoalan penelitian yang sah, bukan cacat desain. Anomali inaktivitas dilengkapi oleh kemampuan mikro-aktivitas dari Al-qaness (2019) yang menunjukkan bahwa granularitas halus gerakan manusia tetap terbaca dari sinyal Wi-Fi [5], sehingga kondisi anak yang terlalu lama tidak bergerak dapat dipantau sebagai anomali pada tingkat ruangan.",
          ],
        },
        {
          h2: "2.5 Privasi pada Sensing Wi-Fi",
          paras: [
            "Argumen privasi dibangun secara proporsional terhadap literatur. Mosharaf et al. (2024) menunjukkan bahwa identifikasi manusia dari sinyal Wi-Fi memang mungkin pada skenario tertentu [10], sehingga klaim privasi tidak disampaikan sebagai sinyal Wi-Fi pasti anonim, melainkan sebagai keputusan desain: mode privasi membuang fitur biometrik, sistem tidak menyimpan profil individu, dan akses data diatur oleh persetujuan sekolah dan orang tua. Brena et al. (2021) menunjukkan penghitungan kerumunan device-free berbasis deskriptor CSI multi-link yang presisinya bergantung pada jumlah subjek dan skenario [8], sehingga penelitian ini menjanjikan kehadiran dan intensitas, bukan penghitungan teliti per orang. Ketersediaan dataset publik seperti eHealth CSI dari Galdino et al. (2023) juga menjadi praktik baik pengumpulan dan pembagian data aktivitas CSI yang dapat ditiru [9]. Pemosisian ini jujur terhadap literatur sekaligus memperkuat argumen tanpa kamera di ruang kelas anak.",
          ],
        },
        {
          h2: "2.6 Penelitian Terdahulu",
          paras: [
            "Tabel 2.2 membandingkan penelitian terdahulu yang paling relevan dari sisi sinyal, fokus keselamatan, konteks ruang belajar, kebebasan kamera, dan keterjangkauan perangkat.",
          ],
          tables: [{
            caption: "Tabel 2.2 Perbandingan penelitian terdahulu",
            widths: [36, 13, 15, 15, 10, 11],
            headers: ["Peneliti (Tahun) dan Judul Singkat", "Sinyal CSI", "Fokus Jatuh/Anomali", "Konteks Ruang Belajar", "Bebas Kamera", "Perangkat Murah"],
            centerCols: [1, 2, 3, 4, 5],
            rows: [
              ["Wang et al. (2017) \u2014 RT-Fall deteksi jatuh real-time Wi-Fi", "\u221a", "\u221a", "\u2212", "\u221a", "\u2212"],
              ["Zhou et al. (2024) \u2014 TCS-Fall lintas-individu", "\u221a", "\u221a", "\u2212", "\u221a", "\u2212"],
              ["Brena et al. (2021) \u2014 crowd counting multi-link CSI", "\u221a", "\u2212", "\u2212", "\u221a", "\u2212"],
              ["Zou et al. (2019) \u2014 HAR multimodal Wi-Fi + visi", "\u221a", "\u2212", "\u2212", "\u2212", "\u2212"],
              ["Al-qaness (2019) \u2014 mikro-aktivitas manusia", "\u221a", "\u2212", "\u2212", "\u221a", "\u2212"],
              ["Galdino et al. (2023) \u2014 dataset publik eHealth CSI", "\u221a", "\u2212", "\u2212", "\u221a", "\u221a"],
              ["Penelitian Ini", "\u221a", "\u221a", "\u221a", "\u221a", "\u221a"],
            ],
          }],
          paras: [
            "Berdasarkan tabel perbandingan di atas, terlihat bahwa penelitian-penelitian sebelumnya kuat pada deteksi jatuh dan pengenalan aktivitas pada populasi dewasa, namun belum ada yang menempatkannya pada ruang kelas pendidikan inklusi atau SLB dengan tata kelola izin yang eksplisit. Belum banyak penelitian yang secara spesifik mengkalibrasi ulang parameter sensing Wi-Fi dari populasi dewasa ke populasi anak berkebutuhan khusus, terdapat juga beberapa celah masalah (gap) yang belum terselesaikan secara simultan oleh peneliti sebelumnya. Penelitian ini mengisi celah tersebut dengan langkah-langkah berikut.",
          ],
          numbered: [
            "Menempatkan pemantauan aktivitas dan keselamatan CSI pada konteks ruang kelas SLB dengan status kebaruan konteks yang dinyatakan terbatas-pencarian dan terbuka untuk diverifikasi.",
            "Menjadikan penyetelan parameter dewasa-ke-anak sebagai kontribusi kalibrasi yang terdokumentasi, bukan asumsi diam-diam.",
            "Membangun protokol izin berjenjang dan tata kelola privasi tanpa kamera yang dapat direplikasi sekolah lain.",
          ],
        },
      ],
    },
    // ================= BAB III =================
    {
      h1: "BAB III", h1b: "METODE PENELITIAN",
      subs: [
        {
          h2: "3.1 Tahapan Penelitian",
          paras: [
            "Penelitian dalam proposal ini dilaksanakan melalui beberapa tahapan yang tersusun secara sistematis sehingga membentuk suatu alur penelitian yang terstruktur. Tahap pertama adalah studi literatur, yaitu pemetaan deteksi jatuh CSI, penghitungan orang, dan privasi sensing yang berujung pada penetapan metrik evaluasi. Tahap kedua adalah perancangan sistem, mencakup penempatan node di ruang kelas, rencana kalibrasi, dan protokol izin berjenjang. Tahap ketiga adalah implementasi, yaitu pemasangan perangkat, uji Delta-CSI, pengumpulan data sesi pembelajaran, dan penyetelan ambang untuk populasi anak. Tahap terakhir adalah pengujian dan evaluasi, yaitu evaluasi presence, anomali inaktivitas, dan deteksi jatuh simulasi, diakhiri penyusunan rekomendasi kalibrasi. Apabila dalam proses pengujian ditemukan kendala seperti alarm palsu tinggi atau izin yang tertunda, maka dilakukan evaluasi dan perbaikan secara berulang hingga sistem dapat dievaluasi secara adil.",
            "Penelitian ini adalah studi kelayakan kuantitatif dengan gerbang go/no-go pada minggu ketiga. Rangkaian evaluasi disusun dari skenario paling murah (uji sinyal di kelas kosong dan terisi) menuju skenario yang menuntut izin lebih dalam (sesi pembelajaran terjadwal dan simulasi jatuh). Setiap tahap menghasilkan artefak tetap, mulai dari karakterisasi sinyal hingga protokol izin, sehingga penelitian tetap bernilai sekalipun berhenti pada salah satu gerbang.",
          ],
        },
        {
          h2: "3.2 Studi Literatur",
          paras: [
            "Studi literatur dilakukan terhadap tiga kelompok sumber, yaitu sensing Wi-Fi CSI pada manusia, deteksi jatuh dan penghitungan orang, serta privasi dan etika sensing. Sumber diutamakan dari jurnal dan prosiding terindeks (IEEE, ACM, MDPI, Elsevier) pada rentang 2017 hingga 2024. Setiap referensi diverifikasi melalui API Crossref dengan mencocokkan judul, penulis, tahun, dan venue terhadap DOI terdaftar sehingga tidak ada referensi fiktif. Status kebaruan konteks SLB diberi label terbatas-pencarian sejak awal dan direncanakan diverifikasi ulang bersama pembimbing sebelum judul difinalkan.",
          ],
        },
        {
          h2: "3.3 Perancangan Arsitektur Sistem",
          paras: [
            "Arsitektur sistem terdiri atas tiga lapisan. Lapisan sensing berisi dua node ESP32 (satu access point, satu station) yang dipasang pada dua sisi ruang kelas sehingga area bergerak siswa berada di antara keduanya. Lapisan pengolahan berisi server RuView pada single board computer yang menjalankan dekoding frame, kalibrasi ruangan, mesin status semantik (room_active, no_movement), dan deteksi jatuh berbasis akselerasi fase. Lapisan penyajian berisi dashboard web dan penerusan alert melalui MQTT ke perangkat guru atau pendamping. Seluruh lapisan berjalan dengan mode privasi aktif yang membuang fitur biometrik sebelum data keluar dari node.",
          ],
        },
        {
          h2: "3.4 Perancangan Perangkat Keras",
          paras: [
            "Perangkat keras utama adalah empat unit ESP32-S3 (dua terpasang, satu cadangan, satu untuk pengembangan) dengan dudukan dinding yang dapat dipindah antar-ruang tanpa perawatan khusus. Server pengolahan berjalan pada single board computer (Orange Pi atau Raspberry Pi) dengan penyimpanan lokal terenkripsi sederhana untuk rekaman sesi. Matras keselamatan dipersiapkan untuk simulasi jatuh yang dilakukan pendamping dewasa, dan tidak ada perangkat lain yang dikenakan pada siswa. Kamera tidak menjadi bagian dari sistem operasional; jika digunakan, kamera hanya menyala pada sesi pelabelan atau audit yang telah disepakati guru.",
          ],
        },
        {
          h2: "3.5 Perancangan Perangkat Lunak dan Dataset",
          paras: [
            "Perangkat lunak penelitian memakai alur bawaan RuView dengan penyesuaian. Tiap kelas dikalibrasi dengan protokol minimal 600 frame baseline ruang kosong dan enrollment 8 anchor (sekitar 4 menit) sebelum sesi pengambilan data. Dataset disusun dari sesi pembelajaran normal, transisi istirahat, dan skenario terstruktur yang dipandu guru, dengan catatan kejadian dari pendamping sebagai label referensi. Evaluasi memakai split blok-waktu dengan data latih dan uji pada hari yang berbeda untuk mencegah kebocoran temporal. Penyetelan ambang dilakukan sistematis: mulai dari nilai dewasa bawaan, mengukur alarm palsu dan kehilangan deteksi per kombinasi ambang, lalu merekam nilai yang layak untuk populasi anak beserta interval kondisinya sebagai tabel parameter rekomendasi.",
          ],
        },
        {
          h2: "3.6 Lokasi, Partisipan, dan Etika",
          paras: [
            "Lokasi penelitian adalah satu ruang kelas mitra di \u3010Nama SLB\u3011. Partisipan eksperimen aktif adalah pendamping dewasa (peneliti dan asisten) untuk semua skenario simulasi; aktivitas siswa hanya direkam sebagai data sensing pada sesi pembelajaran normal yang telah mendapat izin. Izin diambil berjenjang: persetujuan kepala sekolah, pemberitahuan dan persetujuan orang tua/wali dengan hak menarik diri kapan pun tanpa konsekuensi, serta kesepakatan dengan guru kelas tentang sesi dan durasi. Mode privasi RuView aktif sejak instalasi, tidak ada penyimpanan rekaman wajah, dan seluruh data dianonimkan pada tingkat ruangan. Posisi sistem dinyatakan eksplisit sebagai deteksi kondisi untuk membantu pendamping, bukan pengawasan perilaku siswa.",
          ],
        },
        {
          h2: "3.7 Rencana Pengujian",
          paras: [
            "Rencana pengujian terdiri atas tiga kelompok. Pengujian pertama adalah uji Delta-CSI pada minggu pertama hingga ketiga: kelas kosong, satu orang bergerak terstruktur, dan kelas terisi aktivitas normal, dibandingkan terhadap noise floor sebagai gerbang go/no-go. Pengujian kedua adalah uji fungsi pemantauan: akurasi deteksi kehadiran pada tingkat ruangan per window, intensitas aktivitas, dan anomali inaktivitas pada sesi pembelajaran normal. Pengujian ketiga adalah uji keselamatan: deteksi jatuh simulasi oleh pendamping dewasa di atas matras dengan pengukuran sensitivitas dan latensi peringatan. Setiap alert yang muncul diaudit terhadap catatan pendamping untuk menilai benar-salahnya sebelum masuk ke tabel hasil.",
          ],
        },
        {
          h2: "3.8 Evaluasi dan Kriteria Keberhasilan",
          paras: [
            "Metrik utama meliputi akurasi deteksi kehadiran pada tingkat ruangan per window, sensitivitas dan alarm palsu per jam untuk anomali inaktivitas, serta sensitivitas deteksi jatuh simulasi di matras dengan latensi peringatan. Kualitas kalibrasi diukur dari perbaikan alarm palsu setelah penyetelan dibandingkan ambang dewasa bawaan. Seluruh evaluasi memakai split blok-waktu, dan setiap kejadian alert diaudit terhadap catatan pendamping untuk menilai benar-salahnya.",
            "Minggu ketiga menentukan arah penelitian sebagai gerbang go/no-go. Bila kehadiran dan gerakan di kelas tidak terbedakan dari derau, desain dipivot pada minggu yang sama; opsi pivot mencakup penempatan node ulang, pengubahan frekuensi antena, atau pengalihan fokus ke kalibrasi dengan klaim yang lebih sempit. Bila kontras memadai, penelitian lanjut ke sesi pengumpulan data penuh sesuai izin. Keputusan dievaluasi bersama pembimbing dan disampaikan kepada sekolah secara transparan.",
          ],
        },
        {
          h2: "3.9 Rencana Kegiatan dan Jadwal Penelitian",
          paras: [
            "Jadwal satu semester disusun dengan gerbang go/no-go pada minggu ketiga, sebagaimana Tabel 3.1. Persetujuan etik sengaja diletakkan paling awal karena menjadi prasyarat seluruh pengambilan data pada siswa.",
          ],
          tables: [{
            caption: "Tabel 3.1 Jadwal penelitian satu semester",
            widths: [22, 46, 32],
            headers: ["Periode", "Aktivitas", "Keluaran"],
            rows: [
              ["Minggu 1-3", "Surat izin berjenjang ke sekolah dan orang tua; pemasangan node; uji Delta-CSI (kosong, satu orang, kelas terisi) \u2014 GERBANG GO/NO-GO; kalibrasi 600 frame + 8 anchor", "Keputusan go/no-go; kelas terkalibrasi; dokumen persetujuan"],
              ["Minggu 4-7", "Sesi pembelajaran normal terekam sebagai data sensing; skenario terstruktur dipandu guru; simulasi jatuh di matras oleh pendamping", "Dataset blok hari + catatan kejadian pendamping"],
              ["Minggu 8-11", "Penyetelan ambang dewasa ke populasi anak; evaluasi presence, anomali inaktivitas, dan deteksi jatuh simulasi; split blok-waktu", "Tabel parameter anak + metrik sensitivitas/alarm palsu"],
              ["Minggu 12-15", "Audit alert bersama guru; analisis hasil; perbaikan threshold; penyusunan rekomendasi kalibrasi", "Hasil evaluasi utuh + rekomendasi parameter"],
              ["Minggu 16-18", "Penulisan naskah skripsi; finalisasi protokol izin sebagai lampiran; persiapan sidang", "Naskah skripsi siap sidang"],
            ],
          }],
        },
        {
          h2: "3.10 Rencana Biaya Penelitian",
          paras: [
            "Tabel 3.2 merangkum rencana biaya dalam Rupiah. Perangkat dipilih serendah mungkin karena fokus penelitian adalah kelayakan, bukan produksi.",
          ],
          tables: [{
            caption: "Tabel 3.2 Rencana biaya penelitian",
            widths: [44, 26, 30],
            headers: ["Komponen", "Jumlah", "Estimasi Biaya (Rp)"],
            rows: [
              ["ESP32-S3 (satu access point, satu station, plus dua cadangan)", "4 unit", "800.000"],
              ["Single board computer (Orange Pi atau Raspberry Pi) + kartu memori", "1 set", "750.000"],
              ["Matras keselamatan untuk simulasi jatuh", "1 unit", "200.000"],
              ["Bracket, kabel, adaptor, komponen kecil", "1 set", "150.000"],
              ["Operasional lokasi dan percetakan dokumen izin", "\u2014", "100.000"],
              ["Total", "\u2014", "2.000.000"],
            ],
          }],
        },
        {
          h2: "3.11 Analisis Risiko dan Rencana Cadangan",
          paras: [
            "Tabel 3.3 merangkum risiko utama. Risiko etis ditempatkan di baris pertama karena berhak membatalkan penelitian lebih cepat daripada risiko teknis mana pun.",
          ],
          tables: [{
            caption: "Tabel 3.3 Risiko utama dan rencana cadangan",
            widths: [30, 30, 40],
            headers: ["Risiko", "Dampak Bila Terjadi", "Mitigasi / Fallback"],
            rows: [
              ["Izin sekolah atau orang tua tidak terkumpul", "Pengumpulan data pada siswa tidak dapat berjalan", "Urutkan persetujuan sebelum beli alat; siapkan lokasi alternatif; seluruh skenario simulasi tetap dapat berjalan dengan pendamping dewasa"],
              ["Alarm palsu tinggi pada populasi anak (perilaku atipikal dianggap anomali)", "Kepercayaan guru menurun, sistem dimatikan", "Pelibatan guru dalam penandaan kejadian; penyetelan ambang per kelas; framing hasil sebagai temuan kalibrasi"],
              ["Kontras Delta-CSI lemah di kelas dengan furnitur banyak", "Sinyal tidak andal", "Pivot penempatan node minggu 3; pemilihan kelas dengan geometri lebih baik; temuan tetap berupa karakterisasi sinyal kelas"],
              ["Kecurigaan privasi dari wali murid", "Persetujuan rendah", "Mode privasi aktif, tanpa kamera, tanpa penyimpanan profil; dokumen tata kelola data untuk wali; hak menarik diri kapan pun"],
              ["Penghitungan orang tidak akurat", "Janji fitur meleset", "Kehadiran biner dan intensitas sebagai keluaran utama; penghitungan tidak dijanjikan"],
            ],
          }],
        },
      ],
    },
    // ================= DAFTAR PUSTAKA =================
    {
      h1: "DAFTAR PUSTAKA",
      refs: [
        "[1] Ma, Y., Zhou, G., & Wang, S. (2019). WiFi sensing with channel state information: A survey. ACM Computing Surveys, 52(3), 1\u201336. https://doi.org/10.1145/3310194",
        "[2] Hernandez, S. M., & Bulut, E. (2020). Lightweight and standalone IoT based WiFi sensing for active repositioning and mobility. Proceedings of the IEEE International Conference on WoWMoM 2020. https://doi.org/10.1109/WoWMoM49955.2020.00056",
        "[3] Jiang, H., Cai, C., Ma, X., Yang, Y., & Liu, J. (2018). Smart home based on WiFi sensing: A survey. IEEE Access, 6. https://doi.org/10.1109/ACCESS.2018.2812887",
        "[4] Zou, H., Yang, J., Das, H. P., Liu, H., Zhou, Y., & Spanos, C. J. (2019). WiFi and vision multimodal learning for accurate and robust device-free human activity recognition. Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops (CVPRW). https://doi.org/10.1109/CVPRW.2019.00056",
        "[5] Al-qaness, M. A. A. (2019). Device-free human micro-activity recognition method using WiFi signals. Geo-spatial Information Science, 22. https://doi.org/10.1080/10095020.2019.1612600",
        "[6] Wang, H., Zhang, D., Wang, Y., Ma, J., Wang, Y., & Li, S. (2017). RT-Fall: A real-time and contactless fall detection system with commodity WiFi devices. IEEE Transactions on Mobile Computing, 16. https://doi.org/10.1109/TMC.2016.2557795",
        "[7] Zhou, Z., Liu, Z., Liu, Y., Zhao, Y., Wang, J., & Zhang, B. (2024). TCS-Fall: Cross-individual fall detection system based on channel state information and time-continuous stack method. Digital Health. https://doi.org/10.1177/20552076241259047",
        "[8] Brena, R. F., Escudero, E., Vargas-Rosales, C., Galvan-Tejada, C. E., & Munoz, D. (2021). Device-free crowd counting using multi-link Wi-Fi CSI descriptors in Doppler spectrum. Electronics, 10(3), 315. https://doi.org/10.3390/electronics10030315",
        "[9] Galdino, I., Soto, J. C. H., Caballero, E., Ferreira, V., Ramos, T. C., Albuquerque, C., & Muchaluat-Saade, D. C. (2023). eHealth CSI: A Wi-Fi CSI dataset of human activities. IEEE Access. https://doi.org/10.1109/ACCESS.2023.3294429",
        "[10] Mosharaf, M., Kwak, J. B., & Choi, W. (2024). WiFi-based human identification with machine learning: A comprehensive survey. Sensors, 24(19), 6413. https://doi.org/10.3390/s24196413",
      ],
    },
  ],
};
