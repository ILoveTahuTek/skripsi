Berikut isi lengkap laporan, ditempel langsung ke chat:

---

# Analisis Referensi dan Kritik Dewan LLM

**Evaluasi independen ide skripsi Wi-Fi CSI untuk unggas**
Objek: _Sistem Deteksi Anomali Perilaku Ayam Berbasis Wi-Fi CSI_ · Metode: riset literatur terverifikasi + LLM Council 5 advisor · 23 September 2026

---

## 1. Ringkasan Eksekutif

Laporan ini menyajikan evaluasi independen terhadap proposal skripsi berjudul **"Sistem Deteksi Anomali Perilaku Ayam Berbasis Wi-Fi Channel State Information (CSI) dengan ESP32 dan Edge Computing"**. Evaluasi dilakukan dalam dua tahap. Tahap pertama adalah riset literatur yang menghasilkan sepuluh referensi terverifikasi melalui 29 kueri pencarian dalam tiga bahasa, dengan setiap entri divalidasi silang melalui API Crossref dan OpenAlex hingga tingkat DOI. Tahap kedua adalah sidang kritik LLM Council yang mengadaptasi metodologi dewan model Andrej Karpathy: lima advisor independen dengan lensa berpikir berbeda, diikuti lima peer review anonim, dan disintesiskan oleh seorang chairman.

Temuan literatur paling penting bersifat positif: **dari seluruh pencarian, tidak ditemukan satu pun publikasi yang menggunakan Wi-Fi CSI pada ayam atau unggas di dunia.** Karya CSI pada ternak terdekat adalah pemantauan respirasi babi (Hao dkk. 2019; Lu dkk. 2019) dan klasifikasi perilaku estrus sapi perah (Hao dkk. 2020), sementara pemantauan ayam hingga kini didominasi akselerometer lekat dan kamera. Dengan demikian kebaruan pada level unggas dapat dipertahankan, tetapi klaim "pertama untuk hewan" tidak boleh digunakan karena babi dan sapi sudah mendahului.

Sebaliknya, dewan menemukan kelemahan struktural yang serius:

1. **Dilusi sinyal** — satu ayam sakit di kawanan 10–50 ekor hanya menyumbang ±2–10% gangguan total, kemungkinan tenggelam di noise floor ESP32.
2. **Metrik tak terdefinisi** — tanpa kelas positif (ayam sakit terverifikasi), target macro F1 > 0,80 dan FNR < 10% bukan sekadar ambisius, melainkan tak terdefinisi secara metodologis.
3. **Scope creep** — Fase 2 (CNN + TFLite + dashboard 100 pengguna) tidak realistis untuk satu mahasiswa dalam enam bulan.
4. **Judul menjanjikan lebih dari yang bisa dibuktikan.**

Rekomendasi utama dewan: reformulasi masalah menjadi **estimasi/deteksi perubahan aktivitas kawanan** (bukan deteksi penyakit), turunkan metrik ke dua jalur yang jujur, pangkas cakupan ±40%, dan ganti judul dengan salah satu dari tiga kandidat. Tindakan pertama yang dituntut dewan: **uji Delta-CSI fisik dengan dua ESP32 di kandang nyata minggu ini.**

## 2. Latar Belakang dan Tujuan Evaluasi

Proposal menawarkan solusi pemantauan kesehatan unggas tanpa kamera dan tanpa perangkat lekat bagi peternak rakyat Indonesia. Sistem memanfaatkan CSI dari sinyal Wi-Fi murah berbasis ESP32, memprosesnya di SBC sebagai edge gateway, dan mengirim peringatan otomatis via Telegram. Motivasinya kuat: wabah yang terdeteksi terlambat menimbulkan kerugian ekonomi signifikan, sementara solusi eksisting (computer vision, wearable) terlalu mahal untuk skala 10–50 ekor.

**Tabel 1. Ringkasan parameter proposal yang dievaluasi**

| Parameter       | Nilai dalam Proposal                                                                                |
| --------------- | --------------------------------------------------------------------------------------------------- |
| Judul asli      | Sistem Deteksi Anomali Perilaku Ayam Berbasis Wi-Fi CSI dengan ESP32 dan Edge Computing             |
| Target pengguna | Peternak rakyat Indonesia, 10–50 ekor; anggaran < Rp2 juta                                          |
| Perangkat keras | 4–6 ESP32 (1 AP + 3–5 STA); SBC H96 Max X3; DHT22 opsional; ESP-CAM untuk ground truth              |
| Perangkat lunak | ESP32-CSI-Tool + MQTT; filter Butterworth + fitur statistik/temporal/frekuensi/spasial; window 60 s |
| Algoritma       | Fase 1: z-score adaptif; Fase 2: SVM RBF atau CNN ringan + TFLite 8-bit                             |
| Target metrik   | Macro F1 > 0,80; FPR < 5%; FNR < 10%; latensi < 3 menit; uptime > 95%                               |
| Klaim kebaruan  | Penelitian pertama Wi-Fi CSI untuk deteksi perilaku unggas di Indonesia                             |
| Fallback        | Pivot ke DHT22 + PIR + kamera jika SNR < 15 dB setelah pre-eksperimen 2 minggu                      |

## 3. Metodologi Evaluasi

Tahap riset literatur memakai 29 kueri web (Inggris, Mandarin, Indonesia) yang mencakup empat klaster: sensing Wi-Fi CSI pada manusia; CSI pada ternak (babi, sapi, hewan peliharaan); pemantauan perilaku unggas moda lain (akselerometer, kamera, suara); serta tooling ESP32 dan TinyML. Kandidat disaring ketat: hanya publikasi terkonfirmasi via venue atau basis data akademik, lalu diverifikasi silang Crossref/OpenAlex hingga DOI. Hasilnya sepuluh referensi dari sembilan venue, rentang 2019–2024: satu survei kanonik, satu paper tooling ESP32, tiga paper CSI ternak, empat paper pemantauan unggas/peringatan dini, satu paper TinyML.

Tahap kritik memakai LLM Council ala Karpathy. Lima advisor paralel independen: **The Contrarian** (mencari kelemahan fatal), **The First Principles Thinker** (membedah rantai kausal), **The Expansionist** (mencari nilai tersembunyi), **The Outsider** (membaca sebagai awam), **The Executor** (menguji kelayakan mingguan). Kelima respons dianonimkan menjadi Respons A–E, lalu ditinjau silang oleh lima reviewer independen. Peer review anonim menangkap enam blind spot tambahan yang tidak dimiliki advisor mana pun (mis. pseudoreplikasi dan konfound siklus hidup broiler). Chairman menyintesiskan semuanya menjadi satu verdict.

## 4. Sepuluh Referensi Terverifikasi

**Tabel 2. Sepuluh referensi terverifikasi beserta posisi kebaruannya** _(kelompok: No 1–2 fondasi sensing Wi-Fi & tooling ESP32; No 3–5 CSI pada ternak; No 6–10 pemantauan unggas & TinyML)_

| No  | Penulis & Tahun                                                       | Judul Penelitian / Objek                                                                                                                   | Metode yang Digunakan                                                                                                                                                        | Kebaruan / Posisi Penelitian Ini                                                                                                                                                                                                         |
| --- | --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | Ma, Zhou & Wang (2019), _ACM Computing Surveys_ 52(3)                 | WiFi Sensing with Channel State Information: A Survey — objek: manusia (survei)                                                            | Taksonomi sensing Wi-Fi berbasis CSI (amplitudo-fase subcarrier, model Fresnel, Doppler); aplikasi HAR, deteksi jatuh, respirasi, lokalisasi; pemrosesan sinyal menuju ML/DL | Survei kanonik rujukan hampir semua karya CSI; literatur CSI klasik berfokus manusia → mendukung kebaruan skripsi di level unggas; landasan teori bab tinjauan pustaka                                                                   |
| 2   | Hernandez & Bulut (2020), _IEEE WoWMoM_                               | Lightweight and Standalone IoT Based WiFi Sensing for Active Repositioning and Mobility — objek: manusia dengan ESP32                      | CSI diambil langsung di MCU ESP32 tanpa PC; pipeline standalone deteksi reposisi & mobilitas; tim pengembang ESP32-CSI-Tool standar riset saat ini                           | Membuktikan sensing CSI bisa berjalan penuh di MCU murah — preseden teknis langsung bagi node ESP32 skripsi; skripsi berdiri di infrastruktur sama, menambah objek unggas, deteksi level kawanan, dan jalur alarm                        |
| 3   | Hao, Li, Wang & Lin (2019), _ACM ICIT_                                | An Animal Respiration Monitoring System Based on CSI of Wi-Fi Network — objek: babi                                                        | CSI Wi-Fi komersial; filter subcarrier abnormal, smoothing, indeks periodisitas, autokorelasi laju respirasi; window 30 s; akurasi 99,87%                                    | Bukti awal CSI mengikuti ritme fisiologi hewan (babi, bukan manusia); belum menyentuh unggas & belum klasifikasi perilaku — skripsi memperluas sensing dari mamalia ternak ke ayam                                                       |
| 4   | Lu, Li, Hao & Lin (2019), _TCSAE_ 35(24)                              | Monitoring pig respiration frequency using Wi-Fi wireless sensing — objek: babi                                                            | Sensing Wi-Fi non-kontak di kandang babi nyata; ekstraksi komponen gerak untuk estimasi frekuensi napas tanpa sensor lekat                                                   | Kelayakan Wi-Fi sensing non-kontak untuk kesehatan ternak skala 1 ekor/kandang; gangguan napas juga gejala utama unggas, namun objek belum ayam — memperkuat celah yang diklaim skripsi                                                  |
| 5   | Hao, Lin, Wang, Guo & Lu (2020), _TCSAE_ 36(19)                       | Recognition of mounting behavior of dairy cows based on Wi-Fi wireless sensing — objek: sapi perah                                         | Deteksi & klasifikasi perilaku naik (estrus) dari sinyal Wi-Fi di kandang alami; 2.497 sampel uji; tanpa perangkat lekat                                                     | Perluasan CSI ke klasifikasi perilaku ternak — karya terdekat dengan tujuan skripsi; mamalia besar 1–2 hewan/area; skripsi mengklaim transfer ke unggas kecil dalam kawanan banyak, lompatan yang harus diuji kelayakannya               |
| 6   | Yang, Zhao, Street, Huang, Filip To & Purswell (2021), _Animal_ 15(7) | Classification of broiler behaviours using triaxial accelerometer and ML — objek: broiler                                                  | Akselerometer triaksial lekat; klasifikasi makan, minum, berjalan, berbaring dengan KNN & jaringan saraf; data terlabeli manual                                              | Standar emas identifikasi perilaku ayam: akurat tetapi 1 sensor/ekor (mahal utk 10–50 ekor, menambah stres) — pembanding yang memotivasi pendekatan device-free CSI                                                                      |
| 7   | Campbell dkk. (2024), _Computers and Electronics in Agriculture_      | A computer vision approach to monitor activity in commercial broiler chickens using trajectory-based clustering — objek: broiler komersial | Kamera 2D + detektor ayam CNN + pelacakan multi-objek (MOTA 74,7%) + klasterisasi trajektori; memantau perubahan aktivitas jangka pendek                                     | Moda dominan pemantauan unggas = kamera (butuh pencahayaan, rentan oklusi & debu) — skripsi memposisikan CSI sebagai alternatif murah & privat; sekaligus membuktikan perubahan aktivitas jangka pendek valid sebagai fitur deteksi dini |
| 8   | Okinda dkk. (2019), _Biosystems Engineering_ 188                      | A machine vision system for early detection and prediction of sick birds: A broiler chicken model — objek: broiler sakit                   | Kamera (termasuk depth camera) + ciri perilaku & postur individu untuk klasifikasi & prediksi dini status sakit; video untuk pelabelan ground truth                          | Bukti langsung bahwa perubahan perilaku mendahului penyakit unggas — inti hipotesis skripsi valid; modalitasnya kamera sehingga kebaruan skripsi tetap pada moda Wi-Fi CSI                                                               |
| 9   | He, Chen, Yu, Hayat, He, Pan & Lin (2022), _Applied Sciences_ 12(11)  | Research Progress in the Early Warning of Chicken Diseases by Monitoring Clinical Symptoms — objek: unggas (review)                        | Review sistematis gejala klinis yang dapat dipantau otomatis: vokalisasi, suhu, feses, perilaku harian; dipetakan ke teknologi sensor & AI peringatan dini                   | Memetakan seluruh moda peringatan dini penyakit ayam dan **tidak memuat satu pun moda Wi-Fi CSI** — celah eksplisit yang diisi skripsi; sekaligus sumber daftar gejala & label penyakit untuk desain eksperimen                          |
| 10  | Antonini, Pincheira, Vecchio & Antonelli (2023), _Sensors_ 23(4)      | An Adaptable and Unsupervised TinyML Anomaly Detection System for Extreme Industrial Environments — objek: data IoT perangkat terbatas     | Deteksi anomali unsupervised berbasis TinyML di MCU kelas Cortex-M; pipeline end-to-end IoT-edge adaptif tanpa data terlabeli                                                | Preseden deteksi anomali on-device tanpa label di mikrokontroler — mendukung arsitektur skripsi (ambang → SVM/CNN di SBC + alarm Telegram) & menyediakan jalur algoritma bila data terlabeli sulit                                       |

**Tabel 3. Daftar DOI sepuluh referensi**

| No  | DOI / URL                                             |
| --- | ----------------------------------------------------- |
| 1   | https://doi.org/10.1145/3310194                       |
| 2   | https://doi.org/10.1109/WoWMoM49955.2020.00056        |
| 3   | https://doi.org/10.1145/3377170.3377196               |
| 4   | https://doi.org/10.11975/j.issn.1002-6819.2019.24.022 |
| 5   | https://doi.org/10.11975/j.issn.1002-6819.2020.19.019 |
| 6   | https://doi.org/10.1016/j.animal.2021.100269          |
| 7   | https://doi.org/10.1016/j.compag.2023.108591          |
| 8   | https://doi.org/10.1016/j.biosystemseng.2019.09.015   |
| 9   | https://doi.org/10.3390/app12115601                   |
| 10  | https://doi.org/10.3390/s23042344                     |

## 5. Analisis Posisi dan Celah Penelitian

Sensing Wi-Fi CSI adalah teknologi dewasa pada manusia. Pada ternak, CSI terbukti mengukur respirasi babi (akurasi 99,87% di kandang nyata) bahkan mengklasifikasi perilaku estrus sapi perah (2.497 sampel). Namun semua karya ternak memakai 1–2 hewan besar per area, dan perangkat CSI di literatur adalah Intel 5300/Atheros — bukan ESP32 satu antena. Pada unggas: **nol publikasi Wi-Fi CSI**, termasuk dalam review sistematis He dkk. (2022).

**Dua klaim kebaruan dengan kelas berbeda:**

- ✅ **Dapat dipertahankan:** penelitian pertama Wi-Fi CSI pada unggas (kawanan ayam), di Indonesia maupun literatur dunia.
- ❌ **Harus digugurkan:** "pertama untuk hewan" (dipatahkan babi & sapi) dan "pertama di Indonesia" sebagai kebaruan utama (kebaruan geografis lemah di mata penguji). Kebaruan metodologis yang lebih kuat: sensing kolektif device-free pada kawanan kecil yang banyak anggotanya — belum dipetakan siapa pun.

**Lima kelemahan yang harus dijawab sebelum sidang:**

1. **Dilusi sinyal pada kawanan** — satu ayam sakit di kawanan 30 ekor = 3% populasi; literatur sukses pada satu hewan besar yang mendominasi modulasi jalur.
2. **Fisika sinyal lebih lemah** — Doppler skala massa tubuh: broiler 2 kg menghasilkan gangguan puluhan kali lebih lemah daripada babi 80 kg; ESP32 satu antena dengan derau fase tinggi berada di bawah Intel 5300.
3. **Ground truth wajib moda lain** — CSI tak bisa membedakan ayam mana yang bergerak; pelabelan butuh sinkronisasi kamera → membalik klaim tanpa-kamera (kamera tetap dibutuhkan saat training).
4. **Sensitivitas lingkungan** — posisi pakan, kelembapan litter, orang lewat, jadwal harian mengubah CSI jauh lebih kuat daripada penyakit satu ekor → rentan alarm palsu.
5. **Tidak ada dataset publik** — tahap SVM/CNN menuntut pengumpulan dataset mandiri dari nol.

## 6. Hasil Kritik Dewan LLM

### 6.1 Titik Kesepakatan (konsensus 5 advisor)

1. **Klaim deteksi dini penyakit harus keluar dari judul & tujuan** — rantai kausal putus di fisika (Doppler skala massa; satu ayam sakit 2–10% gangguan kawanan) dan di label (tidak ada kelas positif).
2. **Metrik saat ini fiktif** — tanpa kelas positif, macro F1 > 0,80 & FNR < 10% tak terdefinisi; 20–30 sampel event membuat macro F1 tidak stabil.
3. **Unit analisis adalah kawanan** — kata _flock-level_ wajib masuk judul dan desain eksperimen.
4. **Edge Computing keluar dari judul; CNN+TFLite dipangkas** — SVM RBF/z-score di laptop cukup untuk skripsi; edge adalah bonus, bukan janji terukur.
5. **Klaim "pertama di Indonesia" gugur sebagai kebaruan utama** — ganti dengan kebaruan metodologis sensing kolektif device-free pada unggas.
6. **Fallback DHT22+PIR+kamera = skripsi kedua, bukan fallback** — fallback sejati adalah mengecilkan klaim, bukan mengganti teknologi di bulan keempat.
7. **Go/no-go dini wajib** — uji kelayakan minggu kedua, bukan bulan kedua; memakai ayam sungguhan, bukan proxy manusia lewat.
8. **Respons Expansionist adalah outlier** — strategi tiga publikasi dibangun di atas eksperimen yang belum terbukti layak; seluruh reviewer menolaknya sebagai arah utama.

### 6.2 Perbedaan Pandangan Dewan

- **Nasib kata "deteksi anomali":** First Principles menggugurkannya total (ganti estimasi kontinyu indeks aktivitas); Executor & Contrarian ingin mempertahankan deteksi anomali kawanan dengan metrik diturunkan. Jalan tengah reviewer: pertahankan alarm tanpa label, evaluasi dengan **control chart pada indeks aktivitas + precision@k berbasis audit kamera retrospektif**.
- **Nilai aset dataset:** Expansionist menilai dataset CSI ayam pertama di dunia sebagai kemenangan sesungguhnya; reviewer membalas dataset tanpa kelas positif hanyalah rekaman perilaku normal. Resolusi: dataset bernilai setelah label proxy etis ditempelkan, dirilis dengan DOI sebagai kontribusi sekunder.
- **Skala kawanan:** 10–15 ekor (Executor) vs 5–10 ekor terkontrol (Contrarian) — tidak fatal, karena yang menentukan adalah hasil uji Delta-CSI minggu pertama.

### 6.3 Blind Spot yang Terungkap dari Peer Review

1. **Uji kelayakan fisik termurah terlewat** — ukur Delta-CSI aktual satu ayam vs kawanan bergerak di kandang target _sebelum_ memilih arsitektur, metrik, dan judul.
2. **Pseudoreplikasi & kebocoran temporal** — satu kandang satu kawanan = satu unit eksperimen (n=1); split acak pada time-series membocorkan data → wajib split blok-waktu dengan validasi antar-hari.
3. **Konfound siklus hidup broiler** — bobot tumbuh 40 g → 2 kg dalam 35–42 hari menggeser baseline CSI sendiri; z-score adaptif akan salah alarm; usia awal ayam tidak dibahas proposal.
4. **Konfounder terjadwal & lingkungan** — jadwal pakan, panen, cahaya, suhu menggerakkan aktivitas kawanan jauh lebih kuat daripada penyakit; butuh log kejadian harian sebagai kovariat dan definisi FPR = alarm palsu per 24 jam.
5. **Rekayasa RF belum dirancang** — geometri antena harus memotong zona Fresnel area kawanan (TX-RX mengapit kandang); CSI ESP32 praktis amplitudo-only (fase berderau) → membatasi pilihan fitur; amonia & kelembapan mengorosi konektor → housing, pigtail, grounding wajib direncanakan.
6. **Etika & sumber kelas positif** — perlu persetujuan kesejahteraan hewan; jalur label positif: kerja sama puskeswan/fakultas kedokteran hewan (morbiditas alami) atau event proxy etis berlabel (vaksinasi, heat stress, pembatasan pakan).

### 6.4 Rekomendasi Dewan

Verdict tegas: **ide versi asli tidak defensibel di sidang, tetapi versi reformulasi layak sebagai skripsi enam bulan satu orang.** Rumusan masalah operasional yang harus berani ditulis di abstrak:

> _"Sistem memantau tingkat aktivitas kolektif kawanan ayam melalui Wi-Fi CSI pada ESP32; bila menyimpang dari pola baseline hari-hari sebelumnya, sistem mengirim peringatan ke Telegram; sistem tidak mengidentifikasi ayam mana yang sakit."_

Lima blok rekomendasi:

1. **Ganti judul** dengan salah satu dari tiga kandidat (Bagian 7).
2. **Ganti metrik menjadi dua jalur.** Jalur utama (tanpa kelas positif): control chart pada indeks aktivitas + precision@k berbasis audit kamera retrospektif; FPR = alarm palsu per 24 jam, target ≤ 1/hari, precision@k ≥ 0,5. Jalur sekunder (bila event proxy berlabel didapat): F1 > 0,70 dan FPR < 10% level kawanan. Macro F1 > 0,80 hanya bermakna dengan ≥ 50 event anomali — hampir pasti tak tercapai, jangan dijanjikan.
3. **Pangkas cakupan ±40%:** 3 ESP32 (1 AP + 2 STA) mengapit kandang; fitur amplitudo-only; window 60 s; z-score adaptif + satu SVM RBF di laptop; TFLite → future work; **H96 Max diganti Orange Pi / Raspberry Pi** (H96 Max = perangkat Android TV, dukungan Linux & termal buruk).
4. **Kontrol metodologis:** split blok-waktu; log kejadian harian (pakan, cahaya, suhu, panen) sebagai kovariat; catat usia awal ayam; persetujuan etik formal sebelum pengambilan data; kontak puskeswan sejak awal.
5. **Kontribusi jujur:** studi kelayakan pertama CSI kawanan unggas pada MCU murah; dataset + rekaman kamera + label proxy dirilis di Zenodo dengan DOI; protokol & log kejadian terdokumentasi terbuka.

### 6.5 Satu Langkah Pertama

> Minggu ini, jalankan **uji Delta-CSI fisik**: dua ESP32 TX-RX mengapit kandang kecil berisi 10–15 broiler, rekam amplitudo CSI window 60 s untuk tiga skenario — kandang kosong, satu ayam bergerak, kawanan penuh bergerak — bandingkan terhadap noise floor. Jika aktivitas kawanan penuh tak terlihat dari derau, seluruh desain (judul, metrik, arsitektur) harus dipivot sebelum satu baris pipeline ditulis. Jika terlihat jelas, lanjutkan rekomendasi di atas dengan percaya diri. **Beli ESP32-nya hari Senin.**

## 7. Kritik Judul dan Saran Perbaikan

Judul asli mengandung tiga masalah struktural: (1) frasa _deteksi anomali_ menjanjikan klasifikasi padahal tak ada contoh anomali terverifikasi; (2) frasa _Edge Computing_ tak terikat evaluasi terukur mana pun — buzzword yang mengundang pertanyaan penguji; (3) tak ada penanda unit analisis (per ekor vs kawanan). Ujian sederhana: tulis satu kalimat polos yang menjelaskan apa yang dilakukan sistem (rumusan 6.4); frasa judul yang tidak didukung kalimat itu = janji berlebih, harus keluar.

**Tabel 4. Perbandingan tiga kandidat judul pengganti**

| Kandidat      | Rumusan Judul                                                                                                             | Kekuatan                                                                                                                                             | Risiko                                                                                                         |
| ------------- | ------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| **Opsi 1** ⭐ | Estimasi Indeks Aktivitas Kawanan Broiler Berbasis Wi-Fi CSI pada ESP32: Studi Kelayakan Pemantauan Dini Kesehatan Unggas | Paling ilmiah & defensibel; klaim persis sama dengan yang dapat dibuktikan; hubungan ke penyakit jadi motivasi, bukan beban pembuktian               | Terminologi "indeks aktivitas" perlu definisi formal di bab metode; terdengar kurang aplikatif bagi non-teknis |
| **Opsi 2**    | Deteksi Perubahan Aktivitas Kawanan Ayam Berbasis Wi-Fi CSI untuk Sistem Peringatan Dini di Peternakan Rakyat             | Paling aplikatif; mempertahankan janji peringatan dini; kata "perubahan" lebih jujur daripada "anomali"; konteks peternakan rakyat eksplisit         | Perlu metrik alarm jujur (control chart, precision@k) agar tak overclaim; harus menegaskan level kawanan       |
| **Opsi 3**    | Sistem Monitoring Perilaku Kawanan Unggas Device-Free Berbasis Wi-Fi CSI pada ESP32 dengan Dataset Publik                 | Paling kuat untuk publikasi; dua kontribusi konkret (sistem + dataset CSI unggas pertama dengan DOI); kata "monitoring" tak menuntut bukti veteriner | Risiko mengulang pola judul panjang penuh janji; dataset hanya bernilai setelah label proxy etis ditempelkan   |

**Rekomendasi final: Opsi 1** untuk keamanan akademik maksimal — setiap kata dapat dipetakan ke hasil yang terbukti dalam enam bulan, dan kata _studi kelayakan_ memberi ruang keluar elegan jika sinyal ternyata lemah. Opsi 2 jika pembimbing menuntut orientasi aplikasi; Opsi 3 hanya setelah jalur label proxy etis pasti berjalan.

## 8. Kesimpulan dan Tindak Lanjut

Dari sisi kebaruan, ide berdiri di atas celah literatur yang nyata: tidak ada publikasi Wi-Fi CSI pada unggas di dunia, dan sensing kolektif device-free pada kawanan kecil adalah kontribusi metodologis yang sah. Dari sisi kelayakan, proposal bentuk sekarang tidak defensibel karena tiga beban struktural: janji deteksi dini penyakit tanpa kelas positif, metrik tak terdefinisi, dan cakupan melebihi kapasitas satu orang enam bulan. Ketiganya dapat diperbaiki tanpa membuang inti ide.

Urutan tindak lanjut:

1. **Senin ini:** beli dua ESP32 (±Rp500 ribu), pasang ESP32-CSI-Tool, jalankan uji Delta-CSI tiga skenario di kandang nyata.
2. **Minggu kedua:** keputusan go/no-go; jika SNR & kontras memadai, kunci arsitektur tiga node; jika tidak, pivot sebelum pipeline dibangun.
3. Ganti SBC H96 Max → Orange Pi/Raspberry Pi; Fase 2 jadi satu SVM di laptop; CNN/TFLite → future work.
4. Hubungi puskeswan/fakultas kedokteran hewan untuk jalur label positif; siapkan persetujuan kesejahteraan hewan.
5. Revisi proposal: judul Opsi 1, metrik dua jalur, split blok-waktu, log kejadian harian, catat usia awal ayam.
6. Setelah eksperimen jalan: rilis dataset di Zenodo dengan DOI sebagai kontribusi sekunder.

## 9. Daftar Referensi

1. Ma, Y., Zhou, G., & Wang, S. (2019). WiFi sensing with channel state information: A survey. _ACM Computing Surveys, 52_(3), 1–36. https://doi.org/10.1145/3310194
2. Hernandez, S. M., & Bulut, E. (2020). Lightweight and standalone IoT based WiFi sensing for active repositioning and mobility. _Proc. IEEE WoWMoM 2020_. https://doi.org/10.1109/WoWMoM49955.2020.00056
3. Hao, Q., Li, K., Wang, Z., & Lin, F. (2019). An animal respiration monitoring system based on channel state information of Wi-Fi network. _Proc. ACM ICIT 2019_, 283–289. https://doi.org/10.1145/3377170.3377196
4. Lu, M., Li, K., Hao, Q., & Lin, F. (2019). Monitoring pig respiration frequency using Wi-Fi wireless sensing technology. _Transactions of the CSAE, 35_(24), 183–190. https://doi.org/10.11975/j.issn.1002-6819.2019.24.022
5. Hao, Q., Lin, F., Wang, Z., Guo, X., & Lu, M. (2020). Recognition of mounting behavior of dairy cows based on Wi-Fi wireless sensing. _Transactions of the CSAE, 36_(19), 168–176. https://doi.org/10.11975/j.issn.1002-6819.2020.19.019
6. Yang, X., Zhao, Y., Street, G. M., Huang, Y., Filip To, S. D., & Purswell, J. L. (2021). Classification of broiler behaviours using triaxial accelerometer and machine learning. _Animal, 15_(7), 100269. https://doi.org/10.1016/j.animal.2021.100269
7. Campbell, J., Miller, L., Diaz-Chito, K., Hong, J., McLaughlin, N., Parvinzamir, S., Martinez Del Rincon, J., & O'Connell, N. (2024). A computer vision approach to monitor activity in commercial broiler chickens using trajectory-based clustering analysis. _Computers and Electronics in Agriculture_. https://doi.org/10.1016/j.compag.2023.108591
8. Okinda, C., Lu, M., Liu, L., Nyalala, I., Muneri, C., Wang, C., Zhang, M., & Shen, M. (2019). A machine vision system for early detection and prediction of sick birds: A broiler chicken model. _Biosystems Engineering, 188_, 229–242. https://doi.org/10.1016/j.biosystemseng.2019.09.015
9. He, G., Chen, S., Yu, X., Hayat, M. M., He, J., Pan, J., & Lin, H. (2022). Research progress in the early warning of chicken diseases by monitoring clinical symptoms. _Applied Sciences, 12_(11), 5601. https://doi.org/10.3390/app12115601
10. Antonini, M., Pincheira, M., Vecchio, M., & Antonelli, F. (2023). An adaptable and unsupervised TinyML anomaly detection system for extreme industrial environments. _Sensors, 23_(4), 2344. https://doi.org/10.3390/s23042344

---

That is the complete content of the 16-page report. Which section would you like to deepen — for example, turn the Delta-CSI test protocol into a step-by-step guide, or discuss one of the title options with your supervisor?
