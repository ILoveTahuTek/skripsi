#!/usr/bin/env python3
"""Isi penanda [PERLU DATA]/[PERLU RUJUKAN] sempro DPJ-4 SIBI-CSI dengan data terverifikasi.

Suntingan diterapkan pada berkas _berkunci/ (sumber kebenaran, format kunci [@key]).
Penanda yang tetap: keputusan pembimbing, data pribadi/mitra, dan parameter rancangan Tabel 3.6.

Setiap penggantian divalidasi: old_string harus muncul tepat satu kali.
Jalankan: python3 /home/z/my-project/scripts/sempro-isi/edit_materi.py
"""
import pathlib
import sys

D = pathlib.Path("/home/z/my-project/materials/sempro/dpj4-sibi-csi/_berkunci")

EDITS = {
    "bab1-pendahuluan.md": [
        # E1: proporsi Indonesia - pernyataan jujur cakupan penelusuran
        (
            "Angka sebanding untuk Indonesia belum ditemukan dalam penelusuran penelitian ini "
            "[PERLU DATA: proporsi anak tunarungu dari orang tua pendengar di Indonesia] "
            "sehingga angka dari Amerika Serikat itu dipakai sebagai gambaran umum.",
            "Angka sebanding untuk Indonesia belum ditemukan dalam penelusuran penelitian ini "
            "(Google Scholar, Crossref, dan OpenAlex hingga Oktober 2026) sehingga angka dari "
            "Amerika Serikat itu dipakai sebagai gambaran umum.",
        ),
        # E2: SIBI dipakai di sekolah - mandat resmi + bukti lapangan
        (
            "Bagi keluarga yang anaknya bersekolah di jalur formal, SIBI merupakan sistem isyarat "
            "yang dipakai di sekolah [PERLU RUJUKAN: penggunaan SIBI dalam pembelajaran di sekolah "
            "luar biasa atau kurikulum pendidikan khusus].",
            "Bagi keluarga yang anaknya bersekolah di jalur formal, SIBI merupakan sistem isyarat "
            "yang dipakai di sekolah: melalui Surat Pemberitahuan Direktorat Pendidikan Dasar "
            "Nomor 868/C/U/95, semua SLB tunarungu yang menerapkan komunikasi total diwajibkan "
            "memakai sistem isyarat yang telah dibakukan [@kamussibidigital], dan penelitian di "
            "SLB Negeri Ogan Ilir menunjukkan murid tunarungu memakai SIBI dalam komunikasi "
            "sehari-hari di sekolah [@audhi2024].",
        ),
        # E3: latihan berulang + umpan balik + aplikasi SIBI + guru/kursus
        (
            "Isyarat dipelajari melalui gerak tubuh sehingga kemampuan berisyarat tidak cukup "
            "dibangun dengan membaca kamus atau menghafal gambar; pembelajar perlu memperagakan "
            "isyarat berulang kali [PERLU RUJUKAN: pentingnya praktik peragaan berulang dalam "
            "pembelajaran bahasa isyarat]. Latihan berulang itu lebih bermanfaat bila pembelajar "
            "segera mengetahui apakah gerakannya sesuai dengan isyarat target [PERLU RUJUKAN: "
            "peran umpan balik segera dalam latihan keterampilan gerak atau pembelajaran bahasa "
            "isyarat]. Dengan demikian, pembelajar membutuhkan sarana latihan yang cepat memberi "
            "umpan balik atas setiap peragaan isyarat. Sarana yang ditelusuri dalam penelitian ini "
            "masih terbatas untuk kebutuhan tersebut [PERLU DATA: aplikasi atau video belajar SIBI "
            "yang tersedia beserta bentuk umpan baliknya]. Pendampingan oleh guru atau kursus SIBI "
            "belum tentu tersedia bagi keluarga [PERLU DATA: ketersediaan guru atau kursus SIBI "
            "bagi keluarga dan calon guru].",
            "Isyarat dipelajari melalui gerak tubuh sehingga kemampuan berisyarat tidak cukup "
            "dibangun dengan membaca kamus atau menghafal gambar; sebagaimana keterampilan gerak "
            "pada umumnya, kemampuan itu dibangun melalui latihan yang diulang [@sigrist2013]. "
            "Latihan berulang itu lebih bermanfaat bila pembelajar segera mengetahui apakah "
            "gerakannya sesuai dengan isyarat target karena umpan balik tambahan yang segera "
            "memungkinkan perbaikan pada repetisi berikutnya [@sigrist2013]. Dengan demikian, "
            "pembelajar membutuhkan sarana latihan yang cepat memberi umpan balik atas setiap "
            "peragaan isyarat. Sarana yang ditelusuri dalam penelitian ini masih terbatas untuk "
            "kebutuhan tersebut: aplikasi pembelajaran SIBI yang tersedia antara lain menyajikan "
            "materi dasar secara mobile [@intecom2024], memadukan materi dengan keluaran suara "
            "melalui OpenSIBI [@technomedia2022], atau berbentuk kamus digital berbasis suara "
            "yang memetakan kata ke isyarat [@zikky2019], sedangkan pemanfaatan pengenalan "
            "otomatis pada aplikasi SIBI yang ditelusuri masih terbatas mengenali huruf statis "
            "dari kamera [@dbesti2026]. Pendampingan oleh guru atau kursus SIBI belum tentu "
            "tersedia bagi keluarga: guru SLB memang menggunakan sistem isyarat baku "
            "[@kamussibidigital], tetapi kursus SIBI yang terjangkau bagi keluarga belum "
            "terdokumentasi dalam kajian ekosistem bahasa isyarat [@brin2026], sementara jumlah "
            "juru bahasa isyarat bersertifikat sangat terbatas [@kemenkopmk2025].",
        ),
        # E4: sarung tangan sensor + hambatannya
        (
            "Di antara pendekatan pengenalan isyarat, sensor yang dikenakan pada tangan dapat "
            "menangkap konfigurasi jari [PERLU RUJUKAN: pengenalan isyarat berbasis sarung tangan "
            "sensor atau sensor inersia], tetapi perangkatnya harus dipasang setiap kali berlatih "
            "[PERLU RUJUKAN: hambatan pemakaian sensor yang dikenakan dalam latihan isyarat].",
            "Di antara pendekatan pengenalan isyarat, sensor yang dikenakan pada tangan, seperti "
            "sarung tangan sensor dan sensor inersia, dapat menangkap konfigurasi jari [@ong2005], "
            "tetapi perangkatnya harus dikenakan dan dikalibrasi setiap kali berlatih "
            "[@ong2005], [@baldeo2024].",
        ),
        # E5: kepekaan kamera
        (
            "Pendekatan berbasis kamera menuntut pencahayaan dan sudut pengambilan gambar tertentu "
            "[PERLU RUJUKAN: kepekaan pengenalan isyarat berbasis kamera terhadap pencahayaan dan "
            "sudut pandang].",
            "Pendekatan berbasis kamera menuntut pencahayaan dan sudut pengambilan gambar tertentu "
            "karena perubahan pencahayaan menurunkan ketangguhan pengenalan [@mlmsign2024] dan "
            "pengenalan citra bergantung pada garis pandang kamera [@baldeo2024], [@ong2005].",
        ),
        # E6: cakupan penelusuran literatur (BAB I)
        (
            "Meskipun demikian, penelusuran literatur dalam penelitian ini [PERLU DATA: basis "
            "data, kata kunci, dan rentang tahun penelusuran literatur] belum menemukan publikasi "
            "yang memakai CSI untuk mengenali isyarat SIBI maupun untuk memberi umpan balik "
            "latihan kepada pembelajar bahasa isyarat.",
            "Meskipun demikian, penelusuran literatur penelitian ini, yang dilakukan pada Google "
            "Scholar, Crossref, dan OpenAlex hingga Oktober 2026 dengan kata kunci bahasa Inggris "
            '("Wi-Fi sensing", "channel state information", "sign language recognition", dan '
            '"gesture recognition") dan bahasa Indonesia ("SIBI", "BISINDO", "pengenalan '
            'isyarat", dan "bahasa isyarat"), belum menemukan publikasi yang memakai CSI untuk '
            "mengenali isyarat SIBI maupun untuk memberi umpan balik latihan kepada pembelajar "
            "bahasa isyarat.",
        ),
        # E7: resolusi spasial + spesifikasi SignFi/Wi-SL/HandFi
        (
            "Panjang gelombang Wi-Fi pada pita 2,4 GHz dan 5 GHz berkisar 6–12 cm sehingga, pada "
            "satu tautan antara dua node ESP32, perbedaan konfigurasi jari dan ekspresi wajah "
            "diasumsikan terlalu halus untuk dibedakan secara andal [PERLU RUJUKAN: batas "
            "resolusi spasial CSI terhadap gerak jari dan ekspresi wajah]. Keberhasilan SignFi "
            "dan penelitian sejenis dalam mengenali isyarat tangan tidak serta-merta berlaku pada "
            "konfigurasi ini [PERLU DATA: perangkat, jumlah antena, dan lebar pita pada SignFi, "
            "Wi-SL, dan HandFi]. Oleh karena itu, penelitian ini membatasi pengenalan pada "
            "lintasan lengan, tubuh atas, dan kepala.",
            "Panjang gelombang Wi-Fi pada pita 2,4 GHz dan 5 GHz berkisar 6–12 cm. Sistem CSI "
            "yang berhasil mengenali isyarat dan gestur tangan memakai perangkat riset dengan "
            "banyak antena, yaitu SignFi dengan NIC Intel 5300 dan tiga antena penerima "
            "[@signfi2018], Wi-SL dengan tiga antena penerima pada kanal 40 MHz dan laju cuplik "
            "400 Hz [@hao2020], serta HandFi dengan NIC Intel 5300 sebagai penerima dari router "
            "Wi-Fi komersial [@sruthi2024], sehingga keberhasilan mereka tidak serta-merta "
            "berlaku pada satu tautan antara dua node ESP32. Oleh karena itu, pada konfigurasi "
            "itu perbedaan konfigurasi jari dan ekspresi wajah diasumsikan terlalu halus untuk "
            "dibedakan secara andal, dan asumsi ini diperiksa pada uji Delta-CSI sebelum "
            "perekaman (BAB III); penelitian ini membatasi pengenalan pada lintasan lengan, "
            "tubuh atas, dan kepala.",
        ),
    ],
    "bab2-kajian-pustaka.md": [
        # E1: definisi bahasa isyarat
        (
            "Bahasa isyarat merupakan bahasa visual yang menyampaikan makna melalui gerak tangan, "
            "lengan, tubuh, dan ekspresi wajah [PERLU RUJUKAN: definisi bahasa isyarat].",
            "Bahasa isyarat merupakan bahasa visual yang menyampaikan makna melalui gerak tangan, "
            "lengan, tubuh, dan ekspresi wajah [@stokoe2005], [@ong2005].",
        ),
        # E2: karakteristik SIBI vs BISINDO
        (
            "SIBI dan BISINDO memiliki karakteristik yang berbeda [PERLU RUJUKAN: karakteristik "
            "SIBI dan perbedaannya dengan BISINDO].",
            "SIBI dan BISINDO memiliki karakteristik yang berbeda: SIBI merupakan sistem isyarat "
            "baku yang dikembangkan untuk keperluan pendidikan formal, sedangkan BISINDO "
            "berkembang secara alami di komunitas tunarungu [@brin2026], [@kamussibidigital]; "
            "kajian pada mahasiswa tunarungu [@nugraheni2023] dan pada siswa SLB [@malika2025] "
            "memerikan perbedaan pemakaian keduanya.",
        ),
        # E3: parameter fonologis
        (
            "perbedaan pada satu parameter saja dapat membedakan makna dua isyarat [PERLU "
            "RUJUKAN: parameter fonologis isyarat].",
            "perbedaan pada satu parameter saja dapat membedakan makna dua isyarat [@stokoe2005], "
            "[@ong2005].",
        ),
        # E4: kebutuhan belajar pembelajar pendengar SIBI
        (
            "Kebutuhan serupa diduga juga dialami pembelajar pendengar SIBI yang masuk melalui "
            "jalur pendidikan formal [PERLU DATA: kebutuhan belajar pembelajar pendengar SIBI di "
            "Indonesia, termasuk calon guru dan mahasiswa].",
            "Kebutuhan serupa diduga juga dialami pembelajar pendengar SIBI yang masuk melalui "
            "jalur pendidikan formal; kajian khusus tentang kebutuhan kelompok itu belum "
            "ditemukan dalam penelusuran literatur penelitian ini, tetapi kebutuhan pembelajar "
            "pendengar tercermin dari pengembangan aplikasi pembelajaran SIBI bagi masyarakat "
            "umum [@intecom2024], [@technomedia2022] dan dari pemanfaatan SIBI di SLB "
            "[@audhi2024].",
        ),
        # E5: umpan balik segera (2.2)
        (
            "Umpan balik yang segera memungkinkan pembelajar memperbaiki gerak pada repetisi "
            "berikutnya [PERLU RUJUKAN: peran umpan balik segera dalam latihan keterampilan gerak "
            "atau pembelajaran bahasa isyarat].",
            "Umpan balik yang segera memungkinkan pembelajar memperbaiki gerak pada repetisi "
            "berikutnya; dalam telaah pembelajaran motorik, umpan balik tambahan yang diberikan "
            "selama latihan terbukti mempercepat perolehan keterampilan gerak [@sigrist2013], dan "
            "para pendidik bahasa isyarat juga melihat potensi umpan balik berbasis teknologi "
            "dalam mendukung latihan [@hassan2026].",
        ),
        # E6: sistem latihan umpan balik + kepekaan kamera (2.2)
        (
            "Pengenalan isyarat berbasis kamera (Subbab 2.8) dapat menjadi dasar umpan balik "
            "otomatis [PERLU RUJUKAN: sistem latihan bahasa isyarat dengan umpan balik otomatis "
            "berbasis kamera atau sensor], tetapi pendekatan tersebut menuntut pencahayaan dan "
            "sudut pengambilan gambar tertentu [PERLU RUJUKAN: kepekaan pengenalan isyarat "
            "berbasis kamera terhadap pencahayaan dan sudut pandang].",
            "Pengenalan isyarat berbasis kamera (Subbab 2.8) dapat menjadi dasar umpan balik "
            "otomatis; gagasan itu sudah lama diwujudkan, misalnya sistem pembelajaran bahasa "
            "isyarat Jepang yang memadukan pengenalan isyarat dengan pembangkitan isyarat sebagai "
            "umpan balik latihan [@sagawa2002], dan dikembangkan lagi dalam sistem latihan bahasa "
            "dengan umpan balik pengenalan waktu nyata [@daniel2024], tetapi pendekatan tersebut "
            "menuntut pencahayaan dan sudut pengambilan gambar tertentu [@mlmsign2024], "
            "[@ong2005].",
        ),
        # E7: rasa diawasi
        (
            "Kehadiran kamera yang menyala diduga membuat pembelajar merasa diawasi, sedangkan "
            "rasa diawasi dapat memengaruhi kenyamanan dan kemauan untuk berlatih berulang [PERLU "
            "RUJUKAN: pengaruh rasa diawasi terhadap kenyamanan dan kemauan berlatih].",
            "Kehadiran kamera yang menyala diduga membuat pembelajar merasa diawasi, sedangkan "
            "rasa diawasi dapat memengaruhi kenyamanan dan kemauan untuk berlatih berulang: "
            "kehadiran pengamat diketahui memengaruhi perilaku dan kinerja (fasilitasi sosial) "
            "[@zajonc1965], dan paparan kamera yang berkelanjutan dikaitkan dengan kelelahan "
            "nonverbal serta tekanan penampilan diri [@bailenson2021].",
        ),
        # E8: Nyquist + laju pencuplikan RuView
        (
            "sesuai kriteria Nyquist [PERLU RUJUKAN: teorema pencuplikan Nyquist]. Laju "
            "pencuplikan node ESP32 pada konfigurasi RuView adalah [PERLU DATA: laju pencuplikan "
            "CSI node ESP32 pada konfigurasi RuView] dan diukur pada tahap replikasi (BAB III).",
            "sesuai kriteria Nyquist [@nyquist1928], [@shannon1949]. Firmware RuView membatasi "
            "pengiriman frame CSI paling sering setiap 20 ms, yang setara laju maksimum 50 frame "
            "per detik, menurut kode sumber firmware-nya [@ruview]; laju aktual pada konfigurasi "
            "penelitian diukur pada tahap replikasi (BAB III).",
        ),
        # E9: spesifikasi perangkat (2.3) + resolusi
        (
            "Sejumlah penelitian melaporkan pengenalan isyarat dan gestur tangan dari CSI "
            "[@signfi2018], [@hao2020], [@sruthi2024] dengan perangkat dan konfigurasi antena "
            "tertentu [PERLU DATA: perangkat, jumlah antena, dan lebar pita pada SignFi, Wi-SL, "
            "dan HandFi]. Penelitian ini tidak mengasumsikan kemampuan tersebut juga dimiliki "
            "perangkat yang digunakan. Dengan dua node ESP32, perbedaan konfigurasi jari dan "
            "ekspresi wajah diasumsikan terlalu halus untuk dibedakan secara andal [PERLU "
            "RUJUKAN: batas resolusi spasial CSI terhadap gerak jari dan ekspresi wajah] "
            "sehingga cakupan pengenalan dibatasi pada lintasan lengan, tubuh atas, dan kepala.",
            "Sejumlah penelitian melaporkan pengenalan isyarat dan gestur tangan dari CSI "
            "[@signfi2018], [@hao2020], [@sruthi2024] dengan perangkat riset multi-antena: "
            "SignFi memakai NIC Intel 5300 dengan tiga antena penerima [@signfi2018], Wi-SL "
            "memakai router TP-Link WDR4310 dengan dua antena pemancar dan tiga antena penerima "
            "pada kanal 40 MHz dengan laju cuplik 400 Hz [@hao2020], dan HandFi memakai NIC "
            "Intel 5300 sebagai penerima dari router Wi-Fi komersial [@sruthi2024]. Penelitian "
            "ini tidak mengasumsikan kemampuan tersebut juga dimiliki perangkat yang digunakan. "
            "Dengan dua node ESP32, perbedaan konfigurasi jari dan ekspresi wajah diasumsikan "
            "terlalu halus untuk dibedakan secara andal, dan asumsi tersebut diperiksa melalui "
            "uji Delta-CSI (BAB III) sehingga cakupan pengenalan dibatasi pada lintasan lengan, "
            "tubuh atas, dan kepala.",
        ),
        # E10: jumlah kandidat Kamus SIBI - pernyataan jujur
        (
            "Jumlah kandidat isyarat dalam *Kamus SIBI* yang lolos saringan separabilitas fisik "
            "adalah [PERLU DATA: perkiraan jumlah kandidat isyarat Kamus SIBI yang lolos "
            "saringan separabilitas fisik].",
            "Angka pasti jumlah kandidat tidak dapat dikutip karena belum ada publikasi yang "
            "menghitung proporsi kosakata *Kamus SIBI* yang dibedakan terutama oleh lintasan "
            "gerak; jumlah kandidat karena itu ditetapkan pada tahap kurasi T1 melalui penapisan "
            "butir demi butir terhadap *Kamus SIBI* bersama validator penutur tunarungu (Subbab "
            "3.6.2).",
        ),
        # E11: varian ESP32 (2.4)
        (
            "Varian papan yang digunakan dalam penelitian ini adalah [PERLU DATA: varian ESP32 "
            "yang dipakai, misalnya ESP32 DevKit atau ESP32-S3].",
            "Varian papan yang digunakan dalam penelitian ini adalah ESP32-S3, yaitu varian yang "
            "direkomendasikan dokumentasi RuView untuk node penangkap CSI [@ruview].",
        ),
        # E12: arti ADR (2.4)
        (
            "*Firmware* tersebut memakai format *frame* yang ditetapkan dalam dokumen ADR-018 "
            "RuView [PERLU DATA: kepanjangan dan arti ADR pada repositori RuView] dan "
            "mengirimkan data secara *streaming* melalui *User Datagram Protocol* (UDP).",
            "*Firmware* tersebut memakai format *frame* yang ditetapkan dalam dokumen ADR-018 "
            "RuView, yaitu ADR atau *architecture decision record* (catatan keputusan "
            "arsitektur) yang dipakai repositori tersebut untuk mendokumentasikan keputusan "
            "desain [@ruview], dan mengirimkan data secara *streaming* melalui *User Datagram "
            "Protocol* (UDP).",
        ),
        # E13: fitur biometrik mode privasi
        (
            "Mode privasi membuang fitur biometrik [PERLU DATA: fitur biometrik yang dibuang "
            "mode privasi RuView].",
            "Mode privasi menekan fitur biometrik berupa detak jantung, laju napas, dan estimasi "
            "pose agar tidak diterbitkan keluar dari server [@ruview].",
        ),
        # E14: definisi estimasi pose
        (
            "dari citra atau video [PERLU RUJUKAN: definisi estimasi pose manusia].",
            "dari citra atau video [@zheng2023].",
        ),
        # E15: teori SVM (2.6)
        (
            "*hyperplane* pemisah dengan margin terbesar antarkelas [PERLU RUJUKAN: teori "
            "Support Vector Machine].",
            "*hyperplane* pemisah dengan margin terbesar antarkelas [@cortes1995].",
        ),
        # E16: teori 1D-CNN (2.6)
        (
            "yang menerapkan konvolusi sepanjang satu sumbu [PERLU RUJUKAN: teori 1D-CNN untuk "
            "data deret waktu].",
            "yang menerapkan konvolusi sepanjang satu sumbu dan dirancang untuk data deret waktu "
            "[@kiranyaz2021].",
        ),
        # E17: penolakan/open-set
        (
            "atau bukan isyarat sama sekali [PERLU RUJUKAN: klasifikasi dengan opsi "
            "penolakan/open-set].",
            "atau bukan isyarat sama sekali; mekanisme penolakan (*reject option*) memang "
            "dilengkapi ke klasifikator agar keluaran berkeyakinan rendah tidak dipaksa menjadi "
            "kelas tertentu [@chow1970].",
        ),
        # E18: definisi studi kelayakan
        (
            "dijalankan sebelum dikembangkan lebih jauh [PERLU RUJUKAN: definisi studi "
            "kelayakan].",
            "dijalankan sebelum dikembangkan lebih jauh [@bowen2009].",
        ),
        # E19: metrik evaluasi
        (
            "dan *confusion matrix* per isyarat [PERLU RUJUKAN: metrik evaluasi klasifikasi].",
            "dan *confusion matrix* per isyarat [@sokolova2009].",
        ),
        # E20: skala Likert
        (
            "kuesioner skala Likert [PERLU RUJUKAN: skala Likert] dan dianalisis secara "
            "deskriptif tanpa statistik inferensial.",
            "kuesioner skala Likert [@likert1932] dan dianalisis secara deskriptif tanpa "
            "statistik inferensial.",
        ),
        # E21a: baris 1 tabel (Shang dan Wu)
        (
            "| 1 | Shang dan Wu (2017) [@shang2017] | Wi-Fi, beberapa perangkat | [PERLU DATA: "
            "bahasa isyarat yang dikenali] | Ya | Pengenalan bahasa isyarat yang tangguh |",
            "| 1 | Shang dan Wu (2017) [@shang2017] | Wi-Fi, beberapa perangkat | Tidak "
            "disebutkan (isyarat tangan dan lengan) | Ya | Pengenalan bahasa isyarat yang "
            "tangguh |",
        ),
        # E21b: baris 3 tabel (DF-WiSLR)
        (
            "| 3 | Ahmed dkk. (2020) [@ahmed2020] | Wi-Fi, tanpa perangkat yang dikenakan | "
            "[PERLU DATA: bahasa isyarat yang dikenali] | Ya | Pengenalan bahasa isyarat |",
            "| 3 | Ahmed dkk. (2020) [@ahmed2020] | Wi-Fi, tanpa perangkat yang dikenakan | "
            "Tidak disebutkan (49 gestur isyarat) | Ya | Pengenalan bahasa isyarat |",
        ),
        # E21c: baris 7 tabel (Dwijayanti = BISINDO)
        (
            "| 7 | Dwijayanti dkk. (2021) [@dwijayanti2021] | Citra; CNN | Bahasa isyarat di "
            "Indonesia [PERLU DATA: SIBI atau BISINDO] | Tidak | Pengenalan isyarat dari citra |",
            "| 7 | Dwijayanti dkk. (2021) [@dwijayanti2021] | Citra; CNN | BISINDO (huruf dan "
            "angka) | Tidak | Pengenalan isyarat dari citra |",
        ),
        # E21d: baris 11 tabel (SIBI kamera)
        (
            "| 11 | [PERLU RUJUKAN: penelitian pengenalan isyarat SIBI berbasis kamera atau "
            "sensor] | [PERLU DATA: sesuai rujukan] | SIBI | [PERLU DATA: sesuai rujukan] | "
            "Pengenalan isyarat SIBI |",
            "| 11 | Soekarta dkk. (2024) [@soekarta2024] | Citra; MediaPipe; Android | SIBI (24 "
            "huruf statis) | Tidak | Deteksi isyarat SIBI berbasis Android |",
        ),
        # E21e: baris 12 tabel (sistem latihan umpan balik)
        (
            "| 12 | [PERLU RUJUKAN: sistem latihan bahasa isyarat dengan umpan balik otomatis "
            "berbasis kamera atau sensor] | Kamera atau sensor | [PERLU DATA: sesuai rujukan] | "
            "[PERLU DATA: sesuai rujukan] | Latihan isyarat dengan umpan balik otomatis |",
            "| 12 | Sagawa dan Takeuchi (2002) [@sagawa2002] | Kamera | Bahasa isyarat Jepang | "
            "Tidak | Pembelajaran isyarat dengan pengenalan dan pembangkitan isyarat |",
        ),
        # E21f: baris 13 tabel (sarung tangan sensor)
        (
            "| 13 | [PERLU RUJUKAN: pengenalan isyarat berbasis sarung tangan sensor atau sensor "
            "inersia] | Sensor yang dikenakan pada tangan | [PERLU DATA: sesuai rujukan] | Ya | "
            "Pengenalan isyarat, termasuk konfigurasi jari |",
            "| 13 | Ong dan Ranganath (2005) [@ong2005] | Sensor yang dikenakan pada tangan dan "
            "kamera (survei) | Berbagai bahasa isyarat (survei) | Sebagian | Survei pengenalan "
            "isyarat bersensor dan berbasis visi |",
        ),
        # E22: verifikasi orientasi pembelajaran kelompok pertama
        (
            "Sasaran kelompok ini adalah pengenalan isyarat; orientasi pembelajaran belum "
            "ditemukan dalam penelusuran literatur penelitian ini [PERLU DATA: verifikasi apakah "
            "penelitian kelompok pertama memuat orientasi pembelajaran].",
            "Sasaran kelompok ini adalah pengenalan isyarat; orientasi pembelajaran tidak "
            "dijumpai pada keempat publikasi tersebut, yang seluruhnya menargetkan pengenalan.",
        ),
        # E23: narasi pembanding + hambatan sensor
        (
            "Selain ketiga kelompok tersebut, Tabel 2.2 memuat dua pembanding yang paling dekat "
            "dengan penelitian ini, yaitu penelitian pengenalan isyarat SIBI dan sistem latihan "
            "bahasa isyarat dengan umpan balik otomatis; rujukan keduanya masih perlu "
            "dilengkapi. Tabel 2.2 juga memuat pengenalan isyarat berbasis sensor yang dikenakan "
            "pada tangan sebagai pendekatan lain yang tidak memerlukan kamera. Pendekatan "
            "tersebut dapat menangkap konfigurasi jari, tetapi perangkatnya harus dipasang "
            "setiap kali berlatih [PERLU RUJUKAN: hambatan pemakaian sensor yang dikenakan dalam "
            "latihan isyarat].",
            "Selain ketiga kelompok tersebut, Tabel 2.2 memuat dua pembanding yang paling dekat "
            "dengan penelitian ini, yaitu penelitian pengenalan isyarat SIBI berbasis MediaPipe "
            "di Android [@soekarta2024] dan sistem latihan bahasa isyarat dengan umpan balik "
            "otomatis [@sagawa2002]. Tabel 2.2 juga memuat pengenalan isyarat berbasis sensor "
            "yang dikenakan pada tangan sebagai pendekatan lain yang tidak memerlukan kamera. "
            "Pendekatan tersebut dapat menangkap konfigurasi jari, tetapi perangkatnya harus "
            "dikenakan dan dikalibrasi setiap kali berlatih [@ong2005], [@baldeo2024].",
        ),
        # E24: cakupan penelusuran (BAB II)
        (
            "Dalam batas penelusuran literatur penelitian ini [PERLU DATA: basis data, kata "
            "kunci, dan rentang tahun penelusuran literatur], belum ditemukan penelitian yang "
            "mengenali isyarat SIBI dari CSI.",
            "Dalam batas penelusuran literatur penelitian ini, yang mencakup Google Scholar, "
            "Crossref, dan OpenAlex hingga Oktober 2026 dengan kata kunci bahasa Inggris maupun "
            "bahasa Indonesia (Subbab 1.1), belum ditemukan penelitian yang mengenali isyarat "
            "SIBI dari CSI.",
        ),
    ],
    "bab3-metodologi.md": [
        # E1: arti ADR (BAB III)
        (
            "Arti kode ADR adalah [PERLU DATA: kepanjangan dan arti ADR pada repositori RuView].",
            "ADR adalah singkatan dari *architecture decision record* (catatan keputusan "
            "arsitektur), yaitu format dokumentasi keputusan desain yang dipakai repositori "
            "RuView [@ruview].",
        ),
        # E2: baris ESP32 Tabel 3.1
        (
            "| 1 | ESP32 | [PERLU DATA: varian ESP32 yang dipakai, misalnya ESP32 DevKit atau "
            "ESP32-S3] | 2 unit (+1 cadangan) | Node TX dan node RX penangkap CSI |",
            "| 1 | ESP32-S3 | Papan pengembangan ESP32-S3, varian yang direkomendasikan RuView "
            "untuk node CSI [@ruview] | 2 unit (+1 cadangan) | Node TX dan node RX penangkap "
            "CSI |",
        ),
        # E3: laju pencuplikan (3.7.1)
        (
            "Laju pencuplikan CSI node ESP32 pada konfigurasi RuView adalah [PERLU DATA: laju "
            "pencuplikan CSI node ESP32 pada konfigurasi RuView]. Pita Doppler 1–60 Hz hanya "
            "terwakili bila laju pencuplikan sedikitnya 120 Hz (Subbab 2.3).",
            "Firmware RuView membatasi pengiriman frame CSI paling sering setiap 20 ms sehingga "
            "laju maksimumnya adalah 50 frame per detik [@ruview]; laju aktual pada konfigurasi "
            "penelitian diukur pada T0. Pita Doppler 1–60 Hz hanya terwakili bila laju "
            "pencuplikan sedikitnya 120 Hz (Subbab 2.3).",
        ),
        # E4: teori SVM/1D-CNN/SVM-kecil (3.7.4)
        (
            "SVM mencari batas pemisah antarkelas dengan margin terbesar [PERLU RUJUKAN: teori "
            "Support Vector Machine] dan dipilih sebagai pembanding dasar karena dapat dilatih "
            "pada *dataset* berukuran kecil [PERLU RUJUKAN: kesesuaian SVM untuk data latih "
            "berukuran kecil]. Model 1D-CNN menerapkan konvolusi sepanjang sumbu waktu deret "
            "fitur [PERLU RUJUKAN: teori 1D-CNN untuk data deret waktu] dan dipilih karena dapat "
            "mempelajari pola temporal langsung dari deret tersebut.",
            "SVM mencari batas pemisah antarkelas dengan margin terbesar [@cortes1995] dan "
            "dipilih sebagai pembanding dasar karena dapat dilatih pada *dataset* berukuran "
            "kecil [@mountrakis2011]. Model 1D-CNN menerapkan konvolusi sepanjang sumbu waktu "
            "deret fitur [@kiranyaz2021] dan dipilih karena dapat mempelajari pola temporal "
            "langsung dari deret tersebut.",
        ),
    ],
}


def main():
    total = 0
    for fname, edits in EDITS.items():
        p = D / fname
        t = p.read_text(encoding="utf-8")
        for i, (old, new) in enumerate(edits, 1):
            n = t.count(old)
            if n != 1:
                print(f"GAGAL {fname} suntingan #{i}: kemunculan = {n}")
                print(f"  potongan: {old[:90]}...")
                sys.exit(1)
            t = t.replace(old, new)
            total += 1
        p.write_text(t, encoding="utf-8")
        print(f"[ok] {fname}: {len(edits)} suntingan")
    print(f"Total {total} suntingan diterapkan.")


if __name__ == "__main__":
    main()
