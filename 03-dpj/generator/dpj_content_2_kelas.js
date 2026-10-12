// dpj_content_2_kelas.js — DPJ 2: Ruang Kelas SLB (garis sensing manusia, tanpa kamera)
"use strict";

module.exports = {
  fileName: "DPJ-2_Proposal_Judul_Ruang_Kelas_SLB.docx",
  docLabel: "PROPOSAL PENGAJUAN JUDUL SKRIPSI",
  subjectLine: "Opsi Alat 2 dari 3 \u2014 Pemantauan WiFi CSI pada Ruang Kelas SLB",
  headerTitle: "Proposal Pengajuan Judul Skripsi \u2014 Ruang Kelas SLB (WiFi CSI pada ESP32)",
  judulUtama: "Sistem Pemantauan Aktivitas dan Keselamatan Siswa Kelas SLB Berbasis Wi-Fi Channel State Information pada ESP32: Studi Kelayakan Tanpa Kamera",
  alternatif: [
    { kategori: "Alternatif 1", judul: "Deteksi Jatuh dan Anomali Aktivitas Siswa Berkebutuhan Khusus Berbasis Wi-Fi CSI pada Ruang Kelas: Studi Kelayakan Pemantauan Privasi-Preservasi", catatan: "Dipilih bila pembimbing ingin fokus pada keselamatan; framing tetap pendampingan, bukan alat klinis." },
    { kategori: "Alternatif 2", judul: "Kalibrasi Parameter Wi-Fi Sensing untuk Pemantauan Aktivitas Anak Berkebutuhan Khusus pada Ruang Kelas SLB Berbasis ESP32", catatan: "Dipilih bila kontribusi kalibrasi threshold dewasa-ke-anak ingin dijadikan sumbangan utama." },
  ],
  chapters: [
    {
      h1: "1. Latar Belakang",
      paras: [
        "Sekolah Luar Biasa (SLB) melayani siswa dengan kebutuhan pendampingan yang lebih intens daripada sekolah umum. Guru dan pendamping perlu mengawasi aktivitas, keselamatan, dan kondisi siswa di ruang kelas secara terus-menerus, sementara rasio pendamping terhadap siswa sering kali terbatas. Kejadian seperti anak jatuh, pingsan, atau tidak bergerak terlalu lama di pojok kelas tidak selalu segera terlihat, terutama pada jam pembelajaran individual di mana perhatian guru terbagi. Kebutuhan akan alat bantu peringatan dini di ruang kelas oleh karena itu nyata dan spesifik pada konteks ini.",
        "Solusi pemantauan yang paling umum adalah kamera, tetapi pemasangan kamera di ruang kelas anak berkebutuhan khusus menimbulkan beban etis yang berat: kepekaan terhadap identitas, penyimpanan rekaman, potensi penyalahgunaan, serta kekhawatiran orang tua. Wi-Fi Channel State Information (CSI) menawarkan alternatif yang secara prinsip tidak merekam wajah dan tidak membedakan identitas individu, sekaligus mampu melaporkan ada tidaknya orang, intensitas gerakan, hingga kejadian jatuh dari modulasi sinyal antara pemancar dan penerima. Survei Ma dan kawan-kawan mengkatalogkan keluarga kemampuan ini pada manusia [1], dan survei Jiang serta kawan-kawan menempatkannya di dalam ekosistem smart home yang menuntut privasi [3].",
        "Kemampuan deteksi jatuh dengan CSI telah terbukti pada perangkat Wi-Fi umum sejak lama. Wang dan kawan-kawan membangun RT-Fall, sistem deteksi jatuh real-time tanpa kontak pada perangkat Wi-Fi komoditas [6], sementara Zhou dan kawan-kawan menunjukkan bahwa tantangan utama deteksi jatuh CSI kini bergeser ke generalisasi antar-individu (cross-individual) [7]. Temuan terakhir ini justru relevan bagi penelitian ini: sistem perlu dikalibrasi ulang pada populasi yang berbeda dari populasi dewasa neurotipikal pada umumnya data latih, dan itulah yang terjadi bila sistem dirancang untuk anak SLB. Sebaliknya, penghitungan jumlah orang dari CSI terbatas; pekerjaan penghitungan kerumunan menunjukkan penurunan kualitas saat jumlah subjek meningkat [8], sehingga klaim penghitungan harus dikelola hati-hati.",
        "Argumen privasi CSI perlu dinyatakan secara proporsional, bukan berlebihan. Sinyal Wi-Fi pada prinsipnya masih dapat dipakai untuk pengenalan identitas pada skenario tertentu, sebagaimana dirangkum survei Mosharaf dan kawan-kawan tentang identifikasi manusia berbasis Wi-Fi [10]. Namun pada arsitektur sensing yang dipakai penelitian ini, sistem ditempatkan sebagai pelaporan kondisi ruangan tanpa penyimpanan biometrik, mode privasi aktif membuang fitur biometrik sebelum data keluar dari node, dan tata kelola akses mengikuti persetujuan sekolah serta orang tua. Dengan desain semacam ini, keunggulan etis tanpa kamera menjadi argumen utama proposal, bukan sekadar bonus.",
        "Pada level literatur, aplikasi CSI untuk ruang kelas umum telah ada pada tema kehadiran dan penghitungan, namun pencarian awal yang dilakukan pada penyusunan proposal ini belum menemukan penerapan CSI pada ruang kelas pendidikan inklusi atau SLB, sehingga celah ini berlabel terbatas-pencarian (search-limited) dan akan diverifikasi ulang bersama pembimbing. Proposal ini menawarkan studi kelayakan sistem pemantauan aktivitas dan keselamatan siswa kelas SLB tanpa kamera pada ESP32, dengan kalibrasi ulang parameter sensing dari populasi dewasa ke populasi anak sebagai kontribusi eksplisit. Tabel 1 merangkum usulan judul utama dan dua alternatifnya.",
      ],
      tables: [{
        caption: "Tabel N Usulan judul penelitian",
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
      h1: "2. Rumusan Masalah dan Batasan",
      subs: [
        {
          h2: "2.1 Rumusan Masalah",
          paras: ["Pertanyaan penelitian dirumuskan agar jawabannya menghasilkan keputusan kelayakan yang dapat dipertanggungjawabkan kepada sekolah dan orang tua."],
          numbered: [
            "Sejauh mana sinyal Wi-Fi CSI pada ESP32 menghasilkan deteksi kehadiran dan intensitas aktivitas yang andal di ruang kelas SLB pada kondisi kelas kosong, kelas terisi sesi pembelajaran, dan transisi di antaranya (uji Delta-CSI)?",
            "Seberapa baik deteksi jatuh simulasi dan anomali inaktivitas bekerja pada populasi anak setelah ambang sistem yang dirancang untuk dewasa disetel ulang, dilihat dari sensitivitas dan jumlah alarm palsu per jam?",
            "Seberapa besar selisih parameter sensing antara populasi dewasa dan populasi anak SLB, dan penyesuaian apa yang layak direkomendasikan sebagai kontribusi kalibrasi?",
          ],
        },
        {
          h2: "2.2 Batasan Masalah",
          bullets: [
            "Lingkup terbatas pada satu ruang kelas mitra di 【Nama SLB】 dengan maksimal 10 siswa hadir per sesi eksperimen.",
            "Sistem tidak mengidentifikasi individu; seluruh keluaran berupa status ruangan dan peristiwa, bukan profil perilaku tiap anak.",
            "Deteksi jatuh dievaluasi melalui simulasi etis yang dilakukan pendamping dewasa di atas matras, bukan eksperimen pada anak.",
            "Sistem diposisikan sebagai alat bantu pendamping dan peringatan dini, bukan alat diagnosis atau alat medis.",
            "Ambang sistem bawaan dirancang untuk orang dewasa dan perlu disetel ulang; proses penyetelan itulah yang menjadi bagian dari temuan, bukan kelemahan tersembunyi.",
            "Status kebaruan konteks SLB berlabel terbatas-pencarian dan klaim dibatasi pada studi kelayakan.",
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
            "Mengukur kelayakan fisik sinyal CSI pada ruang kelas SLB melalui uji Delta-CSI kondisi kelas kosong, terisi, dan transisi sebagai gerbang go/no-go.",
            "Mengevaluasi deteksi kehadiran, intensitas aktivitas, deteksi jatuh simulasi, dan anomali inaktivitas pada populasi anak dengan ambang yang disetel ulang.",
            "Mendokumentasikan selisih parameter sensing dewasa terhadap populasi anak SLB dan merumuskan rekomendasi kalibrasi.",
            "Menyusun protokol izin berjenjang dan tata kelola privasi yang dapat direplikasi sekolah lain.",
          ],
        },
        {
          h2: "3.2 Manfaat Penelitian",
          paras: [
            "Bagi sekolah SLB, penelitian ini menguji alat peringatan dini yang menambah mata kedua bagi pendamping tanpa memasang kamera di ruang kelas, dengan tata kelola persetujuan yang jelas bagi orang tua. Bagi komunitas ilmiah, penelitian ini menyediakan data empiris tentang perilaku parameter sensing CSI pada populasi anak yang selama ini jarang dipublikasikan, serta memetakan sejauh mana sistem dewasa dapat dikalibrasi ke populasi berbeda. Bagi mahasiswa, penelitian ini melatih eksperimen lapangan pada lingkungan sensitif, manajemen risiko etis, dan pengukuran sistem nyata dari ujung ke ujung.",
          ],
        },
      ],
    },
    {
      h1: "4. Tinjauan Pustaka",
      paras: [
        "Sensing Wi-Fi berbasis CSI adalah teknologi dewasa pada manusia. Survei Ma dan kawan-kawan mengkatalogkan pengenalan aktivitas, deteksi jatuh, dan lokalisasi beserta tantangan kalibrasi dan sensitivitas lingkungan [1]. Survei Jiang dan kawan-kawan menempatkan sensing Wi-Fi sebagai lapisan persepsi smart home dengan aplikasi kesehatan dan keselamatan [3]. Pada arah multimodal, Zou dan kawan-kawan menggabungkan Wi-Fi dan visi untuk pengenalan aktivitas device-free yang lebih akurat [4], sementara Al-qaness membuktikan pengenalan mikro-aktivitas manusia tanpa perangkat dari sinyal Wi-Fi [5]. Kedua arah ini menunjukkan granularitas fitur yang tersedia dari CSI, termasuk untuk aktivitas halus.",
        "Deteksi jatuh adalah kemampuan yang paling matang untuk konteks keselamatan kelas. Wang dan kawan-kawan membangun RT-Fall pada perangkat Wi-Fi komoditas dengan latensi real-time [6]. Zhou dan kawan-kawan kemudian menyoroti persoalan cross-individual pada deteksi jatuh CSI dan menawarkan metode untuk memperbaiki generalisasi [7]. Untuk konteks penelitian ini, dua pelajaran penting: kemampuan deteksi jatuh realistis dijanjikan, dan penyesuaian pada populasi berbeda adalah persoalan penelitian yang sah, bukan cacat desain.",
        "Penghitungan orang dari CSI harus diperlakukan hati-hati. Brena dan kawan-kawan menunjukkan penghitungan kerumunan device-free berbasis deskriptor CSI multi-link, dengan presisi yang bergantung pada jumlah subjek dan skenario [8]. Pada kelas SLB dengan 6 hingga 10 anak yang bergerak tidak terstruktur, penghitungan pasti tidak seakurat kehadiran biner; oleh karena itu proposal ini menjanjikan kehadiran dan intensitas, bukan penghitungan teliti per orang. Ketersediaan dataset publik seperti eHealth CSI dari Galdino dan kawan-kawan juga menunjukkan praktik baik pengumpulan dan pembagian data aktivitas CSI yang dapat ditiru pada penelitian ini [9].",
        "Argumen privasi dibangun secara proporsional. Survei Mosharaf dan kawan-kawan menunjukkan bahwa identifikasi manusia dari sinyal Wi-Fi memang mungkin pada skenario tertentu [10], sehingga klaim privasi tidak boleh disampaikan sebagai sinyal Wi-Fi pasti anonim, melainkan sebagai keputusan desain: mode privasi membuang fitur biometrik, sistem tidak menyimpan profil individu, dan akses data diatur oleh persetujuan sekolah dan orang tua. Pemosisian ini jujur terhadap literatur sekaligus memperkuat argumen tanpa kamera di ruang kelas anak.",
        "Dari pemetaan tersebut, celah penelitian jelas: literatur CSI untuk kelas umum mencakup kehadiran dan penghitungan, namun belum ditemukan penerapan pada ruang kelas pendidikan inklusi atau SLB pada rentang pencarian yang dilakukan, dan literatur kalibrasi CSI untuk populasi anak juga langka. Klaim kebaruan dibatasi: studi kelayakan sistem pemantauan aktivitas dan keselamatan tanpa kamera pada ruang kelas SLB, dengan kalibrasi parameter dewasa-ke-anak sebagai kontribusi eksplisit. Status terbatas-pencarian dinyatakan terbuka dan akan diverifikasi ulang bersama pembimbing.",
      ],
    },
    {
      h1: "5. Basis Teknologi: Platform RuView",
      paras: [
        "Sistem dibangun di atas RuView, proyek open-source (github.com/ruvnet/RuView) yang menyediakan firmware ESP32 untuk penangkapan CSI, server pengolahan berbasis Rust, mesin status semantik untuk status ruangan, dashboard web, serta alert melalui MQTT dan Home Assistant. Fitur deteksi jatuh RuView bekerja dari akselerasi fase dengan debouncing di bawah 200 milidetik, sedangkan anomali inaktivitas dipantau melalui mesin status no_movement. Mode privasi bawaan membuang fitur biometrik sebelum data keluar dari node dan diaktifkan penuh pada penelitian ini karena objek penelitian adalah anak-anak.",
        "Tabel 2 memetakan fitur RuView yang dipakai beserta status keterujinya. Dua catatan jujur perlu dinyatakan sejak awal. Pertama, ambang mesin status (durasi inaktivitas, deteksi tidur, distress) dikalibrasi pada orang dewasa, sehingga penyetelan ulang untuk populasi anak adalah bagian dari penelitian, bukan asumsi bahwa sistem langsung cocok. Kedua, fitur penghitungan orang pada RuView bersifat heuristik dan menurun kualitasnya pada lebih dari dua sampai tiga subjek, sehingga tidak dijanjikan sebagai keluaran utama.",
      ],
      tables: [{
        caption: "Tabel N Pemetaan fitur RuView untuk alat ruang kelas SLB",
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
      h1: "6. Metodologi Penelitian",
      subs: [
        {
          h2: "6.1 Desain Penelitian",
          paras: [
            "Penelitian ini adalah studi kelayakan kuantitatif dengan gerbang go/no-go pada minggu ketiga. Rangkaian evaluasi disusun dari skenario paling murah (uji sinyal di kelas kosong dan terisi) menuju skenario yang menuntut izin lebih dalam (sesi pembelajaran terjadwal dan simulasi jatuh). Setiap tahap menghasilkan artefak tetap, mulai dari karakterisasi sinyal hingga protokol izin, sehingga penelitian tetap bernilai sekalipun berhenti pada salah satu gerbang.",
          ],
        },
        {
          h2: "6.2 Lokasi, Partisipan, dan Etika",
          paras: [
            "Lokasi penelitian adalah satu ruang kelas mitra di 【Nama SLB】. Partisipan eksperimen aktif adalah pendamping dewasa (peneliti dan asisten) untuk semua skenario simulasi; aktivitas siswa hanya direkam sebagai data sensing pada sesi pembelajaran normal yang telah mendapat izin. Izin diambil berjenjang: persetujuan kepala sekolah, pemberitahuan dan persetujuan orang tua/wali dengan hak menarik diri kapan pun tanpa konsekuensi, serta kesepakatan dengan guru kelas tentang sesi dan durasi. Mode privasi RuView aktif sejak instalasi, tidak ada penyimpanan rekaman wajah, dan seluruh data dianonimkan pada tingkat ruangan.",
          ],
        },
        {
          h2: "6.3 Protokol Pengumpulan Data dan Kalibrasi",
          paras: [
            "Gerbang pertama adalah uji Delta-CSI pada minggu pertama hingga ketiga: kelas kosong, satu orang bergerak terstruktur, dan kelas terisi aktivitas normal, dibandingkan terhadap noise floor. Setelah lolos, tiap kelas dikalibrasi dengan protokol RuView minimal 600 frame baseline ruang kosong dan enrollment 8 anchor (sekitar 4 menit). Sesi pengumpulan data mencakup pembelajaran normal, transisi istirahat, dan skenario terstruktur yang dipandu guru. Evaluasi memakai split blok-waktu dengan data latih dan uji pada hari yang berbeda untuk mencegah kebocoran temporal.",
          ],
        },
        {
          h2: "6.4 Penyetelan Parameter untuk Populasi Anak",
          paras: [
            "Ambang bawaan RuView (durasi inaktivitas, ambang gerakan, deteksi tidur) dikalibrasi pada orang dewasa. Penelitian ini menyetel ulang ambang tersebut untuk populasi anak secara sistematis: mulai dari nilai dewasa, mengukur tingkat alarm palsu dan kehilangan deteksi per kombinasi ambang, lalu merekam nilai yang layak untuk populasi anak beserta interval kondisinya. Hasil penyetelan ini diangkat sebagai kontribusi kalibrasi yang dapat dipakai sekolah lain, dan keluarannya berupa tabel parameter yang direkomendasikan, bukan sekadar catatan anekdot.",
          ],
        },
        {
          h2: "6.5 Metrik Evaluasi",
          paras: [
            "Metrik utama meliputi akurasi deteksi kehadiran pada tingkat ruangan per window, sensitivitas dan alarm palsu per jam untuk anomali inaktivitas, serta sensitivitas deteksi jatuh simulasi di matras dengan latensi peringatan. Kualitas kalibrasi diukur dari perbaikan alarm palsu setelah penyetelan dibandingkan ambang dewasa bawaan. Seluruh evaluasi memakai split blok-waktu, dan setiap kejadian alert diaudit terhadap catatan pendamping untuk menilai benar-salahnya.",
          ],
        },
        {
          h2: "6.6 Gerbang Go/No-Go",
          paras: [
            "Minggu ketiga menentukan arah. Bila kehadiran dan gerakan di kelas tidak terbedakan dari derau, desain dipivot pada minggu yang sama; opsi pivot mencakup penempatan node ulang, pengubahan frekuensi antena, atau pengalihan fokus ke kalibrasi dengan klaim yang lebih sempit. Bila kontras memadai, penelitian lanjut ke sesi pengumpulan data penuh sesuai izin. Keputusan dievaluasi bersama pembimbing dan disampaikan kepada sekolah secara transparan.",
          ],
        },
      ],
    },
    {
      h1: "7. Manajemen Risiko dan Rencana Fallback",
      paras: ["Tabel 3 merangkum risiko utama. Risiko etis ditempatkan di baris pertama karena berhak membatalkan penelitian lebih cepat daripada risiko teknis mana pun."],
      tables: [{
        caption: "Tabel N Risiko utama dan mitigasi",
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
    {
      h1: "8. Jadwal Penelitian",
      paras: ["Jadwal satu semester disusun dengan gerbang go/no-go pada minggu ketiga, sebagaimana Tabel 4. Persetujuan etik sengaja diletakkan paling awal karena menjadi prasyarat seluruh pengambilan data pada siswa."],
      tables: [{
        caption: "Tabel N Jadwal penelitian satu semester",
        widths: [22, 46, 32],
        headers: ["Periode", "Aktivitas", "Keluaran"],
        rows: [
          ["Minggu 1-3", "Surat izin berjenjang ke sekolah dan orang tua; pemasangan node; uji Delta-CSI (kosong, satu orang, kelas terisi); kalibrasi 600 frame + 8 anchor", "Keputusan go/no-go; kelas terkalibrasi; dokumen persetujuan"],
          ["Minggu 4-7", "Sesi pembelajaran normal terekam sebagai data sensing; skenario terstruktur dipandu guru; simulasi jatuh di matras oleh pendamping", "Dataset blok hari + catatan kejadian pendamping"],
          ["Minggu 8-11", "Penyetelan ambang dewasa ke populasi anak; evaluasi presence, anomali inaktivitas, dan deteksi jatuh simulasi; split blok-waktu", "Tabel parameter anak + metrik sensitivitas/alarm palsu"],
          ["Minggu 12-15", "Audit alert bersama guru; analisis hasil; perbaikan threshold; penyusunan rekomendasi kalibrasi", "Hasil evaluasi utuh + rekomendasi parameter"],
          ["Minggu 16-18", "Penulisan naskah skripsi; finalisasi protokol izin sebagai lampiran; persiapan sidang", "Naskah skripsi siap sidang"],
        ],
      }],
    },
    {
      h1: "9. Estimasi Anggaran",
      paras: ["Tabel 5 merangkum estimasi anggaran. Perangkat dipilih serendah mungkin karena fokus penelitian adalah kelayakan, bukan produksi."],
      tables: [{
        caption: "Tabel N Estimasi anggaran perangkat dan operasional",
        widths: [44, 26, 30],
        headers: ["Komponen", "Jumlah", "Estimasi Biaya"],
        rows: [
          ["ESP32-S3 (satu access point, dua station, plus satu cadangan)", "4 unit", "Rp 800.000"],
          ["Single board computer (Orange Pi atau Raspberry Pi) + kartu memori", "1 set", "Rp 750.000"],
          ["Matras keselamatan untuk simulasi jatuh", "1 unit", "Rp 200.000"],
          ["Bracket, kabel, adaptor, komponen kecil", "1 set", "Rp 150.000"],
          ["Operasional lokasi dan percetakan dokumen izin", "\u2014", "Rp 100.000"],
          ["Total", "\u2014", "Rp 2.000.000"],
        ],
      }],
    },
    {
      h1: "10. Daftar Referensi",
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
