**PROPOSAL PENGAJUAN JUDUL SKRIPSI**

*Opsi Alat 3 dari 4 — Pemantauan Wi-Fi CSI pada Kamar Asrama SLB (Malam)*

**Judul Utama yang Diusulkan**

**SISTEM PEMANTAUAN POLA TIDUR DAN DETEKSI ANOMALI NOCTURNAL SISWA ASRAMA SLB BERBASIS WI-FI CSI PADA ESP32: STUDI KELAYAKAN NON-KONTAK TANPA KAMERA**

**Judul Alternatif 1:** Pemantauan Laju Napas dan Status Tidur Tanpa Kontak untuk Pendampingan Siswa Asrama SLB Berbasis Wi-Fi Channel State Information

**Judul Alternatif 2:** Studi Kelayakan Wi-Fi Sensing untuk Sistem Peringatan Dini Kondisi Malam Siswa Berkebutuhan Khusus pada Asrama SLB

# **BAB I**

# **PENDAHULUAN**

## **1.1 Latar Belakang**

Perkembangan teknologi telah memengaruhi berbagai layanan pengasuhan, termasuk cara asrama menjaga keamanan dan kenyamanan penghuninya pada malam hari. Asrama SLB melayani siswa yang membutuhkan pendampingan bahkan saat tidur sehingga pengasuh berpatroli berkala untuk memastikan setiap anak tidur dengan aman, napas teratur, dan tidak ada kondisi yang memerlukan bantuan segera. Patroli manual memiliki dua keterbatasan yang saling bertentangan: interval patroli yang rapat mengganggu kualitas tidur anak, sementara interval yang jarang menambah risiko kejadian tidak terdeteksi, seperti anak yang tidak bergerak lama atau napas yang tidak teratur. Kondisi tersebut menunjukkan bahwa kebutuhan akan alat bantu yang memantau tanpa mengganggu dan tanpa kamera di ruang tidur sangat spesifik pada konteks ini.

Wi-Fi Channel State Information (CSI) memungkinkan pemantauan tidur tanpa kontak dan tanpa kamera. Liu dkk. (2014) membuktikan sejak awal bahwa sinyal Wi-Fi dapat memantau tidur tanpa kontak, termasuk respirasi, posisi, dan gerakan menggeliat \[3\]. Tataraidze dkk. (2019) menunjukkan deteksi napas saat tidur dari perangkat Wi-Fi sekelas ponsel \[4\], Burimas dkk. (2024) memantau laju napas tidur pada perangkat mikrokontroler murah \[5\], dan Kontou dkk. (2024) memperbaiki deteksi respirasi dengan jaringan saraf tiruan \[6\]. Pada populasi rentan, Touhiduzzaman dkk. (2024) menerapkan sistem sensing Wi-Fi untuk pelacakan aktivitas harian pada hunian lansia \[9\], yang menunjukkan penerapan pada penghuni sensitif dapat dilakukan dengan tata kelola yang tepat. Pada penelitian ini, CSI digunakan untuk membaca status tidur dan anomali malam pada tingkat kamar, bukan pada tingkat individu.

Tantangan utama pada konteks asrama SLB bukan pada kemampuan dasar sensing, melainkan pada dua hal: populasi dan etika. Secara populasi, band filter napas pada sistem bawaan dirancang untuk orang dewasa, sementara laju napas anak usia sekolah berada pada rentang 18 hingga 25 napas per menit yang mendekati batas atas band sehingga penyesuaian filter menjadi bagian dari pertanyaan penelitian. Secara etika, ruang tidur anak adalah konteks paling sensitif dari seluruh alat yang dipertimbangkan dalam rangkaian riset ini: persetujuan orang tua dan wali wajib, hak menarik diri harus mutlak, dan posisi sistem sebagai pendeteksi kondisi untuk pendamping, bukan pengawas perilaku, harus dinyatakan eksplisit sejak proposal.

Keunggulan privasi arsitektur ini perlu dinyatakan secara proporsional. Sinyal Wi-Fi pada arsitektur penelitian ini tidak dapat mengidentifikasi individu dan tidak menyimpan biometrik; mode privasi membuang fitur biometrik sebelum data keluar dari node. Namun literatur juga menunjukkan bahwa pengenalan identitas dari sinyal Wi-Fi pada skenario lain tetap mungkin \[10\], dan pekerjaan terbaru bahkan menawarkan pemantauan posisi tidur in-bed dengan pembelajaran privasi-preservasi \[8\], menandakan bahwa kesadaran privasi pada sensing tidur adalah norma penelitian yang sedang tumbuh. Proposal ini mengikuti norma tersebut dengan tata kelola izin berjenjang.

Pada level literatur, pemantauan tidur CSI untuk orang dewasa merupakan area yang ramai \[3\] \[4\] \[5\] \[6\], namun pencarian awal yang dilakukan pada penyusunan proposal ini belum menemukan penerapan pada asrama SLB atau populasi anak berkebutuhan khusus sehingga celah ini berlabel terbatas-pencarian dan akan diverifikasi ulang bersama pembimbing. Berdasarkan uraian tersebut, penelitian ini dilakukan untuk menguji kelayakan pemantauan pola tidur dan deteksi anomali nocturnal siswa asrama SLB tanpa kamera pada ESP32, dengan asumsi keras satu penghuni per kamar dan framing skrining untuk pendamping. Tabel 1.1 merangkum usulan judul utama dan dua judul alternatifnya.

Tabel 1.1 Usulan judul penelitian

| **Kategori** | **Usulan Judul**                                                                                                                                   | **Catatan Pemetaan**                                                                                                                         |
|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Utama        | Sistem Pemantauan Pola Tidur dan Deteksi Anomali Nocturnal Siswa Asrama SLB Berbasis Wi-Fi CSI pada ESP32: Studi Kelayakan Non-Kontak Tanpa Kamera | Terpetakan ke fitur terukur (status tidur, laju napas, anomali inaktivitas) dan protokol izin berjenjang yang realistis dalam satu semester. |
| Alternatif 1 | Pemantauan Laju Napas dan Status Tidur Tanpa Kontak untuk Pendampingan Siswa Asrama SLB Berbasis Wi-Fi Channel State Information                   | Dipilih bila fokus pada laju napas; evaluasi tepi band filter untuk anak menjadi bagian inti.                                                |
| Alternatif 2 | Studi Kelayakan Wi-Fi Sensing untuk Sistem Peringatan Dini Kondisi Malam Siswa Berkebutuhan Khusus pada Asrama SLB                                 | Dipilih bila pembimbing mengutamakan framing paling aman dan sederhana.                                                                      |

## **1.2 Rumusan Masalah**

Berdasarkan latar belakang permasalahan yang telah diuraikan serta untuk menjawab permasalahan yang menjadi fokus dalam penelitian ini, maka dapat dirumuskan beberapa rumusan masalah yang akan dikaji lebih lanjut. Rumusan masalah pada penelitian ini adalah sebagai berikut.

1. Bagaimana rancangan uji Delta-CSI pada kamar asrama menghasilkan deteksi status tidur dan estimasi laju napas yang andal pada kamar tunggal penghuni anak SLB, dengan memperhitungkan tepi band filter untuk laju napas anak 18 hingga 25 napas per menit?

2. Bagaimana latensi dan tingkat alarm palsu deteksi anomali inaktivitas nocturnal dibandingkan catatan pendamping asrama, diukur per kamar per minggu?

3. Bagaimana penyesuaian parameter sensing dari nilai dewasa ke populasi anak dirumuskan menjadi rekomendasi kalibrasi yang dapat dipakai ulang oleh asrama lain?

## **1.3 Tujuan Penelitian**

Penelitian ini bertujuan menguji kelayakan pemantauan pola tidur dan deteksi anomali nocturnal siswa asrama SLB berbasis Wi-Fi CSI tanpa kamera pada ESP32. Adapun tujuan dari penelitian ini adalah sebagai berikut.

1. Merancang uji Delta-CSI kondisi kamar kosong, penghuni terjaga, dan penghuni tidur sebagai gerbang go/no-go kelayakan fisik sinyal pada kamar asrama.

2. Mengevaluasi deteksi status tidur dan estimasi laju napas tanpa kontak pada populasi anak, termasuk perilaku tepi band filter bawaan.

3. Menguji deteksi anomali inaktivitas nocturnal dengan metrik latensi dan alarm palsu per kamar per minggu terhadap catatan pendamping, serta merumuskan rekomendasi parameter dari dewasa ke anak dan protokol izin berjenjang.

## **1.4 Batasan Masalah**

Agar penelitian ini memiliki ruang lingkup yang jelas dan terarah sesuai dengan tujuan yang telah ditetapkan, maka ditentukan batasan masalah guna membatasi pembahasan terhadap aspek-aspek yang relevan dengan topik penelitian. Adapun batasan masalah pada penelitian ini adalah sebagai berikut.

1. Satu penghuni per kamar adalah asumsi keras; kamar dengan dua penghuni atau lebih berada di luar lingkup karena superposisi sinyal belum terpecahkan.

2. Seluruh keluaran berstatus skrining untuk pendamping, bukan diagnosis; modul skrining apnea eksperimental pada platform bawaan tidak dijanjikan dan tidak dikompilasi.

3. Tidak ada identifikasi individu dan tidak ada penyimpanan biometrik; sistem melaporkan status kamar, bukan profil anak.

4. Eksperimen hanya berjalan pada kamar yang telah mendapat persetujuan orang tua/wali, pengasuh asrama, dan kepala sekolah, dengan hak menarik diri kapan pun.

5. Penelitian ini tidak membahas diagnosis kondisi medis, hipnogram klinis, skrining apnea, multipenghuni per kamar, maupun identifikasi individu penghuni.

## **1.5 Manfaat Penelitian**

Pemantauan tidur tanpa kontak pada populasi anak berkebutuhan khusus belum banyak dilaporkan di literatur sehingga hasil penelitian ini berkontribusi pada literatur sekaligus pada praktik pengasuhan asrama. Kerangka izin berjenjang yang tertulis juga memberi contoh penelitian pada ruang paling sensitif secara etis. Manfaat penelitian ini diuraikan sebagai berikut.

# **BAB II**

# **KAJIAN PUSTAKA**

## **2.1 Wi-Fi Channel State Information**

Wi-Fi Channel State Information (CSI) merupakan informasi per subcarrier yang menggambarkan kondisi kanal propagasi sinyal Wi-Fi, mencakup amplitudo dan fase pada tiap subcarrier. Gerakan dada dan tubuh orang yang bernapas mengubah kanal propagasi secara periodik sehingga pola napas dapat dibaca dari sinyal tanpa kontak. Ma dkk. (2019) mengelompokkan estimasi respirasi sebagai salah satu keluarga aplikasi utama sensing Wi-Fi pada manusia \[1\], dan Hernandez dan Bulut (2020) membuktikan sensing Wi-Fi mandiri dapat berjalan pada perangkat kelas IoT murah \[2\] yang menjadi dasar pemilihan ESP32 pada penelitian ini. Kombinasi keduanya menegaskan bahwa pemantauan tidur tanpa kontak dapat dibangun di atas perangkat yang terjangkau oleh asrama.

## **2.2 Mikrokontroler ESP32**

ESP32 adalah mikrokontroler murah dengan radio Wi-Fi bawaan yang mampu mengekspor CSI melalui firmware khusus. Hernandez dan Bulut (2020) menunjukkan sensing Wi-Fi mandiri untuk deteksi mobilitas aktif berjalan penuh pada perangkat kelas Internet of Things \[2\]. Burimas dkk. (2024) melangkah lebih jauh dengan memantau laju napas tidur pada perangkat mikrokontroler murah dalam lingkungan terkendali \[5\], yang membuktikan rantai perangkat murah hingga aplikasi tidur adalah jalur riset yang sah. Untuk asrama, karakteristik perangkat murah, berdaya tetap, dan mudah dipasang ini memenuhi kendala biaya dan pemeliharaan; klaim hemat daya node ESP32-C6 low-power belum tervalidasi penuh sehingga penelitian ini memakai ESP32-S3 dengan adaptor daya tetap.

## **2.3 Platform RuView**

Sistem dibangun di atas RuView, proyek open-source (github.com/ruvnet/RuView) yang menyediakan firmware ESP32 untuk capture CSI, server pengolahan Rust, mesin status semantik, dashboard, serta alert MQTT dan Home Assistant. Fitur yang relevan untuk alat ini meliputi mesin status someone_sleeping yang pada pengujian terpisah mencapai F1 0,84 pada data held-out, estimasi laju napas dari band 0,1 hingga 0,5 Hz, anomali inaktivitas no_movement, tren vital mingguan, serta dashboard demo pemantauan tidur. Seluruh keluaran diberi penanda skrining dan tidak diklaim klinis.

Tabel 2.1 memetakan fitur RuView untuk alat ini beserta statusnya. Tiga catatan jujur wajib dibaca sejak awal. Pertama, band filter napas dikodekan permanen untuk rentang napas dewasa; laju napas anak 18 hingga 25 napas per menit mendekati batas atas band sehingga perilaku tepi band wajib dievaluasi, dan bila perlu, konstanta filter diubah secara terdokumentasi. Kedua, modul skrining apnea pada platform berstatus eksperimental dan hanya aktif bila dikompilasi dengan fitur khusus sehingga tidak diaktifkan dan tidak dijanjikan. Ketiga, klaim hemat daya node ESP32-C6 untuk deployment malam belum tervalidasi penuh sehingga penelitian ini memakai ESP32-S3 dengan adaptor daya tetap.

Tabel 2.1 Pemetaan fitur RuView untuk alat kamar asrama SLB

| **Fitur RuView**                                         | **Peran pada Penelitian**                   | **Status**                                            |
|----------------------------------------------------------|---------------------------------------------|-------------------------------------------------------|
| Capture CSI ESP32 + streaming UDP (format frame ADR-018) | Sumber data utama                           | Terukur (MEASURED)                                    |
| Mesin status someone_sleeping                            | Status sedang tidur per kamar               | Terukur (F1 0,84 held-out)                            |
| Estimasi laju napas (band 0,1-0,5 Hz)                    | Pemantauan napas saat tidur                 | Terukur untuk dewasa; tepi band anak wajib dievaluasi |
| No_movement + anomali inaktivitas                        | Peringatan anak tidak bergerak terlalu lama | Ambang dewasa, wajib disetel ulang                    |
| Tren vital mingguan                                      | Ringkasan pola untuk pengasuh asrama        | Terukur                                               |
| Dashboard pemantauan tidur (demo)                        | Antarmuka skrining untuk pendamping         | Demo, dengan penanda skrining                         |
| Privacy mode (strip fitur biometrik)                     | Kepatuhan etika ruang tidur anak            | Terukur, diaktifkan penuh                             |
| Kalibrasi 600 frame + enrollment 8 anchor per kamar      | Kalibrasi ruangan sekitar 4 menit           | Terukur                                               |
| Skrining apnea (modul medis eksperimental)               | Tidak diaktifkan, tidak dijanjikan          | Eksperimental, tidak tervalidasi                      |
| Klaim hemat daya ESP32-C6 LP-core                        | Tidak dipakai; memakai S3 daya tetap        | Belum tervalidasi perangkat                           |

## **2.4 Pemantauan Tidur dan Laju Napas Tanpa Kontak**

Pemantauan tidur tanpa kontak via Wi-Fi memiliki fondasi literatur yang matang pada orang dewasa. Liu dkk. (2014) menunjukkan Wi-Sleep yang memantau respirasi, posisi, dan gerakan menggeliat dari perangkat Wi-Fi umum \[3\]. Tataraidze dkk. (2019) menguji deteksi napas saat tidur melalui CSI pada ponsel tanpa sensor tambahan \[4\], dan Kontou dkk. (2024) meningkatkan deteksi respirasi dengan metode jaringan saraf tiruan pada jurnal biomedis IEEE \[6\]. Pada tema skrining tidur berbasis CSI, Chang dkk. (2023) mendeteksi kejadian apnea dan gerakan anggota badan dari sinyal CSI dengan pembelajaran berbasis attention \[7\]. Penelitian ini mengambil posisi yang jujur terhadap arah tersebut: skrining apnea pada platform bawaan berstatus eksperimental dan tidak tervalidasi sehingga tidak dijanjikan dalam lingkup skripsi; yang dijanjikan adalah deteksi anomali inaktivitas dan pemantauan laju napas untuk pendamping, sejalan dengan norma literatur yang menempatkan sistem semacam ini sebagai alat bantu, bukan pengganti polisomnografi.

## **2.5 Privasi dan Etika pada Populasi Rentan**

Privasi pada sensing tidur menjadi perhatian literatur yang tumbuh. Pich dkk. (2025) mengangkat pemantauan posisi tidur in-bed dengan pembelajaran privasi-preservasi \[8\], dan Mosharaf dkk. (2024) merangkum kemungkinan identifikasi manusia dari sinyal Wi-Fi yang menuntut kewaspadaan tata kelola data \[10\]. Untuk populasi rentan, Touhiduzzaman dkk. (2024) mendokumentasikan penerapan sensing Wi-Fi pada hunian lansia berpenghasilan rendah beserta persoalan operasionalnya \[9\], memberi preseden bahwa pemantauan penghuni sensitif layak dilakukan bila tata kelola izin dan ekspektasi dikelola dengan benar. Penelitian ini mengikuti pola tersebut: persetujuan berjenjang tertulis, hak menarik diri mutlak, sistem tanpa identifikasi individu, dan posisi eksplisit sebagai deteksi kondisi untuk pendamping, bukan pengawasan perilaku.

## **2.6 Penelitian Terdahulu**

Berdasarkan tabel perbandingan di atas, terlihat bahwa penelitian-penelitian sebelumnya matang pada pemantauan tidur CSI orang dewasa dan baru sebagian menyentuh perangkat murah atau populasi rentan. Belum banyak penelitian yang secara spesifik menerapkan pemantauan tidur CSI pada asrama pendidikan khusus dengan populasi anak. Masih terdapat beberapa celah masalah (gap) yang belum terselesaikan secara simultan oleh peneliti sebelumnya. Penelitian ini mengisi celah tersebut dengan langkah-langkah berikut.

1. Menempatkan pemantauan tidur CSI pada konteks asrama SLB dengan asumsi keras satu penghuni per kamar dan framing skrining untuk pendamping.

2. Mengevaluasi tepi band filter napas untuk laju napas anak 18 hingga 25 napas per menit secara eksplisit sebagai bagian dari pertanyaan penelitian.

3. Menyusun protokol izin berjenjang orang tua-sekolah-pengasuh yang dapat direplikasi oleh asrama lain tanpa kamera dan tanpa penyimpanan biometrik.

Tabel 2.2 Perbandingan penelitian terdahulu

| **Peneliti (Tahun) dan Judul Singkat**                  | **Sinyal CSI** | **Tidur/Napas** | **Perangkat Murah** | **Populasi Rentan** | **Privasi Dikelola** |
|---------------------------------------------------------|----------------|-----------------|---------------------|---------------------|----------------------|
| Liu dkk. (2014) — Wi-Sleep tanpa kontak via Wi-Fi      | √              | √               | −                   | −                   | −                    |
| Tataraidze dkk. (2019) — napas tidur via ponsel       | √              | √               | √                   | −                   | −                    |
| Burimas dkk. (2024) — laju napas mikrokontroler murah | √              | √               | √                   | −                   | −                    |
| Kontou dkk. (2024) — respirasi dengan ANN             | √              | √               | −                   | −                   | −                    |
| Chang dkk. (2023) — apnea + gerakan anggota badan     | √              | √               | −                   | −                   | −                    |
| Pich dkk. (2025) — posisi tidur privasi-preservasi    | √              | √               | −                   | −                   | √                    |
| Touhiduzzaman dkk. (2024) — deployment hunian lansia  | √              | −               | √                   | √                   | √                    |
| Penelitian Ini                                          | √              | √               | √                   | √                   | √                    |

# **BAB III**

# **METODE PENELITIAN**

## **3.1 Tahapan Penelitian**

Penelitian dalam proposal ini dilaksanakan melalui beberapa tahapan yang tersusun secara sistematis sehingga membentuk suatu alur penelitian yang terstruktur. Tahap pertama adalah studi literatur, yaitu pemetaan pemantauan tidur CSI, skrining tidur, dan privasi populasi rentan yang berujung pada penetapan metrik evaluasi. Tahap kedua adalah perancangan sistem, mencakup penempatan node di kamar, rencana kalibrasi, dan protokol izin berjenjang. Tahap ketiga adalah implementasi, yaitu pemasangan perangkat pada kamar kosong dan penghuni dewasa, uji Delta-CSI, lalu pengamatan malam berblok pada kamar siswa yang telah disetujui. Tahap terakhir adalah pengujian dan evaluasi, yaitu evaluasi status tidur, laju napas, dan anomali nocturnal, diakhiri rekomendasi parameter dari dewasa ke anak. Apabila dalam proses pengujian ditemukan kendala seperti alarm palsu malam berulang, maka dilakukan evaluasi dan perbaikan secara berulang hingga sistem dapat dievaluasi secara adil.

Penelitian ini adalah studi kelayakan kuantitatif dengan gerbang go/no-go pada minggu ketiga dan masa pengamatan malam berblok setelah gerbang lolos. Desain dibuat bertingkat dari yang paling tidak sensitif: uji sinyal pada kamar kosong terlebih dahulu, kemudian penghuni dewasa (peneliti) pada siang hari, dan hanya setelah semua aman, pengamatan malam pada kamar siswa yang telah mendapat persetujuan penuh. Setiap tingkat menghasilkan artefak tetap sehingga penelitian tetap bernilai sekalipun tidak mencapai tingkat terakhir.

## **3.2 Studi Literatur**

Studi literatur dilakukan terhadap tiga kelompok sumber, yaitu pemantauan tidur dan respirasi CSI, skrining tidur berbasis pembelajaran mesin, serta privasi dan etika sensing pada populasi rentan. Sumber diutamakan dari jurnal dan prosiding terindeks (IEEE, ACM, MDPI) pada rentang 2014 hingga 2025. Setiap referensi diverifikasi melalui API Crossref dengan mencocokkan judul, penulis, tahun, dan venue terhadap DOI terdaftar sehingga tidak ada referensi fiktif. Status kebaruan konteks asrama SLB diberi label terbatas-pencarian dan direncanakan diverifikasi ulang bersama pembimbing.

## **3.3 Perancangan Arsitektur Sistem**

Arsitektur sistem terdiri atas tiga lapisan. Lapisan sensing berisi dua node ESP32 (satu access point, satu station) yang dipasang mengapit area tempat tidur sehingga kanal sinyal memotong zona gerak penghuni. Lapisan pengolahan berisi server RuView pada single board computer yang menjalankan dekoding frame, kalibrasi ruangan, mesin status someone_sleeping, estimasi laju napas, dan anomali inaktivitas no_movement. Lapisan penyajian berisi dashboard dengan penanda skrining dan penerusan alert melalui MQTT ke perangkat pengasuh asrama. Seluruh keluaran berada pada tingkat kamar tanpa identifikasi individu.

## **3.4 Perancangan Perangkat Keras**

Perangkat keras utama adalah empat unit ESP32-S3 (dua terpasang, satu cadangan, satu pengembangan) dengan dudukan rak yang tidak mengganggu aktivitas kamar dan adaptor daya tetap karena klaim hemat daya low-power belum tervalidasi. Server pengolahan berjalan pada single board computer (Orange Pi atau Raspberry Pi) dengan penyimpanan terkontrol untuk rekaman malam berblok. Alat acuan laju napas (oksimeter pulsa atau strap) dipakai hanya pada sesi terjadwal sebagai pembanding, bukan bagian dari sistem operasional. Tidak ada kamera dan tidak ada mikrofon pada ruang tidur; seluruh sensing dilakukan sinyal Wi-Fi.

## **3.5 Perancangan Perangkat Lunak dan Dataset**

Perangkat lunak penelitian memakai alur bawaan RuView dengan penyesuaian dua parameter utama. Penyesuaian pertama adalah perilaku tepi band filter napas bawaan terhadap laju napas anak 18 hingga 25 napas per menit: perilaku diukur pada sesi acuan, dan bila estimasi terdistorsi, konstanta filter diubah secara terdokumentasi di firmware dan server, dengan laporan sebelum-sesudah. Penyesuaian kedua adalah ambang mesin status inaktivitas malam yang disetel ulang dari nilai dewasa dengan mengukur alarm palsu dan kehilangan deteksi per kombinasi ambang. Dataset disusun per blok malam dengan catatan pendamping sebagai ground truth status dan kejadian, dan evaluasi memakai split blok waktu dengan latih dan uji pada blok hari yang berbeda. Keluaran akhir berupa tabel parameter yang direkomendasikan untuk populasi anak.

## **3.6 Lokasi, Partisipan, dan Etika**

Lokasi adalah dua sampai tiga kamar asrama berpenghuni tunggal di 【Nama SLB】. Izin diambil berjenjang dan tertulis: persetujuan orang tua/wali setiap anak kamar partisipan, persetujuan kepala sekolah, kesepakatan pengasuh asrama, serta penjelasan kepada anak dengan bahasa yang sesuai kemampuannya. Hak menarik diri bersifat mutlak dan kapan pun tanpa konsekuensi. Sistem tidak merekam suara, tidak merekam gambar, tidak mengidentifikasi individu, dan mode privasi aktif sejak instalasi; seluruh data dianonimkan pada tingkat kamar dan disimpan pada penyimpanan terkontrol. Posisi sistem dinyatakan eksplisit sebagai deteksi kondisi untuk pendamping, bukan pengawasan perilaku anak.

## **3.7 Rencana Pengujian**

Rencana pengujian terdiri atas tiga kelompok. Pengujian pertama adalah uji Delta-CSI pada minggu pertama hingga ketiga dengan tiga skenario kamar kosong, penghuni terjaga bergerak, dan penghuni tidur, dibandingkan dengan noise floor, dimulai pada penghuni dewasa (peneliti) sebelum melibatkan siswa. Pengujian kedua adalah uji fungsi tidur: akurasi status tidur terhadap catatan pendamping per blok malam dan galat estimasi laju napas terhadap alat acuan pada sesi terjadwal, termasuk perilaku tepi band filter untuk anak. Pengujian ketiga adalah uji anomali: latensi deteksi inaktivitas nocturnal dan jumlah alarm palsu per kamar per minggu. Seluruh alert diaudit terhadap catatan pendamping sebelum masuk ke tabel hasil.

## **3.8 Evaluasi dan Kriteria Keberhasilan**

Metrik utama meliputi akurasi status tidur terhadap catatan pendamping per blok malam, galat estimasi laju napas terhadap alat acuan pada sesi terjadwal, latensi deteksi anomali inaktivitas, dan jumlah alarm palsu per kamar per minggu. Evaluasi juga mencatat beban operasional bagi pengasuh karena sistem yang menuntut perawatan tinggi tidak akan bertahan pada asrama nyata. Kriteria keberhasilan ditetapkan bersama pembimbing sebelum eksperimen dimulai.

Minggu ketiga menentukan lanjut atau pivot sebagai gerbang go/no-go. Bila status tidur dan napas tidak terbedakan dari derau, desain dipivot pada minggu yang sama: opsi meliputi penempatan ulang node, pengubahan geometri antena, atau penyempitan klaim menjadi karakterisasi sinyal malam. Bila kontras memadai, penelitian lanjut ke pengamatan malam pada kamar siswa yang telah mendapat persetujuan penuh, dengan penjajakan ulang persetujuan menjelang tahap tersebut.

## **3.9 Rencana Kegiatan dan Jadwal Penelitian**

Jadwal satu semester disusun dengan gerbang go/no-go pada minggu ketiga, sebagaimana Tabel 3.1. Persetujuan berjenjang sengaja ditempatkan paling awal karena menjadi prasyarat mutlak tahap pengamatan malam.

Tabel 3.1 Jadwal penelitian satu semester

| **Periode**  | **Aktivitas**                                                                                                                                                                                       | **Keluaran**                                                |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| Minggu 1-3   | Pengurusan izin berjenjang (orang tua, sekolah, pengasuh); pemasangan node pada kamar kosong; uji Delta-CSI tiga skenario dengan penghuni dewasa — GERBANG GO/NO-GO; kalibrasi 600 frame + 8 anchor | Keputusan go/no-go; kamar terkalibrasi; dokumen persetujuan |
| Minggu 4-7   | Pengamatan malam blok awal pada kamar partisipan; catatan pendamping; sesi acuan laju napas dengan oksimeter/strap                                                                                  | Dataset malam berblok + catatan kejadian                    |
| Minggu 8-11  | Evaluasi tepi band filter untuk anak; penyetelan ambang inaktivitas malam; evaluasi status tidur dan napas dengan split blok waktu                                                                  | Tabel parameter anak + metrik latensi/alarm palsu           |
| Minggu 12-15 | Audit alert bersama pengasuh; analisis hasil; penyetelan ulang ambang; penyusunan rekomendasi kalibrasi dan protokol izin                                                                               | Hasil evaluasi utuh + rekomendasi parameter                 |
| Minggu 16-18 | Penulisan naskah skripsi; finalisasi lampiran etik; persiapan sidang                                                                                                                                | Naskah skripsi siap sidang                                  |

## **3.10 Rencana Biaya Penelitian**

Tabel 3.2 merangkum rencana biaya dalam rupiah. Alat acuan laju napas dipakai hanya pada sesi terjadwal sebagai pembanding, bukan bagian dari sistem operasional.

Tabel 3.2 Rencana biaya penelitian

| **Komponen**                                                       | **Jumlah** | **Estimasi Biaya (Rp)** |
|--------------------------------------------------------------------|------------|-------------------------|
| ESP32-S3 (satu access point, satu station, plus dua cadangan)      | 4 unit     | 800.000                 |
| Single board computer (Orange Pi atau Raspberry Pi) + kartu memori | 1 set      | 750.000                 |
| Oksimeter pulsa / strap acuan laju napas                           | 1 unit     | 250.000                 |
| Bracket, kabel, adaptor, komponen kecil                            | 1 set      | 150.000                 |
| Operasional lokasi dan percetakan dokumen izin                     | —          | 100.000                 |
| Total                                                              | —          | 2.050.000               |

## **3.11 Analisis Risiko dan Rencana Cadangan**

Tabel 3.3 merangkum risiko utama. Risiko etis ditempatkan paling atas karena menjadi prasyarat mutlak seluruh tahap pengamatan malam.

Tabel 3.3 Risiko utama dan rencana cadangan

| **Risiko**                                         | **Dampak Bila Terjadi**                          | **Mitigasi / Fallback**                                                                                                                            |
|----------------------------------------------------|--------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Persetujuan orang tua atau wali tidak terkumpul    | Pengamatan malam pada siswa tidak dapat berjalan | Tahap penghuni dewasa tetap berjalan; hasil berupa karakterisasi sinyal malam dan protokol izin; pengajuan kembali dijeda sampai kesepakatan penuh |
| Dua anak tidur satu kamar (superposisi sinyal)     | Estimasi tidak valid                             | Asumsi keras satu penghuni per kamar; kamar partisipan dipilih yang berpenghuni tunggal                                                            |
| Alarm palsu malam berulang                         | Pengasuh mengabaikan alert                       | Penyetelan ambang per kamar; audit alert mingguan bersama pengasuh; definisi alarm palsu eksplisit                                                 |
| Tepi band filter napas mendistorsi laju napas anak | Estimasi napas bias                              | Evaluasi tepi band eksplisit; ubah konstanta filter secara terdokumentasi; laporkan sebelum-sesudah                                                       |
| Kontras Delta-CSI lemah malam hari                 | Sinyal tidak andal                               | Pivot penempatan node minggu 3; temuan tetap berupa karakterisasi sinyal kamar                                                                     |
| Salah pemahaman sebagai alat pengawas              | Kepercayaan wali turun                           | Framing skrining untuk pendamping pada semua dokumen; tanpa identifikasi individu; tata kelola data terbuka untuk wali                             |

# **DAFTAR PUSTAKA**

\[1\] Ma, Y., Zhou, G., & Wang, S. (2019). WiFi sensing with channel state information: A survey. ACM Computing Surveys, 52(3), 1–36. https://doi.org/10.1145/3310194

\[2\] Hernandez, S. M., & Bulut, E. (2020). Lightweight and standalone IoT based WiFi sensing for active repositioning and mobility. Proceedings of the IEEE International Conference on WoWMoM 2020. https://doi.org/10.1109/WoWMoM49955.2020.00056

\[3\] Liu, X., Cao, J., Tang, S., & Wen, J. (2014). Wi-Sleep: Contactless sleep monitoring via WiFi signals. Proceedings of the IEEE Real-Time Systems Symposium (RTSS). https://doi.org/10.1109/RTSS.2014.30

\[4\] Tataraidze, A., Olesyuk, R., & Pikhletsky, M. (2019). Can we monitor breathing during sleep via Wi-Fi on smartphone? Proceedings of the 41st Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC). https://doi.org/10.1109/EMBC.2019.8856382

\[5\] Burimas, R., Horanont, T., Thapa, A., & Lamichhane, B. R. (2024). Monitoring the sleep respiratory rate with low-cost microcontroller Wi-Fi in a controlled environment. Applied Sciences, 14(15), 6458. https://doi.org/10.3390/app14156458

\[6\] Kontou, P., Ben Smida, S., & Anagnostou, D. E. (2024). Contactless respiration monitoring using Wi-Fi and artificial neural network detection method. IEEE Journal of Biomedical and Health Informatics. https://doi.org/10.1109/JBHI.2023.3337001

\[7\] Chang, C.-C., Hsiao, A.-H., Shen, L.-H., Feng, K.-T., & Chen, C.-Y. (2023). Attention-based learning for sleep apnea and limb movement detection using Wi-Fi CSI signals. Proceedings of the IEEE 97th Vehicular Technology Conference (VTC2023-Spring). https://doi.org/10.1109/VTC2023-Spring57618.2023.10200274

\[8\] Pich, D., Baselizadeh, A., Torresen, J., & Miura, J. (2025). Privacy-preserving machine learning-based in-bed sleep posture monitoring using Wi-Fi signals. Proceedings of the 13th International Conference on Control, Mechatronics and Automation (ICCMA). https://doi.org/10.1109/ICCMA67641.2025.11369717

\[9\] Touhiduzzaman, M., Chung, J., Pretzer-Aboff, I., & Bulut, E. (2024). Wireless sensing-based daily activity tracking system deployment in low-income senior housing environments. Proceedings of the 30th Annual International Conference on Mobile Computing and Networking (MobiCom). https://doi.org/10.1145/3636534.3698115

\[10\] Mosharaf, M., Kwak, J. B., & Choi, W. (2024). WiFi-based human identification with machine learning: A comprehensive survey. Sensors, 24(19), 6413. https://doi.org/10.3390/s24196413
