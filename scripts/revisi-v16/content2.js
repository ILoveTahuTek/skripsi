// content2.js — Bagian 2 (Supervisi), Bagian 3 (Persamaan & Temporal), Bagian 4 (Deployment)
const { B, I, SUB, V, h1, h2, p, caption, note, eq, block, spacer, tbl } = require("./helpers");

function build() {
  const c = [];

  // ================= BAGIAN 2 =================
  c.push(h1("2. Pemisahan Supervisi: 24 Huruf Statis dan J/Z (Langkah 2)"));
  c.push(p([
    "Evaluasi menemukan ketidaksesuaian peran guru: hasil exp11_huruf24 tercatat untuk 24 huruf statis, sementara beberapa bagian lain menggambarkan YOLO26m-Pose memberi label kelas dan keypoint untuk seluruh 26 huruf (Subbab 2.9, 3.7, rumusan masalah 1.2, dan matriks 2.16). Ketidaksesuaian ini bukan sekadar redaksional \u2014 ia menyembunyikan asumsi berbahaya bahwa model guru yang teruji pada huruf statis otomatis menjadi pengklasifikasi huruf gerak. J dan Z didefinisikan oleh lintasan temporal, dan kepala kelas guru tidak dirancang untuk itu.",
  ]));
  c.push(p([
    "Perbaikannya memisahkan sumber supervisi menurut jenis target, sebagaimana Tabel 4. Prinsipnya satu kalimat: ",
    B("label kelas selalu berasal dari protokol perekaman"),
    " (kartu pemandu per repetisi), sedangkan guru visual menyumbang deret 21 keypoint dan visibilitasnya untuk semua huruf. Keluaran kelas guru hanya dipakai sebagai salinan pembanding untuk penyaringan kualitas, bukan sebagai label kebenaran.",
  ]));
  c.push(caption("Tabel 4  Matriks supervisi per target pelatihan"));
  c.push(tbl(null,
    ["Target", "Sumber supervisi", "Catatan"],
    [
      ["24 kelas statis", "Label protokol perekaman (kartu pemandu) + keypoint dari guru", "Label kelas tidak bergantung pada kepala kelas guru"],
      ["Huruf J", "Label target dari protokol + lintasan keypoint guru", "Kelas tidak diambil dari keluaran kelas guru"],
      ["Huruf Z", "Label target dari protokol + lintasan keypoint guru", "Sama seperti J"],
      ["21 keypoint", "YOLO26m-Pose sebagai guru visual", "Berstatus pseudo-label; disampel oleh validator (Subbab 3.6)"],
      ["Visibilitas keypoint", "Keluaran guru + verifikasi kualitas anotasi", "Mask per keypoint sebagaimana Subbab 2.7"],
    ],
    [20, 44, 36], { centerHeader: false }));
  c.push(spacer());
  c.push(p([
    "Satu pernyataan terbuka harus diselesaikan lewat verifikasi, bukan asumsi: dataset WPC versi 2 memuat 49 kelas isyarat, sehingga ",
    B("kemungkinan model guru memang memuat kelas J dan Z ada, tetapi belum terverifikasi"),
    " \u2014 exp11_huruf24 yang dikutip v16 jelas hanya 24 huruf statis. Bila verifikasi menemukan kelas J/Z pada model juara, keluaran kelas guru untuk J/Z tetap dipakai hanya sebagai pembanding penyaringan; sumber label kebenaran tetap protokol. Angka mAP50 0,9580 dan akurasi huruf 97,6% tidak dicabut, tetapi kutipannya dibatasi pada 24 huruf statis pada data visual \u2014 sebagaimana sudah dijaga kalimat penegas Subbab 2.9.",
  ]));

  c.push(h2("2.1 Blok teks siap sisip \u2014 supervisi"));
  c.push(...block("BLOK B-1 \u2014 Tambahkan paragraf setelah paragraf pertama Subbab 2.9", [
    ["\u201CPeran guru dipisahkan menurut jenis target. Untuk 24 huruf statis, label kelas pelatihan diambil dari protokol perekaman (kartu pemandu), sedangkan guru menyumbang deret 21 keypoint dan visibilitasnya. Untuk J dan Z, label kelas juga berasal dari protokol; guru tidak diposisikan sebagai pengklasifikasi kedua huruf gerak itu kecuali model guru terbukti memuat kelasnya [PERLU VERIFIKASI: kelas J dan Z pada model juara WPC]. Dengan pemisahan ini, hasil exp11_huruf24 pada 24 huruf statis tidak diperluas menjadi klaim pengenalan 26 huruf oleh guru.\u201D"],
  ]));
  c.push(...block("BLOK B-2 \u2014 Tambahkan kalimat setelah angka mAP50 dan akurasi pada Subbab 2.9", [
    ["\u201CAngka mAP50 0,9580 dan akurasi huruf 97,6% berlaku untuk 24 huruf statis pada data visual; angka itu tidak dikutip sebagai kemampuan guru mengenali J dan Z, yang supervisinya diambil dari lintasan keypoint dan label protokol sesuai matriks supervisi.\u201D"],
  ]));
  c.push(...block("BLOK B-3 \u2014 Tambahkan kalimat pada Subbab 3.7 (paragraf penyelarasan tiga deret)", [
    ["\u201CLabel kelas tiap segmen diambil dari kartu pemandu protokol; keluaran kelas guru hanya dipakai sebagai salinan pembanding untuk penyaringan kualitas, bukan sebagai label kebenaran. Ketidakcocokan antara label protokol dan kelas guru dicatat sebagai temuan kualitas anotasi dan dilaporkan bersama tingkat segmen terbuang.\u201D"],
  ]));

  // ================= BAGIAN 3 =================
  c.push(h1("3. Persamaan Optimasi dan Arsitektur Temporal (Langkah 3)"));
  c.push(p([
    "Evaluasi menemukan empat pernyataan yang saling meniadakan: Subbab 2.4 menyatakan hanya kepala tugas yang diperbarui; Subbab 2.8 menyatakan modul temporal ikut dilatih; Subbab 3.7 menyebut adapter masukan mungkin dilatih; sedangkan Persamaan 2.15 hanya menuliskan pembaruan \u03B8",
    SUB("c"),
    " dan \u03B8",
    SUB("r"),
    " dengan encoder tetap. Selain itu, keluaran regresi ",
    V("T") + "\u00D721\u00D72",
    " (Persamaan 2.11) tidak dapat dihasilkan oleh modul temporal yang merangkum seluruh barisan menjadi satu vektor \u2014 urutan waktu lenyap sebelum regresi bekerja. Bagian ini menutup keduanya dengan satu persamaan induk dan satu arsitektur temporal dua cabang.",
  ]));

  c.push(h2("3.1 Persamaan pembaruan tetapan"));
  c.push(p([
    "Persamaan 2.15 diganti dengan himpunan tetapan terlatih yang utuh:",
  ]));
  c.push(eq([
    { t: "\u0398", i: true }, { t: "train", sub: true },
    " = { ", { t: "\u03C6", i: true }, { t: "adapter", sub: true },
    ", ", { t: "\u03B8", i: true }, { t: "temporal", sub: true },
    ", ", { t: "\u03B8", i: true }, { t: "c", sub: true },
    ", ", { t: "\u03B8", i: true }, { t: "r", sub: true },
    " },   ", { t: "\u03B8", i: true }, { t: "encoder", sub: true },
    " = ", { t: "\u03B8", i: true }, { t: "0", sub: true },
  ], "(2.15\u2032)"));
  c.push(p([
    "dengan klausul eksplisit: \u03C6",
    SUB("adapter"),
    " hanya masuk himpunan bila jalur adapter terpilih pada gerbang G0b; \u03B8",
    SUB("encoder"),
    " tetap dibekukan pada \u03B8",
    SUB("0"),
    " sepanjang baseline, dan skema pembukaan tetapan (LoRA serta pelatihan lanjutan) tetap diperlakukan sebagai pembanding, bukan keputusan awal. Seluruh kalimat yang menyebut pembaruan tetapan lalu dirujuk ke Persamaan 2.15\u2032 sehingga 2.4, 2.8, dan 3.7 berbicara dalam satu bahasa. Pembaruan gradiennya tetap ditulis \u0398",
    SUB("train"),
    " \u2190 Optimizer(\u2207",
    V("L"),
    { t: "total", sub: true },
    ") sebagaimana semangat Persamaan 2.14.",
  ]));

  c.push(h2("3.2 Arsitektur temporal dua cabang"));
  c.push(p([
    "Modul temporal dirancang ulang sebagai ",
    B("pengolah barisan, bukan peringkas tunggal"),
    ". Ia memproses barisan embedding per langkah dan mengeluarkan keadaan tersembunyi per langkah ",
    V("h"), { t: "t", sub: true, i: true },
    " (1D-CNN kandidat utama karena memelihara dimensi waktu; pembandingnya pada ablasi tetap disiapkan). Dari situ dua cabang membaca: kepala klasifikasi membaca ringkasan beratensi atas barisan ",
    V("h"), { t: "t", sub: true, i: true },
    " menjadi satu vektor lalu menghitung skor kelas; kepala regresi membaca tiap keadaan secara langsung, ",
    V("Q"), { t: "t", sub: true, i: true },
    " = reshape(",
    V("W"), { t: "r", sub: true, i: true },
    "\u00B7",
    V("h"), { t: "t", sub: true, i: true },
    " + ",
    V("b"), { t: "r", sub: true, i: true },
    ", 21, 2) dengan ",
    V("W"), { t: "r", sub: true, i: true },
    " berukuran 42\u00D7128, sehingga keluaran regresi per segmen berbentuk ",
    V("T"), "\u00D721\u00D72",
    " tanpa kehilangan urutan waktu. Kepala per langkah ini hanya 5.418 parameter \u2014 jauh lebih ringan daripada varian peringkas tunggal Persamaan 2.11 yang membutuhkan 42",
    V("T"),
    "\u00D7128 \u2248 269 ribu parameter untuk ",
    V("T"),
    " = 50.",
  ]));
  c.push(p([
    "Varian peringkas tunggal tetap dipertahankan sebagai pembanding ablasi untuk huruf statis, dengan keterbatasannya bagi J dan Z dinyatakan pada laporan. Konsekuensi yang harus ditulis: kandidat agregasi statistik rata-rata\u2013maksimum hanya berlaku untuk jalur klasifikasi; pelatihan multitugas dengan regresi temporal menuntut modul yang memelihara urutan.",
  ]));

  c.push(h2("3.3 Panjang T, padding, dan segmen berbeda panjang"));
  c.push(p([
    "Panjang ",
    V("T"),
    " ditetapkan sebagai panjang maksimum langkah per segmen: ",
    V("T"),
    " = 16 langkah, cukup untuk segmen hingga sekitar empat detik pada lompatan 0,25 detik [usulan; difinalkan dari distribusi durasi segmen pada pilot T2]. Segmen yang lebih pendek diberi ",
    B("padding nol + mask valid"),
    ", dan kerugian regresi dinormalisasi oleh jumlah langkah valid \u2014 mask ",
    V("m"), { t: "itj", sub: true, i: true },
    " pada Persamaan 2.13 diperluas satu dimensi waktu. ",
    B("Resampling ke panjang tetap ditolak untuk pelatihan J/Z"),
    " karena interpolasi menyeragamkan durasi dan menghapus petunjuk kecepatan \u2014 justru petunjuk yang membedakan J dan Z dari huruf statis lain. Padding membiarkan durasi asli tetap terbaca oleh model.",
  ]));

  c.push(h2("3.4 Penyelarasan laju supervisi keypoint"));
  c.push(p([
    "Guru visual menghasilkan keypoint pada laju kamera, sedangkan langkah embedding lajunya empat per detik (lompatan 0,25 detik). Supaya tiap langkah punya satu target, deret keypoint guru disampel ulang ke pusat tiap jendela (rata-rata bingkai guru dalam jendela; interpolasi linear bila perlu), dan keluaran regresi model didefinisikan pada laju yang sama: per segmen, ",
    V("L"), { t: "valid", sub: true, i: true },
    "\u00D721\u00D72",
    " yang dipadatkan menjadi ",
    V("T"), "\u00D721\u00D72",
    " dengan mask. Untuk pelaporan galat lintasan J/Z pada Subbab 3.8.2, deret prediksi diinterpolasi kembali ke laju kamera agar dapat dibandingkan bingkai demi bingkai dengan acuan guru; metodenya dinyatakan pada laporan.",
  ]));

  c.push(h2("3.5 Blok teks siap sisip \u2014 persamaan dan temporal"));
  c.push(...block("BLOK C-1 \u2014 Ganti kalimat pengantar Persamaan 2.15 dan Persamaan 2.15 itu sendiri (Subbab 2.8)", [
    ["\u201CPada baseline, pembaruan tetapan menyentuh seluruh tetapan di luar encoder:",
    { size: 2, t: "" }],
    [{ t: "\u0398", i: true }, { t: "train", sub: true }, " = { ", { t: "\u03C6", i: true }, { t: "adapter", sub: true }, ", ", { t: "\u03B8", i: true }, { t: "temporal", sub: true }, ", ", { t: "\u03B8", i: true }, { t: "c", sub: true }, ", ", { t: "\u03B8", i: true }, { t: "r", sub: true }, " },   ", { t: "\u03B8", i: true }, { t: "encoder", sub: true }, " = ", { t: "\u03B8", i: true }, { t: "0", sub: true }, "   (2.15\u2032)"],
    ["dengan \u03C6", { t: "adapter", sub: true, i: true }, " tetapan adapter masukan yang hanya hadir bila jalur adapter terpilih pada gerbang G0b, \u03B8", { t: "temporal", sub: true, i: true }, " tetapan modul temporal, serta \u03B8", { t: "c", sub: true, i: true }, " dan \u03B8", { t: "r", sub: true, i: true }, " tetapan kedua kepala. Encoder tetap dibekukan pada \u03B8", { t: "0", sub: true, i: true }, " sepanjang baseline; skema pembukaan tetapan (LoRA dan pelatihan lanjutan) tetap diperlakukan sebagai pembanding pada Subbab 3.7. Seluruh rujukan pembaruan tetapan pada Subbab 2.4, 2.8, dan 3.7 dirujuk ke Persamaan 2.15\u2032.\u201D"],
  ]));
  c.push(...block("BLOK C-2 \u2014 Ganti paragraf modul temporal pada Subbab 2.8 (dan sesuaikan rujukan Persamaan 2.11 pada Subbab 2.7)", [
    ["\u201CModul temporal bukan kepala tugas dan tidak dirancang sebagai peringkas tunggal. Ia memproses barisan embedding per langkah dan mengeluarkan keadaan tersembunyi per langkah, h", { t: "1", sub: true, i: true }, " sampai h", { t: "T", sub: true, i: true }, ". Kepala klasifikasi membaca ringkasan beratensi atas barisan itu menjadi satu vektor, sedangkan kepala regresi membaca tiap keadaan secara langsung, Q", { t: "t", sub: true, i: true }, " = reshape(W", { t: "r", sub: true, i: true }, "\u00B7h", { t: "t", sub: true, i: true }, " + b", { t: "r", sub: true, i: true }, ", 21, 2) dengan W", { t: "r", sub: true, i: true }, " berukuran 42 \u00D7 128, sehingga keluaran regresi per segmen berbentuk T \u00D7 21 \u00D7 2 tanpa kehilangan urutan waktu. Varian peringkas tunggal (Persamaan 2.11) dipertahankan sebagai pembanding ablasi untuk huruf statis, dengan keterbatasannya bagi J dan Z dijelaskan pada laporan. Konsekuensinya, kandidat agregasi statistik rata-rata\u2013maksimum hanya berlaku untuk jalur klasifikasi; pelatihan multitugas dengan regresi temporal menuntut modul yang memelihara urutan.\u201D"],
  ]));
  c.push(...block("BLOK C-3 \u2014 Tambahkan paragraf panjang urutan pada Subbab 2.7 atau 3.7", [
    ["\u201CPanjang T ditetapkan 16 langkah per segmen (usulan; difinalkan dari distribusi durasi segmen pada pilot T2), menutup segmen hingga sekitar empat detik pada lompatan 0,25 detik. Segmen lebih pendek diberi padding nol dengan mask valid, dan kerugian regresi dinormalisasi oleh jumlah langkah valid \u2014 mask visibilitas Persamaan 2.13 diperluas satu dimensi waktu. Resampling ke panjang tetap tidak dipakai untuk pelatihan J dan Z karena menyeragamkan durasi dan menghapus petunjuk kecepatan yang justru membedakan kedua huruf itu.\u201D"],
  ]));
  c.push(...block("BLOK C-4 \u2014 Tambahkan paragraf penyelarasan laju supervisi pada Subbab 3.7", [
    ["\u201CDeret keypoint guru disampel ulang ke pusat tiap jendela fitur sehingga tiap langkah embedding memiliki satu target 21 \u00D7 2; keluaran regresi model didefinisikan pada laju yang sama. Untuk pelaporan galat lintasan J dan Z, deret prediksi diinterpolasi kembali ke laju kamera agar dapat dibandingkan bingkai demi bingkai dengan acuan guru, dan metode interpolasinya dinyatakan pada laporan.\u201D"],
  ]));

  // ================= BAGIAN 4 =================
  c.push(h1("4. Keputusan Model Deployment (Langkah 4)"));
  c.push(p([
    "Dua pernyataan v16 berjalan sendiri-sendiri: metodologi menyatakan \u201Cencoder, modul temporal, dan kedua kepala digabung menjadi satu graph inferensi, lalu dikuantisasi\u201D (Subbab 3.7), sedangkan diagram inferensi hanya menampilkan label dan skor dan Subbab 3.5 menyebut keypoint sebagai \u201Ckeluaran tambahan\u201D. Evaluasi meminta perbedaan ini dijadikan keputusan eksplisit. Kedua pilihannya dirangkum Tabel 5.",
  ]));
  c.push(caption("Tabel 5  Perbandingan dua model deployment"));
  c.push(tbl(null,
    ["Aspek", "Pilihan 1 \u2014 regresi hanya saat pelatihan (usulan baseline)", "Pilihan 2 \u2014 dua kepala aktif saat deployment"],
    [
      ["Peran regresi", "Supervisi tambahan yang merapikan representasi; kepala dilepas setelah pelatihan", "Keluaran kedua model; keypoint tersedia saat operasional"],
      ["Graph ekspor", "Adapter (bila ada) + encoder + modul temporal + kepala klasifikasi", "Seluruh model termasuk kepala regresi"],
      ["Beban ESP32-S3", "Terkecil: memori, komputasi, dan kuantisasi hanya untuk jalur klasifikasi", "Naik: keluaran 42T nilai per langkah ikut dihitung dan dikuantisasi"],
      ["Keluaran perangkat", "Label huruf + skor keyakinan", "Label + skor + deret keypoint (21\u00D72 per langkah)"],
      ["Manfaat debugging", "Keypoint tetap tersedia luring dari model penuh untuk analisis galat", "Keypoint dapat diamati langsung di perangkat"],
      ["Kapan dipilih", "Regresi diposisikan supervisi tambahan \u2014 sejalan dengan hipotesis Subbab 2.8 dan kriteria G1 yang hanya melaporkan MPJPE", "Hanya bila ablasi menunjukkan manfaat multitugas besar dan kebutuhan keypoint di perangkat terdokumentasi (misalnya diagnosis validator)"],
    ],
    [18, 41, 41], { centerHeader: false }));
  c.push(spacer());
  c.push(p([
    "Rekomendasi evaluasi \u2014 ",
    B("Pilihan 1 sebagai baseline deployment"),
    " \u2014 diikuti karena tiga alasannya kokoh: regresi memang diposisikan sebagai supervisi tambahan, G1 hanya melaporkan MPJPE tanpa ambang kelayakan, dan biaya memori serta kuantisasi di ESP32-S3 hemat. Namun sesuai tuntutan evaluasi, keputusan ini dinyatakan terbuka secara formal: ia dicatat sebagai parameter pada Tabel 3.7 v16 (\u201Cmodel deployment: Pilihan 1 atau 2\u201D) dengan dasar penetapan \u201Ctujuan eksperimen dan hasil ablasi manfaat regresi\u201D, dan Pilihan 2 tetap terbuka bila bukti mengarah ke sana.",
  ]));
  c.push(p([
    "Ikutannya pada metrik: dengan Pilihan 1, MPJPE dan PCK@\u03B1 tetap dihitung dan dilaporkan sebagai metrik pemantauan mutu supervisi \u2014 diharapkan menurun terhadap epoch awal dan dirinci untuk pasangan huruf paling mirip serta J/Z \u2014 tetapi tidak menjadi syarat lolos G1. Bila Pilihan 2 yang terpilih, ambang kelayakan regresi (misalnya PCK@\u03B1) ditetapkan lebih dulu pada Tabel 3.7 sebelum gerbang dinilai; MPJPE tanpa ambang memang tidak bermakna sebagai gerbang.",
  ]));

  c.push(h2("4.1 Blok teks siap sisip \u2014 deployment"));
  c.push(...block("BLOK D-1 \u2014 Ganti kalimat \u201CSetelah terpilih, encoder, modul temporal, dan kedua kepala digabung \u2026\u201D pada Subbab 3.7", [
    ["\u201CSetelah terpilih, model deployment disusun menurut Pilihan 1: encoder, adapter (bila dipakai), modul temporal, dan kepala klasifikasi digabung menjadi satu graph inferensi lalu dikuantisasi; kepala regresi dilepas setelah pelatihan karena perannya sebagai supervisi tambahan. Kepala regresi ikut dijalankan pada deployment (Pilihan 2) hanya bila keputusan pada Tabel 3.7 menyatakannya, dengan tambahan biaya memori, komputasi, dan kuantisasi yang diukur serta dilaporkan.\u201D"],
  ]));
  c.push(...block("BLOK D-2 \u2014 Sesuaikan Gambar 3.5 dan kalimat \u201Ckeluaran tambahan\u201D pada Subbab 3.5", [
    ["\u201CGambar 3.5 disesuaikan: simpul model terkuantisasi menampilkan label huruf dan skor keyakinan sebagai satu-satunya keluaran deployment; jalur keypoint hanya digambar pada diagram pelatihan (jalur guru). Kalimat \u2018estimasi keypoint dari kepala regresi menjadi keluaran tambahan\u2019 pada Subbab 3.5 diganti menjadi pernyataan Pilihan 1 beserta rujukan keputusannya pada Tabel 3.7.\u201D"],
  ]));
  c.push(...block("BLOK D-3 \u2014 Tambahkan baris pada Tabel 3.7 dan klausul metrik pada Subbab 2.14", [
    ["Baris baru Tabel 3.7: \u201CModel deployment (Pilihan 1: klasifikator saja; Pilihan 2: dua kepala aktif) \u2014 dasar penetapan: tujuan eksperimen dan hasil ablasi manfaat regresi \u2014 status: [PERLU DATA: keputusan dan dasarnya]\u201D."],
    ["Klausul Subbab 2.14: \u201CPada baseline Pilihan 1, MPJPE dan PCK@\u03B1 berstatus metrik pemantauan yang dilaporkan, bukan syarat gerbang; bila Pilihan 2 dipilih, ambang kelayakan regresi ditetapkan pada Tabel 3.7 sebelum G1 dinilai.\u201D"],
  ]));

  return c;
}

module.exports = { build };
