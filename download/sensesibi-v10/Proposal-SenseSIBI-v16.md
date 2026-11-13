# STUDI KELAYAKAN PURWARUPA SenseSIBI: SISTEM PENERJEMAHAN DUA ARAH HURUF SIBI BERBASIS WI-FI CSI DENGAN INFERENSI ESP32-S3 DAN CLOUD PROCESSING

**PROPOSAL PENELITIAN**

| Identitas | Keterangan |
|---|---|
| Judul | STUDI KELAYAKAN PURWARUPA SenseSIBI: SISTEM PENERJEMAHAN DUA ARAH HURUF SIBI BERBASIS WI-FI CSI DENGAN INFERENSI ESP32-S3 DAN CLOUD PROCESSING |
| Jenis dokumen | Proposal penelitian (seminar proposal), BAB I sampai III + Daftar Pustaka; revisi additif: ruang lingkup sistem dua arah dipertahankan, blok model jalur isyarat menjadi teks diperbarui menjadi encoder CSI terpralatih dengan dua kepala tugas; 49 halaman (tambahan isi brief v2 menaikkan halaman dari 40 pada v15) |
| Disusun oleh | [PERLU DATA: nama penulis] |
| NIM | [PERLU DATA: NIM penulis] |
| Program studi | [PERLU DATA: program studi] |
| Universitas | [PERLU DATA: nama universitas] |
| Pembimbing | [PERLU DATA: nama pembimbing, jika sudah ditentukan] |
| Tahun | [PERLU DATA: tahun penyusunan] |

> Catatan penyusunan: versi ini menyunting naskah v15 sebagai revisi additif. Ruang lingkup sistem tidak berubah: purwarupa penerjemah dua arah dengan inferensi ESP32-S3 dan pemrosesan awan tetap menjadi objek, demikian pula mesin ucapan, pengenalan ucapan, kamus representasi, server dan cadangannya, gerbang keputusan G0 sampai G4, serta seluruh uji kelayakan. Yang berubah hanya blok model pada jalur isyarat menjadi teks: *backbone* WiFi-DensePose berkepala tunggal 1D-CNN diganti menjadi *encoder* CSI terpralatih RuView yang dibekukan dengan dua kepala tugas, yaitu kepala klasifikasi 26 huruf dan kepala regresi 21 *keypoint* tangan, di bawah supervisi guru visual YOLO26m-Pose. Persamaan bernomor bertambah dari 18 menjadi 29; gambar menjadi tujuh dengan satu diagram blok model baru; tabel menjadi dua belas; daftar pustaka menjadi 28 entri. Penanda [PERLU DATA] kini ditemani [PERLU VALIDASI] untuk hal yang baru dapat ditetapkan setelah audit *checkpoint*. Konteks Jawa Timur tanpa mitra lembaga dipertahankan; rincian perubahan per subbab ada pada Log Perubahan gelombang 16 di ujung naskah.

---
# BAB I PENDAHULUAN

## 1.1 Latar Belakang

Anak tunarungu hampir selalu lahir dari orang tua yang bisa mendengar. Sejak hari-hari pertama, komunikasi di rumah berjalan dengan dua bahasa yang tidak saling mengerti: orang tua berbicara dengan suara, anak menjawab dengan isyarat. Orang tua lalu harus mempelajari bahasa isyarat dari nol, padahal waktu dan kesempatan berlatih serba terbatas. Angkanya memang timpang. Di Indonesia ada sekitar 1,92 juta penyandang tunarungu, sementara juru bahasa isyarat hanya sekitar 500 orang [1], sehingga satu juru bahasa harus melayani hampir 4.000 orang. Untuk kebutuhan harian seperti menceritakan sakit atau bertanya kepada penjual di pasar, menunggu juru bahasa jelas bukan jalan keluar. Undang-Undang Nomor 8 Tahun 2016 sudah menjamin hak setiap penyandang disabilitas untuk berkomunikasi [2], tetapi tanpa alat bantu yang benar-benar terjangkau, jaminan itu berjalan lambat.

Kesenjangan seperti itu paling terasa di ruang kelas. Guru menjelaskan dengan suara; siswa tunarungu menangkap sebagian, menebak sisanya, lalu mudah kehilangan alur pelajaran. SIBI menjadi bahasa pengantar pada pendidikan formal; bentuk isyaratnya dibakukan pemerintah dalam *Kamus Sistem Isyarat Bahasa Indonesia* [3]. Survei terhadap 100 responden tunarungu di Jawa dan Bali melaporkan 91% memakai BISINDO sehari-hari, sementara SIBI menempel pada konteks sekolah [4]; keduanya memang hidup di ranah yang berbeda dan tidak saling menggantikan. Karena penelitian ini menyasar alat bantu pembelajaran di sekolah, SIBI yang dipilih. Seluruh pelaksanaannya direncanakan di Jawa Timur tanpa mengikat kerja sama dengan lembaga tertentu.

Upaya membangun alat bantu komunikasi dua arah sebenarnya sudah ada, tetapi jalurnya baru setengah jalan. Sistem yang mengubah ucapan atau teks menjadi animasi isyarat hanya melayani satu arah: orang pendengar berbicara, sistem mengisyaratkan. Arah sebaliknya, isyarat siswa yang dibaca mesin, belum tersedia sebagai alat yang siap dipakai; riset di Indonesia masih berkutat di jalur kamera, misalnya pengenalan huruf BISINDO dari citra dengan CNN [5]. Kendala kamera itu ada dua dan keduanya praktis. Kamera menuntut pencahayaan serta posisi yang tepat, dan begitu cahaya sedikit berubah, akurasi ikut jatuh; kamera yang terus menyala juga membuat penggunanya merasa diawasi, tidak nyaman dipakai sepanjang hari di kelas.

Untuk menghindari dua kendala itu, sinyal Wi-Fi membuka jalan lain tanpa kamera. Sinyal ini membawa informasi kanal bernama *Channel State Information* (CSI) [6]. Begitu tangan bergerak di antara pemancar dan penerima, jalur pantulan sinyal bergeser dan CSI berubah mengikuti pola gerakannya; perubahan itulah yang dibaca untuk mengenali gerak tanpa sensor yang dikenakan di tubuh. SignFi, contoh terkemukanya, mengenali 276 isyarat *American Sign Language* (ASL) dari CSI [7], dan CSI bahkan peka terhadap gerak halus sampai ke gerakan jari [6]. Penelusuran pada Google Scholar, Crossref, dan OpenAlex hingga Oktober 2026 belum menemukan satu pun penerapan CSI untuk isyarat SIBI.

Perangkat yang dibutuhkan pun sederhana dan murah. Modul ESP32-S3, mikrokontroler seharga sekitar Rp150.000, sudah memiliki radio Wi-Fi 2,4 GHz dengan dukungan CSI resmi [8], [9]. Dua modul cukup untuk satu pasang: yang satu memancarkan sinyal, yang lain menangkapnya. Zona isyarat berada di antara keduanya. *Firmware* penangkap CSI yang teruji untuk modul ini tersedia pada platform terbuka RuView [10]. Biaya sepasang node lengkap diperkirakan di bawah Rp350.000, jauh lebih ringan daripada kamera ditambah komputer pengolah citra. Murah di sini bukan soal angka semata; harga yang terjangkau mengundang sekolah berani memasang alat ini di lebih dari satu ruang.

Jawabannya, penelitian ini merancang purwarupa bernama SenseSIBI, singkatan dari *Sensing & Translation of SIBI*. Arah pertamanya berjalan dari siswa: ia mengisyaratkan huruf, modul menangkap pola CSI, model yang berjalan langsung di modul mengenalinya, teks muncul di layar, lalu dibunyikan sebagai suara. Arah kedua berjalan dari guru: ia menekan tombol lalu berbicara; ucapannya dikenali menjadi teks, lalu bentuk isyaratnya ikut tampil di layar. Model pengenal isyaratnya tidak dilatih dari nol. *Encoder* CSI terpralatih dari RuView [11] menjadi tulang punggungnya. Representasinya dibekukan, lalu dua kepala tugas dilatih di atasnya: satu kepala mengenali 26 kelas huruf, satu lagi memperkirakan 21 titik jari tangan. Model penglihatan YOLO26m-Pose yang sudah terlatih pada data citra SIBI milik peneliti berperan sebagai guru yang memberi label itu [12]. Kamera hanya dipakai guru saat data direkam; setelah kedua kepala terlatih, seluruh sistem bekerja tanpa kamera.

Sebagai studi kelayakan, penelitian ini sengaja membatasi klaimnya. Objek pengenalan dibatasi pada alfabet manual SIBI satu tangan sebanyak 26 huruf, yaitu 24 huruf statis ditambah dua huruf gerak J dan Z, bukan penerjemahan kalimat penuh. Kemampuan membedakan huruf diuji lebih dahulu sebelum klaim yang lebih jauh dibuat; tiap tahap ditutup gerbang keputusan, dan kegagalan tetap dilaporkan sebagai temuan. Dalam batas itulah penelitian ini mencoba menjawab pertanyaan yang sederhana sekaligus jujur: apakah sepasang modul Wi-Fi murah sungguh bisa menjadi jembatan komunikasi dua arah antara siswa tunarungu dan gurunya di kelas?

## 1.2 Rumusan Masalah

Dari latar belakang yang telah dipaparkan, masalah yang dikaji dalam penelitian ini dirumuskan sebagai berikut.

1. Bagaimana merancang purwarupa penerjemah dua arah antara huruf SIBI dan teks beserta suara bahasa Indonesia dengan sepasang modul ESP32-S3 tanpa kamera, yang pada jalur isyarat menjadi teks memakai *encoder* CSI terpralatih RuView yang dibekukan dengan dua kepala tugas, yaitu kepala klasifikasi 26 huruf dan kepala regresi 21 *keypoint* tangan di bawah supervisi guru visual YOLO26m-Pose, menjalankan inferensi terkuantisasi langsung di modul, serta menghadirkan mesin ucapan dan pengenalan ucapan bahasa Indonesia?
2. Seberapa baik alfabet manual SIBI dikenali dari sinyal CSI oleh model *encoder* terpralatih berkepala dua, termasuk sumbangan kepala regresi yang diukur lewat ablasi, serta bagaimana kinerja kedua jalur penerjemahan pada skenario dalam sesi, lintas partisipan, dan lintas ruang?
3. Seberapa layak purwarupa menjadi alat bantu komunikasi jika ditinjau dari latensi inferensi terkuantisasi dan ujung ke ujung, cakupan kosakata, keandalan operasional, penerimaan pengguna, serta biaya perangkat dan layanan?

## 1.3 Tujuan Penelitian

Tujuan penelitian ini adalah sebagai berikut.

1. Merancang purwarupa penerjemah dua arah antara huruf SIBI dan teks beserta suara bahasa Indonesia dengan sepasang modul ESP32-S3 tanpa kamera, yang pada jalur isyarat menjadi teks memakai *encoder* CSI terpralatih RuView yang dibekukan dengan dua kepala tugas, yaitu kepala klasifikasi 26 huruf dan kepala regresi 21 *keypoint* tangan di bawah supervisi guru visual YOLO26m-Pose, menjalankan inferensi terkuantisasi langsung di modul, serta menghadirkan mesin ucapan dan pengenalan ucapan bahasa Indonesia.
2. Mengukur seberapa baik alfabet manual SIBI dikenali dari sinyal CSI oleh model *encoder* terpralatih berkepala dua, termasuk sumbangan kepala regresi yang diukur lewat ablasi, serta kinerja kedua jalur penerjemahan pada skenario dalam sesi, lintas partisipan, dan lintas ruang.
3. Menganalisis kelayakan purwarupa sebagai alat bantu komunikasi ditinjau dari latensi inferensi terkuantisasi dan ujung ke ujung, cakupan kosakata, keandalan operasional, penerimaan pengguna, serta biaya perangkat dan layanan.

## 1.4 Batasan Masalah

Agar fokus, ruang lingkup penelitian ini dibatasi sebagai berikut.

1. Objek pengenalan ialah alfabet manual SIBI satu tangan 26 huruf (24 statis serta huruf gerak J dan Z). Bentuk bakunya dicocokkan dengan *Kamus SIBI* [3] dan disetujui validator penutur tunarungu; sistem ini bukan penerjemah kalimat.
2. Pembeda utamanya adalah bentuk tangan dan jari beserta lintasan gerak J dan Z; ekspresi wajah serta penanda nonmanual tidak dikenali.
3. Penginderaan memakai sepasang modul ESP32-S3 (satu pemancar, satu penerima; 2,4 GHz, kanal 20 MHz) dengan layar, baterai, *speaker*, dan mikrofon pada node penerima; kamera hanya menyala saat perekaman data pelatihan.
4. YOLO26m-Pose berperan sebagai guru visual hanya pada saat akuisisi dan pelatihan; produk akhirnya bebas kamera dan bebas citra.
5. *Encoder* murid memakai *checkpoint* terpralatih `ruvnet/wifi-densepose-pretrained` dengan *embedding* 128 dimensi dan 9.280 parameter [11]; *encoder* dibekukan pada baseline, sedangkan LoRA dan pelatihan lanjutan diperlakukan sebagai eksperimen pembanding; bentuk masukan *checkpoint*, yang kartu modelnya mencatat delapan fitur turunan, diaudit pada T0 dan adapter masukan disiapkan jika bentuknya tidak sesuai jendela CSI [PERLU VALIDASI: bentuk masukan checkpoint dan rancangan adapter].
6. Sintesis ucapan berjalan *on-device* di ponsel, sedangkan pengenalan ucapan memakai layanan awan dengan mesin lokal sebagai cadangan; pilihan finalnya ditetapkan pada gerbang G3.
7. Arah kedua terbatas pada kamus tingkat kata dengan *fallback* ejaan jari; cakupan kamusnya diukur lalu dilaporkan.
8. Satu sesi hanya melibatkan satu pengisyarat dan sistem tidak mengidentifikasi individu; pengujian berlangsung di sedikitnya dua ruang berbeda di Jawa Timur yang sudah dikalibrasi.
9. Uji pengguna berskala kecil (3–5 pengguna) dan dianalisis secara deskriptif, tanpa statistik inferensial.
10. Isyarat kontinu, tata bahasa isyarat penuh, BISINDO, serta klasifikasi gerakan otomatis dari video berada di luar pembahasan.

## 1.5 Manfaat Penelitian

Manfaat penelitian ini terbagi atas manfaat teoretis dan manfaat praktis.

### 1.5.1 Manfaat Teoretis

Secara teoretis, penelitian ini menyumbang bukti awal tentang satu pertanyaan yang tajam: apakah *embedding* hasil pretraining kontrastif pada CSI masih informatif untuk gestur jari jika hanya dua kepala tugasnya yang dilatih. Bukti itu terikat pada alfabet manual dan belum tentu berlaku untuk isyarat kata maupun isyarat kontinu. Penelitian ini juga menghasilkan formulasi multitugas lintas modalitas yang mengawasi klasifikasi isyarat dengan regresi bentuk jari pada satu *embedding* bersama, serta *dataset* CSI berlabel beserta protokol perekamannya. Peneliti berikutnya bisa memakainya untuk bahasa isyarat lain, termasuk perluasan ke BISINDO.

### 1.5.2 Manfaat Praktis

Bagi sekolah yang kelak memakainya, penelitian ini memberi gambaran nyata tentang kelayakan alat bantu komunikasi dua arah berbahasa SIBI, lengkap dengan biaya perangkatnya. Purwarupa yang memunculkan teks, menyuarakan isyarat, dan memperagakan bentuk isyarat bagi lawan bicara akan lahir jika seluruh tahap berhasil. Jika berhenti lebih awal, laporan karakterisasi, protokol, dan *dataset* berlabel tetap menjadi warisan penelitian. Bagi keluarga siswa, kosakata yang tervalidasi memastikan isyarat yang muncul di layar benar bentuknya. Bagi komunitas riset, rancangan yang tidak terikat pada satu bahasa isyarat memudahkan replikasi di tempat lain.

## 1.6 Sistematika Penulisan

Secara ringkas, proposal ini disusun atas tiga bab. **BAB I Pendahuluan** memuat latar belakang, rumusan masalah, tujuan, batasan, manfaat, dan sistematika penulisan. **BAB II Kajian Pustaka** menghimpun teori dan penelitian terdahulu yang menjadi dasar perancangan, termasuk *encoder* CSI terpralatih, kedua kepala tugas, dan supervisi guru visual. **BAB III Metode Penelitian** memuat desain, tahapan, waktu dan lokasi, alat dan bahan, perancangan sistem, protokol perekaman, pengolahan sinyal dan pelatihan dua kepala, skenario pengujian, jadwal, parameter yang ditetapkan kemudian, serta risiko dan cadangannya.
# BAB II KAJIAN PUSTAKA

## 2.1 Bahasa Isyarat, SIBI, dan Kebutuhan Komunikasi Dua Arah

Bahasa isyarat menyampaikan makna lewat gerak tangan, lengan, tubuh, dan ekspresi wajah. Satu isyarat tersusun atas bentuk tangan, lokasi, gerak, serta orientasi telapak; cukup satu jari berubah bentuk, maknanya bisa ikut berubah. Susunan inilah yang menjadi acuan penelitian dalam memisahkan bagian isyarat yang bisa dinilai mesin dari bagian yang tetap memerlukan penilaian manusia [3]. SIBI ialah sistem isyarat baku pendidikan formal yang didokumentasikan kamus pemerintah [3], sedangkan BISINDO tumbuh alami di komunitas tunarungu. Survei terhadap 100 responden tunarungu di Jawa dan Bali menemukan 91% memakai BISINDO, sementara SIBI menempel pada konteks sekolah [4]. Penelitian ini tetap memilih SIBI karena sasarannya alat bantu pembelajaran di sekolah, bukan karena jumlah penuturnya lebih besar. Audit label pada dataset visual peneliti menegaskan pembagian kelas yang dipakai seluruh naskah: huruf C termasuk kelompok 24 huruf statis, sedangkan J dan Z satu-satunya huruf yang menuntut lintasan gerak.

Bicara antara pengguna isyarat dan orang pendengar menuntut dua arah. Keluarga dan guru berada di barisan paling depan untuk merasakan kesenjangan ini, sementara jumlah juru bahasa masih jauh dari cukup [1]; alat bantu yang dibangun karena itu harus melayani kedua arah; kamus satu arah tidak menyelesaikan masalahnya. Sistem satu arah yang mengubah ucapan menjadi animasi isyarat sudah lebih dulu hadir di Indonesia, tetapi untuk arah isyarat menjadi teks riset dalam negeri bertumpu pada kamera, misalnya CNN untuk huruf BISINDO [5]. Masalahnya, kamera menuntut pencahayaan dan garis pandang yang baik, dan kamera yang terus menyala membuat pengguna merasa diawasi. Dua kendala inilah yang mendorong pencarian jalur penginderaan tanpa kamera dan tanpa perangkat yang dikenakan.

## 2.2 Wi-Fi Channel State Information

*Channel State Information* (CSI) memuat informasi amplitudo dan fase pada setiap *subcarrier* sinyal Wi-Fi, yang bersama-sama menggambarkan kondisi jalur propagasi [6]. Tubuh yang bergerak di antara pemancar dan penerima mengubah panjang jalur pantulan; amplitudo dan fase tiap *subcarrier* pun ikut bergeser. Geseran inilah yang dipakai untuk mengenali gerak tanpa sensor yang dikenakan. Karena tiap *subcarrier* menempati frekuensi berbeda, satu pasang perangkat sekaligus menyediakan banyak kanal pengamatan [6].

Bentuk formalnya sederhana: pada kanal 20 MHz, tiap *subcarrier* ke-n membawa koefisien kanal kompleks

```rumus
h~n~(t) = |h~n~(t)| · exp( j · φ~n~(t) ) (2.1)
```

dengan n = 1, ..., 56, |h~n~(t)| amplitudo, φ~n~(t) fase, dan j satuan imajiner [6], [9]. Amplitudo dan fase inilah bahan mentah seluruh perhitungan pada bab-bab berikutnya.

Pemodelan CSI sendiri berpijak pada zona Fresnel [13]. Radius zona Fresnel ke-n pada suatu titik dihitung dari jarak titik itu ke pemancar d~1~ dan ke penerima d~2~ [13]:

```rumus
r~n~ = √( n · λ · d~1~ · d~2~ / ( d~1~ + d~2~ ) ) (2.2)
```

dengan λ panjang gelombang pembawa; pada 2,4 GHz, λ = c/f ≈ 12,5 cm. Angkanya bisa langsung dihitung untuk tautan baku penelitian ini. Pada jarak antarmodul 1 meter dengan tangan di titik tengah, radius zona pertama r~1~ = √(0,125 × 0,5 × 0,5) ≈ 0,18 meter. Ruang gerak jadi seluruhnya berada di zona yang paling peka terhadap perubahan jalur. Penempatan itu dirangkum pada Gambar 2.1. Artikulasi jari menggeser jalur pantulan pada orde sentimeter sampai milimeter, dan tiap bentuk huruf meninggalkan pola perubahan *subcarrier* yang khas.

```gambar
Sumber skrip: scripts/sensesibi-v10/gambar_g15_fresnel.py (matplotlib mplot3d) -> assets-v16/gambar-2.1.png
```

Gambar 2.1 Zona Fresnel pertama pada tautan baku 1 meter; tangan pengisyarat berada di dalam zona (ilustrasi skematis tiga dimensi, tidak berskala) [6], [13]

Gerak tubuh juga melahirkan pergeseran Doppler yang besarnya mengikuti kecepatan gerak v [6], [14]:

```rumus
f~D~ = ( v / λ ) · ( cos α + cos β ) (2.3)
```

dengan α dan β sudut antara arah gerak dan garis pandang ke pemancar serta ke penerima; nilai mutlaknya paling besar 2v/λ. Pita Doppler gerak isyarat yang relevan kira-kira 1–60 Hz [6], sedangkan kaidah Nyquist menuntut laju pencuplikan

```rumus
f~s~ ≥ 2 · f~maks~ (2.4)
```

Akibatnya bisa dihitung sejak awal. Pada laju *firmware* RuView 50 bingkai per detik [10], pita teramati hanya sampai 25 Hz, sehingga gerak tangan yang masih teramati tanpa pelipatan kira-kira v = 25 × 0,125/2 ≈ 1,6 meter per detik. Gerak jari yang lebih cepat berisiko terlipat, dan jika laju terukur lebih rendah lagi, pita yang dianalisis ikut menyempit; hal itu dilaporkan apa adanya.

Satu masalah masih tersisa: fase mentah tercemar derau osilator lokal. Teknik CSI-ratio membersihkannya lewat rasio atau perkalian konjugat tanpa perangkat tambahan [13]. Prinsip itu diadaptasi penelitian ini menjadi rasio terhadap rekam acuan kalibrasi ruang (Subbab 3.7):

```rumus
ρ~n~(t) = h~n~(t) / h~n~( t~0~ ) (2.5)
```

dengan t~0~ waktu kalibrasi ruang, yaitu 600 bingkai bawaan RuView [10]. Rasio ini membuang tanggapan statis ruang sehingga yang tersisa adalah perubahan akibat gerak; sisa derau fase yang berjalan lambat diukur pada T0 lalu dilaporkan.

Dari ketukan tombol sampai gerakan jari, bukti kepekaan CSI terhadap gerak halus cukup banyak [6]; akan tetapi, bukti-bukti itu lahir dari kondisi terkendali sehingga bagi penelitian ini statusnya sebatas hipotesis kerja. Model CSI juga mudah *overfitting* terhadap orang dan ruang. Widar3.0 menjawab masalah itu dengan profil kecepatan Doppler untuk pengenalan lintas domain [14]. Kelayakan satu tautan dua modul berantena tunggal untuk membedakan 26 bentuk tangan SIBI karenanya diperlakukan sebagai pertanyaan penelitian, bukan asumsi; uji Delta-CSI dan gerbang G1 yang mengujinya. Jika beberapa huruf terbukti tidak terpisahkan, himpunan huruf dipangkas (Tabel 3.7).

## 2.3 Modul ESP32-S3, Platform RuView, dan Koeksistensi Radio

ESP32-S3 ialah mikrokontroler Wi-Fi 802.11 b/g/n 2,4 GHz berantena tunggal dengan inti ganda 240 MHz, SRAM 512 KB, dan PSRAM hingga 8 MB [8]. Dukungan CSI tersedia resmi lewat repositori esp-csi; pada kanal 20 MHz, CSI memuat 56 *subcarrier* [9]. RuView merekomendasikan ESP32-S3 sebagai modul penangkap CSI sekaligus menyediakan rantai akuisisi lengkap [10] yang dipetakan pada Tabel 2.1. Repositori yang sama menerbitkan *checkpoint encoder* CSI terpralatih yang menjadi tulang punggung murid penelitian ini. Pembedaannya dari dua model lain pada ekosistem itu diuraikan pada Subbab 2.4.

Tabel 2.1 Pemetaan fitur RuView terhadap peran dalam penelitian ini

| Fitur RuView | Peran dalam penelitian ini |
|---|---|
| *Firmware* penangkap CSI (UDP) | Mengalirkan CSI dan label ke server |
| Station + UDP + CSI *promiscuous* + ESP-NOW pada satu *chip* | Dasar topologi satu kanal (Subbab 3.5) |
| Kalibrasi ruang 600 bingkai + 8 *anchor* | Kalibrasi tiap sesi; pemotongan segmen isyarat |
| Mode privasi | Membuang fitur biometrik selama penelitian |
| Akuisisi tersinkron kamera-CSI | Jalur guru; estimator memakai YOLO26m-Pose |
| *Checkpoint encoder* CSI terpralatih (*embedding* 128 dimensi) [11] | *Encoder* murid yang dibekukan pada baseline (Subbab 2.4) |

Fakta paling menentukan justru koeksistensi radio pada satu *chip*. *Firmware* RuView mampu menangkap CSI sambil memelihara koneksi *station* UDP serta sinkronisasi ESP-NOW secara serentak. Dua syaratnya: seluruh perangkat berada pada satu kanal dan mode hemat daya dimatikan [10]. Purwarupa karenanya tidak memerlukan modul gerbang khusus, tetapi ada satu catatan penting: RuView belum melalui telaah sejawat, jadi fungsinya diverifikasi sendiri pada gerbang G0.

## 2.4 Encoder CSI Terpralatih RuView dan Pembedaan Tiga Model

*Encoder* terpralatih yang menjadi tulang punggung jalur isyarat menjadi teks terdokumentasi lengkap pada kartu modelnya [11]. Arsitekturnya dua lapis *fully connected* dengan BatchNorm dan GELU yang memetakan fitur CSI menjadi *embedding* 128 dimensi ternormalisasi L2. Seluruhnya hanya 9.280 parameter. Pemetaannya ditulis

```rumus
z~i~ = f~θ0~( X~i~ ), z~i~ ∈ R^d^, d = 128 (2.6)
```

dengan X~i~ masukan ke-i, f~θ0~ pemetaan *encoder* bertetapan θ~0~, dan z~i~ vektor *embedding* keluaran. Pretrainingnya kontrastif dengan triplet loss dan InfoNCE pada temperatur 0,1. Pasangan positif diambil dari jendela dalam jarak 2 detik, pasangan negatif dari jarak lebih dari 30 detik, selama 60 epoch dengan AdamW dan perlindungan EWC terhadap lupa bencana [11]. Pada baseline penelitian ini, θ~0~ dibekukan sehingga hanya tetapan kepala tugas yang diperbarui.

Satu angka pada kartu model itu perlu dibaca hati-hati. Akurasi triplet-temporal *held-out* sebesar 82,3% tercatat pada 20% akhir rekaman menurut waktu, dengan pembanding 66,4% untuk fitur mentah tanpa *encoder* dan 69,6% untuk *encoder* berinisialisasi acak [11]. Angka itu menghitung peluang bahwa jarak anchor ke positif temporal lebih pendek daripada jaraknya ke negatif temporal. Yang diukurnya ialah kualitas geometri *embedding* pada tugas jarak, bukan akurasi klasifikasi SIBI dan bukan pula galat *keypoint*. Dua hal terakhir justru yang hendak diukur penelitian ini, dan kartu model tidak memuat keduanya.

Ketidaksesuaian bentuk masukan menjadi temuan audit yang paling menentukan. Kartu model mencatat masukan delapan fitur turunan CSI pada laju 1 Hz, yaitu kehadiran, gerak, napas, detak jantung, varians fase, jumlah orang, deteksi jatuh, dan RSSI [11]. Jalur akuisisi penelitian ini, sebaliknya, menghasilkan 56 *subcarrier* pada 50 bingkai per detik [9], [10], sehingga *encoder* itu tidak dapat langsung diberi *subcarrier* mentah. Dua jalur penyelesaiannya disiapkan dan diputuskan setelah audit T0. Jalur pertama menghitung ulang delapan fitur turunan bawaan RuView dari bingkai CSI; jalur kedua melatih adapter masukan kecil yang memetakan jendela CSI ke ruang masukan *encoder*. Keduanya dinyatakan terbuka dengan penanda [PERLU VALIDASI] sampai audit selesai, dan riset ini tidak mengklaim kompatibilitas sebelum terverifikasi.

Dua model lain pada ekosistem yang sama sering tertukar dengan *encoder* ini, sehingga keduanya dipisahkan sejak awal. Model `wifi-densepose-mmfi-pose` [15] adalah *checkpoint* pose terpisah. Masukannya amplitudo CSI berukuran [3, 114, 10] pada 100 Hz, yang diproses *encoder* Transformer 4 lapis 8 kepala menjadi keluaran [17, 2], yaitu 17 *keypoint* tubuh COCO dalam rentang [0, 1], dengan sekitar 2,3 juta parameter. Model itu dilatih pada dataset MM-Fi [16] yang memuat 40 subjek, 27 kategori aksi, dan lebih dari 320 ribu bingkai tersinkron dari lima modalitas. Kinerjanya PCK@20 ternormalisasi badan sebesar 82,69% untuk model tunggal dan 83,59% untuk ansambel. Angka itu turun menjadi sekitar 64% lintas subjek *zero-shot* dan 17,5% lintas lingkungan, lalu naik ke rentang 72% sampai 78% setelah kalibrasi 50 sampai 1.000 bingkai per orang [15]. Lisensi CC BY-NC 4.0 melekat padanya karena mengikuti lisensi datanya. Model ketiga, YOLO26m-Pose [12], ialah model penglihatan pada citra yang berperan sebagai guru visual dan dibahas pada Subbab 2.9. Tabel 2.2 merangkum pembedaan ketiganya.

Tabel 2.2 Pembedaan tiga model ekosistem yang tidak boleh tercampur dalam penelitian ini

| Aspek | Encoder CSI terpralatih [11] | Model pose MM-Fi [15] | Guru visual YOLO26m-Pose [12] |
|---|---|---|---|
| Berkas | `ruvnet/wifi-densepose-pretrained` | `ruvnet/wifi-densepose-mmfi-pose` | Repositori WPC peneliti (eksperimen `exp11_huruf24`) |
| Masukan | 8 fitur turunan CSI | Amplitudo CSI [3, 114, 10] @ 100 Hz | Citra RGB kamera |
| Keluaran | *Embedding* 128 dimensi ternormalisasi L2 | 17 *keypoint* tubuh COCO dalam [0, 1] | Kelas isyarat dan 21 *keypoint* tangan |
| Parameter | 9.280 | ±2,3 juta (varian utama) | [PERLU DATA: jumlah parameter model juara WPC] |
| Peran | Representasi murid, dibekukan pada baseline | Pembanding temuan lintas domain, bukan komponen model | Pemberi label kelas dan *keypoint* saat akuisisi |
| Status bukti | Kartu model; akurasi triplet-temporal 82,3% | Kartu model; PCK@20 82,69%; lisensi CC BY-NC 4.0 | Data pra-penelitian peneliti; mAP50 0,9580 pada 24 huruf statis |

Status tiga dokumen rancangan pada repositori RuView juga dinyatakan terbuka. ADR-024 mengusulkan model penyematan kontrastif AETHER; ADR-146 mengusulkan *encoder* RF bersama dengan tujuh kepala tugas dan ketidakpastian per kepala; ADR-150 mengusulkan *foundation encoder* yang tahan pergantian orang dan ruang. Ketiganya berstatus Proposed, artinya rancangan yang belum diimplementasikan [10]. Penelitian ini bersandar hanya pada *checkpoint* yang benar-benar tersedia; angka estimasi dari ADR dikutip dengan label estimasi rancangan setiap kali muncul.

## 2.5 Transfer Learning pada Encoder Beku: LoRA dan Pelatihan Lanjutan

Baseline penelitian ini membekukan *encoder* dan melatih hanya kedua kepala tugasnya. Alasannya metodologis: dengan *encoder* beku, kualitas *embedding* terpralatih untuk isyarat SIBI terbaca langsung dari kinerja kepala, sehingga sumbangan pretraining terpisah dari sumbangan penyetelan. Karena *encoder* hanya 9.280 parameter, biaya membandingkan skema adaptasi lain pun rendah, dan perbandingannya dijalankan pada data serta seed yang sama.

LoRA menambah pembaruan berperingkat rendah pada tetapan asli tanpa menyimpan gradien untuk seluruh matriks [17]:

```rumus
W~akhir~ = W~0~ + B · A (2.7)
```

dengan W~0~ matriks tetapan asli yang dibekukan, B berukuran d~keluar~ × r dan A berukuran r × d~masuk~, serta r peringkat adapter yang dipilih jauh lebih kecil daripada ukuran matriks; hanya B dan A yang dilatih. Adapter bekerja di dalam lapisan yang sudah ada sebagai jalur adaptasi yang hemat parameter. Perannya berbeda dari kepala tugas maupun dari pelatihan lanjutan, dan ia bukan prasyarat penelitian ini. Ketersediaannya bahkan terdokumentasi untuk kasus ruangan: kartu model menyertakan adapter `node-1.json` dan `node-2.json` masing-masing sekitar 21 KB [11]. ADR-150 menaksir adapter sekitar 11 KB mampu menyamai kinerja lintas subjek dengan 100 sampai 200 data berlabel per ruang [10]; angka itu berstatus estimasi rancangan, bukan hasil terukur. Kompatibilitas LoRA dengan alur ekspor ke ESP32-S3 belum terverifikasi, sehingga statusnya ditandai [PERLU VALIDASI: kompatibilitas LoRA dengan alur ekspor] dan diperiksa pada T0.

Pembanding ketiga ialah pelatihan lanjutan. Pelatihan sebagian membuka lapis terakhir saja, sedangkan pelatihan penuh membuka seluruh tetapan. Keduanya dijaga dengan EWC sebagaimana pretraining *encoder* melakukannya [11], dan keduanya dilaporkan berdampingan dengan hasil *encoder* beku. Ketiga skema itu (beku, beku plus LoRA, pelatihan lanjutan) diperlakukan sebagai eksperimen pembanding pada Subbab 3.7, bukan keputusan yang dikunci di muka.

## 2.6 Kepala Klasifikasi dan Kerugian Silang-Entropi

Kepala klasifikasi mengubah *embedding* menjadi skor tiap kelas huruf. Untuk K kelas dengan K = 26, skor logit dihitung dari

```rumus
a~i~ = W~c~ · z~i~ + b~c~ (2.8)
```

dengan W~c~ matriks berukuran K × 128 dan b~c~ vektor bias. Skor lalu diubah menjadi probabilitas lewat *softmax*

```rumus
q~ik~ = exp( a~ik~ ) / Σ~k~ exp( a~ik~ ) (2.9)
```

sehingga seluruh probabilitas berjumlah satu, dan kelas prediksi ialah kelas dengan probabilitas terbesar. Sebagai lantai pembanding, tebakan acak seragam pada K kelas bernilai 1/K ≈ 3,8%, dan angka itu dihitung ulang jika himpunan huruf dipangkas. Kerugian pelatihannya silang-entropi kategorikal; dengan label *one-hot* y~ik~ yang bernilai satu pada kelas benar dan nol pada kelas lain, kerugian atas N sampel dalam *batch* berbunyi

```rumus
L~cls~ = − ( 1 / N ) · Σ~i~ Σ~k~ y~ik~ · log q~ik~ (2.10)
```

yang menghukum prediksi yang percaya diri pada kelas salah. Jika data latih terbukti timpang antarhuruf, bobot kelas dipasang berbanding terbalik dengan frekuensi kelasnya; bobot itu dihitung hanya dari data latih dan keputusannya dicatat pada Tabel 3.7.

Klasifikator himpunan tertutup selalu memilih satu kelas, sehingga keluarannya dilengkapi skor keyakinan dan mekanisme penolakan [18]: keyakinan yang rendah memunculkan pesan isyarat tidak dikenali alih-alih menebak salah. Menolak lebih aman daripada menebak kelas yang salah. Ambangnya ditetapkan dari data validasi (Subbab 3.7).

## 2.7 Kepala Regresi 21 Keypoint dan Kerugian Smooth L1 Bermask

Target regresi mengikuti skema 21 *landmark* tangan MediaPipe Hands [19], skema yang sama dipakai *pseudo-labeling* pada dataset visual peneliti. Sesuai `kpt_shape` [21, 3], tiap sampel target memuat 21 titik dengan tiga nilai: koordinat x, koordinat y, dan tanda visibilitas. Komponen ketiga itu ialah penanda visibilitas atau keyakinan deteksi sesuai konvensi dataset dan Ultralytics; koordinat target karenanya dipakai berpasangan (x, y) saja, sedangkan visibilitas diperlakukan sebagai mask. Rancangan awal kepala memprediksi koordinat x dan y per bingkai waktu,

```rumus
Q~i~ = reshape( W~r~ · z~i~ + b~r~, T, 21, 2 ) (2.11)
```

dengan W~r~ matriks berukuran 42T × 128 untuk jendela ber-T bingkai, Q~i~ prediksi *keypoint*, dan P~i~ koordinat acuan dari guru visual. Bentuk keluaran per bingkai dipilih karena J dan Z dibedakan oleh lintasan gerak, bukan oleh satu pose. Jika eksperimen menunjukkan regresi cukup dipakai sebagai supervisi tambahan pada satu pose, dimensi T dilepas dan keterbatasannya untuk J dan Z dijelaskan di laporan. Keputusan ini dicatat pada Tabel 3.7.

Sistem koordinat target harus dibakukan sebelum pelatihan, dan di sinilah letak kehati-hatianya. Koordinat piksel kamera tidak otomatis dapat diprediksi dari CSI tanpa definisi koordinat, transformasi, atau kalibrasi yang dapat direproduksi. Koordinat itu juga tidak tahan terhadap perubahan posisi kamera, jarak, maupun orientasi. Kandidat yang kuat ialah koordinat ternormalisasi terhadap kotak deteksi guru atau terhadap titik pergelangan tangan. Pilihan finalnya ditetapkan pada T0 lalu dipakai konsisten oleh guru dan murid [PERLU VALIDASI: sistem koordinat dan normalisasi target regresi]. Kerugian regresinya Smooth L1 yang dibobot mask visibilitas [20]. Fungsi Smooth L1 berperilaku kuadratik dekat nol dan linear untuk galat besar,

```rumus
SmoothL1~δ~( x ) = 0,5 · x^2^ / δ untuk |x| ≤ δ, dan |x| − 0,5 · δ untuk |x| > δ (2.12)
```

dengan δ ambang peralihan, sehingga pencilan anotasi tidak mendominasi gradien. Kerugian bermask dihitung hanya pada titik yang terlihat:

```rumus
L~reg~ = ( Σ~i,t,j~ m~itj~ · SmoothL1~δ~( Q~itj~ − P~itj~ ) ) / ( Σ~i,t,j~ m~itj~ + ε ) (2.13)
```

dengan m~itj~ mask visibilitas dari guru yang bernilai satu jika titik j pada bingkai t terlihat dan nol jika terhalang, serta ε penahan pembagi nol; mask berlaku per *keypoint*, bukan per koordinat. Jika prediksi visibilitas juga diinginkan, kepala tambahan dengan kerugian silang-entropi biner disiapkan sebagai perluasan; keputusan memakainya dicatat pada Tabel 3.7.

## 2.8 Pembelajaran Multitugas, Modul Temporal, dan Kerugian Gabungan

Pembelajaran multitugas melatih beberapa tugas berbarengan di atas representasi yang dibagi, dan representasi yang baik untuk satu tugas kerap menolong tugas lain yang berkaitan [21]. Kedua tugas penelitian ini memang dua pandangan atas isyarat yang sama: kepala klasifikasi membacanya sebagai kelas diskret, sedangkan kepala regresi membacanya sebagai bentuk jari kontinu. Hipotesis kerjanya, supervisi *keypoint* ikut merapikan batas antarhuruf yang bentuknya mirip. Kerugian gabungan menjumlah keduanya dengan bobot:

```rumus
L~total~ = λ~cls~ · L~cls~ + λ~reg~ · L~reg~ (2.14)
```

Penetapan bobotnya tidak asal pilih. Silang-entropi bergerak pada orde logaritma jumlah kelas, sedangkan Smooth L1 bergerak pada satuan koordinat. Keduanya karena itu disamakan skalanya lebih dulu, misalnya dengan membagi tiap kerugian oleh nilai rata-ratanya pada epoch pertama; bobot λ baru ditala dari data validasi (Tabel 3.7). Konflik gradien antartugas dipantau lewat besar gradien tiap kepala; jika keduanya menarik representasi ke arah berlawanan, penyeimbangan gradien atau pelatihan bergantian dipertimbangkan dan perlakuannya dilaporkan. Pada baseline, pembaruan tetapan hanya menyentuh kepala beserta modul temporalnya:

```rumus
θ~c~, θ~r~ ← Optimizer( ∇ L~total~ ), θ~0~ tetap (2.15)
```

dengan θ~c~ dan θ~r~ tetapan kedua kepala serta θ~0~ tetapan *encoder* yang dibekukan.

Satu komponen dari rancangan lama tetap dipertahankan dan dievaluasi ulang perannya: 1D-CNN. Pada rancangan lama ia menjadi kepala tunggal di atas *backbone*. Pada rancangan ini ia kandidat modul temporal, yaitu peringkas barisan *embedding* per bingkai menjadi satu vektor sebelum kedua kepala, yang bersaing dengan alternatif lebih sederhana berupa agregasi statistik rata-rata dan maksimum. Modul temporal bukan kepala tugas: keluarannya tetap masuk bagi kedua kepala, dan model tetap memiliki dua keluaran tugas utama. Parameter modul temporal ikut dilatih bersama kepala pada Persamaan 2.15. Keputusan mempertahankannya atau menggantinya diambil dari hasil ablasi pada data yang sama (Subbab 3.7), bukan dari preferensi implementasi. Untuk menguji manfaat penggabungan itu, kepala tunggal yang dilatih sendiri-sendiri juga disiapkan sebagai pembanding pada split yang sama.

## 2.9 Guru Visual YOLO26m-Pose dan Supervisi Lintas Modalitas

Guru visual bekerja hanya pada tahap akuisisi data. Kamera laptop dan node penerima CSI merekam serentak dengan penanda waktu yang sama; pada tiap bingkai, YOLO26m-Pose [12] menghasilkan kelas isyarat beserta 21 *keypoint* tangan dan visibilitasnya. Label kelas dicocokkan dengan kartu pemandu protokol perekaman sehingga derau label terkendali. Kemampuan guru sudah teruji pada tahap pra-penelitian di repositori WPC milik peneliti. Dataset versi 2 memuat 49 kelas isyarat dengan total 7.210 gambar yang terbagi menjadi 6.231 latih, 650 validasi, dan 329 uji; *keypoint*-nya dihasilkan lewat *pseudo-labeling* MediaPipe HandLandmarker [19]. Eksperimen `exp11_huruf24` pada 24 huruf statis mencatat *pose* mAP50 0,9580 dengan akurasi huruf 97,6%. Dari angka itu terbaca bahwa 21 titik artikulasi jari memuat informasi cukup untuk gestur mikro SIBI. Perlu ditegaskan dua hal: seluruh angka itu adalah hasil model visual pada data visual, bukan hasil model Wi-Fi. Selain itu, dataset itu tidak memuat satu pun rekaman CSI, sehingga pasangan data baru harus direkam sendiri pada T2.

Istilah untuk pola pengawasan ini dipilih dengan hati-hati. Karena murid hanya menerima label keras berupa kelas dan koordinat dari guru, istilah yang presisi ialah supervisi lintas modalitas berpandu guru atau *pseudo-label supervision*. Distilasi pengetahuan klasik yang memindahkan probabilitas lunak antarmodel tidak menggambarkan bentuk transfer ini [22]. Konsep guru-murid tetap dipertahankan secara luas: YOLO26m-Pose adalah guru visual saat akuisisi dan pelatihan, sedangkan model CSI adalah murid yang dipakai tanpa kamera pada inferensi akhir. Konsekuensi status pseudo-label juga dijalani jujur: keluaran guru yang belum diperiksa manusia bukan *ground truth* sempurna. Protokol perekaman karena itu menyertakan verifikasi sampel oleh validator, penyaringan bingkai gagal deteksi, dan pencatatan *jitter keypoint* (Subbab 3.6). Ekspektasi generalisasinya dijaga memakai temuan model pose MM-Fi [15]. Kinerja lintas subjek *zero-shot* hanya sekitar 64% dan lintas lingkungan 17,5%, naik ke 72% sampai 78% setelah kalibrasi 50 sampai 1.000 bingkai per orang. Angka itu dipakai sebagai acuan ekspektasi sekaligus alasan skema kalibrasi per orang dan per ruang disiapkan sebagai jalur cadangan (Tabel 3.8).

## 2.10 Pengenalan Isyarat Berbasis CSI dan Inferensi pada Perangkat

Riset pengenalan bahasa isyarat dari CSI sudah berjalan di beberapa negara. SignFi mengenali 276 isyarat ASL dengan akurasi hingga 99,8% di laboratorium, walau turun menjadi 86,66% ketika diuji pada lima pengguna baru [7]; namun, jalur ini belum menyentuh SIBI. Kebaruan penelitian ini ada pada penerapan CSI untuk alfabet SIBI, formulasi dua kepala tugas di atas *encoder* terpralatih, serta penyatuan dua arah bersama pemrosesan bahasa Indonesia (Subbab 2.15). Model utamanya kini tiga bagian: *encoder* terpralatih yang dibekukan (Subbab 2.4), modul temporal untuk deret waktu (Subbab 2.8), dan dua kepala tugas. Pembandingnya sesama model CSI, yaitu varian kepala tunggal tanpa kepala regresi yang dilatih pada data dan seed sama (ablasi, Subbab 3.7). Inferensi dirancang berjalan langsung di modul. ESP-DL membuktikan hal itu mungkin dengan contoh pengenalan gestur tangan int8 69,2 ms pada keluarga ESP32 [23]. TensorFlow Lite Micro menjadi alternatifnya. Tolok ukur CSI-isyarat pada ESP32-S3 sendiri belum ada, jadi waktu inferensi aktual diukur sendiri (Subbab 3.7).

## 2.11 TTS dan ASR Bahasa Indonesia

Purwarupa membutuhkan mesin sintesis ucapan (*text-to-speech*, TTS) dan pengenalan ucapan (*automatic speech recognition*, ASR). Tiga kriteria menyeleksi keduanya: dukungan bahasa Indonesia terverifikasi, jalur *on-device* dan lokal tersedia, serta biaya berkelanjutan yang masuk akal bagi sekolah. Mesin TTS *on-device* yang direncanakan ialah Kokoro-82M ONNX bersama sekitar 82 juta parameter [24]. Mesinnya berjalan luring di ponsel melalui ONNX Runtime. *Model card* resminya mencantumkan delapan bahasa tanpa bahasa Indonesia, sehingga ketersediaan suara Indonesia perlu diverifikasi pada gerbang G3; jika memang belum tersedia, jalur beralih ke MMS-TTS-ind, model TTS Indonesia dari Meta [25]. Layanan TTS dan ASR awan hadir sebagai pembanding latensi dan mutu, dan pilihan finalnya ditetapkan setelah uji banding (Tabel 3.7).

Pada sisi ASR, Whisper dilatih dengan lima juta jam audio dan mendukung lebih dari 100 bahasa, termasuk Indonesia [26]. Ketika internet terputus, server lokal mengambil alih dengan implementasi faster-whisper sebagai cadangan. Galat kata Whisper untuk percakapan bahasa Indonesia belum terverifikasi dari sumber primer, jadi akurasinya diukur sendiri pada skenario pengujian (Subbab 3.8).

## 2.12 Pemetaan Teks ke Representasi SIBI di Layar

Terjemahan teks menjadi isyarat tidak mungkin dilakukan kata demi kata karena bahasa isyarat memiliki tata bahasa sendiri. Arah kedua karenanya dirancang pada tingkat kamus kata dengan ejaan jari sebagai cadangan. Struktur SIBI mendukung rancangan ini sebab alfabet manualnya lengkap: 26 huruf dan 9 angka [3].

Tampilan pada arah kedua disusun atas dua lapis. Lapis utama memunculkan glos dan gambar bentuk tangan untuk kata yang tersedia di kamus; ukuran gambarnya sekitar dua puluh sampai tiga puluh kilobita sehingga muat di penyimpanan modul. Lapis kedua berupa animasi yang dialirkan dari server, jika waktu pengembangan memungkinkan. Kata di luar kamus dialihkan ke ejaan jari. Sebagai metrik utama arah ini, cakupan kamus, yaitu proporsi kata uji yang terwakili, diukur dan dilaporkan (Subbab 3.8).

## 2.13 Komunikasi Modul, Server, dan Topologi Jaringan

Seluruh perangkat, dari kedua modul penginderaan sampai ponsel, berbagi satu kanal Wi-Fi yang sama sehingga penangkapan CSI berjalan serentak dengan komunikasi data [10]. Peran jembatan jaringan sekaligus penjangkar kanal dipegang *access point*, yang bentuknya bisa *router* sekolah maupun *hotspot* ponsel. Sinkronisasi antarmodul memakai ESP-NOW, sedangkan aliran data ke server memakai UDP [10].

Perangkat lunak server ditulis seluruhnya dalam Rust: konkurensi ditangani Tokio, Axum menyediakan HTTP dan WebSocket, Leptos membangun dasbor yang dikompilasi ke WASM, dan Tauri menjadi aplikasi klien ponsel. Alasannya praktis. Tanpa pengumpul sampah, pemrosesan bingkai UDP tetap cepat; binernya hemat memori; dan satu sistem tipe mendeteksi perubahan format bingkai saat kompilasi. Target *parsing* di bawah 0,2 ms dan memori server di bawah 40 MB adalah target rancangan yang baru diukur pada gerbang G3, bukan hasil yang dijanjikan. Server lokal pada laptop menjalankan server RuView, server Rust, faster-whisper, dan TTS MMS sebagai jalur cadangan tanpa internet. Perlu dicatat pemisahan bahasanya: pelatihan model berjalan di komputer dengan Python dan PyTorch (Subbab 3.7), sedangkan Rust dipakai untuk *runtime* server dan klien; keduanya tidak saling menggantikan.

## 2.14 Evaluasi Kelayakan

Penilaian kelayakan berjalan bertahap lewat lima gerbang G0 sampai G4 (BAB III), dan tiap tahap menghasilkan artefak tetap sehingga kegagalan pun tetap terdokumentasi. Rekomendasi akhirnya menyatakan posisi purwarupa pada skala kesiapterapan teknologi (TKT) yang mengikuti kerangka *technology readiness level* [27]. Kinerja klasifikasi diukur dengan akurasi, presisi, *recall*, skor F1 makro, serta *confusion matrix* per isyarat, selalu dibandingkan terhadap peluang acak. Untuk kelas huruf k, presisi dan *recall* dihitung dari jumlah benar positif TP~k~, salah positif FP~k~, serta salah negatif FN~k~ pada *confusion matrix*:

```rumus
P~k~ = TP~k~ / ( TP~k~ + FP~k~ ) (2.16)
```

```rumus
R~k~ = TP~k~ / ( TP~k~ + FN~k~ ) (2.17)
```

```rumus
F1~k~ = 2 · P~k~ · R~k~ / ( P~k~ + R~k~ ) (2.18)
```

```rumus
F1~makro~ = ( 1 / K ) · Σ~k~ F1~k~ (2.19)
```

```rumus
p~acak~ = 1 / K (2.20)
```

Untuk K = 26 huruf, p~acak~ ≈ 3,8%, dan angka ini dihitung ulang jika himpunan huruf dipangkas (Subbab 3.8.2). Kinerja kepala regresi diukur dengan MPJPE, yaitu rata-rata jarak Euclid antara prediksi dan acuan pada titik yang terlihat,

```rumus
MPJPE = ( Σ~i,t,j~ m~itj~ · || Q~itj~ − P~itj~ || ) / Σ~i,t,j~ m~itj~ (2.21)
```

serta PCK, yaitu proporsi *keypoint* yang galatnya masuk ambang relatif,

```rumus
PCK@α = ( Σ~i,t,j~ m~itj~ · 1( || Q~itj~ − P~itj~ || ≤ α · d~ref~ ) ) / Σ~i,t,j~ m~itj~ (2.22)
```

dengan 1(·) bernilai satu jika kondisinya terpenuhi, α ambang relatif, dan d~ref~ skala acuan yang mengikuti sistem koordinat yang dibakukan (Subbab 2.7); NME dilaporkan sebagai alternatif yang ternormalisasi. Galat per *keypoint* juga diringkas untuk mengenali titik jari mana yang paling sulit diprediksi dari CSI. Pada jalur ucapan, kesalahan pengenalan kata diukur dengan laju galat kata (*word error rate*, WER), yaitu jumlah substitusi S, penghapusan D, dan penyisipan I terhadap N kata acuan:

```rumus
WER = ( S + D + I ) / N (2.23)
```

dan akurasi kata dilaporkan sebagai 1 − WER. Pembagian acak di dalam satu sesi tidak dipakai sebab repetisi berurutan bisa membocorkan informasi latih ke uji. Empat dimensi tambahan menilai kelayakan alat komunikasinya: latensi ujung ke ujung, cakupan kamus, keandalan operasional, dan biaya. Persepsi pengguna diukur dengan kuesioner skala Likert [28] lalu dianalisis secara deskriptif, sedangkan kewajaran keluaran dinilai validator penutur tunarungu.

## 2.15 Penelitian Terdahulu

Penelitian terdahulu yang paling relevan dibandingkan pada Tabel 2.3, mencakup pengenalan isyarat dan gestur dari sinyal Wi-Fi serta pengenalan isyarat berbasis kamera di Indonesia.

Tabel 2.3 Perbandingan penelitian terdahulu

| No. | Peneliti (Tahun) | Modalitas dan arah | Bahasa isyarat | Bebas kamera | Fokus |
|---|---|---|---|---|---|
| 1 | Ma dkk. (2018) [7] | CSI; isyarat menjadi teks | ASL, 276 isyarat | Ya | Pengenalan berskala besar |
| 2 | Zhang dkk. (2022) [14] | CSI; gestur lintas domain | Gestur umum | Ya | Generalisasi lintas orang dan ruang |
| 3 | Dwijayanti dkk. (2021) [5] | Citra; isyarat menjadi teks | BISINDO | Tidak | CNN pengenalan citra |
| 4 | Penelitian ini | CSI sepasang ESP32-S3; *encoder* terpralatih berkepala dua (klasifikasi dan regresi); supervisi guru visual; inferensi tepi; TTS *on-device* | SIBI, alfabet 26 huruf | Ya | Purwarupa penerjemah dua arah |

Dua kelompok penelitian bisa dibaca dari Tabel 2.3. Pengenalan isyarat dan gestur dari Wi-Fi [7], [14] berjalan tanpa kamera tetapi belum menjangkau SIBI. Riset Indonesia berbasis kamera [5] membuktikan tingginya minat, namun tetap terikat pencahayaan dan garis pandang. Dalam batas penelusuran, publikasi pengenalan isyarat SIBI dari CSI maupun purwarupa dua arah yang memadukannya dengan TTS dan ASR bahasa Indonesia pada ESP32-S3 belum ditemukan. Kebaruan penelitian ini karenanya bersifat kombinatif: CSI satu tautan pada sepasang ESP32-S3 untuk alfabet SIBI, dua kepala tugas di atas *encoder* terpralatih, supervisi lintas modalitas berpandu guru, inferensi tepi, serta integrasi dua arah dengan pemrosesan bahasa Indonesia. Di luar itu, kebaruan tidak diklaim untuk pengenalan kontinu maupun penerjemahan kalimat penuh.

## 2.16 Matriks Justifikasi Pemilihan Komponen

Tabel 2.4 merangkum jawaban atas pertanyaan "mengapa X dan bukan Y" untuk delapan keputusan arsitektur. Seluruh target kinerja di dalamnya adalah target rancangan yang baru diukur pada gerbang BAB III, bukan hasil yang dijanjikan.

Tabel 2.4 Matriks justifikasi pemilihan komponen (Mengapa X dan Bukan Y?)

| No. | Keputusan | Komponen dipilih | Alternatif ditinggalkan | Justifikasi |
|---|---|---|---|---|
| 1 | Tumpukan UI dan server | Seluruhnya Rust: Tokio/Axum, Leptos (WASM), Tauri | Node.js, Streamlit, Electron, React/JS | *Parsing* UDP di bawah 0,2 ms; memori di bawah 40 MB; satu sistem tipe (Subbab 2.13) |
| 2 | Mesin TTS | Kokoro TTS ONNX *on-device*; prasyarat suara Indonesia pada G3; alternatif MMS-TTS-ind [24], [25] | TTS awan, VITS/Tacotron penuh | Model 82 juta parameter diinferensikan luring pada ponsel (Subbab 2.11) |
| 3 | Node penginderaan | ESP32-S3 [8] | ESP32 biasa, C3/C6, Arduino Uno | Instruksi vektor int8; PSRAM penyangga CSI dan model; API CSI resmi (Subbab 2.3) |
| 4 | Penginderaan radio | CSI-Ratio 2,4 GHz kanal 20 MHz [13] | RSSI, radar khusus, *time of flight* | RSSI terlalu kasar; CSI-ratio membersihkan derau fase tanpa perangkat tambahan (Subbab 2.2) |
| 5 | Model guru visi | YOLO26m-Pose 21 *keypoint* [12] | YOLOv8-pose, MediaPipe langsung, UNet | 21 titik artikulasi vital untuk membedakan huruf mirip dan lintasan J/Z; akurasi 97,6% pada pra-penelitian (Subbab 2.9) |
| 6 | Model murid tepi | *Encoder* CSI terpralatih dibekukan + modul temporal + dua kepala [11] | SVM, MLP berat, pelatihan dari nol | *Checkpoint* 9.280 parameter teruji kontrastif; beku memisahkan sumbangan pretraining; target inferensi terkuantisasi di bawah 100 ms (Subbab 2.4 dan 2.8) |
| 7 | Dua kepala tugas | Klasifikasi 26 huruf + regresi 21 *keypoint* dengan kerugian gabungan [21] | Kepala klasifikasi saja | Supervisi *keypoint* berpotensi merapikan batas kelas yang mirip; manfaatnya diuji lewat ablasi (Subbab 3.7) |
| 8 | Metode supervisi | Supervisi lintas modalitas berpandu guru; label keras kelas dan *keypoint* [22] | Pelatihan CSI murni; distilasi *soft target* | CSI abstrak memerlukan supervisi spasial guru; bentuk transfer yang dipakai memang label keras, bukan probabilitas lunak (Subbab 2.9) |

## 2.17 Kerangka Pemikiran dan Arsitektur Model

Kerangka pemikiran penelitian ini mengalir dari data sampai perangkat, seperti dirangkum Gambar 2.2. Sinyal CSI dari sepasang ESP32-S3 melewati praproses dan, jika audit menemukannya perlu, adapter masukan yang menyamakan bentuk jendela CSI dengan ruang masukan *encoder* terpralatih. *Encoder* yang dibekukan menghasilkan barisan *embedding* 128 dimensi; modul temporal meringkasnya menjadi satu vektor bersama, lalu kepala klasifikasi membacanya menjadi kelas huruf dan kepala regresi membacanya menjadi 21 koordinat *keypoint*. Keduanya dilatih serentak dengan kerugian gabungan di bawah supervisi guru visual yang hanya aktif saat akuisisi data. Model terpilih lalu dikuantisasi dan dijalankan di modul, sementara arah kedua sistem tetap berjalan lewat ASR, kamus, dan TTS sebagaimana dirancang (Subbab 3.5).

```mermaid
flowchart TD
    accTitle: Arsitektur model dua kepala tugas di atas encoder CSI terpralatih
    accDescr: Jalur guru visual di sebelah kiri berisi kamera tersinkron dan YOLO26m-Pose yang menghasilkan label kelas dan 21 keypoint acuan, hanya saat akuisisi data. Jalur model Wi-Fi di sebelah kanan berisi CSI dari sepasang ESP32-S3 yang dipraproses, adapter masukan jika perlu, encoder terpralatih yang dibekukan, barisan embedding 128 dimensi, dan modul temporal, lalu kepala klasifikasi menghasilkan prediksi 26 kelas huruf dan kepala regresi menghasilkan prediksi 21 keypoint tangan. Dataset berpasangan menggabungkan kedua jalur, kerugian gabungan melatih dan evaluasi mengukur kedua kepala, dan model terpilih diinferensikan pada ESP32-S3. Simpul kuning ialah jalur guru, simpul biru jalur model Wi-Fi, simpul hijau alur pelatihan dan deployment.

    CAM["Kamera laptop<br/>tersinkron CSI<br/>(hanya akuisisi)"]
    GURU["YOLO26m-Pose<br/>(guru visual) [12]"]
    LAB["Label kelas dan<br/>21 keypoint acuan"]
    CAM --> GURU
    GURU --> LAB

    CSI["CSI sepasang ESP32-S3<br/>(56 subcarrier) [9]"]
    PRE["Praproses: kalibrasi,<br/>segmentasi, jendela"]
    ADP["Adapter masukan<br/>(jika audit memerlukannya)"]
    ENC["Encoder CSI terpralatih<br/>dibekukan [11]"]
    EMT["Embedding 128 per bingkai<br/>+ modul temporal"]
    HCL["Kepala klasifikasi<br/>(Persamaan 2.8)"]
    HRG["Kepala regresi<br/>(Persamaan 2.11)"]
    KLS["Prediksi kelas<br/>26 huruf SIBI"]
    KPT["Prediksi 21 keypoint<br/>tangan (T, 21, 2)"]
    CSI --> PRE
    PRE --> ADP
    ADP --> ENC
    ENC --> EMT
    EMT --> HCL
    EMT --> HRG
    HCL --> KLS
    HRG --> KPT

    PAIR["Dataset berpasangan<br/>(Persamaan 2.24)"]
    LTOT["Kerugian gabungan,<br/>evaluasi dan optimasi<br/>(Subbab 3.7)"]
    EDGE["Inferensi terkuantisasi<br/>pada ESP32-S3"]

    LAB --> PAIR
    PRE -. "tersinkron penanda waktu" .-> PAIR
    PAIR --> LTOT
    KLS --> LTOT
    KPT --> LTOT
    LTOT --> EDGE

    classDef guru fill:#fef9c3,stroke:#ca8a04,stroke-width:2px,color:#713f12
    classDef model fill:#dbeafe,stroke:#2563eb,stroke-width:2px,color:#1e3a5f
    classDef proses fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#14532d
    class CAM,GURU,LAB guru
    class CSI,PRE,ADP,ENC,EMT,HCL,HRG,KLS,KPT model
    class PAIR,LTOT,EDGE proses
```

Gambar 2.2 Arsitektur model jalur isyarat menjadi teks: satu encoder CSI terpralatih yang dibekukan, modul temporal, dua kepala tugas yang berbagi representasi, jalur guru visual yang hanya aktif saat akuisisi data, dan jalur deployment ke ESP32-S3; simpul kuning = jalur guru visual, biru = jalur model Wi-Fi, hijau = pelatihan dan deployment

Dataset yang menopang kerangka ini dirumuskan sebagai pasangan berunsur:

```rumus
D~pas~ = { ( X~i~, y~i~, P~i~, m~i~, s~i~, q~i~ ) }, i = 1, ..., N (2.24)
```

dengan X~i~ jendela CSI, y~i~ label kelas isyarat, P~i~ koordinat 21 *keypoint* acuan, m~i~ mask visibilitasnya, s~i~ metadata subjek, sesi, ruang, serta perangkat, dan q~i~ skor kualitas anotasi guru; keseluruhan pasangan direkam sendiri pada T2 karena tidak ada sumber lain yang menyediakannya. Dengan rumusan itu, teori CSI dan zona Fresnel (Subbab 2.2) menyediakan sinyal, *encoder* terpralatih (Subbab 2.4) menyediakan representasi, dan transfer learning (Subbab 2.5) menyediakan skema adaptasi. Kedua formulasi kepala (Subbab 2.6 dan 2.7) menyediakan keluaran tugas, pembelajaran multitugas (Subbab 2.8) mengikat semuanya dalam satu kerugian, dan guru visual (Subbab 2.9) menyediakan labelnya sebelum hasilnya diukur di tepi (Subbab 2.10).
# BAB III METODE PENELITIAN

## 3.1 Desain Penelitian

Penelitian ini berbentuk studi kelayakan kuantitatif bergerbang. Sisi kuantitatifnya mengukur tiga hal: kemampuan CSI dari satu tautan antarmodul ESP32-S3 membedakan 26 huruf alfabet manual SIBI, kemampuan model terkuantisasi berjalan di modul, dan kinerja kedua jalur penerjemahan. Komponen yang lulus uji dikemas menjadi purwarupa, lalu dinilai lewat uji operasional, uji kegunaan skala kecil, dan penilaian validator penutur tunarungu. Mengapa bergerbang? Belum ada yang membuktikan CSI mampu membedakan isyarat SIBI, dan kemampuan semacam itu tidak boleh diperlakukan sebagai asumsi; setiap tahap menghasilkan artefak tetap, kegagalan gerbang dicatat sebagai temuan, dan kriteria akurasi dirumuskan relatif terhadap peluang acak (Subbab 2.14). Inti pelatihannya adalah supervisi lintas modalitas berpandu guru (Subbab 3.7): keluaran guru kamera YOLO26m-Pose berupa label kelas dan deret 21 *keypoint* mengawasi pelatihan dua kepala tugas di atas *encoder* CSI terpralatih yang dibekukan. Model terpilihnya lalu dijalankan langsung di modul. Rumusan pertama dijawab pada replikasi platform hingga perancangan model, kedua pada uji klasifikasi, regresi, dan *deployment*, ketiga pada uji operasional, kegunaan, dan penilaian validator.

## 3.2 Tahapan Penelitian

Empat belas minggu (M1 sampai M14) dibagi ke dalam enam tahap: replikasi platform dan karakterisasi (T0), kurasi isyarat dan protokol (T1), perekaman *dataset* serta pelatihan dua kepala (T2), uji generalisasi (T3), pengemasan purwarupa dan uji penerimaan (T4), serta analisis dan penulisan (T5). Lima gerbang keputusan menutup rangkaian itu dengan kriteria dan tindakan jika gagal yang dirinci pada Tabel 3.5; penerimaan pengguna dan biaya dinilai G4, yang kemudian menyusun rekomendasi posisi TKT/TRL 3–4 [27]. Alur lolosnya dirangkum pada Gambar 3.1. Jika G0 gagal dua kali, jalur CSI dihentikan dan dilaporkan sebagai temuan; kriteria seluruh gerbang difinalkan bersama pembimbing sebelum dinilai (Tabel 3.7).

```mermaid
flowchart LR
    accTitle: Tahapan penelitian T0 sampai T5 dengan gerbang keputusan G0 sampai G4
    accDescr: Diagram dua fase. Fase pembangunan data berisi T0 replikasi platform dan audit checkpoint encoder, gerbang G0 baseline, T1 kurasi isyarat, dan T2 perekaman dataset serta pelatihan dua kepala. Fase pengujian berisi kuantisasi model, gerbang G1 model tepi, T3 uji generalisasi, gerbang G2 konsultasi tiga pilar, T4 pengemasan purwarupa, gerbang G3 integrasi mesin ucapan, gerbang G4 sintesis kelayakan, dan T5 analisis serta penulisan.

    subgraph KA["Fase pembangunan data (M1–M8)"]
        direction TB
    T0["T0 Replikasi platform, verifikasi<br/>CSI 56 subcarrier pada 1 m, uji Delta-CSI,<br/>koeksistensi, audit checkpoint encoder (M1–M2)"]
    G0("G0 akhir M2: baseline CSI-jaringan:<br/>UDP Rust tanpa kehilangan paket,<br/>akuisisi stabil, gerak terpisah")
    T1["T1 Kurasi isyarat, kalibrasi ruang,<br/>protokol, etika, rintisan separabilitas<br/>pasangan huruf mirip (M2–M4)"]
    T2["T2 Perekaman dataset dan<br/>pelatihan dua kepala di atas<br/>encoder beku (M4–M8)"]
    T0 --> G0
    G0 -- "lolos" --> T1
    T1 --> T2
    end
    subgraph KB["Fase pengujian dan penulisan (M8–M14)"]
        direction TB
    T2B["Kuantisasi model terpilih dan uji<br/>deployment encoder berkepala dua<br/>ke modul ESP32-S3"]
    G1("G1 akhir M8: model tepi terkuantisasi:<br/>akurasi skema, ablasi multitugas dilaporkan,<br/>inferensi di bawah 100 ms")
    T3["T3 Uji generalisasi: lintas sesi,<br/>partisipan, ruang, posisi<br/>berdiri/duduk (M8–M10)"]
    G2("G2 akhir M10: konsultasi 3 pilar<br/>pakar SIBI, RF, embedded AI<br/>tanpa temuan blok kritis")
    T4["T4 Pengemasan dua arah, full-stack<br/>Rust, TTS on-device, uji penerimaan<br/>dan biaya (M10–M12)"]
    G3("G3 M11: integrasi Rust dan mesin<br/>ucapan on-device dalam<br/>anggaran latensi")
    G4("G4 akhir M12: sintesis kelayakan,<br/>penerimaan dan biaya layak,<br/>rekomendasi TKT/TRL 3–4")
    T5["T5 Analisis dan penulisan<br/>(M12–M14)"]
    T2B --> G1
    G1 -- "lolos" --> T3
    T3 --> G2
    G2 -- "lolos" --> T4
    T4 --> G3
    G3 -- "lolos" --> G4
    G4 -- "lolos" --> T5
    end
    KA --> KB
```

Gambar 3.1 Tahapan penelitian T0–T5 dan gerbang keputusan G0–G4 (jalur lolos; tindakan jika gagal pada Tabel 3.5)

Tahap T0 sampai T2 lebih dulu membangun dasar data. T0 menyiapkan dua modul dengan *firmware* `esp32-csi-node` RuView [10], lalu menjalankan empat uji tanpa partisipan. Uji itu mencakup verifikasi 56 *subcarrier* stabil pada jarak baku 1 meter, uji Delta-CSI (Subbab 3.8.1), koeksistensi radio dengan *streaming* audio aktif, dan pengukuran laju pencuplikan. T0 juga mengaudit *checkpoint encoder* [11]: bentuk masukan, jumlah parameter, normalisasi L2, dukungan ekspor, dan kompatibilitas LoRA (Subbab 3.7). T1 meliputi kurasi 26 huruf bersama validator, kalibrasi ruang, protokol dan etika, serta perizinan (Subbab 3.6); pasangan huruf paling mirip juga ditetapkan di sini sebagai bahan gerbang G1.

Pada T2, *dataset* kurang lebih 30 repetisi per isyarat per sesi direkam disertai video yang tersinkron (Subbab 3.6). Alur pelatihannya berbentuk supervisi berpandu guru: segmen disaring lewat *keypoint* guru, jendela CSI disandingkan dengan label guru berdasarkan penanda waktu, lalu kedua kepala dilatih di atas *encoder* yang dibekukan dengan kerugian gabungan. Model terpilih selanjutnya dikuantisasi dan diuji di modul (Subbab 3.7). T2 melahirkan *dataset* berlabel, model terlatih, dan laporan *deployment*. G1 menilai hasilnya; jika gagal, cakupan dipangkas menjadi himpunan huruf dengan pembeda CSI terkuat (Tabel 3.7).

Tahap T3 sampai T5 berisi pengujian dan pelaporan. Generalisasi lintas sesi, partisipan, ruang, serta posisi berdiri-duduk diuji pada T3, termasuk pada satu pengguna baru tanpa pelatihan ulang (Subbab 3.7) dengan acuan Widar3.0 [14]. Jika ketahanan lintas pengguna rendah, cakupan berubah menjadi personalisasi per pengguna dan dilaporkan sebagai temuan. T4 mengemas model menjadi purwarupa dua arah (Subbab 3.5), menjalankan uji operasional dan jalur ucapan (Subbab 3.8) yang dinilai G3. Rangkaian itu ditutup uji penerimaan, penilaian validator, dan analisis biaya yang dinilai G4. Pada T5, seluruh artefak dianalisis dan laporan kelayakan disusun lengkap dengan rekomendasi TKT/TRL 3–4 [27] beserta keterbatasan eksplisitnya (Subbab 1.4).

## 3.3 Waktu dan Lokasi Penelitian

Pelaksanaan penelitian jatuh pada [PERLU DATA: bulan dan tahun pelaksanaan penelitian] di Jawa Timur. Penelitian ini tidak bersandar pada mitra lembaga; partisipan direkrut langsung oleh peneliti, sedangkan perekaman dan pengujian berlangsung di sedikitnya dua ruang berbeda, misalnya ruang kelas dan ruang kerja, sebagai jumlah minimum skema *leave-one-room-out*. Tiap ruang dikalibrasi lebih dulu sebelum perekaman (Subbab 3.5).

## 3.4 Alat dan Bahan

Tabel 3.1 dan Tabel 3.2 menyajikan perangkat keras dan perangkat lunak penelitian. Node penginderaan dipegang sepasang modul ESP32-S3: TX memancarkan *beacon* ESP-NOW, sedangkan RX mengekstrak CSI 56 *subcarrier* pada 2,4 GHz kanal 20 MHz sekaligus memuat antarmuka. Supaya eksperimen bisa diulang, versi perangkat lunak dicatat bersama log pelatihan. Bahan penelitiannya meliputi *checkpoint encoder* terpralatih [11], *dataset* CSI berpasangan yang direkam sendiri, dataset citra WPC beserta model guru YOLO26m-Pose dari repositori peneliti, lembar definisi huruf, aset tampilan arah kedua, formulir persetujuan, instrumen uji, dan kuesioner persepsi. Perekaman dilakukan sendiri karena pengenalan isyarat SIBI dari CSI memang belum ditemukan dalam penelusuran (Subbab 2.15).

Tabel 3.1 Perangkat keras penelitian

| No. | Nama | Spesifikasi | Jumlah | Keterangan |
|---|---|---|---|---|
| 1 | Modul ESP32-S3 | PSRAM 8 MB; 2,4 GHz 802.11b/g/n, kanal 20 MHz (56 *subcarrier*), 1T1R; varian yang direkomendasikan RuView [10] | 2 unit | Node TX (pemancar *beacon*) dan node RX (penerima CSI dan antarmuka) |
| 2 | Layar modul | OLED 0,96 inci I2C (128×64) atau TFT 1,3 inci SPI (240×240) [PERLU DATA: model final] | 1 unit | Tampilan huruf, baterai, kanal, mode kerja |
| 3 | *Rotary encoder* EC11 dan tombol tekan | Putar 360 derajat, 20 detak per putaran, tombol terintegrasi; sakelar sesaat *pull-up* internal | 1–2 unit | Navigasi menu, sensitivitas, tekan-untuk-bicara, reset |
| 4 | Pengeras suara dengan DAC I2S | Mini 8 Ohm 3 W, penguat kelas D MAX98357A | 1 set | Pemutaran suara TTS dari modul |
| 5 | Mikrofon I2S | INMP441, MEMS omnidireksional, SNR 61 dBA | 1 unit | Pintu suara arah kedua |
| 6 | Baterai Li-Po, BMS 1S, pengisi TP4056 | Li-Po 3,7 V 2.500–3.000 mAh [PERLU DATA: kapasitas final berdasarkan uji arus]; proteksi; pengisi 1 A USB-C | 1–2 set | Daya portabel, proteksi, dan pengisian |
| 7 | Laptop | ASUS TUF Dash F15 FX516PR: i7-11370H, RTX 3070 Laptop 8 GB VRAM, RAM 16 GB | 1 unit | Akuisisi jalur guru, pelatihan dua kepala, evaluasi, server cadangan |
| 8 | Ponsel pintar | Poco F4 5G: Snapdragon 870, RAM 6 GB, Android | 1 unit | *Hotspot* portabel, klien Tauri, mesin TTS *on-device* |
| 9 | *Access point* | *Router* Wi-Fi 2,4 GHz dengan internet [PERLU DATA: pilihan final] | 1 unit | Jembatan jaringan dan penjangkar kanal, bukan penginderaan |
| 10 | *Webcam* | Bawaan laptop | 1 unit | Hanya untuk jalur guru |

Foto pada Gambar 3.2 memudahkan mengenali bentuk sembilan perangkat pada Tabel 3.1; webcam memakai bawaan laptop sehingga tidak difoto terpisah. Foto produk hanya menjadi pengenal bentuk, bukan acuan merek maupun spesifikasi, dan rujukan spesifikasinya tetap Tabel 3.1 [PERLU ILUSTRASI: foto dokumentasi sendiri setelah seluruh perangkat dibeli].

```gambar
Sumber skrip: scripts/sensesibi-v10/gambar_g15_alatbahan.py (grid foto hasil pencarian gambar daring) -> assets-v16/gambar-3.2.png
```

Gambar 3.2 Perangkat keras penelitian; huruf pada tiap foto mengikuti baris Tabel 3.1 (foto produk sebagai pengenal bentuk, bukan acuan merek)

Tabel 3.2 Perangkat lunak penelitian

| No. | Nama | Fungsi dalam penelitian |
|---|---|---|
| 1 | *Firmware* dan *server* RuView [10] | Menangkap CSI, mengirim UDP, kalibrasi ruang, segmentasi |
| 2 | *Checkpoint* encoder CSI terpralatih `ruvnet/wifi-densepose-pretrained` beserta adapter LoRA ruangannya [11] | *Encoder* murid yang dibekukan pada baseline; kandidat adaptasi LoRA |
| 3 | `scripts/collect-ground-truth.py` (diadaptasi) | Sinkron kamera-CSI; estimator memakai YOLO26m-Pose |
| 4 | Model guru YOLO26m-Pose dan repositori alur kerja YOLO26 peneliti [12] | Ekstraksi *keypoint*; konversi *dataset*, pelatihan deterministik, pencatatan eksperimen (Subbab 3.7) |
| 5 | Layanan GPU Kaggle | Pelatihan lanjutan guru dan pembanding adaptasi *encoder* jika GPU lokal tidak cukup |
| 6 | Python dan PyTorch | Pelatihan dua kepala, LoRA, pelatihan lanjutan, evaluasi; kompatibel dengan *checkpoint* dan mendukung autograd |
| 7 | ESP-DL dengan akselerasi ESP-NN (alternatif: TensorFlow Lite Micro) [23] | Menjalankan model terkuantisasi pada node RX |
| 8 | faster-whisper dan MMS-TTS-ind [26], [25]; layanan ucapan awan [PERLU DATA: layanan final hasil uji banding] | ASR dan TTS cadangan lokal; jalur utama pengenalan ucapan |
| 9 | Rust, Tokio, Axum, Leptos, Tauri | Server seluruhnya Rust, dasbor WASM, aplikasi klien ponsel |
| 10 | Kokoro TTS ONNX dan ONNX Runtime [24] | Mesin TTS *on-device*; prasyarat suara Indonesia pada G3 |
| 11 | Kamus label-teks dan teks-isyarat | Dikembangkan sendiri; kamus label-teks dimuat pada modul |

## 3.5 Perancangan Sistem

Gambar 3.3 memperlihatkan keseluruhan sistem: dua jalur operasional tanpa kamera ditambah satu jalur guru yang hanya aktif saat akuisisi dan pelatihan. Pada arah pertama, *beacon* ESP-NOW node pemancar melintasi zona isyarat, gerak pengisyarat mengubah deret CSI yang ditangkap node penerima, lalu model *encoder* berkepala dua yang terkuantisasi menghasilkan label beserta skor keyakinan. Label itu dipetakan menjadi teks Indonesia di layar dan dibunyikan lewat Kokoro TTS ONNX di aplikasi Tauri secara luring; estimasi *keypoint* dari kepala regresi menjadi keluaran tambahan sesuai rancangan final (Subbab 2.7). Pada arah kedua, tombol tekan-untuk-bicara mengaktifkan mikrofon, ucapan dikenali layanan ASR, dan teks dipetakan ke representasi SIBI dari aset modul (Subbab 2.12). Saat internet terputus, sintesis tetap berjalan *on-device* dan ASR beralih ke server lokal faster-whisper. Jalur guru, yang memakai *webcam* dan YOLO26m-Pose untuk mengekstrak deret *keypoint* sebagai supervisi pelatihan, bukan bagian produk akhir.

```mermaid
flowchart TD
    accTitle: Arsitektur produk akhir tanpa kamera
    accDescr: Tiga rantai. Arah 1 mengalir dari beacon ESP-NOW node pemancar melalui zona isyarat ke node penerima yang menjalankan encoder terpralatih berkepala dua yang terkuantisasi, lalu teks tampil di layar dan dibunyikan Kokoro TTS ONNX di aplikasi Tauri. Arah 2 mengalir dari tombol tekan-untuk-bicara dan mikrofon ke layanan ASR awan, lalu teks dan representasi SIBI tampil di layar. Jalur guru memakai webcam dan YOLO26m-Pose untuk supervisi pelatihan. Garis putus-putus menandai beralih ke server lokal saat internet terputus.

    subgraph A1["Arah 1: isyarat menjadi teks dan suara"]
        TX["Node TX: beacon<br/>ESP-NOW"]
        ZN["Zona isyarat<br/>(satu pengisyarat)"]
        RX["Node RX: CSI promiscuous +<br/>encoder terpralatih berkepala dua<br/>terkuantisasi + antarmuka"]
        MAPL["Kamus label-teks<br/>di modul"]
        DSP1["Layar modul:<br/>teks hasil"]
        TTS["Mesin TTS on-device:<br/>Kokoro ONNX di aplikasi<br/>Tauri (Poco F4 5G)"]
        SPK["Speaker +<br/>rotary encoder"]
        TX --> ZN
        ZN --> RX
        RX --> MAPL
        MAPL --> DSP1
        MAPL -- "teks via Wi-Fi" --> TTS
        TTS -- "audio" --> SPK
    end

    subgraph A2["Arah 2: ucapan menjadi representasi SIBI"]
        BTN["Tombol<br/>tekan-untuk-bicara"]
        MIC["Mikrofon<br/>I2S"]
        STT["Layanan<br/>ASR awan"]
        DSP2["Layar modul: teks lalu<br/>representasi SIBI"]
        AST["Aset SIBI: glos,<br/>gambar, ejaan jari<br/>(Subbab 2.12)"]
        BTN --> MIC
        MIC -- "audio via Wi-Fi" --> STT
        STT -- "teks" --> DSP2
        AST --> DSP2
    end

    subgraph AG["Jalur guru (hanya akuisisi dan pelatihan)"]
        CAM["Webcam laptop"]
        Y26P["YOLO26m-Pose:<br/>21 keypoint pose tangan"]
        SUP["Supervisi pelatihan<br/>dua kepala (Subbab 3.7)"]
        CAM --> Y26P
        Y26P --> SUP
    end

    LOK["Server lokal (cadangan):<br/>ASR faster-whisper,<br/>TTS MMS, server RuView,<br/>server Rust"]
    TTS -. "TTS lokal" .-> LOK
    STT -. "ASR lokal" .-> LOK
```

Gambar 3.3 Arsitektur produk akhir tanpa kamera. Subgraf arah 1 = isyarat menjadi teks dan suara; subgraf arah 2 = ucapan menjadi representasi SIBI; subgraf jalur guru hanya aktif saat akuisisi dan pelatihan; garis putus-putus = beralih ke server lokal ketika internet tidak tersedia.

Topologi jaringannya menyatukan seluruh perangkat pada satu *access point* dan satu kanal, sehingga penangkapan CSI berjalan serentak dengan komunikasi data (Subbab 2.3). Node pemancar memancarkan *beacon* sebagai sumber bingkai CSI, sedangkan node penerima mengirim bingkai, label, dan skor melalui UDP kepada server Rust sebagai telemetri riset. Server lokal menjalankan server RuView, server Rust, faster-whisper, serta MMS-TTS-ind sebagai jalur cadangan.

Kedua modul dipasang setinggi dada dan saling mengapit zona isyarat; uji Delta-CSI memeriksa kesesuaiannya. Zona hanya ditempati satu pengisyarat per sesi, sistem tidak mengidentifikasi individu, dan jarak antarmodul (baku 1 meter) ditetapkan pada T0 lalu dicatat dalam metadata sesi (Tabel 3.7). Karena CSI peka terhadap perubahan ruang [10], [14], setiap sesi diawali kalibrasi ruang bawaan RuView selama kurang lebih empat menit dengan 600 bingkai dan 8 *anchor*. Posisi perabot, pendingin ruangan, serta orang yang lewat dicatat sebagai kovariat analisis.

*Enclosure* cetak tiga dimensi bahan PLA atau ABS menampung papan, baterai, BMS, TP4056, serta seluruh antarmuka node penerima. Layar, pengeras suara, dan mikrofon berada pada muka depan atau atas, *rotary encoder* dan tombol pada samping, port USB-C pada bawah. Node pemancar dikemas serupa tanpa antarmuka. Pemetaan pin GPIO pada Tabel 3.3 dipilih agar tidak menabrak pin *strapping* (GPIO 0, 3, 45, 46) maupun kanal USB bawaan papan [8], dan diverifikasi ulang pada T0. Rantai dayanya tersusun atas baterai, BMS 1S, TP4056, dan regulator 3,3 volt papan; tegangan baterai diukur lewat pembagi tegangan sehingga persentase baterai bisa tampil di layar. [PERLU DATA: berkas model enclosure final] [PERLU ILUSTRASI: foto atau render enclosure dan tata letak komponennya]

Skema tiga dimensi pada Gambar 3.4 merangkum penempatan seluruh komponen node penerima di dalam enclosure; pemetaan pinnya mengikuti Tabel 3.3 dan dimensinya difinalkan setelah uji T0.

```gambar
Sumber skrip: scripts/sensesibi-v10/gambar_g15_rxnode.py (matplotlib mplot3d) -> assets-v16/gambar-3.4.png
```

Gambar 3.4 Skema penempatan komponen node penerima di dalam enclosure (ilustrasi tiga dimensi, tidak berskala)

Tabel 3.3 Matriks pinout wiring GPIO node penerima

| No. | Subsistem | Pin modul | GPIO ESP32-S3 | Fungsi |
|---|---|---|---|---|
| 1 | Layar I2C (OLED) | SDA / SCL | GPIO 8 / GPIO 9 | Jalur data dan *clock* bus I2C |
| 2 | *Rotary encoder* EC11 | CLK (A) / DT (B) / SW | GPIO 10 / GPIO 11 / GPIO 12 | Detak, arah putaran, tombol |
| 3 | Tombol tekan | OUT | GPIO 13 | Tekan-untuk-bicara dan reset; *pull-up* internal |
| 4 | Mikrofon INMP441 | SCK / WS / SD | GPIO 14 / GPIO 15 / GPIO 16 | *Clock*, *word select*, data I2S penerima |
| 5 | DAC MAX98357A | BCLK / LRC / DIN | GPIO 17 / GPIO 18 / GPIO 21 | *Clock*, penanda kiri-kanan, data I2S pengirim |
| 6 | Pemantau tegangan baterai | ADC | GPIO 1 (ADC1_CH0) | Keluaran pembagi tegangan baterai |

Seluruh perangkat lunak server dan klien ditulis dalam Rust (Subbab 2.13): pendengar UDP bingkai CSI berjalan di atas Tokio, sementara Axum menyediakan HTTP dan WebSocket bagi dasbor Leptos WASM. Aplikasi Tauri pada ponsel menerima teks hasil isyarat sekaligus menjalankan Kokoro TTS ONNX [24]. Target *parsing* bingkai di bawah 0,2 ms serta memori server di bawah 40 MB baru diukur pada G3 (Subbab 3.8.3). Mesin sintesisnya berjalan sepenuhnya di ponsel: Kokoro-82M ONNX diinferensikan luring lewat ONNX Runtime di dalam Tauri [24] dengan target inferensi frasa pendek di bawah 100 ms pada Snapdragon 870. Prasyaratnya hanya satu, yaitu tersedia suara bahasa Indonesia pada Kokoro; jika belum, mesin *on-device* beralih ke MMS-TTS-ind [25] dan peralihan itu dilaporkan.

## 3.6 Protokol Perekaman Dataset, Partisipan, dan Etika

Partisipan terdiri atas 3–4 pengisyarat kompeten, sedikitnya satu validator penutur tunarungu, serta 3–5 pengguna uji dari kelompok sasaran, yaitu guru, siswa tunarungu, dan wali murid. Agar skema lintas sesi bisa dijalankan, setiap pengisyarat direkam dalam sedikitnya dua sesi. Kurasi isyarat mengacu pada *Kamus SIBI* [3]: lembar definisi memuat konfigurasi tangan-jari serta lintasan J dan Z, lalu validator menyetujuinya. Pasangan huruf paling mirip ditetapkan sebagai bahan G1, sedangkan kosakata tampilan arah kedua meliputi 26 huruf dan 9 angka [3] serta kata terpilih. Perekaman memakai *elisitasi* terisolasi, satu huruf per segmen dengan jeda antarrepetisi: huruf statis diperagakan sebagai pose yang ditahan sejenak, J dan Z sebagai lintasan gerak. Prosedur perekaman setiap sesi adalah sebagai berikut.

1. Menyiapkan seluruh peralatan yang dipakai.
2. Memasang kedua modul, pemancar dan penerima, lalu menghubungkan seluruh perangkat ke *access point* pada satu kanal.
3. Menjalankan kalibrasi ruang seraya mencatat metadata sesi: tanggal, ruang, kode pengisyarat, posisi modul, dan kondisi latar.
4. Menjalankan `scripts/collect-ground-truth.py` supaya perekaman CSI dan *webcam* berjalan sinkron dengan penanda waktu bersama, lalu memverifikasi ulang kualitas sinkronisasi lewat uji kejadian di awal sesi, misalnya satu ketukan tangan yang terbaca kedua sensor [PERLU DATA: toleransi sinkronisasi yang diterima].
5. Memunculkan kartu pemandu huruf target, merekam satu repetisi, memberi jeda, lalu mengulanginya sampai setiap huruf mencapai kurang lebih 30 repetisi.
6. Membuang segmen yang tangan tidak terdeteksi model guru, yang mengalami *jitter* *keypoint* ekstrem, atau yang terpotong, lalu mencatat tingkat segmen terbuang dan skor kualitas anotasi tiap segmen.
7. Meminta validator mengambil sampel segmen untuk memeriksa kebenaran bentuk isyarat; label guru berstatus *pseudo-label* sampai pemeriksaan ini selesai.

Baru setelah persetujuan etik dari [PERLU DATA: lembaga atau komisi pemberi persetujuan etik] serta persetujuan tertulis setiap partisipan diperoleh, perekaman dimulai; partisipan berhak mengundurkan diri kapan saja. Formulir persetujuan menerangkan bahwa kamera hanya menyala pada sesi akuisisi jalur guru, produk akhir bebas kamera, dan mode privasi RuView aktif. Video semata-mata dipakai untuk verifikasi batas segmen, penyaringan kualitas, dan diagnosis; penyimpanannya terbatas dan tidak dipublikasikan. Karena audio arah kedua dikirim ke layanan awan, tujuannya diungkapkan pada formulir dan kebijakan penyimpanan layanan diperiksa sebelum dipakai. *Dataset* yang dipublikasikan hanya memuat CSI, label, *keypoint*, dan metadata tanpa identitas.

## 3.7 Pengolahan Sinyal, Pelatihan Dua Kepala, dan Deployment

Bingkai CSI dibatasi *firmware* RuView paling sering setiap 20 ms atau 50 bingkai per detik [10]; laju aktualnya diukur pada T0, dan jika terukur lebih rendah, pita Doppler yang dianalisis dipangkas hingga setengah laju aktual. Deret CSI dipotong menjadi segmen huruf dengan segmentasi energi gerak memakai Delta-CSI, yaitu rata-rata perubahan amplitudo antarbingkai pada seluruh 56 *subcarrier*:

```rumus
d( t ) = ( 1 / 56 ) · Σ~n~ | h~n~(t) − h~n~( t − 1 ) | (3.1)
```

Segmen dianggap memuat gerak jika d(t) melampaui ambang τ selama sekurang-kurangnya panjang jendela minimum; J dan Z terpotong jelas dari energinya, sedangkan huruf statis memakai jendela tahan pose yang ambang dan panjangnya ditetapkan dari data validasi, bukan dari data uji (Tabel 3.7). Fitur tiap segmen, yaitu amplitudo dan fase *subcarrier* terpilih serta spektrum Doppler [6], [14], diringkas menjadi masukan *encoder*.

Langkah berikutnya menutup temuan audit Subbab 2.4: bentuk masukan *checkpoint* harus disesuaikan sebelum dipakai. Kartu model mencatat masukan delapan fitur turunan pada laju 1 Hz [11], sedangkan jalur akuisisi menghasilkan 56 *subcarrier* pada 50 bingkai per detik [9], [10]. Dua jalur penyelesaian karenanya disiapkan: menghitung ulang delapan fitur turunan bawaan RuView dari bingkai CSI, atau melatih adapter masukan kecil yang memetakan jendela CSI ke ruang masukan *encoder* [PERLU VALIDASI: bentuk masukan checkpoint dan rancangan adapter]. Setelah bentuk masukan pasti, *encoder* diterapkan pada tiap bingkai menghasilkan barisan *embedding* 128 dimensi, lalu modul temporal meringkas barisan itu menjadi satu vektor bersama. Kandidat modul temporal ialah 1D-CNN ringan dari rancangan lama atau agregasi statistik; pilihan di antara keduanya diambil dari hasil ablasi pada data yang sama (Subbab 2.8).

*Dataset* murid terbentuk dengan menyelaraskan tiga deret menurut penanda waktu: jendela CSI hasil segmentasi, label huruf guru, dan deret *keypoint* guru. Guru memakai model juara pra-penelitian dari repositori peneliti [12]. Jika rekaman baru memperlihatkan pergeseran domain yang menurunkan kualitas deteksi, guru menjalani pelatihan lanjutan di layanan GPU Kaggle dengan alur kerja yang sudah teruji itu sebelum labelnya dipakai. Seluruh pasangan direkam dalam struktur *dataset* berpasangan Subbab 2.17, lengkap dengan mask visibilitas, metadata sesi, dan skor kualitas anotasi. Enam skema pada Tabel 3.4 mengukur kinerja; untuk skema dalam sesi, pembagiannya temporal per blok dan tidak acak. Data validasi hanya berasal dari data latih, sehingga data uji tidak pernah dipakai untuk memilih *subcarrier*, menormalkan fitur, menetapkan ambang, ataupun menala bobot kerugian (Tabel 3.7).

Tabel 3.4 Skema pembagian data

| No. | Skema | Data latih | Data uji | Aspek yang diukur |
|---|---|---|---|---|
| 1 | Dalam sesi (blok temporal) | Blok awal satu sesi | Blok akhir sesi yang sama | Separabilitas orang, ruang, sesi sama |
| 2 | Lintas sesi | Sebagian sesi pengisyarat di satu ruang | Sesi lain, ruang sama | Ketahanan antarsesi |
| 3 | Lintas partisipan (*leave-one-subject-out*) | Semua pengisyarat kecuali satu | Pengisyarat yang ditinggalkan, bergiliran | Ketahanan pergantian orang |
| 4 | Lintas ruang (*leave-one-room-out*) | Semua ruang kecuali satu | Ruang yang ditinggalkan, bergiliran | Ketahanan pergantian ruang |
| 5 | Pengguna baru | Seluruh pengisyarat | Satu pengguna baru tanpa pelatihan ulang | Kesiapan orang baru |
| 6 | Lintas posisi | Posisi berdiri (atau sebaliknya) | Posisi duduk | Ketahanan pergeseran posisi |

Pelatihan berjalan di komputer dengan Python dan PyTorch karena keduanya kompatibel dengan *checkpoint* dan mendukung autograd serta pengoptimal; layanan GPU Kaggle dipakai jika kapasitas GPU lokal tidak cukup. Baseline dilatih dengan urutan yang eksplisit. *Encoder* dimuat lalu dibekukan, dan geometri *embedding*-nya diverifikasi lewat uji triplet kecil pada data sendiri. Setelah itu, kedua kepala beserta modul temporal dilatih serentak dengan kerugian gabungan Persamaan 2.14 dan 2.15, memakai seed tetap dan *early stopping* pada data validasi. Ablasi dijalankan sebagai rangkaian pembanding pada data dan seed yang sama: kepala klasifikasi saja tanpa kepala regresi, multitugas penuh, dan variasi bobot λ~reg~; manfaat supervisi *keypoint* dibaca dari selisih ketiganya, termasuk jika manfaatnya nihil. Sebagai pembanding lanjutan jika waktu dan data mencukupi, adaptasi LoRA (Persamaan 2.7) [17] dan pelatihan lanjutan sebagian atau seluruhnya dijalankan pada pembagian yang sama. Seluruh hasilnya dilaporkan berdampingan, bukan hanya yang terbaik.

Keluaran klasifikator dilengkapi skor keyakinan dan mekanisme penolakan [18]. Segmen di bawah ambang berujung status penolakan pada kedua arah: *speaker* tidak mengucapkan apa pun dan layar memunculkan pesan isyarat tidak dikenali. Menolak lebih aman daripada menebak kelas yang salah; ambangnya ditetapkan dari data validasi, dan kecukupannya diperiksa lewat laju deteksi palsu serta penilaian validator (Subbab 3.8).

Setelah terpilih, *encoder*, modul temporal, dan kedua kepala digabung menjadi satu *graph* inferensi, lalu dikuantisasi. Skema kuantisasinya affine 8-bit [23]: nilai x dipetakan ke bilangan bulat q lewat skala s dan titik nol z~0~

```rumus
q = round( x / s ) + z~0~, dengan s = ( x~maks~ − x~min~ ) / 255 (3.2)
```

dengan parameter s dan z~0~ dihitung dari data kalibrasi; varian float16, int8, dan int4 dievaluasi masing-masing sesuai dukungan operator pada *runtime*. Jalur ekspornya dinyatakan realistis dan bertahap. Format bobot *checkpoint* diperiksa lebih dulu, lalu operator BatchNorm dan GELU diverifikasi pada *runtime* kandidat di ESP32-S3, baik lewat ESP-DL dengan akselerasi ESP-NN maupun TensorFlow Lite Micro [23]. Klaim dukungan operator tidak dibuat sebelum terverifikasi [PERLU VALIDASI: dukungan operator runtime tepi]. Radio tetap terikat satu kanal bersama *access point* dengan *power save* dimatikan [10]. Alur inferensi pada perangkat tampak pada Gambar 3.5. Bingkai *promiscuous* masuk ke penyangga geser, segmen terdeteksi dari energi gerak, dan masukan *encoder* disiapkan sesuai hasil audit. Model terkuantisasi menghasilkan kelas dan skor, lalu keluaran di atas ambang dikirim melalui UDP. Waktu inferensi per segmen, pemakaian memori, serta pengaruhnya pada laju pemrosesan diukur lalu dilaporkan; jika model terbukti terlalu berat, klasifikasi pindah ke server menurut jalur cadangan (Subbab 3.11).

```mermaid
flowchart LR
    accTitle: Alur inferensi langsung pada ESP32-S3
    accDescr: Bingkai promiscuous masuk ke penyangga geser di PSRAM, segmen terdeteksi dari energi gerak, masukan encoder disiapkan sesuai audit bentuk masukan, model terkuantisasi berupa encoder terpralatih, modul temporal, dan dua kepala menghasilkan kelas beserta skor dan keypoint opsional, keluaran di atas ambang dikirim via UDP, dan keluaran di bawah ambang ditolak sebagai isyarat tidak dikenali.

    subgraph R1["Akuisisi dan segmentasi"]
        direction TB
    CSI["Callback CSI,<br/>mode promiscuous,<br/>filter MGMT"]
    BUF["Penyangga geser<br/>CSI di PSRAM"]
    SEG["Segmentasi energi<br/>gerak (perangkat)"]
    FT["Masukan encoder sesuai<br/>audit bentuk masukan"]
    CSI --> BUF
    BUF --> SEG
    SEG --> FT
    end
    subgraph R2["Model dan keluaran"]
        direction TB
    MOD["Model terkuantisasi:<br/>encoder terpralatih +<br/>modul temporal + dua kepala"]
    DEC{"Skor keyakinan<br/>di atas ambang?"}
    OUT["Label + skor (+ keypoint<br/>opsional) dikirim via UDP"]
    RJ["Label ditolak:<br/>isyarat tidak dikenali"]
    MOD --> DEC
    DEC -- "ya" --> OUT
    DEC -- "tidak" --> RJ
    end
    R1 --> R2
```

Gambar 3.5 Inferensi langsung pada ESP32-S3 dengan model gabungan encoder, modul temporal, dan dua kepala; seluruh waktunya diukur, bukan dijanjikan

## 3.8 Skenario Pengujian dan Metrik Evaluasi

G0 berdiri di atas uji Delta-CSI dan koeksistensi, G1 di atas uji model pada Subbab 3.8.2, G2 di atas konsultasi tiga pilar, G3 di atas uji operasional dan jalur ucapan, serta G4 di atas uji kegunaan, penilaian validator, dan analisis biaya. Satu uji lagi, cakupan kamus, melengkapi analisis tanpa menjadi syarat gerbang.

### 3.8.1 Uji Delta-CSI dan Koeksistensi

Satu pertanyaan dijawab uji Delta-CSI: apakah gerak tubuh menghasilkan perubahan CSI yang terpisah jelas dari kondisi tanpa gerak (ukuran keterpisahannya pada Tabel 3.7). Prosedurnya sebagai berikut.

1. Memasang kedua modul pada posisi awal sehingga mengapit zona isyarat.
2. Merekam CSI dalam tiga kondisi: ruang kosong, pengisyarat diam, dan pengisyarat bergerak.
3. Menjalankan modul penerima dengan CSI, koneksi *station*, dan UDP secara serentak, termasuk saat *streaming* audio, serta mencatat laju CSI aktual dan paket yang hilang.
4. Membandingkan pola antarkondisi, lalu mencatat dan menganalisis hasilnya sebagai bahan G0.

### 3.8.2 Uji Klasifikasi, Regresi, dan Ablasi

Keenam skema Tabel 3.4 diuji dengan metrik Subbab 2.14, selalu dibandingkan terhadap peluang acak sekitar 3,8% untuk 26 kelas; angka acak itu dihitung ulang jika cakupan dipangkas. Akurasi dilaporkan dalam dua versi, yaitu tanpa penolakan pada seluruh segmen uji dan dengan penolakan pada segmen yang diterima. Kinerja kepala regresi dilaporkan dengan MPJPE, NME, PCK@α, dan galat per *keypoint* (Subbab 2.14), dan galat itu dirinci untuk pasangan huruf paling mirip serta lintasan J dan Z. Pembanding ablasi dilaporkan berdampingan: kepala klasifikasi saja, multitugas penuh, dan variasi bobot λ~reg~; manfaat supervisi *keypoint* dinyatakan dari selisihnya, termasuk jika manfaatnya nihil.

### 3.8.3 Uji Operasional

Tiga hal diukur pada uji operasional: deteksi palsu per jam tanpa peragaan, latensi ujung ke ujung tiap arah, dan konsumsi arus modul. Prosedurnya sebagai berikut.

1. Menjalankan purwarupa di ruang yang sudah terkalibrasi.
2. Merekam kondisi tanpa peragaan, termasuk ketika orang lewat dan kipas menyala, lalu mencatat isyarat yang terdeteksi.
3. Meminta pengisyarat memperagakan isyarat target, lalu mencatat waktu selesainya isyarat dan terdengarnya suara; pada arah kedua, mengucapkan frasa uji dan mencatat waktu representasi tampil.
4. Mengukur arus modul pada beberapa kondisi kerja, kemudian menghitung estimasi ketahanan baterai.
5. Menghitung biaya purwarupa dari harga komponen serta perkiraan biaya layanan ucapan per jam pemakaian.
6. Menganalisis deteksi palsu, latensi pada kedua arah, dan ketahanan baterai terhadap indikator layak yang ditetapkan kemudian (Tabel 3.7).

Tiga perhitungan penunjang dirumuskan lebih dulu agar hasilnya bisa diperiksa ulang. Latensi ujung ke ujung ialah penjumlahan waktu tiap tahap:

```rumus
t~total~ = t~segmentasi~ + t~inferensi~ + t~pemetaan~ + t~keluaran~ (3.3)
```

dengan t~inferensi~ mencakup seluruh model gabungan (Subbab 3.7) dan t~keluaran~ mencakup sintesis ucapan pada arah pertama serta tampilnya representasi isyarat pada arah kedua; anggaran per tahap dan ambang totalnya diuji pada G3 (Tabel 3.5). Ketahanan baterai diestimasi dari kapasitas baterai C~baterai~ dan arus rata-rata terukur I~rata~:

```rumus
T~baterai~ ≈ 0,8 · C~baterai~ / I~rata~ (3.4)
```

Faktor 0,8 menampung efisiensi konverter dan penuaan baterai. Sebagai ilustrasi angka, baterai 2.500 mAh pada arus rata-rata 250 mA bertahan kira-kira delapan jam; angka arus sebenarnya diukur pada langkah keempat, bukan diasumsikan. Biaya total purwarupa menjumlahkan harga seluruh komponen b~j~ dan biaya layanan ucapan per jam:

```rumus
B~total~ = Σ~j~ b~j~ + b~layanan~ · t~pakai~ (3.5)
```

dengan t~pakai~ jam pemakaian layanan selama uji.

### 3.8.4 Uji Jalur Ucapan dan Cakupan Kamus

Komponen bahasa pada kedua arah dinilai lewat uji jalur ucapan, yang membandingkan jalur *on-device*, awan, dan server lokal disertai cakupan kamus arah kedua. Prosedurnya sebagai berikut.

1. Menyiapkan daftar frasa uji pendek berbahasa Indonesia [PERLU DATA: daftar frasa uji dan jumlah penutur] yang memuat kata di dalam dan di luar kamus.
2. Merekam teks keluaran layanan ASR awan, lalu menghitung akurasi katanya terhadap teks acuan.
3. Mengukur waktu pengenalan, pemetaan, inferensi TTS *on-device*, serta total ujung ke ujung pada kedua arah.
4. Mengulang pengukuran pada kedua kandidat mesin *on-device* (Kokoro ONNX dan MMS-TTS-ind) serta jalur pembanding awan dan server lokal, lalu menimbang mutu dan latensinya.
5. Memverifikasi prasyarat suara Indonesia sambil mengukur *parsing* UDP dan memori server Rust (Subbab 2.13).
6. Mencatat proporsi kata uji yang tampil sebagai representasi isyarat, ejaan jari, dan gagal tampil, kemudian menganalisis mutu, latensi, serta ketergantungan internet sebagai bahan keputusan G3 (Tabel 3.7).

### 3.8.5 Uji Kegunaan dan Penilaian Validator

Keterpakaian purwarupa ditelaah lewat uji kegunaan bersama 3–5 pengguna kelompok sasaran pada skenario tugas terbimbing, yaitu saling menyampaikan pesan pendek melalui ejaan huruf dan kosakata tampilan. Tiap pengguna menjalani langkah berikut.

1. Menjelaskan tujuan uji, batas kosakata, kenyataan bahwa kamera tidak menyala, dan hak mundur, lalu meminta persetujuan tertulis.
2. Memberi waktu berlatih singkat bersama kamus tampilan.
3. Menjalankan tugas komunikasi dua arah sambil mencatat keberhasilan, waktu penyelesaian, dan keluaran yang menyesatkan.
4. Meminta pengguna mengisi kuesioner skala Likert [28] mengenai kegunaan, kejelasan, dan keinginan memakai ulang.
5. Merekapitulasi hasil, lalu menganalisisnya secara deskriptif tanpa klaim kausal.

Kewajaran keluaran kedua arah dinilai validator penutur tunarungu; keluaran sistem dan penilaian independennya dicatat dalam tabel silang, sedangkan kasus yang dinilai keliru dilaporkan tersendiri. Sebagai analisis sekunder, kesalahan klasifikator dikaitkan luring dengan kemiripan pose pada deret *keypoint* guru agar kesalahan konfigurasi mirip dapat dibedakan dari kesalahan sinyal lemah.

### 3.8.6 Kriteria Gerbang Keputusan

Tabel 3.5 menyajikan kriteria tiap gerbang beserta tindakan jika gagal. Kelayakan pada rumusan ketiga ditinjau per dimensi, bukan semata dari lolosnya G4, dan ambang kuantitatifnya difinalkan bersama pembimbing sebelum gerbang dinilai.

Tabel 3.5 Kriteria gerbang keputusan

| Gerbang | Nama dan waktu | Kriteria lolos (ambang usulan) | Tindakan jika gagal |
|---|---|---|---|
| G0 | Baseline CSI dan jaringan, akhir M2 | Akuisisi 56 *subcarrier* 1 m ke UDP Rust terbaca stabil; laju sekurang-kurangnya 25 bingkai per detik; paket hilang tidak melampaui 0,1%; pola bergerak terpisah dari diam; audit *checkpoint encoder* selesai | Perbaikan penempatan satu kali; gagal lagi berarti jalur CSI dihentikan dan dilaporkan |
| G1 | Model tepi terkuantisasi dan dua kepala, akhir M8 | Akurasi dalam sesi sekurang-kurangnya 50% (sekitar 13 kali acak 3,8%) dan melampaui pembanding ablasi kepala tunggal; manfaat multitugas dilaporkan dari ablasi; MPJPE dilaporkan; inferensi terkuantisasi di bawah 100 ms | Pangkas himpunan huruf pembeda terkuat, lalu nilai ulang |
| G2 | Tiga pilar pakar, akhir M10 | Penilaian tertulis pakar SIBI-aksesibilitas, RF-*wireless sensing*, dan *embedded AI* masuk semua; tanpa temuan blok kritis; skor rata-rata per pilar sekurang-kurangnya 3 dari 5 | Perbaiki temuan blok atau sempitkan klaim, lalu nilai ulang |
| G3 | Integrasi Rust dan mesin ucapan, M11 | Latensi arah 1 tidak melampaui 2 detik dan arah 2 tidak melampaui 3 detik pada jalur *on-device* (5 detik cadangan); TTS di bawah 100 ms; *parsing* UDP di bawah 0,2 ms; memori server di bawah 40 MB; suara Indonesia tersedia atau peralihan dilaporkan | Beralih ke mesin *on-device* alternatif, lalu server lokal atau awan; melampaui berarti temuan |
| G4 | Sintesis kelayakan, akhir M12 | Skor persepsi rata-rata sekurang-kurangnya 3,0 dari 5; validator menyetujui kewajaran; biaya lengkap; rekomendasi TKT/TRL 3–4 tertulis | Hasil negatif tetap dilaporkan; rekomendasi menyatakan posisi lebih rendah beserta alasan |

## 3.9 Jadwal Penelitian

Tabel 3.6 memuat jadwal empat belas minggu; tanda ■ menandai minggu pelaksanaan.

Tabel 3.6 Jadwal penelitian

| No. | Kegiatan | M1 | M2 | M3 | M4 | M5 | M6 | M7 | M8 | M9 | M10 | M11 | M12 | M13 | M14 | Gerbang |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | T0 Replikasi platform, audit *checkpoint*, uji Delta-CSI, dan koeksistensi | ■ | ■ | | | | | | | | | | | | | G0 (akhir M2) |
| 2 | T1 Kurasi alfabet SIBI dan kosakata, kalibrasi ruang, protokol, perizinan | | ■ | ■ | ■ | | | | | | | | | | | — |
| 3 | T2 Perekaman *dataset*, pelatihan dua kepala, kuantisasi, uji *deployment* | | | | ■ | ■ | ■ | ■ | ■ | | | | | | | G1 (akhir M8) |
| 4 | T3 Uji lintas sesi, partisipan, ruang, dan pengguna baru | | | | | | | | ■ | ■ | ■ | | | | | G2 (akhir M10) |
| 5 | T4 Pengemasan dua arah, Rust, TTS *on-device*, uji operasional, jalur ucapan, kamus, kegunaan, validator | | | | | | | | | | ■ | ■ | ■ | | | G3 (M11), G4 (akhir M12) |
| 6 | T5 Analisis dan penulisan | | | | | | | | | | | | ■ | ■ | ■ | — |

## 3.10 Parameter Rancangan yang Ditetapkan Kemudian

Sebagian parameter bergantung pada kesepakatan pembimbing, hasil tahap sebelumnya, atau data validasi. Parameter semacam itu dihimpun pada Tabel 3.7 dan ditetapkan lebih dulu sebelum dipakai menilai data uji maupun gerbang terkait.

Tabel 3.7 Parameter rancangan yang ditetapkan kemudian

| No. | Parameter | Waktu atau dasar penetapan | Status |
|---|---|---|---|
| 1 | Finalisasi ambang seluruh gerbang G0–G4 | Sebelum gerbang dinilai | [PERLU DATA: finalisasi ambang usulan Tabel 3.5 bersama pembimbing] |
| 2 | Ambang G1, tindakan gagal kedua, dan kriteria pemangkasan himpunan huruf | Sebelum eksperimen | [PERLU DATA: ambang, tindakan, dan kriteria pemangkasan tanpa data uji] |
| 3 | Kriteria kualitas model guru | Sebelum pelatihan murid | [PERLU DATA: ambang deteksi tangan, batas jitter, prosedur sampel] |
| 4 | Pemilihan *subcarrier*, lintasan puncak, dan segmentasi huruf statis | Sebelum dipakai | [PERLU DATA: kriteria, definisi operasional, ambang dan jendela tahan pose] |
| 5 | Pembagian data dan strategi Widar3.0 | Sebelum dipakai | [PERLU DATA: blok, proporsi latih-validasi-uji, komponen strategi, repetisi uji] |
| 6 | Bentuk masukan *encoder*, rancangan adapter masukan, dan panjang jendela T | Hasil audit T0 | [PERLU VALIDASI: bentuk masukan checkpoint dan rancangan adapter] |
| 7 | Sistem koordinat target regresi, keluaran per bingkai atau satu pose, skala acuan d~ref~, dan ambang α | Sebelum pelatihan | [PERLU VALIDASI: sistem koordinat, bentuk keluaran, dan ambang PCK] |
| 8 | Status modul temporal final (1D-CNN atau agregasi statistik) | Dari hasil ablasi | [PERLU DATA: keputusan modul temporal beserta bukti ablasi] |
| 9 | Bobot λ~cls~, λ~reg~, normalisasi skala kerugian, dan ambang keyakinan | Dari data validasi | [PERLU DATA: nilai bobot, skema normalisasi, dan ambang] |
| 10 | Peringkat LoRA r dan lapis yang disadap | Sebelum adaptasi dijalankan | [PERLU VALIDASI: kompatibilitas LoRA dengan alur ekspor dan pilihan r] |
| 11 | Perlakuan data uji | Sebelum dipakai | [PERLU DATA: segmen tersaring kamera atau segmentasi tanpa koreksi] |
| 12 | Inklusi partisipan, sesi per ruang, dan token apresiasi | Sebelum dipakai | [PERLU DATA: kriteria kompetensi, kefasihan validator, pengguna uji, token] |
| 13 | Publikasi *dataset* dan persetujuan etik | Sebelum dipakai | [PERLU DATA: izin, repositori, lisensi, lembaga persetujuan etik] |
| 14 | Rubrik tiga pilar pakar dan personalisasi jika G2 gagal | Sebelum G2 dinilai | [PERLU DATA: rubrik, ambang skor, prosedur data latih pengguna] |
| 15 | Indikator layak operasional dan durasi pengamatan deteksi palsu | Sebelum G3 dinilai | [PERLU DATA: anggaran latensi, batas deteksi palsu, baterai minimum, durasi] |
| 16 | Kanal, jarak antarmodul, zona, model layar, audio, dan kapasitas baterai | Pada T0 atau sebelum T4 | [PERLU DATA: penetapan, model layar final, kapasitas dari uji arus] |
| 17 | Mesin TTS *on-device* final, layanan ASR, dan frasa uji | Pada G3 | [PERLU DATA: keputusan mesin, layanan, dan daftar frasa dari uji banding] |
| 18 | Kuesioner, rubrik validator dan pakar, serta asumsi biaya G4 | Sebelum T4 | [PERLU DATA: butir kuesioner, rubrik, batas kesesuaian, harga dan asumsi] |

## 3.11 Risiko dan Alternatif Cadangan

Tabel 3.8 merangkum risiko utama beserta mitigasinya. Cadangan disusun bertingkat mengikuti titik kegagalan, sehingga kegagalan komponen hanya mempersempit klaim tanpa menghentikan penelitian; setiap pemakaian cadangan tercatat dalam laporan akhir.

Tabel 3.8 Risiko dan mitigasi

| No. | Risiko | Dampak | Mitigasi dan cadangan |
|---|---|---|---|
| 1 | Pola CSI isyarat tidak terpisah pada konfigurasi dua modul | G0 gagal; jalur CSI tidak layak | Perbaikan penempatan satu kali; gagal lagi berarti dihentikan dan dilaporkan |
| 2 | Bentuk masukan *checkpoint* tidak sesuai jendela CSI (delapan fitur turunan lawan 56 *subcarrier*) | *Encoder* tidak bisa dipakai langsung | Hitung fitur turunan bawaan RuView atau latih adapter masukan; hasil audit T0 dilaporkan |
| 3 | *Embedding encoder* beku tidak memisahkan kelas huruf | Kepala tidak dapat belajar | Jalur adaptasi LoRA dan pelatihan lanjutan; hasilnya dibandingkan apa adanya |
| 4 | Konflik gradien antartugas multitugas | Salah satu tugas terhambat | Penyeimbangan gradien atau pelatihan bergantian; kepala tunggal pembanding |
| 5 | Akurasi lintas partisipan, ruang, atau posisi rendah (G2 gagal) | Klaim pengguna baru tak dapat dibuat | Personalisasi per pengguna (cadangan A); dilaporkan |
| 6 | Model terkuantisasi terlalu berat atau lambat di modul | Inferensi tepi tidak tercapai | Klasifikasi dipindah ke server, modul kirim fitur (cadangan B) |
| 7 | Beban radio gabungan CSI, UDP, dan audio bermasalah | Purwarupa tidak stabil | Modul ketiga khusus antarmuka (cadangan C) |
| 8 | Layanan ucapan tidak memadai, termasuk suara Kokoro belum tersedia | Jalur ucapan terganggu | Beralih ke MMS-TTS-ind ONNX, lalu server lokal atau awan (cadangan D) |
| 9 | Aset representasi isyarat mahal | Cakupan arah kedua sempit | Batasi ke glos dan gambar plus ejaan jari |
| 10 | Ketahanan baterai di bawah target | Klaim portabilitas melemah | Ukur arus, sesuaikan target, laporkan apa adanya |
| 11 | Rekrutmen, etika, atau kuota GPU terlambat | Jadwal mundur | Dua ruang dan pengisyarat cadangan; pelatihan terkompresi; minggu transisi |
| 12 | Huruf sangat mirip tak terpisahkan CSI | Himpunan kelas menyempit | Pangkas himpunan pada G1 sesuai Tabel 3.7; laporkan pasangan gagal |
# DAFTAR PUSTAKA

[1] Kementerian Koordinator Bidang Pembangunan Manusia dan Kebudayaan, "Kemenko PMK bergerak bersama wujudkan selaras bahasa isyarat," 3 Okt. 2025. [Online]. Available: https://www.kemenkopmk.go.id/kemenko-pmk-bergerak-bersama-wujudkan-selaras-bahasa-isyarat, diakses 24 Okt. 2026.

[2] Republik Indonesia, *Undang-Undang Nomor 8 Tahun 2016 tentang Penyandang Disabilitas*. Jakarta, Indonesia, 2016.

[3] Departemen Pendidikan dan Kebudayaan, *Kamus Sistem Isyarat Bahasa Indonesia* (edisi pertama). Jakarta, Indonesia: Departemen Pendidikan dan Kebudayaan, 1994.

[4] R. A. Mursita, "Respon tunarungu terhadap penggunaan Sistem Bahasa Isyarat Indonesia (SIBI) dan Bahasa Isyarat Indonesia (BISINDO) dalam komunikasi," *INKLUSI*, vol. 2, no. 2, p. 221, 2015, doi: 10.14421/ijds.2202.

[5] S. Dwijayanti, Hermawati, S. I. Taqiyyah, H. Hikmarika, and B. Y. Suprapto, "Indonesia sign language recognition using convolutional neural network," *International Journal of Advanced Computer Science and Applications*, vol. 12, no. 10, 2021, doi: 10.14569/IJACSA.2021.0121046.

[6] Y. Ma, G. Zhou, and S. Wang, "WiFi sensing with channel state information: A survey," *ACM Computing Surveys*, vol. 52, no. 3, pp. 1–36, 2019, doi: 10.1145/3310194.

[7] Y. Ma, G. Zhou, S. Wang, H. Zhao, and W. Jung, "SignFi: Sign language recognition using WiFi," *Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies*, vol. 2, no. 1, pp. 1–21, 2018, doi: 10.1145/3191755.

[8] Espressif Systems, *ESP32-S3 Series Datasheet*, versi 2.2, 2026. [Online]. Available: https://www.espressif.com/sites/default/files/documentation/esp32-s3_datasheet_en.pdf, diakses 25 Okt. 2026.

[9] Espressif Systems, "esp-csi: Wi-Fi channel state information based sensing," repositori GitHub. [Online]. Available: https://github.com/espressif/esp-csi, diakses 25 Okt. 2026.

[10] ruvnet, "RuView," repositori GitHub. [Online]. Available: https://github.com/ruvnet/RuView, diakses 13 Nov. 2026.

[11] ruvnet, "wifi-densepose-pretrained," model card Hugging Face. [Online]. Available: https://huggingface.co/ruvnet/wifi-densepose-pretrained, diakses 13 Nov. 2026.

[12] Ultralytics, "Pose estimation" dan "Hand keypoints pose estimation dataset," Ultralytics YOLO Docs. [Online]. Available: https://docs.ultralytics.com/tasks/pose/ dan https://docs.ultralytics.com/datasets/pose/hand-keypoints/, diakses 8 Nov. 2026.

[13] D. Wu, Y. Zeng, F. Zhang, and D. Zhang, "WiFi CSI-based device-free sensing: From Fresnel zone model to CSI-ratio model," *CCF Transactions on Pervasive Computing and Interaction*, vol. 4, no. 1, pp. 88–102, 2022, doi: 10.1007/s42486-021-00077-z.

[14] Y. Zhang, Y. Zheng, K. Qian, G. Zhang, Y. Liu, C. Wu, and Z. Yang, "Widar3.0: Zero-effort cross-domain gesture recognition with Wi-Fi," *IEEE Transactions on Pattern Analysis and Machine Intelligence*, vol. 44, no. 11, pp. 8671–8685, 2022, doi: 10.1109/TPAMI.2021.3105387.

[15] ruvnet, "wifi-densepose-mmfi-pose," model card Hugging Face. [Online]. Available: https://huggingface.co/ruvnet/wifi-densepose-mmfi-pose, diakses 13 Nov. 2026.

[16] J. Yang, H. Huang, Y. Zhou, X. Chen, Y. Xu, S. Yuan, H. Zou, C. X. Lu, and L. Xie, "MM-Fi: Multi-modal non-intrusive 4D human dataset for versatile wireless sensing," in *Proc. NeurIPS Datasets and Benchmarks Track*, 2023. [Online]. Available: https://arxiv.org/abs/2305.10345, doi: 10.48550/arXiv.2305.10345.

[17] E. J. Hu, Y. Shen, P. Wallis, Z. Allen-Zhu, Y. Li, S. Wang, L. Wang, and W. Chen, "LoRA: Low-rank adaptation of large language models," in *Proc. 10th International Conference on Learning Representations (ICLR)*, 2022.

[18] C. K. Chow, "On optimum recognition error and reject tradeoff," *IEEE Transactions on Information Theory*, vol. 16, no. 1, pp. 41–46, 1970, doi: 10.1109/TIT.1970.1054406.

[19] F. Zhang, V. Bazarevsky, A. Vakunov, A. Tkachenka, G. Sung, C.-L. Chang, and M. Grundmann, "MediaPipe Hands: On-device real-time hand tracking," arXiv:2006.10214, 2020, doi: 10.48550/arXiv.2006.10214.

[20] R. Girshick, "Fast R-CNN," in *Proceedings of the IEEE International Conference on Computer Vision (ICCV)*, 2015, pp. 1440–1448.

[21] R. Caruana, "Multitask learning," *Machine Learning*, vol. 28, no. 1, pp. 41–75, 1997, doi: 10.1023/A:1007379606734.

[22] G. Hinton, O. Vinyals, and J. Dean, "Distilling the knowledge in a neural network," arXiv:1503.02531, 2015, doi: 10.48550/arXiv.1503.02531.

[23] Espressif Systems, "esp-dl: Espressif deep-learning library for ESP32-S3," repositori GitHub. [Online]. Available: https://github.com/espressif/esp-dl, diakses 25 Okt. 2026.

[24] hexgrad, "Kokoro-82M," model card Hugging Face. [Online]. Available: https://huggingface.co/hexgrad/Kokoro-82M dan https://doi.org/10.57967/hf/4329, diakses 25 Okt. 2026.

[25] Meta AI, "Massively Multilingual Speech (MMS): Indonesian text-to-speech," model card Hugging Face facebook/mms-tts-ind. [Online]. Available: https://huggingface.co/facebook/mms-tts-ind, diakses 25 Okt. 2026.

[26] A. Radford *et al.*, "Robust speech recognition via large-scale weak supervision," arXiv:2212.04356, 2022, doi: 10.48550/arXiv.2212.04356.

[27] J. C. Mankins, "Technology readiness assessments: A retrospective," *Acta Astronautica*, vol. 65, no. 9-10, pp. 1216–1223, 2009, doi: 10.1016/j.actaastro.2009.03.058.

[28] R. Likert, "A technique for the measurement of attitudes," *Archives of Psychology*, no. 140, pp. 5–55, 1932.
<!-- ===== AKHIR NASKAH (jangan hapus penanda ini) ===

## Log Perubahan — Revisi 13 November 2026, gelombang 16 (revisi additif: dua kepala tugas pada encoder CSI terpralatih)

Permintaan: memperkuat proposal dengan pengembangan head klasifikasi dan regresi pada encoder Wi-Fi CSI terpralatih untuk jalur isyarat menjadi teks, tanpa mengubah ruang lingkup sistem SenseSIBI dua arah; judul dokumen acuan pemilik memakai frasa "CLOUD PROCESSING". Kaidah humanizer-indonesia (adhiprib v1.7, register akademik) dan pedoman scientific-agent-skills (scientific-writing, citation-management, markdown-mermaid-writing) tetap dipakai. Seluruh audit sumber di bawah dilakukan dengan membuka langsung kartu model Hugging Face, model card repositori, dan ADR pada 13 November 2026; matriks klaim lengkap pada Audit-Klaim-v16.md.

Changelog per subbab:

- Sampul: judul diganti mengikuti dokumen acuan pemilik (frasa "PEMROSESAN SERVER" menjadi "CLOUD PROCESSING"); kolom jenis dokumen dan catatan penyusunan ditulis ulang.
- 1.1 Latar belakang: paragraf keenam (model) ditulis ulang; kalimat arah 1 dan arah 2 serta paragraf studi kelayakan dipertahankan.
- 1.2 dan 1.3: butir 1 dan 2 diperbarui (encoder terpralatih beku, dua kepala tugas, supervisi lintas modalitas, ablasi); butir 3 (kelayakan) tetap; cermin rumusan-tujuan tetap 3:3.
- 1.4 Batasan: ditambah butir 5 tentang checkpoint encoder (bentuk masukan diaudit, LoRA berstatus pembanding); butir lama menjadi 1-4 dan 6-10.
- 1.5.1 Manfaat teoretis: ditambah pertanyaan embedding kontrastif untuk gestur jari dan formulasi multitugas lintas modalitas.
- 1.6 Sistematika: disesuaikan dengan subbab baru.
- 2.1: ditambah satu kalimat audit kelas (C statis; J dan Z dinamis) sebagai pemastian konsistensi seluruh naskah.
- 2.2 sampai 2.3: teks v15 dipertahankan; Tabel 2.1 baris "Model WiFi-DensePose terpralatih int8" diganti "Checkpoint encoder CSI terpralatih (embedding 128 dimensi)".
- 2.4 (baru) Encoder CSI terpralatih dan pembedaan tiga model: kartu model encoder (dua lapis FC BatchNorm+GELU, 9.280 parameter, embedding 128 ternormalisasi L2, triplet+InfoNCE temperatur 0,1, positif 2 detik, negatif 30 detik, 60 epoch AdamW, EWC); penegasan 82,3% sebagai akurasi triplet-temporal held-out (pembanding 66,4% fitur mentah dan 69,6% encoder acak), bukan akurasi SIBI; temuan ketidaksesuaian bentuk masukan (delapan fitur turunan pada 1 Hz lawan 56 subcarrier pada 50 bingkai per detik) beserta dua jalur penyelesaian; pembedaan model pose MM-Fi 17 keypoint tubuh (masukan [3, 114, 10] @ 100 Hz, PCK@20 82,69%/83,59%, lintas subjek ±64%, lintas lingkungan 17,5%, lisensi CC BY-NC 4.0) dan YOLO26m-Pose guru visual; status ADR-024, ADR-146, ADR-150 dinyatakan Proposed; Tabel 2.2 pembedaan tiga model; persamaan (2.6).
- 2.5 (baru) Transfer learning: alasan encoder beku; LoRA W = W0 + BA (persamaan 2.7) sebagai opsi adaptasi bukan prasyarat; adapter ruangan node-1/node-2 ±21 KB terdokumentasi; estimasi ADR-150 dilabeli estimasi rancangan; kompatibilitas ekspor ditandai [PERLU VALIDASI].
- 2.6 (baru) Kepala klasifikasi: logits, softmax, silang-entropi 26 kelas (persamaan 2.8-2.10); bobot kelas dari data latih; penolakan dengan skor keyakinan [18].
- 2.7 (baru) Kepala regresi: skema 21 landmark MediaPipe; komponen ketiga kpt_shape [21, 3] ditegaskan sebagai visibilitas, bukan koordinat kedalaman; keluaran (T, 21, 2) karena lintasan J dan Z (persamaan 2.11); pembakuan sistem koordinat [PERLU VALIDASI]; Smooth L1 bermask per keypoint (persamaan 2.12-2.13) [20].
- 2.8 (baru) Multitugas, modul temporal, kerugian gabungan: hipotesis supervisi keypoint merapikan batas kelas; persamaan 2.14-2.15 dengan θ0 beku; normalisasi skala kerugian dan pemantauan konflik gradien; 1D-CNN dari rancangan lama dievaluasi ulang sebagai kandidat modul temporal (peringkas barisan embedding), bukan kepala tugas.
- 2.9 Guru visual YOLO26m-Pose: istilah "distilasi pengetahuan" dikoreksi menjadi supervisi lintas modalitas berpandu guru / pseudo-label [22]; angka WPC (49 kelas, 7.210 gambar, 6.231/650/329, mAP50 0,8944 dan 0,9580, akurasi 97,6%) ditegaskan sebagai hasil visual pada data visual dan dataset tanpa CSI; ekspektasi generalisasi dari temuan MM-Fi.
- 2.10: kalimat SVM diganti pembanding ablasi kepala tunggal; ESP-DL [23] tetap.
- 2.11 sampai 2.13 (dulu 2.6 sampai 2.8): teks v15 dipertahankan; ditambah satu kalimat pemisahan bahasa pelatihan (Python/PyTorch) dan bahasa runtime (Rust).
- 2.14 Evaluasi (dulu 2.9): ditambah metrik regresi MPJPE, NME, PCK@α, dan galat per keypoint (persamaan 2.21-2.22) serta definisi d_ref yang mengikuti pembakuan koordinat; persamaan presisi-recall-F1-WER dipertahankan dengan nomor baru.
- 2.15 Penelitian terdahulu (dulu 2.10): baris "Penelitian ini" diperbarui (encoder terpralatih berkepala dua, supervisi guru visual).
- 2.16 Matriks justifikasi (dulu 2.11): baris model murid diperbarui; ditambah baris 7 (dua kepala lawan satu kepala) dan baris 8 (supervisi lintas modalitas lawan distilasi soft target); SVM keluar dari matriks.
- 2.17 (baru) Kerangka pemikiran: Gambar 2.2 arsitektur model dua kepala (encoder beku, adapter masukan bila perlu, modul temporal, dua kepala, jalur guru visual, deployment); dataset berpasangan D_pas diperluas dengan skor kualitas anotasi q_i (persamaan 2.24).
- 3.1 dan 3.2: kalimat model diperbarui (supervisi lintas modalitas; dua kepala); T0 menambah audit checkpoint; T2 menambah pelatihan dua kepala; Gambar 3.1 digambar ulang (label T0, T2, G1).
- 3.3 dan 3.4: Tabel 3.1 perangkat keras dipertahankan sepuluh baris; Tabel 3.2 diperbarui (checkpoint encoder masuk baris 2; scikit-learn keluar; Kaggle hanya pelatihan lanjutan guru dan pembanding adaptasi; sebelas baris).
- 3.5: Gambar 3.3 node RX diganti labelnya (encoder terpralatih berkepala dua terkuantisasi); teks topologi, kalibrasi, enclosure, Tabel 3.3 pinout, dan Gambar 3.4 dipertahankan.
- 3.6: langkah 4 menambah verifikasi sinkronisasi lewat uji kejadian [PERLU DATA: toleransi sinkronisasi]; langkah 6 menambah skor kualitas anotasi; langkah 7 menegaskan status pseudo-label.
- 3.7 (ditulis ulang): audit bentuk masukan dan adapter; encoder per bingkai plus modul temporal; dataset murid tiga deret selaras waktu; pelatihan Python/PyTorch di komputer (laptop atau Kaggle) dengan seed tetap dan early stopping; rangkaian ablasi (kepala klasifikasi saja, multitugas, variasi bobot λ); LoRA dan pelatihan lanjutan sebagai pembanding opsional; Tabel 3.4 skema pembagian dipertahankan enam baris; ekspor satu graph lalu kuantisasi affine (persamaan 3.2) dengan verifikasi operator runtime [PERLU VALIDASI]; Gambar 3.5 digambar ulang.
- 3.8: 3.8.2 menjadi "Uji Klasifikasi, Regresi, dan Ablasi" (menambah MPJPE, NME, PCK, galat per keypoint, pasangan mirip dan lintasan J/Z, ablasi berdampingan); 3.8.3 persamaan dinomori ulang (3.3 latensi, 3.4 baterai, 3.5 biaya); gerbang G1 pada Tabel 3.5 menambah pembanding ablasi dan laporan MPJPE; subbab lain dipertahankan.
- 3.9: jadwal M1-M14 dipertahankan; label baris 1 dan 3 diperbarui.
- 3.10: Tabel 3.7 dari 14 menjadi 18 baris (bentuk masukan dan adapter; koordinat, bentuk keluaran, dan ambang PCK; status modul temporal; peringkat LoRA; bobot λ dan skala kerugian).
- 3.11: Tabel 3.8 dari 9 menjadi 12 baris (risiko ketidaksesuaian bentuk masukan; embedding beku tidak memisahkan; konflik gradien).
- Daftar pustaka: 22 menjadi 28 entri. Masuk tujuh rujukan primer baru yang diverifikasi dengan membuka sumbernya pada 13 November 2026: kartu model encoder [11], kartu model pose MM-Fi [15], dataset MM-Fi [16], LoRA [17], MediaPipe Hands [19], Fast R-CNN untuk Smooth L1 [20], dan multitask learning [21]. Keluar satu rujukan bersama pembanding lamanya: SVM (Cortes dan Vapnik), karena pembanding klasifikasi kini berupa ablasi kepala tunggal pada model yang sama. Sitasi dinomori ulang menurut kemunculan pertama dan diverifikasi monoton 1-28; tanggal akses RuView dan kedua kartu model diperbarui ke 13 Nov 2026.
- Persamaan: 18 menjadi 29 bernomor (2.1-2.24 dan 3.1-3.5); seluruh persamaan lama dipertahankan isinya dengan nomor baru.
- Gambar: 6 menjadi 7. Gambar 2.1 zona Fresnel dan Gambar 3.2 foto perangkat serta Gambar 3.4 skema node dipertahankan dari gelombang 15; Gambar 2.2 arsitektur model dua kepala baru; Gambar 3.1, 3.3, dan 3.5 digambar ulang dengan label model baru, lengkap accTitle/accDescr dan subgraf berlabel.
- Penanda: [PERLU DATA] 23 sampul-isi, [PERLU VALIDASI] 9 (bentuk masukan dan adapter; koordinat dan ambang PCK; kompatibilitas LoRA; dukungan operator runtime; sistem koordinat; bentuk keluaran regresi), [PERLU ILUSTRASI] 1; penanda VALIDASI baru ditambahkan pada regex parser DOCX agar ikut tersorot.
- Yang tidak berubah: seluruh komponen sistem dua arah (TTS on-device Kokoro dengan prasyarat G3, ASR awan dengan cadangan faster-whisper, kamus representasi SIBI dengan fallback ejaan jari, server Rust, topologi satu kanal, enclosure dan pinout), gerbang G0-G4, jadwal M1-M14, uji kegunaan dan validator, analisis biaya, konteks Jawa Timur tanpa mitra lembaga, register mahasiswa D4/S1, dan seluruh angka pra-penelitian yang dipertahankan tetap bersumber sama.
- Pemetaan nomor ke kunci: [1]kemenkopmk, [2]uu-disabilitas, [3]kamus-cetak, [4]mursita, [5]dwijayanti, [6]ma-csur, [7]signfi, [8]esp32s3, [9]esp-csi, [10]ruview, [11]encoder-card, [12]ultralytics, [13]csi-ratio, [14]widar3, [15]mmfi-card, [16]mmfi-paper, [17]lora, [18]chow, [19]mediapipe, [20]girshick, [21]caruana, [22]hinton, [23]esp-dl, [24]kokoro-card, [25]mms-card, [26]whisper, [27]trl, [28]likert

## Log Perubahan — Revisi 11 November 2026, gelombang 12 (parafrase anti-ai-writer)

Permintaan: memparafrasekan ketiga dokumen (md, docx, pdf) memakai skill anti-ai-writer (mchardyan/anti-ai-writer v2) di atas naskah v11, tanpa mengubah isi. Pekerjaan tetap menjaga kaidah naskah-id (EYD V), register mahasiswa D4/S1, dan seluruh keputusan gelombang 11 (konteks Jawa Timur, prioritas sumber Indonesia, DP 46 entri, istilah asing tidak dipaksakan diterjemahkan):

- Kosakata dan frasa terlarang daftar hitam anti-ai-writer dibersihkan dari prosa: menegaskan (2), mencakup (4), menampilkan (8) diganti padanan konkret yang bervariasi (memunculkan, muncul, memperlihatkan, memuat, meliputi, menunjukkan).
- Ritme kalimat dirombak: 10 deretan tiga kalimat berpanjang seragam pada v11 (toleransi dua kata) dipecah menjadi nol melalui penggabungan, pemenggalan, dan pemanjangan kalimat terpilih; panjang kalimat kini menyebar dari 3 sampai 53 kata (13% kalimat pendek 10 kata ke bawah, 23% kalimat panjang 28 kata ke atas).
- Pola khas AI lain yang dihapus: enumerasi retoris "Pertama, ... Kedua, ..." pada latar belakang (diganti prosa mengalir), pembuka klise, dan ketergantungan pada transisi; beberapa paragraf kini ditutup tiba-tiba dan satu pertanyaan retoris dipertahankan sebagai penutup latar belakang.
- Yang tidak berubah: 46 kunci sitasi beserta urutan kemunculan dan penomoran, seluruh angka pra-penelitian (token angka pada prosa identik dengan v11), 25 penanda [PERLU DATA]/[PERLU ILUSTRASI], 12 tabel, 3 gambar beserta blok mermaid-nya, 39 heading, struktur gerbang G0-G4, jadwal M1-M14, dan keenam prosedur.
- Rumusan masalah dan tujuan diparafrase tercermin tetap 3:3; batasan tetap sembilan butir.

## Log Perubahan — Revisi 12 November 2026, gelombang 13 (humanizer-indonesia + tanpa mitra)

Permintaan: menyunting naskah v12 memakai skill humanizer-indonesia (adhiprib v1.7, register akademik) sekaligus menghapus seluruh klaim kemitraan karena penelitian dijalankan tanpa mitra lembaga. Pengukuran memakai scripts/metrik.py bawaan skill (preset akademik); kalibrasi suara penulis tidak dilakukan karena tidak ada contoh tulisan pemilik, sehingga dipakai suara netral register akademik.

- Klaim kemitraan dihapus dari lima titik (1.1, batasan butir 7, manfaat praktis, 3.3, 3.6): 3.3 kini menyatakan partisipan direkrut langsung oleh peneliti dan pengujian berlangsung di dua ruang berbeda tanpa mengikat lembaga; placeholder nama SLB mitra dihapus dari naskah.
- Sembilan metrik berambang kini lulus semua (sebelumnya tiga PERIKSA): rerata panjang kalimat 20,5 menjadi 19,1 kata; kalimat 28 kata ke atas 20,6% menjadi 13,9%; em dash/en dash di prosa 8 menjadi 0.
- Pola khas keluaran model yang dibersihkan: konstruksi verba ringan diganti verba kerja; penyangkalan antisipatif dinyatakan positif; 18 kemunculan konjungsi "bila" menjadi "jika" (kaidah register akademik skill); rentang alfanumerik di prosa menjadi bentuk "sampai".
- Ritme dirombak tanpa mengubah isi: 24 kalimat panjang dipecah; kalimat pendek lepas diberi partikel atau penghubung sesuai temuan skill bahwa kalimat pendek berpartikel terbaca manusiawi.
- Yang dikecualikan dari suntingan ritme menurut katalog skill: butir prosedur dan daftar batasan yang memang paralel, daftar teknis yang seluruh butirnya membawa isi, pasif bagian metode, dan metafora baku literatur teknik.
- Yang tidak berubah: 46 kunci sitasi beserta urutan kemunculan dan penomoran, seluruh angka pra-penelitian, 12 tabel, 3 gambar beserta blok mermaid, struktur heading, struktur gerbang G0-G4, jadwal M1-M14, keenam prosedur, dan konteks Jawa Timur.

## Log Perubahan — Revisi 12 November 2026, gelombang 14 (daftar pustaka 22 entri, sekitar 30 halaman, diagram direvisi)

Permintaan: memangkas daftar pustaka menjadi sekitar 20-an entri, memadatkan keseluruhan proposal menjadi sekitar 30 halaman, dan merevisi diagram dengan pedoman scientific-agent-skills di atas kaidah humanizer-indonesia.

- Daftar pustaka dipangkas dari 46 menjadi 22 entri dan sitasi dinomori ulang 1 sampai 22 menurut urutan kemunculan.
- Klaim yang kehilangan rujukan diperlunak, bukan dibiarkan tanpa sumber.
- Naskah dipadatkan menjadi sekitar 30 halaman.
- Tiga diagram direvisi mengikuti pedoman scientific-agent-skills: anotasi aksesibilitas accTitle/accDescr ditambahkan, subgraf tanpa judul diberi judul bermakna, setiap label simpul ditelusur ulang ke teks.
- Yang tidak berubah: struktur BAB I sampai III, tabel, gambar beserta semantik alurnya, jadwal, prosedur pengujian, batasan, rumusan dan tujuan, serta penanda [PERLU DATA]/[PERLU ILUSTRASI].

## Log Perubahan — Revisi 12 November 2026, gelombang 15 (rumusan teknologi, persamaan bernomor, ilustrasi tiga dimensi)

Permintaan: rumusan masalah mencantumkan teknologi inti (WiFi-DensePose, YOLO26m-Pose, dan lain-lain), menambah model perhitungan berupa rumus matematika, serta menambah gambar tiga dimensi dan gambar alat-bahan; kaidah humanizer-indonesia dan pedoman scientific-agent-skills tetap dipakai.

- Rumusan masalah dan tujuan kini mencantumkan teknologi intinya dengan cermin 3:3.
- Delapan belas persamaan bernomor ditambahkan beserta definisi lambang dan contoh perhitungan.
- Tiga ilustrasi baru ditambahkan (zona Fresnel tiga dimensi, foto perangkat, skema node penerima) sehingga gambar menjadi enam.
- Pipeline DOCX ditambah dukungan blok rumus serta token subskrip dan superskrip; daftar pustaka tetap 22 entri.
- Yang tidak berubah: struktur BAB I-III, tabel, gerbang, jadwal, prosedur, batasan, konteks Jawa Timur tanpa mitra, dan seluruh angka pra-penelitian.
