#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Revisi terarah v16 -> v17 (gelombang 17): kontrak input, supervisi, persamaan,
deployment, audio, parameter. Mengikuti Dokumen-Revisi-Terarah-SenseSIBI-v16-ke-v17
(blok A-1 s.d. F-6) + keputusan D1/D2/D3 + penyelarasan konsistensi.
Kaidah bahasa: skill sempro-mepet (register baku; 'jika' bukan 'bila'; tanpa em dash prosa)."""
from pathlib import Path

SRC = Path("/home/z/my-project/download/sensesibi-v10/Proposal-SenseSIBI-v16.md")
DST = Path("/home/z/my-project/download/sensesibi-v10/Proposal-SenseSIBI-v17.md")
s = SRC.read_text(encoding="utf-8")

edits = []

def E(old, new, n=1, label=""):
    edits.append((old, new, n, label))

# ============ D1: akhiran judul disatukan ke PEMROSESAN SERVER ============
E("# STUDI KELAYAKAN PURWARUPA SenseSIBI: SISTEM PENERJEMAHAN DUA ARAH HURUF SIBI BERBASIS WI-FI CSI DENGAN INFERENSI ESP32-S3 DAN CLOUD PROCESSING",
  "# STUDI KELAYAKAN PURWARUPA SenseSIBI: SISTEM PENERJEMAHAN DUA ARAH HURUF SIBI BERBASIS WI-FI CSI DENGAN INFERENSI ESP32-S3 DAN PEMROSESAN SERVER",
  1, "D1 judul H1")
E("| Judul | STUDI KELAYAKAN PURWARUPA SenseSIBI: SISTEM PENERJEMAHAN DUA ARAH HURUF SIBI BERBASIS WI-FI CSI DENGAN INFERENSI ESP32-S3 DAN CLOUD PROCESSING |",
  "| Judul | STUDI KELAYAKAN PURWARUPA SenseSIBI: SISTEM PENERJEMAHAN DUA ARAH HURUF SIBI BERBASIS WI-FI CSI DENGAN INFERENSI ESP32-S3 DAN PEMROSESAN SERVER |",
  1, "D1 judul tabel identitas")
E("| Jenis dokumen | Proposal penelitian (seminar proposal), BAB I sampai III + Daftar Pustaka; revisi additif: ruang lingkup sistem dua arah dipertahankan, blok model jalur isyarat menjadi teks diperbarui menjadi encoder CSI terpralatih dengan dua kepala tugas; 49 halaman (tambahan isi brief v2 menaikkan halaman dari 40 pada v15) |",
  "| Jenis dokumen | Proposal penelitian (seminar proposal), BAB I sampai III + Daftar Pustaka; revisi terarah dan aditif atas v16: kontrak masukan *encoder* dikunci, supervisi 24 huruf statis dan J/Z dipisahkan, persamaan pembaruan tetapan disatukan, *deployment* mengikuti Pilihan 1, arsitektur audio disatukan, kriteria gerbang diperkuat; {{HALAMAN}} halaman (naik dari 49 pada v16) |",
  1, "jenis dokumen (halaman diisi setelah build)")

E("> Catatan penyusunan: versi ini menyunting naskah v15 sebagai revisi additif. Ruang lingkup sistem tidak berubah: purwarupa penerjemah dua arah dengan inferensi ESP32-S3 dan pemrosesan awan tetap menjadi objek, demikian pula mesin ucapan, pengenalan ucapan, kamus representasi, server dan cadangannya, gerbang keputusan G0 sampai G4, serta seluruh uji kelayakan. Yang berubah hanya blok model pada jalur isyarat menjadi teks: *backbone* WiFi-DensePose berkepala tunggal 1D-CNN diganti menjadi *encoder* CSI terpralatih RuView yang dibekukan dengan dua kepala tugas, yaitu kepala klasifikasi 26 huruf dan kepala regresi 21 *keypoint* tangan, di bawah supervisi guru visual YOLO26m-Pose. Persamaan bernomor bertambah dari 18 menjadi 29; gambar menjadi tujuh dengan satu diagram blok model baru; tabel menjadi dua belas; daftar pustaka menjadi 28 entri. Penanda [PERLU DATA] kini ditemani [PERLU VALIDASI] untuk hal yang baru dapat ditetapkan setelah audit *checkpoint*. Konteks Jawa Timur tanpa mitra lembaga dipertahankan; rincian perubahan per subbab ada pada Log Perubahan gelombang 16 di ujung naskah.",
  "> Catatan penyusunan: versi ini menyunting naskah v16 sebagai revisi terarah dan aditif atas evaluasi kritis; tidak ada bab yang ditulis ulang dan ruang lingkup sistem tidak berubah. Kontrak masukan *encoder* dikunci menjadi delapan fitur turunan per jendela satu detik dan diuji gerbang G0b; supervisi 24 huruf statis dipisahkan dari huruf gerak J dan Z; himpunan tetapan terlatih dirumuskan utuh pada Persamaan 2.15′ dengan modul temporal dua cabang; *deployment* mengikuti Pilihan 1 (kepala klasifikasi saja, kepala regresi sebagai supervisi tambahan); arsitektur audio disatukan dengan sintesis TTS di server lokal sebagai jalur utama (keputusan D3); kriteria gerbang G1 diperkuat; beban perekaman dihitung ke dalam protokol. Tiga keputusan terbuka, yaitu akhiran judul, model *deployment*, dan lokasi TTS, dicatat pada Tabel 3.7. Penanda [PERLU DATA] dan [PERLU VALIDASI] tetap menandai hal yang belum dapat ditetapkan; rincian perubahan per subbab ada pada Log Perubahan gelombang 17 di ujung naskah.",
  1, "catatan penyusunan")

# ============ LANGKAH 1: kontrak input encoder ============
E("Pada baseline penelitian ini, θ~0~ dibekukan sehingga hanya tetapan kepala tugas yang diperbarui.",
  "Pada baseline penelitian ini, θ~0~ dibekukan; tetapan yang diperbarui mencakup adapter masukan (jika dipakai), modul temporal, dan kedua kepala tugas sebagaimana dirumuskan pada Persamaan 2.15′. Kontrak masukan *checkpoint* diikat secara eksplisit: *encoder* menerima satu vektor delapan fitur turunan per jendela satu detik (bentuk *batch* (B, 8)), bukan deret *subcarrier*, dan menghasilkan satu *embedding* 128 dimensi ternormalisasi L2 per jendela. Deret waktu karenanya hidup pada tingkat barisan jendela, bukan di dalam *encoder*. Parameter normalisasi masukan belum dipublikasikan kartu modelnya sehingga dicari pada artefak *checkpoint* saat audit T0 [PERLU VALIDASI: parameter normalisasi masukan pada artefak checkpoint].",
  1, "A-1 kontrak input 2.4")

E("Keduanya dinyatakan terbuka dengan penanda [PERLU VALIDASI] sampai audit selesai, dan riset ini tidak mengklaim kompatibilitas sebelum terverifikasi.",
  "Keduanya dinyatakan terbuka dengan penanda [PERLU VALIDASI] sampai audit selesai, dan riset ini tidak mengklaim kompatibilitas sebelum terverifikasi.\n\nDelapan fitur itu perlu dibaca dengan jujur sebagai kontrak lingkungan, bukan kontrak artikulasi. Napas, detak jantung, jumlah orang, dan deteksi jatuh hampir tidak berubah selama artikulasi jari; informasi gerak tangan terkonsentrasi pada fitur gerak dan varians fase; pretraining dilakukan pada data ruangan delapan jam dengan supervisi sensor PIR dan BME280 [11], bukan pada gerak tangan. Kelayakan representasi ini bagi huruf SIBI karena itu diperlakukan sebagai hipotesis yang diuji pada gerbang G0b (Subbab 3.7), bukan sebagai sifat yang menyertai *checkpoint*.",
  1, "A-2 kontrak lingkungan 2.4")

E("| Masukan | 8 fitur turunan CSI | Amplitudo CSI [3, 114, 10] @ 100 Hz | Citra RGB kamera |",
  "| Masukan | 8 fitur turunan CSI per jendela 1 detik (laju 1 Hz; *batch* (B, 8)); bukan deret *subcarrier* | Amplitudo CSI [3, 114, 10] @ 100 Hz | Citra RGB kamera |",
  1, "Tabel 2.2 sel masukan")

# ============ LANGKAH 2: pemisahan supervisi ============
E("di bawah supervisi guru visual YOLO26m-Pose, menjalankan inferensi terkuantisasi",
  "dengan label kelas dari protokol perekaman serta supervisi *keypoint* dari guru visual YOLO26m-Pose, menjalankan inferensi terkuantisasi",
  2, "rumusan no.1 + tujuan no.1 (cermin)")

E("Selain itu, dataset itu tidak memuat satu pun rekaman CSI, sehingga pasangan data baru harus direkam sendiri pada T2.",
  "Selain itu, dataset itu tidak memuat satu pun rekaman CSI, sehingga pasangan data baru harus direkam sendiri pada T2.\n\nPeran guru dipisahkan menurut jenis target. Untuk 24 huruf statis, label kelas pelatihan diambil dari protokol perekaman (kartu pemandu), sedangkan guru menyumbang deret 21 *keypoint* beserta visibilitasnya. Untuk J dan Z, label kelas juga berasal dari protokol; guru tidak diposisikan sebagai pengklasifikasi kedua huruf gerak itu kecuali model guru terbukti memuat kelasnya [PERLU VALIDASI: kelas J dan Z pada model juara WPC]. Dengan pemisahan ini, hasil `exp11_huruf24` pada 24 huruf statis tidak diperluas menjadi klaim pengenalan 26 huruf oleh guru.",
  1, "B-1 pemisahan peran guru 2.9")

E("Eksperimen `exp11_huruf24` pada 24 huruf statis mencatat *pose* mAP50 0,9580 dengan akurasi huruf 97,6%. Dari angka itu terbaca",
  "Eksperimen `exp11_huruf24` pada 24 huruf statis mencatat *pose* mAP50 0,9580 dengan akurasi huruf 97,6%; angka itu berlaku untuk 24 huruf statis pada data visual dan tidak dikutip sebagai kemampuan guru mengenali J dan Z, yang supervisinya diambil dari lintasan *keypoint* dan label protokol. Dari angka itu terbaca",
  1, "B-2 batas angka guru 2.9")

E("| 5 | Model guru visi | YOLO26m-Pose 21 *keypoint* [12] | YOLOv8-pose, MediaPipe langsung, UNet | 21 titik artikulasi vital untuk membedakan huruf mirip dan lintasan J/Z; akurasi 97,6% pada pra-penelitian (Subbab 2.9) |",
  "| 5 | Model guru visi | YOLO26m-Pose 21 *keypoint* [12] | YOLOv8-pose, MediaPipe langsung, UNet | 21 titik artikulasi vital untuk membedakan huruf mirip dan lintasan J/Z; mAP50 0,9580 dan akurasi 97,6% pada 24 huruf statis (Subbab 2.9) |",
  1, "Tabel 2.4 baris 5")

E("Inti pelatihannya adalah supervisi lintas modalitas berpandu guru (Subbab 3.7): keluaran guru kamera YOLO26m-Pose berupa label kelas dan deret 21 *keypoint* mengawasi pelatihan dua kepala tugas di atas *encoder* CSI terpralatih yang dibekukan.",
  "Inti pelatihannya adalah supervisi lintas modalitas berpandu guru (Subbab 3.7): label kelas dari protokol perekaman serta deret 21 *keypoint* dari guru kamera YOLO26m-Pose mengawasi pelatihan dua kepala tugas di atas *encoder* CSI terpralatih yang dibekukan.",
  1, "3.1 sumber label diselaraskan")

# ============ LANGKAH 3: persamaan dan arsitektur temporal ============
E("Pada baseline, pembaruan tetapan hanya menyentuh kepala beserta modul temporalnya:\n\n```rumus\nθ~c~, θ~r~ ← Optimizer( ∇ L~total~ ), θ~0~ tetap (2.15)\n```\n\ndengan θ~c~ dan θ~r~ tetapan kedua kepala serta θ~0~ tetapan *encoder* yang dibekukan.",
  "Pada baseline, pembaruan tetapan menyentuh seluruh tetapan di luar *encoder*:\n\n```rumus\nΘ~train~ = { φ~adapter~, θ~temporal~, θ~c~, θ~r~ }, θ~encoder~ = θ~0~ (2.15′)\n```\n\ndengan φ~adapter~ tetapan adapter masukan yang hanya hadir jika jalur adapter terpilih pada gerbang G0b, θ~temporal~ tetapan modul temporal, serta θ~c~ dan θ~r~ tetapan kedua kepala; pembaruannya mengikuti Θ~train~ ← Optimizer( ∇ L~total~ ). *Encoder* tetap dibekukan pada θ~0~ sepanjang baseline; skema pembukaan tetapan (LoRA dan pelatihan lanjutan) tetap diperlakukan sebagai pembanding pada Subbab 3.7.",
  1, "C-1 Persamaan 2.15'")

E("Satu komponen dari rancangan lama tetap dipertahankan dan dievaluasi ulang perannya: 1D-CNN. Pada rancangan lama ia menjadi kepala tunggal di atas *backbone*. Pada rancangan ini ia kandidat modul temporal, yaitu peringkas barisan *embedding* per bingkai menjadi satu vektor sebelum kedua kepala, yang bersaing dengan alternatif lebih sederhana berupa agregasi statistik rata-rata dan maksimum. Modul temporal bukan kepala tugas: keluarannya tetap masuk bagi kedua kepala, dan model tetap memiliki dua keluaran tugas utama. Parameter modul temporal ikut dilatih bersama kepala pada Persamaan 2.15. Keputusan mempertahankannya atau menggantinya diambil dari hasil ablasi pada data yang sama (Subbab 3.7), bukan dari preferensi implementasi. Untuk menguji manfaat penggabungan itu, kepala tunggal yang dilatih sendiri-sendiri juga disiapkan sebagai pembanding pada split yang sama.",
  "Satu komponen dari rancangan lama tetap dipertahankan dan dievaluasi ulang perannya: 1D-CNN. Pada rancangan lama ia menjadi kepala tunggal di atas *backbone*. Pada rancangan ini ia kandidat modul temporal yang memelihara urutan waktu. Modul temporal bukan kepala tugas dan tidak dirancang sebagai peringkas tunggal: ia memproses barisan *embedding* per langkah dan mengeluarkan keadaan tersembunyi per langkah, h~1~ sampai h~T~. Kepala klasifikasi membaca ringkasan beratensi (*attention*) atas barisan itu menjadi satu vektor, sedangkan kepala regresi membaca tiap keadaan secara langsung, Q~t~ = reshape( W~r~ · h~t~ + b~r~, 21, 2 ) dengan W~r~ berukuran 42 × 128, sehingga keluaran regresi per segmen berbentuk T × 21 × 2 tanpa kehilangan urutan waktu. Varian peringkas tunggal (Persamaan 2.11) dipertahankan sebagai pembanding ablasi untuk huruf statis, dengan keterbatasannya bagi J dan Z dijelaskan pada laporan. Konsekuensinya, kandidat agregasi statistik rata-rata dan maksimum hanya berlaku untuk jalur klasifikasi; pelatihan multitugas dengan regresi temporal menuntut modul yang memelihara urutan. Parameter modul temporal ikut dilatih bersama kepala pada Persamaan 2.15′. Keputusan mempertahankannya atau menggantinya diambil dari hasil ablasi pada data yang sama (Subbab 3.7), bukan dari preferensi implementasi. Untuk menguji manfaat penggabungan itu, kepala tunggal yang dilatih sendiri-sendiri juga disiapkan sebagai pembanding pada split yang sama.",
  1, "C-2 modul temporal dua cabang 2.8")

E("Rancangan awal kepala memprediksi koordinat x dan y per bingkai waktu,",
  "Varian peringkas tunggal kepala, yang menjadi pembanding ablasi untuk huruf statis, memprediksi koordinat x dan y seluruh jendela dari satu vektor ringkasan,",
  1, "2.7 rujukan varian 2.11 (a)")
E("dengan W~r~ matriks berukuran 42T × 128 untuk jendela ber-T bingkai, Q~i~ prediksi *keypoint*, dan P~i~ koordinat acuan dari guru visual. Bentuk keluaran per bingkai dipilih karena J dan Z dibedakan oleh lintasan gerak, bukan oleh satu pose.",
  "dengan W~r~ matriks berukuran 42T × 128 untuk jendela ber-T langkah, Q~i~ prediksi *keypoint*, dan P~i~ koordinat acuan dari guru visual. Varian utama kepala membaca tiap keadaan tersembunyi modul temporal secara langsung sehingga keluarannya tetap per langkah (Subbab 2.8); bentuk keluaran per langkah dipilih karena J dan Z dibedakan oleh lintasan gerak, bukan oleh satu pose.",
  1, "2.7 rujukan varian 2.11 (b)")

E("*Encoder* yang dibekukan menghasilkan barisan *embedding* 128 dimensi; modul temporal meringkasnya menjadi satu vektor bersama, lalu kepala klasifikasi membacanya menjadi kelas huruf dan kepala regresi membacanya menjadi 21 koordinat *keypoint*.",
  "*Encoder* yang dibekukan menghasilkan barisan *embedding* 128 dimensi; modul temporal memproses barisan itu menjadi keadaan tersembunyi per langkah, lalu kepala klasifikasi membaca ringkasannya menjadi kelas huruf dan kepala regresi membaca tiap langkah menjadi 21 koordinat *keypoint*.",
  1, "2.17 kerangka diselaraskan")

E('    EMT["Embedding 128 per bingkai<br/>+ modul temporal"]',
  '    EMT["Embedding 128 per langkah jendela<br/>+ modul temporal"]',
  1, "Gambar 2.2 simpul EMT")
E('    HRG["Kepala regresi<br/>(Persamaan 2.11)"]',
  '    HRG["Kepala regresi per langkah<br/>(Subbab 2.8)"]',
  1, "Gambar 2.2 simpul HRG")

# ============ LANGKAH 4: keputusan deployment ============
E("Setelah terpilih, *encoder*, modul temporal, dan kedua kepala digabung menjadi satu *graph* inferensi, lalu dikuantisasi.",
  "Setelah terpilih, model *deployment* disusun menurut Pilihan 1: *encoder*, adapter (jika dipakai), modul temporal, dan kepala klasifikasi digabung menjadi satu *graph* inferensi lalu dikuantisasi; kepala regresi dilepas setelah pelatihan karena perannya supervisi tambahan. Kepala regresi ikut dijalankan pada *deployment* (Pilihan 2) hanya jika keputusan pada Tabel 3.7 menyatakannya, dengan tambahan biaya memori, komputasi, dan kuantisasi yang diukur serta dilaporkan.",
  1, "D-1 deployment Pilihan 1 3.7")

E("Galat per *keypoint* juga diringkas untuk mengenali titik jari mana yang paling sulit diprediksi dari CSI.",
  "Galat per *keypoint* juga diringkas untuk mengenali titik jari mana yang paling sulit diprediksi dari CSI. Pada baseline Pilihan 1, MPJPE dan PCK@α berstatus metrik pemantauan yang dilaporkan, bukan syarat gerbang; jika Pilihan 2 yang terpilih, ambang kelayakan regresi ditetapkan lebih dulu pada Tabel 3.7 sebelum G1 dinilai.",
  1, "D-3 klausul MPJPE 2.14")

# ============ LANGKAH 5: arsitektur audio terpadu ============
E("Gambar 3.3 memperlihatkan keseluruhan sistem: dua jalur operasional tanpa kamera ditambah satu jalur guru yang hanya aktif saat akuisisi dan pelatihan. Pada arah pertama, *beacon* ESP-NOW node pemancar melintasi zona isyarat, gerak pengisyarat mengubah deret CSI yang ditangkap node penerima, lalu model *encoder* berkepala dua yang terkuantisasi menghasilkan label beserta skor keyakinan. Label itu dipetakan menjadi teks Indonesia di layar dan dibunyikan lewat Kokoro TTS ONNX di aplikasi Tauri secara luring; estimasi *keypoint* dari kepala regresi menjadi keluaran tambahan sesuai rancangan final (Subbab 2.7). Pada arah kedua, tombol tekan-untuk-bicara mengaktifkan mikrofon, ucapan dikenali layanan ASR, dan teks dipetakan ke representasi SIBI dari aset modul (Subbab 2.12). Saat internet terputus, sintesis tetap berjalan *on-device* dan ASR beralih ke server lokal faster-whisper. Jalur guru, yang memakai *webcam* dan YOLO26m-Pose untuk mengekstrak deret *keypoint* sebagai supervisi pelatihan, bukan bagian produk akhir.",
  "Gambar 3.3 memperlihatkan keseluruhan sistem: dua jalur operasional tanpa kamera ditambah satu jalur guru yang hanya aktif saat akuisisi dan pelatihan. Pada arah pertama, *beacon* ESP-NOW node pemancar melintasi zona isyarat, gerak pengisyarat mengubah deret CSI yang ditangkap node penerima, dan model berkepala klasifikasi yang terkuantisasi dijalankan langsung di modul menghasilkan label beserta skor keyakinan. Label dikirim melalui UDP ke server Rust sebagai telemetri, dipetakan menjadi teks Indonesia, lalu teks itu tampil di layar modul dan aplikasi Tauri sekaligus disintesis mesin TTS di server lokal; audio hasil sintesis dialirkan kembali ke modul dan diputar pada *speaker* DAC I2S. Jika aliran audio ke modul tidak stabil atau server tidak tersedia, sintesis beralih ke mesin *on-device* pada ponsel dan pemutaran memakai *speaker* ponsel; peralihan itu dicatat. Dengan keputusan *deployment* Pilihan 1 (Tabel 3.7), kepala regresi berperan sebagai supervisi tambahan saat pelatihan dan dilepas pada *deployment*, sehingga keluaran perangkat ialah label huruf beserta skor keyakinan.\n\nPada arah kedua, tombol tekan-untuk-bicara mengaktifkan mikrofon I2S pada node penerima; audio ditangkap di modul lalu dialirkan ke server Rust, yang meneruskannya ke layanan ASR awan saat daring atau memprosesnya sendiri dengan faster-whisper. Teks hasil pengenalan dipetakan ke representasi SIBI dari aset modul dan tampil pada aplikasi Tauri, dengan indikator opsional di layar modul. Saat internet terputus, kedua arah tetap berjalan karena ASR dan TTS beralih ke server lokal; kebutuhan pemrosesan audio di node penerima sebatas penangkapan dan pengaliran, bukan pengenalan. Jalur guru, yang memakai *webcam* dan YOLO26m-Pose untuk mengekstrak deret *keypoint* sebagai supervisi pelatihan, bukan bagian produk akhir.",
  1, "E-1 dua paragraf alur arah 3.5")

E("    accDescr: Tiga rantai. Arah 1 mengalir dari beacon ESP-NOW node pemancar melalui zona isyarat ke node penerima yang menjalankan encoder terpralatih berkepala dua yang terkuantisasi, lalu teks tampil di layar dan dibunyikan Kokoro TTS ONNX di aplikasi Tauri. Arah 2 mengalir dari tombol tekan-untuk-bicara dan mikrofon ke layanan ASR awan, lalu teks dan representasi SIBI tampil di layar. Jalur guru memakai webcam dan YOLO26m-Pose untuk supervisi pelatihan. Garis putus-putus menandai beralih ke server lokal saat internet terputus.",
  "    accDescr: Tiga rantai. Arah 1 mengalir dari beacon ESP-NOW node pemancar melalui zona isyarat ke node penerima yang menjalankan model klasifikasi terkuantisasi; label dan skor dikirim via UDP ke server Rust, teks tampil di layar modul dan aplikasi Tauri, teks disintesis mesin TTS Kokoro di server lokal, dan audio dialirkan kembali ke speaker node penerima. Arah 2 mengalir dari tombol tekan-untuk-bicara dan mikrofon I2S; audio dialirkan ke server lalu dikenali layanan ASR awan saat daring atau faster-whisper saat luring, dan teks dipetakan ke representasi SIBI pada aplikasi Tauri. Jalur guru memakai webcam dan YOLO26m-Pose untuk supervisi pelatihan. Garis putus-putus menandai jalur cadangan TTS on-device pada ponsel jika server tidak tersedia.",
  1, "Gambar 3.3 accDescr")
E('    RX["Node RX: CSI promiscuous +<br/>encoder terpralatih berkepala dua<br/>terkuantisasi + antarmuka"]',
  '    RX["Node RX: CSI promiscuous +<br/>model klasifikasi terkuantisasi<br/>+ antarmuka"]',
  1, "Gambar 3.3 simpul RX")
E('    DSP1["Layar modul:<br/>teks hasil"]',
  '    DSP1["Layar modul dan aplikasi Tauri:<br/>teks hasil"]',
  1, "Gambar 3.3 simpul DSP1")
E('    SPK["Speaker +<br/>rotary encoder"]',
  '    SPK["Speaker DAC I2S<br/>di node RX"]',
  1, "Gambar 3.3 simpul SPK")
E('        TTS["Mesin TTS on-device:<br/>Kokoro ONNX di aplikasi<br/>Tauri (Poco F4 5G)"]\n', '',
  1, "Gambar 3.3 simpul TTS dihapus")
E('        MAPL -- "teks via Wi-Fi" --> TTS\n        TTS -- "audio" --> SPK\n', '',
  1, "Gambar 3.3 tepi TTS lama dihapus")
E('    MIC -- "audio via Wi-Fi" --> STT',
  '    MIC -- "audio via UDP" --> SVR',
  1, "Gambar 3.3 tepi MIC")
E('    STT["Layanan<br/>ASR awan"]',
  '    STT["Layanan ASR awan<br/>(saat daring)"]',
  1, "Gambar 3.3 simpul STT")
E('    DSP2["Layar modul: teks lalu<br/>representasi SIBI"]',
  '    DSP2["Aplikasi Tauri: teks lalu<br/>representasi SIBI"]',
  1, "Gambar 3.3 simpul DSP2")
E('    LOK["Server lokal (cadangan):<br/>ASR faster-whisper,<br/>TTS MMS, server RuView,<br/>server Rust"]\n    TTS -. "TTS lokal" .-> LOK\n    STT -. "ASR lokal" .-> LOK',
  '    SVR["Server Rust di laptop:<br/>telemetri CSI, orkestrasi,<br/>TTS Kokoro/MMS utama,<br/>faster-whisper ASR luring"]\n    TTSP["TTS on-device ponsel:<br/>Kokoro ONNX di Tauri<br/>(cadangan)"]\n\n    RX -- "label + skor via UDP" --> SVR\n    SVR -- "teks" --> DSP1\n    SVR -- "audio dialirkan" --> SPK\n    SVR -- "audio" --> STT\n    SVR -- "teks (luring)" --> DSP2\n    SVR -. "server tak tersedia" .-> TTSP',
  1, "Gambar 3.3 simpul server + tepi")
E("Gambar 3.3 Arsitektur produk akhir tanpa kamera. Subgraf arah 1 = isyarat menjadi teks dan suara; subgraf arah 2 = ucapan menjadi representasi SIBI; subgraf jalur guru hanya aktif saat akuisisi dan pelatihan; garis putus-putus = beralih ke server lokal ketika internet tidak tersedia.",
  "Gambar 3.3 Arsitektur produk akhir tanpa kamera. Subgraf arah 1 = isyarat menjadi teks dan suara; subgraf arah 2 = ucapan menjadi representasi SIBI; subgraf jalur guru hanya aktif saat akuisisi dan pelatihan; garis putus-putus = jalur cadangan TTS *on-device* pada ponsel jika server tidak tersedia.",
  1, "Gambar 3.3 keterangan")

E("| 4 | Pengeras suara dengan DAC I2S | Mini 8 Ohm 3 W, penguat kelas D MAX98357A | 1 set | Pemutaran suara TTS dari modul |",
  "| 4 | Pengeras suara dengan DAC I2S | Mini 8 Ohm 3 W, penguat kelas D MAX98357A | 1 set | Pemutaran suara TTS hasil sintesis server yang dialirkan ke modul (keputusan D3 pada Tabel 3.7); *speaker* ponsel sebagai cadangan |",
  1, "E-2 Tabel 3.1 baris 4")
E("| 7 | Laptop | ASUS TUF Dash F15 FX516PR: i7-11370H, RTX 3070 Laptop 8 GB VRAM, RAM 16 GB | 1 unit | Akuisisi jalur guru, pelatihan dua kepala, evaluasi, server cadangan |",
  "| 7 | Laptop | ASUS TUF Dash F15 FX516PR: i7-11370H, RTX 3070 Laptop 8 GB VRAM, RAM 16 GB | 1 unit | Server Rust (penelan CSI, orkestrasi, ASR lokal cadangan, TTS lokal utama, dasbor); akuisisi jalur guru; pelatihan dua kepala; evaluasi |",
  1, "E-2 Tabel 3.1 baris 7")
E("| 8 | Ponsel pintar | Poco F4 5G: Snapdragon 870, RAM 6 GB, Android | 1 unit | *Hotspot* portabel, klien Tauri, mesin TTS *on-device* |",
  "| 8 | Ponsel pintar | Poco F4 5G: Snapdragon 870, RAM 6 GB, Android | 1 unit | Klien Tauri (tampilan teks dan representasi SIBI), mesin TTS *on-device* sebagai cadangan, *hotspot* cadangan |",
  1, "E-2 Tabel 3.1 baris 8")

E("6. Sintesis ucapan berjalan *on-device* di ponsel, sedangkan pengenalan ucapan memakai layanan awan dengan mesin lokal sebagai cadangan; pilihan finalnya ditetapkan pada gerbang G3.",
  "6. Sintesis ucapan utama berjalan di server lokal dan audio diputar pada *speaker* node penerima, dengan mesin *on-device* pada ponsel sebagai cadangan; pengenalan ucapan memakai layanan awan dengan faster-whisper lokal sebagai cadangan; pilihan final mesin dan layanan tetap ditetapkan pada gerbang G3.",
  1, "E-3 Batasan no.6")

E("Mesin TTS *on-device* yang direncanakan ialah Kokoro-82M ONNX bersama sekitar 82 juta parameter [24]. Mesinnya berjalan luring di ponsel melalui ONNX Runtime.",
  "Mesin TTS yang direncanakan ialah Kokoro-82M ONNX berserta sekitar 82 juta parameter [24]; dengan keputusan D3, mesin itu diposisikan pada dua lokasi, yaitu server lokal sebagai jalur utama dan ponsel melalui ONNX Runtime sebagai jalur cadangan, dan keduanya memakai prasyarat suara Indonesia yang sama serta diverifikasi pada G3.",
  1, "E-3 kalimat 2.11")

E("Server lokal pada laptop menjalankan server RuView, server Rust, faster-whisper, dan TTS MMS sebagai jalur cadangan tanpa internet.",
  "Server lokal pada laptop menjalankan server RuView, server Rust, faster-whisper, serta TTS Kokoro/MMS sebagai jalur utama luring, sehingga pemrosesan teks dan suara tetap berjalan tanpa internet; server Rust bukan sekadar perantara, melainkan titik orkestrasi kedua arah penerjemahan.",
  1, "E-4 kalimat 2.13")

E("Server lokal menjalankan server RuView, server Rust, faster-whisper, serta MMS-TTS-ind sebagai jalur cadangan.",
  "Server lokal menjalankan server RuView, server Rust, faster-whisper sebagai ASR cadangan, serta TTS Kokoro/MMS sebagai jalur utama sintesis luring.",
  1, "3.5 paragraf topologi diselaraskan")

E("Aplikasi Tauri pada ponsel menerima teks hasil isyarat sekaligus menjalankan Kokoro TTS ONNX [24]. Target *parsing* bingkai di bawah 0,2 ms serta memori server di bawah 40 MB baru diukur pada G3 (Subbab 3.8.3). Mesin sintesisnya berjalan sepenuhnya di ponsel: Kokoro-82M ONNX diinferensikan luring lewat ONNX Runtime di dalam Tauri [24] dengan target inferensi frasa pendek di bawah 100 ms pada Snapdragon 870. Prasyaratnya hanya satu, yaitu tersedia suara bahasa Indonesia pada Kokoro; jika belum, mesin *on-device* beralih ke MMS-TTS-ind [25] dan peralihan itu dilaporkan.",
  "Aplikasi Tauri pada ponsel menerima teks hasil isyarat sekaligus menjadi klien antarmuka dua arah. Target *parsing* bingkai di bawah 0,2 ms serta memori server di bawah 40 MB baru diukur pada G3 (Subbab 3.8.3). Mesin sintesis utamanya berjalan di server lokal dengan Kokoro-82M ONNX yang diinferensikan luring [24], sementara jalur cadangan *on-device* berjalan di ponsel lewat ONNX Runtime di dalam Tauri. Target latensinya didefinisikan sebagai waktu menuju audio pertama (*time-to-first-audio*, TTFA) di bawah 100 ms pada frasa uji paling banyak lima kata; durasi sintesis keseluruhan dilaporkan terpisah. Prasyaratnya hanya satu, yaitu tersedia suara bahasa Indonesia pada Kokoro; jika belum, jalur beralih ke MMS-TTS-ind [25] dan peralihan itu dilaporkan.",
  1, "3.5 paragraf TTS + TTFA (F-5)")

E("| 2 | Mesin TTS | Kokoro TTS ONNX *on-device*; prasyarat suara Indonesia pada G3; alternatif MMS-TTS-ind [24], [25] | TTS awan, VITS/Tacotron penuh | Model 82 juta parameter diinferensikan luring pada ponsel (Subbab 2.11) |",
  "| 2 | Mesin TTS | Kokoro TTS ONNX luring; prasyarat suara Indonesia pada G3; alternatif MMS-TTS-ind [24], [25] | TTS awan, VITS/Tacotron penuh | Model 82 juta parameter diinferensikan luring di server lokal (utama) dan ponsel (cadangan) (Subbab 2.11) |",
  1, "Tabel 2.4 baris 2")
E("| 8 | faster-whisper dan MMS-TTS-ind [26], [25]; layanan ucapan awan [PERLU DATA: layanan final hasil uji banding] | ASR dan TTS cadangan lokal; jalur utama pengenalan ucapan |",
  "| 8 | faster-whisper dan MMS-TTS-ind [26], [25]; layanan ucapan awan [PERLU DATA: layanan final hasil uji banding] | ASR cadangan lokal (faster-whisper); alternatif TTS lokal (MMS-TTS-ind); ASR utama saat daring |",
  1, "Tabel 3.2 baris 8")
E("| 10 | Kokoro TTS ONNX dan ONNX Runtime [24] | Mesin TTS *on-device*; prasyarat suara Indonesia pada G3 |",
  "| 10 | Kokoro TTS ONNX dan ONNX Runtime [24] | Mesin TTS utama di server lokal dan cadangan *on-device* di ponsel; prasyarat suara Indonesia pada G3 |",
  1, "Tabel 3.2 baris 10")

E("3. Mengukur waktu pengenalan, pemetaan, inferensi TTS *on-device*, serta total ujung ke ujung pada kedua arah.",
  "3. Mengukur waktu pengenalan, pemetaan, waktu menuju audio pertama (TTFA) sintesis TTS, serta total ujung ke ujung pada kedua arah.",
  1, "3.8.4 langkah 3 TTFA")
E("4. Mengulang pengukuran pada kedua kandidat mesin *on-device* (Kokoro ONNX dan MMS-TTS-ind) serta jalur pembanding awan dan server lokal, lalu menimbang mutu dan latensinya.",
  "4. Mengulang pengukuran pada kedua kandidat mesin (Kokoro ONNX dan MMS-TTS-ind) di server lokal maupun *on-device* ponsel serta jalur pembanding awan, lalu menimbang mutu dan latensinya.",
  1, "3.8.4 langkah 4 diselaraskan")

# Gambar 3.1: simpul diselaraskan + simpul G0b
E("    accDescr: Diagram dua fase. Fase pembangunan data berisi T0 replikasi platform dan audit checkpoint encoder, gerbang G0 baseline, T1 kurasi isyarat, dan T2 perekaman dataset serta pelatihan dua kepala. Fase pengujian berisi kuantisasi model, gerbang G1 model tepi, T3 uji generalisasi, gerbang G2 konsultasi tiga pilar, T4 pengemasan purwarupa, gerbang G3 integrasi mesin ucapan, gerbang G4 sintesis kelayakan, dan T5 analisis serta penulisan.",
  "    accDescr: Diagram dua fase. Fase pembangunan data berisi T0 replikasi platform dan audit checkpoint encoder, gerbang G0 baseline, T1 kurasi isyarat, sub-gerbang G0b probe kompatibilitas representasi atas data pilot, dan T2 perekaman dataset serta pelatihan dua kepala. Fase pengujian berisi kuantisasi model, gerbang G1 model tepi, T3 uji generalisasi, gerbang G2 konsultasi tiga pilar, T4 pengemasan purwarupa, gerbang G3 integrasi mesin ucapan, gerbang G4 sintesis kelayakan, dan T5 analisis serta penulisan.",
  1, "Gambar 3.1 accDescr G0b")
E("    T1 --> T2\n    end",
  '    G0b("G0b awal T2: probe linear embedding beku,<br/>keputusan jalur masukan")\n    T1 --> G0b\n    G0b -- "lolos" --> T2\n    end',
  1, "Gambar 3.1 simpul G0b")
E('    T2B["Kuantisasi model terpilih dan uji<br/>deployment encoder berkepala dua<br/>ke modul ESP32-S3"]',
  '    T2B["Kuantisasi model terpilih dan uji<br/>deployment jalur klasifikasi<br/>ke modul ESP32-S3"]',
  1, "Gambar 3.1 simpul T2B")
E('    T4["T4 Pengemasan dua arah, full-stack<br/>Rust, TTS on-device, uji penerimaan<br/>dan biaya (M10–M12)"]',
  '    T4["T4 Pengemasan dua arah, full-stack<br/>Rust, TTS server lokal, uji penerimaan<br/>dan biaya (M10–M12)"]',
  1, "Gambar 3.1 simpul T4")
E('    G3("G3 M11: integrasi Rust dan mesin<br/>ucapan on-device dalam<br/>anggaran latensi")',
  '    G3("G3 M11: integrasi Rust dan mesin<br/>ucapan dalam anggaran latensi")',
  1, "Gambar 3.1 simpul G3")
E("| 5 | T4 Pengemasan dua arah, Rust, TTS *on-device*, uji operasional, jalur ucapan, kamus, kegunaan, validator |",
  "| 5 | T4 Pengemasan dua arah, Rust, TTS server lokal, uji operasional, jalur ucapan, kamus, kegunaan, validator |",
  1, "Tabel 3.6 baris 5")

E("Lima gerbang keputusan menutup rangkaian itu dengan kriteria dan tindakan jika gagal yang dirinci pada Tabel 3.5; penerimaan pengguna dan biaya dinilai G4, yang kemudian menyusun rekomendasi posisi TKT/TRL 3–4 [27].",
  "Lima gerbang keputusan menutup rangkaian itu, ditambah sub-gerbang G0b yang mengaudit kompatibilitas representasi *encoder* atas data pilot sebelum pelatihan penuh; kriteria dan tindakan jika gagal dirinci pada Tabel 3.5; penerimaan pengguna dan biaya dinilai G4, yang kemudian menyusun rekomendasi posisi TKT/TRL 3–4 [27].",
  1, "3.2 kalimat gerbang G0b")
E("T0 juga mengaudit *checkpoint encoder* [11]: bentuk masukan, jumlah parameter, normalisasi L2, dukungan ekspor, dan kompatibilitas LoRA (Subbab 3.7).",
  "T0 juga mengaudit *checkpoint encoder* [11]: bentuk masukan, parameter normalisasi masukan, jumlah parameter, normalisasi L2, dukungan ekspor, dan kompatibilitas LoRA (Subbab 3.7).",
  1, "3.2 daftar audit T0")

# ============ LANGKAH 6: parameter, ambang, temuan tambahan ============
E("Deret CSI dipotong menjadi segmen huruf dengan segmentasi energi gerak memakai Delta-CSI, yaitu rata-rata perubahan amplitudo antarbingkai pada seluruh 56 *subcarrier*:",
  "Deret CSI dipotong menjadi segmen huruf dengan segmentasi energi gerak memakai Delta-CSI, yaitu rata-rata besar perubahan koefisien kanal kompleks antarbingkai pada seluruh 56 *subcarrier*:",
  1, "F-1 definisi Delta-CSI")

E("Fitur tiap segmen, yaitu amplitudo dan fase *subcarrier* terpilih serta spektrum Doppler [6], [14], diringkas menjadi masukan *encoder*.",
  "Fitur tiap segmen, yaitu amplitudo dan fase *subcarrier* terpilih serta spektrum Doppler [6], [14], diringkas menjadi masukan *encoder*. Sebagai pembanding sensitivitas pada uji Delta-CSI (Subbab 3.8.1), varian berbasis amplitudo saja juga dihitung dan dilaporkan berdampingan:\n\n```rumus\nd~|H|~( t ) = ( 1 / 56 ) · Σ~n~ | |h~n~(t)| − |h~n~( t − 1 )| |\n```",
  1, "F-1 varian amplitudo")

E("Setelah bentuk masukan pasti, *encoder* diterapkan pada tiap bingkai menghasilkan barisan *embedding* 128 dimensi, lalu modul temporal meringkas barisan itu menjadi satu vektor bersama. Kandidat modul temporal ialah 1D-CNN ringan dari rancangan lama atau agregasi statistik; pilihan di antara keduanya diambil dari hasil ablasi pada data yang sama (Subbab 2.8).",
  "Setelah bentuk masukan pasti, alur fitur dibakukan pada tiga tingkat: bingkai CSI (56 *subcarrier*, hingga 50 bingkai per detik), jendela fitur sepanjang W = 1 detik yang diringkas menjadi satu vektor delapan fitur, dan langkah *embedding*, yaitu satu keluaran *encoder* per jendela. Jalur pertama menghitung ulang delapan fitur turunan bawaan RuView dari bingkai CSI; jalur kedua melatih adapter masukan kecil berbasis konvolusi satu dimensi yang memetakan jendela CSI mentah ke vektor masukan *encoder*, sehingga informasi *subcarrier* tidak diringkas lebih dulu oleh rumus tetap. Pada kedua jalur, *encoder* diterapkan per jendela, bukan per bingkai, sesuai kontrak laju 1 Hz kartu model [11].\n\nResolusi temporal dijaga dengan jendela bergulir berlompatan H = 0,25 detik (usulan; dikalibrasi pada T2), sehingga satu segmen huruf menghasilkan satu sampai sekitar tiga belas langkah *embedding* tergantung durasinya. Untuk J dan Z, kelas tidak dibaca dari satu jendela: barisan langkah diproses modul temporal secara berurutan dan klasifikasinya diambil dari ringkasan barisan tersebut. Dengan itu lintasan gerak J dan Z tetap tersedia pada laju empat langkah per detik, cukup untuk lintasan sekitar satu detik, tanpa melanggar kontrak masukan *encoder*. Kandidat modul temporal ialah 1D-CNN ringan dari rancangan lama yang memelihara urutan waktu per langkah; agregasi statistik hanya menjadi kandidat bagi jalur klasifikasi, dan pilihan di antara keduanya diambil dari hasil ablasi pada data yang sama (Subbab 2.8).\n\nKompatibilitas representasi diuji pada gerbang G0b sebagai eksperimen sungguh-sungguh, bukan asumsi. Gerbang G0b dinilai setelah G0 atas data pilot satu pengisyarat satu sesi (sekitar 97 menit) yang direkam lebih dulu atau diambil dari sesi pertama T2. Alat ujinya *probe* linear, yaitu pengklasifikasi linear sederhana di atas *embedding* beku; cara ini baku untuk membaca seberapa informatif sebuah representasi tanpa melatih model penuh. Rangkaiannya: *probe* 24 huruf statis pada skema blok temporal, *probe* sekuensial atas gabungan langkah tiap segmen, *probe* biner J terhadap Z, serta dua kontrol, yaitu *probe* pada fitur mentah ringkas dan kontrol label-acak (p < 0,05), agar hasilnya tidak menipu. Ambang usulannya: F1 makro *probe* sekurang-kurangnya 0,30 dan sekurang-kurangnya tiga kali peluang acak; *probe* J–Z sekurang-kurangnya 70%; seluruhnya difinalkan bersama pembimbing sebelum gerbang dinilai. Jalur fitur turunan dipakai jika lulus; jika gagal tetapi adapter lulus, adapter yang dipilih; jika keduanya gagal, *encoder* beku ditinggalkan menuju skema adaptasi LoRA dan pelatihan lanjutan (Subbab 2.5) dan hasilnya dilaporkan sebagai temuan.",
  1, "A-3 + A-4 + A-5 tiga tingkat, jendela bergulir, G0b")

E("*Dataset* murid terbentuk dengan menyelaraskan tiga deret menurut penanda waktu: jendela CSI hasil segmentasi, label huruf guru, dan deret *keypoint* guru. Guru memakai model juara pra-penelitian dari repositori peneliti [12].",
  "*Dataset* murid terbentuk dengan menyelaraskan tiga deret menurut penanda waktu: jendela CSI hasil segmentasi, label huruf dari kartu pemandu protokol, dan deret *keypoint* guru. Guru memakai model juara pra-penelitian dari repositori peneliti [12]. Label kelas tiap segmen diambil dari kartu pemandu protokol; keluaran kelas guru hanya dipakai sebagai salinan pembanding untuk penyaringan kualitas, bukan sebagai label kebenaran. Ketidakcocokan antara label protokol dan kelas guru dicatat sebagai temuan kualitas anotasi dan dilaporkan bersama tingkat segmen terbuang.",
  1, "B-3 sumber label 3.7")

E("Seluruh pasangan direkam dalam struktur *dataset* berpasangan Subbab 2.17, lengkap dengan mask visibilitas, metadata sesi, dan skor kualitas anotasi. Enam skema pada Tabel 3.4 mengukur kinerja; untuk skema dalam sesi, pembagiannya temporal per blok dan tidak acak.",
  "Seluruh pasangan direkam dalam struktur *dataset* berpasangan Subbab 2.17, lengkap dengan mask visibilitas, metadata sesi, dan skor kualitas anotasi.\n\nDeret *keypoint* guru disampel ulang ke pusat tiap jendela fitur sehingga tiap langkah *embedding* memiliki satu target 21 × 2; keluaran regresi model didefinisikan pada laju yang sama. Untuk pelaporan galat lintasan J dan Z, deret prediksi diinterpolasi kembali ke laju kamera agar dapat dibandingkan bingkai demi bingkai dengan acuan guru, dan metode interpolasinya dinyatakan pada laporan. Panjang T ditetapkan 16 langkah per segmen (usulan; difinalkan dari distribusi durasi segmen pada data pilot T2), menutup segmen hingga sekitar empat detik pada lompatan 0,25 detik. Segmen lebih pendek diberi *padding* nol dengan mask valid, dan kerugian regresi dinormalisasi oleh jumlah langkah valid; mask visibilitas Persamaan 2.13 diperluas satu dimensi waktu. Resampling ke panjang tetap tidak dipakai untuk pelatihan J dan Z karena menyeragamkan durasi dan menghapus petunjuk kecepatan yang justru membedakan kedua huruf itu.\n\nEnam skema pada Tabel 3.4 mengukur kinerja; untuk skema dalam sesi, pembagiannya temporal per blok dan tidak acak.",
  1, "C-4 + C-3 penyelarasan laju + panjang T")

E("dengan kerugian gabungan Persamaan 2.14 dan 2.15, memakai seed tetap",
  "dengan kerugian gabungan Persamaan 2.14 dan 2.15′, memakai seed tetap",
  1, "3.7 rujukan 2.15'")

E("10. Isyarat kontinu, tata bahasa isyarat penuh, BISINDO, serta klasifikasi gerakan otomatis dari video berada di luar pembahasan.",
  "10. Isyarat kontinu, tata bahasa isyarat penuh, BISINDO, serta klasifikasi gerakan otomatis dari video berada di luar pembahasan.\n11. Seluruh hasil dilaporkan sebagai bukti awal pada populasi terbatas, yaitu 3–4 pengisyarat, sedikitnya dua ruang, dan satu konfigurasi perangkat; skema *leave-one-subject-out*, pengguna baru, dan *leave-one-room-out* dibaca sebagai indikasi ketahanan awal, bukan bukti generalisasi populasi, sehingga klaim lintas populasi tidak dibuat.",
  1, "F-2 Batasan no.11")

E("Satu uji lagi, cakupan kamus, melengkapi analisis tanpa menjadi syarat gerbang.",
  "Satu uji lagi, cakupan kamus, melengkapi analisis tanpa menjadi syarat gerbang. Seluruh hasil klasifikasi, regresi, dan operasional dilaporkan sebagai bukti awal pada populasi terbatas 3–4 pengisyarat, sedikitnya dua ruang, dan satu konfigurasi perangkat; skema *leave-one-subject-out*, pengguna baru, dan *leave-one-room-out* dibaca sebagai indikasi ketahanan awal, bukan bukti generalisasi populasi (Subbab 1.4).",
  1, "F-2 batas klaim 3.8")

E("Keterpakaian purwarupa ditelaah lewat uji kegunaan bersama 3–5 pengguna kelompok sasaran pada skenario tugas terbimbing, yaitu saling menyampaikan pesan pendek melalui ejaan huruf dan kosakata tampilan. Tiap pengguna menjalani langkah berikut.",
  "Uji kegunaan diposisikan sebagai uji kelayakan skala kecil: hasilnya dianalisis secara deskriptif untuk menemukan hambatan pemakaian dan mengarahkan perbaikan purwarupa, bukan sebagai bukti efektivitas pada populasi pengguna; rumusan ini selaras dengan Batasan no. 9. Keterpakaian purwarupa ditelaah lewat uji kegunaan bersama 3–5 pengguna kelompok sasaran pada skenario tugas terbimbing, yaitu saling menyampaikan pesan pendek melalui ejaan huruf dan kosakata tampilan. Tiap pengguna menjalani langkah berikut.",
  1, "F-6 framing 3.8.5")

E("7. Meminta validator mengambil sampel segmen untuk memeriksa kebenaran bentuk isyarat; label guru berstatus *pseudo-label* sampai pemeriksaan ini selesai.\n",
  "7. Meminta validator mengambil sampel segmen untuk memeriksa kebenaran bentuk isyarat; label guru berstatus *pseudo-label* sampai pemeriksaan ini selesai.\n\nBeban perekaman dihitung agar protokolnya realistis dan etis. Dengan 26 huruf dan kurang lebih 30 repetisi, satu sesi memuat sekitar 780 repetisi; pada asumsi lima detik per repetisi, perekaman murninya sekitar 65 menit, dan dengan jeda blok, kalibrasi, serta persiapan, satu sesi memakan waktu sekitar 97 menit. Setiap sesi dibagi blok sekitar sepuluh menit dengan jeda wajib sekurang-kurangnya tiga menit di antaranya; paling banyak dua sesi per hari untuk satu pengisyarat; pengisyarat boleh menghentikan repetisi kapan saja tanpa konsekuensi. Tingkat kelelahan diamati dari penurunan mutu segmen pada blok akhir dan dilaporkan bersama tingkat segmen terbuang.\n",
  1, "F-3 beban perekaman 3.6")

E("Akurasi dilaporkan dalam dua versi, yaitu tanpa penolakan pada seluruh segmen uji dan dengan penolakan pada segmen yang diterima.",
  "Akurasi dilaporkan dalam dua versi, yaitu tanpa penolakan pada seluruh segmen uji dan dengan penolakan pada segmen yang diterima. *Recall* tiap kelas dilaporkan, dengan *recall* J dan Z terpisah beserta *confusion* terhadap huruf paling mirip.",
  1, "3.8.2 recall J/Z")

# Tabel 3.5: baris G0b baru + G1 diperkuat + G3 TTFA
E("| G0 | Baseline CSI dan jaringan, akhir M2 | Akuisisi 56 *subcarrier* 1 m ke UDP Rust terbaca stabil; laju sekurang-kurangnya 25 bingkai per detik; paket hilang tidak melampaui 0,1%; pola bergerak terpisah dari diam; audit *checkpoint encoder* selesai | Perbaikan penempatan satu kali; gagal lagi berarti jalur CSI dihentikan dan dilaporkan |",
  "| G0 | Baseline CSI dan jaringan, akhir M2 | Akuisisi 56 *subcarrier* 1 m ke UDP Rust terbaca stabil; laju sekurang-kurangnya 25 bingkai per detik; paket hilang tidak melampaui 0,1%; pola bergerak terpisah dari diam; audit *checkpoint encoder* selesai | Perbaikan penempatan satu kali; gagal lagi berarti jalur CSI dihentikan dan dilaporkan |\n| G0b | Audit kompatibilitas representasi *encoder*, setelah G0 atas data pilot (awal T2) | *Probe* linear di atas *embedding* beku: F1 makro 24 huruf statis sekurang-kurangnya 0,30 dan sekurang-kurangnya tiga kali peluang acak; *probe* biner J–Z sekurang-kurangnya 70% [usulan]; kontrol label-acak signifikan; keputusan jalur masukan tercatat | Jalur fitur turunan gagal maka jalur adapter diuji; keduanya gagal maka skema adaptasi LoRA/pelatihan lanjutan (Subbab 2.5) dan hasilnya dilaporkan sebagai temuan |",
  1, "Tabel 3.5 baris G0b")
E("| G1 | Model tepi terkuantisasi dan dua kepala, akhir M8 | Akurasi dalam sesi sekurang-kurangnya 50% (sekitar 13 kali acak 3,8%) dan melampaui pembanding ablasi kepala tunggal; manfaat multitugas dilaporkan dari ablasi; MPJPE dilaporkan; inferensi terkuantisasi di bawah 100 ms | Pangkas himpunan huruf pembeda terkuat, lalu nilai ulang |",
  "| G1 | Model tepi terkuantisasi dan dua kepala, akhir M8 | Akurasi dalam sesi sekurang-kurangnya 50% (sekitar 13 kali acak 3,8%); F1 makro sekurang-kurangnya 0,45 [usulan]; tidak ada kelas dengan *recall* nol pada himpunan huruf terpilih; melampaui pembanding ablasi kepala tunggal dengan manfaat multitugas dilaporkan; *recall* J dan Z dilaporkan terpisah beserta *confusion* terhadap huruf paling mirip; MPJPE dilaporkan sebagai pemantauan; inferensi terkuantisasi di bawah 100 ms; seluruh ambang difinalkan bersama pembimbing sebelum G1 dinilai | Pangkas himpunan huruf pembeda terkuat, lalu nilai ulang |",
  1, "F-4 Tabel 3.5 G1")
E("| G3 | Integrasi Rust dan mesin ucapan, M11 | Latensi arah 1 tidak melampaui 2 detik dan arah 2 tidak melampaui 3 detik pada jalur *on-device* (5 detik cadangan); TTS di bawah 100 ms; *parsing* UDP di bawah 0,2 ms; memori server di bawah 40 MB; suara Indonesia tersedia atau peralihan dilaporkan | Beralih ke mesin *on-device* alternatif, lalu server lokal atau awan; melampaui berarti temuan |",
  "| G3 | Integrasi Rust dan mesin ucapan, M11 | Latensi arah 1 tidak melampaui 2 detik dan arah 2 tidak melampaui 3 detik pada jalur utama server lokal (5 detik untuk jalur cadangan *on-device*); TTFA TTS di bawah 100 ms pada frasa uji paling banyak lima kata; *parsing* UDP di bawah 0,2 ms; memori server di bawah 40 MB; suara Indonesia tersedia atau peralihan dilaporkan | Beralih ke mesin alternatif, lalu jalur *on-device* ponsel atau awan; melampaui berarti temuan |",
  1, "F-5 Tabel 3.5 G3 TTFA")

# Tabel 3.7: baris 6, 7 diperbarui; baris 17 diperbarui; baris 19-20 baru
E("| 6 | Bentuk masukan *encoder*, rancangan adapter masukan, dan panjang jendela T | Hasil audit T0 | [PERLU VALIDASI: bentuk masukan checkpoint dan rancangan adapter] |",
  "| 6 | Pilihan jalur masukan *encoder* (fitur turunan atau adapter), parameter normalisasi masukan, dan panjang barisan T | Hasil audit T0 dan gerbang G0b | [PERLU VALIDASI: parameter normalisasi masukan checkpoint; keputusan jalur G0b; finalisasi T dari data pilot] |",
  1, "Tabel 3.7 baris 6")
E("| 7 | Sistem koordinat target regresi, keluaran per bingkai atau satu pose, skala acuan d~ref~, dan ambang α | Sebelum pelatihan | [PERLU VALIDASI: sistem koordinat, bentuk keluaran, dan ambang PCK] |",
  "| 7 | Sistem koordinat target regresi, skala acuan d~ref~, dan ambang α | Sebelum pelatihan | [PERLU VALIDASI: sistem koordinat dan ambang PCK] |",
  1, "Tabel 3.7 baris 7")
E("| 17 | Mesin TTS *on-device* final, layanan ASR, dan frasa uji | Pada G3 | [PERLU DATA: keputusan mesin, layanan, dan daftar frasa dari uji banding] |",
  "| 17 | Lokasi sintesis dan pemutaran TTS (keputusan D3: server lokal utama, ponsel cadangan), mesin final, layanan ASR, dan frasa uji | Pada G3 | [PERLU DATA: keputusan final lokasi, mesin, layanan, dan daftar frasa dari uji banding] |",
  1, "Tabel 3.7 baris 17 (D3)")
E("| 18 | Kuesioner, rubrik validator dan pakar, serta asumsi biaya G4 | Sebelum T4 | [PERLU DATA: butir kuesioner, rubrik, batas kesesuaian, harga dan asumsi] |",
  "| 18 | Kuesioner, rubrik validator dan pakar, serta asumsi biaya G4 | Sebelum T4 | [PERLU DATA: butir kuesioner, rubrik, batas kesesuaian, harga dan asumsi] |\n| 19 | Model *deployment* (Pilihan 1: klasifikator saja; Pilihan 2: dua kepala aktif) | Tujuan eksperimen dan hasil ablasi manfaat regresi | [PERLU DATA: keputusan dan dasarnya] |\n| 20 | Akhiran judul (PEMROSESAN SERVER atau CLOUD PROCESSING) | Kesesuaian dengan arsitektur aktual yang berpusat di server | [PERLU DATA: keputusan akhiran judul bersama pembimbing] |",
  1, "Tabel 3.7 baris 19-20 (D2, D1)")

# Batasan no. 5 diselaraskan dengan kontrak terkunci
E("5. *Encoder* murid memakai *checkpoint* terpralatih `ruvnet/wifi-densepose-pretrained` dengan *embedding* 128 dimensi dan 9.280 parameter [11]; *encoder* dibekukan pada baseline, sedangkan LoRA dan pelatihan lanjutan diperlakukan sebagai eksperimen pembanding; bentuk masukan *checkpoint*, yang kartu modelnya mencatat delapan fitur turunan, diaudit pada T0 dan adapter masukan disiapkan jika bentuknya tidak sesuai jendela CSI [PERLU VALIDASI: bentuk masukan checkpoint dan rancangan adapter].",
  "5. *Encoder* murid memakai *checkpoint* terpralatih `ruvnet/wifi-densepose-pretrained` dengan *embedding* 128 dimensi dan 9.280 parameter [11]; *encoder* dibekukan pada baseline, sedangkan LoRA dan pelatihan lanjutan diperlakukan sebagai eksperimen pembanding; masukan *checkpoint* berupa delapan fitur turunan per jendela satu detik disesuaikan lewat jalur fitur turunan atau adapter masukan yang dipilih pada gerbang G0b [PERLU VALIDASI: parameter normalisasi masukan dan keputusan jalur G0b].",
  1, "Batasan no.5 kontrak terkunci")

# Log Perubahan gelombang 17
LOG = """
## Log Perubahan — Revisi 14 November 2026, gelombang 17 (revisi terarah v16 ke v17: kontrak input, supervisi, persamaan, deployment, audio, parameter)

Permintaan: evaluasi kritis pemilik atas v16 (kesesuaian visi 8,5 dari 10; kesiapan metodologi 6 dari 10, penilaian kualitatif) dengan lima kelompok masalah dan delapan temuan tambahan; revisi bersifat aditif dan terarah mengikuti enam langkah, tanpa menulis ulang bab; dokumen kerja: Dokumen-Revisi-Terarah-SenseSIBI-v16-ke-v17.pdf; kaidah bahasa mengikuti skill sempro-mepet (register baku naskah akademik).

- D1 (judul): akhiran judul diputuskan "PEMROSESAN SERVER" dan disatukan ke H1, tabel identitas, dan sampul (sampul memang sudah memakai frasa itu; H1 dan tabel identitas yang diselaraskan; rekomendasi dokumen revisi: arsitektur v16 berpusat di server); keputusan dicatat pada Tabel 3.7 no. 20.
- Langkah 1 (kontrak input): 2.4 kalimat terakhir paragraf pertama diganti blok A-1 (himpunan tetapan terlatih utuh + kontrak masukan (B, 8) per jendela 1 detik + penanda normalisasi masukan); paragraf baru A-2 (delapan fitur sebagai kontrak lingkungan, bukan kontrak artikulasi; hipotesis diuji G0b); Tabel 2.2 sel masukan diperbarui; 3.7 paragraf "encoder diterapkan pada tiap bingkai" diganti A-3 (tiga tingkat: bingkai CSI, jendela fitur 1 detik, langkah embedding; encoder per jendela, bukan per bingkai) + A-4 (jendela bergulir H = 0,25 detik; J/Z dibaca dari barisan langkah); 3.2 daftar audit T0 ditambah parameter normalisasi masukan; Batasan no. 5 diselaraskan (jalur dipilih pada G0b).
- Langkah 2 (supervisi): 2.9 paragraf baru B-1 (label kelas dari protokol perekaman; guru menyumbang deret keypoint; penanda kelas J/Z pada model juara WPC) + kalimat B-2 (angka mAP50 0,9580 dan akurasi 97,6% terbatas 24 huruf statis pada data visual); 3.7 B-3 (keluaran kelas guru hanya pembanding penyaringan kualitas); rumusan no. 1 dan tujuan no. 1 diselaraskan (label kelas dari protokol); Tabel 2.4 baris 5 dibatasi 24 huruf statis; 3.1 kalimat inti pelatihan diselaraskan.
- Langkah 3 (persamaan/temporal): Persamaan 2.15 diganti 2.15′ (Θtrain = {φadapter, θtemporal, θc, θr}, θencoder = θ0) dengan klausa kehadiran φadapter hanya jika jalur adapter terpilih; paragraf modul temporal 2.8 diganti C-2 (keadaan tersembunyi per langkah h1–hT; kepala klasifikasi lewat ringkasan beratensi; kepala regresi per langkah Qt = reshape(Wr·ht + br, 21, 2) dengan Wr 42 × 128; varian peringkas tunggal Persamaan 2.11 menjadi ablasi; agregasi statistik hanya jalur klasifikasi); rujukan Persamaan 2.11 pada 2.7 disesuaikan (varian ablasi vs varian utama per langkah); C-3 (T = 16 langkah, padding nol + mask valid, resampling ditolak untuk J/Z) dan C-4 (resampel keypoint ke pusat jendela; interpolasi balik ke laju kamera untuk pelaporan) masuk 3.7; 2.17 kerangka dan Gambar 2.2 (EMT per langkah jendela; HRG per langkah) diselaraskan.
- Langkah 4 (deployment): 3.7 kalimat deployment diganti D-1 (Pilihan 1: graph = encoder + adapter + modul temporal + kepala klasifikasi; kepala regresi dilepas setelah pelatihan; Pilihan 2 terbuka via Tabel 3.7); Gambar 3.5 (simpul model dan keluaran hanya label + skor) serta keterangannya disesuaikan D-2; kalimat "keluaran tambahan" 3.5 diganti pernyataan Pilihan 1; klausul MPJPE/PCK sebagai metrik pemantauan ditambah di 2.14; baris Tabel 3.7 no. 19 (model deployment) baru.
- Langkah 5 (audio): dua paragraf alur arah 3.5 diganti E-1 (label via UDP ke server Rust sebagai telemetri; TTS Kokoro di server lokal; audio dialirkan ke speaker node RX; arah 2 audio via server ke ASR awan/faster-whisper; saat luring kedua arah tetap jalan); Gambar 3.3 dirakit ulang (server Rust menjadi simpul orkestrasi utama; TTS ponsel menjadi cadangan); Tabel 3.1 baris 4, 7, 8 diperbarui E-2; Batasan no. 6, 2.11, 2.13, paragraf topologi dan paragraf Rust/TTS 3.5, Tabel 2.4 baris 2, Tabel 3.2 baris 8 dan 10, Gambar 3.1 (T2B, T4, G3), Tabel 3.6 baris 5 diselaraskan dengan keputusan D3; Tabel 3.7 no. 17 memuat D3.
- Langkah 6 (parameter/temuan): definisi Delta-CSI diperbaiki ke koefisien kanal kompleks dengan varian amplitudo sebagai pembanding (F-1); beban perekaman (780 repetisi per sesi, 65 menit perekaman murni, sekitar 97 menit per sesi, blok sepuluh menit dengan jeda tiga menit, paling banyak dua sesi per hari) masuk 3.6 (F-3); kriteria G1 diperkuat (F1 makro 0,45, tanpa kelas recall nol, recall J/Z terpisah) pada Tabel 3.5 dan 3.8.2 (F-4); target TTS didefinisikan sebagai waktu menuju audio pertama (TTFA) pada 3.5, baris G3 Tabel 3.5, dan 3.8.4 (F-5); batas klaim populasi masuk Batasan no. 11 dan 3.8 (F-2); framing uji kegunaan skala kecil masuk 3.8.5 (F-6); sub-gerbang G0b (probe linear dengan dua kontrol, ambang F1 makro 0,30 dan tiga kali acak, probe J-Z 70%, dinilai atas data pilot sekitar 97 menit) baru pada 3.7, Tabel 3.5, Gambar 3.1, dan 3.2 (A-5).
- Verifikasi: sitasi tetap [1] sampai [28] monoton urut kemunculan; penanda PERLU VALIDASI bertambah dua (kelas J/Z model juara WPC; parameter normalisasi masukan); delapan pagar klaim v16 (encoder beku baseline, guru hanya akuisisi, 1D-CNN via ablasi, MM-Fi pembanding, ADR Proposed, tanpa klaim hasil, keputusan terbuka diputuskan data, ruang lingkup tetap) dipertahankan; seluruh angka baru (780, 65, 97, 16, 0,25, 0,30, 0,45, 70%) diperiksa aritmetikanya; "bila" tidak dipakai di badan naskah; tanpa em dash prosa baru.
"""
E("## Log Perubahan — Revisi 13 November 2026, gelombang 16 (revisi additif: dua kepala tugas pada encoder CSI terpralatih)",
  LOG.strip("\n") + "\n\n## Log Perubahan — Revisi 13 November 2026, gelombang 16 (revisi additif: dua kepala tugas pada encoder CSI terpralatih)",
  1, "Log gelombang 17")

# ============ terapkan ============
gagal = []
for old, new, n, label in edits:
    c = s.count(old)
    if c != n:
        gagal.append((label, c, n))
        continue
    s = s.replace(old, new)

if gagal:
    for label, c, n in gagal:
        print(f"GAGAL: {label}: kemunculan {c}, harus {n}")
    raise SystemExit(1)

DST.write_text(s, encoding="utf-8")
print(f"OK: {len(edits)} suntingan diterapkan -> {DST}")
print(f"Karakter: {len(s)} (v16: {len(SRC.read_text(encoding='utf-8'))})")
