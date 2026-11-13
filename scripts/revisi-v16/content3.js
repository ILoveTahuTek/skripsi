// content3.js — Bagian 5 (Audio), 6 (Parameter & Temuan), 7 (Administratif), 8 (Peta Sisipan), 9 (Batasan Klaim)
const { B, I, SUB, V, h1, h2, p, caption, note, block, spacer, tbl, bullet } = require("./helpers");

function build() {
  const c = [];

  // ================= BAGIAN 5 =================
  c.push(h1("5. Arsitektur Audio Terpadu (Langkah 5)"));
  c.push(p([
    "Evaluasi menemukan Tabel 3.1 dan Subbab 3.5 berbicara tentang dua sistem yang berbeda: tabel perangkat keras menulis speaker dengan DAC I2S untuk \u201Cpemutaran suara TTS dari modul\u201D dan laptop ASUS TUF sebagai \u201Cserver cadangan\u201D, sementara subbab sistem menyatakan Kokoro ONNX disintesis di ponsel melalui Tauri dan ASR memakai layanan awan dengan server lokal sebagai cadangan. Lima pertanyaan teknis evaluasi \u2014 di mana audio mikrofon diproses, dari mana speaker modul menerima suara, apakah TTS diputar di ponsel, apa fungsi laptop saat daring, dan apakah server Rust sekadar perantara \u2014 semuanya lahir dari kontradiksi ini.",
  ]));
  c.push(h2("5.1 Keputusan D1: akhiran judul"));
  c.push(p([
    B("Rekomendasi: pertahankan \u201CPEMROSESAN SERVER\u201D."),
    " Arsitektur yang dikeraskan v16 memang berpusat di server: server Rust menelan telemetri CSI, mengorkestrasi WebSocket, menjalankan faster-whisper sebagai ASR cadangan, dan (dengan keputusan D3 di bawah) menjadi lokasi utama sintesis TTS; layanan awan hanya sumber ASR saat daring dan objek pembanding pada uji jalur ucapan. Akhiran \u201CCLOUD PROCESSING\u201D justru menyesatkan karena TTS tidak berjalan di awan dan sistem dinyatakan tetap berfungsi luring. Bila akhiran lama tetap dimaukan, seluruh Subbab 3.5 dan Tabel 3.1 harus ditulis ulang mengikuti awan \u2014 perubahan besar yang tidak diperlukan. Keputusan D1 dicatat pada Tabel 3.7 dan konsisten dengan Blok E-1.",
  ]));
  c.push(h2("5.2 Keputusan D3: lokasi sintesis dan pemutaran TTS"));
  c.push(p([
    B("Rekomendasi: TTS disintesis di server lokal dan audio dialirkan ke speaker node penerima"),
    " (D3). Alasannya: speaker dengan DAC I2S memang terpasang pada node penerima (Tabel 3.1 no. 4), purwarupa berdiri sendiri tanpa mengharuskan ponsel berada di dekat pengguna, dan pembagian ini mengembalikan peran laptop/server sebagai pusat pemrosesan teks dan TTS sebagaimana rancangan sebelumnya yang dirujuk evaluasi. TTS on-device di ponsel (Kokoro ONNX dalam Tauri) tetap dipertahankan sebagai jalur cadangan kedua agar cerita luring v16 tidak hilang: internet terputus tidak mengganggu apa pun (server lokal bekerja), sedangkan server laptop yang mati memindahkan TTS ke ponsel dengan keterbatasan yang dilaporkan. Keputusan mesin final tetap dinilai pada G3 sebagaimana Tabel 3.7 no. 17.",
  ]));
  c.push(h2("5.3 Pembagian kerja perangkat dan aliran data"));
  c.push(caption("Tabel 6  Pembagian kerja perangkat yang disatukan (jawaban atas lima pertanyaan evaluasi)"));
  c.push(tbl(null,
    ["Perangkat", "Fungsi tetap", "Jawaban atas pertanyaan evaluasi"],
    [
      ["Node RX (ESP32-S3 + layar, rotary, tombol, mic I2S, speaker I2S)", "Inferensi model arah 1 di perangkat; menangkap audio arah 2; memutar audio TTS; menampilkan huruf", "Audio mikrofon ditangkap di modul lalu dikirim ke server; ASR diproses di server/awan, bukan di modul"],
      ["Node TX (ESP32-S3)", "Memancarkan beacon ESP-NOW sebagai sumber bingkai CSI", "\u2014"],
      ["Laptop ASUS TUF", "Server Rust: penelan UDP CSI, orkestrasi WebSocket, ASR lokal (faster-whisper) cadangan, TTS lokal utama, dasbor Leptos; saat pelatihan: PyTorch", "Pusat pemrosesan teks dan TTS saat daring maupun luring \u2014 bukan sekadar cadangan"],
      ["Ponsel Poco F4 (Tauri)", "Klien antarmuka dua arah: teks, representasi SIBI, kontrol; TTS on-device cadangan; hotspot cadangan", "TTS utama tidak lagi di ponsel; speaker ponsel dipakai hanya sebagai cadangan"],
      ["Layanan awan", "ASR primer saat daring; pembanding mutu-latensi pada uji jalur ucapan", "Bukan pusat pemrosesan; pilihan final pada G3"],
      ["Access point", "Jangkar kanal dan jembatan jaringan", "\u2014"],
      ["Webcam", "Jalur guru pada akuisisi saja", "Tidak ada pada produk akhir"],
    ],
    [22, 40, 38], { centerHeader: false }));
  c.push(spacer());
  c.push(caption("Tabel 7  Aliran data kedua arah setelah disatukan"));
  c.push(tbl(null,
    ["Arah", "Rantai tahap (perangkat \u2192 perangkat)"],
    [
      ["Arah 1: SIBI \u2192 teks/suara", "CSI 56 subcarrier (Node RX) \u2192 fitur/adapter per jendela \u2192 model terkuantisasi di Node RX \u2192 label + skor (UDP) \u2192 server Rust \u2192 teks Indonesia \u2192 TTS server (Kokoro; cadangan MMS-TTS-ind) \u2192 aliran audio \u2192 speaker Node RX; teks tampil di layar Node RX dan aplikasi Tauri"],
      ["Arah 2: ucapan \u2192 SIBI", "Tombol tekan-untuk-bicara \u2192 mikrofon INMP441 (Node RX) \u2192 aliran audio (UDP) \u2192 server Rust \u2192 ASR awan primer saat daring, faster-whisper lokal cadangan \u2192 teks \u2192 kamus teks\u2192isyarat \u2192 representasi SIBI (glos + gambar) \u2192 tampil di Tauri; indikator opsional di layar Node RX"],
      ["Fallback luring", "Internet terputus: ASR beralih ke faster-whisper dan TTS tetap di server lokal \u2014 kedua arah berjalan. Server laptop mati: TTS beralih ke on-device ponsel, ASR awan tidak tersedia \u2014 keterbatasan dilaporkan pada uji operasional"],
    ],
    [20, 80], { centerHeader: false }));
  c.push(spacer());

  c.push(h2("5.4 Blok teks siap sisip \u2014 audio dan arsitektur"));
  c.push(...block("BLOK E-1 \u2014 Ganti dua paragraf alur arah pada Subbab 3.5 (paragraf pertama dan kedua setelah Gambar 3.3)", [
    ["\u201CPada arah pertama, beacon ESP-NOW node pemancar melintasi zona isyarat, gerak pengisyarat mengubah deret CSI yang ditangkap node penerima, dan model berkepala klasifikasi yang terkuantisasi dijalankan langsung di modul menghasilkan label beserta skor keyakinan. Label dikirim melalui UDP ke server Rust sebagai telemetri, dipetakan menjadi teks Indonesia, lalu teks itu tampil di layar modul dan aplikasi Tauri sekaligus disintesis mesin TTS di server lokal; audio hasil sintesis dialirkan kembali ke modul dan diputar pada speaker DAC I2S. Bila aliran audio ke modul tidak stabil atau server tidak tersedia, sintesis beralih ke mesin on-device pada ponsel dan pemutaran memakai speaker ponsel; peralihan itu dicatat.\u201D"],
    ["\u201CPada arah kedua, tombol tekan-untuk-bicara mengaktifkan mikrofon I2S pada node penerima; audio ditangkap di modul lalu dialirkan ke server Rust, yang meneruskannya ke layanan ASR awan saat daring atau memprosesnya sendiri dengan faster-whisper. Teks hasil pengenalan dipetakan ke representasi SIBI dari aset modul dan tampil pada aplikasi Tauri, dengan indikator opsional di layar modul. Saat internet terputus, kedua arah tetap berjalan karena ASR dan TTS beralih ke server lokal; kebutuhan pemrosesan audio di node penerima sebatas penangkapan dan pengaliran, bukan pengenalan.\u201D"],
  ]));
  c.push(...block("BLOK E-2 \u2014 Perbarui tiga baris Tabel 3.1", [
    ["Baris 4 (pengeras suara + DAC I2S) \u2014 keterangan diganti: \u201CPemutaran suara TTS hasil sintesis server yang dialirkan ke modul (keputusan D3 pada Tabel 3.7); speaker ponsel sebagai cadangan\u201D."],
    ["Baris 7 (laptop ASUS TUF) \u2014 keterangan diganti: \u201CServer Rust (penelan CSI, orkestrasi, ASR lokal cadangan, TTS lokal utama, dasbor); akuisisi jalur guru; pelatihan dua kepala; evaluasi\u201D."],
    ["Baris 8 (ponsel Poco F4) \u2014 keterangan diganti: \u201CKlien Tauri (tampilan teks dan representasi SIBI), mesin TTS on-device sebagai cadangan, hotspot cadangan\u201D."],
  ]));
  c.push(...block("BLOK E-3 \u2014 Ganti Batasan no. 6 (Subbab 1.4) dan selaraskan Subbab 2.11", [
    ["\u201CSintesis ucapan utama berjalan di server lokal dan audio diputar pada speaker node penerima, dengan mesin on-device pada ponsel sebagai cadangan; pengenalan ucapan memakai layanan awan dengan faster-whisper lokal sebagai cadangan. Pilihan final mesin dan layanan tetap ditetapkan pada gerbang G3.\u201D"],
    ["Kalimat penyelarasan Subbab 2.11: \u201CDengan keputusan D3, Kokoro-82M ONNX diposisikan pada dua lokasi: server lokal sebagai jalur utama dan ponsel sebagai jalur cadangan; keduanya memakai prasyarat suara Indonesia yang sama dan diverifikasi pada G3.\u201D"],
  ]));
  c.push(...block("BLOK E-4 \u2014 Tambahkan kalimat pada Subbab 2.13", [
    ["\u201CServer lokal pada laptop menjalankan server RuView, server Rust, faster-whisper, serta TTS Kokoro/MMS sebagai jalur utama luring, sehingga pemrosesan teks dan suara tetap berjalan tanpa internet; server Rust bukan sekadar perantara, melainkan titik orkestrasi kedua arah penerjemahan.\u201D"],
  ]));

  // ================= BAGIAN 6 =================
  c.push(h1("6. Finalisasi Parameter, Ambang, dan Temuan Tambahan (Langkah 6)"));
  c.push(p([
    "Delapan temuan tambahan evaluasi ditindaklanjuti satu per satu pada Tabel 8, lalu empat di antaranya \u2014 definisi Delta-CSI, beban perekaman, gerbang G1, dan definisi target TTS \u2014 dituangkan menjadi blok teks. Temuan tentang regresi temporal (T dan padding) sudah ditutup pada Bagian 3 (Blok C-3), dan temuan MPJPE sudah ditutup pada Bagian 4 (Blok D-3).",
  ]));
  c.push(caption("Tabel 8  Delapan temuan tambahan dan perbaikannya"));
  c.push(tbl(null,
    ["Temuan evaluasi", "Perbaikan", "Blok"],
    [
      ["Persamaan \u0394-CSI menyebut amplitudo, rumus memakai selisih koefisien kompleks", "Definisi diselaraskan ke koefisien kompleks; varian amplitudo-saja dilaporkan berdampingan", "F-1"],
      ["Panjang T dan strategi padding/resampling belum ditentukan", "T = 16 langkah; padding + mask; resampling ditolak untuk J/Z", "C-3"],
      ["Dataset 3\u20134 pengisyarat \u2014 klaim generalisasi harus dibatasi", "Batas klaim eksplisit pada Subbab 1.4 dan 3.8", "F-2"],
      ["30 repetisi per huruf per sesi \u2014 beban perekaman belum dihitung", "Hitungan beban lengkap + mitigasi kelelahan pada protokol", "F-3"],
      ["Gerbang G1 hanya akurasi \u2265 50% \u2014 terlalu lemah", "Ditambah F1 makro dan recall per kelas; J/Z dilaporkan terpisah", "F-4"],
      ["Target TTS di bawah 100 ms ambigu", "Didefinisikan sebagai waktu menuju audio pertama (TTFA)", "F-5"],
      ["MPJPE tanpa ambang kelayakan", "Menjadi metrik pemantauan pada Pilihan 1; ambang hanya bila Pilihan 2", "D-3"],
      ["Uji pengguna 3\u20135 orang", "Diframing sebagai uji kelayakan skala kecil, bukan bukti populasi", "F-6"],
    ],
    [40, 46, 14], { centerHeader: false }));
  c.push(spacer());

  c.push(h2("6.1 Beban perekaman dan mitigasi kelelahan"));
  c.push(p([
    "Perhitungan berikut memakai angka v16 apa adanya (26 huruf, 30 repetisi, sedikitnya dua sesi per pengisyarat, 3\u20134 pengisyarat) dan asumsi durasi yang dinyatakan terbuka pada protokol: satu repetisi memakan sekitar lima detik (peragaan dua detik ditahan atau dilintaskan, ditambah jeda tiga detik). Hasilnya dirangkum Tabel 9: satu sesi memakan sekitar 97 menit termasuk jeda blok, kalibrasi, dan persiapan, sehingga seluruh program perekaman memakan sekitar 10\u201313 jam waktu dinding untuk 4.680\u20136.240 segmen. Angka ini layak dan realistis untuk studi kelayakan, tetapi hanya bila kelelahan dikelola; oleh karena itu mitigasinya ditulis ke dalam protokol (Blok F-3), bukan dibiarkan implisit.",
  ]));
  c.push(caption("Tabel 9  Hitungan beban perekaman dataset"));
  c.push(tbl(null,
    ["Parameter", "Nilai"],
    [
      ["Huruf per sesi", "26 (24 statis + J + Z)"],
      ["Repetisi per huruf per sesi", "\u00B130 (sesuai Subbab 3.6)"],
      ["Repetisi per sesi per pengisyarat", "\u00B1780"],
      ["Durasi per repetisi (asumsi protokol: 2 s peragaan + 3 s jeda)", "5 detik"],
      ["Waktu perekaman murni per sesi", "\u00B165 menit"],
      ["Jeda blok (blok \u00B110 menit, jeda 3 menit, 6 jeda)", "+18 menit"],
      ["Kalibrasi ruang 600 bingkai + persiapan dan pencatatan", "+14 menit"],
      ["Durasi sesi total", "\u00B197 menit (\u2248 1,6 jam)"],
      ["Sesi per pengisyarat (minimum, sesuai v16)", "2 sesi \u2192 \u00B13,2 jam"],
      ["Total 3\u20134 pengisyarat", "\u00B110\u201313 jam waktu dinding; perekaman murni \u00B16,5\u20138,7 jam; total segmen \u00B14.680\u20136.240"],
    ],
    [58, 42], { centerHeader: false }));
  c.push(spacer());

  c.push(h2("6.2 Usulan penguatan gerbang G1"));
  c.push(p([
    "Akurasi dalam sesi \u2265 50% tetap dipertahankan sebagai lantai kelayakan \u2014 ia sekitar 13 kali peluang acak dan berperan sebagai gerbang hidup-mati jalur CSI \u2014 tetapi tidak lagi menjadi satu-satunya ukuran. Tiga dimensi ditambahkan agar \u201Clolos\u201D tidak bisa dicapai dengan model yang mengabaikan sebagian huruf, dan hasil J/Z diwajibkan terpisah agar huruf gerak tidak tertutupi rata-rata. Seluruh angka tambahan berstatus usulan yang difinalkan bersama pembimbing.",
  ]));
  c.push(caption("Tabel 10  Kriteria G1 yang diperkuat (usulan)"));
  c.push(tbl(null,
    ["Dimensi", "Kriteria usulan", "Status"],
    [
      ["Akurasi dalam sesi", "\u2265 50% (\u2248 13\u00D7 peluang acak 3,8%)", "Sudah ada di v16; dipertahankan"],
      ["F1 makro", "\u2265 0,45", "[Usulan \u2014 difinalkan bersama pembimbing]"],
      ["Recall per kelas", "Tidak ada kelas dengan recall = 0 pada himpunan huruf terpilih; pasangan paling mirip dilaporkan", "[Usulan]"],
      ["Perbandingan ablasi", "Melampaui pembanding kepala tunggal; manfaat multitugas dilaporkan", "Sudah ada di v16; dipertahankan"],
      ["Huruf J dan Z", "Recall J dan recall Z dilaporkan terpisah beserta confusion terhadap huruf paling mirip; galat lintasan bila Pilihan 2", "[Usulan \u2014 wajib dilaporkan]"],
      ["Inferensi terkuantisasi", "Di bawah 100 ms", "Sudah ada di v16; dipertahankan"],
      ["MPJPE", "Dilaporkan sebagai pemantauan (Blok D-3)", "Sejalan dengan Pilihan 1"],
    ],
    [22, 50, 28], { centerHeader: false }));
  c.push(spacer());

  c.push(h2("6.3 Blok teks siap sisip \u2014 temuan tambahan"));
  c.push(...block("BLOK F-1 \u2014 Perbaiki definisi Delta-CSI pada Subbab 3.7 (kalimat pengantar Persamaan 3.1)", [
    ["\u201CDeret CSI dipotong menjadi segmen huruf dengan segmentasi energi gerak memakai Delta-CSI, yaitu rata-rata besar perubahan koefisien kanal kompleks antarbingkai pada seluruh 56 subcarrier: d(t) = (1/56) \u00B7 \u03A3", { t: "n", sub: true, i: true }, " | h", { t: "n", sub: true, i: true }, "(t) \u2212 h", { t: "n", sub: true, i: true }, "(t \u2212 1) |. Kata \u2018amplitudo\u2019 pada rumusan lama diganti \u2018koefisien kanal kompleks\u2019 agar definisi dan rumusnya identik. Sebagai pembanding sensitivitas pada uji Delta-CSI (Subbab 3.8.1), varian berbasis amplitudo saja, d", { t: "|H|", sub: true, i: true }, "(t) = (1/56) \u00B7 \u03A3", { t: "n", sub: true, i: true }, " ||h", { t: "n", sub: true, i: true }, "(t)| \u2212 |h", { t: "n", sub: true, i: true }, "(t \u2212 1)||, dihitung dan dilaporkan berdampingan.\u201D"],
  ]));
  c.push(...block("BLOK F-2 \u2014 Tambahkan kalimat batas klaim pada Subbab 1.4 (setelah Batasan no. 8) dan Subbab 3.8", [
    ["\u201CSeluruh hasil klasifikasi, regresi, dan operasional dilaporkan sebagai bukti awal pada populasi terbatas: 3\u20134 pengisyarat, sedikitnya dua ruang, dan satu konfigurasi perangkat. Skema leave-one-subject-out, pengguna baru, dan leave-one-room-out dibaca sebagai indikasi ketahanan awal, bukan bukti generalisasi populasi; klaim lintas populasi tidak dibuat.\u201D"],
  ]));
  c.push(...block("BLOK F-3 \u2014 Tambahkan paragraf beban perekaman pada Subbab 3.6 (setelah langkah protokol nomor 5)", [
    ["\u201CBeban perekaman dihitung agar protokolnya realistis dan etis. Dengan 26 huruf dan kurang lebih 30 repetisi, satu sesi memuat sekitar 780 repetisi; pada asumsi lima detik per repetisi, perekaman murninya sekitar 65 menit, dan dengan jeda blok, kalibrasi, serta persiapan, satu sesi memakan waktu sekitar 97 menit. Setiap sesi dibagi blok sekitar sepuluh menit dengan jeda wajib minimal tiga menit di antaranya; maksimal dua sesi per hari untuk satu pengisyarat; pengisyarat boleh menghentikan repetisi kapan saja tanpa konsekuensi. Tingkat kelelahan diamati dari penurunan mutu segmen pada blok akhir dan dilaporkan bersama tingkat segmen terbuang.\u201D"],
  ]));
  c.push(...block("BLOK F-4 \u2014 Perbarui kriteria G1 pada Tabel 3.5", [
    ["\u201CKriteria G1 dilengkapi menjadi: akurasi dalam sesi sekurang-kurangnya 50% (sekitar 13 kali acak 3,8%) DAN F1 makro sekurang-kurangnya 0,45 [usulan] DAN tidak ada kelas dengan recall 0 pada himpunan huruf terpilih DAN melampaui pembanding ablasi kepala tunggal; manfaat multitugas dilaporkan dari ablasi; recall J dan recall Z dilaporkan terpisah beserta confusion terhadap huruf paling mirip; MPJPE dilaporkan sebagai pemantauan; inferensi terkuantisasi di bawah 100 ms. Seluruh ambang difinalkan bersama pembimbing sebelum G1 dinilai.\u201D"],
  ]));
  c.push(...block("BLOK F-5 \u2014 Definisikan target TTS pada Subbab 3.5 dan baris G3 Tabel 3.5", [
    ["\u201CTarget \u2018TTS di bawah 100 ms\u2019 didefinisikan sebagai waktu menuju audio pertama (time-to-first-audio, TTFA): diukur dari pemanggilan sintesis hingga sampel audio pertama tersedia untuk diputar, pada frasa uji pendek paling banyak lima kata. Durasi sintesis keseluruhan dilaporkan terpisah. Definisi yang sama dipakai pada Subbab 3.5, baris G3 Tabel 3.5, dan instrumen uji jalur ucapan Subbab 3.8.4.\u201D"],
  ]));
  c.push(...block("BLOK F-6 \u2014 Tambahkan kalimat framing pada awal Subbab 3.8.5", [
    ["\u201CUji kegunaan bersama 3\u20135 pengguna diposisikan sebagai uji kelayakan skala kecil: hasilnya dianalisis secara deskriptif untuk menemukan hambatan pemakaian dan mengarahkan perbaikan purwarupa, bukan sebagai bukti efektivitas pada populasi pengguna; rumusan ini selaras dengan Batasan no. 9.\u201D"],
  ]));

  // ================= BAGIAN 7 =================
  c.push(h1("7. Halaman Administratif dan Etik"));
  c.push(p([
    "Sesuai urutan evaluasi, administrasi dituntaskan setelah substansi terkunci. Checklist Tabel 11 memuat seluruh butir administratif yang disebut evaluasi beserta lokasinya di v16; tidak ada butir yang boleh dibiarkan kosong saat proposal dicetak. Penanda [PERLU DATA] dan [PERLU VALIDASI] yang tersebar di v16 sebaiknya diinventarisasi sekali lagi setelah blok teks Bagian 1\u20136 disisipkan, karena sebagian penanda \u2014 bentuk masukan encoder, rancangan adapter, panjang jendela T, keputusan deployment, dan pemutaran TTS \u2014 justru tertutup oleh dokumen ini.",
  ]));
  c.push(caption("Tabel 11  Checklist administratif dan etik"));
  c.push(tbl(null,
    ["Butir", "Lokasi di v16", "Tindakan"],
    [
      ["Nama penulis, NIM, program studi, universitas, pembimbing", "Halaman sampul", "Isi seluruh placeholder sebelum cetak"],
      ["Tanggal dan bulan pelaksanaan penelitian", "Subbab 3.3", "Isi [PERLU DATA] saat jadwal disetujui"],
      ["Lembaga/komisi pemberi persetujuan etik", "Subbab 3.6", "Tetapkan lembaga; siapkan formulir persetujuan dan protokol etik"],
      ["Keputusan D1: akhiran judul", "Sampul", "Konfirmasi sesuai Subbab 5.1; catat pada Tabel 3.7"],
      ["Keputusan D2: model deployment", "Subbab 3.7, Tabel 3.7", "Catat Pilihan 1/2 beserta dasarnya (Blok D-1, D-3)"],
      ["Keputusan D3: pemutaran TTS", "Tabel 3.1, Subbab 3.5", "Catat sesuai Subbab 5.2 (Blok E-1, E-2)"],
      ["Finalisasi ambang seluruh gerbang", "Tabel 3.7 no. 1, Tabel 3.5", "Rapat finalisasi bersama pembimbing sebelum gerbang dinilai"],
      ["Verifikasi kelas J/Z pada model guru", "Subbab 2.9", "Periksa konfigurasi kelas model juara WPC (Blok B-1)"],
      ["Parameter normalisasi checkpoint", "Subbab 2.4, 3.7", "Cari pada artefak checkpoint saat audit T0 (Tabel 1)"],
    ],
    [34, 24, 42], { centerHeader: false }));

  // ================= BAGIAN 8 =================
  c.push(h1("8. Peta Sisipan v16 \u2192 v17"));
  c.push(p([
    "Tabel 12 memetakan seluruh perubahan ke lokasinya di v16 beserta prioritasnya. Urutan pengerjaannya mengikuti enam langkah evaluasi: langkah 1 mencakup butir 3\u20135 dan 10; langkah 2 butir 6; langkah 3 butir 7\u20139 dan 13; langkah 4 butir 12; langkah 5 butir 2, 11, 14, dan 15; langkah 6 butir 16\u201319; administrasi menutup dengan butir 20. Blok teks disalin apa adanya ke lokasi yang disebut; kalimat penghubung lokal boleh disesuaikan asalkan makna blok tidak berubah.",
  ]));
  c.push(caption("Tabel 12  Peta sisipan lengkap"));
  c.push(tbl(null,
    ["No", "Lokasi di v16", "Aksi", "Blok/bagian", "Prioritas"],
    [
      ["1", "Judul sampul", "Keputusan D1", "Bagian 5.1", "Sedang"],
      ["2", "Sampul dan administrasi", "Isi checklist", "Bagian 7", "Terakhir"],
      ["3", "Subbab 2.4, kalimat terakhir paragraf pertama", "Ganti", "A-1", "Tinggi"],
      ["4", "Subbab 2.4, setelah daftar delapan fitur", "Tambah paragraf", "A-2", "Tinggi"],
      ["5", "Subbab 2.4, Tabel 2.2 baris masukan", "Perbarui sel masukan", "Tabel 1 dokumen ini", "Tinggi"],
      ["6", "Subbab 2.9", "Tambah paragraf + kalimat", "B-1, B-2", "Tinggi"],
      ["7", "Subbab 2.7\u20132.8, paragraf modul temporal", "Ganti", "C-2", "Tinggi"],
      ["8", "Persamaan 2.15 dan kalimat pengantarnya", "Ganti", "C-1", "Tinggi"],
      ["9", "Subbab 2.7 atau 3.7, panjang urutan", "Tambah paragraf", "C-3", "Tinggi"],
      ["10", "Subbab 3.7, \u201Cencoder diterapkan pada tiap bingkai\u201D", "Ganti + tambah", "A-3, A-4", "Tinggi"],
      ["11", "Subbab 3.5, dua paragraf alur arah", "Ganti", "E-1", "Tinggi"],
      ["12", "Subbab 3.7, paragraf deployment dan Gambar 3.5", "Ganti + sesuaikan", "D-1, D-2", "Tinggi"],
      ["13", "Subbab 3.7, penyelarasan supervisi", "Tambah paragraf", "C-4, B-3", "Sedang"],
      ["14", "Tabel 3.1, baris 4, 7, 8", "Perbarui keterangan", "E-2", "Tinggi"],
      ["15", "Subbab 2.11, 2.13, dan Batasan no. 6", "Selaraskan", "E-3, E-4", "Sedang"],
      ["16", "Subbab 3.7, Persamaan 3.1", "Perbaiki definisi", "F-1", "Sedang"],
      ["17", "Subbab 3.6", "Tambah beban perekaman", "F-3", "Sedang"],
      ["18", "Tabel 3.5, kriteria G0, G1, G3", "Tambah/perbarui", "A-5, F-4, F-5", "Tinggi"],
      ["19", "Subbab 1.4 dan 3.8", "Tambah batas klaim", "F-2", "Sedang"],
      ["20", "Subbab 3.8.5", "Tambah framing uji kegunaan", "F-6", "Rendah"],
    ],
    [7, 34, 21, 22, 16], { centerHeader: false }));

  // ================= BAGIAN 9 =================
  c.push(h1("9. Batasan Klaim yang Dipertahankan"));
  c.push(p([
    "Revisi aditif hanya aman bila pagar klaim v16 tidak ikut bergeser saat menyisipkan teks baru. Delapan pagar berikut dipertahankan apa adanya; bila sebuah blok teks tampak menyentuh salah satunya, blok itu yang disesuaikan, bukan pagarnya.",
  ]));
  c.push(bullet([B("Encoder beku tetap baseline."), " LoRA dan pelatihan lanjutan tetap pembanding yang dijalankan berdampingan, bukan keputusan awal."]));
  c.push(bullet([B("YOLO26m-Pose tetap guru visual"), " yang hanya aktif pada akuisisi dan pelatihan; produk akhir bebas kamera dan bebas citra."]));
  c.push(bullet([B("1D-CNN tetap kandidat modul temporal"), " yang keputusannya diambil dari ablasi pada data yang sama, bukan dari preferensi implementasi."]));
  c.push(bullet([B("Model MM-Fi tetap pembanding, bukan komponen."), " Checkpoint wifi-densepose-mmfi-pose (17 keypoint COCO) tidak menjadi bagian murid; skema 21 keypoint tetap mengikuti MediaPipe Hands."]));
  c.push(bullet([B("ADR tetap berstatus Proposed."), " ADR-024, ADR-146, dan ADR-150 adalah rancangan yang belum diimplementasikan; angka estimasinya selalu dilabeli estimasi rancangan."]));
  c.push(bullet([B("Tidak ada hasil eksperimen yang diklaim."), " Seluruh angka target tetap berstatus target rancangan yang diukur pada gerbang; hasil exp11_huruf24 tetap dikutip sebagai hasil visual pada data visual."]));
  c.push(bullet([B("Keputusan terbuka diputuskan data."), " Jalur fitur turunan atau adapter, modul temporal final, skema adaptasi, Pilihan 1/2, serta mesin TTS/ASR final diputuskan pada gerbang dan dicatat pada Tabel 3.7."]));
  c.push(bullet([B("Ruang lingkup tidak meluas."), " 24 huruf statis + J/Z, alfabet manual, satu pengisyarat per sesi; bukan penerjemah kalimat; BISINDO dan isyarat kontinu tetap di luar lingkup."]));
  c.push(p([
    "Dengan delapan pagar itu, seluruh blok A-1 sampai F-6 dapat disisipkan tanpa mengubah identitas proposal: penelitian tetap studi kelayakan purwarupa penerjemah dua arah huruf SIBI berbasis Wi-Fi CSI dengan inferensi di ESP32-S3 dan pemrosesan di server \u2014 kini dengan kontrak input yang terkunci, supervisi yang terpisah rapi, matematika yang konsisten, dan arsitektur audio yang satu suara.",
  ], { spacing: { before: 160 } }));

  return c;
}

module.exports = { build };
