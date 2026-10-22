**PANDUAN PENULISAN PROPOSAL PENGAJUAN JUDUL**

DPJ-4 — Pengenalan Gestur Bahasa Isyarat SIBI Berbasis Wi-Fi Channel State Information pada ESP32 untuk Prasarana Edukasi (Lingkup SIBI, tanpa BISINDO)

*Disusun dari korpus Drive D4 TRSE Universitas Negeri Malang (69 dokumen), skill proposal-writing hasil GEPA, skill naskah-id, dan 22 referensi terverifikasi Crossref*

# **1. TENTANG PANDUAN INI**

## **1.1 Tujuan dan Cara Memakai Panduan**

Panduan ini menyatukan seluruh aturan penulisan yang dipelajari dari folder Drive berisi 69 dokumen korpus D4 Teknologi Rekayasa Sistem Elektronika (TRSE) Universitas Negeri Malang (proposal tugas akhir, naskah, seminar hasil, dan dokumen paten), rubrik evaluasi hasil optimasi GEPA, aturan bahasa dari skill naskah-id, serta 22 referensi yang telah diverifikasi melalui Crossref, lalu menerapkannya secara khusus untuk satu kebutuhan: menulis ulang DPJ-4 ke lingkup SIBI saja tanpa BISINDO. Setiap bagian memuat aturan yang berlaku, templat kalimat siap tempel yang diambil literal dari korpus, dan contoh penerapannya pada konteks bahasa isyarat SIBI. Dengan demikian, revisi dapat dikerjakan secara mandiri tanpa menebak-nebak gaya yang diharapkan pembimbing.

Cara memakai panduan ini terdiri atas tiga langkah. Pertama, baca Bagian 2 untuk memahami makna dan implikasi keputusan lingkup SIBI-only, termasuk argumen yang dapat dipertahankan di hadapan pembimbing dan jebakan yang harus dihindari. Kedua, kerjakan revisi per bagian dokumen dengan mengikuti peta revisi pada Bagian 6 sambil menempelkan templat bahasa dari Bagian 3 dan menjaga disiplin klaim dari Bagian 5. Ketiga, akhiri dengan checklist pada Bagian 8 dan jalankan alat pemeriksaan yang tersedia agar dokumen lolos semua gerbang mutu sebelum dibawa ke pembimbing.

Seluruh bahan pendukung sudah tersedia dan tidak perlu dibuat ulang. Repositori skripsi memuat empat file markdown DPJ (folder 08-markdown-dpj) dan DOCX yang sinkron (folder 03-dpj), 22 referensi terverifikasi DOI beserta gap-analisis (folder 06-referensi-isyarat), pemetaan fitur RuView untuk kasus isyarat, generator DOCX, evaluator rubrik D1-D6, dan pemeriksa bahasa periksa.py. Panduan ini merangkai semuanya menjadi satu alur kerja tunggal sehingga yang tersisa hanyalah pekerjaan penyuntingan yang terarah.

## **1.2 Keputusan Lingkup: SIBI tanpa BISINDO**

Keputusan lingkup baru mengunci target bahasa penelitian pada satu sistem, yaitu Sistem Isyarat Bahasa Indonesia (SIBI); BISINDO keluar dari objek penelitian dan hanya boleh muncul sebagai konteks literatur serta arah pengembangan lanjutan. Keputusan ini mengubah inti narasi DPJ-4 versi lama, yang justru berdiri di atas ketegangan dua sistem: sekolah formal cenderung memakai SIBI sedangkan pergaulan siswa berlangsung dalam BISINDO sehingga alat bantu idealnya mengenali keduanya. Kalimat-kalimat dengan pola seperti itu harus hilang dari dokumen baru karena mereka memotivasi cakupan dua sistem, bukan satu.

Lingkup SIBI-only dapat dipertahankan dengan tiga argumen yang kuat di hadapan pembimbing. Pertama, SIBI bersifat formal dan terstandar sehingga selaras dengan target konteks prasarana edukasi formal; definisi subset gestur dapat dirujuk secara konsisten pada satu rujukan sistem yang sama, sesuatu yang tidak dimiliki variasi komunitas. Kedua, lingkup satu sistem menekan beban dataset dan pelabelan agar realistis untuk satu semester, karena perekaman 5 sampai 12 gestur dengan 30 repetisi per gestur per sesi sudah merupakan beban yang berat. Ketiga, kebaruan kombinatif tetap utuh: pencarian literatur saat penyusunan DPJ-4 belum menemukan satu pun publikasi pengenalan isyarat berbasis Wi-Fi CSI untuk bahasa isyarat Indonesia apa pun, termasuk SIBI. Klaim pertama untuk SIBI karena itu tetap sah secara literatur.

Hampir seluruh kerangka penelitian tidak berubah oleh keputusan ini. Struktur BAB I sampai BAB III plus Daftar Pustaka, platform ESP32 dua node dengan firmware RuView, paradigma klasifikasi gestur langsung dari pola Channel State Information (CSI), gerbang go/no-go uji fisik Delta-CSI pada minggu ketiga, tabel jadwal-biaya-risiko, serta 19 referensi terverifikasi semuanya dipertahankan. Yang berubah hanyalah bahasa target dan seluruh kalimat yang memotivasi cakupan dua sistem, mulai dari judul, rumusan masalah, tujuan, batasan, hingga satu subbab kajian pustaka.

Jebakan terbesar revisi ini adalah menyisakan kalimat dua sistem di dokumen satu sistem. Contoh frasa yang wajib dihapus atau ditulis ulang adalah bermakna sama pada kedua sistem, sebaiknya menguji gestur yang berakar pada kedua sistem, dan idealnya mengenali keduanya, bukan salah satunya saja. Pembimbing lazim menguji konsistensi lingkup, dan satu frasa saja yang tersisa dapat membatalkan kredibilitas keputusan pengetatan. Bagian 6 memuat daftar lengkap titik-titik yang harus disentuh agar tidak ada yang lolos.

# **2. STRUKTUR WAJIB PROPOSAL (BAB I-III)**

## **2.1 Ruang Lingkup Dokumen**

Proposal berbeda dari skripsi: dokumen pengajuan judul hanya mencakup BAB I PENDAHULUAN, BAB II KAJIAN PUSTAKA, BAB III METODE PENELITIAN, dan DAFTAR PUSTAKA. Korpus TRSE memang menggunakan struktur lima bab untuk naskah selesai, tetapi tahap pengajuan judul berhenti pada metode penelitian; konten rencana (jadwal, biaya, risiko) dikonsolidasikan menjadi subbab di BAB III, bukan bab terpisah. Dokumen tidak memakai halaman sampul, lembar pengesahan, kata pengantar, abstrak, maupun daftar isi, sesuai keputusan pemilik yang konsisten diterapkan pada keempat DPJ sebelumnya.

Judul dokumen diletakkan di paling atas, ditulis KAPITAL SEMUA dan terpusat, mengikuti pola korpus RANCANG BANGUN atau IMPLEMENTASI atau PERANCANGAN atau SISTEM diikuti BERBASIS, PADA atau UNTUK, lalu STUDI KELAYAKAN. Penomoran halaman Arab mulai dari 1 pada footer dengan format - N -, dan tidak ada page break di tengah isi. Penamaan bab dibuat konsisten sepanjang dokumen: pilih KAJIAN PUSTAKA (bukan TINJAUAN PUSTAKA) dan METODE PENELITIAN (bukan METODOLOGI PENELITIAN), mengikuti pilihan yang sudah dipakai DPJ-4 lama.

## **2.2 Kerangka Lengkap DPJ-4 SIBI-only**

Tabel 2.1 merangkum kerangka lengkap proposal yang menjadi target revisi, beserta isi wajib setiap subbab. Kerangka ini identik dengan DPJ-4 versi lama kecuali pada titik-titik yang disebut di kolom isi wajib sebagai khusus SIBI. Gunakan tabel ini sebagai peta saat menyusun ulang dokumen agar tidak ada subbab wajib yang tertinggal.

Tabel 2.1 Kerangka wajib proposal DPJ-4 SIBI-only

| **Bab**                   | **Subbab**                                  | **Isi wajib**                                                                                                                                              |
|---------------------------|---------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BAB I PENDAHULUAN         | 1.1 Latar Belakang                          | Corong 4 lapis versi SIBI (Bagian 3.1) + Tabel 1.1 usulan judul utama dan dua alternatif                                                                   |
|                           | 1.2 Rumusan Masalah                         | Pembuka korpus + 3 pertanyaan berpola Bagaimana (templat di 6.4)                                                                                           |
|                           | 1.3 Tujuan Penelitian                       | Pembuka korpus + 3 frasa kerja yang mirror rumusan (templat di 6.4)                                                                                        |
|                           | 1.4 Batasan Masalah                         | 7 item bernomor; item terakhir Penelitian ini tidak membahas; ditutup pernyataan disiplin klaim (Bagian 5.3)                                               |
|                           | 1.5 Manfaat Penelitian                      | Paragraf pengantar + 1.5.1 Manfaat Teoretis + 1.5.2 Manfaat Praktis (Bagi Peneliti, Bagi Sekolah dan Guru, Bagi Pengguna, Bagi Praktisi)                   |
| BAB II KAJIAN PUSTAKA     | 2.1 Wi-Fi Channel State Information         | Definisi CSI, fisika modulasi Doppler gerak lengan, sitasi survei Ma dkk. dan Chen dkk.                                                                    |
|                           | 2.2 Mikrokontroler ESP32                    | ESP32-CSI-Tool (Hernandez dan Bulut), dua node mengapit zona penandatangan, biaya rendah untuk replikasi sekolah                                           |
|                           | 2.3 Platform RuView                         | Fitur terukur + Tabel 2.1 pemetaan fitur + dua batas jujur (pose stub PCK@20 sekitar 3 persen; person counting lemah)                                      |
|                           | 2.4 Pengenalan Isyarat Berbasis Wi-Fi CSI   | Rantai bukti: WiSign, SignFi, DF-WiSLR, LSTM, Widar3.0, lalu granularitas halus (Wi-SL, HandFi, Cai, WiASL)                                                |
|                           | 2.5 Sistem Isyarat Bahasa Indonesia (SIBI)  | Khusus SIBI: definisi dan sifat formal-terstandar + lanskap riset isyarat Indonesia berbasis visi sebagai bukti celah (Bagian 6.5)                         |
|                           | 2.6 Penelitian Terdahulu                    | Prosa gap + daftar bernomor mengisi celah + Tabel 2.2 komparasi (baris terakhir Penelitian Ini dengan kolom SIBI)                                          |
| BAB III METODE PENELITIAN | 3.1 Tahapan Penelitian                      | Narasi tahapan korpus + paragraf studi kelayakan bergerbang (artefak tetap per tahap)                                                                      |
|                           | 3.2 Studi Literatur                         | Tiga kelompok sumber, rentang 2017-2025, verifikasi Crossref untuk semua referensi                                                                         |
|                           | 3.3 Perancangan Arsitektur Sistem           | Tiga lapisan: sensing dua node ESP32, pengolahan (kalibrasi, segmentasi, fitur Doppler 1-60 Hz), penyajian (dashboard, alert MQTT/Home Assistant)          |
|                           | 3.4 Perancangan Perangkat Keras             | Dua unit ESP32 DevKit + satu cadangan, dudukan setinggi dada, laptop milik pribadi, kamera hanya untuk pelabelan                                           |
|                           | 3.5 Perancangan Perangkat Lunak dan Dataset | Protokol perekaman dataset SIBI (khusus SIBI): kalibrasi ruang, N repetisi per gestur, metadata, fitur amplitudo-fase-Doppler, klasifikator SVM dan 1D-CNN |
|                           | 3.6 Lokasi, Partisipan, dan Etika           | Mitra 【Nama Sekolah/Lokasi】, subjek utama guru/pembina SIBI, izin berjenjang, mode privasi RuView                                                        |
|                           | 3.7 Rencana Pengujian                       | Tiga kelompok: uji fisik Delta-CSI (gerbang), uji klasifikasi, uji operasional (alarm palsu, latensi)                                                      |
|                           | 3.8 Evaluasi dan Kriteria Keberhasilan      | Empat kelompok metrik + kriteria gerbang go/no-go minggu ketiga (lolos, kalibrasi ulang satu kali, atau beralih judul cadangan)                            |
|                           | 3.9 Rencana Kegiatan dan Jadwal Penelitian  | Tabel 3.1 jadwal satu semester; gerbang go/no-go minggu ketiga ditandai eksplisit                                                                          |
|                           | 3.10 Rencana Biaya Penelitian               | Tabel 3.2 komponen biaya dalam Rupiah (tidak berubah oleh pengetatan lingkup)                                                                              |
|                           | 3.11 Analisis Risiko dan Rencana Cadangan   | Tabel 3.3 risiko, dampak, dan fallback per risiko                                                                                                          |
| DAFTAR PUSTAKA            | \-                                          | APA edisi 7, hanging indent, URL https://doi.org pada setiap entri, urut nomor sitasi                                                                      |

## **2.3 Tabel-Tabel Wajib dan Aturan Penulisannya**

Ada enam tabel yang wajib ada pada proposal ini: Tabel 1.1 usulan judul penelitian, Tabel 2.1 pemetaan fitur RuView, Tabel 2.2 perbandingan penelitian terdahulu, Tabel 3.1 jadwal penelitian satu semester, Tabel 3.2 rencana biaya, dan Tabel 3.3 risiko beserta rencana cadangan. Seluruh tabel memakai gaya three-line (garis atas, garis bawah header, garis bawah tabel) tanpa garis vertikal, dengan judul tabel di atas tabel berpola Tabel nomor.bab.urut dilanjutkan judul singkat.

Tabel komparasi penelitian terdahulu memakai tanda centang dan tanda minus untuk menyatakan ada-tidaknya fitur, dengan baris terakhir selalu bernama Penelitian Ini. Setiap tabel didahului kalimat pengantar yang merujuk nomor tabel, misalnya Tabel 2.2 membandingkan penelitian terdahulu dengan penelitian ini, dan ditutup analisis singkat setelah tabel. Tabel tidak boleh menggantung tanpa pembahasan karena rubrik D1 memeriksa keterkaitan narasi dan tabel.

# **3. POLA BAHASA KORPUS (TEMPLAT LITERAL)**

## **3.1 Corong Latar Belakang Empat Lapis, Versi SIBI**

Latar belakang korpus selalu berbentuk corong empat lapis yang menyempit dari konteks umum ke keputusan penelitian. Lapis pertama adalah konteks umum, satu paragraf yang membuka kondisi lapangan. Lapis kedua memperjelas masalah spesifik pada praktik yang ada beserta kelemahannya. Lapis ketiga memperkenalkan satu paragraf per teknologi penyuluhan dengan sitasi pada setiap paragraf. Lapis keempat menutup dengan keputusan penelitian. Untuk DPJ-4 SIBI-only, lapis satu sampai tiga dipertahankan dari dokumen lama karena isinya tidak menyentuh pertanyaan bahasa target.

Lapis 1 dan 2 boleh disalin dari DPJ-4 lama tanpa perubahan. Lapis 1 membuka cara teknologi memengaruhi layanan pendidikan bagi kelompok tunarungu; lapis 2 menguraikan tiga hambatan pendekatan kamera di lingkungan pendidikan, yaitu beban privasi dan kesiapan institusi, ketergantungan pada pencahayaan dan sudut pandang, serta biaya solusi komersial yang tidak realistis untuk sekolah. Lapis 3 memperkenalkan CSI sebagai informasi fase dan amplitudo subcarrier yang berubah saat gelombang terganggu gerakan tubuh, lalu ESP32 dengan basis ESP32-CSI-Tool, lalu bukti paradigma SignFi dan preseden Filipino Sign Language, lalu platform RuView sebagai fondasi rekayasa. Semua sitasi pada lapis ini tetap dipakai.

Lapis 4 harus ditulis ulang karena versi lama berisi argumen dua sistem. Templat penggantinya ada di Bagian 6.3; intinya memperkenalkan SIBI sebagai sistem formal yang selaras dengan target prasarana edukasi formal, memberi dua keuntungan metodologis penargetan satu sistem, memposisikan BISINDO sebagai pengembangan lanjutan, lalu menutup dengan kalimat korpus Berdasarkan uraian tersebut, penelitian ini dilakukan untuk menguji kelayakan pengenalan gestur terisolasi bahasa isyarat SIBI dari pola Wi-Fi CSI pada ESP32 sebagai langkah awal translasi tanpa kamera di prasarana edukasi. Perhatikan bahwa frasa pembuka penutup ini wajib utuh karena merupakan penanda gaya korpus yang diperiksa evaluator.

## **3.2 Kalimat Pembuka Subbab BAB I**

Empat subbab BAB I punya kalimat pembuka baku yang diambil literal dari korpus dan sudah diterapkan pada keempat DPJ. Tempelkan pola berikut apa adanya, cukup mengganti isi pada bagian dalam tanda kutip. Konsistensi pembuka ini dinilai pada rubrik D2 sehingga mengubah polanya berisiko menurunkan skor tanpa manfaat apa pun.

> Pembuka 1.2 Rumusan Masalah: Berdasarkan latar belakang permasalahan yang telah diuraikan serta untuk menjawab permasalahan yang menjadi fokus dalam penelitian ini, maka dapat dirumuskan beberapa rumusan masalah yang akan dikaji lebih lanjut. Rumusan masalah pada penelitian ini adalah sebagai berikut. Item bernomor berupa pertanyaan Bagaimana, tiga butir.

> Pembuka 1.3 Tujuan Penelitian: Penelitian ini bertujuan menguji kelayakan pengenalan gestur terisolasi bahasa isyarat SIBI dari pola Wi-Fi CSI pada ESP32 untuk prasarana edukasi. Adapun tujuan dari penelitian ini adalah sebagai berikut. Item bernomor berupa frasa kerja: Merancang, Mengimplementasikan, Menguji, mirror satu-satu dengan rumusan masalah.

> Pembuka 1.4 Batasan Masalah: Agar penelitian ini memiliki ruang lingkup yang jelas dan terarah sesuai dengan tujuan yang telah ditetapkan, maka ditentukan batasan masalah guna membatasi pembahasan terhadap aspek-aspek yang relevan dengan topik penelitian. Adapun batasan masalah pada penelitian ini adalah sebagai berikut. Item terakhir selalu berpola Penelitian ini tidak membahas.

> Pembuka 1.5 Manfaat Penelitian: paragraf pengantar singkat, lalu subbab 1.5.1 Manfaat Teoretis yang menempatkan penelitian sebagai referensi pengembangan bidang, dan 1.5.2 Manfaat Praktis dengan sub-item Bagi Peneliti, Bagi Sekolah dan Guru, Bagi Pengguna, serta Bagi Praktisi Teknologi.

## **3.3 Narasi Tahapan Metodologi**

Pembuka BAB III pada korpus selalu berupa narasi tahapan yang tersusun sistematis. Pola ini sudah terbukti lolos pembimbing pada keempat DPJ dan dipertahankan untuk versi SIBI-only dengan satu penggantian kata: pemetaan subset gestur dilakukan bersama guru atau pembina yang menguasai SIBI.

> Penelitian dalam proposal ini dilaksanakan melalui beberapa tahapan yang tersusun secara sistematis sehingga membentuk suatu alur penelitian yang terstruktur. Tahap pertama adalah studi literatur, yaitu pemetaan sistematis pengenalan isyarat CSI dan bahasa isyarat Indonesia beserta penetapan subset gestur bersama guru atau pembina yang menguasai SIBI. Tahap kedua adalah perancangan sistem, mencakup penyiapan dua node ESP32 dengan firmware RuView, skenario penempatan node di ruang edukasi, dan protokol perekaman dataset. Tahap ketiga adalah implementasi, yaitu perekaman dataset gestur berlabel, ekstraksi fitur, dan pelatihan klasifikator. Tahap terakhir adalah pengujian dan evaluasi. Apabila dalam proses pengujian ditemukan kendala, maka dilakukan evaluasi dan perbaikan secara berulang hingga sistem dapat dievaluasi secara adil.

## **3.4 Sitasi dan Daftar Pustaka**

Sitasi dalam teks memakai pola korpus: Nama dkk. (Tahun) menjelaskan bahwa, Nama dkk. (Tahun) menunjukkan bahwa, atau Nama dan Nama (Tahun) membangun, diakhiri nomor sitasi dalam kurung siku yang berurutan sesuai kemunculan. Kata kerja pelaporan korpus yang aman adalah menjelaskan, menunjukkan, memperlihatkan, dan menyoroti. Hindari kata kerja berorientasi penulis seperti mengklaim atau membuktikan secara mutlak, karena gaya akademik korpus menempatkan literatur sebagai sumber yang dilaporkan, bukan sebagai vonis.

Daftar pustaka ditulis dalam APA edisi 7 dengan hanging indent dan URL https://doi.org pada setiap entri yang punya DOI, berurutan sesuai nomor sitasi. Pola entri jurnalnya adalah Nama, A. (Tahun). Judul artikel. Nama Jurnal, volume(nomor), halaman. https://doi.org/nomor. Pola prosiding mengganti nama jurnal dengan nama prosiding diawali kata In. Seluruh 19 entri DPJ-4 sudah berformat ini dan tinggal dipindahkan; aturan penambahannya diatur di Bagian 6.7.

Setelah tabel penelitian terdahulu, korpus selalu menaruh prosa gap dengan pola tetap: Berdasarkan tabel perbandingan di atas, terlihat bahwa, lalu ringkasan dua kutub penelitian, lalu Masih terdapat beberapa celah masalah (gap) yang belum terselesaikan secara simultan oleh peneliti sebelumnya, ditutup Penelitian ini mengisi celah tersebut dengan langkah-langkah berikut dan daftar bernomor tiga butir. Templat lengkap versi SIBI ada di Bagian 6.5.

## **3.5 Mekanika Penulisan**

- Judul dokumen KAPITAL SEMUA dan terpusat; judul alternatif ditulis normal setelahnya.

- Penomoran tabel dan gambar per bab: Tabel 2.2, Gambar 3.1, dengan judul; setiap tabel dan gambar dirujuk dalam teks sebelum muncul.

- Ejaan PUEBI: memengaruhi (bukan mempengaruhi), desimal koma (0,5 sampai 3 detik), persen tanpa spasi (80 persen), tanpa orang pertama (saya, kami).

- Subjek kalimat adalah penelitian ini, sistem, atau alat; paragraf berisi 3 sampai 8 kalimat; tidak ada bullet tanpa kalimat pengantar.

- Istilah teknis asing lazim dipertahankan dalam Latin: capture, dataset, device-free, embedded, dashboard; definisinya diberikan pada kalimat perkenalan istilah, bukan kurung berlebihan.

- Tidak ada penanda akhir dokumen artifisial seperti garis atau kalimat penutup meta; dokumen berakhir pada entri Daftar Pustaka terakhir.

# **4. EJAAN, KATA BAKU, DAN GAYA (PELAJARAN NASKAH-ID)**

## **4.1 Aturan yang Wajib Dipertahankan Saat Revisi**

Pada sesi perbaikan bahasa sebelumnya, empat DPJ sudah disunting menyeluruh dengan lebih dari 60 pasangan perbaikan berdasarkan aturan PUEBI dan pola-pola anti-kalke. Panduan ini meringkas aturan yang paling relevan agar pekerjaan revisi SIBI-only tidak menghidupkan kembali kesalahan yang sudah dibersihkan. Prinsipnya sederhana: saat menulis ulang sebuah paragraf, salin dari versi lama yang sudah bersih, bukan dari memori.

Tabel 4.1 Perbaikan baku yang sudah diterapkan dan harus dipertahankan

| **Pola yang dihindari**               | **Bentuk baku**                    | **Catatan**                                          |
|---------------------------------------|------------------------------------|------------------------------------------------------|
| et al.                                | dkk.                               | Sudah diganti 46 kali pada 4 DPJ; jangan muncul lagi |
| mempengaruhi                          | memengaruhi                        | PUEBI; pola pembuka corong memakai kata ini          |
| di mana (non-interogatif)             | yang di / letaknya                 | Di mana hanya untuk pertanyaan                       |
| koma sebelum sehingga                 | tanpa koma                         | Kalimat komposit EJ-10; periksa setiap sehingga      |
| entropy, threshold                    | entropi, ambang                    | Istilah Inggris non-lazim diindonesiakan             |
| lintas-person, kontak-less            | lintas-penandatangan, tanpa kontak | Anti-kalke Inggris; serangkai dengan tanda hubung    |
| antarsesi, antarruang (dipisah salah) | antarsesi, antarruang serangkai    | Awalan antar- ditulis serangkai                      |
| Doppler huruf kecil                   | Doppler (kapital)                  | Nama orang                                           |
| kalimat lebih dari 35 kata            | dipecah menjadi dua                | Kalimat efektif; cek paragraf hasil tempel           |
| Mengetahui hasil pengujian (tujuan)   | Menguji hasil pengujian            | Frasa kerja konkret, bukan nominalisasi              |

## **4.2 Alat Periksa dan Keputusan yang Masih Terbuka**

Pemeriksa bahasa periksa.py dari skill naskah-id bisa dijalankan pada file markdown untuk menemukan pola ejaan dan gaya yang melanggar; hasil bersih ditandai nol temuan. Jalankan alat ini setelah setiap sesi penyuntingan besar, bukan hanya di akhir, karena pola koma-sehingga dan kalimat panjang paling mudah terbawa saat menempel teks baru. Detail pemanggilan ada di Bagian 8.2.

Satu keputusan masih terbuka sejak sesi sebelumnya: pencetakan miring untuk istilah asing ditunda menunggu pedoman kampus, karena aturan lokal didahulukan dan konsistensi lebih penting daripada miring sebagian istilah saja. Sampai pedoman tersedia, pertahankan istilah teknis asing dalam bentuk tegak seperti sekarang, dan catat keputusan ini pada checklist Bagian 8 agar tidak terlupa saat dokumen final disiapkan.

# **5. DISIPLIN KLAIM SIBI-ONLY**

## **5.1 Aturan Inti**

Keempat aturan ini tidak berubah oleh pengetatan lingkup; yang berubah hanyalah objek yang tidak diklaim, yaitu BISINDO kini masuk daftar eksklusi eksplisit bersama penerjemahan kontinu dan multi-penandatangan. Pernyataan disiplin pada 5.3 sudah mengikat kelima hal itu dalam satu paragraf yang ditempel di akhir 1.4.

1. Semua klaim dibatasi studi kelayakan. Framing yang benar adalah menguji kelayakan, mengevaluasi kemampuan, dan menghasilkan dataset beserta rekomendasi, bukan membangun sistem jadi yang menerjemahkan.

2. Paradigma yang benar adalah klasifikasi gestur langsung dari pola CSI. Modul pose 17 keypoint RuView adalah stub dengan PCK@20 sekitar 3 persen sehingga ekstraksi pose atau kerangka tangan terlarang dijanjikan; preseden paradigma adalah SignFi 2018, DF-WiSLR 2020, Widar3.0 2021, dan FSL-CSI TENCON 2024.

3. Gerbang fisik Delta-CSI dua node ESP32 adalah titik go/no-go pada minggu ketiga; jadwal wajib menandainya eksplisit dan keputusan lanjut, kalibrasi ulang satu kali, atau beralih judul cadangan mengikutinya.

4. Risiko utama dan mitigasinya eksplisit per risiko pada Tabel 3.3, mencakup lintas-domain, dataset, konfound lingkungan, dan etika.

## **5.2 Tabel Batas Klaim Versi SIBI-only**

Tabel 5.1 mengikat apa yang boleh dan tidak boleh diklaim pada proposal versi SIBI-only. Gunakan tabel ini saat menyusun setiap paragraf klaim; bila sebuah kalimat berada di kolom kanan, tulis ulang sampai berada di kolom kiri atau hapus.

Tabel 5.1 Batas klaim proposal SIBI-only

| **Boleh diklaim**                                                                        | **Tidak boleh diklaim**                                            |
|------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| Kelayakan klasifikasi gestur terisolasi 5 sampai 12 kelas SIBI yang dominan gerak lengan | Penerjemah kalimat bahasa isyarat kontinu (BLEU/WER)               |
| Dataset CSI SIBI pertama: protokol perekaman + mini-dataset publik berlabel              | Dataset BISINDO atau pengenalan BISINDO pada penelitian ini        |
| Integrasi keluaran klasifikasi ke jalur alert RuView (MQTT/Home Assistant)               | Ekstraksi pose atau kerangka tangan (stub PCK@20 3 persen)         |
| Model sah per sesi atau per penandatangan dengan kalibrasi ulang                         | Multi-penandatangan simultan; akurasi lintas-ruang tanpa kalibrasi |
| Kebaruan kombinatif: pertama untuk SIBI via Wi-Fi CSI pada konteks edukasi               | Klaim menemukan metode baru secara umum                            |

## **5.3 Pernyataan Disiplin Klaim (Templat Siap Tempel)**

Pernyataan berikut ditempatkan sebagai paragraf penutup subbab 1.4, tepat setelah item tidak membahas. Templat ini sudah diadaptasi untuk lingkup SIBI-only, termasuk butir eksklusi BISINDO pada huruf e.

> Penelitian ini merupakan studi kelayakan pengenalan gestur terisolasi dari pola Wi-Fi CSI pada platform RuView (capture + DSP + alert) dengan target bahasa Sistem Isyarat Bahasa Indonesia (SIBI). Penelitian ini tidak mengklaim: (a) ekstraksi pose atau kerangka tangan; (b) penerjemahan kalimat bahasa isyarat kontinu; (c) pengenalan multi-penandatangan simultan; (d) akurasi lintas-ruang tanpa kalibrasi ulang; (e) pengenalan BISINDO atau sistem isyarat komunitas lain. Kelayakan diuji pada subset 5 sampai 12 gestur SIBI yang dominan gerak lengan, dengan satu penandatangan per sesi, di ruang edukasi yang terkalibrasi. Gerbang fisik Delta-CSI 2×ESP32 pada lokasi target (minggu ketiga) menjadi titik go/no-go penelitian.

# **6. PETA REVISI DPJ-4 KE LINGKUP SIBI-ONLY**

## **6.1 Ringkasan Perubahan Per Bagian**

Tabel 6.1 memetakan seluruh titik yang berubah saat dokumen SIBI+BISINDO dipadatkan menjadi SIBI-only, beserta tindakannya. Tiga bagian terakhir (biaya, risiko, daftar pustaka) secara prinsip tidak berubah isinya dan hanya perlu diperiksa ulang. Rincian templat untuk titik-titik besar ada pada subbab 6.2 sampai 6.7.

Tabel 6.1 Peta revisi per bagian dokumen

| **Bagian**                 | **Yang berubah**                                            | **Tindakan**                                                                   |
|----------------------------|-------------------------------------------------------------|--------------------------------------------------------------------------------|
| Judul utama + 2 alternatif | Frasa SIBI dan BISINDO / SIBI/BISINDO menjadi SIBI          | Ganti (templat 6.2)                                                            |
| Tabel 1.1 catatan pemetaan | Catatan baris utama menyebut dua sistem                     | Ganti menjadi SIBI (subset gestur terpilih)                                    |
| 1.1 Latar Belakang lapis 4 | Narasi ketegangan dua sistem                                | Tulis ulang dengan templat 6.3                                                 |
| 1.2 Rumusan Masalah        | SIBI/BISINDO pada 3 butir                                   | Ganti kata (templat 6.4)                                                       |
| 1.3 Tujuan Penelitian      | SIBI dan BISINDO pada pembuka                               | Ganti kata (templat 6.4)                                                       |
| 1.4 Batasan Masalah        | Butir 1 bermakna sama pada kedua sistem                     | Tulis ulang butir 1; sisipkan butir eksklusi BISINDO; tutup dengan templat 5.3 |
| 1.5 Manfaat Penelitian     | Klaim belum ada publikasi CSI SIBI atau BISINDO tetap benar | Pertahankan; cek ejaan                                                         |
| 2.5 Judul dan isi subbab   | Bahasa Isyarat Indonesia: SIBI dan BISINDO                  | Retitel Sistem Isyarat Bahasa Indonesia (SIBI) + tulis ulang (templat 6.5)     |
| 2.6 dan Tabel 2.2          | Baris Penelitian Ini: SIBI & BISINDO                        | Ganti sel menjadi SIBI; prosa gap tetap menyebut dua kutub                     |
| 3.1 Tahapan                | guru/pembina yang memahami SIBI dan BISINDO                 | Ganti menjadi menguasai SIBI                                                   |
| 3.5 Dataset                | Kriteria subset dua sistem                                  | Subset dari rujukan SIBI + preferensi separasi kinematik (6.6)                 |
| 3.6 Partisipan             | Penandatangan dewasa                                        | Sebut eksplisit guru/pembina SIBI                                              |
| Tabel 3.1 jadwal           | Baris W1-W2 menyebut SIBI/BISINDO                           | Ganti menjadi Daftar 5-12 gestur SIBI terpilih                                 |
| Tabel 3.2 biaya            | Tidak berubah                                               | Periksa ulang saja                                                             |
| 3.11 dan Tabel 3.3 risiko  | Tidak berubah                                               | Periksa ulang kata isyarat dua sistem                                          |
| DAFTAR PUSTAKA             | 19 entri tetap dipakai                                      | Pertahankan; kebijakan di 6.7                                                  |

## **6.2 Usulan Judul Versi SIBI-only**

Tiga judul berikut diadaptasi langsung dari versi lama dengan menghapus BISINDO dan merapikan polanya; pemetaan kata ke hal yang terukur tetap berlaku, yaitu SIBI berarti subset gestur terpilih, studi kelayakan berarti batas klaim, ESP32 dan Wi-Fi CSI berarti perangkat serta sinyal yang diklasifikasikan, dan prasarana edukasi berarti lokasi kalibrasi.

**Judul utama: PENGENALAN GESTUR BAHASA ISYARAT SIBI BERBASIS WI-FI CHANNEL STATE INFORMATION PADA ESP32 UNTUK PRASARANA EDUKASI: STUDI KELAYAKAN TRANSLASI TANPA KAMERA**

**Judul Alternatif 1:** Studi Kelayakan Klasifikasi Gestur Terisolasi SIBI dari Pola Wi-Fi CSI pada Platform RuView untuk Ruang Kelas Tunarungu

**Judul Alternatif 2:** Dataset dan Klasifikasi Gestur Sistem Isyarat Bahasa Indonesia (SIBI) dari Sinyal Wi-Fi CSI pada ESP32: Studi Kelayakan Alat Bantu Komunikasi Pendidikan Tunarungu

Judul Alternatif 2 sengaja memakai bentuk panjang Sistem Isyarat Bahasa Indonesia (SIBI) agar pola nama lengkap-lalu-singkatan tetap muncul minimal sekali di halaman judul dokumen. Setelah judul ditetapkan, samakan istilah bahasa target di Tabel 1.1 dengan catatan pemetaan yang baru sehingga tabel dan judul tidak saling bertentangan.

## **6.3 Menulis Ulang Lapis 4 Latar Belakang**

Lapis 4 versi lama memotivasi dua sistem dengan kalimat ketegangan SIBI-BISINDO; versi baru harus memotivasi satu sistem tanpa membohongi realitas lapangan. Templat berikut menjalankan tugas itu dalam satu paragraf utuh: memperkenalkan SIBI sebagai sistem formal sekolah, memberi dua keuntungan metodologis, memposisikan BISINDO sebagai pengembangan lanjutan, lalu menutup dengan kalimat korpus. Salin dan sesuaikan seperlunya, lalu lanjutkan dengan kalimat pengantar Tabel 1.1.

> Di Indonesia, sistem isyarat yang diajarkan pada lembaga pendidikan formal adalah SIBI (Sistem Isyarat Bahasa Indonesia), sistem yang bersifat formal dan terstandar sehingga definisi gesturnya dapat dirujuk secara konsisten pada satu rujukan yang sama. Menargetkan satu sistem formal memberikan dua keuntungan metodologis bagi studi kelayakan: dataset dapat didefinisikan secara konsisten dari satu rujukan sistem, dan beban pelabelan tetap terkendali pada durasi satu semester. Pengenalan sistem lain seperti BISINDO yang tumbuh secara alami di komunitas diposisikan sebagai pengembangan lanjutan setelah kelayakan paradigma terbukti pada SIBI. Berdasarkan uraian tersebut, penelitian ini dilakukan untuk menguji kelayakan pengenalan gestur terisolasi bahasa isyarat SIBI dari pola Wi-Fi CSI pada ESP32 sebagai langkah awal translasi tanpa kamera di prasarana edukasi. Tabel 1.1 merangkum usulan judul utama beserta dua judul alternatifnya.

## **6.4 Rumusan, Tujuan, dan Batasan Versi SIBI-only**

Tiga blok berikut sudah diadaptasi penuh dan siap tempel. Pembuka masing-masing mengikuti pola korpus dari Bagian 3.2. Perhatikan bahwa batasan kini berisi tujuh butir: satu butir eksklusi BISINDO disisipkan sebagai butir kedua agar keputusan lingkup terbaca sejak awal, dan butir terakhir tetap pola tidak membahas yang kini juga menyebut BISINDO secara eksplisit.

**Rumusan masalah (setelah pembuka 1.2):**

1. Bagaimana perancangan sistem capture Wi-Fi CSI dua node ESP32 berbasis platform RuView beserta protokol pengumpulan dataset gestur SIBI terisolasi di ruang edukasi yang terkalibrasi?

2. Bagaimana implementasi ekstraksi fitur dan pelatihan klasifikator gestur dari pola amplitudo, fase, dan Doppler CSI untuk subset gestur SIBI yang dominan gerak lengan?

3. Bagaimana hasil pengujian akurasi klasifikasi per gestur, tingkat alarm palsu, dan integrasi keluaran klasifikasi ke jalur alert RuView (MQTT/Home Assistant) sebagai indikator kelayakan translasi tanpa kamera?

**Tujuan penelitian (setelah pembuka 1.3):**

1. Merancang sistem capture Wi-Fi CSI dua node ESP32 berbasis RuView beserta protokol pengumpulan dataset gestur terisolasi SIBI yang terdokumentasi dan dapat direplikasi. 2. Mengimplementasikan ekstraksi fitur dan pelatihan klasifikator gestur dari pola amplitudo, fase, dan Doppler CSI untuk subset gestur SIBI yang dipilih. 3. Menguji akurasi klasifikasi per gestur, alarm palsu, dan kelayakan integrasi keluaran ke jalur alert RuView, termasuk keputusan go/no-go pada uji fisik Delta-CSI di minggu ketiga.

**Batasan masalah (setelah pembuka 1.4):**

1. Lingkup penelitian adalah studi kelayakan pengenalan gestur terisolasi (isolated) pada subset 5 sampai 12 gestur SIBI yang dominan gerak lengan dan memiliki definisi konsisten pada rujukan sistem yang sama, bukan penerjemah kalimat bahasa isyarat kontinu. 2. Target bahasa diikat pada SIBI; pengenalan BISINDO tidak diuji pada penelitian ini dan diposisikan sebagai pengembangan lanjutan. 3. Satu penandatangan per sesi capture di zona pengambilan data; sistem tidak mengidentifikasi individu dan person counting tidak dijanjikan karena kualitasnya menurun pada lebih dari dua sampai tiga subjek. 4. Kamera hanya digunakan saat perekaman dataset untuk pelabelan ground truth; penggunaan operasional sistem bebas kamera. 5. Ekstraksi pose atau kerangka tangan tidak dipakai dan tidak dijanjikan karena modul pose on-device RuView masih berupa stub (PCK@20 sekitar 3 persen); klasifikasi dilakukan langsung dari pola CSI. 6. Setiap ruang edukasi mitra di 【Nama Sekolah/Lokasi】 wajib dikalibrasi ulang (600 frame + 8 anchor) dan model dianggap sah untuk sesi yang sama, bukan lintas ruang tanpa kalibrasi. 7. Penelitian ini tidak membahas penerjemahan kontinu dua arah, pengenalan BISINDO, pengenalan beberapa penandatangan secara simultan, akurasi lintas ruang tanpa kalibrasi, ekstraksi pose tangan, serta aspek komersialisasi alat.

## **6.5 BAB II: Subbab SIBI dan Prosa Gap**

Subbab 2.5 diganti judulnya menjadi Sistem Isyarat Bahasa Indonesia (SIBI). Paragraf pertamanya mendefinisikan SIBI dan menautkan sifat formal-terstandar pada kebutuhan dataset; paragraf keduanya menghadirkan lanskap riset isyarat Indonesia yang seluruhnya berbasis visi sebagai bukti celah, dengan tetap menyitasi kelima referensi lokal. Referensi BISINDO tidak dihapus karena justru mereka yang membuktikan bahwa belum ada jalur CSI pada bahasa isyarat Indonesia apa pun; yang berubah adalah peran mereka, dari objek pembanding sejajar menjadi bukti lanskap dan celah.

> Pembuka 2.5 baru: Sistem Isyarat Bahasa Indonesia (SIBI) merupakan sistem isyarat yang bersifat formal dan terstandar serta diajarkan pada lembaga pendidikan formal sehingga definisi gesturnya dapat dirujuk secara konsisten untuk pembangunan dataset penelitian ini. Pada penelitian ini, subset gestur diambil dari sistem SIBI dengan preferensi gestur yang dominan gerak lengan agar komponen Doppler CSI cukup kuat untuk dipisahkan dari latar.

> Prosa lanskap dan celah (paragraf kedua 2.5): Riset pengenalan bahasa isyarat Indonesia tumbuh pesat dan seluruhnya berbasis kamera serta pengolahan citra: Dwijayanti dkk. (2021) menerapkan CNN untuk pengenalan isyarat Indonesia \[3\], dataset video tingkat kata disusun oleh Kindy dkk. (2025) \[17\], pengenalan kalimat berbasis arsitektur 3D dilakukan Wiguna dan Rojali (2025) \[18\], dan pendekatan sadar-ruang ditawarkan Sebastian dkk. (2025) \[19\]. Tinjauan sistematis Sanjaya dkk. (2023) menegaskan dominasi kamera pada keseluruhan riset tersebut dan mencatat belum adanya pendekatan sensor wireless device-free \[2\]. Belum ditemukan satu pun publikasi pengenalan isyarat berbasis Wi-Fi CSI untuk SIBI maupun BISINDO sehingga celah kebaruan bagi penelitian ini tetap terbuka.

Pada 2.6, baris Penelitian Ini pada Tabel 2.2 diubah dari SIBI & BISINDO menjadi SIBI pada kolom Bahasa Isyarat Indonesia, sementara prosa gap tetap menuliskan dua kutub (isyarat CSI pada bahasa dunia versus riset isyarat Indonesia berbasis kamera) karena kutub-kutub itu sendiri tidak berubah oleh pengetatan lingkup. Daftar tiga butir mengisi celah dipertahankan dengan mengganti SIBI dan BISINDO menjadi SIBI pada butir pertama.

## **6.6 BAB III: Subset Gestur dan Partisipan**

Pada 3.1, penggantian kata memahami SIBI dan BISINDO menjadi menguasai SIBI sudah cukup. Pada 3.5, kriteria pemilihan subset ditulis ulang: gestur diambil dari rujukan sistem SIBI yang sama, didahulukan yang dominan gerak lengan, dan yang secara kinematik berbeda besar satu sama lain agar confusion matrix tidak penuh pada pasangan mirip; kriteria mirip gerak tetap menjadi item pada Tabel 3.3. Tabel 3.1 baris pertama menjadi Daftar 5-12 gestur SIBI terpilih beserta lembar definisi.

Pada 3.6, subjek utama ditulis eksplisit sebagai guru atau pembina yang menguasai SIBI, karena mereka yang mengajarkan sistem formal di sekolah mitra; siswa tetap mungkin menjadi partisipan sukarela untuk pengujian variasi dengan persetujuan orang tua. Seluruh pernyataan etika, mode privasi, dan perekaman kamera untuk ground truth dipertahankan apa adanya karena tidak tersentuh pengetatan lingkup.

## **6.7 Kebijakan Referensi**

1. Semua 19 referensi DPJ-4 tetap dipakai. Kelima entri isyarat Indonesia (Dwijayanti; Kindy; Wiguna dan Rojali; Sebastian; Sanjaya) mayoritas menargetkan BISINDO; pada proposal SIBI-only posisinya adalah bukti lanskap dan bukti celah, bukan target penelitian.

2. Klaim kebaruan ditulis dua lapis: belum ada publikasi CSI untuk SIBI maupun BISINDO (pernyataan tentang literatur, tetap benar), lalu penelitian ini menargetkan SIBI (pernyataan tentang lingkup). Jangan menulis belum ada riset apa pun tentang SIBI karena itu tidak terverifikasi.

3. Dilarang menambah referensi baru tanpa verifikasi Crossref yang mencocokkan judul, penulis, tahun, dan venue terhadap DOI terdaftar; referensi tanpa DOI wajib lolos verifikasi web kedua berupa venue, tahun, dan penulis.

4. Bila pembimbing meminta sumber definisi SIBI, cari literaturnya, verifikasi dulu sesuai aturan nomor 3, lalu masukkan; jangan mengarang tahun atau nomor kamus.

5. Bila referensi bertambah, perbarui file verified_refs.json pada folder 06-referensi-isyarat agar arsip verifikasi tetap satu sumber kebenaran.

# **7. DAFTAR REFERENSI TERVERIFIKASI (PERAN SIBI-ONLY)**

## **7.1 Peta Referensi dan Perannya**

Seluruh 19 referensi pada DPJ-4 sudah diverifikasi melalui Crossref pada sesi riset T2-a dan tidak ada satu pun yang hanya terverifikasi web. Tabel 7.1 merangkum setiap entri beserta perannya pada proposal SIBI-only agar saat menulis dapat langsung dipilih referensi yang tepat untuk setiap klaim. Kategorinya empat: intisari paradigma (bukti klasifikasi isyarat dari CSI), konteks edukasi, lanskap-celah (riset isyarat Indonesia berbasis visi), dan teknis pipeline.

Tabel 7.1 Referensi terverifikasi dan perannya pada proposal SIBI-only

| **No** | **Referensi**                                        | **DOI**                           | **Peran**                                      |
|--------|------------------------------------------------------|-----------------------------------|------------------------------------------------|
| 1      | Rodríguez-Correa dkk. (2023), Frontiers in Education | 10.3389/feduc.2023.1121597        | Konteks edukasi: hambatan komunikasi tunarungu |
| 2      | Sanjaya dkk. (2023), Indonesian J. Computer Science  | 10.33022/ijcs.v12i6.3539          | Lanskap-celah: SLR BISINDO 100 persen visi     |
| 3      | Dwijayanti dkk. (2021), IJACSA                       | 10.14569/IJACSA.2021.0121046      | Lanskap-celah: CNN isyarat Indonesia           |
| 4      | Ma dkk. (2019), ACM Computing Surveys                | 10.1145/3310194                   | Teknis: survei kanonik CSI                     |
| 5      | Hernandez dan Bulut (2020), WoWMoM                   | 10.1109/WoWMoM49955.2020.00056    | Teknis: basis ESP32-CSI-Tool                   |
| 6      | Ma dkk. (2018), SignFi, IMWUT                        | 10.1145/3191755                   | Intisari: 276 isyarat dari CSI                 |
| 7      | Baldeo dkk. (2024), TENCON                           | 10.1109/TENCON61640.2024.10903008 | Intisari: preseden FSL, analog porting ke SIBI |
| 8      | Shang dan Wu (2017), MobiArch                        | 10.1145/3097620.3097624           | Teknis: topologi multi-node                    |
| 9      | Thariq Ahmed dkk. (2020), DF-WiSLR                   | 10.1016/j.pmcj.2020.101289        | Intisari: pipeline 30+19 gestur device-free    |
| 10     | Thariq Ahmed dan Ahmad (2021), IAICT                 | 10.1109/IAICT52856.2021.9532548   | Teknis: LSTM temporal pada CSI                 |
| 11     | Zhang dkk. (2021), Widar3.0, TPAMI                   | 10.1109/TPAMI.2021.3105387        | Intisari: strategi lintas-domain, bukan janji  |
| 12     | Chen dkk. (2023), ACM Computing Surveys              | 10.1145/3570325                   | Teknis: survei cross-domain                    |
| 13     | Hao dkk. (2020), Wi-SL, Sensors                      | 10.3390/s20144025                 | Teknis: 12 gestur perangkat murah              |
| 14     | Sruthi dkk. (2024), HandFi, Procedia CS              | 10.1016/j.procs.2024.04.042       | Teknis: pipeline amplitudo-fase                |
| 15     | Cai dkk. (2024), Sensors                             | 10.3390/s24113414                 | Teknis: komplementaritas amplitudo-fase        |
| 16     | Qin dkk. (2023), WiASL, Measurement                  | 10.1016/j.measurement.2023.113125 | Teknis: arah aplikasi praktis                  |
| 17     | Kindy dkk. (2025), Procedia CS                       | 10.1016/j.procs.2025.08.277       | Lanskap-celah: dataset video BISINDO           |
| 18     | Wiguna dan Rojali (2025), IJACSA                     | 10.14569/IJACSA.2025.0160941      | Lanskap-celah: level kalimat masih visi        |
| 19     | Sebastian dkk. (2025), Procedia CS                   | 10.1016/j.procs.2025.09.042       | Lanskap-celah: klasifikasi per-gestur          |

Kelima entri lanskap-celah tetap wajib disitasi meski menargetkan BISINDO, dengan peran sebagai bukti celah sebagaimana dijelaskan pada 6.5 dan 6.7. Bila penulisan BAB II akhirnya memakai lebih sedikit entri daripada 19, pastikan tidak ada nomor sitasi yang menggantung tanpa entri maupun entri tanpa sitasi; penomoran mengikuti urutan kemunculan dalam teks.

# **8. CHECKLIST AKHIR DAN ALAT QA**

## **8.1 Checklist Rubrik D1-D6 Versi SIBI-only**

- D1 Struktur: hanya BAB I-III + DAFTAR PUSTAKA; semua subbab wajib Tabel 2.1 terisi; enam tabel utuh; penamaan bab konsisten (KAJIAN PUSTAKA, METODE PENELITIAN); tanpa cover, tanpa abstrak, tanpa daftar isi.

- D2 Pola bahasa: keempat pembuka subbab BAB I memakai pola korpus; item tujuan berupa frasa kerja; batasan ditutup butir tidak membahas; target bahasa konsisten SIBI di seluruh dokumen.

- D3 Sitasi: pola Nama dkk. (Tahun) menjelaskan/menunjukkan; nomor sitasi berurutan dan cocok satu-satu dengan Daftar Pustaka; APA 7 + URL DOI; nol referensi fiktif.

- D4 Mekanika: judul kapital semua; Tabel/Gambar bernomor per bab dan dirujuk dalam teks; memengaruhi; desimal koma; tanpa orang pertama; nol kalimat lebih dari 35 kata.

- D5 Disiplin: pernyataan studi kelayakan menempel di akhir 1.4; pose stub tidak dijanjikan; gerbang go/no-go minggu ketiga eksplisit di Tabel 3.1 dan 3.8; risiko beserta fallback lengkap.

- D6 Kelengkapan: satu judul utama + dua alternatif; jadwal semester; biaya Rupiah; risiko; placeholder eksplisit 【Nama Sekolah/Lokasi】 dan 【Mohon diisi】 pada biaya; tanpa halaman sampul.

- Konsistensi lingkup (baru): pencarian kata BISINDO hanya boleh muncul pada konteks literatur 2.5, butir batasan, pernyataan disiplin butir e, dan Daftar Pustaka; pencarian frasa SIBI dan BISINDO maupun SIBI/BISINDO sebagai target harus nol.

## **8.2 Alat QA dan Urutan Menjalankannya**

1. Periksa bahasa: python3 skills/naskah-id/scripts/periksa.py \<file.md\> dijalankan setelah setiap sesi penyuntingan; target nol temuan.

2. Evaluasi rubrik: python3 skills/proposal-writing/scripts/evaluator.py --doc \<file.md\> pada dokumen akhir; skor minimal 0,8 dengan dimensi terendah diperbaiki lebih dulu.

3. Regenerasi DOCX: node scripts/generate_dpj.js setelah konten pada modul JS disunting, atau sunting DOCX langsung bila revisi kecil; jangan biarkan dua format berbeda isi.

4. Postcheck DOCX: python3 \<folder skill docx\>/scripts/postcheck.py \<file.docx\>; semua error wajib dibereskan sebelum dokumen dipakai.

5. Sinkronisasi dua format: python3 scripts/verify_sync_dpj.py membandingkan markdown dan DOCX hasil pandoc round-trip; target identik setelah normalisasi padding tabel.

6. Konversi PDF untuk pemeriksaan visual: soffice --headless --convert-to pdf, lalu periksa jumlah halaman, tabel three-line, dan halaman judul.

## **8.3 Keputusan yang Masih Milik Pemilik dan Langkah Berikutnya**

Dengan seluruh checklist terpenuhi, dokumen hasil revisi berada pada taruhan mutu yang sama dengan empat DPJ sebelumnya yang semuanya mencapai skor evaluator 1,0. Perbedaannya kini terletak pada lingkup yang lebih fokus: satu sistem isyarat, satu rujukan definisi, dan satu lintasan kebaruan yang jelas untuk dibawa ke meja pembimbing.

1. Konfirmasi judul kepada pembimbing: pilih di antara judul utama dan dua alternatif pada 6.2 sebelum revisi penuh dimulai, karena seluruh dokumen mengikuti judul yang dipilih.

2. Isi placeholder: 【Nama Sekolah/Lokasi】 pada 1.4 dan 3.6, dan baris total biaya pada Tabel 3.2 bila angka final sudah ada.

3. Konfirmasi pencetakan miring istilah asing begitu pedoman kampus tersedia, lalu jalankan ulang seluruh QA.

4. Lakukan uji fisik Delta-CSI dua node ESP32 di lokasi target pada minggu ketiga; hasil gerbang ini menentukan apakah proposal berjalan, dikalibrasi ulang, atau beralih ke judul cadangan.

5. Setelah revisi SIBI-only selesai dan disetujui pembimbing, perbarui markdown dan DOCX bersamaan, jalankan seluruh alat QA pada 8.2, lalu commit dan push ke repositori dengan pesan yang menyebut pengetatan lingkup.
