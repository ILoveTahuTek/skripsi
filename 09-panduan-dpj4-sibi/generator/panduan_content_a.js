// panduan_content_a.js — Bagian 1-4 dari Panduan Penulisan Proposal DPJ-4 (SIBI-only)
"use strict";

const chaptersA = [
  // ================= BAGIAN 1 =================
  {
    h1: "1. TENTANG PANDUAN INI",
    subs: [
      {
        h2: "1.1 Tujuan dan Cara Memakai Panduan",
        paras: [
          "Panduan ini menyatukan seluruh aturan penulisan yang dipelajari dari folder Drive berisi 69 dokumen korpus D4 Teknologi Rekayasa Sistem Elektronika (TRSE) Universitas Negeri Malang (proposal tugas akhir, naskah, seminar hasil, dan dokumen paten), rubrik evaluasi hasil optimasi GEPA, aturan bahasa dari skill naskah-id, serta 22 referensi yang telah diverifikasi melalui Crossref, lalu menerapkannya secara khusus untuk satu kebutuhan: menulis ulang DPJ-4 ke lingkup SIBI saja tanpa BISINDO. Setiap bagian memuat aturan yang berlaku, templat kalimat siap tempel yang diambil literal dari korpus, dan contoh penerapannya pada konteks bahasa isyarat SIBI. Dengan demikian, revisi dapat dikerjakan secara mandiri tanpa menebak-nebak gaya yang diharapkan pembimbing.",
          "Cara memakai panduan ini terdiri atas tiga langkah. Pertama, baca Bagian 2 untuk memahami makna dan implikasi keputusan lingkup SIBI-only, termasuk argumen yang dapat dipertahankan di hadapan pembimbing dan jebakan yang harus dihindari. Kedua, kerjakan revisi per bagian dokumen dengan mengikuti peta revisi pada Bagian 6 sambil menempelkan templat bahasa dari Bagian 3 dan menjaga disiplin klaim dari Bagian 5. Ketiga, akhiri dengan checklist pada Bagian 8 dan jalankan alat pemeriksaan yang tersedia agar dokumen lolos semua gerbang mutu sebelum dibawa ke pembimbing.",
          "Seluruh bahan pendukung sudah tersedia dan tidak perlu dibuat ulang. Repositori skripsi memuat empat file markdown DPJ (folder 08-markdown-dpj) dan DOCX yang sinkron (folder 03-dpj), 22 referensi terverifikasi DOI beserta gap-analisis (folder 06-referensi-isyarat), pemetaan fitur RuView untuk kasus isyarat, generator DOCX, evaluator rubrik D1-D6, dan pemeriksa bahasa periksa.py. Panduan ini merangkai semuanya menjadi satu alur kerja tunggal sehingga yang tersisa hanyalah pekerjaan penyuntingan yang terarah.",
        ],
      },
      {
        h2: "1.2 Keputusan Lingkup: SIBI tanpa BISINDO",
        paras: [
          "Keputusan lingkup baru mengunci target bahasa penelitian pada satu sistem, yaitu Sistem Isyarat Bahasa Indonesia (SIBI); BISINDO keluar dari objek penelitian dan hanya boleh muncul sebagai konteks literatur serta arah pengembangan lanjutan. Keputusan ini mengubah inti narasi DPJ-4 versi lama, yang justru berdiri di atas ketegangan dua sistem: sekolah formal cenderung memakai SIBI sedangkan pergaulan siswa berlangsung dalam BISINDO sehingga alat bantu idealnya mengenali keduanya. Kalimat-kalimat dengan pola seperti itu harus hilang dari dokumen baru karena mereka memotivasi cakupan dua sistem, bukan satu.",
          "Lingkup SIBI-only dapat dipertahankan dengan tiga argumen yang kuat di hadapan pembimbing. Pertama, SIBI bersifat formal dan terstandar sehingga selaras dengan target konteks prasarana edukasi formal; definisi subset gestur dapat dirujuk secara konsisten pada satu rujukan sistem yang sama, sesuatu yang tidak dimiliki variasi komunitas. Kedua, lingkup satu sistem menekan beban dataset dan pelabelan agar realistis untuk satu semester, karena perekaman 5 sampai 12 gestur dengan 30 repetisi per gestur per sesi sudah merupakan beban yang berat. Ketiga, kebaruan kombinatif tetap utuh: pencarian literatur saat penyusunan DPJ-4 belum menemukan satu pun publikasi pengenalan isyarat berbasis Wi-Fi CSI untuk bahasa isyarat Indonesia apa pun, termasuk SIBI. Klaim pertama untuk SIBI karena itu tetap sah secara literatur.",
          "Hampir seluruh kerangka penelitian tidak berubah oleh keputusan ini. Struktur BAB I sampai BAB III plus Daftar Pustaka, platform ESP32 dua node dengan firmware RuView, paradigma klasifikasi gestur langsung dari pola Channel State Information (CSI), gerbang go/no-go uji fisik Delta-CSI pada minggu ketiga, tabel jadwal-biaya-risiko, serta 19 referensi terverifikasi semuanya dipertahankan. Yang berubah hanyalah bahasa target dan seluruh kalimat yang memotivasi cakupan dua sistem, mulai dari judul, rumusan masalah, tujuan, batasan, hingga satu subbab kajian pustaka.",
          "Jebakan terbesar revisi ini adalah menyisakan kalimat dua sistem di dokumen satu sistem. Contoh frasa yang wajib dihapus atau ditulis ulang adalah bermakna sama pada kedua sistem, sebaiknya menguji gestur yang berakar pada kedua sistem, dan idealnya mengenali keduanya, bukan salah satunya saja. Pembimbing lazim menguji konsistensi lingkup, dan satu frasa saja yang tersisa dapat membatalkan kredibilitas keputusan pengetatan. Bagian 6 memuat daftar lengkap titik-titik yang harus disentuh agar tidak ada yang lolos.",
        ],
      },
    ],
  },
  // ================= BAGIAN 2 =================
  {
    h1: "2. STRUKTUR WAJIB PROPOSAL (BAB I-III)",
    subs: [
      {
        h2: "2.1 Ruang Lingkup Dokumen",
        paras: [
          "Proposal berbeda dari skripsi: dokumen pengajuan judul hanya mencakup BAB I PENDAHULUAN, BAB II KAJIAN PUSTAKA, BAB III METODE PENELITIAN, dan DAFTAR PUSTAKA. Korpus TRSE memang menggunakan struktur lima bab untuk naskah selesai, tetapi tahap pengajuan judul berhenti pada metode penelitian; konten rencana (jadwal, biaya, risiko) dikonsolidasikan menjadi subbab di BAB III, bukan bab terpisah. Dokumen tidak memakai halaman sampul, lembar pengesahan, kata pengantar, abstrak, maupun daftar isi, sesuai keputusan pemilik yang konsisten diterapkan pada keempat DPJ sebelumnya.",
          "Judul dokumen diletakkan di paling atas, ditulis KAPITAL SEMUA dan terpusat, mengikuti pola korpus RANCANG BANGUN atau IMPLEMENTASI atau PERANCANGAN atau SISTEM diikuti BERBASIS, PADA atau UNTUK, lalu STUDI KELAYAKAN. Penomoran halaman Arab mulai dari 1 pada footer dengan format - N -, dan tidak ada page break di tengah isi. Penamaan bab dibuat konsisten sepanjang dokumen: pilih KAJIAN PUSTAKA (bukan TINJAUAN PUSTAKA) dan METODE PENELITIAN (bukan METODOLOGI PENELITIAN), mengikuti pilihan yang sudah dipakai DPJ-4 lama.",
        ],
      },
      {
        h2: "2.2 Kerangka Lengkap DPJ-4 SIBI-only",
        paras: [
          "Tabel 2.1 merangkum kerangka lengkap proposal yang menjadi target revisi, beserta isi wajib setiap subbab. Kerangka ini identik dengan DPJ-4 versi lama kecuali pada titik-titik yang disebut di kolom isi wajib sebagai khusus SIBI. Gunakan tabel ini sebagai peta saat menyusun ulang dokumen agar tidak ada subbab wajib yang tertinggal.",
        ],
        tables: [
          {
            caption: "Tabel 2.1 Kerangka wajib proposal DPJ-4 SIBI-only",
            headers: ["Bab", "Subbab", "Isi wajib"],
            widths: [23, 26, 51],
            rows: [
              ["BAB I PENDAHULUAN", "1.1 Latar Belakang", "Corong 4 lapis versi SIBI (Bagian 3.1) + Tabel 1.1 usulan judul utama dan dua alternatif"],
              ["", "1.2 Rumusan Masalah", "Pembuka korpus + 3 pertanyaan berpola Bagaimana (templat di 6.4)"],
              ["", "1.3 Tujuan Penelitian", "Pembuka korpus + 3 frasa kerja yang mirror rumusan (templat di 6.4)"],
              ["", "1.4 Batasan Masalah", "7 item bernomor; item terakhir Penelitian ini tidak membahas; ditutup pernyataan disiplin klaim (Bagian 5.3)"],
              ["", "1.5 Manfaat Penelitian", "Paragraf pengantar + 1.5.1 Manfaat Teoretis + 1.5.2 Manfaat Praktis (Bagi Peneliti, Bagi Sekolah dan Guru, Bagi Pengguna, Bagi Praktisi)"],
              ["BAB II KAJIAN PUSTAKA", "2.1 Wi-Fi Channel State Information", "Definisi CSI, fisika modulasi Doppler gerak lengan, sitasi survei Ma dkk. dan Chen dkk."],
              ["", "2.2 Mikrokontroler ESP32", "ESP32-CSI-Tool (Hernandez dan Bulut), dua node mengapit zona penandatangan, biaya rendah untuk replikasi sekolah"],
              ["", "2.3 Platform RuView", "Fitur terukur + Tabel 2.1 pemetaan fitur + dua batas jujur (pose stub PCK@20 sekitar 3 persen; person counting lemah)"],
              ["", "2.4 Pengenalan Isyarat Berbasis Wi-Fi CSI", "Rantai bukti: WiSign, SignFi, DF-WiSLR, LSTM, Widar3.0, lalu granularitas halus (Wi-SL, HandFi, Cai, WiASL)"],
              ["", "2.5 Sistem Isyarat Bahasa Indonesia (SIBI)", "Khusus SIBI: definisi dan sifat formal-terstandar + lanskap riset isyarat Indonesia berbasis visi sebagai bukti celah (Bagian 6.5)"],
              ["", "2.6 Penelitian Terdahulu", "Prosa gap + daftar bernomor mengisi celah + Tabel 2.2 komparasi (baris terakhir Penelitian Ini dengan kolom SIBI)"],
              ["BAB III METODE PENELITIAN", "3.1 Tahapan Penelitian", "Narasi tahapan korpus + paragraf studi kelayakan bergerbang (artefak tetap per tahap)"],
              ["", "3.2 Studi Literatur", "Tiga kelompok sumber, rentang 2017-2025, verifikasi Crossref untuk semua referensi"],
              ["", "3.3 Perancangan Arsitektur Sistem", "Tiga lapisan: sensing dua node ESP32, pengolahan (kalibrasi, segmentasi, fitur Doppler 1-60 Hz), penyajian (dashboard, alert MQTT/Home Assistant)"],
              ["", "3.4 Perancangan Perangkat Keras", "Dua unit ESP32 DevKit + satu cadangan, dudukan setinggi dada, laptop milik pribadi, kamera hanya untuk pelabelan"],
              ["", "3.5 Perancangan Perangkat Lunak dan Dataset", "Protokol perekaman dataset SIBI (khusus SIBI): kalibrasi ruang, N repetisi per gestur, metadata, fitur amplitudo-fase-Doppler, klasifikator SVM dan 1D-CNN"],
              ["", "3.6 Lokasi, Partisipan, dan Etika", "Mitra \u3010Nama Sekolah/Lokasi\u3011, subjek utama guru/pembina SIBI, izin berjenjang, mode privasi RuView"],
              ["", "3.7 Rencana Pengujian", "Tiga kelompok: uji fisik Delta-CSI (gerbang), uji klasifikasi, uji operasional (alarm palsu, latensi)"],
              ["", "3.8 Evaluasi dan Kriteria Keberhasilan", "Empat kelompok metrik + kriteria gerbang go/no-go minggu ketiga (lolos, kalibrasi ulang satu kali, atau beralih judul cadangan)"],
              ["", "3.9 Rencana Kegiatan dan Jadwal Penelitian", "Tabel 3.1 jadwal satu semester; gerbang go/no-go minggu ketiga ditandai eksplisit"],
              ["", "3.10 Rencana Biaya Penelitian", "Tabel 3.2 komponen biaya dalam Rupiah (tidak berubah oleh pengetatan lingkup)"],
              ["", "3.11 Analisis Risiko dan Rencana Cadangan", "Tabel 3.3 risiko, dampak, dan fallback per risiko"],
              ["DAFTAR PUSTAKA", "-", "APA edisi 7, hanging indent, URL https://doi.org pada setiap entri, urut nomor sitasi"],
            ],
          },
        ],
      },
      {
        h2: "2.3 Tabel-Tabel Wajib dan Aturan Penulisannya",
        paras: [
          "Ada enam tabel yang wajib ada pada proposal ini: Tabel 1.1 usulan judul penelitian, Tabel 2.1 pemetaan fitur RuView, Tabel 2.2 perbandingan penelitian terdahulu, Tabel 3.1 jadwal penelitian satu semester, Tabel 3.2 rencana biaya, dan Tabel 3.3 risiko beserta rencana cadangan. Seluruh tabel memakai gaya three-line (garis atas, garis bawah header, garis bawah tabel) tanpa garis vertikal, dengan judul tabel di atas tabel berpola Tabel nomor.bab.urut dilanjutkan judul singkat.",
          "Tabel komparasi penelitian terdahulu memakai tanda centang dan tanda minus untuk menyatakan ada-tidaknya fitur, dengan baris terakhir selalu bernama Penelitian Ini. Setiap tabel didahului kalimat pengantar yang merujuk nomor tabel, misalnya Tabel 2.2 membandingkan penelitian terdahulu dengan penelitian ini, dan ditutup analisis singkat setelah tabel. Tabel tidak boleh menggantung tanpa pembahasan karena rubrik D1 memeriksa keterkaitan narasi dan tabel.",
        ],
      },
    ],
  },
  // ================= BAGIAN 3 =================
  {
    h1: "3. POLA BAHASA KORPUS (TEMPLAT LITERAL)",
    subs: [
      {
        h2: "3.1 Corong Latar Belakang Empat Lapis, Versi SIBI",
        paras: [
          "Latar belakang korpus selalu berbentuk corong empat lapis yang menyempit dari konteks umum ke keputusan penelitian. Lapis pertama adalah konteks umum, satu paragraf yang membuka kondisi lapangan. Lapis kedua memperjelas masalah spesifik pada praktik yang ada beserta kelemahannya. Lapis ketiga memperkenalkan satu paragraf per teknologi penyuluhan dengan sitasi pada setiap paragraf. Lapis keempat menutup dengan keputusan penelitian. Untuk DPJ-4 SIBI-only, lapis satu sampai tiga dipertahankan dari dokumen lama karena isinya tidak menyentuh pertanyaan bahasa target.",
          "Lapis 1 dan 2 boleh disalin dari DPJ-4 lama tanpa perubahan. Lapis 1 membuka cara teknologi memengaruhi layanan pendidikan bagi kelompok tunarungu; lapis 2 menguraikan tiga hambatan pendekatan kamera di lingkungan pendidikan, yaitu beban privasi dan kesiapan institusi, ketergantungan pada pencahayaan dan sudut pandang, serta biaya solusi komersial yang tidak realistis untuk sekolah. Lapis 3 memperkenalkan CSI sebagai informasi fase dan amplitudo subcarrier yang berubah saat gelombang terganggu gerakan tubuh, lalu ESP32 dengan basis ESP32-CSI-Tool, lalu bukti paradigma SignFi dan preseden Filipino Sign Language, lalu platform RuView sebagai fondasi rekayasa. Semua sitasi pada lapis ini tetap dipakai.",
          "Lapis 4 harus ditulis ulang karena versi lama berisi argumen dua sistem. Templat penggantinya ada di Bagian 6.3; intinya memperkenalkan SIBI sebagai sistem formal yang selaras dengan target prasarana edukasi formal, memberi dua keuntungan metodologis penargetan satu sistem, memposisikan BISINDO sebagai pengembangan lanjutan, lalu menutup dengan kalimat korpus Berdasarkan uraian tersebut, penelitian ini dilakukan untuk menguji kelayakan pengenalan gestur terisolasi bahasa isyarat SIBI dari pola Wi-Fi CSI pada ESP32 sebagai langkah awal translasi tanpa kamera di prasarana edukasi. Perhatikan bahwa frasa pembuka penutup ini wajib utuh karena merupakan penanda gaya korpus yang diperiksa evaluator.",
        ],
      },
      {
        h2: "3.2 Kalimat Pembuka Subbab BAB I",
        paras: [
          "Empat subbab BAB I punya kalimat pembuka baku yang diambil literal dari korpus dan sudah diterapkan pada keempat DPJ. Tempelkan pola berikut apa adanya, cukup mengganti isi pada bagian dalam tanda kutip. Konsistensi pembuka ini dinilai pada rubrik D2 sehingga mengubah polanya berisiko menurunkan skor tanpa manfaat apa pun.",
        ],
        quotes: [
          "Pembuka 1.2 Rumusan Masalah: Berdasarkan latar belakang permasalahan yang telah diuraikan serta untuk menjawab permasalahan yang menjadi fokus dalam penelitian ini, maka dapat dirumuskan beberapa rumusan masalah yang akan dikaji lebih lanjut. Rumusan masalah pada penelitian ini adalah sebagai berikut. Item bernomor berupa pertanyaan Bagaimana, tiga butir.",
          "Pembuka 1.3 Tujuan Penelitian: Penelitian ini bertujuan menguji kelayakan pengenalan gestur terisolasi bahasa isyarat SIBI dari pola Wi-Fi CSI pada ESP32 untuk prasarana edukasi. Adapun tujuan dari penelitian ini adalah sebagai berikut. Item bernomor berupa frasa kerja: Merancang, Mengimplementasikan, Menguji, mirror satu-satu dengan rumusan masalah.",
          "Pembuka 1.4 Batasan Masalah: Agar penelitian ini memiliki ruang lingkup yang jelas dan terarah sesuai dengan tujuan yang telah ditetapkan, maka ditentukan batasan masalah guna membatasi pembahasan terhadap aspek-aspek yang relevan dengan topik penelitian. Adapun batasan masalah pada penelitian ini adalah sebagai berikut. Item terakhir selalu berpola Penelitian ini tidak membahas.",
          "Pembuka 1.5 Manfaat Penelitian: paragraf pengantar singkat, lalu subbab 1.5.1 Manfaat Teoretis yang menempatkan penelitian sebagai referensi pengembangan bidang, dan 1.5.2 Manfaat Praktis dengan sub-item Bagi Peneliti, Bagi Sekolah dan Guru, Bagi Pengguna, serta Bagi Praktisi Teknologi.",
        ],
      },
      {
        h2: "3.3 Narasi Tahapan Metodologi",
        paras: [
          "Pembuka BAB III pada korpus selalu berupa narasi tahapan yang tersusun sistematis. Pola ini sudah terbukti lolos pembimbing pada keempat DPJ dan dipertahankan untuk versi SIBI-only dengan satu penggantian kata: pemetaan subset gestur dilakukan bersama guru atau pembina yang menguasai SIBI.",
        ],
        quotes: [
          "Penelitian dalam proposal ini dilaksanakan melalui beberapa tahapan yang tersusun secara sistematis sehingga membentuk suatu alur penelitian yang terstruktur. Tahap pertama adalah studi literatur, yaitu pemetaan sistematis pengenalan isyarat CSI dan bahasa isyarat Indonesia beserta penetapan subset gestur bersama guru atau pembina yang menguasai SIBI. Tahap kedua adalah perancangan sistem, mencakup penyiapan dua node ESP32 dengan firmware RuView, skenario penempatan node di ruang edukasi, dan protokol perekaman dataset. Tahap ketiga adalah implementasi, yaitu perekaman dataset gestur berlabel, ekstraksi fitur, dan pelatihan klasifikator. Tahap terakhir adalah pengujian dan evaluasi. Apabila dalam proses pengujian ditemukan kendala, maka dilakukan evaluasi dan perbaikan secara berulang hingga sistem dapat dievaluasi secara adil.",
        ],
        paras2: [],
      },
      {
        h2: "3.4 Sitasi dan Daftar Pustaka",
        paras: [
          "Sitasi dalam teks memakai pola korpus: Nama dkk. (Tahun) menjelaskan bahwa, Nama dkk. (Tahun) menunjukkan bahwa, atau Nama dan Nama (Tahun) membangun, diakhiri nomor sitasi dalam kurung siku yang berurutan sesuai kemunculan. Kata kerja pelaporan korpus yang aman adalah menjelaskan, menunjukkan, memperlihatkan, dan menyoroti. Hindari kata kerja berorientasi penulis seperti mengklaim atau membuktikan secara mutlak, karena gaya akademik korpus menempatkan literatur sebagai sumber yang dilaporkan, bukan sebagai vonis.",
          "Daftar pustaka ditulis dalam APA edisi 7 dengan hanging indent dan URL https://doi.org pada setiap entri yang punya DOI, berurutan sesuai nomor sitasi. Pola entri jurnalnya adalah Nama, A. (Tahun). Judul artikel. Nama Jurnal, volume(nomor), halaman. https://doi.org/nomor. Pola prosiding mengganti nama jurnal dengan nama prosiding diawali kata In. Seluruh 19 entri DPJ-4 sudah berformat ini dan tinggal dipindahkan; aturan penambahannya diatur di Bagian 6.7.",
          "Setelah tabel penelitian terdahulu, korpus selalu menaruh prosa gap dengan pola tetap: Berdasarkan tabel perbandingan di atas, terlihat bahwa, lalu ringkasan dua kutub penelitian, lalu Masih terdapat beberapa celah masalah (gap) yang belum terselesaikan secara simultan oleh peneliti sebelumnya, ditutup Penelitian ini mengisi celah tersebut dengan langkah-langkah berikut dan daftar bernomor tiga butir. Templat lengkap versi SIBI ada di Bagian 6.5.",
        ],
      },
      {
        h2: "3.5 Mekanika Penulisan",
        bullets: [
          "Judul dokumen KAPITAL SEMUA dan terpusat; judul alternatif ditulis normal setelahnya.",
          "Penomoran tabel dan gambar per bab: Tabel 2.2, Gambar 3.1, dengan judul; setiap tabel dan gambar dirujuk dalam teks sebelum muncul.",
          "Ejaan PUEBI: memengaruhi (bukan mempengaruhi), desimal koma (0,5 sampai 3 detik), persen tanpa spasi (80 persen), tanpa orang pertama (saya, kami).",
          "Subjek kalimat adalah penelitian ini, sistem, atau alat; paragraf berisi 3 sampai 8 kalimat; tidak ada bullet tanpa kalimat pengantar.",
          "Istilah teknis asing lazim dipertahankan dalam Latin: capture, dataset, device-free, embedded, dashboard; definisinya diberikan pada kalimat perkenalan istilah, bukan kurung berlebihan.",
          "Tidak ada penanda akhir dokumen artifisial seperti garis atau kalimat penutup meta; dokumen berakhir pada entri Daftar Pustaka terakhir.",
        ],
      },
    ],
  },
  // ================= BAGIAN 4 =================
  {
    h1: "4. EJAAN, KATA BAKU, DAN GAYA (PELAJARAN NASKAH-ID)",
    subs: [
      {
        h2: "4.1 Aturan yang Wajib Dipertahankan Saat Revisi",
        paras: [
          "Pada sesi perbaikan bahasa sebelumnya, empat DPJ sudah disunting menyeluruh dengan lebih dari 60 pasangan perbaikan berdasarkan aturan PUEBI dan pola-pola anti-kalke. Panduan ini meringkas aturan yang paling relevan agar pekerjaan revisi SIBI-only tidak menghidupkan kembali kesalahan yang sudah dibersihkan. Prinsipnya sederhana: saat menulis ulang sebuah paragraf, salin dari versi lama yang sudah bersih, bukan dari memori.",
        ],
        tables: [
          {
            caption: "Tabel 4.1 Perbaikan baku yang sudah diterapkan dan harus dipertahankan",
            headers: ["Pola yang dihindari", "Bentuk baku", "Catatan"],
            widths: [30, 30, 40],
            rows: [
              ["et al.", "dkk.", "Sudah diganti 46 kali pada 4 DPJ; jangan muncul lagi"],
              ["mempengaruhi", "memengaruhi", "PUEBI; pola pembuka corong memakai kata ini"],
              ["di mana (non-interogatif)", "yang di / letaknya", "Di mana hanya untuk pertanyaan"],
              ["koma sebelum sehingga", "tanpa koma", "Kalimat komposit EJ-10; periksa setiap sehingga"],
              ["entropy, threshold", "entropi, ambang", "Istilah Inggris non-lazim diindonesiakan"],
              ["lintas-person, kontak-less", "lintas-penandatangan, tanpa kontak", "Anti-kalke Inggris; serangkai dengan tanda hubung"],
              ["antarsesi, antarruang (dipisah salah)", "antarsesi, antarruang serangkai", "Awalan antar- ditulis serangkai"],
              ["Doppler huruf kecil", "Doppler (kapital)", "Nama orang"],
              ["kalimat lebih dari 35 kata", "dipecah menjadi dua", "Kalimat efektif; cek paragraf hasil tempel"],
              ["Mengetahui hasil pengujian (tujuan)", "Menguji hasil pengujian", "Frasa kerja konkret, bukan nominalisasi"],
            ],
          },
        ],
      },
      {
        h2: "4.2 Alat Periksa dan Keputusan yang Masih Terbuka",
        paras: [
          "Pemeriksa bahasa periksa.py dari skill naskah-id bisa dijalankan pada file markdown untuk menemukan pola ejaan dan gaya yang melanggar; hasil bersih ditandai nol temuan. Jalankan alat ini setelah setiap sesi penyuntingan besar, bukan hanya di akhir, karena pola koma-sehingga dan kalimat panjang paling mudah terbawa saat menempel teks baru. Detail pemanggilan ada di Bagian 8.2.",
          "Satu keputusan masih terbuka sejak sesi sebelumnya: pencetakan miring untuk istilah asing ditunda menunggu pedoman kampus, karena aturan lokal didahulukan dan konsistensi lebih penting daripada miring sebagian istilah saja. Sampai pedoman tersedia, pertahankan istilah teknis asing dalam bentuk tegak seperti sekarang, dan catat keputusan ini pada checklist Bagian 8 agar tidak terlupa saat dokumen final disiapkan.",
        ],
      },
    ],
  },
];

module.exports = { chaptersA };
