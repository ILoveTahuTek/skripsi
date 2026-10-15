// dpj_content_4_isyarat.js — DPJ 4: Translasi Bahasa Isyarat SIBI/BISINDO via WiFi CSI
// Bahasa mengikuti skill proposal-writing (pola korpus TRSE UNM); struktur konsisten DPJ 1-3.
"use strict";

module.exports = {
  fileName: "DPJ-4_Proposal_Judul_Translasi_Isyarat_SIBI_BISINDO.docx",
  docLabel: "PROPOSAL PENGAJUAN JUDUL SKRIPSI",
  subjectLine: "Judul Usulan Baru (ke-4) \u2014 Translasi Bahasa Isyarat SIBI/BISINDO via Wi-Fi CSI (Human Presence High-Frequency)",
  headerTitle: "Proposal Pengajuan Judul Skripsi \u2014 Translasi Bahasa Isyarat SIBI/BISINDO (Wi-Fi CSI pada ESP32)",
  judulUtama: "Pengenalan Gestur Bahasa Isyarat SIBI dan BISINDO Berbasis Wi-Fi Channel State Information pada ESP32 untuk Prasarana Edukasi: Studi Kelayakan Translasi Tanpa Kamera",
  alternatif: [
    { kategori: "Alternatif 1", judul: "Studi Kelayakan Klasifikasi Gestur Terisolasi SIBI/BISINDO dari Pola Wi-Fi CSI pada Platform RuView untuk Ruang Kelas Tunarungu", catatan: "Dipilih bila pembimbing ingin fokus pada sisi klasifikasi sinyal dan dataset; luaran utama berupa model per-gestur beserta laporan kelayakan." },
    { kategori: "Alternatif 2", judul: "Dataset dan Klasifikasi Gestur Bahasa Isyarat Indonesia dari Sinyal Wi-Fi CSI pada ESP32: Studi Kelayakan Alat Bantu Komunikasi Pendidikan Tunarungu", catatan: "Dipilih bila kontribusi dataset publik CSI SIBI/BISINDO yang belum ada ingin dijadikan sumbangan utama." },
  ],
  chapters: [
    {
      h1: "1. Latar Belakang",
      paras: [
        "Perkembangan teknologi telah memengaruhi hampir semua sisi kehidupan manusia, termasuk cara masyarakat berkomunikasi dan cara lembaga pendidikan melayani peserta didiknya. Pada kelompok tunarungu, teknologi justru menentukan akses informasi karena bahasa isyarat merupakan sarana komunikasi utama, dan di Indonesia dua sistem yang paling banyak digunakan adalah SIBI (Sistem Isyarat Bahasa Indonesia) yang bersifat formal dan terstandar, serta BISINDO (Bahasa Isyarat Indonesia) yang tumbuh secara alami di komunitas. Ketegangan antara keduanya nyata di lembaga pendidikan: sekolah formal cenderung memakai SIBI, sedangkan pergaulan siswa berlangsung dalam BISINDO, sehingga alat bantu komunikasi di prasarana edukasi idealnya mengenali keduanya, bukan salah satunya saja. Studi tentang teknologi bantu bagi orang tunarungu menunjukkan bahwa hambatan komunikasi sehari-hari masih menjadi persoalan utama yang belum terjawab tuntas oleh teknologi yang tersedia [1]. Di sisi lain, tinjauan sistematis pengenalan bahasa isyarat BISINDO memperlihatkan bahwa hampir seluruh penelitian yang ada bertumpu pada kamera dan pengolahan citra [2], termasuk pendekatan jaringan saraf dalam pada citra video [3].",
        "Pendekatan berbasis kamera memang maju pesat, tetapi penerapannya di lingkungan pendidikan menghadapi tiga hambatan sekaligus. Pertama, kamera menimbulkan beban privasi dan kesiapan institusi, terutama ketika ruang juga dipakai kelompok lain yang tidak bersedia terekam. Kedua, kualitas pengenalan citra sangat bergantung pada pencahayaan dan sudut pandang, sementara ruang kelas berubah-ubah sepanjang hari. Ketiga, solusi penerjemah isyarat komersial berbasis sensor khusus atau layanan manusia berbiaya tinggi dan tidak realistis untuk sekolah. Akibatnya, alat bantu pengenalan isyarat yang layak untuk prasarana edukasi perlu bebas kamera saat digunakan, murah, dan mudah dipindahkan antar-ruang.",
        "Wi-Fi Channel State Information (CSI) menawarkan jalur alternatif yang berbeda secara prinsip. CSI adalah informasi fase dan amplitudo subcarrier Wi-Fi yang berubah ketika gelombang terganggu oleh gerakan tubuh manusia, sehingga pola gestur dapat diklasifikasikan langsung dari sinyal tanpa kamera dan tanpa perangkat yang dipakai pada tubuh penandatangan; survei Ma dan kawan-kawan mengkatalogkan keluarga kemampuan sensing semacam ini pada manusia [4]. Pengambilan CSI dapat dilakukan perangkat murah seperti ESP32 yang telah memiliki basis penelitian resmi melalui ESP32-CSI-Tool [5]. SignFi membuktikan pengenalan 276 isyarat bahasa isyarat Amerika dari sinyal Wi-Fi [6], dan preseden terbaru menunjukkan bahasa isyarat nasional lain, Filipino Sign Language, juga dapat dikenali dari CSI dengan perangkat komoditas [7]. Fisika sinyalnya menguntungkan: gestur isyarat melibatkan gerakan lengan dan tubuh bagian atas berdurasi 0,5 sampai 3 detik yang memodulasi sinyal jauh lebih kuat daripada gerakan napas, sehingga tantangan sinyal-lemah yang menghantui kasus objek kecil praktis tidak muncul di sini.",
        "Platform open-source RuView (github.com/ruvnet/RuView) menyediakan fondasi rekayasa yang dibutuhkan: firmware penangkap CSI pada ESP32, alur pengolahan sinyal, mekanisme rekam lalu latih yang adaptif, dashboard, serta penerusan notifikasi melalui MQTT dan Home Assistant. Dengan memakai RuView sebagai basis, penelitian tidak perlu membangun infrastruktur capture dari nol dan dapat memusatkan usaha pada pertanyaan yang benar-benar terbuka, yaitu apakah gestur SIBI dan BISINDO yang dipilih dapat diklasifikasikan dari pola CSI pada perangkat semurah ESP32. Berdasarkan uraian tersebut, penelitian ini dilakukan untuk menguji kelayakan pengenalan gestur terisolasi bahasa isyarat SIBI dan BISINDO dari pola Wi-Fi CSI pada ESP32 sebagai langkah awal translasi tanpa kamera di prasarana edukasi. Tabel 1 merangkum usulan judul utama beserta dua alternatifnya.",
      ],
      tables: [{
        caption: "Tabel N Usulan judul penelitian",
        widths: [16, 50, 34],
        headers: ["Kategori", "Usulan Judul", "Catatan Pemetaan"],
        rows: [
          ["Utama", "Pengenalan Gestur Bahasa Isyarat SIBI dan BISINDO Berbasis Wi-Fi Channel State Information pada ESP32 untuk Prasarana Edukasi: Studi Kelayakan Translasi Tanpa Kamera", "Setiap kata terpetakan ke hal yang terukur: SIBI dan BISINDO (subset gestur terpilih), Wi-Fi CSI (sinyal yang diklasifikasikan), ESP32 (perangkat), prasarana edukasi (lokasi kalibrasi), studi kelayakan (batas klaim)."],
          ["Alternatif 1", "Studi Kelayakan Klasifikasi Gestur Terisolasi SIBI/BISINDO dari Pola Wi-Fi CSI pada Platform RuView untuk Ruang Kelas Tunarungu", "Dipilih bila fokus pada kelayakan klasifikasi dan integrasi RuView; luaran utama model per-gestur dan laporan kelayakan."],
          ["Alternatif 2", "Dataset dan Klasifikasi Gestur Bahasa Isyarat Indonesia dari Sinyal Wi-Fi CSI pada ESP32: Studi Kelayakan Alat Bantu Komunikasi Pendidikan Tunarungu", "Dipilih bila dataset publik CSI SIBI/BISINDO dijadikan kontribusi utama; cocok untuk arah publikasi dataset."],
        ],
      }],
    },
    {
      h1: "2. Rumusan Masalah dan Batasan",
      subs: [
        {
          h2: "2.1 Rumusan Masalah",
          paras: ["Berdasarkan latar belakang permasalahan yang telah diuraikan serta untuk menjawab permasalahan yang menjadi fokus dalam penelitian ini, maka dapat dirumuskan beberapa rumusan masalah yang akan dikaji lebih lanjut. Rumusan masalah pada penelitian ini sebagai berikut."],
          numbered: [
            "Bagaimana perancangan sistem capture Wi-Fi CSI dua node ESP32 berbasis platform RuView beserta protokol pengumpulan dataset gestur SIBI/BISINDO terisolasi di ruang edukasi yang terkalibrasi?",
            "Bagaimana implementasi ekstraksi fitur dan pelatihan klasifikator gestur dari pola amplitudo, fase, dan Doppler CSI untuk subset gestur SIBI/BISINDO yang dominan gerak lengan?",
            "Bagaimana hasil pengujian akurasi klasifikasi per-gestur, tingkat alarm palsu, dan integrasi keluaran klasifikasi ke jalur alert RuView (MQTT/Home Assistant) sebagai indikator kelayakan translasi tanpa kamera?",
          ],
        },
        {
          h2: "2.2 Batasan Masalah",
          paras: ["Agar penelitian ini memiliki ruang lingkup yang jelas dan terarah sesuai dengan tujuan yang telah ditetapkan, maka ditentukan batasan masalah guna membatasi pembahasan terhadap aspek-aspek yang relevan dengan topik penelitian. Adapun batasan masalah pada penelitian ini sebagai berikut."],
          bullets: [
            "Lingkup penelitian adalah studi kelayakan pengenalan gestur terisolasi (isolated) pada subset 5 sampai 12 gestur SIBI/BISINDO yang dominan gerak lengan dan bermakna sama pada kedua sistem, bukan penerjemah kalimat bahasa isyarat kontinu.",
            "Satu penandatangan per sesi capture di zona pengambilan data; sistem tidak mengidentifikasi individu dan person counting tidak dijanjikan karena kualitasnya menurun pada lebih dari dua sampai tiga subjek.",
            "Kamera hanya digunakan saat perekaman dataset untuk pelabelan ground truth; penggunaan operasional sistem bebas kamera.",
            "Ekstraksi pose atau kerangka tangan tidak dipakai dan tidak dijanjikan karena modul pose on-device RuView masih berupa stub (PCK@20 sekitar 3 persen); klasifikasi dilakukan langsung dari pola CSI.",
            "Setiap ruang edukasi mitra di 【Nama Sekolah/Lokasi】 wajib dikalibrasi ulang (600 frame + 8 anchor) dan model dianggap sah untuk sesi yang sama, bukan lintas ruang tanpa kalibrasi.",
            "Penelitian ini tidak membahas penerjemahan kontinu dua arah, pengenalan multi-penandatangan simultan, akurasi lintas-ruang tanpa kalibrasi, serta aspek komersialisasi alat.",
          ],
        },
      ],
    },
    {
      h1: "3. Tujuan dan Manfaat",
      subs: [
        {
          h2: "3.1 Tujuan Penelitian",
          paras: ["Penelitian ini bertujuan untuk menguji kelayakan pengenalan gestur terisolasi bahasa isyarat SIBI dan BISINDO dari pola Wi-Fi CSI pada ESP32 untuk prasarana edukasi. Adapun tujuan dari penelitian ini adalah sebagai berikut."],
          numbered: [
            "Merancang sistem capture Wi-Fi CSI dua node ESP32 berbasis RuView beserta protokol pengumpulan dataset gestur terisolasi SIBI/BISINDO yang terdokumentasi dan dapat direplikasi.",
            "Mengimplementasikan ekstraksi fitur dan pelatihan klasifikator gestur dari pola amplitudo, fase, dan Doppler CSI untuk subset gestur yang dipilih.",
            "Mengetahui hasil pengujian akurasi klasifikasi per-gestur, alarm palsu, dan kelayakan integrasi keluaran ke jalur alert RuView, termasuk keputusan go/no-go pada uji fisik Delta-CSI di minggu ketiga.",
          ],
        },
        {
          h2: "3.2 Manfaat Penelitian",
          paras: [
            "Manfaat penelitian mencakup manfaat Teoretis dan Praktis. Secara teoretis, penelitian ini diharapkan dapat menjadi referensi pertama pengenalan gestur bahasa isyarat Indonesia (SIBI dan BISINDO) berbasis Wi-Fi CSI, mengingat literatur yang tersedia saat proposal ini disusun belum menemukan publikasi CSI pada kedua bahasa isyarat tersebut; preseden terdekat adalah bahasa isyarat negara lain [7]. Penelitian ini juga menjadi acuan penerapan pipeline capture-DSP-alert open-source pada domain komunikasi, bukan sekadar pemantauan.",
          ],
          bullets: [
            "Bagi sekolah dan siswa tunarungu: hasil kelayakan menjadi dasar pengembangan alat bantu komunikasi bebas kamera yang murah (ESP32) dan menghormati privasi ruang belajar.",
            "Bagi peneliti: pengalaman eksperimen sensing nyata, pembuatan dataset berlabel, dan disiplin evaluasi kelayakan bergerbang.",
            "Bagi pengembang platform sensing: pemetaan fitur RuView pada domain baru (klasifikasi gestur) beserta batas-batas jujurnya.",
            "Bagi praktisi teknologi pendidikan: protokol izin, kalibrasi ruang, dan tata kelola data yang dapat direplikasi lembaga lain.",
          ],
        },
      ],
    },
    {
      h1: "4. Tinjauan Pustaka",
      paras: [
        "Pengenalan isyarat dari sinyal Wi-Fi memiliki rantai bukti yang cukup panjang pada bahasa isyarat dunia. Shang dan Wu membangun WiSign, sistem pengenalan isyarat dengan beberapa transceiver Wi-Fi dan desain fitur tangguh terhadap variasi pengguna [8]. SignFi kemudian menunjukkan 276 isyarat ASL dapat diklasifikasikan dari CSI Wi-Fi komoditas dengan akurasi yang layak pada skenario terkalibrasi [6]. Ahmed dan kawan-kawan menyusun DF-WiSLR, sistem pengenalan isyarat bebas-perangkat berbasis Wi-Fi dengan pembagian subcarrier aktif [9], dan melanjutkannya dengan arsitektur LSTM pada tahun berikutnya [10]. Pada tingkat gestur umum (bukan khusus isyarat), Widar3.0 menyelesaikan persoalan lintas-domain dengan ekstraksi komponen gerak dari Doppler sehingga model tetap bekerja pada pengguna dan lingkungan baru tanpa pelatihan ulang [11], dan survei lintas-domain CSI mengkatalogkan strategi-strategi semacam itu secara lengkap [12]. Untuk granularitas halus, Wi-SL membuktikan pengenalan gestur jarimuhan dari CSI [13], HandFi mengenali gestur tangan dengan integrasi fitur amplitudo-fase [14], serta pendekatan amplitudo-fase komplementer ditegaskan kembali pada perangkat komoditas [15]. WiASL memperlihatkan arah aplikasi praktis dengan sistem tulisan-isyarat pada kamera komersial [16], menegaskan nilai aplikatif domain ini.",
        "Pada bahasa isyarat Indonesia, literatur yang tumbuh nyata-nyata berbasis visi. Dwijayanti dan kawan-kawan menerapkan CNN untuk pengenalan isyarat bahasa isyarat Indonesia [3]. Tiga karya 2025 memperluas arah ini: dataset video isyarat BISINDO tingkat kata [17], pengenalan kalimat BISINDO berbasis arsitektur 3D [18], dan pengenalan BISINDO dengan blok sadar-ruang [19]. Tinjauan sistematis Sanjaya dan kawan-kawan menegaskan dominasi kamera pada keseluruhan riset BISINDO dan mencatat belum adanya pendekatan sensor wireless device-free [2]. Dari seluruh pencarian yang dilakukan pada penyusunan proposal ini, belum ditemukan satu pun publikasi pengenalan SIBI atau BISINDO berbasis Wi-Fi CSI; preseden lintas-bahasa terdekat adalah Filipino Sign Language via CSI pada TENCON 2024 [7].",
        "Berdasarkan tabel perbandingan di atas, terlihat bahwa penelitian-penelitian sebelumnya terpisah pada dua kutub: pengenalan isyarat CSI yang matang pada ASL dan bahasa isyarat dunia lain, serta pengenalan BISINDO yang kuat tetapi seluruhnya bergantung kamera. Belum banyak penelitian yang secara spesifik menggabungkan bahasa isyarat Indonesia, platform capture CSI murah (ESP32), dan konteks prasarana edukasi bebas kamera, terdapat juga beberapa celah masalah (gap) yang belum terselesaikan secara simultan oleh peneliti sebelumnya. Penelitian ini mengisi celah tersebut dengan langkah-langkah berikut.",
        "Pertama, memindahkan paradigma bukti CSI dari bahasa isyarat asing ke SIBI dan BISINDO pada subset gestur terisolasi yang dominan gerak lengan, sehingga sinyal Doppler cukup kuat untuk dipisahkan dari latar. Kedua, memakai platform open-source RuView agar seluruh rantai capture, kalibrasi ruang, dataset, dan alert dapat direplikasi sekolah lain tanpa biaya lisensi. Ketiga, menempatkan luaran sebagai studi kelayakan bergerbang dengan dataset publik berlabel sebagai artefak tetap, sehingga keputusan lanjut-atau-berhenti dibuat berdasarkan data, bukan harapan.",
      ],
      tables: [{
        caption: "Tabel N Perbandingan Penelitian Terdahulu",
        widths: [34, 16, 12, 12, 12, 14],
        headers: ["Peneliti (Tahun) dan Judul Singkat", "Sinyal/Modalitas", "Bahasa Isyarat Indonesia", "Bebas Kamera", "Perangkat Murah", "Konteks Edukasi"],
        rows: [
          ["Shang & Wu (2017) \u2014 WiSign: robust sign language recognition", "Wi-Fi CSI", "−", "√", "−", "−"],
          ["Ma et al. (2018) \u2014 SignFi: sign language recognition using WiFi", "Wi-Fi CSI", "−", "√", "√", "−"],
          ["Ahmed et al. (2020) \u2014 DF-WiSLR device-free Wi-Fi sign language", "Wi-Fi CSI", "−", "√", "√", "−"],
          ["Baldeo et al. (2024) \u2014 Filipino SL recognition using Wi-Fi CSI", "Wi-Fi CSI", "−", "√", "√", "−"],
          ["Dwijayanti et al. (2021) \u2014 Indonesia SL recognition using CNN", "Kamera/citra", "√", "−", "−", "−"],
          ["Kindy et al. (2025) \u2014 Word-level BISINDO video dataset", "Kamera/citra", "√", "−", "−", "−"],
          ["Wiguna & Rojali (2025) \u2014 Sentence-level BISINDO 3D", "Kamera/citra", "√", "−", "−", "−"],
          ["Penelitian Ini", "Wi-Fi CSI (ESP32 + RuView)", "√ (SIBI & BISINDO)", "√", "√", "√"],
        ],
      }],
    },
    {
      h1: "5. Basis Teknologi: Platform RuView",
      paras: [
        "Sistem dibangun di atas RuView, proyek open-source (github.com/ruvnet/RuView) yang menyediakan firmware ESP32 untuk penangkapan CSI dengan format frame tetap, alur pengolahan sinyal berbasis buffer frekuensi tinggi, mekanisme rekam lalu latih yang adaptif, dashboard web, serta penerusan notifikasi melalui MQTT dan Home Assistant. Untuk kasus isyarat, komponen yang sama dibaca ulang dengan cara baru: level dan energi gerakan dipakai untuk memotong durasi gestur secara otomatis, dan alur rekam-latih yang semula dipakai untuk kalibrasi kehadiran diadaptasi menjadi prosedur perekaman N repetisi per gestur untuk pembangunan dataset berlabel. Kalibrasi ruang bawaan (600 frame + 8 anchor) tetap dipakai di setiap ruang edukasi mitra sebelum pengambilan data.",
        "Perbedaan fisika dengan kasus pemantauan lain justru menguntungkan proposal ini. Gestur isyarat memindahkan massa lengan dan tubuh bagian atas sehingga modulasi Doppler pada CSI berorde puluhan kali lebih besar daripada modulasi napas yang menjadi acuan ambang bawaan RuView; band analisis berpindah dari 0,1 sampai 0,5 Hz ke pita gerak tubuh sekitar 1 sampai 60 Hz. Lingkungan pengambilan data juga lebih terkendali: penandatangan statis di zona capture dengan satu subjek per sesi, jauh lebih bersih daripada kandang unggas atau kamar berisi banyak orang.",
        "Tabel 3 memetakan fitur RuView yang dipakai beserta status keterujinya. Dua batas jujur dinyatakan sejak awal. Pertama, modul pose on-device 17 keypoint pada RuView masih berupa stub dengan PCK@20 sekitar 3 persen, sehingga penelitian ini mengklasifikasikan gestur langsung dari pola CSI mengikuti paradigma literatur [6], [11], dan tidak menjanjikan kerangka tangan. Kedua, penghitungan orang bersifat heuristik dan menurun pada lebih dari dua sampai tiga subjek, sehingga asumsi satu penandatangan per sesi dinyatakan eksplisit pada batasan masalah.",
      ],
      tables: [{
        caption: "Tabel N Pemetaan fitur RuView untuk kasus translasi isyarat",
        widths: [30, 42, 28],
        headers: ["Fitur RuView", "Peran pada Penelitian", "Status"],
        rows: [
          ["Capture CSI ESP32 + streaming UDP (format frame ADR-018)", "Sumber data utama saat penandatangan bergerak", "Terukur (MEASURED)"],
          ["Buffer CSI frekuensi tinggi + motion level/energy", "Segmentasi awal durasi gestur (mulai/berhenti gerak)", "Terukur, ambang disetel untuk gestur 0,5-3 detik"],
          ["Presence heuristik", "Deteksi penandatangan masuk zona capture", "Terukur; FP kipas/orang lewat jadi item pengujian"],
          ["Kalibrasi 600 frame + enrollment 8 anchor", "Kalibrasi tiap ruang edukasi mitra (sekitar 4 menit)", "Terukur"],
          ["Workflow record → train adaptif", "Diadaptasi: rekam N repetisi per gestur → dataset berlabel → pelatihan klasifikator", "Terukur untuk presence; adaptasi gestur = bagian penelitian"],
          ["Pipeline DSP (filtering, subcarrier, Doppler)", "Ekstraksi fitur amplitudo/fase/Doppler pita gerak 1-60 Hz", "Terukur; penyesuaian band = bagian penelitian"],
          ["MQTT ke Home Assistant + dashboard/notifikasi", "Penerusan hasil klasifikasi gestur ke guru/pendamping", "Terukur; entitas baru semacam gesture terdeteksi"],
          ["Privacy mode (strip fitur biometrik)", "Kepatuhan etika ruang edukasi; identitas tidak tersimpan", "Terukur, diaktifkan penuh"],
          ["Person counting heuristik", "Tidak dijanjikan; satu penandatangan per sesi", "Lemah pada lebih dari 2-3 subjek"],
          ["Pose 17-keypoint on-device", "Tidak dipakai; klasifikasi langsung dari pola CSI", "Stub terukur (PCK@20 3,0 persen) — terlarang dijanjikan"],
        ],
      }],
    },
    {
      h1: "6. Metodologi Penelitian",
      subs: [
        {
          h2: "6.1 Desain Penelitian",
          paras: [
            "Penelitian ini adalah studi kelayakan kuantitatif dengan gerbang go/no-go pada minggu ketiga. Tahap pertama adalah studi literatur, yaitu pemetaan sistematis pengenalan isyarat CSI dan bahasa isyarat Indonesia beserta penetapan subset gestur bersama guru/pembina yang memahami SIBI dan BISINDO. Tahap kedua adalah perancangan sistem, mencakup penyiapan dua node ESP32 dengan firmware RuView, skenario penempatan node di ruang edukasi, dan protokol perekaman dataset. Tahap ketiga adalah implementasi, yaitu perekaman dataset gestur berlabel, ekstraksi fitur, dan pelatihan klasifikator. Tahap terakhir adalah pengujian dan evaluasi: pengukuran akurasi per-gestur, alarm palsu, serta integrasi keluaran ke jalur alert, yang berujung pada keputusan kelayakan dan rekomendasi pengembangan. Apabila dalam proses pengujian ditemukan kendala, maka dilakukan evaluasi dan perbaikan secara berulang hingga sistem dapat dievaluasi secara adil.",
            "Setiap tahap menghasilkan artefak tetap — karakterisasi sinyal, protokol perekaman, dataset publik berlabel, model, dan laporan kelayakan — sehingga penelitian tetap bernilai sekalipun berhenti pada salah satu gerbang. Struktur bergerbang ini konsisten dengan tiga proposal pengajuan judul sebelumnya pada garis penelitian yang sama.",
          ],
        },
        {
          h2: "6.2 Lokasi, Partisipan, dan Etika",
          paras: [
            "Lokasi pengambilan data adalah satu ruang edukasi mitra di 【Nama Sekolah/Lokasi】 yang dipilih bersama pihak sekolah, dengan penandatangan dewasa berbahasa isyarat (guru atau pembina) sebagai subjek utama pengambilan dataset dan, apabila disetujui, siswa sebagai partisipan sukarela untuk pengujian variasi. Etika ditangani berjenjang: persetujuan institusi, persetujuan tertulis subjek, hak menarik diri tanpa konsekuensi, dan keterbukaan bahwa kamera hanya menyala saat sesi pelabelan. Sistem operasional bebas kamera dan mode privasi RuView membuang fitur biometrik sebelum data keluar dari node; identifikasi individu bukan keluaran penelitian.",
          ],
        },
        {
          h2: "6.3 Protokol Pengumpulan Data dan Kalibrasi",
          paras: [
            "Setiap sesi diawali kalibrasi ruang (600 frame + 8 anchor) dan pencatatan kondisi lingkungan (posisi perabot, sumber gerak latar seperti kipas atau AC) sebagai kovariat. Untuk tiap gestur pada subset terpilih, penandatangan melakukan N repetisi (target 30 repetisi per gestur per sesi) di dalam zona capture sambil terekam CSI dua node dan kamera sinkron untuk pelabelan; penanda waktu pada ketiganya disinkronkan lewat trigger bersama. Dataset disimpan lengkap dengan metadata (tanggal, ruang, penandatangan, posisi node) dan dibagikan sebagai dataset publik CSI bahasa isyarat Indonesia berlabel — kontribusi yang belum tersedia pada literatur [2], [17].",
          ],
        },
        {
          h2: "6.4 Ekstraksi Fitur dan Pelatihan Klasifikator",
          paras: [
            "Fitur diekstraksi dari segmen gestur hasil pemotongan berbasis energi gerak: amplitudo dan fase subcarrier terpilih, komponen Doppler pita gerak sekitar 1 sampai 60 Hz, serta statistik ringkasnya (energi, entropy, lintasan puncak), mengikuti praktik literatur CSI [4], [11], [14], [15]. Klasifikator dimulai dari model yang jujur pada data kecil (SVM dan jaringan kecil 1D-CNN) dengan validasi silang per-sesi; strategi lintas-person dari Widar3.0 dipakai sebagai sumber strategi, bukan janji hasil [11], [12]. Seluruh pelatihan berjalan pada laptop; node ESP32 tidak dibebani pelatihan agar tetap sesuai kemampuan perangkat.",
          ],
        },
        {
          h2: "6.5 Metrik Evaluasi",
          paras: [
            "Kelayakan dinilai dari empat kelompok metrik: akurasi klasifikasi per-gestur dan confusion matrix pada skenario dalam-sesi dan lintas-sesi; tingkat alarm palsu per jam saat tidak ada gestur (termasuk saat orang lewat atau perabot bergeser); latensi ujung-ke-ujung dari selesainya gestur hingga entitas alert ter-update; dan kualitas dataset (jumlah repetisi valid, cakupan kelas). Kriteria keberhasilan ditetapkan bersama pembimbing sebelum eksperimen, dengan target indikatif akurasi per-gestur di atas 80 persen dalam-sesi pada subset 5 gestur sebagai tanda kelayakan lanjut.",
          ],
        },
        {
          h2: "6.6 Gerbang Go/No-Go Delta-CSI",
          paras: [
            "Pada minggu ketiga, uji fisik Delta-CSI dilakukan dengan dua node ESP32 di ruang mitra: membandingkan pola CSI ruang kosong, ruang terisi tanpa gestur, dan ruang dengan penandatangan aktif. Gerbang lolos bila delta antara kondisi penandatangan aktif dan tidak aktif terpisah jelas pada fitur Doppler pita gerak tanpa pembersihan khusus yang rumit; gerbang gagal bila pola tidak dapat dipisahkan setelah penempatan node dioptimalkan. Keputusan mengikuti protokol yang sama dengan tiga proposal sebelumnya: lanjut, kalibrasi ulang satu kali, atau beralih ke judul cadangan.",
          ],
        },
      ],
    },
    {
      h1: "7. Manajemen Risiko dan Rencana Fallback",
      paras: [
        "Risiko utama diidentifikasi dari tiga sumber: temuan eksplorasi kode RuView, literatur CSI lintas-domain, dan karakteristik bahasa isyarat itu sendiri. Tabel 4 merangkum risiko, dampak, dan rencana cadangan. Dua risiko di antaranya menuntut kejujuran sejak proposal: generalisasi lintas-person pada sensing CSI terbatas sehingga model diperlakukan sah per-sesi atau per-penandatangan dengan kalibrasi ulang [11], [12], dan gestur yang berbeda artinya namun mirip geraknya dapat saling tertukar sehingga pemilihan subset gestur dilakukan bersama guru, mengutamakan gestur yang dominan gerak lengan.",
      ],
      tables: [{
        caption: "Tabel N Risiko utama dan rencana cadangan",
        widths: [26, 22, 52],
        headers: ["Risiko", "Dampak bila terjadi", "Rencana cadangan (fallback)"],
        rows: [
          ["Gerbang fisik Delta-CSI minggu-3 gagal", "Paradigma klasifikasi CSI tidak layak di lokasi", "Lanjut sebagai studi karakterisasi sinyal + laporan kegagalan yang bermakna ilmiah; atau alih ke judul cadangan dari tabel usulan"],
          ["Akurasi lintas-person rendah", "Model tidak tahan ganti penandatangan", "Batas klaim: model sah per-sesi/per-penandatangan; dokumentasikan biaya kalibrasi ulang sebagai temuan"],
          ["Dataset kecil membuat model bias", "Akurasi tidak stabil antar-sesi", "Mulai dari 5 gestur dengan 30 repetisi; augmentasi sederhana; jangan menjanjikan akurasi di luar data"],
          ["Gestur ambigu (mirip gerak)", "Confusion matrix penuh pada pasangan tertentu", "Ganti pasangan gestur pada subset; pisahkan fitur Doppler; laporkan pasangan yang tak terpisahkan sebagai temuan"],
          ["Konfound gerak latar (kipas, orang lewat)", "Alarm palsu tinggi", "Log kejadian harian sebagai kovariat; penempatan node ulang; threshold energi gerak disetel per ruang"],
          ["Perizinan sekolah tertunda", "Pengambilan data mundur", "Mitra cadangan; simulasi di lab dengan penandatangan internal; urutan izin dimulai minggu pertama"],
        ],
      }],
    },
    {
      h1: "8. Jadwal Penelitian",
      paras: [
        "Jadwal disusun untuk satu semester (sekitar 4,5 bulan efektif) dengan gerbang keputusan yang menandai titik tidak-kembali. Tabel 5 merangkum kegiatan per rentang minggu beserta keluarannya; gerbang go/no-go pada minggu ketiga ditandai eksplisit dan menentukan jalur berikutnya.",
      ],
      tables: [{
        caption: "Tabel N Jadwal penelitian satu semester",
        widths: [34, 16, 50],
        headers: ["Kegiatan", "Minggu", "Keluaran"],
        rows: [
          ["Studi literatur lanjutan + penetapan subset gestur bersama guru", "W1-W2", "Daftar 5-12 gestur SIBI/BISINDO terpilih + lembar definisi"],
          ["Uji fisik Delta-CSI (GERBANG GO/NO-GO)", "W3", "Laporan karakterisasi + keputusan lanjut/kalibrasi/berhenti"],
          ["Perizinan berjenjang + kalibrasi ruang mitra", "W3-W5", "Surat persetujuan + sesi kalibrasi 600 frame + 8 anchor"],
          ["Perekaman dataset gestur (N repetisi per gestur)", "W6-W8", "Dataset berlabel + kamera ground truth tersinkron"],
          ["Ekstraksi fitur + pelatihan klasifikator", "W8-W11", "Model per-gestur + confusion matrix per-sesi"],
          ["Pengujian lintas-sesi + alarm palsu + latensi alert", "W12-W14", "Laporan metrik kelayakan lengkap"],
          ["Integrasi keluaran ke MQTT/Home Assistant (demo)", "W14-W15", "Demo entitas gesture terdeteksi pada dashboard"],
          ["Penulisan laporan + persiapan seminar", "W15-W18", "Draf skripsi + slide + dataset publik dirapikan"],
        ],
      }],
    },
    {
      h1: "9. Estimasi Anggaran",
      paras: [
        "Kebutuhan biaya disusun hemat dengan memanfaatkan perangkat yang sudah dimiliki mahasiswa. Tabel 6 merangkum komponen biaya; laptop pengolahan data menggunakan milik pribadi sehingga tidak dianggarkan, dan platform RuView tidak menimbulkan biaya lisensi karena open-source.",
      ],
      tables: [{
        caption: "Tabel N Rencana biaya penelitian",
        widths: [30, 34, 12, 24],
        headers: ["Komponen", "Spesifikasi", "Jumlah", "Estimasi Biaya (Rp)"],
        rows: [
          ["ESP32 DevKit", "Node TX dan RX untuk capture CSI", "2 unit", "120.000"],
          ["Aksesor elektronik", "Breadboard, jumper, adaptor, dudukan node", "1 set", "150.000"],
          ["Laptop pengolahan", "Milik pribadi (tidak dianggarkan)", "-", "0"],
          ["Transportasi mitra", "Kunjungan lokasi untuk kalibrasi dan perekaman", "±10 kunjungan", "400.000"],
          ["Pencetakan dan penggandaan", "Laporan, lembar izin, bahan seminar", "1 set", "150.000"],
          ["Cadangan (±15 persen)", "Penggantian perangkat rusak, kebutuhan tak terduga", "-", "130.000"],
          ["Total", "", "", "±950.000"],
        ],
      }],
    },
    {
      h1: "10. Daftar Referensi",
      refs: [
        "[1] Rodríguez-Correa, P. A., Valencia-Arias, A., Chanchí-Golondrino, G. E., & Palacio-Piedrahita, J. (2023). Benefits and development of assistive technologies for Deaf people's communication: A systematic review. Frontiers in Education, 8, 1121597. https://doi.org/10.3389/feduc.2023.1121597",
        "[2] Sanjaya, S. A., Ilone, H. F., dkk. (2023). BISINDO Sign Language Recognition: A systematic literature review of datasets, methods, and challenges. Indonesian Journal of Computer Science, 12(6). https://doi.org/10.33022/ijcs.v12i6.3539",
        "[3] Dwijayanti, S., Hermawati, F. A., & Taqiyyah, S. (2021). Indonesia Sign Language Recognition using Convolutional Neural Network. International Journal of Advanced Computer Science and Applications, 12(10). https://doi.org/10.14569/IJACSA.2021.0121046",
        "[4] Ma, Y., Zhou, G., & Wang, S. (2019). WiFi sensing with channel state information: A survey. ACM Computing Surveys, 52(3), 1-36. https://doi.org/10.1145/3310194",
        "[5] Hernandez, S. M., & Bulut, E. (2020). Lightweight and standalone IoT based WiFi sensing for active repositioning and mobility. In 2020 IEEE 21st International Symposium on \"A World of Wireless, Mobile and Multimedia Networks\" (WoWMoM). https://doi.org/10.1109/WoWMoM49955.2020.00056",
        "[6] Ma, Y., Zhou, G., & Wang, S. (2018). SignFi: Sign language recognition using WiFi. Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies, 2(1), 1-22. https://doi.org/10.1145/3191755",
        "[7] Baldeo, J. M. E. G., Canlas, dkk. (2024). Filipino Sign Language recognition using Wi-Fi channel state information. In TENCON 2024 - 2024 IEEE Region 10 Conference. https://doi.org/10.1109/TENCON61640.2024.10903008",
        "[8] Shang, J., & Wu, J. (2017). A robust sign language recognition system with multiple sparse Wi-Fi arrays. In Proceedings of the Workshop on Mobility in the Evolving Internet Architecture. https://doi.org/10.1145/3097620.3097624",
        "[9] Thariq Ahmed, H. F., Ahmad, H., & dkk. (2020). DF-WiSLR: Device-free Wi-Fi-based sign language recognition. Pervasive and Mobile Computing, 68, 101289. https://doi.org/10.1016/j.pmcj.2020.101289",
        "[10] Thariq Ahmed, H. F., & Ahmad, H. (2021). Wi-Fi CSI based human sign language recognition using LSTM network. In 2021 IEEE International Conference on Artificial Intelligence in ICT (IAICT). https://doi.org/10.1109/IAICT52856.2021.9532548",
        "[11] Zhang, Y., Zheng, Y., Qian, K., Zhang, G., Liu, Y., Wu, C., & Yang, Z. (2021). Widar3.0: Zero-effort cross-domain gesture recognition with Wi-Fi. IEEE Transactions on Pattern Analysis and Machine Intelligence, 44(11), 8671-8685. https://doi.org/10.1109/TPAMI.2021.3105387",
        "[12] Chen, C., Zhou, G., & Lin, Y. (2023). Cross-domain WiFi sensing with channel state information: A survey. ACM Computing Surveys, 55(11), 1-37. https://doi.org/10.1145/3570325",
        "[13] Hao, Z., Duan, Y., Dang, X., Liu, X., & Zhang, D. (2020). Wi-SL: Contactless fine-grained gesture recognition uses channel state information. Sensors, 20(14), 4025. https://doi.org/10.3390/s20144025",
        "[14] Sruthi, P., Satapathy, S. C., & Udgata, S. K. (2024). HandFi: WiFi sensing based hand gesture recognition using channel state information. Procedia Computer Science, 235, 110-117. https://doi.org/10.1016/j.procs.2024.04.042",
        "[15] Cai, Z., Li, Z., Chen, Z., & Zhu, dkk. (2024). Device-free wireless sensing for gesture recognition based on complementary amplitude and phase information. Sensors, 24(11), 3414. https://doi.org/10.3390/s24113414",
        "[16] Qin, Y., Pan, S., Zhou, W., & Pan, D. (2023). WiASL: American Sign Language writing recognition system using commercial devices. Measurement, 218, 113125. https://doi.org/10.1016/j.measurement.2023.113125",
        "[17] Kindy, G. O., Leonali, G., dkk. (2025). Word-level BISINDO: A novel video Indonesian sign language dataset and benchmark. Procedia Computer Science, 269. https://doi.org/10.1016/j.procs.2025.08.277",
        "[18] Wiguna, K. L., & Rojali. (2025). Sentence-level Indonesian Sign Language (BISINDO) recognition using 3D architecture. International Journal of Advanced Computer Science and Applications. https://doi.org/10.14569/IJACSA.2025.0160941",
        "[19] Sebastian, C., Limanza, J., dkk. (2025). Indonesian Sign Language (BISINDO) recognition using spatially aware blocks. Procedia Computer Science, 269. https://doi.org/10.1016/j.procs.2025.09.042",
      ],
    },
  ],
};
