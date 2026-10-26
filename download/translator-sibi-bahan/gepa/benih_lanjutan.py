# -*- coding: utf-8 -*-
"""Benih komponen mudah-mutasi dossier bahan Translator SIBI (bagian 2).

Empat komponen terakhir: kit_bab1, kit_bab23, sidang, keputusan.
Nomor [n] mengikuti Daftar Pustaka Proposal-Revisi (79 entri).
"""

KIT_BAB1 = """### 9.1 Subbab 1.1 Latar Belakang

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
"""

KIT_BAB23 = """### 10.1 Kerangka BAB II (sebelas subbab, urutan mengikuti proposal revisi)

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
"""

SIDANG = """**P1 — "Kenapa SIBI, padahal BISINDO yang dipakai komunitas?"**
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
"""

KEPUTUSAN = """### 12.1 Keputusan yang menunggu pembimbing

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
"""
