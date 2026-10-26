# -*- coding: utf-8 -*-
"""Benih komponen mudah-mutasi dossier bahan Translator SIBI (bagian 1).

Empat komponen pertama: ringkasan, arah_latar, peta_masalah, konsep_alat.
Semua fakta tertelusur ke Proposal-Revisi / Matriks / Audit (Task 17).
"""

RINGKASAN = """1. **Topik berganti arah, bukan tambal sulam.** Bahan kerja bergerak dari alat latihan satu arah bagi pembelajar pendengar menjadi purwarupa penerjemah dua arah yang portabel berbasis 2–3 modul ESP32-S3. Perangkat keras, rumusan masalah, arsitektur, dan seluruh kit penulisan pada dossier ini mengikuti kerangka baru; dokumen pendahulu (23 Oktober 2026) tetap berguna sebagai kontras keputusan, bukan sebagai sumber klaim utama.
2. **Arah pertama: SIBI menjadi teks dan suara.** Modul pemancar dan modul penerima mengapit zona isyarat; modul penerima menangkap CSI lalu menjalankan inferensi model int8 langsung pada perangkat. Label beserta skor keyakinannya dikirim melalui User Datagram Protocol (UDP) ke server lokal laptop; server mencocokkan label ke kamus, lalu TTS menyuarakan kalimat Indonesia pada speaker modul.
3. **Arah kedua: ucapan atau teks menjadi representasi SIBI.** Mikrofon I2S (antarmuka audio digital) modul mengalirkan audio ke server; ASR faster-whisper mengenali ucapan menjadi teks. Teks dinormalisasi lalu dipetakan ke kamus kata-level dengan fallback ejaan jari (26 huruf dan 9 angka) yang ditampilkan pada layar modul.
4. **Peran kamera dan YOLO26 dipatok ketat.** Model pose YOLO26 (17 keypoint COCO, tanpa jari) hanya berjalan luring di laptop pada jalur pelabelan dataset riset mengikuti pola ADR-079; produk akhir tidak memakai kamera maupun citra, dan tidak ada model visi pada modul.
5. **Server lokal dipisahkan dari cloud jarak jauh.** Laptop ASUS TUF Dash F15 FX516PR menjadi mesin pelatihan sekaligus server lokal prototipe (RuView + faster-whisper + MMS-TTS-ind + kamus) pada satu kanal dengan modul dan dapat berjalan lewat hotspot tanpa internet. Layanan cloud dibahas sebagai alternatif skalabel dan tidak diuji pada prototipe.
6. **Kebaruan bersifat kombinatif dan dibatasi preseden.** Dalam batas penelusuran hingga Oktober 2026 belum ada publikasi CSI untuk SIBI maupun purwarupa dua arah CSI + TTS/ASR Indonesia pada ESP32-S3. WiSign telah mengenali kalimat American Sign Language (ASL) kontinu, dan KASIBI serta OpenSIBI telah membangun arah balik kata-level sehingga klaim kontinu dan klaim kebaruan arah balik tidak dibuat.
7. **Kelayakan berlapis, bukan asumsi.** Audit menempatkan empat komponen layak terverifikasi dan empat layak bersyarat, sementara pengenalan isyarat SIBI dari CSI menjadi inti riset yang belum terbukti dan "dua arah sebagai satu produk mulus" menjadi keputusan desain yang dibatasi klaim. Karena itu seluruh tahapan ditutup gerbang keputusan G0–G4.
8. **Teknologi ucapan sudah diaudit ke sumber primer.** TTS utama adalah model MMS-TTS-ind (Massively Multilingual Speech) yang berjalan lokal dengan lisensi CC-BY-NC 4.0 dicatat sebagai batas pemakaian; Google dan Azure menjadi pembanding berbayar. Kokoro tercatat tidak mendukung Bahasa Indonesia sehingga tidak dipakai. ASR memakai faster-whisper yang pada GPU kelas RTX 3070 8 GB menghabiskan sekitar 2,9 GB VRAM dalam mode int8 dan bekerja sekitar tiga belas kali lebih cepat daripada waktu nyata.
9. **Batas MVP mengikat semua klaim.** Pengenalan terbatas pada 5–8 isyarat SIBI terisolasi yang dibedakan lintasan lengan, tubuh atas, atau kepala; sistem bukan penerjemah kalimat; konfigurasi jari dan ekspresi wajah tidak dikenali; posisi produk adalah sarana bantu komunikasi dan pembelajaran kosakata terbatas pada konteks pendidikan formal, bukan pengganti juru bahasa.
10. **Posisi SIBI dibuka sejak awal.** Survei Badan Riset dan Inovasi Nasional (BRIN) mencatat pemakaian Bahasa Isyarat Indonesia (BISINDO) sebesar 77,7% dan SIBI 1,9% pada sampel purposive; survei Mursita mencatat 91% responden memakai BISINDO harian; pembelaannya: SIBI hidup di jalur pendidikan formal yang memang menjadi konteks pemakaian purwarupa, arsitektur dibuat bahasa-agnostik, dan validator penutur tunarungu wajib terlibat sejak kurasi.
11. **Metode bergerbang dengan jaring pengaman.** Enam tahap T0–T5 berjalan empat belas minggu dengan gerbang bertanggal dan alternatif cadangan A–D yang mempersempit klaim tanpa mengubah rumusan masalah; kegagalan gerbang dilaporkan sebagai temuan kelayakan, bukan kegagalan skripsi.
12. **Yang menunggu manusia tetap menunggu.** Dua puluh lima butir keputusan (daftar isyarat, ambang gerbang, kanal dan jarak antarmodul, model layar-audio-baterai final, ukuran ASR dan pilihan TTS, frasa uji, kuesioner, rubrik validator, mitra, etika) dibukukan pada Tabel 3.6 proposal dan dirangkum pada seksi keputusan dossier ini; tidak satu pun diisi tebakan.
"""

ARAH_LATAR = """### 1.1 Prinsip penyusunan (berubah dari topik lama)

Lima prinsip mengikat seluruh latar belakang. Pertama, corong dibuka dari masalah manusia dua arah — keluarga, sekolah, layanan publik — dan teknologi hanya muncul di lapisan akhir sebagai cara, bukan pembuka. Kedua, "dua arah" adalah bagian dari masalah sejak paragraf kedua, bukan fitur tambahan: penutur tunarungu menyampaikan lewat isyarat sementara lawan bicara pendengar membalas lewat ucapan, dan kedua arah sama-sama tersendat bila tak ada jembatan bersama. Ketiga, setiap klaim angka memakai bank fakta seksi 3 dengan status verifikasi dan keterbatasan sampelnya (survei BRIN purposive, data orang tua dari Amerika Serikat). Keempat, posisi SIBI versus BISINDO dibuka sendiri sebelum ditanya penguji. Kelima, setiap janji teknis dibingkai sebagai hipotesis yang diuji lewat gerbang, bukan keunggulan yang dirunut mundur.

### 1.2 Kerangka empat paragraf (muara ke rumusan)

**Paragraf 1 — keluarga dan kesenjangan dua arah.** Buka dengan fakta bahwa sebagian besar anak tunarungu lahir di tengah keluarga pendengar: Mitchell dan Karchmer [1], [2] mencatat 90–95% (data siswa AS) sekaligus membantah mitos sepuluh persen; kejujuran mengharuskan mencatat bahwa angka Indonesia belum ditemukan pada penelusuran hingga Oktober 2026. Orang tua yang belajar isyarat membutuhkan dukungan terstruktur [3] dan menghadapi hambatan praktis [4]. Tutup dengan kelangkaan juru bahasa (sekitar 500 untuk sekitar 1,92 juta tunarungu, atau 1 : 3.840 [5]) dan kewajiban aksesibilitas menurut UU Nomor 8 Tahun 2016 [6]. ID-READY: "Komunikasi antara penutur tunarungu dan lawan bicara pendengarnya bersifat dua arah: keduanya harus menguasai moda lawannya, dan kedua arah sama-sama tersendat apabila jembatannya tidak ada."

**Paragraf 2 — alat yang ada terbelah menurut arah.** Kelompokkan sistem terdahulu menurut arah kerjanya, bukan menurut teknologinya: pada arah balik ada KASIBI (suara ke animasi peraga 3D, skor uji 3,362/4 [12]) dan OpenSIBI (50 kosakata: 9 angka, 26 huruf, 15 kata [13]) — keduanya kamus kata-level yang mengakui sempit; pada arah pengenalan, riset Indonesia bertumpu kamera [14]–[17] dengan kebutuhan pencahayaan dan garis pandang [18], dan kamera yang menyala terus selama percakapan dikaitkan dengan kelelahan nonverbal oleh Bailenson [19]. Muara paragraf: belum ada perangkat yang menyatukan kedua arah pada satu purwarupa tanpa kamera.

**Paragraf 3 — teknologi sebagai jawaban, dengan kejujuran.** Perkenalkan CSI sebagai informasi amplitudo-fase tiap subcarrier yang berubah oleh gerak tubuh [20]; preseden SignFi (276 isyarat ASL [21]) dan WiSign (kalimat ASL kontinu [24] — batas klaim kebaruan); bukti kepekaan gerak halus WiKey [25] dan Mosleh [26] sebagai dasar hipotesis gerak lengan, bukan jari. Lalu ESP32-S3: CSI resmi [27], koeksistensi radio pada satu chip terbukti di firmware RuView [28], dan tolok ukur inferensi tepi (ESP-NN 54 ms [30]; ESP-DL 69,2 ms [31]). Tutup dengan audit ucapan: Whisper mendukung Indonesia [32], faster-whisper cepat di GPU 8 GB [33], MMS-TTS-ind jalan lokal [34], [35].

**Paragraf 4 — posisi dan komitmen.** Nyatakan pilihan SIBI beserta angkanya (BISINDO 77,7%, SIBI 1,9% [8]; 91% pemakai harian [9]) dan pembelaannya (jalur pendidikan formal [10], [11]; arsitektur bahasa-agnostik). Kunci janji: studi kelayakan kosakata terbatas dengan validator penutur tunarungu di dalam proyek, latensi diukur bukan dijanjikan, setiap tahap bergerbang. ID-READY: "Berdasarkan uraian tersebut, penelitian ini merancang bangun purwarupa penerjemah dua arah isyarat SIBI berbasis Wi-Fi CSI pada modul ESP32-S3 dan menguji kelayakannya sebagai alat bantu komunikasi kosakata terbatas pada konteks pendidikan formal."

Dua visual menopang corong ini: Gambar 1.1 (peta masalah empat kesenjangan menuju posisi penelitian) dan Gambar 1.2 (visi purwarupa dua arah tanpa kamera).

### 1.3 Anti-pola (jangan tulis)

- Membuka dengan definisi CSI atau keunggulan ESP32 — membalik urutan masalah.
- Klaim penerjemahan kalimat penuh atau pengenalan isyarat kontinu tidak dibuat (WiSign sudah ada untuk ASL; SLMT kalimat masih masalah terbuka [43]).
- Janji pengenalan bentuk jari atau ekspresi wajah dari CSI tidak dibenarkan resolusi fisika (lihat seksi 2).
- Menyembunyikan angka 1,9% atau mengaburkan keterbatasan sampel survei BRIN.
- Memposisikan produk sebagai pengganti juru bahasa atau alat komunikasi komunitas tunarungu sehari-hari (kebutuhan sehari-hari mereka lebih dekat ke BISINDO).
- Menjanjikan angka akurasi atau latensi; parameter itu diukur dan dilaporkan, ambangnya ditetapkan sebelum pengukuran.
- Memakai kembali kerangka "alat latihan umpan balik bagi pembelajar" dari dossier lama sebagai muara utama — kerangka pembelajar kini menjadi salah satu manfaat, bukan identitas produk.
"""

PETA_MASALAH = """### 2.1 Masalah lapangan yang dijawab purwarupa

1. **Kesenjangan komunikasi dua arah di keluarga dan sekolah.** Sebagian besar anak tunarungu tinggal bersama keluarga pendengar yang belum menguasai isyarat (F1) sehingga percakapan harian bergantung pada kemauan kedua pihak menembus moda yang berbeda; siswa tunarungu memakai SIBI di sekolah [11] sementara lawan bicara pendengarnya belum tentu bisa membalas dalam representasi yang bisa dibaca siswa.
2. **Kelangkaan juru bahasa di layanan publik dan pendidikan.** Rasio sekitar 1 : 3.840 [5] membuat kehadiran juru bahasa pada kegiatan belajar harian bukan hal yang bisa diandalkan; purwarupa diposisikan sebagai pelengkap pada kosakata terbatas, bukan pengganti profesional.
3. **Alat bantu yang ada terbelah menurut arah dan moda.** Arah balik hanya diwakili kamus kata-level (KASIBI, OpenSIBI 50 kosakata [12], [13]); arah pengenalan didominasi kamera yang menuntut pencahayaan dan garis pandang [18]; belum ada purwarupa dua arah yang menyatu, murah, portabel, dan bebas kamera saat dipakai.
4. **Hambatan pemakaian kamera selama percakapan.** Kamera yang terus menyala dikaitkan dengan kelelahan nonverbal [19] dan menuntut kondisi ruang; persepsi kenyamanan pengguna CSI (yang justru bebas kamera) ditanyakan terbuka pada uji kegunaan, bukan diasumsikan.

### 2.2 Celah riset yang bisa dipertahankan

1. Dalam batas penelusuran Google Scholar, Crossref, dan OpenAlex hingga Oktober 2026 (kata kunci Inggris dan Indonesia, metodologi pada Matriks), belum ditemukan publikasi pengenalan isyarat SIBI dari Wi-Fi CSI.
2. Belum ditemukan pula purwarupa penerjemah dua arah yang memadukan penginderaan CSI dengan TTS dan ASR Bahasa Indonesia pada perangkat ESP32-S3.
3. Kebaruan bersifat kombinatif: CSI untuk SIBI + inferensi tepi pada modul + integrasi dua arah dengan pemrosesan bahasa Indonesia pada server lokal. Klaim pengenalan kontinu tidak dibuat (WiSign [24] lebih dulu untuk ASL); klaim kebaruan arah balik tidak dibuat (KASIBI dan OpenSIBI lebih dulu, kata-level); klaim penerjemahan kalimat tidak dibuat (masalah terbuka [43], [44]).
4. Lapisan kegunaan jarang dilaporkan riset CSI — latensi ujung ke ujung per arah, cakupan kamus, keandalan operasional, dan penilaian validator penutur menjadikan kontribusi praktis yang terukur.

### 2.3 Masalah teknis yang ditulis jujur sejak proposal

1. **Resolusi fisika.** Panjang gelombang Wi-Fi 2,4 GHz sekitar 12,5 cm membatasi resolusi spasial; dengan satu tautan antarmodul, konfigurasi jari dan ekspresi wajah tidak dianggap dapat dibedakan secara andal sehingga cakupan pengenalan dibatasi lintasan lengan, tubuh atas, dan kepala; asumsi ini diperiksa pada uji Delta-CSI (G0).
2. **Perangkat berbeda dari preseden.** SignFi memakai Intel 5300 tiga antena, Wi-SL memakai dua pemancar tiga penerima pada 400 Hz; modul ini SISO 1T1R berantena tunggal — angka preseden dikutip untuk konteks, tidak diproyeksikan.
3. **Laju cuplik menyempit.** Firmware membatasi pengiriman hingga sekali tiap 20 ms (maksimum 50 bingkai per detik) padahal pita Doppler 1–60 Hz idealnya menuntut 120 Hz menurut kriteria Nyquist; pita per subcarrier yang bisa dianalisis dibatasi setengah laju terukur dan pembatasan ini dilaporkan.
4. **Koeksistensi radio berpamu.** CSI promiscuous + station + UDP (+ streaming audio arah kedua) pada satu chip menuntut satu kanal, filter paket kelompok MGMT, dan WIFI_PS_NONE; pola ini terbukti di firmware RuView, tetapi beban gabungannya diukur ulang pada T0.
5. **Belum ada tolok ukur model CSI-isyarat di ESP32-S3.** Pembanding kelas kompleksitas tersedia (ESP-NN 54 ms dengan model 293,5 KB; ESP-DL 69,2 ms gestur tangan), namun waktu inferensi aktual model CSI diukur sendiri pada T2 — klaim inferensi tepi ditopang hasil ukur, bukan tolok ukur orang lain.
6. **Generalisasi lintas domain.** Model CSI mudah overfit terhadap orang dan ruang [39]; karena itu lima skema pembagian data (dalam sesi blok temporal, lintas sesi, lintas partisipan, lintas ruang, pengguna baru) dan strategi Widar3.0 [40] menjadi acuan tanpa janji hasil, dan keputusan cakupan personalisasi diambil hanya setelah G3 terbaca.
7. **Kualitas label guru visi.** YOLO26 bisa gagal mendeteksi orang atau menghasilkan keypoint bergoyang; protokol memuat aturan buang segmen, pencatatan tingkat segmen terbuang, dan pemeriksaan sampel oleh validator tunarungu agar dataset tidak rapi labelnya tetapi salah isinya.
8. **Ketahanan baterai dan aset tampilan.** Arus chip terverifikasi dari datasheet tetapi arus modul lengkap (radio + layar + audio) belum terukur — diukur pada T4 sebelum klaim portabel dibuat; aset representasi per isyarat mahal dibuat (pelajaran OpenSIBI yang berhenti di 50 kosakata) sehingga tampilan utama berupa glos dan gambar konfigurasi dengan ejaan jari sebagai fallback, animasi hanya pengayaan.
"""

KONSEP_ALAT = """### 8.1 Pemetaan masalah ke fitur dan bukti

| Masalah lapangan (seksi 2.1) | Fitur purwarupa yang menjawab | Bukti pada penelitian |
|---|---|---|
| Kesenjangan komunikasi dua arah keluarga/sekolah | Dua arah menyatu: arah 1 mengenali isyarat lalu menyuarakan teks pada speaker modul; arah 2 menangkap ucapan lalu menampilkan representasi SIBI (glos + gambar, fallback ejaan jari) pada layar | Uji klasifikasi G2–G3; uji jalur ucapan dan cakupan kamus; penilaian validator pada G4 |
| Kelangkaan juru bahasa | Pelengkap komunikasi kosakata terbatas pada kegiatan belajar terbimbing — bukan pengganti juru bahasa profesional | Batasan klaim §1.4 proposal; kuesioner kegunaan 3–5 pengguna; rubrik validator |
| Alat bantu terbelah arah dan bergantung kamera | Kedua arah pada satu topologi modul ESP32-S3 + server lokal, seluruh jalur operasional tanpa kamera | Uji koeksistensi radio T0; uji operasional (deteksi palsu per jam, arus modul); diagram G3.2–G3.3 |
| Kamera terasa mengawasi saat percakapan | Produk akhir tanpa kamera; kamera hanya menyala pada sesi pelabelan dataset riset dan dinyatakan tertulis pada formulir persetujuan | Persepsi kenyamanan ditanyakan terbuka pada uji kegunaan; hasil dilaporkan apa adanya |

### 8.2 Skenario pemakaian konkret (ilustrasi BAB I/II)

*Seorang guru pendamping di SLB mitra meletakkan dua modul ESP32-S3 di meja belajar dan menghubungkan semuanya ke hotspot laptop; kamera tidak menyala. Seorang siswa tunarungu mengisyaratkan "terima kasih" di antara kedua modul; layar guru menampilkan teks hasil pengenalan dan speaker modul menyuarakannya. Guru membalas "sama-sama"; mikrofon modul mengirim ucapannya ke server, teksnya ditemukan di kamus, dan layar menampilkan glos beserta gambar konfigurasi tangan isyarat tersebut. Ketika guru mengucapkan kata yang belum ada di kamus, layar beralih menampilkan urutan ejaan jari huruf demi huruf sehingga percakapan tetap berjalan pada kosakata yang ada [PERLU DATA: daftar isyarat SIBI terpilih menunggu kurasi bersama validator].* Skenario ini adalah hipotesis pemakaian yang versi sederhananya diuji pada G4 — keberhasilan pesan tersampaikan, waktu penyelesaian, dan keluaran menyesatkan dicatat — bukan klaim bahwa produk jadi telah ada.

### 8.3 Disiplin klaim (pelajaran riwayat klaim 92,9% RuView yang ditarik)

**Layak ditulis:** "purwarupa penerjemah dua arah kosakata terbatas"; "studi kelayakan"; "dataset CSI berlabel isyarat SIBI yang pertama (dalam batas penelusuran)"; "arsitektur bahasa-agnostik yang dapat diperluas ke BISINDO dengan penggantian dataset dan validasi ulang"; "inferensi model terkuantisasi pada perangkat untuk 5–8 kelas"; "umpan balik komunikasi dua arah pada kosakata terbatas konteks pendidikan formal".

**Tidak layak (setiap butir berikut jangan ditulis tanpa kait negasi):** jangan tulis "penerjemah SIBI penuh"; jangan tulis "penerjemahan kontinu"; jangan klaim "mengenali bentuk jari atau ekspresi wajah dari CSI"; jangan janjikan "akurasi sekian persen"; jangan posisikan produk sebagai "menggantikan juru bahasa"; jangan sebut "alat komunikasi komunitas tunarungu sehari-hari"; jangan ukur "meningkatkan empati" sebagai hasil terukur (komponen empati dari topik lama tidak dioperasionalkan lagi pada kerangka baru; manfaat ditulis sebagai akses komunikasi dan sarana belajar).

Aturan praktis: setiap kali sebuah kalimat memuat kata "mampu", "menjamin", atau "secara akurat", periksa apakah ada hasil ukur atau gerbang yang menopang; bila belum, ganti menjadi "dirancang untuk" atau "diuji pada". Kekuatan klaim mengikuti kekuatan bukti — diduga tidak pernah naik kelas menjadi terbukti.
"""
