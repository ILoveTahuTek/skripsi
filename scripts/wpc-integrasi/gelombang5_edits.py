# -*- coding: utf-8 -*-
"""Kumpulan suntingan Gelombang 5 (Task 39, Agent Brief v3).
Semua anchor memakai penomoran TABEL LAMA (renumber tabel dijalankan setelah EDITS).
Anchor 'YOLO26m-Pose' mengasumsikan penggantian global YOLO26-Pose -> YOLO26m-Pose sudah berjalan."""

# ============ BAB I ============

EDITS_BAB1 = [
    ("1.1 konteks SLB/inklusif",
     "Kewajiban itu sulit dipenuhi bila kemampuan menjembatani dua arah hanya dimiliki segelintir juru bahasa sehingga teknologi bantu komunikasi yang murah dan tersedia menjadi salah satu jalur pelengkap [7].",
     "Kebutuhan menjembatani kedua arah tersebut paling terasa di lingkungan pendidikan formal, baik di SLB maupun di sekolah inklusif, tempat siswa tunarungu berguru kepada guru dan belajar bersama teman pendengar yang umumnya tidak menguasai isyarat [11]. Kewajiban aksesibilitas itu sulit dipenuhi bila kemampuan menjembatani dua arah hanya dimiliki segelintir juru bahasa sehingga teknologi bantu komunikasi yang murah dan tersedia menjadi jalur pelengkap yang penting [7]."),

    ("1.1 privasi + nirsentuh",
     "sedangkan kehadiran kamera yang terus menyala selama percakapan diduga memengaruhi kenyamanan pengguna dan dikaitkan dengan kelelahan nonverbal [19]. Kesenjangan-kesenjangan tersebut menjadi titik berangkat penelitian ini.",
     "sedangkan kehadiran kamera yang terus menyala selama percakapan diduga memengaruhi kenyamanan pengguna dan dikaitkan dengan kelelahan nonverbal [19], serta menuntut perhatian terhadap privasi bila perekaman citra berlangsung terus-menerus di ruang kelas. Kondisi tersebut mendorong kebutuhan teknologi penginderaan nirsentuh (*device-free*) dan bebas kamera (*camera-free*) berbasis gelombang radio Wi-Fi yang menjaga privasi penggunanya sekaligus menekan biaya perangkat. Kesenjangan-kesenjangan tersebut menjadi titik berangkat penelitian ini."),

    ("1.1 paragraf pra-penelitian (sisip)",
     "Sebagai studi kelayakan, penelitian ini tidak mengklaim penerjemahan kontinu kosakata penuh.",
     "Sisi visi dari gagasan tersebut telah dibuktikan pada tahap pra-penelitian. Model visi YOLO26m-Pose telah dilatih pada *dataset* visual SIBI terkurasi bersumber banyak melalui repositori milik peneliti (Subbab 2.5 dan 3.7.4); model tersebut mengestimasi 21 titik artikulasi tangan, yaitu satu titik pergelangan tangan dan empat titik pada setiap jari, dan terbukti mengenali 26 huruf SIBI secara akurat, termasuk membedakan pasangan huruf yang mirip seperti V dan U dari jarak antarujung telunjuk dan jari tengah serta mengikuti lintasan gerak telunjuk huruf J dan Z. Proposal ini merupakan tahap pengembangan berikutnya, yaitu membangun purwarupa berbasis Wi-Fi CSI yang mereplikasi kemampuan pembedaan tersebut tanpa kamera.\n\nSebagai studi kelayakan, penelitian ini tidak mengklaim penerjemahan kontinu kosakata penuh."),

    ("1.1 ground truth guru",
     "Model murid CSI dilatih dengan distilasi guru\u2013murid (*teacher\u2013student*): model guru kamera YOLO26m-Pose mengekstrak deret 21 *keypoint* pose tangan dari video perekaman, sedangkan label kelas tetap berasal dari anotasi protokol (Subbab 2.5).",
     "Model murid CSI dilatih dengan distilasi guru\u2013murid (*teacher\u2013student*): model guru kamera YOLO26m-Pose hasil pra-penelitian mengekstrak deret 21 *keypoint* pose tangan beserta label huruf dari video perekaman tersinkron, dan keluaran tersebut direkam sebagai *ground truth* sekaligus supervisi distilasi selama akuisisi data (Subbab 2.5 dan 3.7)."),

    ("1.1 penamaan SenseSIBI",
     "Berdasarkan uraian tersebut, penelitian ini merancang dan membangun purwarupa sistem penerjemahan dua arah antara SIBI dan teks atau ujaran bahasa Indonesia berbasis Wi-Fi CSI dengan inferensi model pada modul ESP32-S3 dan pemrosesan bahasa pada server.",
     "Berdasarkan uraian tersebut, penelitian ini merancang dan membangun purwarupa sistem penerjemahan dua arah antara SIBI dan teks atau ujaran bahasa Indonesia berbasis Wi-Fi CSI dengan inferensi model pada modul ESP32-S3 dan pemrosesan bahasa pada server. Purwarupa tersebut diberi nama SenseSIBI, singkatan dari *Sensing & Translation of SIBI*."),

    ("1.2 rumusan 1",
     "1. Bagaimana merancang purwarupa sistem penerjemahan dua arah antara SIBI dan teks atau ujaran bahasa Indonesia berbasis dua hingga tiga modul ESP32-S3 yang menangkap CSI dan menjalankan inferensi model pada perangkat, dengan pemrosesan bahasa pada server melalui layanan ucapan awan dan server lokal cadangan, termasuk protokol perekaman *dataset* isyarat terisolasi serta pelatihan model murid CSI dengan supervisi model guru YOLO26m-Pose?",
     "1. Bagaimana merancang purwarupa sistem penerjemahan dua arah antara SIBI dan teks atau ujaran bahasa Indonesia berbasis sepasang modul ESP32-S3 (node pemancar dan node penerima) yang menangkap CSI dan menjalankan inferensi model pada perangkat, dengan pemrosesan bahasa pada server melalui layanan ucapan awan dan server lokal cadangan, termasuk adaptasi arsitektur RuView dan *backbone* WiFi-DensePose terkuantisasi int8, protokol perekaman *dataset* isyarat terisolasi, serta pelatihan model murid CSI dengan supervisi model guru YOLO26m-Pose?"),

    ("1.2 rumusan 3",
     "3. Bagaimana kelayakan purwarupa sebagai alat bantu komunikasi dua arah untuk kosakata terbatas ditinjau dari latensi ujung ke ujung, cakupan kosakata, keandalan operasional, dan penilaian validator penutur tunarungu?",
     "3. Bagaimana kelayakan purwarupa sebagai alat bantu komunikasi dua arah untuk kosakata terbatas ditinjau dari latensi ujung ke ujung, cakupan kosakata, keandalan operasional, penerimaan pengguna akhir, dan biaya purwarupa?"),

    ("1.3 tujuan 1",
     "1. Merancang purwarupa sistem penerjemahan dua arah antara SIBI dan teks atau ujaran bahasa Indonesia berbasis dua hingga tiga modul ESP32-S3 yang menangkap CSI dan menjalankan inferensi model pada perangkat, dengan pemrosesan bahasa pada server melalui layanan ucapan awan dan server lokal cadangan, termasuk protokol perekaman *dataset* isyarat terisolasi serta pelatihan model murid CSI dengan supervisi model guru YOLO26m-Pose.",
     "1. Merancang purwarupa sistem penerjemahan dua arah antara SIBI dan teks atau ujaran bahasa Indonesia berbasis sepasang modul ESP32-S3 (node pemancar dan node penerima) yang menangkap CSI dan menjalankan inferensi model pada perangkat, dengan pemrosesan bahasa pada server melalui layanan ucapan awan dan server lokal cadangan, termasuk adaptasi arsitektur RuView dan *backbone* WiFi-DensePose terkuantisasi int8, protokol perekaman *dataset* isyarat terisolasi, serta pelatihan model murid CSI dengan supervisi model guru YOLO26m-Pose."),

    ("1.3 tujuan 3",
     "3. Menguji kelayakan purwarupa sebagai alat bantu komunikasi dua arah untuk kosakata terbatas berdasarkan latensi ujung ke ujung, cakupan kosakata, keandalan operasional, dan penilaian validator penutur tunarungu.",
     "3. Menganalisis kelayakan operasional purwarupa sebagai alat bantu komunikasi dua arah untuk kosakata terbatas melalui pengujian bergerbang lima tahap (G0 hingga G4) yang menilai latensi ujung ke ujung, cakupan kosakata, keandalan operasional, penerimaan pengguna akhir, dan biaya purwarupa."),

    ("1.4 batasan 3 perangkat",
     "3. Perangkat keras terdiri atas 2\u20133 modul ESP32-S3 (masing-masing direncanakan memiliki layar kecil, baterai, *speaker*, mikrofon I2S, tombol tekan-untuk-bicara, dan rotary encoder volume) serta satu laptop ASUS TUF Dash F15 FX516PR (Intel Core i7-11370H, RTX 3070 Laptop 8 GB VRAM, RAM 16 GB) sebagai mesin akuisisi jalur guru, mesin pengembangan, dan server lokal cadangan. Pelatihan model guru dan murid memakai layanan server GPU Kaggle.",
     "3. Perangkat keras penginderaan terdiri atas sepasang modul ESP32-S3, yaitu node pemancar (TX) dan node penerima (RX), yang beroperasi pada pita 2,4 GHz (IEEE 802.11b/g/n) dengan kanal 20 MHz (56 *subcarrier*: 52 data dan 4 pilot) serta antena tunggal 1T1R; modul penerima sekaligus memuat antarmuka pengguna berupa layar kecil, baterai, *speaker*, mikrofon I2S, tombol tekan-untuk-bicara, dan rotary encoder volume. Selain itu, disediakan satu laptop ASUS TUF Dash F15 FX516PR (Intel Core i7-11370H, RTX 3070 Laptop 8 GB VRAM, RAM 16 GB) sebagai mesin akuisisi jalur guru, mesin pengembangan, dan server lokal cadangan, serta satu *router* Wi-Fi atau *access point* yang berfungsi murni sebagai jembatan jaringan dan penjangkar kanal bagi server ucapan, bukan perangkat penginderaan. Pelatihan model guru dan model murid memakai layanan server GPU Kaggle."),

    ("1.6 sistematika BAB II",
     "Kajian mencakup bahasa isyarat dan SIBI, kebutuhan komunikasi dua arah dan sistem terdahulu, Wi-Fi CSI, modul ESP32-S3 dan platform RuView beserta koeksistensi radionya, peran YOLO26m-Pose sebagai model guru kamera dalam distilasi guru\u2013murid,",
     "Kajian mencakup bahasa isyarat dan SIBI, kebutuhan komunikasi dua arah dan sistem terdahulu, Wi-Fi CSI beserta model zona Fresnel dan pembersihan CSI-ratio, modul ESP32-S3 dan platform RuView beserta koeksistensi radionya dan keluarga model WiFi-DensePose, peran YOLO26m-Pose sebagai model guru kamera dalam distilasi guru\u2013murid,"),
]

# ============ BAB II ============

EDITS_BAB2 = [
    ("2.3 sisip zona Fresnel + CSI-ratio",
     "Dengan demikian, CSI menyediakan banyak kanal pengamatan dari satu pasang pemancar dan penerima.\n\nGerak lengan juga menghasilkan komponen Doppler",
     "Dengan demikian, CSI menyediakan banyak kanal pengamatan dari satu pasang pemancar dan penerima.\n\nPerubahan kanal tersebut memiliki dasar fisika pada model zona Fresnel. Wu dkk. [81] merumuskan zona Fresnel sebagai wilayah elips di sekitar garis pandang pemancar\u2013penerima tempat gelombang dipantulkan dan dilenturkan; gerakan objek yang melintasi batas zona mengubah panjang jalur pantulan sehingga amplitudo dan fase pada tiap *subcarrier* bergeser. Pada skala gerak mikro, artikulasi 21 titik jari pengisyarat menggeser jalur pantulan pada orde sentimeter hingga milimeter sehingga setiap konfigurasi huruf membentuk pola perubahan *subcarrier* yang khas. Akan tetapi, fase CSI mentah tercemar derau fase osilator lokal (*local oscillator phase noise*) dan offset fase acak sehingga tidak dapat dipakai secara langsung. Model CSI-ratio mengatasinya melalui rasio atau perkalian konjugat yang saling menghapus komponen fase bawaan perangkat tanpa memerlukan perangkat tambahan [81]; teknik konjugat serupa menjadi dasar kalibrasi fase Widar2.0 pada tautan Wi-Fi tunggal [82]. Dalam penelitian ini, prinsip CSI-ratio diterapkan pada modul penerima sebagai rasio terhadap rekam acuan hasil kalibrasi ruang karena setiap tautan ESP32-S3 hanya memuat satu antena penerima; formulasi pastinya ditetapkan pada tahap karakterisasi (Subbab 3.7).\n\nGerak lengan juga menghasilkan komponen Doppler"),

    ("2.4 nama firmware",
     "Komponennya meliputi *firmware* ESP32 penangkap CSI dengan format bingkai ADR-018 yang dikirim melalui *User Datagram Protocol* (UDP)",
     "Komponennya meliputi *firmware* `esp32-csi-node` penangkap CSI dengan format bingkai ADR-018 yang dikirim melalui *User Datagram Protocol* (UDP)"),

    ("2.4 sisip WiFi-DensePose",
     "Kalibrasi ruang bawaan memakai 600 bingkai dan 8 *anchor* selama kurang lebih empat menit, sedangkan mode privasi menekan fitur biometrik agar tidak diterbitkan keluar dari server [28].\n\nFakta teknis yang paling menentukan",
     "Kalibrasi ruang bawaan memakai 600 bingkai dan 8 *anchor* selama kurang lebih empat menit, sedangkan mode privasi menekan fitur biometrik agar tidak diterbitkan keluar dari server [28].\n\nSelain rantai akuisisi, RuView juga menerbitkan keluarga model WiFi-DensePose untuk penginderaan spasial dari CSI. Arsitektur tersebut menelusuri DensePose from WiFi yang memetakan sinyal Wi-Fi ke koordinat permukaan tubuh dengan jaringan visi sebagai guru [64]. Repositori RuView menyediakan enkode terpralatih ruvnet/wifi-densepose-pretrained yang dilatih secara kontrastif dan mencapai akurasi *triplet* temporal 82,3% pada data pisah-uji [28], serta varian ruvnet/wifi-densepose-mmfi-pose yang dilatih pada *dataset* multimodal MM-Fi berisi lebih dari 320 ribu bingkai tersinkron dari 40 partisipan [83]. Kedua model tersebut tersedia dalam kuantisasi int8 untuk komputasi tepi [28]. Dalam penelitian ini, enkode terpralatih tersebut dipakai sebagai *backbone* pengekstrak fitur murid CSI, sedangkan varian MM-Fi menjadi preseden bahwa CSI perangkat komersial dapat dipetakan ke *keypoint* tubuh (Subbab 2.6 dan 3.7).\n\nFakta teknis yang paling menentukan"),

    ("2.4 Tabel 2.1 baris model",
     "| *Pipeline* akuisisi tersinkron kamera\u2013CSI (ADR-079) | Jalur guru riset dengan estimator diganti YOLO26m-Pose |\n| Modul estimasi pose *on-device* | Tidak dipakai |",
     "| *Pipeline* akuisisi tersinkron kamera\u2013CSI (ADR-079) | Jalur guru riset dengan estimator diganti YOLO26m-Pose |\n| Model WiFi-DensePose terpralatih (pretrained dan mmfi-pose, int8) | Inisialisasi *backbone* murid CSI dan preseden pemetaan CSI ke pose |\n| Modul estimasi pose *on-device* | Tidak dipakai |"),

    ("2.5 label dari guru",
     "Label kelas SIBI tetap berasal dari kartu pemandu pada protokol *elisitasi* sehingga makna huruf tidak bergantung pada dugaan model visi; keluaran klasifikasi huruf yang juga dimiliki model guru repositori peneliti tidak dipakai pada jalur pelatihan murid. Deret *keypoint* guru juga tetap dipakai untuk verifikasi batas segmen, penyaringan segmen buruk, dan diagnosis kesalahan secara luring (Subbab 3.8).",
     "Selama akuisisi data, keluaran guru berupa deret 21 *keypoint* dan label huruf direkam sebagai *ground truth* yang menjadi supervisi distilasi murid, mengikuti pola akuisisi tersinkron ADR-079; kartu pemandu protokol tetap ditampilkan pada setiap repetisi dan dicocokkan dengan label guru untuk menjaga konsistensi anotasi (Subbab 3.6 dan 3.7). Deret *keypoint* guru juga dipakai untuk verifikasi batas segmen, penyaringan segmen buruk, dan diagnosis kesalahan secara luring (Subbab 3.8)."),

    ("2.5 sisip hasil pra-penelitian + luring/daring",
     "Peran kamera dengan demikian terbatas pada tahap akuisisi data dan pelatihan serta tidak pernah menyala pada produk akhir.",
     "Kemampuan pembedaan model guru telah dibuktikan pada tahap pra-penelitian melalui pelatihan pada *dataset* visual SIBI terkurasi bersumber banyak (Subbab 3.7.4). Pelatihan tersebut menghasilkan model juara dengan *pose* mAP50 0,8944 pada 49 kelas isyarat, serta mAP50 0,9580 dan akurasi huruf 97,6% pada himpunan 24 huruf statis. Model tersebut juga terbukti membedakan pasangan huruf yang konfigurasinya mirip, seperti V dan U yang hanya berbeda jarak antarujung telunjuk dan jari tengah, serta mengikuti lintasan gerak telunjuk huruf J dan Z. Bukti tersebut menegaskan bahwa 21 titik artikulasi jari memuat informasi yang cukup untuk membedakan gestur mikro SIBI; pertanyaan penelitian ini adalah apakah sinyal CSI mampu mereplikasi kemampuan tersebut tanpa kamera.\n\nKerangka distilasi tersebut bekerja dalam dua ranah. Pelatihan berjalan luring (*offline*) di server GPU, yaitu murid ber-*backbone* WiFi-DensePose int8 dengan kepala 1D-CNN melatih bobotnya di bawah supervisi guru memakai rekaman tersinkron ADR-079. Operasi lapangan berjalan tanpa kamera, yaitu murid menyimpulkan label huruf murni dari jendela CSI.\n\nPeran kamera dengan demikian terbatas pada tahap akuisisi data dan pelatihan serta tidak pernah menyala pada produk akhir."),

    ("2.6 arsitektur murid",
     "Model utamanya adalah *one-dimensional Convolutional Neural Network* (1D-CNN) berukuran kecil yang menerapkan konvolusi sepanjang sumbu waktu dan cocok untuk data deret waktu [70]. Dalam penelitian ini, 1D-CNN berperan sebagai model murid yang dilatih dari jendela CSI dengan supervisi tambahan deret pose guru (Subbab 3.7).",
     "Model utamanya berupa murid dua bagian, yaitu *backbone* WiFi-DensePose terkuantisasi int8 [28], [64] sebagai pengekstrak fitur spasial sinyal CSI 56 *subcarrier* dan kepala klasifikasi *one-dimensional Convolutional Neural Network* (1D-CNN) yang menerapkan konvolusi sepanjang sumbu waktu [70]. Kepala 1D-CNN dipilih karena ringan dan cocok untuk data deret waktu; dalam penelitian ini, seluruh murid dilatih dari jendela CSI di bawah supervisi label dan deret pose guru (Subbab 3.7)."),

    ("2.6 inisialisasi murid",
     "Model murid dilatih dengan PyTorch pada layanan server GPU Kaggle, dikuantisasi int8, lalu dijalankan melalui TensorFlow Lite Micro atau ESP-DL dengan penyangga pada PSRAM.",
     "Model murid diinisialisasi dari bobot terpralatih WiFi-DensePose (ruvnet/wifi-densepose-pretrained) [28], dilatih dengan PyTorch pada layanan server GPU Kaggle, dikuantisasi int8, lalu dijalankan pada modul penerima melalui ESP-DL dengan akselerasi ESP-NN dan penyangga pada PSRAM."),

    ("2.9 klarifikasi peran AP",
     "Seluruh komunikasi purwarupa berlangsung pada satu kanal Wi-Fi yang mengikuti kanal *access point* sehingga modul dapat menjalankan penangkapan CSI dan komunikasi data secara serentak (Subbab 2.4).",
     "Seluruh komunikasi purwarupa berlangsung pada satu kanal Wi-Fi yang mengikuti kanal *access point* sehingga modul dapat menjalankan penangkapan CSI dan komunikasi data secara serentak (Subbab 2.4). *Access point* tersebut berfungsi murni sebagai jembatan jaringan (*network bridge*) dan penjangkar kanal (*same-channel lock*) bagi komunikasi data serta server ucapan; *access point* bukan perangkat penginderaan dan purwarupa tidak memakai *router* 5 GHz multi-antena."),

    ("2.10 lima gerbang",
     "Dalam penelitian ini, kelayakan dinilai bertahap melalui gerbang keputusan G0\u2013G4 (BAB III).",
     "Dalam penelitian ini, kelayakan dinilai bertahap melalui lima gerbang keputusan G0\u2013G4 (BAB III)."),

    ("2.10 dimensi biaya",
     "Ketiga, keandalan operasional ditinjau dari laju deteksi palsu per jam saat tidak ada isyarat dan konsumsi arus modul sebagai indikator ketahanan baterai.",
     "Ketiga, keandalan operasional ditinjau dari laju deteksi palsu per jam saat tidak ada isyarat dan konsumsi arus modul sebagai indikator ketahanan baterai. Keempat, biaya purwarupa dianalisis dari harga komponen dan biaya layanan yang dipakai sebagai bahan penilaian kelayakan adopsi."),

    ("Tabel 2.2 baris 17",
     "| 17 | Penelitian ini | CSI dua-tiga modul ESP32-S3, distilasi guru\u2013murid YOLO26m-Pose pose tangan ke CSI, inferensi tepi; dua arah | SIBI, alfabet manual 26 huruf | Ya | Purwarupa penerjemah dua arah alfabet manual SIBI |",
     "| 17 | Penelitian ini | CSI sepasang modul ESP32-S3 dengan *backbone* WiFi-DensePose int8, distilasi guru\u2013murid YOLO26m-Pose 21 *keypoint*, inferensi tepi; dua arah | SIBI, alfabet manual 26 huruf | Ya | Purwarupa penerjemah dua arah alfabet manual SIBI |"),

    ("2.11 kebaruan kombinatif",
     "yaitu menggabungkan penginderaan CSI satu tautan antarmodul untuk alfabet manual SIBI, distilasi guru\u2013murid dari YOLO26m-Pose pose tangan ke model CSI, inferensi pada perangkat, dan integrasi dua arah dengan pemrosesan bahasa Indonesia berbasis layanan awan.",
     "yaitu menggabungkan penginderaan CSI satu tautan pada sepasang modul ESP32-S3 untuk alfabet manual SIBI, distilasi guru\u2013murid dari YOLO26m-Pose pose tangan ke murid ber-*backbone* WiFi-DensePose int8, inferensi pada perangkat, dan integrasi dua arah dengan pemrosesan bahasa Indonesia berbasis layanan awan."),
]

# ============ BAB III ============
# Blok 3.2 (intro + Gambar 3.1 + Gambar 3.2) diganti utuh

BLOK_32_LAMA = """Penelitian berlangsung selama empat belas minggu (M1\u2013M14) dalam enam tahap. Tahapan dimulai dari replikasi platform dan uji karakterisasi (T0), kemudian kurasi isyarat dan protokol (T1), perekaman *dataset* serta pelatihan guru\u2013murid (T2), uji generalisasi (T3), pengemasan purwarupa dua arah dan uji kegunaan (T4), hingga analisis dan penulisan (T5). Lima tahap pertama ditutup gerbang keputusan G0\u2013G4: jalur lolos dirangkum pada Gambar 3.1, sedangkan jalur gagal, tindakan korektif, dan uji ulang tiap gerbang dirinci pada Gambar 3.2. Bila G0 gagal untuk kedua kalinya setelah perbaikan, jalur CSI dihentikan dan dilaporkan sebagai temuan karakterisasi, lalu penelitian berlanjut ke T5; bila G1 gagal untuk kedua kalinya, tindakan mengikuti Tabel 3.6 dan dicatat sebagai temuan. Kriteria lolos dan tindakan bila gagal direncanakan untuk ditetapkan sebelum gerbang terkait dinilai; parameter yang belum ditetapkan dihimpun pada Tabel 3.6.

```mermaid
flowchart LR
    subgraph KA[" "]
        direction TB
        T0["T0 Replikasi platform,<br/>uji Delta-CSI dan<br/>koeksistensi radio (M1\u2013M2)"]
        G0("G0 akhir M2: akuisisi stabil,<br/>gerak terpisah dari diam/kosong")
        T1["T1 Kurasi isyarat, kalibrasi<br/>ruang, protokol,<br/>etika (M2\u2013M4)"]
        G1("G1 M3: separabilitas awal<br/>2\u20133 pasang huruf (nearest-centroid)")
        T2["T2 Perekaman dataset dan<br/>pelatihan guru\u2013murid<br/>(M4\u2013M8)"]
        G2("G2 M6\u2013M7: akurasi dalam sesi<br/>jauh di atas peluang acak")
        T0 --> G0
        G0 -- "lolos" --> T1
        T1 --> G1
        G1 -- "lolos" --> T2
        T2 --> G2
    end
    subgraph KB[" "]
        direction TB
        T2B["Kuantisasi int8 dan uji<br/>deployment murid ke<br/>modul ESP32-S3"]
        T3["T3 Uji generalisasi: lintas<br/>sesi, partisipan, ruang,<br/>pengguna baru (M8\u2013M10)"]
        G3("G3 M10: kinerja lintas domain<br/>di atas peluang acak")
        T4["T4 Pengemasan purwarupa<br/>dua arah dan uji kegunaan<br/>(M10\u2013M12)"]
        G4("G4 M12: kelengkapan uji<br/>dan persetujuan validator")
        T5["T5 Analisis dan penulisan<br/>(M12\u2013M14)"]
        T2B --> T3
        T3 --> G3
        G3 -- "lolos" --> T4
        T4 --> G4
        G4 -- "lolos" --> T5
    end
    KA -- "lolos" --> KB
```

Gambar 3.1 Tahapan penelitian T0\u2013T5 dan gerbang keputusan G0\u2013G4 (jalur lolos; jalur gagal dirinci pada Gambar 3.2)

```mermaid
flowchart TB
    subgraph R0[" "]
        direction LR
        G0{"G0 gagal"}
        P0["Perbaikan penempatan modul<br/>(satu kali), lalu G0 diuji ulang"]
        O0((" "))
        B0(("temuan"))
        G0 -- "gagal" --> P0
        P0 -- "lolos: T1" --> O0
        P0 -- "gagal lagi" --> B0
    end
    subgraph R1[" "]
        direction LR
        G1{"G1 gagal"}
        P1["Perubahan penempatan atau<br/>orientasi modul (satu kali),<br/>lalu G1 diuji ulang"]
        O1((" "))
        B1(("temuan"))
        G1 -- "gagal" --> P1
        P1 -- "lolos: T2" --> O1
        P1 -- "gagal lagi" --> B1
    end
    subgraph R2[" "]
        direction LR
        G2{"G2 gagal"}
        P2["Pemangkasan ke himpunan huruf<br/>yang pembeda CSI-nya paling kuat"]
        O2((" "))
        G2 -- "gagal" --> P2
        P2 -- "lanjut T2B" --> O2
    end
    subgraph R3[" "]
        direction LR
        G3{"G3 gagal"}
        P3["Cakupan menjadi personalisasi<br/>per pengguna, ditulis<br/>sebagai temuan"]
        O3((" "))
        G3 -- "gagal" --> P3
        P3 -- "lanjut T4" --> O3
    end
    subgraph R4[" "]
        direction LR
        G4{"G4 gagal"}
        P4["Hasil negatif dilaporkan<br/>sebagai temuan kelayakan"]
        O4((" "))
        G4 -- "gagal" --> P4
        P4 -- "lanjut T5" --> O4
    end
    R0 ~~~ R1
    R1 ~~~ R2
    R2 ~~~ R3
    R3 ~~~ R4
```

Gambar 3.2 Jalur gagal dan remediasi gerbang keputusan G0\u2013G4. Lingkaran kosong = lanjut ke tahap yang tertera pada label sisi; lingkaran "temuan" = penelitian berlanjut dengan hasil dilaporkan sebagai temuan. Kriteria lengkap tiap gerbang diuraikan pada Subbab 3.2.1\u20133.2.5 dan parameter yang menyertai pada Tabel 3.6."""

BLOK_32_BARU = """Penelitian berlangsung selama empat belas minggu (M1\u2013M14) dalam enam tahap. Tahapan dimulai dari replikasi platform dan uji karakterisasi meja kerja (T0), kemudian kurasi isyarat dan protokol (T1), perekaman *dataset* serta pelatihan guru\u2013murid (T2), uji generalisasi (T3), pengemasan purwarupa dua arah dan uji penerimaan pengguna (T4), hingga analisis dan penulisan (T5). Lima gerbang keputusan menutup rangkaian tersebut: G0 (meja kerja dan garis pandang langsung) memverifikasi akuisisi CSI 56 *subcarrier* pada jarak 1 meter, G1 (ruang terkontrol SLB) menilai akurasi klasifikasi 24 huruf statis serta J dan Z di lingkungan kelas, G2 (variasi pengguna dan posisi) menguji ketahanan lintas pengguna dan pergeseran posisi berdiri\u2013duduk, G3 (integrasi pemrosesan suara dua arah) mengukur latensi terjemahan isyarat-ke-suara dan suara-ke-visual, serta G4 (kelayakan operasional) menilai penerimaan pengguna akhir dan biaya purwarupa. Jalur lolos dirangkum pada Gambar 3.1, sedangkan jalur gagal, tindakan korektif, dan uji ulang tiap gerbang dirinci pada Gambar 3.2. Bila G0 gagal untuk kedua kalinya setelah perbaikan, jalur CSI dihentikan dan dilaporkan sebagai temuan karakterisasi, lalu penelitian berlanjut ke T5; tindakan bila gerbang lain gagal mengikuti Tabel 3.4. Kriteria lolos dan tindakan bila gagal direncanakan difinalkan bersama pembimbing sebelum gerbang terkait dinilai; parameter yang menyertainya dihimpun pada Tabel 3.6.

```mermaid
flowchart LR
    subgraph KA[" "]
        direction TB
        T0["T0 Replikasi platform, verifikasi<br/>CSI 56 subcarrier pada 1 m,<br/>uji Delta-CSI, koeksistensi (M1\u2013M2)"]
        G0("G0 akhir M2: meja kerja dan<br/>garis pandang langsung,<br/>akuisisi stabil, gerak terpisah")
        T1["T1 Kurasi isyarat, kalibrasi ruang,<br/>protokol, etika, rintisan separabilitas<br/>pasangan huruf mirip (M2\u2013M4)"]
        T2["T2 Perekaman dataset dan<br/>pelatihan guru\u2013murid<br/>(M4\u2013M8)"]
        T0 --> G0
        G0 -- "lolos" --> T1
        T1 --> T2
    end
    subgraph KB[" "]
        direction TB
        T2B["Kuantisasi int8 dan uji<br/>deployment murid ke<br/>modul ESP32-S3"]
        G1("G1 akhir M8: akurasi 24 statis<br/>+ J dan Z di ruang kelas<br/>di atas ambang")
        T3["T3 Uji generalisasi: lintas sesi,<br/>partisipan, ruang, posisi<br/>berdiri/duduk (M8\u2013M10)"]
        G2("G2 akhir M10: ketahanan lintas<br/>pengguna dan posisi<br/>di atas ambang")
        T4["T4 Pengemasan purwarupa dua arah,<br/>integrasi suara, uji penerimaan<br/>pengguna dan biaya (M10\u2013M12)"]
        G3("G3 M11: latensi isyarat-ke-suara<br/>dan suara-ke-visual<br/>dalam anggaran")
        G4("G4 akhir M12: penerimaan<br/>pengguna dan biaya<br/>purwarupa layak")
        T5["T5 Analisis dan penulisan<br/>(M12\u2013M14)"]
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

Gambar 3.1 Tahapan penelitian T0\u2013T5 dan gerbang keputusan G0\u2013G4 (jalur lolos; jalur gagal dirinci pada Gambar 3.2)

```mermaid
flowchart TB
    subgraph R0[" "]
        direction LR
        G0{"G0 gagal"}
        P0["Perbaikan penempatan modul<br/>(satu kali), lalu G0 diuji ulang"]
        O0((" "))
        B0(("temuan"))
        G0 -- "gagal" --> P0
        P0 -- "lolos: T1" --> O0
        P0 -- "gagal lagi" --> B0
    end
    subgraph R1[" "]
        direction LR
        G1{"G1 gagal"}
        P1["Pemangkasan ke himpunan huruf<br/>yang pembeda CSI-nya paling kuat,<br/>lalu G1 dinilai ulang"]
        O1((" "))
        G1 -- "gagal" --> P1
        P1 -- "lanjut T3" --> O1
    end
    subgraph R2[" "]
        direction LR
        G2{"G2 gagal"}
        P2["Cakupan menjadi personalisasi<br/>per pengguna, ditulis<br/>sebagai temuan"]
        O2((" "))
        G2 -- "gagal" --> P2
        P2 -- "lanjut T4" --> O2
    end
    subgraph R3[" "]
        direction LR
        G3{"G3 gagal"}
        P3["Jalur ucapan beralih ke server<br/>lokal; bila masih melampaui,<br/>dilaporkan sebagai temuan"]
        O3((" "))
        G3 -- "gagal" --> P3
        P3 -- "lanjut G4" --> O3
    end
    subgraph R4[" "]
        direction LR
        G4{"G4 gagal"}
        P4["Hasil negatif dilaporkan<br/>sebagai temuan kelayakan"]
        O4((" "))
        G4 -- "gagal" --> P4
        P4 -- "lanjut T5" --> O4
    end
    R0 ~~~ R1
    R1 ~~~ R2
    R2 ~~~ R3
    R3 ~~~ R4
```

Gambar 3.2 Jalur gagal dan remediasi gerbang keputusan G0\u2013G4. Lingkaran kosong = lanjut ke tahap yang tertera pada label sisi; lingkaran "temuan" = penelitian berlanjut dengan hasil dilaporkan sebagai temuan. Kriteria lengkap tiap gerbang diuraikan pada Subbab 3.2.1\u20133.2.6 dan parameter yang menyertai pada Tabel 3.4."""

EDITS_BAB3 = [
    ("3.1 inti distilasi",
     "Inti metodologi pelatihannya berbentuk distilasi guru\u2013murid. Model guru kamera YOLO26m-Pose mengekstrak deret 21 *keypoint* pose tangan dari video perekaman; deret tersebut menjadi supervisi tambahan bagi model murid yang mengenali huruf dari jendela CSI dan berjalan langsung pada modul (Subbab 3.7).",
     "Inti metodologi pelatihannya berbentuk distilasi guru\u2013murid. Model guru kamera YOLO26m-Pose mengekstrak deret 21 *keypoint* pose tangan dan label huruf dari video perekaman tersinkron; keluaran tersebut menjadi *ground truth* dan supervisi pelatihan bagi model murid ber-*backbone* WiFi-DensePose int8 dengan kepala 1D-CNN yang mengenali huruf dari jendela CSI dan berjalan langsung pada modul (Subbab 3.7)."),

    ("3.2.1 T0 benchtop",
     "Dua modul ESP32-S3 disiapkan dengan *firmware* RuView [28], lalu *pipeline* akuisisi tersinkron diuji tanpa partisipan. Tiga uji dilakukan pada tahap ini. Pertama, uji Delta-CSI (Subbab 3.8.1) dilakukan untuk mengetahui apakah pola CSI saat bergerak terpisah dari kondisi diam dan ruang kosong. Kedua, uji koeksistensi radio dilakukan dengan menjalankan penangkapan CSI, koneksi *station* ke *access point*, dan pengiriman UDP secara serentak pada modul penerima. Laju CSI aktual dan kehilangan paket kemudian diukur, termasuk ketika *streaming* audio dari mikrofon diaktifkan. Ketiga, laju pencuplikan aktual diukur sebagai dasar penetapan pita Doppler (Subbab 3.7.1). Keluaran tahap ini adalah laporan karakterisasi sinyal sebagai bahan G0.",
     "Dua modul ESP32-S3 disiapkan dengan *firmware* `esp32-csi-node` dari RuView [28]; node pemancar TX memancarkan paket *beacon* ESP-NOW, sedangkan node penerima RX mengekstrak CSI dari paket tersebut melalui mode *promiscuous* dan mengemasnya dalam bingkai UDP format ADR-018. Empat uji dilakukan pada tahap ini tanpa partisipan. Pertama, uji meja kerja dan garis pandang langsung (*benchtop and line-of-sight*) memverifikasi bahwa seluruh 56 *subcarrier*, yaitu 52 data dan 4 pilot, terbaca stabil pada konfigurasi baku jarak 1 meter antarmodul. Kedua, uji Delta-CSI (Subbab 3.8.1) dilakukan untuk mengetahui apakah pola CSI saat bergerak terpisah dari kondisi diam dan ruang kosong. Ketiga, uji koeksistensi radio dilakukan dengan menjalankan penangkapan CSI, koneksi *station* ke *access point*, dan pengiriman UDP secara serentak pada modul penerima, termasuk ketika *streaming* audio dari mikrofon diaktifkan, lalu laju CSI aktual dan kehilangan paket diukur. Keempat, laju pencuplikan aktual diukur sebagai dasar penetapan pita Doppler (Subbab 3.7.1). Keluaran tahap ini adalah laporan karakterisasi sinyal sebagai bahan G0."),

    ("3.2.2 T1 separabilitas jadi rintisan",
     "G1 menguji separabilitas awal 2\u20133 pasang huruf tersebut dengan uji *nearest-centroid* sederhana yang rata-ratanya dihitung tanpa repetisi yang sedang diuji.",
     "Rintisan separabilitas 2\u20133 pasang huruf tersebut dijalankan dengan uji *nearest-centroid* sederhana yang rata-ratanya dihitung tanpa repetisi yang sedang diuji; hasilnya bukan gerbang, melainkan bahan penyetelan protokol, yaitu penambahan repetisi bagi pasangan yang rawan tertukar dan rencana pemangkasan bila G1 nantinya gagal (Tabel 3.6)."),

    ("3.2.3 T2 ADR-079 + backbone + G1",
     "*Dataset* direkam dengan kurang lebih 30 repetisi per isyarat per sesi disertai video tersinkron (Subbab 3.6). Alur pelatihan pada tahap ini berbentuk distilasi guru\u2013murid: tahap perekaman, penyaringan segmen, pelatihan guru, dan penyandingan data ditunjukkan pada Gambar 3.3, sedangkan pelatihan murid, pembanding, dan *deployment* ditunjukkan pada Gambar 3.4. Model guru YOLO26m-Pose menjalani pelatihan lanjutan pada data visual SIBI di layanan server GPU Kaggle memakai pipeline pelatihan YOLO26 yang telah terimplementasi pada repositori milik peneliti (Subbab 3.7.4), lalu kualitas *keypoint*-nya dievaluasi sebelum dipakai. Jendela CSI, label kelas dari anotasi protokol, dan deret pose guru diselaraskan berdasarkan penanda waktu untuk membentuk *dataset* murid; kemudian murid 1D-CNN dilatih dengan supervisi label dan deret pose guru (Subbab 3.7.5). Dua pembanding dilatih pada data yang sama, yaitu SVM dan murid ablasi tanpa supervisi guru. Setelah pelatihan, model terpilih dikuantisasi int8, di-*deploy* ke modul penerima, lalu waktu inferensi dan pemakaian memorinya diukur pada laju bingkai aktual. Keluaran T2 adalah *dataset* murid berlabel, model guru dan murid terlatih, serta laporan *deployment*; bila G2 gagal, cakupan dipangkas menjadi himpunan huruf yang pembeda CSI-nya paling kuat (Tabel 3.6).",
     "*Dataset* direkam dengan kurang lebih 30 repetisi per isyarat per sesi disertai video tersinkron melalui adaptasi skrip `scripts/collect-ground-truth.py` (ADR-079) dari RuView (Subbab 3.6). Alur pelatihan pada tahap ini berbentuk distilasi guru\u2013murid: tahap perekaman, penyaringan segmen, pelatihan guru, dan penyandingan data ditunjukkan pada Gambar 3.3, sedangkan pelatihan murid, pembanding, dan *deployment* ditunjukkan pada Gambar 3.4. Model guru YOLO26m-Pose menjalani pelatihan lanjutan pada data visual SIBI di layanan server GPU Kaggle memakai pipeline pelatihan YOLO26 yang telah terimplementasi pada repositori milik peneliti (Subbab 3.7.4), lalu kualitas *keypoint*-nya dievaluasi sebelum dipakai. Jendela CSI dan *ground truth* guru berupa label huruf serta deret pose 21 *keypoint* diselaraskan berdasarkan penanda waktu untuk membentuk *dataset* murid; kemudian murid ber-*backbone* WiFi-DensePose int8 dengan kepala 1D-CNN dilatih dengan supervisi label dan replikasi deret pose guru (Subbab 3.7.5). Dua pembanding dilatih pada data yang sama, yaitu SVM dan murid ablasi tanpa supervisi guru. Setelah pelatihan, model terpilih dikuantisasi int8, di-*deploy* ke modul penerima, lalu waktu inferensi dan pemakaian memorinya diukur pada laju bingkai aktual. Keluaran T2 adalah *dataset* murid berlabel, model guru dan murid terlatih, serta laporan *deployment*; G1 menilai akurasi klasifikasi 24 huruf statis serta J dan Z pada skema dalam sesi yang direkam di ruang kelas mitra, dan bila G1 gagal, cakupan dipangkas menjadi himpunan huruf yang pembeda CSI-nya paling kuat (Tabel 3.6)."),

    ("3.2.4 T3 posisi + G2",
     "Model mudah mengalami *overfitting* pada orang dan ruang tempat data latih direkam [39] sehingga model diuji lintas sesi, lintas partisipan, lintas ruang, dan pada satu pengguna baru tanpa pelatihan ulang (Subbab 3.7.6). Strategi lintas domain Widar3.0 [40] dijadikan acuan tanpa mengasumsikan hasil yang sama pada isyarat SIBI. Bila G3 gagal, cakupan menjadi personalisasi per pengguna yang memerlukan data latih singkat dari setiap pengguna, dan perubahan itu dilaporkan sebagai temuan.",
     "Model mudah mengalami *overfitting* pada orang dan ruang tempat data latih direkam [39] sehingga model diuji lintas sesi, lintas partisipan, lintas ruang, pada variasi posisi berdiri dan duduk, serta pada satu pengguna baru tanpa pelatihan ulang (Subbab 3.7.6). Strategi lintas domain Widar3.0 [40] dijadikan acuan tanpa mengasumsikan hasil yang sama pada isyarat SIBI. G2 menilai ketahanan lintas pengguna dan posisi tersebut; bila G2 gagal, cakupan menjadi personalisasi per pengguna yang memerlukan data latih singkat dari setiap pengguna, dan perubahan itu dilaporkan sebagai temuan."),

    ("3.2.5 T4 G3 + G4",
     "Model murid yang telah berjalan di modul dikemas menjadi purwarupa dua arah (Subbab 3.5) dengan mengaktifkan layanan ucapan awan pada kedua arah. Pengemasan menambahkan tombol tekan-untuk-bicara dan rotary encoder volume pada modul pengguna, pemetaan teks ke representasi SIBI, serta tampilan layar modul dan pemutaran audio pada *speaker*. Selanjutnya dilakukan uji operasional, uji jalur ucapan, uji cakupan kamus, uji kegunaan dengan 3\u20135 pengguna, dan penilaian validator (Subbab 3.8). G4 menilai kelengkapan data uji dan persetujuan validator atas kewajaran keluaran.",
     "Model murid yang telah berjalan di modul dikemas menjadi purwarupa dua arah (Subbab 3.5) dengan mengaktifkan layanan ucapan pada kedua arah. Pengemasan memanfaatkan antarmuka pada modul penerima, yaitu tombol tekan-untuk-bicara, rotary encoder volume, layar, dan *speaker*, serta menambahkan pemetaan teks ke representasi SIBI. Selanjutnya dilakukan uji operasional, uji jalur ucapan, dan uji cakupan kamus (Subbab 3.8); G3 menilai latensi terjemahan isyarat-ke-suara (TTS) dan suara-ke-visual (ASR) pada jalur utama maupun jalur lokal. Tahap ini ditutup uji penerimaan pengguna akhir dari kelompok sasaran, yaitu guru, siswa tunarungu, dan wali murid, penilaian validator, serta analisis biaya purwarupa; G4 menilai penerimaan tersebut, persetujuan validator atas kewajaran keluaran, dan hasil analisis biaya."),
]

EDITS_BAB3_B = [
    ("3.4 intro perangkat",
     "Perangkat keras penelitian disajikan pada Tabel 3.1. Dua modul ESP32-S3 berperan sebagai modul pemancar dan modul penerima, sedangkan modul ketiga direncanakan sebagai modul pengguna yang memuat layar, *speaker*, mikrofon, tombol tekan-untuk-bicara, dan rotary encoder volume. Pemakaian dua atau tiga modul ditetapkan sesuai hasil uji beban pada T0.",
     "Perangkat keras penelitian disajikan pada Tabel 3.1. Sepasang modul ESP32-S3 menjadi node penginderaan: node pemancar (TX) memancarkan paket *beacon* ESP-NOW dan node penerima (RX) mengekstrak CSI 56 *subcarrier* pada pita 2,4 GHz (IEEE 802.11b/g/n) dengan kanal 20 MHz dan antena tunggal 1T1R; node penerima sekaligus memuat antarmuka pengguna."),

    ("Tabel 3.1 baris modul",
     "| 1 | Modul ESP32-S3 | Papan pengembangan ESP32-S3 dengan PSRAM, varian yang direkomendasikan RuView [28] | 3 unit | Modul TX, modul RX, dan modul pengguna (dapat dipakai bergilir dengan cadangan) |",
     "| 1 | Modul ESP32-S3 | Papan pengembangan ESP32-S3 dengan PSRAM, varian yang direkomendasikan RuView [28]; 2,4 GHz 802.11b/g/n, kanal 20 MHz (56 *subcarrier*: 52 data + 4 pilot), 1T1R | 2 unit | Node TX (pemancar *beacon* ESP-NOW) dan node RX (penerima CSI dan antarmuka pengguna) |"),

    ("Tabel 3.1 baris layar",
     "| 2 | Layar modul | Layar SPI/TFT kecil (1,8\u20132,8 inci) [PERLU DATA: model final] | 1\u20132 unit | Tampilan representasi SIBI pada modul pengguna |",
     "| 2 | Layar modul | Layar SPI/TFT kecil (1,8\u20132,8 inci) [PERLU DATA: model final] | 1 unit | Tampilan teks dan representasi SIBI pada node RX |"),

    ("Tabel 3.1 baris AP",
     "| 7 | *Access point* | Router Wi-Fi 2,4 GHz dengan akses internet atau fitur hotspot laptop [PERLU DATA: pilihan final] | 1 unit | Seluruh modul berada pada satu kanal; akses internet menopang layanan ucapan awan |",
     "| 7 | *Access point* | Router Wi-Fi 2,4 GHz dengan akses internet atau fitur hotspot laptop [PERLU DATA: pilihan final] | 1 unit | Jembatan jaringan dan penjangkar kanal bagi server ucapan, bukan perangkat penginderaan; seluruh modul berada pada satu kanal |"),

    ("Tabel 3.2 baris Kaggle",
     "| 4 | Layanan server GPU Kaggle | Melatih model guru YOLO26m-Pose dan model murid CSI |",
     "| 4 | Layanan server GPU Kaggle | Melatih model guru YOLO26m-Pose dan murid CSI ber-*backbone* WiFi-DensePose |"),

    ("Tabel 3.2 sisip baris WiFi-DensePose",
     "| 6 | Python, scikit-learn, PyTorch | Ekstraksi fitur, pelatihan SVM dan murid 1D-CNN, serta evaluasi |\n| 7 | TensorFlow Lite Micro dan ESP-DL | Menjalankan murid int8 pada modul penerima |\n| 8 | faster-whisper | ASR Bahasa Indonesia cadangan pada server lokal dan pembanding jalur awan |\n| 9 | MMS-TTS-ind | TTS Bahasa Indonesia cadangan pada server lokal dan pembanding jalur awan |\n| 10 | Layanan TTS awan | Jalur utama sintesis pada arah pertama [PERLU DATA: layanan final hasil uji banding] |\n| 11 | Layanan ASR awan | Jalur utama pengenalan ucapan pada arah kedua [PERLU DATA: layanan final hasil uji banding] |\n| 12 | Kamus label-teks dan teks-isyarat | Dikembangkan sendiri sebagai bagian purwarupa; salinan kamus label-teks dimuat pada modul |",
     "| 6 | Model WiFi-DensePose terpralatih (ruvnet/wifi-densepose-pretrained dan ruvnet/wifi-densepose-mmfi-pose) [28] | Inisialisasi *backbone* murid CSI dan preseden pemetaan CSI ke *keypoint* |\n| 7 | Python, scikit-learn, PyTorch | Ekstraksi fitur, pelatihan SVM dan murid ber-*backbone* WiFi-DensePose, serta evaluasi |\n| 8 | ESP-DL dengan akselerasi ESP-NN (alternatif: TensorFlow Lite Micro) | Menjalankan murid int8 pada node RX |\n| 9 | faster-whisper | ASR Bahasa Indonesia cadangan pada server lokal dan pembanding jalur awan |\n| 10 | MMS-TTS-ind | TTS Bahasa Indonesia cadangan pada server lokal dan pembanding jalur awan |\n| 11 | Layanan TTS awan | Jalur utama sintesis pada arah pertama [PERLU DATA: layanan final hasil uji banding] |\n| 12 | Layanan ASR awan | Jalur utama pengenalan ucapan pada arah kedua [PERLU DATA: layanan final hasil uji banding] |\n| 13 | Kamus label-teks dan teks-isyarat | Dikembangkan sendiri sebagai bagian purwarupa; salinan kamus label-teks dimuat pada modul |"),

    ("3.5 sisip matriks arsitektur",
     "## 3.5 Perancangan Sistem\n\n### 3.5.1 Arsitektur Dua Arah",
     "## 3.5 Perancangan Sistem\n\nKomponen penyusun purwarupa SenseSIBI beserta spesifikasi dan fungsinya dirangkum pada Tabel XX, kemudian tiap subsistem diuraikan pada Subbab 3.5.1 sampai 3.5.4.\n\nTabel XX Matriks komponen arsitektur purwarupa\n\n| Komponen | Spesifikasi dan implementasi teknis | Fungsi utama |\n|---|---|---|\n| Node penginderaan TX/RX | Sepasang modul ESP32-S3, pita 2,4 GHz (IEEE 802.11b/g/n), kanal 20 MHz (56 *subcarrier*: 52 data + 4 pilot), antena tunggal 1T1R | Memancarkan *beacon* ESP-NOW dan mengekstrak CSI 56 *subcarrier* |\n| Firmware modul | *Firmware* `esp32-csi-node` (RuView) dengan bingkai UDP format ADR-018 [28] | Akuisisi CSI mode *promiscuous* dan pengemasan paket UDP |\n| Pembersih derau sinyal | Algoritma CSI-ratio terhadap rekam acuan kalibrasi (Subbab 2.3) | Mengeliminasi derau fase osilator lokal dan offset fase acak tanpa perangkat tambahan |\n| Jembatan jaringan / AP | *Router* Wi-Fi atau *hotspot* laptop dengan penjangkar kanal sama | Jembatan komunikasi data ke server ucapan; bukan perangkat penginderaan |\n| Model guru (pelatihan) | YOLO26m-Pose 21 *keypoint* pose tangan pada server GPU | Menuntun pelatihan model Wi-Fi melalui akuisisi tersinkron ADR-079 |\n| *Backbone* model tepi | WiFi-DensePose int8 (ruvnet/wifi-densepose-pretrained) dengan akselerasi ESP-NN/ESP-DL [28] | Ekstraksi fitur spasial sinyal CSI |\n| Kepala klasifikasi tepi | 1D-CNN terkuantisasi int8 pada modul ESP32-S3 | Inferensi 24 huruf statis serta gestur dinamis J dan Z tanpa kamera |\n| Mesin pemroses suara | Server lokal atau awan ASR dan TTS | Mengubah teks isyarat menjadi suara dan suara menjadi representasi SIBI |\n\n### 3.5.1 Arsitektur Dua Arah"),

    ("3.5.1 teks jalur TX beacon",
     "Pada jalur arah pertama, modul pemancar memancarkan bingkai bersama; gerak pengisyarat mengubah deret CSI pada modul penerima; model murid int8 berjalan pada modul dan menghasilkan label beserta skor keyakinan; label dipetakan menjadi teks Indonesia melalui kamus label-teks kecil pada modul. Teks tampil di layar modul pengguna, lalu dikirim ke layanan TTS awan; audio hasil sintesis diputar pada *speaker* modul dengan volume yang diatur rotary encoder. Pada jalur arah kedua, tombol tekan-untuk-bicara pada modul pengguna mengaktifkan mikrofon; ucapan dikirim ke layanan ASR awan; teks hasil pengenalan tampil di layar, lalu dipetakan ke representasi SIBI dari aset yang tersimpan pada modul (Subbab 2.8).",
     "Pada jalur arah pertama, node pemancar memancarkan paket *beacon* ESP-NOW; gerak pengisyarat mengubah deret CSI yang ditangkap node penerima melalui mode *promiscuous*; model murid int8 berjalan pada modul dan menghasilkan label beserta skor keyakinan; label dipetakan menjadi teks Indonesia melalui kamus label-teks kecil pada modul. Teks tampil di layar node penerima, lalu dikirim melalui *router* ke layanan TTS; audio hasil sintesis diputar pada *speaker* modul dengan volume yang diatur rotary encoder. Pada jalur arah kedua, tombol tekan-untuk-bicara pada node penerima mengaktifkan mikrofon; ucapan dikirim ke layanan ASR; teks hasil pengenalan tampil di layar, lalu dipetakan ke representasi SIBI dari aset yang tersimpan pada modul (Subbab 2.8)."),

    ("Gambar 3.5 simpul TX/RX/guru",
     '    TX["Modul TX<br/>(ESP-NOW)"]',
     '    TX["Node TX: beacon<br/>ESP-NOW"]'),
    ("Gambar 3.5 simpul RX",
     '    RX["Modul RX: CSI +<br/>inferensi murid int8"]',
     '    RX["Node RX: CSI promiscuous +<br/>inferensi murid int8 +<br/>antarmuka pengguna"]'),
    ("Gambar 3.5 simpul guru",
     '    Y26P["YOLO26m-Pose:<br/>17 keypoint COCO"]',
     '    Y26P["YOLO26m-Pose:<br/>21 keypoint pose tangan"]'),

    ("3.5.2 teks topologi",
     "Topologi jaringan purwarupa ditunjukkan pada Gambar 3.6. Seluruh perangkat, yaitu 2\u20133 modul dan server lokal laptop, terhubung ke satu *access point* pada kanal yang sama sehingga penangkapan CSI dan komunikasi data berjalan serentak (Subbab 2.4). *Access point* tersebut juga menyediakan akses internet yang menopang layanan ucapan awan pada kedua arah. Modul pemancar dan modul penerima berkomunikasi melalui ESP-NOW untuk bingkai bersama, modul penerima mengirim label dan skor melalui UDP sebagai telemetri riset, dan modul pengguna mengirim teks atau audio singkat ke layanan ucapan awan.",
     "Topologi jaringan purwarupa ditunjukkan pada Gambar 3.6. Seluruh perangkat, yaitu sepasang modul dan server lokal laptop, terhubung ke satu *access point* pada kanal yang sama sehingga penangkapan CSI dan komunikasi data berjalan serentak (Subbab 2.4). *Access point* tersebut berperan murni sebagai jembatan jaringan dan penjangkar kanal bagi server ucapan pada kedua arah, bukan sebagai perangkat penginderaan. Node pemancar memancarkan *beacon* ESP-NOW sebagai sumber bingkai CSI bagi node penerima, node penerima mengirim label dan skor melalui UDP sebagai telemetri riset serta meneruskan teks atau audio singkat ke layanan ucapan."),

    ("Gambar 3.6 blok diganti utuh",
     '    subgraph MODS["2\u20133 modul ESP32-S3 (baterai)"]\n        MA["Modul A (TX):<br/>pemancar ESP-NOW"]\n        MB["Modul B (RX):<br/>CSI + inferensi murid int8"]\n        MC["Modul C (pengguna):<br/>layar, speaker, mikrofon I2S,<br/>tombol, rotary"]\n    end',
     '    subgraph MODS["Sepasang modul ESP32-S3 (baterai)"]\n        MA["Node TX:<br/>pemancar beacon ESP-NOW"]\n        MB["Node RX: CSI + inferensi murid int8<br/>+ layar, speaker, mikrofon I2S,<br/>tombol, rotary (antarmuka pengguna)"]\n    end'),
    ("Gambar 3.6 tepi MC diganti MB",
     '    MC -- "teks hasil isyarat<br/>(arah 1)" --> TTSA\n    TTSA -- "audio hasil sintesis" --> MC\n    MC -- "audio ucapan<br/>(arah 2)" --> STTA\n    STTA -- "teks" --> MC',
     '    MB -- "teks hasil isyarat<br/>(arah 1)" --> TTSA\n    TTSA -- "audio hasil sintesis" --> MB\n    MB -- "audio ucapan<br/>(arah 2)" --> STTA\n    STTA -- "teks" --> MB'),

    ("3.5.3 jarak baku 1 m",
     "Jarak antarmodul, ukuran zona, dan penempatan modul pengguna ditetapkan pada T0 dan dicatat dalam metadata sesi (Tabel 3.6).",
     "Jarak antarmodul, dengan konfigurasi baku 1 meter pada tahap karakterisasi, ukuran zona, dan penempatan antarmuka pengguna ditetapkan pada T0 dan dicatat dalam metadata sesi (Tabel 3.6)."),

    ("3.6.1 kelompok sasaran pengguna uji",
     "pengguna uji mencoba purwarupa dua arah pada uji kegunaan.",
     "pengguna uji, yang direkrut dari kelompok sasaran yaitu guru, siswa tunarungu, dan wali murid, mencoba purwarupa dua arah pada uji kegunaan."),

    ("3.6.2 pasangan huruf dan G1",
     "dan pasangan huruf dengan konfigurasi tangan yang paling mirip ditetapkan sebagai bahan gerbang G1.",
     "dan pasangan huruf dengan konfigurasi tangan yang paling mirip ditetapkan sebagai bahan rintisan separabilitas dan pengujian G1."),

    ("3.7.4 struktur 21 keypoint",
     "sehingga kemampuan melatih guru pose tangan pada data visual SIBI telah terbukti sebelum penelitian ini dimulai.",
     "sehingga kemampuan melatih guru pose tangan pada data visual SIBI telah terbukti sebelum penelitian ini dimulai. Struktur keluarannya mengikuti standar 21 *keypoint* pose tangan, yaitu satu titik pergelangan tangan dan empat titik artikulasi pada setiap jari [42]."),

    ("3.7.4 guru penyedia ground truth",
     "Model guru dipakai sebagai penyedia deret *keypoint*, bukan sebagai sumber label; meskipun model pose tangan repositori peneliti juga memuat keluaran klasifikasi huruf, label kelas SIBI tetap berasal dari anotasi protokol *elisitasi*, yaitu kartu pemandu yang menentukan huruf pada setiap segmen (Subbab 3.6) sehingga makna huruf tidak bergantung pada dugaan model visi. Klasifikasi gerakan otomatis dari video menuntut pengklasifikasi temporal di atas deret *keypoint* dan berada di luar cakupan penelitian ini karena label kelas telah tersedia dari protokol.",
     "Selama akuisisi data, model guru berperan sebagai penyedia *ground truth*: deret 21 *keypoint* dan label huruf keluarannya direkam tersinkron dengan CSI mengikuti pola ADR-079, kemudian keduanya menjadi supervisi pelatihan murid. Kartu pemandu protokol *elisitasi* tetap menentukan huruf yang diperintahkan pada setiap repetisi (Subbab 3.6) sehingga label guru dapat dicocokkan dengan perintah protokol dan ketidaksesuaiannya tercatat sebagai segmen yang diperiksa. Klasifikasi gerakan otomatis dari video tanpa perintah protokol menuntut pengklasifikasi temporal di atas deret *keypoint* dan berada di luar cakupan penelitian ini karena perintah protokol telah tersedia."),

    ("3.7.5 target pelatihan",
     "Target pelatihan berupa label kelas, sedangkan deret pose guru menjadi supervisi tambahan yang melengkapi label.",
     "Target pelatihan berupa label huruf hasil *ground truth* guru, sedangkan deret pose guru menjadi supervisi distilasi yang melengkapi label."),

    ("3.7.5 arsitektur murid backbone",
     "Model murid 1D-CNN dilatih dengan PyTorch [70] pada layanan server GPU Kaggle memakai fungsi kerugian gabungan: kerugian klasifikasi kelas ditambah suku supervisi guru yang mengikat representasi internal murid pada deret pose guru.",
     "Model murid ber-*backbone* WiFi-DensePose int8 yang diinisialisasi dari ruvnet/wifi-densepose-pretrained [28] dengan kepala 1D-CNN dilatih dengan PyTorch [70] pada layanan server GPU Kaggle memakai fungsi kerugian gabungan: kerugian klasifikasi kelas ditambah suku supervisi guru yang mengikat representasi internal murid pada deret pose guru."),

    ("3.7.6 enam skema",
     "Kinerja diukur dengan lima skema pembagian data pada Tabel 3.3.",
     "Kinerja diukur dengan enam skema pembagian data pada Tabel 3.3."),

    ("Tabel 3.3 sisip skema posisi",
     "| 5 | Pengguna baru | Seluruh pengisyarat *dataset* | Satu pengguna baru tanpa pelatihan ulang | Kesiapan dipakai orang baru tanpa perekaman tambahan |",
     "| 5 | Pengguna baru | Seluruh pengisyarat *dataset* | Satu pengguna baru tanpa pelatihan ulang | Kesiapan dipakai orang baru tanpa perekaman tambahan |\n| 6 | Lintas posisi | Data latih posisi berdiri (atau sebaliknya) | Data uji posisi duduk | Ketahanan terhadap pergeseran posisi berdiri dan duduk |"),

    ("3.7.6 skema kedua sampai keenam",
     "Skema kedua sampai kelima mengukur ketahanan terhadap perubahan domain [39];",
     "Skema kedua sampai keenam mengukur ketahanan terhadap perubahan domain [39];"),

    ("3.7.8 runtime ESP-DL",
     "Model murid terpilih dikuantisasi int8 lalu dijalankan pada modul penerima melalui TensorFlow Lite Micro atau ESP-DL dengan penyangga pada PSRAM.",
     "Model murid terpilih dikuantisasi int8 lalu dijalankan pada modul penerima melalui ESP-DL dengan akselerasi ESP-NN dan penyangga pada PSRAM; TensorFlow Lite Micro menjadi runtime alternatif."),

    ("Gambar 3.7 simpul model",
     '    MOD["Model murid int8<br/>TFLM/ESP-DL: 26 kelas huruf,<br/>arena tetap di PSRAM"]',
     '    MOD["Model murid int8:<br/>backbone WiFi-DensePose +<br/>kepala 1D-CNN, 26 kelas"]'),

    ("3.8 intro pemetaan gerbang",
     "Uji Delta-CSI dan koeksistensi mendasari G0, uji *nearest-centroid* mendasari G1, uji klasifikasi mendasari G2 dan G3, serta uji kegunaan dan penilaian validator mendasari G4. Uji operasional, uji jalur ucapan, dan uji cakupan kamus melengkapi analisis tanpa menjadi syarat gerbang.",
     "Uji Delta-CSI dan koeksistensi mendasari G0, uji klasifikasi mendasari G1 dan G2, uji operasional dan uji jalur ucapan mendasari G3, serta uji kegunaan, penilaian validator, dan analisis biaya mendasari G4. Uji cakupan kamus melengkapi analisis tanpa menjadi syarat gerbang."),

    ("3.8.2 enam skema",
     "Uji klasifikasi pada kelima skema memakai metrik pada Subbab 2.10.",
     "Uji klasifikasi pada keenam skema memakai metrik pada Subbab 2.10."),

    ("3.8.3 langkah biaya",
     "4. Mengukur arus modul lengkap dengan alat ukur arus pada beberapa kondisi kerja, lalu menghitung estimasi ketahanan baterai.\n5. Menghitung laju deteksi palsu, latensi kedua arah, dan estimasi ketahanan baterai, lalu menganalisisnya terhadap indikator layak (Tabel 3.6).",
     "4. Mengukur arus modul lengkap dengan alat ukur arus pada beberapa kondisi kerja, lalu menghitung estimasi ketahanan baterai.\n5. Menghitung biaya purwarupa dari harga komponen serta perkiraan biaya layanan ucapan per jam pemakaian sebagai bahan analisis kelayakan adopsi.\n6. Menghitung laju deteksi palsu, latensi kedua arah, dan estimasi ketahanan baterai, lalu menganalisisnya terhadap indikator layak (Tabel 3.6)."),

    ("3.8.6 kelompok sasaran",
     "Uji kegunaan dengan 3\u20135 pengguna menelaah keterpakaian purwarupa sebagai alat bantu komunikasi kosakata terbatas pada skenario tugas terbimbing",
     "Uji kegunaan dengan 3\u20135 pengguna dari kelompok sasaran, yaitu guru, siswa tunarungu, dan wali murid, menelaah keterpakaian purwarupa sebagai alat bantu komunikasi kosakata terbatas pada skenario tugas terbimbing"),
]

EDITS_BAB3_C = [
    ("3.9 jadwal gerbang T1",
     "| 2 | T1 Kurasi alfabet manual SIBI dan kosakata tampilan, kalibrasi ruang, protokol, perizinan | | \u25a0 | \u25a0 | \u25a0 | | | | | | | | | | | G1 (M3) |",
     "| 2 | T1 Kurasi alfabet manual SIBI dan kosakata tampilan, kalibrasi ruang, protokol, perizinan | | \u25a0 | \u25a0 | \u25a0 | | | | | | | | | | | \u2014 |"),
    ("3.9 jadwal gerbang T2",
     "G2 (M6\u2013M7) |",
     "G1 (akhir M8) |"),
    ("3.9 jadwal gerbang T3",
     "G3 (M10) |",
     "G2 (akhir M10) |"),
    ("3.9 jadwal gerbang T4",
     "G4 (M12) |",
     "G3 (M11), G4 (akhir M12) |"),

    ("Tabel 3.6 baris 1 finalisasi G0",
     "| 1 | Kriteria G0 | Sebelum T0 | [PERLU DATA: ukuran keterpisahan Delta-CSI dan ambang kehilangan paket pada uji koeksistensi] |",
     "| 1 | Finalisasi ambang G0 | Sebelum T0 | [PERLU DATA: finalisasi ambang usulan G0 pada Tabel 3.4 bersama pembimbing] |"),
    ("Tabel 3.6 baris 2 pemangkasan",
     "| 2 | Tindakan bila G1 gagal kedua kalinya | Sebelum eksperimen | [PERLU DATA: tindakan, disepakati bersama pembimbing] |",
     "| 2 | Kriteria pemangkasan himpunan huruf | Sebelum G1 dinilai | [PERLU DATA: kriteria pemangkasan yang tidak memakai data uji] |"),
    ("Tabel 3.6 baris 7 ambang G1",
     "| 7 | Ambang G2 | Sebelum eksperimen | [PERLU DATA: ambang, disepakati bersama pembimbing] |",
     "| 7 | Ambang G1 | Sebelum eksperimen | [PERLU DATA: finalisasi ambang akurasi G1, disepakati bersama pembimbing] |"),
    ("Tabel 3.6 baris 8 tindakan G1",
     "| 8 | Kriteria pemangkasan himpunan huruf | Sebelum G2 dinilai | [PERLU DATA: kriteria pemangkasan yang tidak memakai data uji] |",
     "| 8 | Tindakan bila G1 gagal kedua kalinya | Sebelum eksperimen | [PERLU DATA: tindakan, disepakati bersama pembimbing] |"),
    ("Tabel 3.6 baris 16 ambang G2",
     "| 16 | Ambang G3 | Sebelum T3 | [PERLU DATA: ambang, disepakati bersama pembimbing] |",
     "| 16 | Ambang G2 | Sebelum T3 | [PERLU DATA: finalisasi ambang ketahanan lintas pengguna G2, disepakati bersama pembimbing] |"),
    ("Tabel 3.6 baris 17 personalisasi G2",
     "| 17 | Personalisasi bila G3 gagal | Sebelum T4 | [PERLU DATA: prosedur perekaman data latih pengguna] |",
     "| 17 | Personalisasi bila G2 gagal | Sebelum T4 | [PERLU DATA: prosedur perekaman data latih pengguna] |"),
    ("Tabel 3.6 baris 18 indikator G3",
     "| 18 | Indikator layak operasional | Sebelum T4 | [PERLU DATA: batas latensi ujung ke ujung tiap arah, batas laju deteksi palsu, dan ketahanan baterai minimum] |",
     "| 18 | Indikator layak operasional | Sebelum G3 dinilai | [PERLU DATA: finalisasi anggaran latensi G3, batas laju deteksi palsu, dan ketahanan baterai minimum] |"),
    ("Tabel 3.6 sisip baris biaya",
     "| 28 | Segmentasi huruf statis | Sebelum dipakai | [PERLU DATA: ambang energi dan panjang jendela tahan pose untuk huruf statis] |",
     "| 28 | Segmentasi huruf statis | Sebelum dipakai | [PERLU DATA: ambang energi dan panjang jendela tahan pose untuk huruf statis] |\n| 29 | Asumsi analisis biaya G4 | Sebelum G4 dinilai | [PERLU DATA: daftar harga komponen dan asumsi biaya layanan ucapan per jam] |"),

    ("Tabel 3.7 risiko baris 2 G2",
     "| 2 | Akurasi lintas partisipan atau lintas ruang rendah | Klaim pengguna baru tidak dapat dibuat | Personalisasi per pengguna (cadangan A); dilaporkan sebagai temuan |",
     "| 2 | Akurasi lintas partisipan, ruang, atau posisi rendah (G2 gagal) | Klaim pengguna baru tidak dapat dibuat | Personalisasi per pengguna (cadangan A); dilaporkan sebagai temuan |"),
    ("Tabel 3.7 risiko baris 4 cadangan C",
     "| 4 | Beban radio gabungan CSI, UDP, dan audio bermasalah | Purwarupa dua arah tidak stabil | Pemisahan peran modul menjadi modul CSI dan modul pengguna (cadangan C) |",
     "| 4 | Beban radio gabungan CSI, UDP, dan audio bermasalah | Purwarupa dua arah tidak stabil | Penambahan modul ketiga khusus antarmuka pengguna sehingga node RX hanya menangani CSI dan inferensi (cadangan C) |"),
    ("Tabel 3.7 risiko baris 10 pemangkasan G1",
     "Pemangkasan himpunan huruf pada G1\u2013G2 mengikuti kriteria Tabel 3.6; pasangan yang gagal dilaporkan sebagai temuan kelayakan |",
     "Pemangkasan himpunan huruf pada G1 mengikuti kriteria Tabel 3.6; pasangan yang gagal dilaporkan sebagai temuan kelayakan |"),
]

# Tabel 3.4 (kriteria gerbang) diganti utuh
TABEL_KRITERIA_LAMA = """### 3.8.8 Kriteria Gerbang Keputusan

Kriteria setiap gerbang beserta tindakan bila gagal disajikan pada Tabel 3.4. Kelayakan pada rumusan masalah ketiga ditinjau per dimensi, yaitu latensi kedua arah, cakupan kamus, keandalan operasional, persepsi pengguna, dan penilaian validator, bukan dari lolosnya G4 semata.

Tabel 3.4 Kriteria gerbang keputusan

| Gerbang | Waktu | Ukuran | Kriteria lolos | Tindakan bila gagal |
|---|---|---|---|---|
| G0 | Akhir M2 | Uji Delta-CSI dan koeksistensi | Pola CSI bergerak terpisah dari diam dan kosong; CSI, koneksi station, dan UDP berjalan serentak dengan kehilangan paket terkendali (ambang pada Tabel 3.6) | Penempatan modul diperbaiki satu kali; bila gagal lagi, jalur CSI dihentikan dan dilaporkan sebagai temuan karakterisasi |
| G1 | M3 | Separabilitas awal 2\u20133 pasang huruf mirip (*nearest-centroid*) | Repetisi huruf yang sama lebih dekat satu sama lain daripada ke huruf lain | Penempatan atau orientasi modul diubah satu kali; bila gagal lagi, tindakan mengikuti Tabel 3.6 |
| G2 | M6\u2013M7 | Akurasi skema dalam sesi | Jauh di atas peluang acak; ambang pada Tabel 3.6 | Cakupan dipangkas menjadi himpunan huruf yang pembeda CSI-nya paling kuat |
| G3 | M10 | Kinerja lintas partisipan dan lintas ruang | Di atas peluang acak; ambang pada Tabel 3.6 | Cakupan menjadi personalisasi per pengguna dan ditulis sebagai temuan |
| G4 | M12 | Kelengkapan uji dan persetujuan validator | Data uji operasional, jalur ucapan, cakupan kamus, dan kegunaan tercatat; validator menyetujui kewajaran keluaran | Hasil negatif tetap dilaporkan sebagai temuan kelayakan |"""

TABEL_KRITERIA_BARU = """### 3.8.8 Kriteria Gerbang Keputusan

Kriteria setiap gerbang beserta tindakan bila gagal disajikan pada Tabel 3.4. Kelayakan pada rumusan masalah ketiga ditinjau per dimensi, yaitu latensi kedua arah, cakupan kamus, keandalan operasional, penerimaan pengguna, penilaian validator, dan biaya, bukan dari lolosnya G4 semata. Ambang kuantitatif pada tabel berikut merupakan usulan awal yang difinalkan bersama pembimbing sebelum gerbang terkait dinilai; parameter yang menyertainya dihimpun pada Tabel 3.6.

Tabel 3.4 Kriteria gerbang keputusan

| Gerbang | Nama dan waktu | Ukuran | Kriteria lolos (ambang usulan) | Tindakan bila gagal |
|---|---|---|---|---|
| G0 | Meja kerja dan garis pandang langsung, akhir M2 | Akuisisi CSI 56 *subcarrier* pada jarak 1 m, uji Delta-CSI, dan koeksistensi radio | Seluruh 56 *subcarrier* terbaca stabil; laju bingkai sekurang-kurangnya 25 bingkai per detik; kehilangan paket tidak melampaui 5%; pola CSI bergerak terpisah dari diam dan kosong | Penempatan modul diperbaiki satu kali; bila gagal lagi, jalur CSI dihentikan dan dilaporkan sebagai temuan karakterisasi |
| G1 | Ruang terkontrol SLB, akhir M8 | Akurasi klasifikasi 24 huruf statis serta J dan Z pada skema dalam sesi yang direkam di ruang kelas mitra | Akurasi tanpa penolakan sekurang-kurangnya 50% atau sekitar 13 kali peluang acak 3,8%, dan melampaui pembanding SVM | Cakupan dipangkas menjadi himpunan huruf yang pembeda CSI-nya paling kuat, lalu G1 dinilai ulang |
| G2 | Variasi pengguna dan posisi, akhir M10 | Skema lintas partisipan, lintas ruang, lintas posisi, dan pengguna baru | Akurasi lintas pengguna sekurang-kurangnya dua pertiga akurasi dalam sesi dan tetap di atas peluang acak | Cakupan menjadi personalisasi per pengguna dan ditulis sebagai temuan |
| G3 | Integrasi pemrosesan suara dua arah, M11 | Latensi isyarat-ke-suara (TTS) dan suara-ke-visual (ASR) ujung ke ujung | Latensi arah pertama tidak melampaui 2 detik dan arah kedua tidak melampaui 3 detik pada jalur utama, atau 5 detik pada jalur lokal | Beralih ke server lokal; bila masih melampaui, dilaporkan sebagai temuan |
| G4 | Kelayakan operasional, akhir M12 | Penerimaan pengguna dari kelompok sasaran, penilaian validator, dan analisis biaya | Skor persepsi rata-rata sekurang-kurangnya 3,0 dari 5 pada seluruh dimensi; validator menyetujui kewajaran keluaran; analisis biaya lengkap | Hasil negatif tetap dilaporkan sebagai temuan kelayakan |"""

# Entri Daftar Pustaka baru (verifikasi 8 Nov 2026)
DP_BARU = [
    "[81] D. Wu, Y. Zeng, F. Zhang, and D. Zhang, \u201cWiFi CSI-based device-free sensing: From Fresnel zone model to CSI-ratio model,\u201d *CCF Transactions on Pervasive Computing and Interaction*, vol. 4, no. 1, pp. 88\u2013102, 2022, doi: 10.1007/s42486-021-00077-z.",
    "[82] K. Qian, C. Wu, Y. Zhang, G. Zhang, Z. Yang, and Y. Liu, \u201cWidar2.0: Passive human tracking with a single Wi-Fi link,\u201d in *Proc. 16th Annual Int. Conf. Mobile Systems, Applications, and Services (MobiSys)*, 2018, pp. 350\u2013361, doi: 10.1145/3210240.3210314.",
    "[83] J. Yang, H. Huang, Y. Zhou, X. Chen, Y. Xu, S. Yuan, H. Zou, C. X. Lu, and L. Xie, \u201cMM-Fi: Multi-Modal Non-Intrusive 4D Human Dataset for Versatile Wireless Sensing,\u201d in *Proc. 37th Conf. Neural Information Processing Systems (NeurIPS), Datasets and Benchmarks Track*, 2023, arXiv:2305.10345, doi: 10.48550/arXiv.2305.10345.",
]

LOG_GELOMBANG5 = """## Log Perubahan \u2014 Revisi 8 November 2026, gelombang 5 (Agent Brief v3: arsitektur teknis + gerbang G0\u2013G4 baru)

- Judul tetap SenseSIBI; asal-usul nama ditambahkan pada BAB I (*Sensing & Translation of SIBI*).
- BAB I: konteks dua arah diperjelas ke SLB dan sekolah inklusif; urgensi penginderaan nirsentuh dan bebas kamera (privasi + biaya) ditambahkan; paragraf baru hasil pra-penelitian YOLO26m-Pose (21 titik artikulasi, diskriminasi V\u2013U dan lintasan J\u2013Z) sebagai dasar tahap pengembangan tanpa kamera; keluaran guru (keypoint + label huruf) kini menjadi *ground truth* distilasi selama akuisisi (mengikuti brief; sebelumnya label hanya dari anotasi protokol \u2014 kartu pemandu kini berperan verifikasi konsistensi).
- BAB II: fisika zona Fresnel dan model CSI-ratio (derau fase osilator lokal + offset acak) ditambahkan di 2.3 dengan rujukan baru Wu dkk. 2022 dan Qian dkk. 2018 (Widar2.0); keluarga model WiFi-DensePose RuView (pretrained 82,3% triplet temporal; mmfi-pose pada dataset MM-Fi, rujukan baru Yang dkk. 2023) ditambahkan di 2.4 sebagai *backbone* murid; hasil pelatihan pra-penelitian guru (mAP50 0,8944/49 kelas; 0,9580 + akurasi huruf 97,6%/24 statis) dipindah tuntas ke 2.5; murid kini dua bagian: *backbone* WiFi-DensePose int8 + kepala 1D-CNN; peran AP diklarifikasi sebagai jembatan jaringan murni (bukan penginderaan, bukan 5 GHz multi-antena).
- BAB III: gerbang didefinisikan ulang sesuai brief \u2014 G0 meja kerja & LoS 1 m (verifikasi 56 *subcarrier*), G1 ruang kelas SLB (akurasi 24 statis + J dan Z), G2 variasi pengguna & posisi berdiri/duduk (skema pembagian ke-6 ditambahkan), G3 latensi TTS/ASR dua arah, G4 penerimaan (guru, siswa tunarungu, wali murid) + analisis biaya; uji separabilitas menjadi rintisan internal T1 (bukan gerbang); Tabel 3.4 kriteria gerbang memuat ambang kuantitatif usulan; matriks komponen arsitektur 8 baris ditambahkan sebagai Tabel 3.3 (tabel 3.3\u20133.7 lama bergeser ke 3.4\u20133.8); perangkat dikunci ke sepasang modul TX/RX (2,4 GHz, 20 MHz, 56 *subcarrier* 52 data + 4 pilot, 1T1R) dengan antarmuka pengguna pada node RX; firmware dinamai `esp32-csi-node`; alur akuisisi ADR-079 (`scripts/collect-ground-truth.py`) dan pra-pemrosesan CSI-ratio dirinci.
- Rujukan: 80 \u2192 83 (tiga rujukan terverifikasi ditambahkan: Wu dkk. 2022 CCFT PCI, Qian dkk. 2018 MobiSys, Yang dkk. 2023 NeurIPS D&B); seluruh sitasi dinomori ulang mengikuti urutan kemunculan pertama.
"""

EDITS_BAB1_B = [
    ("1.1 gerbang separabilitas -> G1-G2",
     "sehingga penelitian ini mengujinya melalui uji Delta-CSI dan gerbang separabilitas (Subbab 2.3 dan BAB III).",
     "sehingga penelitian ini mengujinya melalui uji Delta-CSI serta gerbang G1 dan G2 (Subbab 2.3 dan BAB III)."),

    ("1.1 supervisi label + pose",
     "Model murid belajar mengenali isyarat dari jendela CSI dengan supervisi tambahan deret pose guru, lalu berjalan sendiri pada modul tanpa kamera sehingga kamera dan model guru hanya aktif pada tahap akuisisi data dan pelatihan [41], [42].",
     "Model murid belajar mengenali isyarat dari jendela CSI dengan supervisi label dan deret pose guru, lalu berjalan sendiri pada modul tanpa kamera sehingga kamera dan model guru hanya aktif pada tahap akuisisi data dan pelatihan [41], [42]."),

    ("1.4 batasan 4 ground truth guru",
     "4. Kamera dan YOLO26m-Pose hanya dipakai sebagai model guru pada tahap akuisisi data dan pelatihan di laptop dan layanan server GPU Kaggle. Label kelas isyarat berasal dari anotasi protokol, bukan keluaran model guru, dan produk akhir tidak memakai kamera maupun citra.",
     "4. Kamera dan YOLO26m-Pose hanya dipakai sebagai model guru pada tahap akuisisi data dan pelatihan di laptop dan layanan server GPU Kaggle. Keluaran guru berupa deret 21 *keypoint* dan label huruf menjadi *ground truth* distilasi, kartu pemandu protokol menjadi alat verifikasi konsistensi anotasi, dan produk akhir tidak memakai kamera maupun citra."),
]

EDITS_BAB3_D = [
    ("Gambar 3.3 penyandingan",
     '    PAIR["Penyandingan berbasis waktu:<br/>jendela CSI + label kelas<br/>+ deret pose guru"]',
     '    PAIR["Penyandingan berbasis waktu:<br/>jendela CSI + ground truth guru<br/>(label huruf + deret pose)"]'),

    ("Gambar 3.4 dataset murid",
     '    SD["Dataset murid: jendela CSI,<br/>label kelas SIBI,<br/>supervisi deret pose guru"]',
     '    SD["Dataset murid: jendela CSI +<br/>ground truth guru: label huruf<br/>+ deret pose 21 keypoint"]'),

    ("Gambar 3.4 latih murid",
     '    STU["Latih murid 1D-CNN di server<br/>GPU Kaggle: kerugian klasifikasi<br/>+ suku supervisi guru"]',
     '    STU["Latih murid backbone WiFi-DensePose<br/>int8 + kepala 1D-CNN di GPU Kaggle:<br/>kerugian klasifikasi + suku supervisi guru"]'),

    ("3.7.5 tiga deret",
     "*Dataset* murid dibentuk dengan menyelaraskan tiga deret berdasarkan penanda waktu, yaitu jendela CSI hasil segmentasi, label kelas dari anotasi protokol, dan deret pose guru.",
     "*Dataset* murid dibentuk dengan menyelaraskan tiga deret berdasarkan penanda waktu, yaitu jendela CSI hasil segmentasi, label huruf dari *ground truth* guru, dan deret pose guru."),
]
