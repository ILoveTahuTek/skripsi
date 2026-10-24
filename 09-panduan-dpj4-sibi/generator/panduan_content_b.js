// panduan_content_b.js — Bagian 5-8 dari Panduan Penulisan Proposal DPJ-4 (SIBI-only)
"use strict";

const chaptersB = [
  // ================= BAGIAN 5 =================
  {
    h1: "5. DISIPLIN KLAIM SIBI-ONLY",
    subs: [
      {
        h2: "5.1 Aturan Inti",
        numbered: [
          "Semua klaim dibatasi studi kelayakan. Framing yang benar adalah menguji kelayakan, mengevaluasi kemampuan, dan menghasilkan dataset beserta rekomendasi, bukan membangun sistem jadi yang menerjemahkan.",
          "Paradigma yang benar adalah klasifikasi gestur langsung dari pola CSI. Modul pose 17 keypoint RuView adalah stub dengan PCK@20 sekitar 3 persen sehingga ekstraksi pose atau kerangka tangan terlarang dijanjikan; preseden paradigma adalah SignFi 2018, DF-WiSLR 2020, Widar3.0 2021, dan FSL-CSI TENCON 2024.",
          "Gerbang fisik Delta-CSI dua node ESP32 adalah titik go/no-go pada minggu ketiga; jadwal wajib menandainya eksplisit dan keputusan lanjut, kalibrasi ulang satu kali, atau beralih judul cadangan mengikutinya.",
          "Risiko utama dan mitigasinya eksplisit per risiko pada Tabel 3.3, mencakup lintas-domain, dataset, konfound lingkungan, dan etika.",
        ],
        paras: [
          "Keempat aturan ini tidak berubah oleh pengetatan lingkup; yang berubah hanyalah objek yang tidak diklaim, yaitu BISINDO kini masuk daftar eksklusi eksplisit bersama penerjemahan kontinu dan multi-penandatangan. Pernyataan disiplin pada 5.3 sudah mengikat kelima hal itu dalam satu paragraf yang ditempel di akhir 1.4.",
        ],
      },
      {
        h2: "5.2 Tabel Batas Klaim Versi SIBI-only",
        paras: [
          "Tabel 5.1 mengikat apa yang boleh dan tidak boleh diklaim pada proposal versi SIBI-only. Gunakan tabel ini saat menyusun setiap paragraf klaim; bila sebuah kalimat berada di kolom kanan, tulis ulang sampai berada di kolom kiri atau hapus.",
        ],
        tables: [
          {
            caption: "Tabel 5.1 Batas klaim proposal SIBI-only",
            headers: ["Boleh diklaim", "Tidak boleh diklaim"],
            widths: [50, 50],
            rows: [
              ["Kelayakan klasifikasi gestur terisolasi 5 sampai 12 kelas SIBI yang dominan gerak lengan", "Penerjemah kalimat bahasa isyarat kontinu (BLEU/WER)"],
              ["Dataset CSI SIBI pertama: protokol perekaman + mini-dataset publik berlabel", "Dataset BISINDO atau pengenalan BISINDO pada penelitian ini"],
              ["Integrasi keluaran klasifikasi ke jalur alert RuView (MQTT/Home Assistant)", "Ekstraksi pose atau kerangka tangan (stub PCK@20 3 persen)"],
              ["Model sah per sesi atau per penandatangan dengan kalibrasi ulang", "Multi-penandatangan simultan; akurasi lintas-ruang tanpa kalibrasi"],
              ["Kebaruan kombinatif: pertama untuk SIBI via Wi-Fi CSI pada konteks edukasi", "Klaim menemukan metode baru secara umum"],
            ],
          },
        ],
      },
      {
        h2: "5.3 Pernyataan Disiplin Klaim (Templat Siap Tempel)",
        paras: [
          "Pernyataan berikut ditempatkan sebagai paragraf penutup subbab 1.4, tepat setelah item tidak membahas. Templat ini sudah diadaptasi untuk lingkup SIBI-only, termasuk butir eksklusi BISINDO pada huruf e.",
        ],
        quotes: [
          "Penelitian ini merupakan studi kelayakan pengenalan gestur terisolasi dari pola Wi-Fi CSI pada platform RuView (capture + DSP + alert) dengan target bahasa Sistem Isyarat Bahasa Indonesia (SIBI). Penelitian ini tidak mengklaim: (a) ekstraksi pose atau kerangka tangan; (b) penerjemahan kalimat bahasa isyarat kontinu; (c) pengenalan multi-penandatangan simultan; (d) akurasi lintas-ruang tanpa kalibrasi ulang; (e) pengenalan BISINDO atau sistem isyarat komunitas lain. Kelayakan diuji pada subset 5 sampai 12 gestur SIBI yang dominan gerak lengan, dengan satu penandatangan per sesi, di ruang edukasi yang terkalibrasi. Gerbang fisik Delta-CSI 2×ESP32 pada lokasi target (minggu ketiga) menjadi titik go/no-go penelitian.",
        ],
      },
    ],
  },
  // ================= BAGIAN 6 =================
  {
    h1: "6. PETA REVISI DPJ-4 KE LINGKUP SIBI-ONLY",
    subs: [
      {
        h2: "6.1 Ringkasan Perubahan Per Bagian",
        paras: [
          "Tabel 6.1 memetakan seluruh titik yang berubah saat dokumen SIBI+BISINDO dipadatkan menjadi SIBI-only, beserta tindakannya. Tiga bagian terakhir (biaya, risiko, daftar pustaka) secara prinsip tidak berubah isinya dan hanya perlu diperiksa ulang. Rincian templat untuk titik-titik besar ada pada subbab 6.2 sampai 6.7.",
        ],
        tables: [
          {
            caption: "Tabel 6.1 Peta revisi per bagian dokumen",
            headers: ["Bagian", "Yang berubah", "Tindakan"],
            widths: [22, 48, 30],
            rows: [
              ["Judul utama + 2 alternatif", "Frasa SIBI dan BISINDO / SIBI/BISINDO menjadi SIBI", "Ganti (templat 6.2)"],
              ["Tabel 1.1 catatan pemetaan", "Catatan baris utama menyebut dua sistem", "Ganti menjadi SIBI (subset gestur terpilih)"],
              ["1.1 Latar Belakang lapis 4", "Narasi ketegangan dua sistem", "Tulis ulang dengan templat 6.3"],
              ["1.2 Rumusan Masalah", "SIBI/BISINDO pada 3 butir", "Ganti kata (templat 6.4)"],
              ["1.3 Tujuan Penelitian", "SIBI dan BISINDO pada pembuka", "Ganti kata (templat 6.4)"],
              ["1.4 Batasan Masalah", "Butir 1 bermakna sama pada kedua sistem", "Tulis ulang butir 1; sisipkan butir eksklusi BISINDO; tutup dengan templat 5.3"],
              ["1.5 Manfaat Penelitian", "Klaim belum ada publikasi CSI SIBI atau BISINDO tetap benar", "Pertahankan; cek ejaan"],
              ["2.5 Judul dan isi subbab", "Bahasa Isyarat Indonesia: SIBI dan BISINDO", "Retitel Sistem Isyarat Bahasa Indonesia (SIBI) + tulis ulang (templat 6.5)"],
              ["2.6 dan Tabel 2.2", "Baris Penelitian Ini: SIBI & BISINDO", "Ganti sel menjadi SIBI; prosa gap tetap menyebut dua kutub"],
              ["3.1 Tahapan", "guru/pembina yang memahami SIBI dan BISINDO", "Ganti menjadi menguasai SIBI"],
              ["3.5 Dataset", "Kriteria subset dua sistem", "Subset dari rujukan SIBI + preferensi separasi kinematik (6.6)"],
              ["3.6 Partisipan", "Penandatangan dewasa", "Sebut eksplisit guru/pembina SIBI"],
              ["Tabel 3.1 jadwal", "Baris W1-W2 menyebut SIBI/BISINDO", "Ganti menjadi Daftar 5-12 gestur SIBI terpilih"],
              ["Tabel 3.2 biaya", "Tidak berubah", "Periksa ulang saja"],
              ["3.11 dan Tabel 3.3 risiko", "Tidak berubah", "Periksa ulang kata isyarat dua sistem"],
              ["DAFTAR PUSTAKA", "19 entri tetap dipakai", "Pertahankan; kebijakan di 6.7"],
            ],
          },
        ],
      },
      {
        h2: "6.2 Usulan Judul Versi SIBI-only",
        paras: [
          "Tiga judul berikut diadaptasi langsung dari versi lama dengan menghapus BISINDO dan merapikan polanya; pemetaan kata ke hal yang terukur tetap berlaku, yaitu SIBI berarti subset gestur terpilih, studi kelayakan berarti batas klaim, ESP32 dan Wi-Fi CSI berarti perangkat serta sinyal yang diklasifikasikan, dan prasarana edukasi berarti lokasi kalibrasi.",
        ],
        runParas: [
          { seg: [{ t: "Judul utama: ", b: true }, { t: "PENGENALAN GESTUR BAHASA ISYARAT SIBI BERBASIS WI-FI CHANNEL STATE INFORMATION PADA ESP32 UNTUK PRASARANA EDUKASI: STUDI KELAYAKAN TRANSLASI TANPA KAMERA", b: true }], noIndent: true, after: 120 },
          { seg: [{ t: "Judul Alternatif 1: ", b: true }, { t: "Studi Kelayakan Klasifikasi Gestur Terisolasi SIBI dari Pola Wi-Fi CSI pada Platform RuView untuk Ruang Kelas Tunarungu" }], noIndent: true, after: 120 },
          { seg: [{ t: "Judul Alternatif 2: ", b: true }, { t: "Dataset dan Klasifikasi Gestur Sistem Isyarat Bahasa Indonesia (SIBI) dari Sinyal Wi-Fi CSI pada ESP32: Studi Kelayakan Alat Bantu Komunikasi Pendidikan Tunarungu" }], noIndent: true, after: 120 },
        ],
        paras2: [
          "Judul Alternatif 2 sengaja memakai bentuk panjang Sistem Isyarat Bahasa Indonesia (SIBI) agar pola nama lengkap-lalu-singkatan tetap muncul minimal sekali di halaman judul dokumen. Setelah judul ditetapkan, samakan istilah bahasa target di Tabel 1.1 dengan catatan pemetaan yang baru sehingga tabel dan judul tidak saling bertentangan.",
        ],
      },
      {
        h2: "6.3 Menulis Ulang Lapis 4 Latar Belakang",
        paras: [
          "Lapis 4 versi lama memotivasi dua sistem dengan kalimat ketegangan SIBI-BISINDO; versi baru harus memotivasi satu sistem tanpa membohongi realitas lapangan. Templat berikut menjalankan tugas itu dalam satu paragraf utuh: memperkenalkan SIBI sebagai sistem formal sekolah, memberi dua keuntungan metodologis, memposisikan BISINDO sebagai pengembangan lanjutan, lalu menutup dengan kalimat korpus. Salin dan sesuaikan seperlunya, lalu lanjutkan dengan kalimat pengantar Tabel 1.1.",
        ],
        quotes: [
          "Di Indonesia, sistem isyarat yang diajarkan pada lembaga pendidikan formal adalah SIBI (Sistem Isyarat Bahasa Indonesia), sistem yang bersifat formal dan terstandar sehingga definisi gesturnya dapat dirujuk secara konsisten pada satu rujukan yang sama. Menargetkan satu sistem formal memberikan dua keuntungan metodologis bagi studi kelayakan: dataset dapat didefinisikan secara konsisten dari satu rujukan sistem, dan beban pelabelan tetap terkendali pada durasi satu semester. Pengenalan sistem lain seperti BISINDO yang tumbuh secara alami di komunitas diposisikan sebagai pengembangan lanjutan setelah kelayakan paradigma terbukti pada SIBI. Berdasarkan uraian tersebut, penelitian ini dilakukan untuk menguji kelayakan pengenalan gestur terisolasi bahasa isyarat SIBI dari pola Wi-Fi CSI pada ESP32 sebagai langkah awal translasi tanpa kamera di prasarana edukasi. Tabel 1.1 merangkum usulan judul utama beserta dua judul alternatifnya.",
        ],
      },
      {
        h2: "6.4 Rumusan, Tujuan, dan Batasan Versi SIBI-only",
        paras: [
          "Tiga blok berikut sudah diadaptasi penuh dan siap tempel. Pembuka masing-masing mengikuti pola korpus dari Bagian 3.2. Perhatikan bahwa batasan kini berisi tujuh butir: satu butir eksklusi BISINDO disisipkan sebagai butir kedua agar keputusan lingkup terbaca sejak awal, dan butir terakhir tetap pola tidak membahas yang kini juga menyebut BISINDO secara eksplisit.",
        ],
        runParas: [
          { seg: [{ t: "Rumusan masalah (setelah pembuka 1.2):", b: true }], noIndent: true, after: 60 },
        ],
        numbered: [
          "Bagaimana perancangan sistem capture Wi-Fi CSI dua node ESP32 berbasis platform RuView beserta protokol pengumpulan dataset gestur SIBI terisolasi di ruang edukasi yang terkalibrasi?",
          "Bagaimana implementasi ekstraksi fitur dan pelatihan klasifikator gestur dari pola amplitudo, fase, dan Doppler CSI untuk subset gestur SIBI yang dominan gerak lengan?",
          "Bagaimana hasil pengujian akurasi klasifikasi per gestur, tingkat alarm palsu, dan integrasi keluaran klasifikasi ke jalur alert RuView (MQTT/Home Assistant) sebagai indikator kelayakan translasi tanpa kamera?",
        ],
      },
      {
        runParas: [
          { seg: [{ t: "Tujuan penelitian (setelah pembuka 1.3):", b: true }], noIndent: true, after: 60 },
        ],
        quotes: [
          "1. Merancang sistem capture Wi-Fi CSI dua node ESP32 berbasis RuView beserta protokol pengumpulan dataset gestur terisolasi SIBI yang terdokumentasi dan dapat direplikasi. 2. Mengimplementasikan ekstraksi fitur dan pelatihan klasifikator gestur dari pola amplitudo, fase, dan Doppler CSI untuk subset gestur SIBI yang dipilih. 3. Menguji akurasi klasifikasi per gestur, alarm palsu, dan kelayakan integrasi keluaran ke jalur alert RuView, termasuk keputusan go/no-go pada uji fisik Delta-CSI di minggu ketiga.",
        ],
      },
      {
        runParas: [
          { seg: [{ t: "Batasan masalah (setelah pembuka 1.4):", b: true }], noIndent: true, after: 60 },
        ],
        quotes: [
          "1. Lingkup penelitian adalah studi kelayakan pengenalan gestur terisolasi (isolated) pada subset 5 sampai 12 gestur SIBI yang dominan gerak lengan dan memiliki definisi konsisten pada rujukan sistem yang sama, bukan penerjemah kalimat bahasa isyarat kontinu. 2. Target bahasa diikat pada SIBI; pengenalan BISINDO tidak diuji pada penelitian ini dan diposisikan sebagai pengembangan lanjutan. 3. Satu penandatangan per sesi capture di zona pengambilan data; sistem tidak mengidentifikasi individu dan person counting tidak dijanjikan karena kualitasnya menurun pada lebih dari dua sampai tiga subjek. 4. Kamera hanya digunakan saat perekaman dataset untuk pelabelan ground truth; penggunaan operasional sistem bebas kamera. 5. Ekstraksi pose atau kerangka tangan tidak dipakai dan tidak dijanjikan karena modul pose on-device RuView masih berupa stub (PCK@20 sekitar 3 persen); klasifikasi dilakukan langsung dari pola CSI. 6. Setiap ruang edukasi mitra di \u3010Nama Sekolah/Lokasi\u3011 wajib dikalibrasi ulang (600 frame + 8 anchor) dan model dianggap sah untuk sesi yang sama, bukan lintas ruang tanpa kalibrasi. 7. Penelitian ini tidak membahas penerjemahan kontinu dua arah, pengenalan BISINDO, pengenalan beberapa penandatangan secara simultan, akurasi lintas ruang tanpa kalibrasi, ekstraksi pose tangan, serta aspek komersialisasi alat.",
        ],
      },
      {
        h2: "6.5 BAB II: Subbab SIBI dan Prosa Gap",
        paras: [
          "Subbab 2.5 diganti judulnya menjadi Sistem Isyarat Bahasa Indonesia (SIBI). Paragraf pertamanya mendefinisikan SIBI dan menautkan sifat formal-terstandar pada kebutuhan dataset; paragraf keduanya menghadirkan lanskap riset isyarat Indonesia yang seluruhnya berbasis visi sebagai bukti celah, dengan tetap menyitasi kelima referensi lokal. Referensi BISINDO tidak dihapus karena justru mereka yang membuktikan bahwa belum ada jalur CSI pada bahasa isyarat Indonesia apa pun; yang berubah adalah peran mereka, dari objek pembanding sejajar menjadi bukti lanskap dan celah.",
        ],
        quotes: [
          "Pembuka 2.5 baru: Sistem Isyarat Bahasa Indonesia (SIBI) merupakan sistem isyarat yang bersifat formal dan terstandar serta diajarkan pada lembaga pendidikan formal sehingga definisi gesturnya dapat dirujuk secara konsisten untuk pembangunan dataset penelitian ini. Pada penelitian ini, subset gestur diambil dari sistem SIBI dengan preferensi gestur yang dominan gerak lengan agar komponen Doppler CSI cukup kuat untuk dipisahkan dari latar.",
          "Prosa lanskap dan celah (paragraf kedua 2.5): Riset pengenalan bahasa isyarat Indonesia tumbuh pesat dan seluruhnya berbasis kamera serta pengolahan citra: Dwijayanti dkk. (2021) menerapkan CNN untuk pengenalan isyarat Indonesia \u005B3\u005D, dataset video tingkat kata disusun oleh Kindy dkk. (2025) \u005B17\u005D, pengenalan kalimat berbasis arsitektur 3D dilakukan Wiguna dan Rojali (2025) \u005B18\u005D, dan pendekatan sadar-ruang ditawarkan Sebastian dkk. (2025) \u005B19\u005D. Tinjauan sistematis Sanjaya dkk. (2023) menegaskan dominasi kamera pada keseluruhan riset tersebut dan mencatat belum adanya pendekatan sensor wireless device-free \u005B2\u005D. Belum ditemukan satu pun publikasi pengenalan isyarat berbasis Wi-Fi CSI untuk SIBI maupun BISINDO sehingga celah kebaruan bagi penelitian ini tetap terbuka.",
        ],
        paras2: [
          "Pada 2.6, baris Penelitian Ini pada Tabel 2.2 diubah dari SIBI & BISINDO menjadi SIBI pada kolom Bahasa Isyarat Indonesia, sementara prosa gap tetap menuliskan dua kutub (isyarat CSI pada bahasa dunia versus riset isyarat Indonesia berbasis kamera) karena kutub-kutub itu sendiri tidak berubah oleh pengetatan lingkup. Daftar tiga butir mengisi celah dipertahankan dengan mengganti SIBI dan BISINDO menjadi SIBI pada butir pertama.",
        ],
      },
      {
        h2: "6.6 BAB III: Subset Gestur dan Partisipan",
        paras: [
          "Pada 3.1, penggantian kata memahami SIBI dan BISINDO menjadi menguasai SIBI sudah cukup. Pada 3.5, kriteria pemilihan subset ditulis ulang: gestur diambil dari rujukan sistem SIBI yang sama, didahulukan yang dominan gerak lengan, dan yang secara kinematik berbeda besar satu sama lain agar confusion matrix tidak penuh pada pasangan mirip; kriteria mirip gerak tetap menjadi item pada Tabel 3.3. Tabel 3.1 baris pertama menjadi Daftar 5-12 gestur SIBI terpilih beserta lembar definisi.",
          "Pada 3.6, subjek utama ditulis eksplisit sebagai guru atau pembina yang menguasai SIBI, karena mereka yang mengajarkan sistem formal di sekolah mitra; siswa tetap mungkin menjadi partisipan sukarela untuk pengujian variasi dengan persetujuan orang tua. Seluruh pernyataan etika, mode privasi, dan perekaman kamera untuk ground truth dipertahankan apa adanya karena tidak tersentuh pengetatan lingkup.",
        ],
      },
      {
        h2: "6.7 Kebijakan Referensi",
        numbered: [
          "Semua 19 referensi DPJ-4 tetap dipakai. Kelima entri isyarat Indonesia (Dwijayanti; Kindy; Wiguna dan Rojali; Sebastian; Sanjaya) mayoritas menargetkan BISINDO; pada proposal SIBI-only posisinya adalah bukti lanskap dan bukti celah, bukan target penelitian.",
          "Klaim kebaruan ditulis dua lapis: belum ada publikasi CSI untuk SIBI maupun BISINDO (pernyataan tentang literatur, tetap benar), lalu penelitian ini menargetkan SIBI (pernyataan tentang lingkup). Jangan menulis belum ada riset apa pun tentang SIBI karena itu tidak terverifikasi.",
          "Dilarang menambah referensi baru tanpa verifikasi Crossref yang mencocokkan judul, penulis, tahun, dan venue terhadap DOI terdaftar; referensi tanpa DOI wajib lolos verifikasi web kedua berupa venue, tahun, dan penulis.",
          "Bila pembimbing meminta sumber definisi SIBI, cari literaturnya, verifikasi dulu sesuai aturan nomor 3, lalu masukkan; jangan mengarang tahun atau nomor kamus.",
          "Bila referensi bertambah, perbarui file verified_refs.json pada folder 06-referensi-isyarat agar arsip verifikasi tetap satu sumber kebenaran.",
        ],
      },
    ],
  },
  // ================= BAGIAN 7 =================
  {
    h1: "7. DAFTAR REFERENSI TERVERIFIKASI (PERAN SIBI-ONLY)",
    subs: [
      {
        h2: "7.1 Peta Referensi dan Perannya",
        paras: [
          "Seluruh 19 referensi pada DPJ-4 sudah diverifikasi melalui Crossref pada sesi riset T2-a dan tidak ada satu pun yang hanya terverifikasi web. Tabel 7.1 merangkum setiap entri beserta perannya pada proposal SIBI-only agar saat menulis dapat langsung dipilih referensi yang tepat untuk setiap klaim. Kategorinya empat: intisari paradigma (bukti klasifikasi isyarat dari CSI), konteks edukasi, lanskap-celah (riset isyarat Indonesia berbasis visi), dan teknis pipeline.",
        ],
        tables: [
          {
            caption: "Tabel 7.1 Referensi terverifikasi dan perannya pada proposal SIBI-only",
            headers: ["No", "Referensi", "DOI", "Peran"],
            widths: [6, 40, 26, 28],
            centerCols: [0],
            rows: [
              ["1", "Rodr\u00edguez-Correa dkk. (2023), Frontiers in Education", "10.3389/feduc.2023.1121597", "Konteks edukasi: hambatan komunikasi tunarungu"],
              ["2", "Sanjaya dkk. (2023), Indonesian J. Computer Science", "10.33022/ijcs.v12i6.3539", "Lanskap-celah: SLR BISINDO 100 persen visi"],
              ["3", "Dwijayanti dkk. (2021), IJACSA", "10.14569/IJACSA.2021.0121046", "Lanskap-celah: CNN isyarat Indonesia"],
              ["4", "Ma dkk. (2019), ACM Computing Surveys", "10.1145/3310194", "Teknis: survei kanonik CSI"],
              ["5", "Hernandez dan Bulut (2020), WoWMoM", "10.1109/WoWMoM49955.2020.00056", "Teknis: basis ESP32-CSI-Tool"],
              ["6", "Ma dkk. (2018), SignFi, IMWUT", "10.1145/3191755", "Intisari: 276 isyarat dari CSI"],
              ["7", "Baldeo dkk. (2024), TENCON", "10.1109/TENCON61640.2024.10903008", "Intisari: preseden FSL, analog porting ke SIBI"],
              ["8", "Shang dan Wu (2017), MobiArch", "10.1145/3097620.3097624", "Teknis: topologi multi-node"],
              ["9", "Thariq Ahmed dkk. (2020), DF-WiSLR", "10.1016/j.pmcj.2020.101289", "Intisari: pipeline 30+19 gestur device-free"],
              ["10", "Thariq Ahmed dan Ahmad (2021), IAICT", "10.1109/IAICT52856.2021.9532548", "Teknis: LSTM temporal pada CSI"],
              ["11", "Zhang dkk. (2021), Widar3.0, TPAMI", "10.1109/TPAMI.2021.3105387", "Intisari: strategi lintas-domain, bukan janji"],
              ["12", "Chen dkk. (2023), ACM Computing Surveys", "10.1145/3570325", "Teknis: survei cross-domain"],
              ["13", "Hao dkk. (2020), Wi-SL, Sensors", "10.3390/s20144025", "Teknis: 12 gestur perangkat murah"],
              ["14", "Sruthi dkk. (2024), HandFi, Procedia CS", "10.1016/j.procs.2024.04.042", "Teknis: pipeline amplitudo-fase"],
              ["15", "Cai dkk. (2024), Sensors", "10.3390/s24113414", "Teknis: komplementaritas amplitudo-fase"],
              ["16", "Qin dkk. (2023), WiASL, Measurement", "10.1016/j.measurement.2023.113125", "Teknis: arah aplikasi praktis"],
              ["17", "Kindy dkk. (2025), Procedia CS", "10.1016/j.procs.2025.08.277", "Lanskap-celah: dataset video BISINDO"],
              ["18", "Wiguna dan Rojali (2025), IJACSA", "10.14569/IJACSA.2025.0160941", "Lanskap-celah: level kalimat masih visi"],
              ["19", "Sebastian dkk. (2025), Procedia CS", "10.1016/j.procs.2025.09.042", "Lanskap-celah: klasifikasi per-gestur"],
            ],
          },
        ],
        parasAfterTables: [
          "Kelima entri lanskap-celah tetap wajib disitasi meski menargetkan BISINDO, dengan peran sebagai bukti celah sebagaimana dijelaskan pada 6.5 dan 6.7. Bila penulisan BAB II akhirnya memakai lebih sedikit entri daripada 19, pastikan tidak ada nomor sitasi yang menggantung tanpa entri maupun entri tanpa sitasi; penomoran mengikuti urutan kemunculan dalam teks.",
        ],
      },
    ],
  },
  // ================= BAGIAN 8 =================
  {
    h1: "8. CHECKLIST AKHIR DAN ALAT QA",
    subs: [
      {
        h2: "8.1 Checklist Rubrik D1-D6 Versi SIBI-only",
        bullets: [
          "D1 Struktur: hanya BAB I-III + DAFTAR PUSTAKA; semua subbab wajib Tabel 2.1 terisi; enam tabel utuh; penamaan bab konsisten (KAJIAN PUSTAKA, METODE PENELITIAN); tanpa cover, tanpa abstrak, tanpa daftar isi.",
          "D2 Pola bahasa: keempat pembuka subbab BAB I memakai pola korpus; item tujuan berupa frasa kerja; batasan ditutup butir tidak membahas; target bahasa konsisten SIBI di seluruh dokumen.",
          "D3 Sitasi: pola Nama dkk. (Tahun) menjelaskan/menunjukkan; nomor sitasi berurutan dan cocok satu-satu dengan Daftar Pustaka; APA 7 + URL DOI; nol referensi fiktif.",
          "D4 Mekanika: judul kapital semua; Tabel/Gambar bernomor per bab dan dirujuk dalam teks; memengaruhi; desimal koma; tanpa orang pertama; nol kalimat lebih dari 35 kata.",
          "D5 Disiplin: pernyataan studi kelayakan menempel di akhir 1.4; pose stub tidak dijanjikan; gerbang go/no-go minggu ketiga eksplisit di Tabel 3.1 dan 3.8; risiko beserta fallback lengkap.",
          "D6 Kelengkapan: satu judul utama + dua alternatif; jadwal semester; biaya Rupiah; risiko; placeholder eksplisit \u3010Nama Sekolah/Lokasi\u3011 dan \u3010Mohon diisi\u3011 pada biaya; tanpa halaman sampul.",
          "Konsistensi lingkup (baru): pencarian kata BISINDO hanya boleh muncul pada konteks literatur 2.5, butir batasan, pernyataan disiplin butir e, dan Daftar Pustaka; pencarian frasa SIBI dan BISINDO maupun SIBI/BISINDO sebagai target harus nol.",
        ],
      },
      {
        h2: "8.2 Alat QA dan Urutan Menjalankannya",
        numbered: [
          "Periksa bahasa: python3 skills/naskah-id/scripts/periksa.py <file.md> dijalankan setelah setiap sesi penyuntingan; target nol temuan.",
          "Evaluasi rubrik: python3 skills/proposal-writing/scripts/evaluator.py --doc <file.md> pada dokumen akhir; skor minimal 0,8 dengan dimensi terendah diperbaiki lebih dulu.",
          "Regenerasi DOCX: node scripts/generate_dpj.js setelah konten pada modul JS disunting, atau sunting DOCX langsung bila revisi kecil; jangan biarkan dua format berbeda isi.",
          "Postcheck DOCX: python3 <folder skill docx>/scripts/postcheck.py <file.docx>; semua error wajib dibereskan sebelum dokumen dipakai.",
          "Sinkronisasi dua format: python3 scripts/verify_sync_dpj.py membandingkan markdown dan DOCX hasil pandoc round-trip; target identik setelah normalisasi padding tabel.",
          "Konversi PDF untuk pemeriksaan visual: soffice --headless --convert-to pdf, lalu periksa jumlah halaman, tabel three-line, dan halaman judul.",
        ],
      },
      {
        h2: "8.3 Keputusan yang Masih Milik Pemilik dan Langkah Berikutnya",
        numbered: [
          "Konfirmasi judul kepada pembimbing: pilih di antara judul utama dan dua alternatif pada 6.2 sebelum revisi penuh dimulai, karena seluruh dokumen mengikuti judul yang dipilih.",
          "Isi placeholder: \u3010Nama Sekolah/Lokasi\u3011 pada 1.4 dan 3.6, dan baris total biaya pada Tabel 3.2 bila angka final sudah ada.",
          "Konfirmasi pencetakan miring istilah asing begitu pedoman kampus tersedia, lalu jalankan ulang seluruh QA.",
          "Lakukan uji fisik Delta-CSI dua node ESP32 di lokasi target pada minggu ketiga; hasil gerbang ini menentukan apakah proposal berjalan, dikalibrasi ulang, atau beralih ke judul cadangan.",
          "Setelah revisi SIBI-only selesai dan disetujui pembimbing, perbarui markdown dan DOCX bersamaan, jalankan seluruh alat QA pada 8.2, lalu commit dan push ke repositori dengan pesan yang menyebut pengetatan lingkup.",
        ],
        paras: [
          "Dengan seluruh checklist terpenuhi, dokumen hasil revisi berada pada taruhan mutu yang sama dengan empat DPJ sebelumnya yang semuanya mencapai skor evaluator 1,0. Perbedaannya kini terletak pada lingkup yang lebih fokus: satu sistem isyarat, satu rujukan definisi, dan satu lintasan kebaruan yang jelas untuk dibawa ke meja pembimbing.",
        ],
      },
    ],
  },
];

module.exports = { chaptersB };
