// dpj_content_3_asrama.js — DPJ 3: Kamar Asrama SLB (pemantauan malam, sensitivitas etis tertinggi)
"use strict";

module.exports = {
  fileName: "DPJ-3_Proposal_Judul_Kamar_Asrama_SLB.docx",
  docLabel: "PROPOSAL PENGAJUAN JUDUL SKRIPSI",
  subjectLine: "Opsi Alat 3 dari 3 \u2014 Pemantauan WiFi CSI pada Kamar Asrama SLB (Malam)",
  headerTitle: "Proposal Pengajuan Judul Skripsi \u2014 Kamar Asrama SLB (WiFi CSI pada ESP32)",
  judulUtama: "Sistem Pemantauan Pola Tidur dan Deteksi Anomali Nocturnal Siswa Asrama SLB Berbasis Wi-Fi CSI pada ESP32: Studi Kelayakan Non-Kontak Tanpa Kamera",
  alternatif: [
    { kategori: "Alternatif 1", judul: "Pemantauan Laju Napas dan Status Tidur Tanpa Kontak untuk Pendampingan Siswa Asrama SLB Berbasis Wi-Fi Channel State Information", catatan: "Dipilih bila fokus pada laju napas; tepi band filter untuk anak dievaluasi eksplisit." },
    { kategori: "Alternatif 2", judul: "Studi Kelayakan Wi-Fi Sensing untuk Sistem Peringatan Dini Kondisi Malam Siswa Berkebutuhan Khusus pada Asrama SLB", catatan: "Framing paling aman: seluruh keluaran berstatus skrining dan peringatan dini untuk pendamping." },
  ],
  chapters: [
    {
      h1: "1. Latar Belakang",
      paras: [
        "Asrama SLB melayani siswa yang membutuhkan pendampingan bahkan pada malam hari. Pengasuh asrama melakukan patroli berkala untuk memastikan setiap anak tidur dengan aman, napas teratur, dan tidak ada kondisi yang memerlukan bantuan segera. Patroli manual memiliki dua keterbatasan yang saling bertentangan: interval patroli yang rapat mengganggu kualitas tidur anak, sementara interval yang jarang menambah risiko kejadian tidak terdeteksi, seperti anak yang tidak bergerak lama atau napas yang tidak teratur. Kebutuhan akan alat bantu yang memantau tanpa mengganggu dan tanpa kamera di ruang tidur oleh karena itu sangat spesifik pada konteks ini.",
        "Wi-Fi Channel State Information (CSI) memungkinkan pemantauan tidur tanpa kontak dan tanpa kamera. Liu dan kawan-kawan membuktikan sejak awal bahwa sinyal Wi-Fi dapat memantau tidur secara kontak-less, termasuk respirasi, posisi, dan gerakan menggeliat [3]. Tataraidze dan kawan-kawan menunjukkan deteksi napas saat tidur dari perangkat Wi-Fi sekelas ponsel [4], sementara Burimas dan kawan-kawan memantau laju napas tidur pada perangkat mikrokontroler murah [5] dan Kontou serta kawan-kawan memperbaiki deteksi respirasi dengan jaringan saraf tiruan [6]. Pada populasi rentan, Touhiduzzaman dan kawan-kawan mendeploy sistem sensing Wi-Fi untuk pelacakan aktivitas harian pada hunian lansia [9], yang menunjukkan pola deployment pada penghuni sensitif dapat dilakukan dengan tata kelola yang tepat.",
        "Tantangan utama pada konteks asrama SLB bukan pada kemampuan dasar sensing, melainkan pada dua hal: populasi dan etika. Secara populasi, band filter napas pada sistem bawaan dirancang untuk orang dewasa, sementara laju napas anak usia sekolah berada di 18 hingga 25 napas per menit yang mendekati batas atas band, sehingga penyesuaian filter menjadi bagian dari pertanyaan penelitian. Secara etika, ruang tidur anak adalah ruang paling sensitif dari ketiga alat yang dipertimbangkan dalam rangkaian riset ini: persetujuan orang tua dan wali wajib, hak menarik diri harus mutlak, dan posisi sistem sebagai pendeteksi kondisi untuk pendamping, bukan pengawas perilaku, harus dinyatakan eksplisit sejak proposal.",
        "Keunggulan privasi arsitektur ini perlu dinyatakan secara proporsional. Sinyal Wi-Fi pada arsitektur penelitian ini tidak dapat mengidentifikasi individu dan tidak menyimpan biometrik; mode privasi membuang fitur biometrik sebelum data keluar dari node. Namun literatur juga menunjukkan bahwa pengenalan identitas dari sinyal Wi-Fi pada skenario lain tetap mungkin [10], dan pekerjaan terbaru bahkan menawarkan pemantauan posisi tidur in-bed dengan pembelajaran privasi-preservasi [8], menandakan bahwa kesadaran privasi pada sensing tidur adalah norma penelitian yang sedang tumbuh. Proposal ini mengikuti norma tersebut dengan tata kelola izin berjenjang.",
        "Pada level literatur, pemantauan tidur CSI untuk orang dewasa merupakan area yang ramai [3] [4] [5] [6], namun pencarian awal yang dilakukan pada penyusunan proposal ini belum menemukan penerapan pada asrama SLB atau populasi anak berkebutuhan khusus, sehingga celah ini berlabel terbatas-pencarian dan akan diverifikasi ulang bersama pembimbing. Proposal ini menawarkan studi kelayakan pemantauan pola tidur dan deteksi anomali nocturnal siswa asrama SLB tanpa kamera pada ESP32, dengan asumsi keras satu penghuni per kamar dan framing skrining untuk pendamping. Tabel 1 merangkum usulan judul utama dan dua alternatifnya.",
      ],
      tables: [{
        caption: "Tabel N Usulan judul penelitian",
        widths: [16, 50, 34],
        headers: ["Kategori", "Usulan Judul", "Catatan Pemetaan"],
        rows: [
          ["Utama", "Sistem Pemantauan Pola Tidur dan Deteksi Anomali Nocturnal Siswa Asrama SLB Berbasis Wi-Fi CSI pada ESP32: Studi Kelayakan Non-Kontak Tanpa Kamera", "Terpetakan ke fitur terukur (status tidur, laju napas, anomali inaktivitas) dan protokol izin berjenjang yang realistis dalam satu semester."],
          ["Alternatif 1", "Pemantauan Laju Napas dan Status Tidur Tanpa Kontak untuk Pendampingan Siswa Asrama SLB Berbasis Wi-Fi Channel State Information", "Dipilih bila fokus pada laju napas; evaluasi tepi band filter untuk anak menjadi bagian inti."],
          ["Alternatif 2", "Studi Kelayakan Wi-Fi Sensing untuk Sistem Peringatan Dini Kondisi Malam Siswa Berkebutuhan Khusus pada Asrama SLB", "Dipilih bila pembimbing mengutamakan framing paling aman dan sederhana."],
        ],
      }],
    },
    {
      h1: "2. Rumusan Masalah dan Batasan",
      subs: [
        {
          h2: "2.1 Rumusan Masalah",
          numbered: [
            "Sejauh mana sinyal Wi-Fi CSI pada ESP32 menghasilkan deteksi status tidur dan estimasi laju napas yang andal pada kamar tunggal penghuni anak SLB, dengan memperhitungkan tepi band filter untuk laju napas anak 18 hingga 25 napas per menit (uji Delta-CSI dan uji band)?",
            "Seberapa cepat dan seberapa sering sistem mendeteksi anomali inaktivitas nocturnal dibandingkan catatan pendamping asrama, dilihat dari latensi dan jumlah alarm palsu per kamar per minggu?",
            "Penyesuaian parameter apa yang layak direkomendasikan untuk memindahkan ambang dewasa ke populasi anak pada konteks asrama?",
          ],
        },
        {
          h2: "2.2 Batasan Masalah",
          bullets: [
            "Satu penghuni per kamar adalah asumsi keras; kamar dengan dua penghuni atau lebih berada di luar lingkup karena superposisi sinyal belum terpecahkan.",
            "Seluruh keluaran berstatus skrining untuk pendamping, bukan diagnosis; modul skrining apnea eksperimental pada platform bawaan tidak dijanjikan dan tidak dikompilasi.",
            "Tidak ada identifikasi individu dan tidak ada penyimpanan biometrik; sistem melaporkan status kamar, bukan profil anak.",
            "Eksperimen hanya berjalan pada kamar yang telah mendapat persetujuan orang tua/wali, pengasuh asrama, dan kepala sekolah, dengan hak menarik diri kapan pun.",
            "Status kebaruan konteks asrama SLB berlabel terbatas-pencarian dan klaim dibatasi pada studi kelayakan.",
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
            "Mengukur kelayakan fisik sinyal CSI untuk sensing malam pada kamar asrama melalui uji Delta-CSI kondisi kamar kosong, penghuni terjaga, dan penghuni tidur.",
            "Mengevaluasi deteksi status tidur dan estimasi laju napas tanpa kontak pada populasi anak, termasuk perilaku tepi band filter bawaan.",
            "Mengevaluasi deteksi anomali inaktivitas nocturnal dengan latensi dan alarm palsu per kamar per minggu terhadap catatan pendamping.",
            "Merumuskan rekomendasi parameter dewasa-ke-anak dan protokol izin berjenjang yang dapat direplikasi asrama lain.",
          ],
        },
        {
          h2: "3.2 Manfaat Penelitian",
          paras: [
            "Bagi asrama SLB, penelitian ini menguji lapisan keamanan malam yang memperpendek waktu antara kejadian dan ketahuan tanpa menambah kamera dan tanpa mengganggu tidur anak, sehingga patroli pendamping dapat diarahkan pada kamar yang memang memerlukan perhatian. Bagi komunitas ilmiah, penelitian ini menyediakan data empiris perilaku CSI pada populasi anak di ruang tidur yang langka di literatur, termasuk evaluasi tepi band filter napas untuk laju napas anak. Bagi mahasiswa, penelitian ini melatih desain eksperimen pada lingkungan paling sensitif secara etis, tata kelola persetujuan, dan pengukuran sistem nyata dari sensor hingga alert.",
          ],
        },
      ],
    },
    {
      h1: "4. Tinjauan Pustaka",
      paras: [
        "Pemantauan tidur tanpa kontak via Wi-Fi memiliki fondasi literatur yang matang pada orang dewasa. Liu dan kawan-kawan menunjukkan Wi-Sleep yang memantau respirasi, posisi, dan gerakan menggeliat dari perangkat Wi-Fi umum [3]. Tataraidze dan kawan-kawan menguji deteksi napas saat tidur melalui CSI pada ponsel tanpa sensor tambahan [4]. Burimas dan kawan-kawan memantau laju napas tidur pada perangkat mikrokontroler murah dalam lingkungan terkendali [5], relevan langsung dengan kendala biaya asrama, dan Kontou serta kawan-kawan meningkatkan deteksi respirasi dengan metode jaringan saraf tiruan pada jurnal biomedis IEEE [6].",
        "Pada tema skrining tidur berbasis CSI, Chang dan kawan-kawan mendeteksi kejadian apnea dan gerakan anggota badan dari sinyal CSI dengan pembelajaran berbasis attention [7]. Penelitian ini mengambil posisi yang jujur terhadap arah tersebut: skrining apnea pada platform bawaan berstatus eksperimental dan tidak tervalidasi, sehingga tidak dijanjikan dalam lingkup skripsi; yang dijanjikan adalah deteksi anomali inaktivitas dan pemantauan laju napas untuk pendamping. Pemosisian ini konsisten dengan norma literatur yang menempatkan sistem semacam ini sebagai alat bantu, bukan pengganti polisomnografi.",
        "Privasi pada sensing tidur menjadi perhatian literatur yang tumbuh. Pich dan kawan-kawan mengangkat pemantauan posisi tidur in-bed dengan pembelajaran privasi-preservasi [8], dan Mosharaf serta kawan-kawan merangkum kemungkinan identifikasi manusia dari sinyal Wi-Fi yang menuntut kewaspadaan tata kelola data [10]. Untuk populasi rentan, Touhiduzzaman dan kawan-kawan mendokumentasikan deployment sensing Wi-Fi pada hunian lansia berpenghasilan rendah beserta persoalan operasionalnya [9], memberi preseden bahwa pemantauan penghuni sensitif layak dilakukan bila tata kelola izin dan ekspektasi dikelola dengan benar.",
        "Fondasi teknis lintas garis juga relevan. Survei Ma dan kawan-kawan mengkatalogkan kemampuan sensing CSI pada manusia termasuk estimasi respirasi [1], dan Hernandez serta Bulut membuktikan sensing Wi-Fi mandiri pada perangkat kelas IoT murah [2] yang menjadi dasar pemilihan ESP32. Kedua rujukan ini mengikat penelitian ini ke tradisi literatur yang sama dengan dua alat lain dalam rangkaian riset, sehingga hasilnya dapat dibandingkan antar-alat.",
        "Dari pemetaan tersebut, celah penelitian teridentifikasi: literatur pemantauan tidur CSI ramai pada orang dewasa, namun belum ditemukan penerapan pada asrama SLB atau populasi anak berkebutuhan khusus pada rentang pencarian yang dilakukan, dan perilaku tepi band filter napas untuk laju napas anak juga belum banyak dilaporkan. Klaim kebaruan dibatasi: studi kelayakan pemantauan pola tidur dan anomali nocturnal tanpa kamera pada asrama SLB dengan satu penghuni per kamar. Klaim diagnostik secara eksplisit tidak diusulkan.",
      ],
    },
    {
      h1: "5. Basis Teknologi: Platform RuView",
      paras: [
        "Sistem dibangun di atas RuView, proyek open-source (github.com/ruvnet/RuView) yang menyediakan firmware ESP32 untuk capture CSI, server pengolahan Rust, mesin status semantik, dashboard, serta alert MQTT dan Home Assistant. Fitur yang relevan untuk alat ini meliputi mesin status someone_sleeping yang pada pengujian terpisah mencapai F1 0,84 pada data held-out, estimasi laju napas dari band 0,1 hingga 0,5 Hz, anomali inaktivitas no_movement, tren vital mingguan, serta dashboard demo pemantauan tidur. Seluruh keluaran diberi penanda skrining dan tidak diklaim klinis.",
        "Tabel 2 memetakan fitur RuView untuk alat ini beserta statusnya. Tiga catatan jujur wajib dibaca sejak awal. Pertama, band filter napas dikodekan permanen untuk rentang napas dewasa; laju napas anak 18 hingga 25 napas per menit berada dekat batas atas band sehingga perilaku tepi band wajib dievaluasi, dan bila perlu, konstanta filter diubah secara terdokumentasi. Kedua, modul skrining apnea pada platform berstatus eksperimental dan terkunci di belakang fitur kompilasi khusus, sehingga tidak diaktifkan dan tidak dijanjikan. Ketiga, klaim hemat daya node ESP32-C6 untuk deployment malam belum tervalidasi penuh, sehingga penelitian ini memakai ESP32-S3 dengan adaptor daya tetap.",
      ],
      tables: [{
        caption: "Tabel N Pemetaan fitur RuView untuk alat kamar asrama SLB",
        widths: [30, 42, 28],
        headers: ["Fitur RuView", "Peran pada Penelitian", "Status"],
        rows: [
          ["Capture CSI ESP32 + streaming UDP (format frame ADR-018)", "Sumber data utama", "Terukur (MEASURED)"],
          ["Mesin status someone_sleeping", "Status sedang tidur per kamar", "Terukur (F1 0,84 held-out)"],
          ["Estimasi laju napas (band 0,1-0,5 Hz)", "Pemantauan napas saat tidur", "Terukur untuk dewasa; tepi band anak wajib dievaluasi"],
          ["No_movement + anomali inaktivitas", "Peringatan anak tidak bergerak terlalu lama", "Ambang dewasa, wajib disetel ulang"],
          ["Tren vital mingguan", "Ringkasan pola untuk pengasuh asrama", "Terukur"],
          ["Dashboard pemantauan tidur (demo)", "Antarmuka skrining untuk pendamping", "Demo, dengan penanda skrining"],
          ["Privacy mode (strip fitur biometrik)", "Kepatuhan etika ruang tidur anak", "Terukur, diaktifkan penuh"],
          ["Kalibrasi 600 frame + enrollment 8 anchor per kamar", "Kalibrasi ruangan sekitar 4 menit", "Terukur"],
          ["Skrining apnea (modul medis eksperimental)", "Tidak diaktifkan, tidak dijanjikan", "Eksperimental, tidak tervalidasi"],
          ["Klaim hemat daya ESP32-C6 LP-core", "Tidak dipakai; memakai S3 daya tetap", "Belum tervalidasi perangkat"],
        ],
      }],
    },
    {
      h1: "6. Metodologi Penelitian",
      subs: [
        {
          h2: "6.1 Desain Penelitian",
          paras: [
            "Penelitian ini adalah studi kelayakan kuantitatif dengan gerbang go/no-go pada minggu ketiga dan masa pengamatan malam berblok setelah gerbang lolos. Desain dibuat bertingkat dari yang paling tidak sensitif: uji sinyal pada kamar kosong terlebih dahulu, kemudian penghuni dewasa (peneliti) pada siang hari, dan hanya setelah semua aman, pengamatan malam pada kamar siswa yang telah mendapat persetujuan penuh. Setiap tingkat menghasilkan artefak tetap sehingga penelitian tetap bernilai sekalipun tidak mencapai tingkat terakhir.",
          ],
        },
        {
          h2: "6.2 Lokasi, Partisipan, dan Etika",
          paras: [
            "Lokasi adalah dua sampai tiga kamar asrama berpenghuni tunggal di 【Nama SLB】. Izin diambil berjenjang dan tertulis: persetujuan orang tua/wali setiap anak kamar partisipan, persetujuan kepala sekolah, kesepakatan pengasuh asrama, serta penjelasan kepada anak dengan bahasa yang sesuai kemampuannya. Hak menarik diri bersifat mutlak dan kapan pun tanpa konsekuensi. Sistem tidak merekam suara, tidak merekam gambar, tidak mengidentifikasi individu, dan mode privasi aktif sejak instalasi; seluruh data dianonimkan pada tingkat kamar dan disimpan pada penyimpanan terkontrol.",
          ],
        },
        {
          h2: "6.3 Protokol Pengumpulan Data dan Kalibrasi",
          paras: [
            "Gerbang pertama adalah uji Delta-CSI pada minggu pertama hingga ketiga dengan tiga skenario: kamar kosong, penghuni terjaga bergerak, dan penghuni tidur, dibandingkan terhadap noise floor, dimulai pada penghuni dewasa (peneliti) sebelum melibatkan siswa. Setelah lolos, tiap kamar dikalibrasi dengan protokol RuView minimal 600 frame baseline dan enrollment 8 anchor. Pengamatan malam berjalan per blok hari dengan catatan pendamping sebagai ground truth status dan kejadian, serta pengukuran acuan laju napas (oksimeter atau strap) pada sesi terjadwal. Evaluasi memakai split blok-waktu dengan latih dan uji pada blok hari yang berbeda.",
          ],
        },
        {
          h2: "6.4 Penyesuaian Parameter untuk Populasi Anak",
          paras: [
            "Dua penyesuaian dievaluasi secara sistematis. Pertama, perilaku tepi band filter napas bawaan terhadap laju napas anak 18 hingga 25 napas per menit diukur pada sesi acuan; bila estimasi terdistorsi, konstanta filter diubah terdokumentasi di firmware dan server, dan hasil sebelum sesudah dilaporkan. Kedua, ambang mesin status inaktivitas malam disetel ulang dari nilai dewasa dengan mengukur alarm palsu dan kehilangan deteksi per kombinasi ambang. Keluaran berupa tabel parameter yang direkomendasikan untuk populasi anak, sejajar dengan kontribusi kalibrasi pada dua alat lain dalam rangkaian riset ini.",
          ],
        },
        {
          h2: "6.5 Metrik Evaluasi",
          paras: [
            "Metrik utama meliputi akurasi status tidur terhadap catatan pendamping per blok malam, galat estimasi laju napas terhadap alat acuan pada sesi terjadwal, latensi deteksi anomali inaktivitas, dan jumlah alarm palsu per kamar per minggu. Seluruh alert diaudit terhadap catatan pendamping. Evaluasi juga mencatat beban operasional bagi pengasuh, karena sistem yang menuntut perawatan tinggi tidak akan bertahan pada asrama nyata.",
          ],
        },
        {
          h2: "6.6 Gerbang Go/No-Go",
          paras: [
            "Minggu ketiga menentukan lanjut atau pivot. Bila status tidur dan napas tidak terbedakan dari derau, desain dipivot pada minggu yang sama: opsi meliputi penempatan ulang node, pengubahan geometri antena, atau penyempitan klaim menjadi karakterisasi sinyal malam. Bila kontras memadai, penelitian lanjut ke pengamatan malam pada kamar siswa yang telah mendapat persetujuan penuh, dengan penjajakan ulang persetujuan menjelang tahap tersebut.",
          ],
        },
      ],
    },
    {
      h1: "7. Manajemen Risiko dan Rencana Fallback",
      paras: ["Tabel 3 merangkum risiko utama. Risiko etis ditempatkan paling atas karena menjadi prasyarat mutlak seluruh tahap pengamatan malam."],
      tables: [{
        caption: "Tabel N Risiko utama dan mitigasi",
        widths: [30, 30, 40],
        headers: ["Risiko", "Dampak Bila Terjadi", "Mitigasi / Fallback"],
        rows: [
          ["Persetujuan orang tua atau wali tidak terkumpul", "Pengamatan malam pada siswa tidak dapat berjalan", "Tahap penghuni dewasa tetap berjalan; hasil berupa karakterisasi sinyal malam dan protokol izin; pengajuan kembali dijeda sampai kesepakatan penuh"],
          ["Dua anak tidur satu kamar (superposisi sinyal)", "Estimasi tidak valid", "Asumsi keras satu penghuni per kamar; kamar partisipan dipilih yang berpenghuni tunggal"],
          ["Alarm palsu malam berulang", "Pengasuh mengabaikan alert", "Penyetelan ambang per kamar; audit alert mingguan bersama pengasuh; definisi alarm palsu eksplisit"],
          ["Tepi band filter napas mendistorsi laju napas anak", "Estimasi napas bias", "Evaluasi tepi band eksplisit; ubah konstanta filter terdokumentasi; laporkan sebelum-sesudah"],
          ["Kontras Delta-CSI lemah malam hari", "Sinyal tidak andal", "Pivot penempatan node minggu 3; temuan tetap berupa karakterisasi sinyal kamar"],
          ["Salah pemahaman sebagai alat pengawas", "Kepercayaan wali turun", "Framing skrining untuk pendamping pada semua dokumen; tanpa identifikasi individu; tata kelola data terbuka untuk wali"],
        ],
      }],
    },
    {
      h1: "8. Jadwal Penelitian",
      paras: ["Jadwal satu semester disusun dengan gerbang go/no-go pada minggu ketiga, sebagaimana Tabel 4. Persetujuan berjenjang sengaja ditempatkan paling awal karena menjadi prasyarat mutlak tahap pengamatan malam."],
      tables: [{
        caption: "Tabel N Jadwal penelitian satu semester",
        widths: [22, 46, 32],
        headers: ["Periode", "Aktivitas", "Keluaran"],
        rows: [
          ["Minggu 1-3", "Pengurusan izin berjenjang (orang tua, sekolah, pengasuh); pemasangan node pada kamar kosong; uji Delta-CSI tiga skenario dengan penghuni dewasa; kalibrasi 600 frame + 8 anchor", "Keputusan go/no-go; kamar terkalibrasi; dokumen persetujuan"],
          ["Minggu 4-7", "Pengamatan malam blok awal pada kamar partisipan; catatan pendamping; sesi acuan laju napas dengan oksimeter/strap", "Dataset malam berblok + catatan kejadian"],
          ["Minggu 8-11", "Evaluasi tepi band filter untuk anak; penyetelan ambang inaktivitas malam; evaluasi status tidur dan napas dengan split blok-waktu", "Tabel parameter anak + metrik latensi/alarm palsu"],
          ["Minggu 12-15", "Audit alert bersama pengasuh; analisis hasil; perbaikan threshold; penyusunan rekomendasi kalibrasi dan protokol izin", "Hasil evaluasi utuh + rekomendasi parameter"],
          ["Minggu 16-18", "Penulisan naskah skripsi; finalisasi lampiran etik; persiapan sidang", "Naskah skripsi siap sidang"],
        ],
      }],
    },
    {
      h1: "9. Estimasi Anggaran",
      paras: ["Tabel 5 merangkum estimasi anggaran. Alat acuan laju napas dipakai hanya pada sesi terjadwal sebagai pembanding, bukan bagian dari sistem operasional."],
      tables: [{
        caption: "Tabel N Estimasi anggaran perangkat dan operasional",
        widths: [44, 26, 30],
        headers: ["Komponen", "Jumlah", "Estimasi Biaya"],
        rows: [
          ["ESP32-S3 (satu access point, dua station, plus satu cadangan)", "4 unit", "Rp 800.000"],
          ["Single board computer (Orange Pi atau Raspberry Pi) + kartu memori", "1 set", "Rp 750.000"],
          ["Oksimeter pulsa / strap acuan laju napas", "1 unit", "Rp 250.000"],
          ["Bracket, kabel, adaptor, komponen kecil", "1 set", "Rp 150.000"],
          ["Operasional lokasi dan percetakan dokumen izin", "\u2014", "Rp 100.000"],
          ["Total", "\u2014", "Rp 2.050.000"],
        ],
      }],
    },
    {
      h1: "10. Daftar Referensi",
      refs: [
        "[1] Ma, Y., Zhou, G., & Wang, S. (2019). WiFi sensing with channel state information: A survey. ACM Computing Surveys, 52(3), 1\u201336. https://doi.org/10.1145/3310194",
        "[2] Hernandez, S. M., & Bulut, E. (2020). Lightweight and standalone IoT based WiFi sensing for active repositioning and mobility. Proceedings of the IEEE International Conference on WoWMoM 2020. https://doi.org/10.1109/WoWMoM49955.2020.00056",
        "[3] Liu, X., Cao, J., Tang, S., & Wen, J. (2014). Wi-Sleep: Contactless sleep monitoring via WiFi signals. Proceedings of the IEEE Real-Time Systems Symposium (RTSS). https://doi.org/10.1109/RTSS.2014.30",
        "[4] Tataraidze, A., Olesyuk, R., & Pikhletsky, M. (2019). Can we monitor breathing during sleep via Wi-Fi on smartphone? Proceedings of the 41st Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC). https://doi.org/10.1109/EMBC.2019.8856382",
        "[5] Burimas, R., Horanont, T., Thapa, A., & Lamichhane, B. R. (2024). Monitoring the sleep respiratory rate with low-cost microcontroller Wi-Fi in a controlled environment. Applied Sciences, 14(15), 6458. https://doi.org/10.3390/app14156458",
        "[6] Kontou, P., Ben Smida, S., & Anagnostou, D. E. (2024). Contactless respiration monitoring using Wi-Fi and artificial neural network detection method. IEEE Journal of Biomedical and Health Informatics. https://doi.org/10.1109/JBHI.2023.3337001",
        "[7] Chang, C.-C., Hsiao, A.-H., Shen, L.-H., Feng, K.-T., & Chen, C.-Y. (2023). Attention-based learning for sleep apnea and limb movement detection using Wi-Fi CSI signals. Proceedings of the IEEE 97th Vehicular Technology Conference (VTC2023-Spring). https://doi.org/10.1109/VTC2023-Spring57618.2023.10200274",
        "[8] Pich, D., Baselizadeh, A., Torresen, J., & Miura, J. (2025). Privacy-preserving machine learning-based in-bed sleep posture monitoring using Wi-Fi signals. Proceedings of the 13th International Conference on Control, Mechatronics and Automation (ICCMA). https://doi.org/10.1109/ICCMA67641.2025.11369717",
        "[9] Touhiduzzaman, M., Chung, J., Pretzer-Aboff, I., & Bulut, E. (2024). Wireless sensing-based daily activity tracking system deployment in low-income senior housing environments. Proceedings of the 30th Annual International Conference on Mobile Computing and Networking (MobiCom). https://doi.org/10.1145/3636534.3698115",
        "[10] Mosharaf, M., Kwak, J. B., & Choi, W. (2024). WiFi-based human identification with machine learning: A comprehensive survey. Sensors, 24(19), 6413. https://doi.org/10.3390/s24196413",
      ],
    },
  ],
};
