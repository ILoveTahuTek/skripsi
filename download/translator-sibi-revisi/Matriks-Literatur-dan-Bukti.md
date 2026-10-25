# Matriks Literatur dan Bukti — Purwarupa Penerjemah Dua Arah SIBI Berbasis Wi-Fi CSI

Dokumen ini merangkum bukti yang menopang proposal revisi (`Proposal-Revisi-Translator-SIBI.md`): setiap rujukan, klaim yang dipakainya, status verifikasi, dan perannya di naskah. Daftar pustaka lengkap berformat APA tercantum pada proposal revisi; matriks ini memakai rujukan ringkas.

## 1. Metodologi penelusuran

Penelusuran dilakukan berlapis pada dua periode. Periode pertama (sesi sebelumnya, terarsip pada `verifikasi-rujukan-2026-10-24/`) menghimpun 22 rujukan penginderaan isyarat CSI dan 40 rujukan konteks melalui Google Scholar, Crossref, dan OpenAlex dengan kata kunci Inggris ("Wi-Fi sensing", "channel state information", "sign language recognition", "gesture recognition") dan Indonesia ("SIBI", "BISINDO", "pengenalan isyarat", "bahasa isyarat", "penerjemah bahasa isyarat"). Periode kedua (25 Oktober 2026) menambah penelusuran khusus teknologi baru visi produk: ("TTS Indonesian", "ASR Indonesian WER", "Kokoro languages", "MMS TTS", "faster-whisper benchmark", "keystroke CSI", "respiration CSI", "continuous sign language CSI", "text to sign language Indonesia", "SIBI inflectional"). Kriteria inklusi: makalah terindeks ber-DOI yang terverifikasi melalui Crossref, dokumentasi resmi vendor, model card resmi, dataset publik, atau kode sumber repositori resmi yang diinspeksi langsung. Kriteria eksklusi: tulisan blog pihak ketiga untuk klaim teknis (kecuali sebagai petunjuk penemuan yang kemudian diverifikasi ke sumber primer), klaim tanpa sumber yang dapat diinspeksi, dan angka harga yang tidak terbaca langsung dari halaman resmi.

## 2. Cara membaca status bukti

Setiap klaim diberi salah satu label berikut. **DIVERIFIKASI**: sumber dilihat langsung (halaman resmi dibuka, PDF diunduh, kode sumber dibaca, atau metadata DOI dikonfirmasi melalui Crossref) pada 24-25 Oktober 2026. **CUPILIKAN**: hanya potongan hasil penelusuran yang terbaca, sumber primer belum diinspeksi penuh. **TIDAK DITEMUKAN**: dicari dengan jujur pada sumber yang diakses tetapi tidak ditemukan; klaim terkait tidak boleh masuk naskah. **ESTIMASI**: hitungan penulis dari angka terverifikasi, bukan klaim sumber, dan selalu ditandai sebagai demikian. Pemisahan jenis pernyataan: *fakta* bersumber dan berlabel, *hipotesis* ditandai kata duga/periwayatan akan-diuji, *keputusan desain* dijelaskan alasannya pada dokumen audit, dan *belum diketahui* ditandai penanda `[PERLU DATA: ...]` atau `[PERLU RUJUKAN: ...]` di naskah.

## 3. Matriks rujukan per kelompok

### Kelompok A — Konteks tunarungu, SIBI, dan bahasa isyarat Indonesia

| Kunci | Rujukan ringkas | Klaim yang dipakai proposal | Status | Bab |
|---|---|---|---|---|
| mitchell2004, mitchell2005 | Mitchell & Karchmer, Sign Language Studies 2004/2005 | 90-95% anak tunarungu lahir dari orang tua pendengar (AS) | DIVERIFIKASI | 1.1 |
| lieberman2022 | Lieberman dkk., Appl. Linguistics Review 2022 | Orang tua pendengar belajar isyarat butuh dukungan terstruktur | DIVERIFIKASI | 1.1 |
| ritmeester2025 | Ritmeester dkk., J. Deaf Stud. Deaf Educ. 2025 | Hambatan praktis orang tua pendengar mempelajari isyarat | DIVERIFIKASI | 1.1 |
| kemenkopmk2025 | Kemenko PMK, situs resmi 2025 | Sekitar 500 juru bahasa isyarat untuk sekitar 1,92 juta tunarungu | DIVERIFIKASI | 1.1 |
| uu8_2016 | UU No. 8/2016 | Pengakuan bahasa isyarat dan kewajiban aksesibilitas | DIVERIFIKASI | 1.1, 2.1 |
| brin2026 | BRIN, siaran pers 2026 | BISINDO 77,7%, SIBI 1,9% (survei daring purposive 26 provinsi) | DIVERIFIKASI | 1.1, 2.1 |
| kamussibi2020 | Kamus SIBI Digital, Kemendikdasmen | Acuan bentuk baku; SK 0190/P/1994; Surat 868/C/U/95 | DIVERIFIKASI | 1.1, 2.1 |
| kamussibi1994 | Depdikbud, Kamus SIBI 1994 | Dokumen baku bentuk isyarat SIBI | DIVERIFIKASI (keberadaan entri pustaka) | 2.1, 3.6 |
| satillah2024 | As Satillah dkk., AUDHI 2024 | SIBI dominan dalam pembelajaran di SLB N Ogan Ilir | DIVERIFIKASI | 1.1, 2.1 |
| mursita2015 | Mursita, INKLUSI 2015 (DOI 10.14421/ijds.2202) | 91% dari 100 responden tunarungu memakai BISINDO sehari-hari | DIVERIFIKASI (baru) | 2.1 |
| nugraheni2023, malika2025 | Nugraheni dkk. 2023; Malika & Berlianti 2025 | Perbedaan pemakaian SIBI/BISINDO di kampus dan SLB | DIVERIFIKASI | 2.1 |
| rodriguez2023 | Rodríguez-Correa dkk., Frontiers in Education 2023 | Tinjauan sistematis teknologi bantu komunikasi tunarungu | DIVERIFIKASI | 2.2 |
| stokoe2005 | Stokoe (cetak ulang 1960) | Isyarat tersusun parameter: bentuk tangan, lokasi, gerak, orientasi, non-manual | DIVERIFIKASI | 2.1 |
| ong2005 | Ong & Ranganath, TPAMI 2005 | Survei pengenalan isyarat bersensor dan berbasis visi | DIVERIFIKASI | 2.2 |

### Kelompok B — Pengenalan isyarat dari Wi-Fi CSI

| Kunci | Rujukan ringkas | Klaim yang dipakai proposal | Status | Bab |
|---|---|---|---|---|
| ma2018 | Ma dkk., IMWUT 2018 (SignFi) | 276 isyarat ASL dari CSI Intel 5300 3 antena; dalam sesi 98,01% (lab), 98,91% (rumah), 94,81% (campuran) | DIVERIFIKASI | 1.1, 2.3, 2.6, 2.11 |
| shang2017 | Shang & Wu, MobiArch 2017 | Sistem pengenalan isyarat tangguh dengan banyak perangkat Wi-Fi | DIVERIFIKASI | 2.6, 2.11 |
| ahmed2020 | Ahmed dkk., PMC 2020 (DF-WiSLR) | Pengenalan 49 gestur tanpa perangkat dikenakan | DIVERIFIKASI | 2.6, 2.11 |
| ahmed2021 | Ahmed dkk., IAICT 2021 | Model LSTM untuk isyarat dari CSI | DIVERIFIKASI | 2.6, 2.11 |
| qin2023 | Qin dkk., Measurement 2023 (WiASL) | Pengenalan tulisan ASL dengan perangkat Wi-Fi komersial | DIVERIFIKASI | 2.6, 2.11 |
| baldeo2024 | Baldeo dkk., TENCON 2024 | Pengenalan Filipino Sign Language dari CSI | DIVERIFIKASI | 2.6, 2.11 |
| hao2020 | Hao dkk., Sensors 2020 (Wi-SL) | Gestur halus dari CSI; perangkat 2TX-3RX 40 MHz 400 Hz | DIVERIFIKASI | 2.3, 2.6 |
| sruthi2024 | Sruthi dkk., Procedia CS 2024 (HandFi) | Gestur tangan dari CSI (Intel 5300 + router komersial) | DIVERIFIKASI | 2.3, 2.6 |
| wisign2020 | Zhang, Zhang & Zheng, ACM TIST 11(3) 2020 (DOI 10.1145/3377553) | Pengenalan kalimat ASL kontinu dari CSI komersial dengan segmentasi PSD; batas kebaruan kontinu | DIVERIFIKASI (baru) | 2.6, 2.11 |

### Kelompok C — Sensitivitas gerak halus dan generalisasi lintas domain

| Kunci | Rujukan ringkas | Klaim yang dipakai proposal | Status | Bab |
|---|---|---|---|---|
| wikey2015 | Ali dkk., MobiCom 2015 (DOI 10.1145/2789168.2790109) | Ketukan tombol (gerak jari skala sentimeter) terdeteksi CSI: deteksi 97,5%, klasifikasi kunci tunggal 96,4% pada kondisi terkendali | DIVERIFIKASI (baru) | 2.3 |
| mosleh2022 | Mosleh dkk., IEEE Access 10 2022 (DOI 10.1109/access.2022.3230003) | Gerak napas (dada milimeter) dari CSI: pola 99,54%, laju 98,69% pada kanal cukup baik | DIVERIFIKASI (baru) | 2.3 |
| chen2023 | Chen dkk., ACM CSUR 2023 | Model CSI mudah overfitting terhadap orang dan ruang; strategi lintas domain | DIVERIFIKASI | 2.3, 3.2 |
| zhang2022 | Zhang dkk., TPAMI 2022 (Widar3.0) | Generalisasi gestur lintas domain dengan profil kecepatan Doppler | DIVERIFIKASI | 2.3, 2.6 |
| ma2019 | Ma dkk., ACM CSUR 2019 | Survei penginderaan Wi-Fi CSI (amplitudo, fase, Doppler) | DIVERIFIKASI | 2.3 |

### Kelompok D — Preseden supervisi visi untuk pelatihan model Wi-Fi

| Kunci | Rujukan ringkas | Klaim yang dipakai proposal | Status | Bab |
|---|---|---|---|---|
| wang2019 | Wang dkk., ICCV 2019 (Person-in-WiFi) | Persepsi tubuh dari Wi-Fi dengan supervisi kamera | DIVERIFIKASI | 2.5 |
| geng2023 | Geng dkk., arXiv 2023 (DensePose from WiFi) | Pemetaan permukaan tubuh dari Wi-Fi dengan jaringan visi sebagai guru | DIVERIFIKASI | 2.5 |

### Kelompok E — Pengenalan isyarat Indonesia berbasis visi, dataset, dan YOLO26

| Kunci | Rujukan ringkas | Klaim yang dipakai proposal | Status | Bab |
|---|---|---|---|---|
| dwijayanti2021 | Dwijayanti dkk., IJACSA 2021 | CNN BISINDO 26 huruf + 10 angka; SIBI bahasa formal sekolah | DIVERIFIKASI | 2.2, 2.11 |
| kindy2025 | Kindy dkk., Procedia CS 2025 | Dataset video BISINDO tingkat kata + baseline | DIVERIFIKASI | 2.11 |
| wiguna2025 | Wiguna & Rojali, IJACSA 2025 | Kalimat BISINDO dari video (3D CNN-LSTM) | DIVERIFIKASI | 2.11 |
| sebastian2025 | Sebastian dkk., Procedia CS 2025 | Pengenalan gestur tubuh sadar-spasial BISINDO | DIVERIFIKASI | 2.11 |
| sanjaya2023 | Sanjaya & Ilone, IJCS 2023 | SLR deep learning citra BISINDO | DIVERIFIKASI | 2.2, 2.11 |
| soekarta2024 | Soekarta dkk., INSECT 2024 | MediaPipe Android; 24 huruf statis SIBI; 90,85% | DIVERIFIKASI | 2.2, 2.11 |
| rabit2026 | Amelia Safrida dkk., Rabit 11(2) 2026 (DOI 10.36341/rabit.v11i2.8340) | Dataset citra alfabet SIBI 24 kelas (A-Y tanpa J dan Z), MobileNetV2 97,10% | DIVERIFIKASI (baru) | 2.8 |
| dbesti2026 | Maulana dkk., DBESTI 2026 | Aplikasi Android pengenalan alfabet statis SIBI (arah pengenalan) | DIVERIFIKASI | 2.2 |
| zheng2023 | Zheng dkk., ACM CSUR 2023 | Survei estimasi pose berbasis pembelajaran dalam | DIVERIFIKASI | 2.5 |
| lugaresi2019 | Lugaresi dkk., arXiv 2019 | MediaPipe: kerangka pipeline persepsi; PoseLandmarker dipakai skrip ADR-079 RuView | DIVERIFIKASI | 2.4 |
| jocher2026 | Jocher dkk., arXiv 2026 (YOLO26) | Keluarga model visi waktu nyata multi-tugas termasuk pose | DIVERIFIKASI | 2.5 |
| ultralytics_pose | Ultralytics, dok. resmi tasks/pose | Model YOLO26 pose terlatih COCO menghasilkan 17 keypoint tubuh | DIVERIFIKASI | 2.5 |
| sapkota2025 | Sapkota dkk., arXiv 2025 | Analisis YOLO26: efisiensi inferensi dan kesiapan perangkat tepi | DIVERIFIKASI | 2.5 |

### Kelompok F — Arah balik: teks/ucapan menjadi isyarat

| Kunci | Rujukan ringkas | Klaim yang dipakai proposal | Status | Bab |
|---|---|---|---|---|
| kasibi2019 | Zikky & Akbar, JST 2019 | KASIBI: suara → STT → basis data → animasi peraga 3D; uji 3,362/4 | DIVERIFIKASI | 2.2, 2.8, 2.11 |
| opensibi2022 | Fatmawati dkk., TMJ 2022 | OpenSIBI: Google STT → API model 3D Collada → animasi; 50 kosakata (9 angka, 26 huruf, 15 kata); keterbatasan kosakata diakui | DIVERIFIKASI (PDF penuh) | 2.2, 2.8, 2.11 |
| intecoms2024 | Rodhiyah & Wulandari, INTECOMS 2024 | Aplikasi pembelajaran dasar isyarat SIBI | DIVERIFIKASI | 2.2 |
| sagawa2002 | Sagawa & Takeuchi, ACM Multimedia 2002 | Sistem pengajaran JSL dengan pengenalan dan pembangkitan isyarat | DIVERIFIKASI | 2.2 |
| rakun2015 | Rakun dkk., IEEE TIME-E 2015 (DOI 10.1109/TIME-E.2015.7389747) | Kata berinfleksi SIBI dikenali dengan HMM: bukti struktur kata jadian | DIVERIFIKASI (baru) | 2.8 |
| anggraini2019 | Anggraini & Rakun dkk., ICEEI 2019 (DOI 10.1109/ICEEI47359.2019.8988806) | Komponen gestur kata berinfleksi SIBI | DIVERIFIKASI (baru) | 2.8 |
| picron2024 | Picron dkk., Springer 2024 | Penerjemahan mesin bahasa isyarat dalam praktik: masalah terbuka | DIVERIFIKASI (metadata) | 2.8 |
| hakozaki2025 | Hakozaki dkk., ASSETS 2025 | Evaluasi avatar JSL dengan mouthing: non-manual isu kelas satu | DIVERIFIKASI (metadata) | 2.8 |
| bailenson2021 | Bailenson, TMB 2021 | Paparan kamera berkelanjutan dikaitkan kelelahan nonverbal | DIVERIFIKASI | 1.1, 2.2 |

### Kelompok G — TTS dan ASR Bahasa Indonesia

| Kunci | Rujukan ringkas | Klaim yang dipakai proposal | Status | Bab |
|---|---|---|---|---|
| kokoro | hexgrad, model card Kokoro-82M (HF) | Kokoro v1.0 mendukung 8 bahasa dan 54 suara; Indonesia tidak termasuk; lisensi Apache-2.0; 82 juta parameter | DIVERIFIKASI (baru) | 2.7 |
| pratap2023 | Pratap dkk., arXiv 2305.13516 (MMS) | Proyek MMS: teknologi ucapan masif multibahasa | DIVERIFIKASI | 2.7 |
| mmsttsind | facebook/mms-tts-ind, model card (HF) | Checkpoint TTS Indonesia (VITS), lisensi CC-BY-NC 4.0, dapat dijalankan lokal | DIVERIFIKASI (baru) | 2.7 |
| radford2022 | Radford dkk., arXiv 2212.04356 (Whisper) | ASR 100+ bahasa termasuk Indonesia; dilatih 5 juta jam (1 juta lemah + 4 juta pseudo) | DIVERIFIKASI | 2.7 |
| fasterwhisper | SYSTRAN, repo faster-whisper | large-v3 fp16 ±4,5 GB VRAM; int8 ±2,9 GB; 13 menit audio 59 detik (int8) pada RTX 3070 Ti 8 GB | DIVERIFIKASI (baru) | 2.7, 3.4 |
| googlecloud_tts | Google Cloud, dok. suara dan harga | Suara id-ID Standard dan Premium; Standard ±4 dolar AS/juta karakter setelah jatah gratis bulanan | DIVERIFIKASI (baru) | 2.7 |
| azure_tts | Microsoft Learn, dukungan bahasa | Suara id-ID-GadisNeural dan id-ID-ArdiNeural | DIVERIFIKASI (baru) | 2.7 |

### Kelompok H — Platform ESP32-S3/RuView, metode, dan evaluasi

| Kunci | Rujukan ringkas | Klaim yang dipakai proposal | Status | Bab |
|---|---|---|---|---|
| hernandez2020 | Hernandez & Bulut, WoWMoM 2020 | Dasar akuisisi CSI mandiri berbasis IoT pada ESP32 | DIVERIFIKASI | 2.4 |
| ruvnet2026 | RuView, GitHub commit fefb0f9 | Firmware CSI (ADR-018, UDP), server, kalibrasi 600 frame + 8 anchor, segmentasi energi, dashboard, mode privasi, ADR-079; CSI_MIN_SEND_INTERVAL_US 20 ms (maks 50 fps) | DIVERIFIKASI (kode dibaca) | 2.4, 3.2 |
| esp32s3_datasheet | Espressif, datasheet ESP32-S3 v2.2 | Dual-core LX7 240 MHz; SRAM 512 KB; ROM 384 KB; PSRAM s.d. 8 MB octal; WiFi b/g/n 2,4 GHz 1T1R; arus RX 88-91 mA, TX puncak 283-340 mA | DIVERIFIKASI (baru) | 2.4, 3.4 |
| espcsi | Espressif, repo esp-csi | Dukungan CSI seluruh seri ESP32 termasuk S3; pola kirim/terima CSI; 56 subcarrier HT20 | DIVERIFIKASI (baru) | 2.4 |
| esptflm | Espressif, tflite-micro-esp-examples | Contoh TFLM (micro_speech 18,4 KB; person detection) | DIVERIFIKASI (baru) | 2.6, 3.7 |
| espdl | Espressif, repo esp-dl | Model int8 contoh dan tolok ukur di S3 (MobileNetV2 437,9 ms; hand-gesture 69,2 ms) | DIVERIFIKASI (baru) | 2.6 |
| espnn | Espressif, repo esp-nn | Akselerasi kernel int8; person detection 2.300 ms → 54 ms di S3 (model 293,5 KB) | DIVERIFIKASI (baru) | 2.6, 3.7 |
| cortes1995 | Cortes & Vapnik, Machine Learning 1995 | SVM margin maksimum | DIVERIFIKASI | 2.6 |
| mountrakis2011 | Mountrakis dkk., ISPRS 2011 | SVM kuat pada data kecil | DIVERIFIKASI | 2.6 |
| kiranyaz2021 | Kiranyaz dkk., MSSP 2021 | 1D-CNN untuk deret waktu | DIVERIFIKASI | 2.6 |
| chow1970 | Chow, IEEE TIT 1970 | Pertukaran galat-penolakan optimal | DIVERIFIKASI | 2.6 |
| cai2024 | Cai dkk., Sensors 2024 | Amplitudo dan fase CSI saling melengkapi | DIVERIFIKASI | 2.6 |
| nyquist1928, shannon1949 | Nyquist 1928; Shannon 1949 | Kriteria pencuplikan untuk pita Doppler | DIVERIFIKASI | 2.3 |
| bowen2009 | Bowen dkk., AJPM 2009 | Desain studi kelayakan | DIVERIFIKASI | 2.10 |
| sokolova2009 | Sokolova & Lapalme, IPM 2009 | Metrik klasifikasi | DIVERIFIKASI | 2.10 |
| likert1932 | Likert, Archives of Psychology 1932 | Skala pengukuran sikap untuk kuesioner | DIVERIFIKASI | 3.8 |

## 4. Pemisahan fakta, hipotesis, keputusan desain, dan hal yang belum diketahui

Fakta bersumber pada kelompok A-H di atas dan dipakai tanpa melebihi sumbernya (misalnya angka akurasi SignFi hanya dikutip untuk konteks dalam sesi satu pengguna perangkat multi-antena, bukan untuk memproyeksikan kinerja ESP32). Hipotesis penelitian yang dinyatakan sebagai dugaan dan diuji melalui gerbang: (a) isyarat SIBI yang dibedakan lintasan lengan dapat dipisahkan dari CSI satu tautan ESP32-S3 (G0-G2); (b) kinerja menurun lintas pengguna dan ruang sehingga perlu kalibrasi atau personalisasi (G3); (c) latensi ujung ke ujung kedua arah cukup rendah untuk pemakaian nyaman (diukur, tidak dijanjikan angkanya); (d) ejaan jari dapat menjadi fallback yang diterima pengguna (ditelaah lewat uji kegunaan). Keputusan desain dengan alasannya (bukan fakta): memakai server lokal sebagai jalur utama prototipe; memakai kamus kata-level dan bukan penerjemahan tata bahasa; menempatkan TTS lokal MMS sebagai pilihan utama dengan catatan lisensi nonkomersial; memakai UDP untuk aliran label. Hal yang belum diketahui dan ditandai di naskah dengan penanda: daftar isyarat terpilih, ambang tiap gerbang, jarak antarmodul, jumlah sesi, profil pengguna baru, pilihan final ukuran model ASR, indikator latensi layak, butir kuesioner, rubrik validator, serta identitas mitra dan persetujuan etika.

## 5. Kontradiksi dan catatan verifikasi penting

Lima kontradiksi atau jebakan verifikasi dijumpai selama riset dan diselesaikan sebagai berikut. Pertama, judul "penerjemah" pada sejumlah publikasi Indonesia menunjuk arah pengenalan (isyarat menjadi teks), bukan arah balik; hanya KASIBI dan OpenSIBI yang benar-benar membangun arah teks/suara menjadi isyarat, keduanya kata-level. Kedua, jumlah huruf alfabet SIBI tercatat 26 (A-Z) pada OpenSIBI tetapi dataset citra statis riset hanya memuat 24 kelas (A-Y tanpa J dan Z) karena dua huruf tersebut bergerak; alasan persisnya belum terbaca dari sumber primer sehingga naskah hanya menyebut perbedaan cakupan tanpa menebak sebab. Ketiga, angka kosakata kamus SIBI yang sering dikutip (sekitar 2.600) tidak ditemukan sumber layak kutip setelah penelusuran DDG, Bing, Crossref, dan OpenAlex; angka ini tidak dipakai di naskah. Keempat, Kokoro dikenal sebagai TTS ringan multibahasa, tetapi model cardnya mencantumkan delapan bahasa tanpa Indonesia; Kokoro dicantumkan di naskah justru sebagai bukti kehati-hatian pemilihan teknologi. Kelima, repo esp32-csi-tool pada organisasi espressif tidak dapat diakses (404) sedangkan alat serupa berada pada repositori penelitinya; klaim teknis CSI pada naskah tetap merujuk dokumentasi ESP-IDF dan esp-csi resmi.

## 6. Rujukan baru sejak proposal lama

Dua puluh rujukan baru ditambahkan pada proposal revisi, seluruhnya terverifikasi pada 25 Oktober 2026: WiSign (ACM TIST 2020), WiKey (MobiCom 2015), Mosleh dkk. (IEEE Access 2022), Mursita (INKLUSI 2015), Picron dkk. (Springer 2024), Hakozaki dkk. (ASSETS 2025), Amelia Safrida dkk. (Rabit 2026), Rakun dkk. (TIME-E 2015), Anggraini dkk. (ICEEI 2019), Radford dkk. (Whisper, arXiv), Pratap dkk. (MMS, arXiv), model card facebook/mms-tts-ind, model card Kokoro-82M, repositori faster-whisper, halaman suara dan harga Google Cloud TTS, halaman dukungan suara Azure, datasheet ESP32-S3 v2.2, repositori esp-csi, repositori esp-dl, repositori tflite-micro-esp-examples, dan repositori esp-nn. Enam rujukan lama dikeluarkan karena kerangkanya melekat pada uji persepsi kamera dan umpan balik latihan yang tidak lagi menjadi rancangan inti: Sigrist dkk. 2013, Zajonc 1965, Daniel dkk. 2024, dan Hassan dkk. 2026, ditambah dua entri pendukung minor lainnya sesuai catatan audit. Arsip JSON verifikasi Crossref tersimpan pada `scripts/translator-sibi/meta_rujukan_baru.json` dan catatan riset lengkap pada `riset-translator-sibi/` sebagai jejak audit.
