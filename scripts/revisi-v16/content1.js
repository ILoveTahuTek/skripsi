// content1.js — Ringkasan Eksekutif + Bagian 1 (Kontrak Input Encoder RuView)
const { B, I, SUB, V, h1, h2, p, caption, note, block, spacer, tbl } = require("./helpers");

function build() {
  const c = [];

  // ================= RINGKASAN EKSEKUTIF =================
  c.push(h1("Ringkasan Eksekutif"));
  c.push(p([
    "Dokumen ini menjawab evaluasi kritis atas Proposal Studi Kelayakan Purwarupa SenseSIBI versi 16 (49 halaman) dan menyiapkan revisi menuju v17. Penilaian evaluasi \u2014 kesesuaian visi 8,5 dari 10 dan kesiapan metodologi 6 dari 10 \u2014 menetapkan bahwa struktur, ruang lingkup, dan identitas sistem dua arah sudah benar, sementara lima kelompok masalah pada detail implementasi model dan integrasi perangkat harus dikunci sebelum proposal dipakai untuk seminar. Sesuai arahan evaluasi, seluruh perbaikan pada dokumen ini bersifat ",
    B("aditif dan terarah"),
    ": tidak ada bab yang ditulis ulang dan tidak ada keputusan arsitektur yang diputar balik; yang dilakukan ialah mengunci definisi yang masih terbuka, memisahkan supervisi yang tercampur, dan menyelaraskan pernyataan yang saling bertentangan.",
  ]));
  c.push(p([
    "Titik paling kritis sesuai evaluasi ialah pertanyaan apakah representasi encoder RuView benar-benar dapat digunakan untuk mengenali detail alfabet SIBI \u2014 terutama gerakan J dan Z \u2014 dengan input CSI yang tersedia. Audit ulang kartu model checkpoint ",
    V("ruvnet/wifi-densepose-pretrained"),
    " mempertegas urgensi itu. Delapan fitur masukan encoder terdiri atas kehadiran, gerak, napas, detak jantung, varians fase, jumlah orang, deteksi jatuh, dan RSSI. Empat di antaranya \u2014 napas, detak jantung, jumlah orang, dan deteksi jatuh \u2014 adalah fitur lingkungan atau fisiologis yang praktis tidak berubah selama artikulasi jari, dan pretraining dilakukan pada 60.630 sampel data ruangan selama delapan jam dengan supervisi sensor PIR, BME280, triangulasi RSSI, dan asimetri subcarrier [11], bukan pada gerak tangan. Kontrak masukan encoder karenanya adalah ",
    B("kontrak lingkungan, bukan kontrak artikulasi"),
    ". Konsekuensinya dituangkan pada Bagian 2: kompatibilitas representasi dijadikan gerbang eksperimen sungguh-sungguh (G0b) dengan protokol probe linear dan kriteria lulus yang diusulkan, bukan asumsi yang dinyatakan diam-diam.",
  ]));
  c.push(p([
    "Dokumen disusun mengikuti urutan pengerjaan enam langkah dari evaluasi: (1) kontrak input encoder RuView; (2) pemisahan supervisi 24 huruf statis dan J/Z; (3) persamaan optimasi dan arsitektur temporal; (4) keputusan model deployment; (5) arsitektur audio terpadu; serta (6) finalisasi parameter dan ambang, dilanjutkan halaman administratif dan etik. Setiap langkah memuat blok teks berlabel (A-1 sampai F-6) yang siap disisipkan ke lokasi tertentu di v16; seluruhnya dirangkum pada peta sisipan Bagian 8.",
  ]));
  c.push(p([
    "Tiga keputusan menunggu keputusan penulis dan diberi rekomendasi eksplisit: ",
    B("D1"),
    " \u2014 mempertahankan akhiran judul \u201CPEMROSESAN SERVER\u201D (rekomendasi: ya, karena pemrosesan berpusat di server; Bagian 5); ",
    B("D2"),
    " \u2014 model deployment Pilihan 1 sebagai baseline, yaitu multitugas saat pelatihan dan klasifikator saja saat deployment (Bagian 4); dan ",
    B("D3"),
    " \u2014 perangkat pemutar TTS (rekomendasi: speaker node penerima menerima aliran audio dari server, speaker ponsel sebagai cadangan; Bagian 5). Ketiganya dicatat sebagai parameter pada Tabel 3.7 v16 agar tidak diputuskan diam-diam oleh penulis.",
  ]));

  // ================= BAGIAN 1 =================
  c.push(h1("1. Kontrak Input Encoder RuView (Langkah 1)"));
  c.push(p([
    "Ini prioritas tertinggi evaluasi. v16 sudah mengidentifikasi ketidaksesuaian yang benar \u2014 checkpoint menerima delapan fitur turunan pada laju 1 Hz, sedangkan akuisisi menghasilkan 56 subcarrier pada sekitar 50 bingkai per detik [9], [11] \u2014 dan sudah menyiapkan dua jalur penyelesaian. Namun kontraknya belum didefinisikan secara presisi, sehingga kata \u201Cadapter\u201D berisiko menjadi istilah penutup alih-alih gerbang eksperimen. Subbab ini mengunci lima hal yang diminta evaluasi: bentuk tensor masukan, definisi dan normalisasi delapan fitur, hubungan laju input dengan deret CSI, pemeliharaan informasi temporal J/Z, dan eksperimen pengujian adapter.",
  ]));

  c.push(h2("1.1 Bentuk tensor masukan checkpoint"));
  c.push(p([
    "Dibaca dari kartu model, encoder menerima ",
    B("satu vektor delapan fitur per sampel"),
    " \u2014 bukan deret \u2014 dengan satu sampel mewakili ringkasan satu jendela satu detik; bentuk batch-nya (B, 8). Arsitekturnya dua lapis fully connected dengan BatchNorm dan GELU, keluaran embedding 128 dimensi ternormalisasi L2, total 9.280 parameter [11]. Karena encoder tidak menerima deret, urutan waktu hanya dapat hidup pada tingkat barisan sampel: satu segmen huruf menjadi barisan jendela, dan tiap jendela menghasilkan satu langkah embedding. Kontrak lengkapnya dirangkum Tabel 1; satu-satunya sel yang belum terjawab ialah parameter normalisasi masukan, yang harus ditemukan pada artefak checkpoint saat audit T0.",
  ]));
  c.push(caption("Tabel 1  Kontrak masukan checkpoint ruvnet/wifi-densepose-pretrained"));
  c.push(tbl(null,
    ["Butir kontrak", "Nilai yang tercatat", "Status"],
    [
      ["Bentuk masukan per sampel", "Vektor 8 fitur turunan CSI; bukan deret subcarrier", "Kartu model [11]; diverifikasi ulang saat memuat checkpoint pada T0"],
      ["Satuan waktu per sampel", "Satu jendela 1 detik pada laju 1 Hz", "Kartu model; hubungannya ke CSI 50 fps diatur Subbab 1.3"],
      ["Keluaran", "Embedding 128 dimensi, ternormalisasi L2", "Kartu model [11]"],
      ["Arsitektur", "2 lapis FC (BatchNorm + GELU), 9.280 parameter", "Kartu model [11]"],
      ["Normalisasi masukan", "Kartu model menyebut standardizer untuk varian kuantisasi 4-bit; parameter mean/std tidak dipublikasikan", "[PERLU VERIFIKASI: parameter normalisasi pada artefak checkpoint]"],
      ["Domain pretraining", "Kontrastif triplet + InfoNCE; 60.630 sampel, 8 jam; supervisi PIR, BME280, RSSI, asimetri subcarrier", "Kartu model [11]; domain bukan gerak tangan \u2014 lihat Subbab 1.2"],
    ],
    [26, 44, 30]));
  c.push(spacer());

  c.push(h2("1.2 Delapan fitur dan relevansinya bagi artikulasi jari"));
  c.push(p([
    "Evaluasi menuntut definisi delapan fitur, dan definisi itu menentukan segalanya. Tabel 2 mengutip makna tiap fitur dari kartu model lalu menilai relevansinya bagi tugas mengenali bentuk jari. Hasilnya tegas: ",
    B("empat dari delapan dimensi praktis tidak membawa informasi artikulasi"),
    " karena mengukur napas, detak jantung, jumlah orang, dan peristiwa jatuh; dua dimensi \u2014 gerak dan varians fase \u2014 membawa informasi gerak global tangan; sisanya marginal. Dengan kata lain, mengubah jendela CSI menjadi delapan angka tidak otomatis mempertahankan informasi artikulasi jari; sebagian besar kanal informasinya memang bukan untuk itu.",
  ]));
  c.push(caption("Tabel 2  Delapan fitur masukan encoder dan relevansinya bagi huruf SIBI"));
  c.push(tbl(null,
    ["Dim", "Fitur", "Makna menurut kartu model [11]", "Relevansi bagi artikulasi jari"],
    [
      ["0", "Kehadiran", "Besarnya gangguan sinyal Wi-Fi", "Sedang \u2014 berubah saat tangan memasuki zona isyarat"],
      ["1", "Gerak", "Laju perubahan sinyal (jalan > mengetik > diam)", "Tinggi \u2014 mencakup gerak tangan dan jari secara global"],
      ["2", "Napas", "Modulasi fase oleh gerak dada, 6\u201330 BPM", "Rendah \u2014 tidak membedakan bentuk huruf"],
      ["3", "Detak jantung", "Mikro-Doppler denyut darah, 40\u2013120 BPM", "Rendah \u2014 tidak membedakan bentuk huruf"],
      ["4", "Varians fase", "Kualitas sinyal; naik saat ada gerak", "Tinggi \u2014 mengikuti aktivitas gerak"],
      ["5", "Jumlah orang", "Klaster gerak independen (min-cut graph)", "Rendah \u2014 satu sesi hanya satu pengisyarat"],
      ["6", "Deteksi jatuh", "Akselerasi fase mendadak lalu diam", "Rendah \u2014 tidak terjadi selama pengisyaratan"],
      ["7", "RSSI", "Kekuatan sinyal, indikasi jarak", "Rendah\u2013sedang \u2014 konstan selama posisi tetap"],
    ],
    [7, 16, 42, 35], { centerHeader: false }));
  c.push(note("Tabel 2 memakai istilah kartu model; padanan yang dipakai v16 (kehadiran, gerak, napas, detak jantung, varians fase, jumlah orang, deteksi jatuh, RSSI) sama persis."));
  c.push(p([
    "Konsekuensinya dirumuskan sebagai hipotesis kerja ",
    B("H1"),
    ": pada jalur A (menghitung ulang delapan fitur turunan), masukan encoder berisiko hampir konstan antarhuruf, sehingga embedding beku dapat kehilangan pemisahan antar kelas SIBI. Jalur B (adapter masukan dari CSI mentah) menjadi kandidat utama karena menyimpan seluruh informasi 56 subcarrier sebelum ada peringkasan oleh rumus tetap. H1 tidak diasumsikan benar ataupun salah; ia diuji pada gerbang G0b (Subbab 1.5), dan keputusan jalurnya dicatat pada Tabel 3.7 v16.",
  ]));

  c.push(h2("1.3 Hubungan laju input checkpoint dengan deret CSI aktual"));
  c.push(p([
    "Untuk menghapus kebingungan istilah yang membuat Persamaan 2.11, Subbab 2.8, dan Subbab 3.7 saling bertabrakan, alur fitur dibakukan pada ",
    B("tiga tingkat"),
    ": (i) ",
    B("bingkai CSI"),
    " \u2014 satu pengukuran 56 subcarrier pada laju hingga 50 bingkai per detik (per 20 ms); (ii) ",
    B("jendela fitur"),
    " \u2014 kumpulan bingkai sepanjang W = 1 detik yang diringkas menjadi satu vektor delapan fitur, yakni satu sampel masukan encoder; dan (iii) ",
    B("langkah embedding"),
    " \u2014 satu keluaran encoder per jendela, yang barisannya menjadi masukan modul temporal; satu segmen berisi satu huruf. Pada jalur A, ringkasan per jendela memakai rumus fitur bawaan RuView; pada jalur B, adapter konvolusi satu dimensi memetakan jendela CSI mentah (56 \u00D7 50 nilai) ke vektor delapan dimensi sintetis per jendela, lalu encoder beku memprosesnya; tetapan adapter dilatih, sehingga \u03C6",
    SUB("adapter"),
    " masuk himpunan tetapan terlatih (Bagian 3).",
  ]));
  c.push(p([
    "Perbaikan kecil tetapi penting: Subbab 3.7 v16 menulis \u201Cencoder diterapkan pada tiap bingkai\u201D. Kalimat itu bertentangan dengan kontrak 1 Hz \u2014 pada kedua jalur, encoder diterapkan ",
    B("per jendela, bukan per bingkai"),
    ". Blok A-3 menggantinya.",
  ]));

  c.push(h2("1.4 Cara mempertahankan informasi temporal J dan Z"));
  c.push(p([
    "Resolusi 1 Hz pada satu jendela tunggal jelas tidak cukup untuk lintasan J dan Z. Solusinya jendela bergulir berlompatan: dengan lompatan H = 0,25 detik (usulan, dikalibrasi pada T2), satu segmen menghasilkan satu sampai sekitar tiga belas langkah embedding tergantung durasinya \u2014 segmen 1,0 detik memberi 1 langkah, 1,5 detik memberi 3, dan 2,0 detik memberi 5. Lintasan J/Z bertahan sebagai ",
    B("urutan langkah"),
    " yang diproses modul temporal secara berurutan; klasifikasi J/Z tidak pernah dibaca dari satu jendela tunggal. Pada laju empat langkah per detik, lintasan sekitar satu detik tersampel empat kali \u2014 kasar, tetapi cukup untuk membedakan lintasan J dan Z yang arah dan bentuknya berbeda; hal itu tetap diverifikasi pada probe J\u2013Z (Subbab 1.5) dan galat lintasan dilaporkan pada uji Subbab 3.8.2.",
  ]));

  c.push(h2("1.5 Gerbang G0b: kompatibilitas representasi sebagai eksperimen"));
  c.push(p([
    "Evaluasi meminta agar kompatibilitas adapter tidak dianggap otomatis. Gerbangnya dirancang sebagai ",
    B("G0b"),
    ", berjalan pada data pilot satu pengisyarat satu sesi (sekitar 1,6 jam, tanpa publikasi) yang direkam lebih dulu atau diambil dari sesi pertama T2. Protokolnya memakai probe linear di atas embedding beku \u2014 cara baku membaca seberapa informatif representasi tanpa melatih model penuh \u2014 disertai dua kontrol agar hasilnya tidak menipu. Kriteria lulusnya diusulkan pada Tabel 3 dan difinalkan bersama pembimbing sebelum gerbang dinilai, konsisten dengan Tabel 3.7 v16.",
  ]));
  c.push(caption("Tabel 3  Protokol gerbang G0b (audit kompatibilitas representasi)"));
  c.push(tbl(null,
    ["Langkah", "Prosedur", "Keluaran dan kriteria usulan"],
    [
      ["1", "Merekam sesi pilot 26 huruf: satu pengisyarat, satu sesi, protokol Subbab 3.6", "Data pilot tercatat dengan metadata sesi"],
      ["2", "Jalur A: menghitung delapan fitur per jendela 1 s, mengekstrak embedding beku, melatih probe linear 24 kelas dengan pembagian blok temporal", "F1 makro probe \u2265 0,30 dan \u2265 3\u00D7 peluang acak (\u2248 12,5% untuk 24 kelas) [usulan]"],
      ["3", "Probe sekuensial: menggabungkan langkah tiap segmen (rata-rata + maksimum) lalu memprobe 24 kelas", "Tidak lebih rendah nyata daripada probe per jendela; selisih dilaporkan"],
      ["4", "Probe biner J terhadap Z atas barisan langkah", "\u2265 70% [usulan]; dilaporkan bersama kontrol label-acak"],
      ["5", "Kontrol: probe linear pada fitur mentah ringkas sebagai pembanding; kontrol label-acak (p < 0,05)", "Batas bawah dan signifikansi ditetapkan"],
      ["6", "Keputusan jalur: A lulus \u2192 jalur A; A gagal tetapi jalur B (adapter) lulus uji lanjutan \u2192 adapter; keduanya gagal \u2192 skema LoRA/pelatihan lanjutan Subbab 3.7, dilaporkan sebagai temuan", "Keputusan dan buktinya dicatat pada Tabel 3.7"],
    ],
    [9, 52, 39], { centerHeader: false }));
  c.push(spacer(80));
  c.push(p([
    "Satu konsekuensi perlu dinyatakan sejak awal: bila kedua jalur gagal, itu bukan kegagalan penelitian. v16 sudah menyiapkan pembanding adaptasi (LoRA dan pelatihan lanjutan, Subbab 2.5 dan 3.7) serta cadangan risiko nomor 2 dan 3 pada Tabel 3.8. G0b hanya memastikan jalurnya dipilih berdasarkan bukti, dan hasil negatifnya tetap menjadi temuan yang dilaporkan.",
  ]));

  // ---------- Blok teks A ----------
  c.push(h2("1.6 Blok teks siap sisip \u2014 kontrak input"));
  c.push(...block("BLOK A-1 \u2014 Ganti kalimat terakhir paragraf pertama Subbab 2.4", [
    ["Teks lama: \u201CPada baseline penelitian ini, ",
      { t: "\u03B8", i: true }, { t: "0", sub: true, i: true },
      " dibekukan sehingga hanya tetapan kepala tugas yang diperbarui.\u201D"],
    ["Teks pengganti: \u201CPada baseline penelitian ini, ",
      { t: "\u03B8", i: true }, { t: "0", sub: true, i: true },
      " dibekukan; tetapan yang diperbarui mencakup adapter masukan (bila dipakai), modul temporal, dan kedua kepala tugas sebagaimana dirumuskan pada Persamaan 2.15. Kontrak masukan checkpoint diikat secara eksplisit: encoder menerima satu vektor delapan fitur turunan per jendela satu detik (bentuk batch (B, 8)), bukan deret subcarrier, dan menghasilkan satu embedding 128 dimensi ternormalisasi L2 per jendela. Deret waktu karenanya hidup pada tingkat barisan jendela, bukan di dalam encoder.\u201D"],
  ]));
  c.push(...block("BLOK A-2 \u2014 Tambahkan paragraf setelah daftar delapan fitur pada Subbab 2.4", [
    ["\u201CDelapan fitur itu perlu dibaca dengan jujur sebagai kontrak lingkungan, bukan kontrak artikulasi. Napas, detak jantung, jumlah orang, dan deteksi jatuh hampir tidak berubah selama artikulasi jari; informasi gerak tangan terkonsentrasi pada fitur gerak dan varians fase; pretraining dilakukan pada data ruangan semalaman dengan supervisi sensor PIR dan BME280 [11], bukan pada gerak tangan. Kelayakan representasi ini bagi huruf SIBI karena itu diperlakukan sebagai hipotesis yang diuji pada gerbang G0b (Subbab 3.7), bukan sebagai sifat yang menyertai checkpoint.\u201D"],
  ]));
  c.push(...block("BLOK A-3 \u2014 Ganti kalimat \u201CSetelah bentuk masukan pasti, encoder diterapkan pada tiap bingkai \u2026\u201D pada Subbab 3.7", [
    ["\u201CSetelah bentuk masukan pasti, alur fitur dibakukan pada tiga tingkat: bingkai CSI (56 subcarrier, hingga 50 bingkai per detik), jendela fitur sepanjang W = 1 detik yang diringkas menjadi satu vektor delapan fitur, dan langkah embedding \u2014 satu keluaran encoder per jendela. Jalur pertama menghitung ulang delapan fitur turunan bawaan RuView dari bingkai CSI; jalur kedua melatih adapter masukan kecil berbasis konvolusi satu dimensi yang memetakan jendela CSI mentah ke vektor masukan encoder, sehingga informasi subcarrier tidak diringkas lebih dulu oleh rumus tetap. Pada kedua jalur, encoder diterapkan per jendela \u2014 bukan per bingkai \u2014 sesuai kontrak laju 1 Hz kartu model [11].\u201D"],
  ]));
  c.push(...block("BLOK A-4 \u2014 Tambahkan paragraf setelah Blok A-3 pada Subbab 3.7", [
    ["\u201CResolusi temporal dijaga dengan jendela bergulir berlompatan H = 0,25 detik (usulan; dikalibrasi pada T2), sehingga satu segmen huruf menghasilkan satu sampai sekitar tiga belas langkah embedding tergantung durasinya. Untuk J dan Z, kelas tidak dibaca dari satu jendela: barisan langkah diproses modul temporal secara berurutan dan klasifikasinya diambil dari ringkasan barisan tersebut. Dengan itu lintasan gerak J dan Z tetap tersedia pada laju empat langkah per detik \u2014 cukup untuk lintasan sekitar satu detik \u2014 tanpa melanggar kontrak masukan encoder.\u201D"],
  ]));
  c.push(...block("BLOK A-5 \u2014 Tambahkan paragraf pada Subbab 3.7 dan satu klausul pada kriteria G0 (Tabel 3.5)", [
    ["\u201CKompatibilitas representasi diuji pada gerbang G0b dengan probe linear di atas embedding beku: probe 24 huruf statis pada skema blok temporal, probe sekuensial atas gabungan langkah, probe biner J terhadap Z, serta dua kontrol \u2014 probe pada fitur mentah dan kontrol label-acak. Ambang usulannya: F1 makro probe sekurang-kurangnya 0,30 dan sekurang-kurangnya tiga kali peluang acak; probe J\u2013Z sekurang-kurangnya 70 persen; seluruhnya difinalkan bersama pembimbing sebelum gerbang dinilai. Jalur fitur turunan dipakai bila lulus; bila gagal tetapi adapter lulus, adapter dipilih; bila keduanya gagal, encoder beku ditinggalkan menuju skema adaptasi pada Subbab 3.7 dan hasilnya dilaporkan sebagai temuan.\u201D"],
    ["Klausul tambahan pada kriteria G0 (Tabel 3.5): \u201Cprobe G0b memenuhi ambang pada salah satu jalur masukan, dan keputusan jalurnya tercatat\u201D."],
  ]));

  return c;
}

module.exports = { build };
