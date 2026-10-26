# Dossier Bahan Penyusunan Proposal — Purwarupa Penerjemah Dua Arah SIBI (Topik Diperbarui)

**Dokumen kerja internal pengumpul bahan** — penerus `DPJ-4_Bahan-Proposal-SIBI.md` (23 Oktober 2026) yang masih mengacu topik lama (alat latihan satu arah bagi pembelajar pendengar).
Disusun: 26 Oktober 2026 · Basis: `Proposal-Revisi-Translator-SIBI.md` + `Audit-Arsitektur-Translator-SIBI.md` + `Matriks-Literatur-dan-Bukti.md` + catatan riset `riset-translator-sibi/` (Task 17, 24–25 Oktober 2026).

> **Status keputusan pemilik yang tercatat (visi produk terbaru):**
> 1. Produk berupa purwarupa penerjemah dua arah yang portabel berbasis 2–3 modul ESP32-S3; setiap modul direncanakan memiliki layar kecil, baterai, *speaker*, dan mikrofon.
> 2. Arah pertama: Sistem Isyarat Bahasa Indonesia (SIBI) menjadi teks dan suara Bahasa Indonesia — pengenalan isyarat lewat Wi-Fi *channel state information* (CSI) dengan inferensi berjalan langsung pada modul, hasil dikirim ke server untuk dijadikan teks dan disuarakan sintesis ucapan (*text-to-speech*, TTS).
> 3. Arah kedua: ucapan atau teks Indonesia menjadi representasi SIBI pada layar modul — ucapan dikenali pengenal ucapan otomatis (*automatic speech recognition*, ASR) di server, teks dipetakan ke kamus kata-level dengan *fallback* ejaan jari.
> 4. Model pose YOLO26 hanya dipakai pada tahap riset (pelabelan, ekstraksi informasi gerakan, pembentukan *ground truth*); produk akhir tidak memakai kamera maupun citra, dan modul tidak menjalankan model visi.
> 5. Laptop ASUS TUF Dash F15 FX516PR (Intel Core i7-11370H, RTX 3070 Laptop 8 GB VRAM, RAM 16 GB) menjadi mesin pengembangan, pelatihan, dan server lokal prototipe; layanan *cloud* jarak jauh dibedakan tegas dan tidak diuji pada prototipe.
> 6. Draf `Proposal-Revisi-Translator-SIBI.md` **tidak ditulis ulang** — dossier ini adalah bahan kerja bagi pemilik untuk menulis, menyesuaikan, atau membela naskahnya sendiri.

---


## 0. Ringkasan Eksekutif

1. **Topik berganti arah, bukan tambal sulam.** Bahan kerja bergerak dari alat latihan satu arah bagi pembelajar pendengar menjadi purwarupa penerjemah dua arah yang portabel berbasis 2–3 modul ESP32-S3. Perangkat keras, rumusan masalah, arsitektur, dan seluruh kit penulisan pada dossier ini mengikuti kerangka baru; dokumen pendahulu (23 Oktober 2026) tetap berguna sebagai kontras keputusan, bukan sebagai sumber klaim utama.
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

## 1. Arah Latar Belakang

### 1.1 Prinsip penyusunan (berubah dari topik lama)

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

## 2. Masalah yang Dijawab

### 2.1 Masalah lapangan yang dijawab purwarupa

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

## 3. Bank Fakta Siap Kutip

Nomor dalam kurung siku merujuk Daftar Pustaka `Proposal-Revisi-Translator-SIBI.md`. Status **DV** = terverifikasi (sumber dilihat langsung, 24–25 Oktober 2026, jejak pada `Matriks-Literatur-dan-Bukti.md`); **EST** = estimasi internal yang selalu dilabeli demikian bila dipakai; **XT** = tidak layak kutip (jangan dipakai).

| Kunci | Inti siap tulis | Sumber | Status |
|---|---|---|---|
| F1 orang-tua-pendengar | 90–95% anak tunarungu lahir dari orang tua pendengar (data siswa AS); mengbantah mitos "10% orang tua tuli". Angka Indonesia belum ditemukan pada penelusuran hingga Okt 2026 — ditulis terbuka di naskah | [1], [2] | DV |
| F2 dukungan-belajar | Orang tua pendengar yang belajar isyarat membutuhkan dukungan terstruktur | [3] | DV |
| F3 hambatan-praktis | Orang tua DHH menghadapi hambatan praktis navigasi belajar isyarat | [4] | DV |
| F4 juru-bahasa | Sekitar 500 juru bahasa isyarat untuk sekitar 1,92 juta penyandang tunarungu (±1 : 3.840) | [5] | DV |
| F5 landasan-hukum | UU No. 8/2016 mengakui bahasa isyarat dan mewajibkan aksesibilitas komunikasi | [6] | DV |
| F6 peta-BRIN | BISINDO 77,7%; SIBI 1,9%; campuran 14,9%; lainnya 5,6% — survei daring purposive 26 provinsi (bukan nasional); keterbatasan sampel wajib disebut saat angka dipakai | [8] | DV |
| F7 survei-Mursita | 91% dari 100 responden tunarungu (Jawa–Bali) memakai BISINDO sehari-hari; konsep SIBI dianggap sulit | [9] | DV |
| F8 baku-SIBI | Kamus SIBI 1994 (SK 0190/P/1994); Surat 868/C/U/95 mewajibkan sistem isyarat baku pada SLB komunikasi total; Kamus SIBI Digital tersedia daring (asetnya tak terverifikasi sesi ini — halaman terblokir) | [10], [45] | DV |
| F9 SIBI-di-SLB | Murid SLB N Ogan Ilir memakai SIBI dalam pembelajaran harian | [11] | DV |
| F10 KASIBI | Suara → pengenal ucapan → basis data → animasi peraga 3D; uji kelayakan 3,362 dari 4 | [12] | DV |
| F11 OpenSIBI | Google Speech-to-Text → API model 3D Collada → animasi Android; hanya 50 kosakata (9 angka, 26 huruf, 15 kata); keterbatasan kosakata diakui penulisnya | [13] | DV (PDF penuh) |
| F12 kamera-moda-utama | Riset isyarat Indonesia bertumpu kamera: SLR BISINDO [14]; CNN 26 huruf + 10 angka [15]; 24 huruf statis SIBI MediaPipe 90,85% [16]; TFLite alfabet statis [17]; keberhasilan bergantung pencahayaan dan garis pandang [18] | [14]–[18] | DV |
| F13 kamera-kelelahan | Paparan kamera yang terus menyala dikaitkan dengan kelelahan nonverbal | [19] | DV |
| F14 dasar-CSI | CSI memuat amplitudo dan fase tiap subcarrier yang berubah saat gerak tubuh mengganggu jalur pantulan; gerak menghasilkan komponen Doppler | [20] | DV |
| F15 SignFi | 276 isyarat ASL dari CSI Intel 5300 (3 antena penerima); dalam sesi 98,01% (lab), 98,91% (rumah), 94,81% (campuran) — dikutip untuk konteks multi-antena, bukan proyeksi ESP32 | [21] | DV |
| F16 DF-WiSLR | 49 gestur dikenali tanpa perangkat yang dikenakan | [22] | DV |
| F17 Filipino-SL | Pengenalan Filipino Sign Language dari CSI (preseden bahasa nasional lain) | [23] | DV |
| F18 WiSign | Kalimat ASL kontinu dikenali dari CSI perangkat komersial (segmentasi kepadatan spektrum) — membatasi klaim kebaruan kontinu | [24] | DV |
| F19 WiKey | Ketukan tombol (gerak jari skala sentimeter): deteksi >97,5%, klasifikasi kunci tunggal 96,4% pada kondisi terkendali | [25] | DV |
| F20 napas | Pola pernapasan (gerak dada milimeter) 99,54%; laju napas 98,69% pada kanal cukup baik | [26] | DV |
| F21 esp-csi | CSI didukung resmi seluruh seri ESP32 termasuk S3; kanal HT20 802.11n memuat 56 subcarrier (52 data + 4 pilot) | [27] | DV |
| F22 RuView | Firmware CSI format ADR-018 via UDP; batas kirim 20 ms → maksimum 50 bingkai/detik; kalibrasi ruang 600 bingkai + 8 anchor ±4 menit; segmentasi energi gerak; dashboard web; mode privasi; pipeline kamera–CSI `collect-ground-truth.py` (ADR-079); koeksistensi STA + CSI promiscuous + ESP-NOW pada satu chip (terbukti di firmware, "works on both S3 and C6") dengan tiga syarat: satu kanal, filter paket MGMT, `WIFI_PS_NONE`; ESP-NOW memuat hingga 250 bita per paket | [28] | DV (kode dibaca) |
| F23 datasheet-S3 | Dual-core LX7 240 MHz (instruksi vektor); SRAM 512 KB; ROM 384 KB; PSRAM terpasang s.d. 8 MB oktal; Wi-Fi b/g/n 2,4 GHz tautan tunggal SISO 1T1R | [29] | DV |
| F24 ESP-NN | Person detection 2.300 ms → 54 ms pada S3 (model 293,5 KB, arena 100 KB) | [30] | DV |
| F25 ESP-DL | Model int8 contoh pada S3: hand-gesture 69,2 ms; MobileNetV2 437,9 ms | [31] | DV |
| F26 TFLM | Contoh micro_speech 18,4 KB berjalan penyangga terkendali | [72] | DV |
| F27 Whisper | 100+ bahasa termasuk Indonesia; large-v3 1,55 miliar parameter; turbo 809 juta (±6 GB) | [32] | DV |
| F28 faster-whisper | Tolok ukur RTX 3070 Ti 8 GB: large-v3 int8 ±2,9 GB VRAM; 13 menit audio selesai 59 detik (±13× waktu nyata) | [33] | DV |
| F29 MMS-TTS-ind | Checkpoint TTS Indonesia (VITS), lisensi CC-BY-NC 4.0, dapat dijalankan lokal | [34], [35] | DV |
| F30 Google-TTS | Suara id-ID Standard dan Premium; Standard ±US$4 per juta karakter setelah jatah gratis bulanan | [36] | DV |
| F31 Azure | Suara id-ID-GadisNeural dan id-ID-ArdiNeural | [37] | DV |
| F32 Kokoro | Model card resmi: 8 bahasa dan 54 suara — Bahasa Indonesia tidak termasuk (bukti kehati-hatian pemilihan teknologi) | [38] | DV |
| F33 YOLO26 | Keluarga model visi waktu nyata multi-tugas; model pose terlatih COCO menghasilkan 17 keypoint tubuh per orang tanpa keypoint jari | [41], [42] | DV |
| F34 supervisi-visi | Person-in-WiFi dan DensePose from WiFi = preseden pengetahuan visi untuk model Wi-Fi (kamera aktif hanya saat pelatihan) | [63], [64] | DV |
| F35 parameter-isyarat | Isyarat tersusun atas bentuk tangan, lokasi, gerak, orientasi telapak, dan komponen nonmanual (perbedaan satu parameter mengubah makna) | [46], [47] | DV |
| F36 kata-infleksi | Kata jadian SIBI dikenali dengan HMM; komponen gesturnya diurai karya lanjutan | [74], [75] | DV |
| F37 SLMT-terbuka | Penerjemahan mesin bahasa isyarat tingkat kalimat masih masalah terbuka; mouthing adalah isu kelas satu keterbacaan avatar | [43], [44] | DV |
| F38 ejaan-jari | Alfabet manual: 26 huruf + 9 angka [13]; dataset citra statis riset hanya 24 kelas tanpa J dan Z (keduanya melibatkan gerakan) — 7.582 citra, MobileNetV2 97,10% | [13], [16], [73] | DV |
| F39 angka-2600 | Angka "±2.600 kosakata kamus SIBI" tidak ditemukan sumber layak kutip (DDG, Bing, Crossref, OpenAlex) — jangan dipakai | — | XT |
| F40 Sagawa | Preseden internasional sistem pembelajaran isyarat dengan pengenalan + pembangkitan | [76] | DV |
| F41 lintas-domain | Model CSI mudah overfitting terhadap orang dan ruang; strategi generalisasi dirangkum; Widar3.0 memakai profil kecepatan Doppler | [39], [40] | DV |
| F42 Nyquist | Pita Doppler 1–60 Hz terwakili bila laju pencuplikan ≥ 120 Hz; firmware maksimum 50 bingkai/detik → pita menyempit setengah laju aktual dan dilaporkan | [55], [56], [28] | DV |
| F43 kelayakan-metrik | Desain studi kelayakan bertahap; metrik klasifikasi (akurasi, presisi, recall, F1 makro, confusion matrix); kuesioner skala Likert | [77]–[79] | DV |
| F44 Vosk | Vosk resmi tidak menyediakan model Bahasa Indonesia | riset T17-R1 | DV |
| F45 arus-S3 | Datasheet: arus penerimaan 88–91 mA; pemancaran puncak 283–340 mA — basis estimasi baterai; arus modul lengkap (radio + layar + audio) belum terukur, diukur pada T4 | [29] | DV |

Cara pemakaian: setiap fakta dipakai **tidak melebihi sumbernya**. Angka SignFi/Wi-SL tidak diproyeksikan ke perangkat satu antena; angka WiKey/Mosleh dikutip sebagai bukti kepekaan pada kondisi terkendali, bukan jaminan; survei BRIN dan Mursita selalu disertai keterbatasan sampelnya.

## 4. Bank Rujukan per Kelompok (peta ke Daftar Pustaka Proposal-Revisi)

| Kelompok | Nomor [n] | Peran di naskah |
|---|---|---|
| A — konteks tunarungu, SIBI, hukum | [1]–[11], [45]–[49] | Latar belakang BAB I §1.1–1.2; kajian BAB II §2.1–2.2 |
| B — pengenalan isyarat dari CSI | [20]–[24], [57], [58], [65]–[67] | BAB II §2.3, §2.6; tabel penelitian terdahulu |
| C — sensitivitas gerak halus & lintas domain | [25], [26], [39], [40] | BAB II §2.3 (kepekaan), §2.6 (strategi fitur) |
| D — supervisi visi untuk Wi-Fi | [63], [64] | BAB II §2.5 (preseden peran kamera hanya saat pelatihan) |
| E — visi isyarat Indonesia + pose | [14]–[17], [51]–[53], [60]–[62], [73] | BAB II §2.2, §2.5; pembanding moda kamera |
| F — arah balik teks/suara → isyarat | [12], [13], [19], [43], [44], [50], [74]–[76] | BAB II §2.2, §2.8 (desain arah kedua) |
| G — TTS dan ASR Indonesia | [32]–[38] | BAB II §2.7 (audit teknologi ucapan) |
| H — platform ESP32-S3/RuView + metode + evaluasi | [27]–[31], [54]–[56], [68]–[72], [77]–[79] | BAB II §2.4, §2.6, §2.10; BAB III §3.4, §3.7 |

Dua puluh rujukan baru ditambahkan pada revisi (WiSign, WiKey, Mosleh, Mursita, Picron, Hakozaki, Safrida/Rabit, Rakun, Anggraini, Whisper, MMS, mms-tts-ind, Kokoro, faster-whisper, Google TTS, Azure, datasheet S3, esp-csi, esp-dl, tflite-micro-esp, esp-nn) dan enam rujukan lama dikeluarkan karena melekat pada uji persepsi kamera yang sudah dihapus (Sigrist 2013; Zajonc 1965; Daniel 2024; Hassan 2026; dua entri pendukung). Metadata verifikasi: `scripts/translator-sibi/meta_rujukan_baru.json`.

## 5. Perangkat, Aset, dan Peta Diagram

### 5.1 Perangkat keras (selaras Tabel 3.1 proposal revisi)

| No. | Nama | Spesifikasi | Jumlah | Keterangan |
|---|---|---|---|---|
| 1 | Modul ESP32-S3 | Papan pengembangan S3 dengan PSRAM, varian yang direkomendasikan RuView | 3 unit | Modul TX, modul RX, modul pengguna (bergilir dengan cadangan) |
| 2 | Layar modul | SPI/TFT 1,8–2,8 inci [PERLU DATA: model final] | 1–2 unit | Tampilan representasi SIBI |
| 3 | Antarmuka audio | Mikrofon I2S + speaker dengan penguat I2S (contoh umum: INMP441, MAX98357A) [PERLU DATA: model final] | 1 set | Pintu suara arah kedua dan pemutaran TTS |
| 4 | Baterai modul | Li-ion/Li-Po dengan regulator daya [PERLU DATA: kapasitas berdasar uji arus] | 1–2 set | Ketahanan diukur pada uji operasional |
| 5 | Laptop | ASUS TUF Dash F15 FX516PR: i7-11370H, RTX 3070 Laptop 8 GB VRAM, RAM 16 GB | 1 unit | Pelatihan, server lokal, jalur pelabelan |
| 6 | Access point | Router 2,4 GHz atau hotspot laptop [PERLU DATA: pilihan final] | 1 unit | Seluruh perangkat satu kanal |
| 7 | Webcam | Bawaan laptop | 1 unit | Hanya menyala pada jalur pelabelan dataset riset |

### 5.2 Perangkat lunak (selaras Tabel 3.2 proposal revisi)

Firmware dan server RuView; `scripts/collect-ground-truth.py` (ADR-079, estimator diganti pose YOLO26); model pose YOLO26; Python + scikit-learn + PyTorch; TensorFlow Lite Micro dan ESP-DL; faster-whisper (ASR); MMS-TTS-ind (TTS); layanan TTS awan (opsional pembanding); kamus label-teks dan teks-isyarat (dikembangan sendiri). Versi dicatat bersama log konfigurasi agar eksperimen dapat diulang.

### 5.3 Aset RuView yang dipakai (selaras Tabel 2.1 proposal revisi)

Firmware penangkap CSI (ADR-018, streaming UDP) → aliran CSI dan label; koeksistensi STA + UDP + CSI + ESP-NOW pada satu chip → dasar topologi satu kanal; kalibrasi ruang 600 bingkai + 8 anchor → awal setiap sesi; segmentasi energi gerak → memotong segmen terisolasi; dashboard web → pemantauan sesi riset; mode privasi → membuang fitur biometrik; pipeline ADR-079 → jalur pelabelan dengan estimator diganti YOLO26; modul estimasi pose on-device RuView → **tidak dipakai**. Fungsi yang dipakai diverifikasi ulang pada G0 sebelum perekaman karena RuView tidak melalui telaah sejawat.

### 5.4 Peta diagram (sepuluh visual `diagram/*.mmd`, lolos validasi mmdc)

| Kode | Judul | Lokasi | Tugas argumen |
|---|---|---|---|
| G1.1 | Peta masalah dan kesenjangan | 1.1 | Masalah inti bercabang empat kesenjangan → posisi penelitian |
| G1.2 | Visi purwarupa dua arah tanpa kamera | 1.1 | Modul TX/RX, server lokal, speaker/mikrofon/layar |
| G2.1 | Taksonomi pengenalan dan translasi | 2.2 | Tiga moda pengenalan; tiga tingkat translasi balik |
| G2.2 | Alur arah pertama | 2.7 | ESP-NOW → CSI → segmen → fitur → int8 → label → TTS |
| G2.3 | Alur arah kedua | 2.8 | Dua pintu masuk → ASR → kamus → tampil/ejaan jari |
| G3.1 | Alur pelatihan bergerbang | 3.2 | T0–T5 + G0–G4; YOLO26 hanya di T2 |
| G3.2 | Arsitektur produk akhir tanpa kamera | 3.5.1 | Dua arah resmi; jalur pelabelan putus-putus |
| G3.3 | Topologi jaringan | 3.5.2 | Modul A/B/C, AP satu kanal, server, cloud alternatif |
| G3.4 | Inferensi langsung pada S3 | 3.7.7 | Callback CSI → penyangga PSRAM → int8 → ambang |
| G3.5 | Alur dataset–evaluasi–deployment | 3.8 | Perekaman → penyaringan → 5 skema → metrik → uji |

### 5.5 Tabel gerbang keputusan (selaras Tabel 3.4 proposal revisi)

| Gerbang | Waktu | Ukuran | Kriteria lolos | Tindakan bila gagal |
|---|---|---|---|---|
| G0 | Akhir M2 | Uji Delta-CSI dan koeksistensi | Pola CSI bergerak terpisah dari diam dan kosong; CSI + STA + UDP serentak, kehilangan paket terkendali | Perbaiki penempatan satu kali; gagal lagi → jalur CSI dihentikan, dilaporkan sebagai temuan karakterisasi |
| G1 | M3 | Separabilitas awal 2–3 isyarat (nearest-centroid) | Repetisi isyarat sama lebih rapat sesamanya daripada ke isyarat lain | Ubah penempatan/orientasi satu kali; gagal lagi → tindakan sesuai Tabel 3.6 |
| G2 | M6–M7 | Akurasi skema dalam sesi | Jauh di atas peluang acak (ambang pada Tabel 3.6) | Pangkas ke 3–5 isyarat yang bertumpu lintasan |
| G3 | M10 | Kinerja lintas partisipan dan ruang | Di atas peluang acak | Cakupan menjadi personalisasi per pengguna, ditulis sebagai temuan |
| G4 | M12 | Kelengkapan uji dan persetujuan validator | Data uji operasional, jalur ucapan, cakupan kamus, kegunaan tercatat; validator menyetujui kewajaran keluaran | Hasil negatif tetap dilaporkan sebagai temuan kelayakan |

### 5.6 Risiko dan alternatif cadangan (selaras Tabel 3.7 proposal revisi)

| No. | Risiko | Mitigasi / cadangan |
|---|---|---|
| 1 | Pola CSI isyarat tidak terpisah pada konfigurasi dua modul | Perbaikan penempatan satu kali; bila tetap gagal → dihentikan, dilaporkan sebagai temuan |
| 2 | Akurasi lintas partisipan/ruang rendah | Personalisasi per pengguna (cadangan A) |
| 3 | Model int8 terlalu berat di modul | Klasifikasi dipindah ke server, modul kirim fitur (cadangan B); klaim inferensi tepi jadi hasil uji banding |
| 4 | Beban radio gabungan CSI + UDP + audio bermasalah | Pemisahan peran modul: modul CSI khusus dan modul pengguna khusus (cadangan C) |
| 5 | TTS/ASR lokal terlalu lambat untuk frasa pendek | Turunkan ukuran model ASR atau uji layanan awan sebagai pembanding (cadangan D) |
| 6 | Aset representasi mahal dibuat | Batasi ke glos + gambar konfigurasi + ejaan jari; animasi jadi pengayaan |
| 7 | Ketahanan baterai di bawah target | Ukur arus tiap kondisi, sesuaikan target, laporkan apa adanya |
| 8 | Rekrutmen/etika terlambat | Dua ruang dan pengisyarat cadangan di T1; transisi satu minggu |

## 8. Konsep Penyelesaian: Pemetaan, Skenario, Disiplin Klaim

### 8.1 Pemetaan masalah ke fitur dan bukti

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

## 9. Kit Penulisan BAB I (kalimat ID-READY)

### 9.1 Subbab 1.1 Latar Belakang

Corong empat paragraf sudah dirinci pada seksi 1 dossier ini; bagian berikut memberi bata kalimat ID-READY yang bisa disalin lalu disesuaikan. Pembuka P1: "Sebagian besar anak tunarungu lahir di tengah keluarga pendengar; Mitchell dan Karchmer [1], [2] mencatat proporsi 90–95% pada data siswa Amerika Serikat sekaligus membantah anggapan lama bahwa sepuluh persen orang tua anak tunarungu ikut tunarungu." Jembatan dua arah P1: "Karena orang tua dan saudara pendengar umumnya tidak menguasai isyarat, giliran komunikasi tidak selalu datang: anak menyampaikan lewat isyarat, keluarga membalas lewat ucapan, dan keduanya sama-sama menunggu diterjemahkan." Angka layanan P1: "Di Indonesia, juru bahasa isyarat berjumlah sekitar lima ratus orang untuk sekitar 1,92 juta penyandang tunarungu [5], sementara aksesibilitas komunikasi menjadi kewajiban hukum menurut UU Nomor 8 Tahun 2016 [6]."

Paragraf P2 memetakan sistem terdahulu menurut arah, lalu menutup dengan rujukan Gambar 1.1: "Kesenjangan empat arah tersebut — kelangkaan juru bahasa, kamus satu arah yang sempit, pengenalan bergantung kamera, dan CSI yang belum tersentuh untuk SIBI — dirangkum pada Gambar 1.1." Paragraf P3 memperkenalkan CSI dengan satu kalimat mekanisme sebelum preseden, dan menutup pengantar perangkat dengan dua fakta kelayakan (koeksistensi radio [28]; tolok ukur inferensi [30], [31]). Paragraf P4 menutup corong dengan rujukan Gambar 1.2 dan kalimat komitmen: "Berdasarkan uraian tersebut, penelitian ini merancang bangun purwarupa penerjemah dua arah isyarat SIBI berbasis Wi-Fi CSI pada modul ESP32-S3 dan menguji kelayakannya sebagai alat bantu komunikasi kosakata terbatas pada konteks pendidikan formal."

### 9.2 Subbab 1.2 Rumusan Masalah (salinan final dari proposal revisi)

Pengantar: "Berdasarkan latar belakang yang telah dipaparkan, masalah yang dikaji dalam penelitian ini dapat dirumuskan sebagai berikut."
1. Bagaimana merancang purwarupa penerjemah dua arah SIBI berbasis dua hingga tiga modul ESP32-S3 yang menangkap CSI, melakukan inferensi pada perangkat, dan berkomunikasi dengan server lokal, termasuk protokol perekaman dataset isyarat terisolasi dengan pelabelan berbantuan model pose YOLO26?
2. Bagaimana kinerja pengenalan 5–8 isyarat SIBI terisolasi dari CSI melalui inferensi pada perangkat, serta kinerja jalur isyarat menjadi teks dan suara dan jalur teks atau ucapan menjadi representasi SIBI, pada skenario dalam sesi, lintas partisipan, dan lintas ruang?
3. Bagaimana kelayakan purwarupa sebagai alat bantu komunikasi dua arah kosakata terbatas ditinjau dari latensi ujung ke ujung, cakupan kosakata, keandalan operasional, dan penilaian validator penutur tunarungu?

### 9.3 Subbab 1.3 Tujuan Penelitian (cermin 1:1)

Pengantar: "Berdasarkan rumusan masalah tersebut, penelitian ini bertujuan untuk:" — diikuti tiga butir yang menyalin objek rumusan di atas dengan verba pembuka "Merancang", "Mengukur", dan "Menguji". Aturan cermin: jumlah butir sama, urutan sama, objek sama; tidak ada tujuan yang tidak ditanya rumusannya, dan tidak ada verba kabur seperti "mempelajari lebih lanjut".

### 9.4 Subbab 1.4 Batasan Masalah (sembilan pagar, salin dari proposal §1.4)

Kesembilan pagar itu: (1) objek pengenalan 5–8 isyarat terisolasi yang lolos dua saringan — separabilitas fisik lintasan lengan/tubuh atas/kepala dan validitas pedagogis bersama validator serta Kamus SIBI [45]; (2) konfigurasi jari dan ekspresi wajah tidak dikenali pada kedua arah; (3) perangkat 2–3 modul ESP32-S3 berlayar-baterai-speaker-mikrofon plus laptop sebagai mesin pelatihan dan server lokal; (4) kamera dan YOLO26 hanya pada jalur pelabelan dataset riset; (5) ASR berbasis Whisper dan TTS lokal MMS dengan pembanding awan, pilihan final pada T4; (6) arah kedua berupa kamus kata-level dengan fallback ejaan jari; (7) satu pengisyarat per sesi, sedikitnya dua ruang mitra terkalibrasi; (8) uji pengguna 3–5 orang analisis deskriptif; (9) di luar cakupan: pengenalan kontinu, penerjemahan kalimat bertata bahasa penuh dengan penanda nonmanual, BISINDO, dan penerapan cloud jarak jauh pada prototipe. Redaksi final per butir disalin apa adanya dari proposal revisi supaya angka tidak bergeser. [PERLU DATA: konfirmasi pembimbing atas sembilan pagar bila lingkup mitra berubah]

### 9.5 Subbab 1.5 Manfaat Penelitian

Pilih satu bentuk, jangan campur. Bentuk terpilih proposal: teoretis-praktis. Bata teoretis: bukti awal kelayakan pengenalan sekelompok kecil isyarat SIBI dari CSI satu tautan antarmodul beserta kelayakan inferensi terkuantisasi pada perangkat; dataset CSI berlabel dan protokol yang bisa dipakai peneliti lain termasuk untuk perluasan ke BISINDO; dokumentasi arsitektur tepi-server yang dapat ditelusuri ulang. Bata praktis: bagi lembaga mitra — gambaran kelayakan alat bantu komunikasi dua arah SIBI pada kegiatan pembelajaran dan protokol kurasi kosakata bersama validator; bagi keluarga siswa — kosakata tervalidasi penutur tunarungu sesuai jalur pendidikan formal; artefak tetap dihasilkan walau gerbang berhenti lebih awal (laporan karakterisasi, protokol, atau dataset). Manfaat tidak boleh melebihi tujuan.

### 9.6 Subbab 1.6 Sistematika Penulisan

Satu baris per bab, kala kini: BAB I memuat latar belakang sampai sistematika; BAB II memuat kajian bahasa isyarat dan SIBI, kebutuhan dua arah dan sistem terdahulu, CSI, ESP32-S3 dan RuView, peran YOLO26 sebagai alat bantu pelabelan riset, pengenalan isyarat berbasis CSI dan inferensi tepi, TTS-ASR Indonesia, pemetaan teks ke representasi SIBI, komunikasi perangkat-server, evaluasi kelayakan, dan penelitian terdahulu; BAB III memuat desain, tahapan bergerbang, waktu-lokasi, alat-bahan, perancangan, protokol dataset dan etika, pengolahan sinyal sampai deployment, skenario pengujian dan metrik, jadwal, parameter yang ditetapkan kemudian, serta risiko dan cadangan. [PERLU DATA: kepastian jumlah bab akhir sesuai pedoman kampus sebelum baris BAB IV–BAB V ditulis]

### 9.7 Catatan pemakaian kit

Nomor rujukan [n] pada kit ini mengikuti urutan Daftar Pustaka proposal revisi; bila urutan berubah karena penyuntingan, perbarui nomor sebelum menempel. Kalimat berfrasa kunci (misalnya "kosakata terbatas", "inferensi pada perangkat", "validator penutur tunarungu") tidak boleh diparafrasekan tanpa memeriksa konsistensi dengan rumusan, batasan, dan judul. Setiap angka pada kit bersumber dari bank fakta seksi 3; menambah angka baru tanpa status verifikasi dilarang.

## 10. Kit Penulisan BAB II dan BAB III

### 10.1 Kerangka BAB II (sebelas subbab, urutan mengikuti proposal revisi)

2.1 Bahasa isyarat dan SIBI (parameter isyarat [46], [47]; peta pemakaian [8], [9]; Kamus SIBI [45]) · 2.2 Kebutuhan komunikasi dua arah dan sistem terdahulu (kelompok menurut arah; taksonomi Gambar 2.1) · 2.3 Wi-Fi CSI (mekanisme, amplitudo-fase, Doppler, kepekaan halus WiKey-Mosleh, lintas domain, batas resolusi 12,5 cm) · 2.4 Modul ESP32-S3, RuView, dan koeksistensi radio (datasheet; esp-csi; firmware; tiga syarat satu kanal) · 2.5 Estimasi pose berbasis visi sebagai alat bantu pelabelan riset (YOLO26 17 keypoint COCO; Person-in-WiFi dan DensePose sebagai preseden supervisi) · 2.6 Pengenalan isyarat dan gestur berbasis CSI serta inferensi pada perangkat (preseden SignFi-WiSign; fitur; SVM dan 1D-CNN; penolakan; tolok ukur ESP-NN/ESP-DL/TFLM) · 2.7 TTS dan ASR Bahasa Indonesia (audit sumber primer; alur Gambar 2.2; pembagian server lokal dan cloud) · 2.8 Pemetaan teks ke representasi SIBI (kenapa bukan substitusi kata; KASIBI-OpenSIBI; ejaan jari; alur Gambar 2.3) · 2.9 Komunikasi modul, server, dan topologi · 2.10 Evaluasi kelayakan (metrik relatif peluang acak; dimensi tambahan) · 2.11 Penelitian terdahulu (tabel dan sintesis).

### 10.2 Pola blok teori (empat langkah, jangan tumpuk definisi)

Setiap subbab teori berjalan empat langkah: (1) definisi dengan rujukan — "Menurut [Nama] ([tahun]), [istilah] merupakan [definisi]" atau "[Istilah] merupakan [definisi] ([Nama], [tahun])"; (2) dekomposisi — komponen, jenis, atau kriteria: "Komponen [X] menurut [sumber] terdiri atas ..."; (3) prinsip kerja pada konteks penelitian ini — "Prinsip kerja [X] adalah ..."; (4) diskusi relevansi yang wajib menutup blok — "Dalam penelitian ini, [X] digunakan sebagai [peran] karena [alasan yang dikaitkan kebutuhan BAB I]." Definisi cukup satu per konsep; definisi serupa cukup disebut "Definisi serupa dikemukakan oleh [Nama]". Verba pelapor dipilih sesuai perbuatan sumber: mengukur, menemukan, mengusulkan, membandingkan, memperluas, membantah — tidak semuanya "mengatakan". Istilah asing miring pada tiap pemakaian (machine learning, dataset, fallback); istilah serapan KBBI tegak (mikrokontroler, purwarupa).

### 10.3 Penelitian terdahulu: tabel, sintesis, dan celah

Tabel perbandingan (Tabel 2.2 proposal) memuat kolom No., Peneliti (Tahun), Modalitas dan arah, Bahasa isyarat, Bebas kamera saat dipakai, Fokus; tujuh belas barisnya sudah final — salin, jangan rangkum. Sintesis mengelompokkan menurut temuan, bukan menurut sumber. Kerangka ID-READY: "Pengenalan bahasa isyarat dari sinyal Wi-Fi telah dibuktikan pada beberapa bahasa [21], [24], [65], [22], [23], termasuk kalimat kontinu untuk ASL [24]; kepekaan CSI terhadap gerak halus telah diukur hingga skala sentimeter [25] dan milimeter [26]; pengetahuan visi juga telah dipindahkan ke Wi-Fi sebagai supervisi pelatihan [63], [64]. Namun, dari penelitian tersebut belum ada yang menyasar SIBI, dan sistem SIBI yang ada bekerja satu arah — kamus kata-level pada arah balik [12], [13] atau pengenalan berbasis kamera [14]–[17]. Oleh karena itu, penelitian ini menggabungkan penginderaan CSI satu tautan antarmodul untuk SIBI, inferensi pada perangkat ESP32-S3, dan integrasi dua arah dengan TTS dan ASR Bahasa Indonesia pada server lokal." Celah ditulis positif dan spesifik, selalu bisa dilacak ke baris tabel di atasnya; frasa "belum ada penelitian tentang" hanya boleh dipakai karena memang sudah dicari (metodologi penelusuran ada di Matriks).

### 10.4 Kerangka BAB III (sebelas subbab)

3.1 Desain penelitian (studi kelayakan kuantitatif bergerbang; pemetaan rumusan ke tahap) · 3.2 Tahapan penelitian T0–T5 dengan gerbang G0–G4 (Gambar 3.1) · 3.3 Waktu dan lokasi · 3.4 Alat dan bahan · 3.5 Perancangan sistem (arsitektur dua arah Gambar 3.2; topologi Gambar 3.3; penempatan modul; kalibrasi ruang 600 bingkai 8 anchor) · 3.6 Protokol dataset, partisipan, etika · 3.7 Pengolahan sinyal sampai deployment (laju cuplik; segmentasi; fitur; SVM/1D-CNN; lima skema; penolakan; kuantisasi int8; Gambar 3.4) · 3.8 Skenario pengujian dan metrik (Delta-CSI; klasifikasi dengan confusion matrix; operasional latensi-arus; jalur ucapan; cakupan kamus; kegunaan; validator; kriteria gerbang) · 3.9 Jadwal empat belas minggu [PERLU DATA: kalender mulai penelitian untuk mengisi Tabel 3.5] · 3.10 Parameter ditetapkan kemudian (Tabel 3.6) · 3.11 Risiko dan cadangan A–D.

### 10.5 Register prosedural (pola wajib BAB III)

Langkah prosedur memakai bentuk berawalan me- dan ditutup rangkap tiga. Contoh perekaman (salin dari proposal §3.6.3): 1. Menyiapkan peralatan, memasang modul pemancar dan modul penerima, lalu menghubungkan seluruh perangkat ke access point pada satu kanal. 2. Menjalankan kalibrasi ruang dan mencatat metadata sesi. 3. Menjalankan `scripts/collect-ground-truth.py` agar perekaman CSI dan webcam tersinkron. 4. Menampilkan kartu pemandu, merekam satu repetisi, memberi jeda, dan mengulanginya hingga sekitar 30 repetisi per isyarat. 5. Membuang segmen bila orang tidak terdeteksi model pose, keypoint bergoyang ekstrem, atau segmen terpotong, lalu mencatat tingkat penyaringan per isyarat. 6. Meminta validator mengambil sampel segmen. Contoh uji Delta-CSI (§3.8.1): memasang kedua modul; merekam kondisi ruang kosong, pengisyarat diam, pengisyarat bergerak; menjalankan koeksistensi termasuk streaming audio; membandingkan pola antarkondisi sebagai bahan G0. Setiap prosedur ditutup "mengamati, mencatat, dan menganalisis" atau padanannya, dan berhenti di situ — kalimat hasil adalah bahasa BAB IV yang dilarang di proposal.

### 10.6 Pola kalimat rancangan dan rujukan

Walkthrough per interkoneksi: "[Komponen A] terhubung dengan [komponen B] melalui [jalur], yang berfungsi untuk [fungsi data/sinyal]" — satu kalimat per sambungan, urut arah aliran data; untuk topologi dipakai pada Gambar 3.3 (modul A pemancar ESP-NOW, modul B penerima CSI dan inferensi, modul C pengguna layar-speaker-mikrofon, access point satu kanal, server lokal empat layanan, cloud alternatif putus-putus). Pemilihan metode tiga kalimat: nama dan rujukan; alasan cocok dengan karakteristik masalah; peran dalam penelitian ini. Rujukan gambar tiga bentuk sah: "... ditunjukkan pada Gambar 3.x", "Gambar 3.x menunjukkan ...", "... dapat dilihat pada Gambar 3.x" — keterangan gambar di bawah gambar, keterangan tabel di atas tabel, tidak pernah "gambar di bawah ini". Angka dan satuan konsisten antara batasan BAB I dan alat-bahan BAB III (5–8 isyarat, 2–3 modul, 30 repetisi, 600 bingkai, 8 anchor, 250 bita).

### 10.7 Daftar istilah inti (jaga satu istilah per konsep)

modul pemancar (TX), modul penerima (RX), modul pengguna; zona isyarat; gerbang keputusan; penyaringan segmen; glos; ejaan jari; kamus label-teks; inferensi pada perangkat (inferensi tepi); model terkuantisasi int8; laju bingkai; peluang acak; validator penutur tunarungu; pengisyarat kompeten; server lokal; purwarupa. [PERLU DATA: keputusan final penulisan "server lokal" versus "server prototipe" pada seluruh naskah bila pembimbing memilih salah satu]

## 11. Antisipasi Sidang: Pertanyaan dan Jawaban Siap Pakai

**P1 — "Kenapa SIBI, padahal BISINDO yang dipakai komunitas?"**
Jawaban: data BRIN (77,7% BISINDO, 1,9% SIBI, sampel purposive 26 provinsi) dan survei Mursita (91% pemakaian harian) justru kami kutip terbuka di BAB I. SIBI dipilih karena konteks pemakaian purwarupa adalah pendidikan formal — SIBI adalah sistem baku yang diajarkan di jalur itu (Kamus SIBI 1994, Surat 868/C/U/95, temuan SLB Ogan Ilir), bukan karena jumlah penuturnya. Arsitektur kami bahasa-agnostik: perluasan ke BISINDO memerlukan penggantian dataset dan validasi ulang bersama penuturnya, dan itu kami usulkan sebagai penelitian lanjutan.

**P2 — "Kenapa Wi-Fi CSI, bukan kamera?"**
Kamera menuntut pencahayaan dan garis pandang serta menyala terus selama percakapan (dikaitkan kelelahan nonverbal); CSI bekerja tanpa kamera dan tanpa perangkat yang dikenakan. Preseden kelayakannya kuat (SignFi 276 isyarat ASL; WiSign kalimat kontinu; WiKey dan Mosleh untuk gerak halus). Kejujurannya: untuk SIBI belum ada — justru itu yang kami uji lewat gerbang, bukan asumsi.

**P3 — "Kenapa isyaratnya tidak sampai ke jari?"**
Fisika: panjang gelombang 2,4 GHz sekitar 12,5 cm; perangkat kami SISO 1T1R satu antena, berbeda dari perangkat riset multi-antena (Intel 5300 tiga antena; Wi-SL dua pemancar tiga penerima). Preseden kepekaan halus bekerja pada kondisi terkendali dan jarak dekat. Karena itu cakupan kami lintasan lengan, tubuh atas, dan kepala; jari dan wajah ditulis eksplisit sebagai keterbatasan, dan arah kedua justru mengandalkan ejaan jari sebagai fallback yang sah secara kebahasaan.

**P4 — "Apa kebaruan Anda, kalau WiSign sudah mengenali kalimat kontinu?"**
Kebaruan kami kombinatif dan kami batasi presedennya: CSI untuk SIBI (belum ada dalam penelusuran kami), inferensi terkuantisasi pada modul ESP32-S3, dan integrasi dua arah dengan TTS/ASR Bahasa Indonesia pada server lokal. Kami tidak mengklaim kontinu dan tidak mengklaim kebaruan arah balik kata-level (KASIBI dan OpenSIBI lebih dulu).

**P5 — "Apakah sistem ini dimaksudkan menggantikan juru bahasa?"**
Tidak — dan itu tertulis di batasan. Dengan rasio sekitar 1 : 3.840, kebutuhan jembatan sangat nyata, tetapi purwarupa kami hanya pelengkap pada kosakata terbatas untuk kegiatan belajar terbimbing; keputusan layanan publik dan konteks berisiko tetap milik juru bahasa profesional.

**P6 — "Kenapa server laptop, bukan cloud?"**
Prototipe memakai server lokal karena tiga alasan terukur: latensi yang diukur murni berasal dari sistem (bukan jaringan luar), tanpa biaya berlangganan, dan mandiri jaringan lewat hotspot. Cloud jarak jauh kami bahas sebagai alternatif skalabel; latensi layanan ucapan awan dari Indonesia belum terdokumentasi pada sumber yang kami inspeksi sehingga tidak kami jadikan dasar klaim apa pun.

**P7 — "Kenapa TTS-nya bukan Kokoro yang ringan itu?"**
Kami periksa model card-nya: Kokoro v1.0 mendukung delapan bahasa dan Bahasa Indonesia tidak termasuk. Itu contoh kehati-hatian pemilihan teknologi: klaim "multibahasa" diverifikasi ke sumber primer sebelum dipakai. Jalur utama kami MMS-TTS-ind (jalan lokal, lisensi nonkomersial dicatat), dengan Google dan Azure sebagai pembanding.

**P8 — "YOLO26 masuk produk akhir?"**
Tidak. Model pose YOLO26 hanya alat riset pada jalur pelabelan dataset di laptop (pola ADR-079 RuView), keluarannya 17 keypoint tubuh tanpa jari, seluruhnya luring. Produk akhir tanpa kamera dan tanpa model visi — itu sebabnya jalur kamera digambar putus-putus pada arsitektur.

**P9 — "Baterai-nya tahan berapa lama?"**
Belum kami klaim; itu yang membedakan proposal ini dari brosur. Arus chip terverifikasi dari datasheet (penerimaan 88–91 mA; pemancaran puncak 283–340 mA), tetapi arus modul lengkap dengan layar dan audio diukur pada T4, dan ketahanan baterai dilaporkan dari hasil ukur beserta indikator layak yang ditetapkan sebelum pengukuran.

**P10 — "Kalau G0 gagal, skripsinya gagal?"**
Tidak. Desainnya studi kelayakan bergerbang: setiap tahap menghasilkan artefak (laporan karakterisasi sinyal, protokol, dataset, model terdeploy, laporan kelayakan) sehingga kegagalan gerbang adalah temuan yang sah dan terlapor; cadangan A–D mempersempit klaim tanpa mengubah rumusan masalah.

**P11 — "Kenapa cuma 5–8 isyarat? Sedikit sekali."**
Jumlah itu keputusan disiplin klaim dan realisme satu semester: klasifikasi himpunan tertutup dengan peluang acak yang selalu dilaporkan (20% untuk lima kelas, 12,5% untuk delapan), plus jalur pemangkasan bila G2 gagal. Kalimat kontinu ber Tata bahasa penuh adalah masalah terbuka internasional — masuk ke sana tanpa data justru tidak ilmiah.

**P12 — "Apa beda SIBI dan BISINDO, dan produk ini untuk siapa?"**
SIBI sistem isyarat baku yang dikembangkan untuk pendidikan formal (kamus resmi 1994), BISINDO bahasa isyarat alami komunitas tunarungu. Purwarupa kami untuk konteks pendidikan formal — guru pendamping, keluarga siswa pada kegiatan belajar — dengan validator penutur tunarungu di dalam proyek sejak kurasi kosakata; kami tidak mengklaim kebutuhan komunikasi komunitas sehari-hari.

## 12. Keputusan Terbuka dan Langkah Pertama

### 12.1 Keputusan yang menunggu pembimbing

1. Gaya sitasi IEEE bernomor yang dipakai proposal revisi — konfirmasi akhir. [PERLU DATA: konfirmasi gaya sitasi]
2. Frasa judul "purwarupa" dan "kosakata terbatas" sebagai penanda klaim — konfirmasi akhir. [PERLU DATA: konfirmasi frasa judul]
3. Ambang G2 dan G3 yang dirumuskan relatif peluang acak — disepakati sebelum eksperimen. [PERLU DATA: ambang G2 dan G3]
4. Kesediaan atas rencana dua ruang mitra dan 3–4 pengisyarat. [PERLU DATA: persetujuan rencana dua ruang]
5. Token apresiasi validator dan skala uji kegunaan 3–5 pengguna. [PERLU DATA: bentuk token apresiasi validator]

### 12.2 Keputusan yang menunggu hasil tahap (tidak boleh ditebak sekarang)

- T0: kanal, jarak antarmodul, ukuran zona, kriteria keterpisahan Delta-CSI, ambang kehilangan paket. [PERLU DATA: hasil uji T0]
- T2: kriteria pemilihan subcarrier, definisi lintasan puncak, pembagian blok data, ambang skor keyakinan dari data validasi. [PERLU DATA: hasil T2]
- T4: ukuran model ASR dan pilihan TTS final, indikator layak latensi tiap arah, model layar-audio-baterai final, daftar frasa uji dan jumlah penutur, butir kuesioner, rubrik validator. [PERLU DATA: hasil T4]
- Bersama validator: daftar 5–8 isyarat terpilih dan kosakata tampilan. [PERLU DATA: daftar isyarat terpilih]

### 12.3 Keputusan pemilik dan mitra

Identitas mitra (SLB/lembaga), jadwal perizinan dan persetujuan etik, komposisi pengisyarat kompeten dan validator, profil pengguna baru untuk T3. [PERLU DATA: identitas mitra dan jadwal etika]

### 12.4 Langkah pertama (senin pagi, urutan kepentingan)

1. Klon RuView, siapkan dua modul ESP32-S3, pasang firmware, dan mulai uji Delta-CSI serta uji koeksistensi radio — keputusan G0 dikunci akhir M2; tanpa ini seluruh rantai berdiri di asumsi.
2. Kirim undangan calon validator penutur tunarungu dan gerbang mitra — jalur ini berlead time paling panjang; sambil jalan susun draf formulir persetujuan.
3. Bawa lima butir seksi 12.1 ke sesi bimbingan terdekat.
4. Mulai kurasi kandidat isyarat dari Kamus SIBI (dua saringan: separabilitas fisik lintasan + kelayakan pedagogis) sebagai bahan diskusi validator — daftar final tetap milik validator dan pemilik.

### 12.5 Catatan penutup pemakaian dossier

Draf proposal tidak ditulis ulang oleh dossier ini. Bila pemilik ingin menulis sendiri, seksi 1–2 memberi arah argumen, seksi 3–5 memberi bahan terverifikasi, seksi 9–10 memberi bata kalimat, dan seksi 11 melatih pembelaan. Bila pemilih memakai `Proposal-Revisi-Translator-SIBI.md` langsung, dossier ini menjadi peta sumber: setiap klaim di naskah bisa dilacak ke bank fakta dan bank rujukan di sini. Yang berubah pada naskah sebaiknya dicatat balik ke seksi 3 agar jejak verifikasi tetap utuh.

## 13. Lampiran — Jejak Riset dan Cara Memakai Dossier

**Jejak bukti.** Matriks rujukan dan status verifikasi per klaim: `download/translator-sibi-revisi/Matriks-Literatur-dan-Bukti.md`. Vonis kelayakan komponen: `Audit-Arsitektur-Translator-SIBI.md`. Catatan riset teknis: `riset-translator-sibi/T17-R1-tts-asr-indonesia.md`, `T17-R2-esp32s3-csi.md`, `T17-R3-representasi-sibi.md`. Metadata Crossref rujukan baru: `scripts/translator-sibi/meta_rujukan_baru.json`. Arsip verifikasi rujukan lama: `13-sempro-docx/verifikasi-rujukan-2026-10-24/`. Dossier pendahulu (topik lama, masih berguna untuk kontras): `12-council-alur-dpj4/DPJ-4_Bahan-Proposal-SIBI.md` beserta transkrip dewan.

**Konvensi penanda.** `[PERLU DATA: ...]` = keputusan yang menunggu pemilik, pembimbing, atau hasil tahap sebelumnya; `[PERLU RUJUKAN: ...]` = klaim yang belum punya rujukan terverifikasi (dossier ini tidak memuatnya). Frasa ID-READY = kalimat bahasa Indonesia siap disalin lalu disesuaikan ke naskah.

**Optimisasi GEPA.** Dossier ini disusun sebagai kandidat benih dan disempurnakan lewat `optimize_anything` (paket gepa 0.1.4, backend gepa) dengan evaluator hibrida: cek objektif (jangkar fakta, klaim terlarang, penanda, panjang) × rubrik juri LLM lima dimensi. Log iterasi tersimpan pada `scripts/translator-sibi-bahan/runs/`; laporan ringkas pada `catatan.md` paket pengiriman.
