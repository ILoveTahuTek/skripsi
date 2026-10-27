# -*- coding: utf-8 -*-
"""Data peta literatur: 79 rujukan (Daftar Pustaka draft) dipetakan ke 9 kolom titik temu.
Sumber klaim: download/translator-sibi-revisi/Matriks-Literatur-dan-Bukti.md (verifikasi 24-25 Okt 2026).
Nomor [n] = nomor Daftar Pustaka Draft-Proposal-Translator-SIBI.md.
Kartu = (nomor, grup_matriks, penulis, tahun|None, venue_pendek, klaim_pendek, warna_peran, jenis)
"""

R_BLUE, R_GREEN, R_AMBER, R_PURPLE, R_CYAN, R_GRAY = "blue", "green", "amber", "purple", "cyan", "gray"

COLUMNS = [
    {
        "no": "01", "tanya": "Mengapa komunikasi tunarungu\u2013pendengar menjadi masalah?",
        "meta": "Konteks tunarungu, SIBI vs BISINDO, regulasi \u00b7 dipakai di \u00a71.1, 2.1",
        "kartu": [
            (1,  "A", "Mitchell & Karchmer", 2004, "Sign Language Studies", "90\u201395% anak tunarungu lahir dari orang tua pendengar (data AS)", R_BLUE, "Jurnal"),
            (2,  "A", "Mitchell & Karchmer", 2005, "Sign Language Studies", "Status pendengaran orang tua berkaitan dengan pemakaian isyarat siswa", R_BLUE, "Jurnal"),
            (3,  "A", "Lieberman dkk.", 2022, "Appl. Linguistics Review", "Orang tua pendengar butuh dukungan terstruktur untuk belajar bahasa isyarat", R_BLUE, "Jurnal"),
            (4,  "A", "Ritmeester dkk.", 2025, "J. Deaf Stud. Deaf Educ.", "Hambatan praktis yang dihadapi orang tua saat mempelajari isyarat", R_BLUE, "Jurnal"),
            (5,  "A", "Kemenko PMK", 2025, "Situs resmi", "\u00b1500 juru bahasa isyarat untuk \u00b11,92 juta tunarungu (1 : 3.840)", R_BLUE, "Dok. resmi"),
            (6,  "A", "Republik Indonesia", 2016, "UU No. 8/2016", "Hukum mengakui bahasa isyarat dan mewajibkan aksesibilitas komunikasi", R_BLUE, "Regulasi"),
            (7,  "A", "Rodr\u00edguez-Correa dkk.", 2023, "Frontiers in Education", "Tinjauan sistematis teknologi bantu komunikasi penyandang tunarungu", R_BLUE, "Jurnal"),
            (8,  "A", "BRIN", 2026, "Siaran pers", "Survei 26 provinsi: BISINDO 77,7%, SIBI 1,9%, campuran 14,9%", R_BLUE, "Dok. resmi"),
            (9,  "A", "Mursita", 2015, "INKLUSI", "91% dari 100 responden tunarungu memakai BISINDO sehari-hari", R_BLUE, "Jurnal"),
            (10, "A", "Kemendikbud", 2020, "Kamus SIBI Digital", "Acuan bentuk baku SIBI; SK 0190/P/1994; Surat 868/C/U/95", R_BLUE, "Kamus resmi"),
            (11, "A", "As Satillah dkk.", 2024, "AUDHI", "Murid SLB N Ogan Ilir memakai SIBI dalam pembelajaran harian", R_BLUE, "Jurnal"),
            (45, "A", "Depdikbud", 1994, "Kamus SIBI (edisi pertama)", "Dokumen baku pertama bentuk isyarat SIBI (verifikasi entri pustaka)", R_BLUE, "Kamus resmi"),
            (46, "A", "Stokoe", 2005, "J. Deaf Stud. Deaf Educ.", "Isyarat tersusun parameter: bentuk tangan, lokasi, gerak, orientasi, nonmanual", R_BLUE, "Jurnal"),
            (47, "A", "Ong & Ranganath", 2005, "IEEE TPAMI", "Survei klasik pengenalan isyarat bersensor dan berbasis visi", R_BLUE, "Jurnal"),
            (48, "A", "Nugraheni dkk.", 2023, "Jurnal Holistika", "Pemakaian SIBI/BISINDO oleh mahasiswa tunarungu di kampus", R_BLUE, "Jurnal"),
            (49, "A", "Malika & Berlianti", 2025, "Concept", "Pemakaian SIBI/BISINDO oleh siswa SLB Negeri Pembina Medan", R_BLUE, "Jurnal"),
        ],
        "celah": "Benang merah: SIBI hidup di jalur pendidikan formal (bukan keseharian) \u2014 purwarupa diarahkan ke konteks pendidikan, bukan pengganti BISINDO.",
    },
    {
        "no": "02", "tanya": "Apa yang sudah dicoba lewat kamera & kenapa kurang?",
        "meta": "SLR visi Indonesia, dataset, alat pelabelan riset \u00b7 dipakai di \u00a71.1, 2.2, 2.5, 2.8",
        "kartu": [
            (14, "E", "Sanjaya & Ilone", 2023, "IJCS", "Tinjauan SLR deep learning BISINDO berbasis citra", R_BLUE, "Jurnal"),
            (15, "E", "Dwijayanti dkk.", 2021, "IJACSA", "CNN mengenali 26 huruf + 10 angka BISINDO dari citra", R_BLUE, "Jurnal"),
            (16, "E", "Soekarta dkk.", 2024, "INSECT", "MediaPipe di Android; 24 huruf statis SIBI; akurasi 90,85%", R_BLUE, "Jurnal"),
            (17, "E", "Maulana dkk.", 2026, "DBESTI", "Android + TensorFlow Lite untuk alfabet SIBI statis (UAT 91,3%)", R_BLUE, "Jurnal"),
            (18, "E", "Sadeghzadeh dkk.", 2024, "ISWA", "MLMSign membuat SLR tahan perubahan pencahayaan \u2014 bukti kamera lemah pada cahaya", R_AMBER, "Jurnal"),
            (19, "F", "Bailenson", 2021, "Technology, Mind & Behavior", "Kamera terus menyala selama percakapan dikaitkan dengan kelelahan nonverbal", R_AMBER, "Jurnal"),
            (41, "E", "Jocher dkk.", 2026, "arXiv \u00b7 YOLO26", "YOLO26: keluarga model visi waktu nyata multi-tugas termasuk pose", R_CYAN, "arXiv"),
            (42, "E", "Ultralytics", None, "Dok. resmi \u00b7 tasks/pose", "YOLO26 pose terlatih COCO menghasilkan 17 keypoint tubuh", R_CYAN, "Dok. resmi"),
            (61, "E", "Sapkota dkk.", 2025, "arXiv", "Analisis YOLO26: efisiensi inferensi & kesiapan perangkat tepi", R_CYAN, "arXiv"),
            (60, "E", "Zheng dkk.", 2023, "ACM CSUR", "Survei estimasi pose berbasis pembelajaran dalam", R_CYAN, "Jurnal"),
            (62, "E", "Lugaresi dkk.", 2019, "arXiv \u00b7 MediaPipe", "Kerangka pipeline persepsi; dipakai skrip ADR-079 RuView", R_CYAN, "arXiv"),
            (51, "E", "Kindy dkk.", 2025, "Procedia CS", "Dataset video BISINDO tingkat kata beserta baseline", R_BLUE, "Prosiding"),
            (52, "E", "Wiguna & Rojali", 2025, "IJACSA", "Kalimat BISINDO dari video dengan 3D CNN-LSTM", R_BLUE, "Jurnal"),
            (53, "E", "Sebastian dkk.", 2025, "Procedia CS", "Pengenalan gestur tubuh sadar-spasial untuk BISINDO", R_BLUE, "Prosiding"),
            (73, "E", "Safrida dkk.", 2026, "Rabit", "Dataset citra alfabet SIBI 24 kelas (A\u2013Y); MobileNetV2 97,10%", R_BLUE, "Jurnal"),
        ],
        "celah": "Semua sistem visi Indonesia mengarah ke pengenalan atau kamus statis. Penelitian ini memakai kamera + pose YOLO26 hanya di jalur pelabelan riset \u2014 produk akhir tanpa kamera.",
    },
    {
        "no": "03", "tanya": "Bisakah isyarat dikenali tanpa kamera (Wi-Fi CSI)?",
        "meta": "Kelompok B \u2014 SLR dari CSI \u00b7 dipakai di \u00a72.6, 2.11",
        "kartu": [
            (21, "B", "Ma dkk.", 2018, "IMWUT \u00b7 SignFi", "276 isyarat ASL dari CSI Intel 5300; dalam sesi 98,01% (lab)", R_GREEN, "Jurnal"),
            (65, "B", "Shang & Wu", 2017, "MobiArch", "Sistem SLR tangguh dengan banyak perangkat Wi-Fi komersial", R_GREEN, "Prosiding"),
            (22, "B", "Ahmed dkk.", 2020, "PMC \u00b7 DF-WiSLR", "49 gestur dikenali tanpa perangkat yang dikenakan pengguna", R_GREEN, "Jurnal"),
            (66, "B", "Ahmed dkk.", 2021, "IAICT", "Model LSTM mengenali isyarat dari deret CSI", R_GREEN, "Prosiding"),
            (67, "B", "Qin dkk.", 2023, "Measurement \u00b7 WiASL", "Pengenalan tulisan ASL dengan perangkat Wi-Fi komersial", R_GREEN, "Jurnal"),
            (23, "B", "Baldeo dkk.", 2024, "IEEE TENCON", "Pengenalan Filipino Sign Language dari CSI", R_GREEN, "Prosiding"),
            (57, "B", "Hao dkk.", 2020, "Sensors \u00b7 Wi-SL", "Gestur halus dari CSI; perangkat 2TX\u20133RX 40 MHz 400 Hz", R_GREEN, "Jurnal"),
            (58, "B", "Sruthi dkk.", 2024, "Procedia CS \u00b7 HandFi", "Gestur tangan dari CSI Intel 5300 + router komersial", R_GREEN, "Prosiding"),
            (24, "B", "Zhang dkk.", 2020, "ACM TIST \u00b7 WiSign", "Kalimat ASL kontinu dari CSI komersial \u2014 batas atas klaim kebaruan kontinu", R_GREEN, "Jurnal"),
        ],
        "celah": "Celah riset: belum ada publikasi CSI untuk SIBI, apalagi purwarupa dua arah CSI + TTS/ASR Indonesia (penelusuran Scholar, Crossref, OpenAlex \u2014 Okt 2026).",
    },
    {
        "no": "04", "tanya": "Seberapa peka CSI & apa risiko lintas domain?",
        "meta": "Kelompok C \u2014 sensitivitas & generalisasi \u00b7 dipakai di \u00a72.3",
        "kartu": [
            (25, "C", "Ali dkk.", 2015, "MobiCom \u00b7 WiKey", "Ketukan tombol (skala sentimeter): deteksi 97,5%; kunci tunggal 96,4% (terkendali)", R_GREEN, "Prosiding"),
            (26, "C", "Mosleh dkk.", 2022, "IEEE Access", "Gerak napas (skala milimeter): pola 99,54% pada kanal cukup baik", R_GREEN, "Jurnal"),
            (20, "C", "Ma dkk.", 2019, "ACM CSUR", "Survei penginderaan CSI: amplitudo, fase, komponen Doppler", R_BLUE, "Jurnal"),
            (39, "C", "Chen dkk.", 2023, "ACM CSUR", "Model CSI mudah overfitting terhadap orang dan ruang; strategi lintas domain", R_AMBER, "Jurnal"),
            (40, "C", "Zhang dkk.", 2022, "IEEE TPAMI \u00b7 Widar3.0", "Generalisasi gestur lintas domain dengan profil kecepatan Doppler", R_PURPLE, "Jurnal"),
        ],
        "celah": "Implikasi rancangan: kinerja wajib diukur lintas partisipan & lintas ruang (gerbang G3); kalibrasi/personalisasi disiapkan sebagai mitigasi.",
    },
    {
        "no": "05", "tanya": "Bagaimana melatih model CSI tanpa label manual?",
        "meta": "Kelompok D \u2014 supervisi visi untuk data Wi-Fi \u00b7 dipakai di \u00a72.5",
        "kartu": [
            (63, "D", "Wang dkk.", 2019, "ICCV \u00b7 Person-in-WiFi", "Persepsi tubuh dari Wi-Fi dengan supervisi kamera", R_PURPLE, "Prosiding"),
            (64, "D", "Geng dkk.", 2023, "arXiv \u00b7 DensePose from WiFi", "Pemetaan permukaan tubuh dari Wi-Fi; jaringan visi sebagai guru", R_PURPLE, "arXiv"),
        ],
        "celah": "Celah: supervisi pose belum pernah dipakai untuk ground-truth isyarat SIBI pada CSI ESP32-S3 \u2014 dasar jalur pelabelan YOLO26 pada riset ini.",
    },
    {
        "no": "06", "tanya": "Bisakah semuanya berjalan di modul kecil?",
        "meta": "Kelompok H (platform) \u2014 ESP32-S3 & RuView \u00b7 dipakai di \u00a72.4, 3.2",
        "kartu": [
            (29, "H", "Espressif", 2026, "Datasheet S3 v2.2", "Dual-core LX7 240 MHz; SRAM 512 KB; PSRAM s.d. 8 MB; RX 88\u201391 mA", R_CYAN, "Dok. resmi"),
            (27, "H", "Espressif", None, "Repo esp-csi", "CSI didukung resmi seluruh seri ESP32 termasuk S3; 56 subcarrier HT20", R_CYAN, "Repo"),
            (28, "H", "ruvnet", None, "Repo RuView", "Firmware CSI + UDP, kalibrasi 600 frame + 8 anchor; CSI + STA + ESP-NOW serentak satu chip", R_CYAN, "Repo"),
            (59, "H", "Hernandez & Bulut", 2020, "WoWMoM", "Basis akuisisi CSI mandiri berbasis IoT pada keluarga ESP32", R_PURPLE, "Prosiding"),
            (30, "H", "Espressif", None, "Repo esp-nn", "Person detection 2.300 \u2192 54 ms di S3 (model int8 293,5 KB)", R_GREEN, "Repo"),
            (31, "H", "Espressif", None, "Repo esp-dl", "MobileNetV2 437,9 ms; pengenalan gestur tangan 69,2 ms di S3", R_GREEN, "Repo"),
            (72, "H", "Espressif", None, "Repo tflite-micro-esp", "Contoh TFLM: micro_speech 18,4 KB; person detection", R_GREEN, "Repo"),
        ],
        "celah": "Belum teruji (diukur pada T0): benchmark model CSI-isyarat di S3; koeksistensi streaming audio I2S + CSI; arus total modul berperiferal.",
    },
    {
        "no": "07", "tanya": "Bagaimana arah balik teks/ucapan \u2192 isyarat?",
        "meta": "Kelompok F \u2014 representasi balik & struktur SIBI \u00b7 dipakai di \u00a71.1, 2.2, 2.8",
        "kartu": [
            (12, "F", "Zikky & Akbar", 2019, "JST \u00b7 KASIBI", "Suara \u2192 STT \u2192 basis data \u2192 animasi peraga 3D; uji kelayakan 3,362/4", R_PURPLE, "Jurnal"),
            (13, "F", "Fatmawati dkk.", 2022, "TMJ \u00b7 OpenSIBI", "Google STT \u2192 API model Collada 3D; 50 kosakata (9 angka, 26 huruf, 15 kata)", R_PURPLE, "Jurnal"),
            (50, "F", "Rodhiyah & Wulandari", 2024, "INTECOMS", "Aplikasi mobile pembelajaran dasar isyarat SIBI", R_PURPLE, "Jurnal"),
            (76, "F", "Sagawa & Takeuchi", 2002, "ACM Multimedia", "Sistem pengajaran JSL: pengenalan + pembangkitan isyarat (dua arah)", R_PURPLE, "Prosiding"),
            (74, "F", "Rakun dkk.", 2015, "IEEE TIME-E", "Kata berinfleksi SIBI dikenali dengan HMM \u2014 bukti struktur kata jadian SIBI", R_BLUE, "Prosiding"),
            (75, "F", "Anggraini dkk.", 2019, "ICEEI", "Komponen gestur kata berinfleksi SIBI dianalisis lebih lanjut", R_BLUE, "Prosiding"),
            (43, "F", "Picron dkk.", 2024, "Springer (bab buku)", "Penerjemahan mesin bahasa isyarat penuh masih masalah terbuka (metadata)", R_AMBER, "Buku/bab"),
            (44, "F", "Hakozaki dkk.", 2025, "ACM ASSETS", "Avatar JSL dengan mouthing: isu nonmanual kelas satu (metadata)", R_AMBER, "Prosiding"),
        ],
        "celah": "Konsekuensi MVP: arah kedua = kamus kata-level + fallback ejaan jari (26 huruf, angka 1\u20139) mengikuti preseden OpenSIBI \u2014 bukan tata bahasa penuh.",
    },
    {
        "no": "08", "tanya": "Dari mana suara Bahasa Indonesia (TTS/ASR)?",
        "meta": "Kelompok G \u2014 TTS & ASR Indonesia \u00b7 dipakai di \u00a72.7, 3.4",
        "kartu": [
            (38, "G", "hexgrad", None, "Model card \u00b7 Kokoro-82M", "8 bahasa tanpa Indonesia (82 juta parameter) \u2192 tidak dipakai; bukti disiplin pemilihan teknologi", R_AMBER, "Model card"),
            (34, "G", "Pratap dkk.", 2023, "arXiv \u00b7 MMS", "Skala teknologi ucapan ke 1.000+ bahasa termasuk Indonesia", R_GREEN, "arXiv"),
            (35, "G", "Meta AI", None, "Model card \u00b7 mms-tts-ind", "Checkpoint TTS Indonesia (VITS); CC-BY-NC 4.0; dapat dijalankan lokal", R_GREEN, "Model card"),
            (32, "G", "Radford dkk.", 2022, "arXiv \u00b7 Whisper", "ASR 100+ bahasa termasuk Indonesia; dilatih 5 juta jam data", R_GREEN, "arXiv"),
            (33, "G", "SYSTRAN", None, "Repo faster-whisper", "int8 \u00b12,9 GB VRAM; 13 menit audio \u2192 59 detik pada RTX 3070 Ti 8 GB", R_GREEN, "Repo"),
            (36, "G", "Google Cloud", None, "Dok. resmi \u00b7 TTS", "Suara id-ID Standard & Premium; Standard \u00b1US$4 per juta karakter", R_PURPLE, "Dok. resmi"),
            (37, "G", "Microsoft", None, "Azure AI Speech", "Suara id-ID-GadisNeural dan id-ID-ArdiNeural", R_PURPLE, "Dok. resmi"),
        ],
        "celah": "Keputusan final TTS/ASR ditetapkan pada T4 (Tabel 3.6); jalur utama = faster-whisper + MMS-TTS lokal dengan catatan lisensi nonkomersial.",
    },
    {
        "no": "09", "tanya": "Dengan metode & tolok ukur apa dibuktikan?",
        "meta": "Kelompok H (metode) \u00b7 dipakai di \u00a72.3, 2.6, 2.10, 3.8",
        "kartu": [
            (68, "H", "Cortes & Vapnik", 1995, "Machine Learning", "SVM margin maksimum \u2014 kandidat klasifikasi data kecil", R_GRAY, "Jurnal"),
            (69, "H", "Mountrakis dkk.", 2011, "ISPRS", "SVM terbukti kuat pada dataset kecil \u2014 alasan pemilihan baseline", R_GRAY, "Jurnal"),
            (70, "H", "Kiranyaz dkk.", 2021, "MSSP", "1D-CNN untuk deret waktu \u2014 kandidat arsitektur model CSI", R_GRAY, "Jurnal"),
            (71, "H", "Chow", 1970, "IEEE TIT", "Pertukaran galat\u2013penolakan optimal \u2014 dasar ambang penolakan", R_GRAY, "Jurnal"),
            (54, "H", "Cai dkk.", 2024, "Sensors", "Amplitudo dan fase CSI saling melengkapi sebagai fitur", R_GRAY, "Jurnal"),
            (55, "H", "Nyquist", 1928, "Trans. AIEE", "Kriteria pencuplikan \u2014 menentukan laju akuisisi pita Doppler", R_GRAY, "Jurnal"),
            (56, "H", "Shannon", 1949, "Proc. IRE", "Kapasitas kanal dalam derau \u2014 dasar teoretis kanal nirkabel", R_GRAY, "Jurnal"),
            (77, "H", "Bowen dkk.", 2009, "Am. J. Prev. Med.", "Kerangka desain studi kelayakan \u2014 rancangan penelitian ini", R_GRAY, "Jurnal"),
            (78, "H", "Sokolova & Lapalme", 2009, "Inf. Processing & Mgmt.", "Analisis sistematis metrik klasifikasi (presisi, galat, F1 makro)", R_GRAY, "Jurnal"),
            (79, "H", "Likert", 1932, "Archives of Psychology", "Skala pengukuran sikap \u2014 dasar kuesioner uji kegunaan", R_GRAY, "Jurnal"),
        ],
        "celah": "Semua tolok ukur diukur dan dilaporkan; tidak ada angka kinerja yang dijanjikan di muka (disiplin klaim studi kelayakan).",
    },
]

TITLE = "Peta Literatur \u2192 Titik Temu Permasalahan"
SUBTITLE = "Purwarupa Penerjemah Dua Arah Isyarat SIBI Berbasis Wi-Fi CSI pada Modul ESP32-S3"
META_LINE = "79 rujukan terverifikasi (24\u201325 Okt 2026) \u00b7 nomor [n] = Daftar Pustaka Draft-Proposal-Translator-SIBI.md \u00b7 huruf grup (A\u2013H) = kelompok pada Matriks-Literatur-dan-Bukti.md"

MASALAH = ("MASALAH INTI", "Komunikasi dua arah tunarungu\u2013pendengar sulit terjadi tanpa kemampuan isyarat bersama; juru bahasa sangat langka.")
KESENJANGAN = [
    ("K1", "Juru bahasa isyarat terbatas: \u00b1500 untuk \u00b11,92 juta tunarungu"),
    ("K2", "Aplikasi SIBI yang ada satu arah dan kata-level (kamus/pembelajaran)"),
    ("K3", "Pengenalan berbasis kamera menuntut cahaya, garis pandang, dan kamera terus menyala"),
    ("K4", "CSI belum diterapkan pada SIBI; belum ada purwarupa dua arah CSI + TTS/ASR"),
]
TITIK_TEMU = ("TITIK TEMU PENELITIAN", "Purwarupa dua arah SIBI tanpa kamera: CSI + inferensi tepi pada 2\u20133 modul ESP32-S3, TTS/ASR Indonesia di server lokal")
STRIP_NOTE = "Sembilan kolom di bawah adalah pertanyaan-pertanyaan yang harus terjawab agar posisi penelitian berdiri \u2014 baca kiri \u2192 kanan mengikuti alur argumen; setiap kartu menunjukkan apa yang dibuktikan rujukan itu bagi pertanyaannya."

FOOTER_NOTES = [
    "Seluruh 79 rujukan berstatus DIVERIFIKASI pada 24\u201325 Oktober 2026 (halaman resmi/PDF/kode sumber dibaca langsung, metadata DOI dikonfirmasi via Crossref). Kualifikasi kedalaman verifikasi \u2014 PDF penuh, kode dibaca, metadata, entri pustaka \u2014 tercantum per rujukan pada Matriks-Literatur-dan-Bukti.md \u00a73.",
    "Angka akurasi dari literatur dikutip apa adanya untuk konteks sistem sumbernya (mis. SignFi = dalam sesi, perangkat multi-antena) dan tidak diproyeksikan ke kinerja ESP32-S3; klaim kebaruan penelitian dibatasi kombinatif karena WiSign telah mengenali kalimat ASL kontinu.",
    "Cara pakai: pilih kolom sesuai bagian proposal yang sedang dibaca (\u00a7 pada kepala kolom) \u2192 buka kartu \u2192 telusuri rujukan [n] lengkap di daftar pustaka draft. Kotak putus-putus kuning menandai batas bukti yang menjadi ruang kontribusi riset.",
]
