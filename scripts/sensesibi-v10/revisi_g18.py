#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Revisi terarah v17 -> v18 (gelombang 18) sesuai paket perbaikan pemilik
(30 isu ISS-01..ISS-30 + temuan verifikasi sumber primer 14 Nov 2026).
Kaidah bahasa: skill sempro-mepet (bila->jika, tanpa em dash baru,
tanpa koma-sebelum-sehingga baru, signifikan selalu bersama uji statistik).
Semua suntingan berjangkar; setiap jangkar wajib ditemukan tepat 1 kali.
"""
from pathlib import Path

SRC = Path("/home/z/my-project/download/sensesibi-v10/Proposal-SenseSIBI-v17.md")
DST = Path("/home/z/my-project/download/sensesibi-v10/Proposal-SenseSIBI-v18.md")

s = SRC.read_text(encoding="utf-8")
log = []

def ganti(nama, lama, baru, n=1):
    global s
    hitung = s.count(lama)
    assert hitung == n, f"[{nama}] jangkar ditemukan {hitung}x (harusnya {n})"
    s = s.replace(lama, baru)
    log.append(nama)

# ============================================================
# E01 — Sampul: jenis dokumen + catatan penyusunan (ISS-30)
# ============================================================
ganti("E01a-jenis-dokumen",
"| Jenis dokumen | Proposal penelitian (seminar proposal), BAB I sampai III + Daftar Pustaka; revisi terarah dan aditif atas v16: kontrak masukan *encoder* dikunci, supervisi 24 huruf statis dan J/Z dipisahkan, persamaan pembaruan tetapan disatukan, *deployment* mengikuti Pilihan 1, arsitektur audio disatukan, kriteria gerbang diperkuat; 55 halaman (naik dari 49 pada v16) |",
"| Jenis dokumen | Proposal penelitian (seminar proposal), BAB I sampai III + Daftar Pustaka; revisi verifikasi sumber primer atas v17: audit artefak *encoder* (NUL-padding, keluarga csi-embed-v2, lupa EWC 32,97%, batasan SISO), himpunan *subcarrier* valid (LLTF/HT-LTF, `first_word_invalid`), formalisasi Jalur A/B1/B2 dan Pembanding C, mask efektif serta uji permutasi G0b, TTS MMS-TTS-ind sebagai kandidat utama operasional, latensi terpisah per arah, tata kelola data etik; 31 rujukan |")

ganti("E01b-catatan",
"> Catatan penyusunan: versi ini menyunting naskah v16 sebagai revisi terarah dan aditif atas evaluasi kritis; tidak ada bab yang ditulis ulang dan ruang lingkup sistem tidak berubah. Kontrak masukan *encoder* dikunci menjadi delapan fitur turunan per jendela satu detik dan diuji gerbang G0b; supervisi 24 huruf statis dipisahkan dari huruf gerak J dan Z; himpunan tetapan terlatih dirumuskan utuh pada Persamaan 2.15′ dengan modul temporal dua cabang; *deployment* mengikuti Pilihan 1 (kepala klasifikasi saja, kepala regresi sebagai supervisi tambahan); arsitektur audio disatukan dengan sintesis TTS di server lokal sebagai jalur utama (keputusan D3); kriteria gerbang G1 diperkuat; beban perekaman dihitung ke dalam protokol. Tiga keputusan terbuka, yaitu akhiran judul, model *deployment*, dan lokasi TTS, dicatat pada Tabel 3.7. Penanda [PERLU DATA] dan [PERLU VALIDASI] tetap menandai hal yang belum dapat ditetapkan; rincian perubahan per subbab ada pada Log Perubahan gelombang 17 di ujung naskah.",
"> Catatan penyusunan: versi ini menyunting naskah v17 sebagai revisi terarah atas paket perbaikan yang seluruh klaim eksternalnya telah diverifikasi langsung ke sumber primer pada 14 November 2026; tidak ada bab yang ditulis ulang dan ruang lingkup sistem tidak berubah. Temuan verifikasi dimasukkan sebagai bukti: audit artefak *encoder* (NUL-padding `model.safetensors`, keluarga `csi-embed-v2` dengan *standardizer* FP16, tingkat lupa EWC 32,97%, peringatan SISO), struktur *subcarrier* ESP32-S3 (52 LLTF atau 56 HT-LTF serta penanganan `first_word_invalid`), ketiadaan suara Indonesia pada Kokoro-82M v1.0 (sehingga MMS-TTS-ind menjadi kandidat utama operasional TTS), dan konteks tolok ukur ESP-DL 69,2 ms. Perbaikan metodologis meliputi: formalisasi Jalur A, Jalur B1/B2, dan Pembanding C; mask efektif gabungan (Persamaan 2.13a); uji permutasi G0b; koreksi tafsir *overlap* jendela 75% dan rentang T = 16; pemisahan latensi Arah 1 dan Arah 2 (Persamaan 3.3a dan 3.3b); segmentasi tiga fase (onset, tahan pose, lintasan dinamis); penghapusan rumus 1 − WER; pelaporan cakupan diterima dan akurasi selektif; penguatan etika (retensi video, persetujuan wali dan *assent*); serta rujukan TKT nasional Permenristekdikti No. 42/2016. Tiga rujukan baru ditambahkan, yaitu DF-WiSLR, Wi-SignFi, dan Permenristekdikti Nomor 42 Tahun 2016; nomor sitasi lama 1 sampai 28 dipertahankan tanpa penomoran ulang. Sembilan keputusan terbuka tetap dicatat pada Tabel 3.7 dan tidak diputuskan sepihak; rincian perubahan per subbab ada pada Log Perubahan gelombang 18 di ujung naskah.")

# ============================================================
# E02 — 1.1 par. 1: haluskan klaim demografi (ISS-28)
# ============================================================
ganti("E02-1.1-par1",
"Anak tunarungu hampir selalu lahir dari orang tua yang bisa mendengar. Sejak hari-hari pertama, komunikasi di rumah berjalan dengan dua bahasa yang tidak saling mengerti: orang tua berbicara dengan suara, anak menjawab dengan isyarat. Orang tua lalu harus mempelajari bahasa isyarat dari nol, padahal waktu dan kesempatan berlatih serba terbatas. Angkanya memang timpang. Di Indonesia ada sekitar 1,92 juta penyandang tunarungu, sementara juru bahasa isyarat hanya sekitar 500 orang [1], sehingga satu juru bahasa harus melayani hampir 4.000 orang. Untuk kebutuhan harian seperti menceritakan sakit atau bertanya kepada penjual di pasar, menunggu juru bahasa jelas bukan jalan keluar. Undang-Undang Nomor 8 Tahun 2016 sudah menjamin hak setiap penyandang disabilitas untuk berkomunikasi [2], tetapi tanpa alat bantu yang benar-benar terjangkau, jaminan itu berjalan lambat.",
"Sebagian besar anak tunarungu tumbuh dalam lingkungan keluarga penutur dengar yang belum menguasai bahasa isyarat sejak awal. Sejak hari-hari pertama, komunikasi di rumah kerap berjalan dengan dua bahasa yang belum saling menjembatani: orang tua berbicara dengan suara, sedangkan anak berkomunikasi dengan isyarat, sementara waktu dan kesempatan belajar bahasa isyarat bagi orang tua serba terbatas. Ketimpangan akses layanan juru bahasa juga masih lebar. Di Indonesia terdapat sekitar 1,92 juta penyandang tunarungu, sedangkan jumlah juru bahasa isyarat diperkirakan baru sekitar 500 orang [1], sehingga rasio ketersediaannya sangat terbatas. Untuk kebutuhan harian seperti menceritakan keluhan sakit atau berinteraksi di ruang publik, ketergantungan penuh pada juru bahasa manusia tidak realistis. Undang-Undang Nomor 8 Tahun 2016 telah menjamin hak akses komunikasi bagi penyandang disabilitas [2], namun perwujudannya membutuhkan alat bantu yang terjangkau secara biaya dan praktis dipakai sehari-hari.")

# ============================================================
# E03 — 1.1 par. 4: penelusuran + DF-WiSLR/Wi-SignFi (ISS-14, ISS-28)
# ============================================================
ganti("E03-1.1-par4",
"Untuk menghindari dua kendala itu, sinyal Wi-Fi membuka jalan lain tanpa kamera. Sinyal ini membawa informasi kanal bernama *Channel State Information* (CSI) [6]. Begitu tangan bergerak di antara pemancar dan penerima, jalur pantulan sinyal bergeser dan CSI berubah mengikuti pola gerakannya; perubahan itulah yang dibaca untuk mengenali gerak tanpa sensor yang dikenakan di tubuh. SignFi, contoh terkemukanya, mengenali 276 isyarat *American Sign Language* (ASL) dari CSI [7], dan CSI bahkan peka terhadap gerak halus sampai ke gerakan jari [6]. Penelusuran pada Google Scholar, Crossref, dan OpenAlex hingga Oktober 2026 belum menemukan satu pun penerapan CSI untuk isyarat SIBI.",
"Untuk menghindari dua kendala itu, sinyal Wi-Fi membuka jalan lain tanpa kamera melalui *Channel State Information* (CSI) [6]. Begitu tangan bergerak di antara pemancar dan penerima, jalur pantulan sinyal bergeser dan CSI berubah mengikuti pola gerakannya; perubahan itulah yang dibaca untuk mengenali gerak tanpa sensor yang dikenakan di tubuh. SignFi menunjukkan potensi CSI untuk mengenali 276 isyarat *American Sign Language* (ASL) [7], diikuti kajian pengenalan gestur statis dan dinamis pada DF-WiSLR [29] serta pendekatan multitugas pada Wi-SignFi [30], disertai berbagai studi kepekaan CSI hingga gerak jari [6]. Berdasarkan penelusuran sistematis pada Google Scholar, Crossref, dan OpenAlex hingga Oktober 2026 memakai kombinasi kata kunci bahasa Inggris dan Indonesia (*\"Wi-Fi CSI\"*, *\"sign language\"*, *\"SIBI\"*, *\"Sistem Isyarat Bahasa Indonesia\"*), belum ditemukan publikasi yang menerapkan Wi-Fi CSI secara khusus untuk pengenalan alfabet SIBI maupun purwarupa komunikasi dua arah berbasis ESP32-S3. Ketiadaan temuan ini dicatat sebagai hasil penelusuran basis data tersebut, bukan klaim kemutlakan di luar cakupan indeks.")

# ============================================================
# E04 — 1.1 par. 5: biaya BOM, hapus klaim "di bawah Rp350.000" (ISS-18)
# ============================================================
ganti("E04-1.1-par5",
"Perangkat yang dibutuhkan pun sederhana dan murah. Modul ESP32-S3, mikrokontroler seharga sekitar Rp150.000, sudah memiliki radio Wi-Fi 2,4 GHz dengan dukungan CSI resmi [8], [9]. Dua modul cukup untuk satu pasang: yang satu memancarkan sinyal, yang lain menangkapnya. Zona isyarat berada di antara keduanya. *Firmware* penangkap CSI yang teruji untuk modul ini tersedia pada platform terbuka RuView [10]. Biaya sepasang node lengkap diperkirakan di bawah Rp350.000, jauh lebih ringan daripada kamera ditambah komputer pengolah citra. Murah di sini bukan soal angka semata; harga yang terjangkau mengundang sekolah berani memasang alat ini di lebih dari satu ruang.",
"Dari sisi perangkat keras, modul ESP32-S3 yang memiliki radio Wi-Fi 2,4 GHz dengan dukungan API CSI resmi [8], [9] berharga sekitar Rp150.000 per modul penginderaan dasar, atau sekitar Rp300.000 untuk sepasang modul TX-RX sebelum penambahan layar, sensor audio, pengisi daya, baterai, dan *enclosure*; *firmware* penangkap CSI yang teruji tersedia pada platform terbuka RuView [10]. Rincian biaya purwarupa lengkap disusun melalui daftar komponen (*bill of materials*, BOM) aktual dan dievaluasi pada gerbang G4, alih-alih diasumsikan murah di muka. Dengan arsitektur yang terukur, sekolah berpeluang menguji kelayakan pemasangan alat bantu tanpa infrastruktur kamera yang mahal.")

# ============================================================
# E05 — 1.1 par. 6: alur dua arah presisi + kalimat model diselaraskan (ISS-01)
# ============================================================
ganti("E05-1.1-par6",
"Jawabannya, penelitian ini merancang purwarupa bernama SenseSIBI, singkatan dari *Sensing & Translation of SIBI*. Arah pertamanya berjalan dari siswa: ia mengisyaratkan huruf, modul menangkap pola CSI, model yang berjalan langsung di modul mengenalinya, teks muncul di layar, lalu dibunyikan sebagai suara. Arah kedua berjalan dari guru: ia menekan tombol lalu berbicara; ucapannya dikenali menjadi teks, lalu bentuk isyaratnya ikut tampil di layar. Model pengenal isyaratnya tidak dilatih dari nol. *Encoder* CSI terpralatih dari RuView [11] menjadi tulang punggungnya. Representasinya dibekukan, lalu dua kepala tugas dilatih di atasnya: satu kepala mengenali 26 kelas huruf, satu lagi memperkirakan 21 titik jari tangan. Model penglihatan YOLO26m-Pose yang sudah terlatih pada data citra SIBI milik peneliti berperan sebagai guru yang memberi label itu [12]. Kamera hanya dipakai guru saat data direkam; setelah kedua kepala terlatih, seluruh sistem bekerja tanpa kamera.",
"Jawabannya, penelitian ini merancang purwarupa bernama **SenseSIBI** (*Sensing & Translation of SIBI*). Arah pertamanya berjalan dari siswa: ia mengisyaratkan huruf, modul RX menangkap pola CSI, model klasifikasi tepi yang berjalan di modul mengenali label huruf, lalu label dikirim ke server lokal untuk pemetaan teks Indonesia, tampilan layar, dan sintesis suara yang diputar pada *speaker* modul RX. Arah kedua berjalan dari guru: ia menekan tombol tekan-untuk-bicara (*push-to-talk*, PTT) lalu berbicara; ucapannya ditranskripsikan oleh mesin pengenalan ucapan (*automatic speech recognition*, ASR), lalu dipetakan ke aset kamus kata SIBI beserta *fallback* ejaan jari pada layar aplikasi. Model pengenal isyaratnya tidak dilatih dari nol: *encoder* CSI terpralatih RuView [11] menjadi tulang punggungnya, tetapannya dibekukan, sedangkan adapter masukan (jika dipakai), modul temporal, dan dua kepala tugas dilatih di atasnya, yaitu kepala klasifikasi 26 kelas huruf dan kepala regresi 21 titik jari tangan. Model penglihatan YOLO26m-Pose yang terlatih pada data citra SIBI milik peneliti menjadi guru pemberi label itu [12]; kamera hanya menyala saat data direkam, dan setelah pelatihan selesai seluruh sistem bekerja tanpa kamera.")

# ============================================================
# E06 — 1.5.1: konsistensi tetapan terlatih (ISS-01)
# ============================================================
ganti("E06-1.5.1",
"Secara teoretis, penelitian ini menyumbang bukti awal tentang satu pertanyaan yang tajam: apakah *embedding* hasil pretraining kontrastif pada CSI masih informatif untuk gestur jari jika hanya dua kepala tugasnya yang dilatih.",
"Secara teoretis, penelitian ini menyumbang bukti awal tentang satu pertanyaan yang tajam: apakah *embedding* hasil *pretraining* kontrastif pada CSI masih informatif untuk gestur jari apabila tetapan *encoder* dibekukan dan hanya adapter masukan (jika dipakai), modul temporal, serta kedua kepala tugasnya yang dilatih.")

# ============================================================
# E07 — 2.2: persamaan (2.1) + struktur subcarrier ESP-IDF (ISS-11)
# ============================================================
ganti("E07-2.2-intro",
"Bentuk formalnya sederhana: pada kanal 20 MHz, tiap *subcarrier* ke-n membawa koefisien kanal kompleks",
"Bentuk formalnya pada kanal 20 MHz 802.11n menyatakan bahwa tiap *subcarrier* valid n anggota N~valid~ membawa koefisien kanal kompleks")

ganti("E07-2.2-follow",
"dengan n = 1, ..., 56, |h~n~(t)| amplitudo, φ~n~(t) fase, dan j satuan imajiner [6], [9]. Amplitudo dan fase inilah bahan mentah seluruh perhitungan pada bab-bab berikutnya.",
"dengan |h~n~(t)| amplitudo, φ~n~(t) fase, dan j satuan imajiner [6], [9]. Pada implementasi ESP32-S3 dalam ESP-IDF, struktur `wifi_csi_info_t` menyimpan tiap koefisien sebagai dua *byte* bertanda (imajiner lalu riil) menurut urutan *Long Training Field* (LTF): LLTF, HT-LTF, dan STBC-HT-LTF bergantung jenis paket [9]. Untuk kanal 20 MHz tanpa STBC, LLTF memuat 52 *subcarrier* efektif setelah mengecualikan *null/guard* dan empat *pilot*, sedangkan HT-LTF memuat 56 *subcarrier*; apabila tanda perangkat keras `first_word_invalid` bernilai benar, empat *byte* pertama (dua *subcarrier* awal) tidak valid dan wajib dibuang [9]. Himpunan indeks valid N~valid~, jenis paket, LTF yang dipilih, dan filter alamat MAC dibakukan serta diaudit pada tahap T0 sebelum perhitungan fitur dilakukan. Amplitudo dan fase inilah bahan mentah seluruh perhitungan pada bab-bab berikutnya.")

# ============================================================
# E08 — 2.2: persamaan (2.5) sebagai normalisasi baseline ruang (ISS-11)
# ============================================================
ganti("E08-2.2-2.5",
"dengan t~0~ waktu kalibrasi ruang, yaitu 600 bingkai bawaan RuView [10]. Rasio ini membuang tanggapan statis ruang sehingga yang tersisa adalah perubahan akibat gerak; sisa derau fase yang berjalan lambat diukur pada T0 lalu dilaporkan.",
"dengan t~0~ waktu kalibrasi ruang, yaitu 600 bingkai acuan bawaan RuView [10]. Berbeda dari teknik *CSI-ratio* antar-antena atau perkalian konjugat pada literatur [13] yang menekan *carrier frequency offset* (CFO) dan *sampling frequency offset* (SFO) secara langsung antarsaluran, Persamaan (2.5) berfungsi sebagai normalisasi relatif terhadap *baseline* statis ruang pada konfigurasi antena tunggal. Pembagian ini membuang tanggapan pantulan statis ruangan, tetapi tidak otomatis menghilangkan *phase drift* lambat yang berubah seiring waktu; oleh karena itu, kestabilan fase sisa serta perbandingan varian amplitudo-saja tetap diukur pada tahap T0 dan dilaporkan apa adanya.")

# ============================================================
# E09 — 2.3: selaras jumlah subcarrier (ISS-11)
# ============================================================
ganti("E09-2.3-56",
"Dukungan CSI tersedia resmi lewat repositori esp-csi; pada kanal 20 MHz, CSI memuat 56 *subcarrier* [9].",
"Dukungan CSI tersedia resmi lewat repositori esp-csi; pada kanal 20 MHz, bingkai CSI memuat 56 *subcarrier* pada HT-LTF dan 52 *subcarrier* efektif pada LLTF setelah penyaringan (Subbab 2.2) [9].")

# ============================================================
# E10 — 2.4: rujukan Persamaan 2.15' -> (2.15) (ISS-08)
# ============================================================
ganti("E10-2.4-rujukan-215",
"tetapan yang diperbarui mencakup adapter masukan (jika dipakai), modul temporal, dan kedua kepala tugas sebagaimana dirumuskan pada Persamaan 2.15′.",
"tetapan yang diperbarui mencakup adapter masukan (jika dipakai), modul temporal, dan kedua kepala tugas sebagaimana dirumuskan pada Persamaan (2.15).")

# ============================================================
# E11 — 2.4: sisip paragraf audit artefak primer 14 Nov 2026 (ISS-13)
# ============================================================
ganti("E11-2.4-audit",
"Parameter normalisasi masukan belum dipublikasikan kartu modelnya sehingga dicari pada artefak *checkpoint* saat audit T0 [PERLU VALIDASI: parameter normalisasi masukan pada artefak checkpoint].\n\nSatu angka pada kartu model itu perlu dibaca hati-hati.",
"Parameter normalisasi masukan belum dipublikasikan kartu modelnya sehingga dicari pada artefak *checkpoint* saat audit T0 [PERLU VALIDASI: parameter normalisasi masukan pada artefak *checkpoint*].\n\nAudit dokumentasi repositori RuView dan Hugging Face per 14 November 2026 menemukan dua hal teknis yang wajib diverifikasi pada tahap T0. Pertama, kartu model memuat dua keluarga berkas, yaitu `model.safetensors`/`model.rvf.jsonl` dan keluarga `csi-embed-v2` (`csi-embed-v2.safetensors`, `csi-embed-v2-int4.bin`, serta `csi-embed-v2.py` yang menyertakan *standardizer* FP16), sedangkan berkas `model.safetensors` tercatat memiliki *NUL-padding* pada *header* sehingga ditolak oleh `safetensors.torch.load_file` [10], [11]. Kedua, catatan teknis RuView secara eksplisit memperingatkan bahwa aliran CSI antena tunggal (SISO) 56 *subcarrier* pada ESP32 tidak menyimpan informasi spasial sehalus NIC multi-antena, dan percobaan awal estimasi sendi distal pada satu perangkat mendekati acak; angka triplet-temporal 82,3% juga hanya diukur pada satu ruangan, satu rekaman, dan dua node [10], [11]. Karena itu, audit T0 mencakup pemilihan keluarga berkas yang dimuat, verifikasi *standardizer*, serta pembatasan klaim ke kondisi terukur tersebut.\n\nSatu angka pada kartu model itu perlu dibaca hati-hati.")

# ============================================================
# E12 — 2.4: paragraf ketidaksesuaian -> Jalur A/B1/B2 + Pembanding C (ISS-02)
# ============================================================
ganti("E12-2.4-jalur",
"Ketidaksesuaian bentuk masukan menjadi temuan audit yang paling menentukan. Kartu model mencatat masukan delapan fitur turunan CSI pada laju 1 Hz, yaitu kehadiran, gerak, napas, detak jantung, varians fase, jumlah orang, deteksi jatuh, dan RSSI [11]. Jalur akuisisi penelitian ini, sebaliknya, menghasilkan 56 *subcarrier* pada 50 bingkai per detik [9], [10], sehingga *encoder* itu tidak dapat langsung diberi *subcarrier* mentah. Dua jalur penyelesaiannya disiapkan dan diputuskan setelah audit T0. Jalur pertama menghitung ulang delapan fitur turunan bawaan RuView dari bingkai CSI; jalur kedua melatih adapter masukan kecil yang memetakan jendela CSI ke ruang masukan *encoder*. Keduanya dinyatakan terbuka dengan penanda [PERLU VALIDASI] sampai audit selesai, dan riset ini tidak mengklaim kompatibilitas sebelum terverifikasi.",
"Ketidaksesuaian bentuk masukan menjadi risiko ilmiah utama penelitian ini. Kartu model mencatat masukan delapan fitur turunan CSI pada laju 1 Hz, yaitu kehadiran, gerak, napas, detak jantung, varians fase, jumlah orang, deteksi jatuh, dan RSSI [11], sedangkan jalur akuisisi ESP32-S3 menghasilkan N~valid~ *subcarrier* (52 pada LLTF atau 56 pada HT-LTF) pada laju target hingga 50 bingkai per detik [9], [10]. Karena delapan fitur lingkungan tersebut tidak dirancang untuk menangkap artikulasi jari, merangkum CSI menjadi delapan angka berisiko membuang informasi spasial tangan. Untuk membedakan efek representasi masukan dari efek *encoder*, penelitian ini memformalkan tiga rute evaluasi yang berbeda tujuannya. Jalur A (rekonstruksi delapan fitur bawaan) menghitung ulang secara deterministik delapan fitur RuView dari jendela CSI beserta *standardizer* resminya untuk menguji langsung daya pisah *checkpoint* θ~0~ tanpa pembelajaran ulang masukan. Jalur B (adapter konvolusi satu dimensi) memetakan jendela CSI mentah ke vektor delapan dimensi melalui dua objektif yang dipisahkan tegas: Jalur B1 (adapter rekonstruksi fitur) dilatih meminimalkan galat rekonstruksi terhadap delapan fitur Jalur A, sedangkan Jalur B2 (adapter terpandu tugas) dilatih langsung oleh kerugian tugas SIBI (Persamaan 2.14). Jika Jalur B2 berhasil sementara Jalur A gagal, kontribusi pemisahan kelas berasal dari adapter terlatih dan tidak boleh diklaim semata sebagai bukti kualitas representasi *pretraining* RuView. Pembanding C (*baseline* CSI temporal lebih kaya) ialah model temporal ringan yang membaca langsung spektrum amplitudo dan fase N~valid~ *subcarrier* tanpa penyempitan delapan fitur; pembanding ini menjaga agar keterbatasan informasi delapan fitur tidak keliru ditafsirkan sebagai ketidakmampuan CSI secara umum, sekaligus menegaskan bahwa kegagalan delapan fitur tidak dipulihkan sekadar dengan membuka bobot *encoder* lewat LoRA. Ketiga rute dinyatakan terbuka dengan penanda [PERLU VALIDASI] sampai audit T0 dan gerbang G0b selesai, dan penelitian ini tidak mengklaim kompatibilitas sebelum terverifikasi.")

# ============================================================
# E13 — 2.5: baseline trainable + EWC 32,97% (ISS-01, ISS-13)
# ============================================================
ganti("E13-2.5-baseline",
"Baseline penelitian ini membekukan *encoder* dan melatih hanya kedua kepala tugasnya. Alasannya metodologis: dengan *encoder* beku, kualitas *embedding* terpralatih untuk isyarat SIBI terbaca langsung dari kinerja kepala, sehingga sumbangan pretraining terpisah dari sumbangan penyetelan.",
"Baseline penelitian ini membekukan tetapan *encoder* (θ~encoder~ = θ~0~) dan melatih bersama adapter masukan (jika Jalur B dipilih), modul temporal, serta kedua kepala tugas sebagaimana dirumuskan pada Persamaan (2.15). Alasannya metodologis: dengan menjaga θ~0~ tetap beku di atas Jalur A dan membandingkannya terhadap Pembanding C, sumbangan representasi *pretraining* RuView terhadap tugas alfabet SIBI dapat diisolasi secara jujur, terpisah dari sumbangan penyetelan.")

ganti("E13-2.5-ewc",
"Pembanding ketiga ialah pelatihan lanjutan. Pelatihan sebagian membuka lapis terakhir saja, sedangkan pelatihan penuh membuka seluruh tetapan. Keduanya dijaga dengan EWC sebagaimana pretraining *encoder* melakukannya [11], dan keduanya dilaporkan berdampingan dengan hasil *encoder* beku. Ketiga skema itu (beku, beku plus LoRA, pelatihan lanjutan) diperlakukan sebagai eksperimen pembanding pada Subbab 3.7, bukan keputusan yang dikunci di muka.",
"Pembanding ketiga ialah pelatihan lanjutan (*fine-tuning* sebagian pada lapis terakhir maupun penuh seluruh lapis *encoder*) yang dipantau terhadap risiko lupa bencana menggunakan *Elastic Weight Consolidation* (EWC) sebagaimana pretraining *encoder* melakukannya [11]. Kartu model melaporkan bahwa perlindungan EWC bawaannya (*Fisher strength* 2.000) masih menyisakan tingkat lupa sebesar 32,97% pada empat tugas *pretraining* [11]; EWC karena itu diperlakukan sebagai mitigasi parsial, bukan jaminan bebas lupa. Selain itu, membuka bobot *encoder* melalui LoRA maupun pelatihan lanjutan tidak dapat memulihkan detail artikulasi jari apabila informasi tersebut sudah hilang saat CSI diringkas menjadi delapan fitur masukan; skema LoRA dan pelatihan lanjutan karena itu wajib dibandingkan langsung terhadap Pembanding C pada data dan *seed* yang sama. Seluruh skema (beku, beku plus LoRA, pelatihan lanjutan, dan Pembanding C) dilaporkan berdampingan sebagai eksperimen pembanding pada Subbab 3.7, bukan keputusan yang dikunci di muka.")

# ============================================================
# E14 — 2.6: persamaan (2.8) memakai ringkasan temporal s_i (ISS-08)
# ============================================================
ganti("E14-2.6-eq28",
"a~i~ = W~c~ · z~i~ + b~c~ (2.8)",
"a~i~ = W~c~ · s~i~ + b~c~ (2.8)")

ganti("E14-2.6-def",
"dengan W~c~ matriks berukuran K × 128 dan b~c~ vektor bias.",
"dengan s~i~ vektor ringkasan beratensi dari modul temporal berdimensi d~h~ (Subbab 2.8; pada uji *probe* dan ablasi tanpa proyeksi temporal, s~i~ = z~i~ dan d~h~ = 128), W~c~ matriks berukuran K × d~h~, dan b~c~ vektor bias.")

# ============================================================
# E15 — 2.6 akhir: cakupan diterima + akurasi selektif (ISS-22)
# ============================================================
ganti("E15-2.6-selektif",
"Menolak lebih aman daripada menebak kelas yang salah. Ambangnya ditetapkan dari data validasi (Subbab 3.7).",
"Menolak lebih aman daripada menebak kelas yang salah. Ambangnya ditetapkan dari data validasi (Subbab 3.7). Karena klasifikator dengan ambang penolakan dapat mencapai ketepatan tinggi dengan menolak sebagian besar masukan, evaluasi mewajibkan pelaporan berpasangan atas cakupan diterima (*accepted coverage*), akurasi selektif (*selective accuracy*) pada segmen yang diterima, akurasi keseluruhan tanpa penolakan, serta laju terima dan tolak palsu (*false accept/reject rate*) sebagaimana dirinci pada Subbab 3.8.2.")

# ============================================================
# E16 — 2.7: sistem koordinat + handedness + proyeksi 2D (ISS-07)
# ============================================================
ganti("E16-2.7-koordinat",
"Sistem koordinat target harus dibakukan sebelum pelatihan, dan di sinilah letak kehati-hatianya. Koordinat piksel kamera tidak otomatis dapat diprediksi dari CSI tanpa definisi koordinat, transformasi, atau kalibrasi yang dapat direproduksi. Koordinat itu juga tidak tahan terhadap perubahan posisi kamera, jarak, maupun orientasi. Kandidat yang kuat ialah koordinat ternormalisasi terhadap kotak deteksi guru atau terhadap titik pergelangan tangan. Pilihan finalnya ditetapkan pada T0 lalu dipakai konsisten oleh guru dan murid [PERLU VALIDASI: sistem koordinat dan normalisasi target regresi].",
"Sistem koordinat target harus dibakukan sebelum pelatihan, dan di sinilah letak kehati-hatiannya. Koordinat piksel mentah tidak otomatis dapat diprediksi dari CSI karena bergantung pada posisi kamera, jarak, dan pembingkaian. Dua kandidat sistem koordinat ternormalisasi ditetapkan untuk dikunci pada T0: (a) koordinat (x, y) relatif terhadap kotak pembatas deteksi tangan pada rentang [0, 1], atau (b) koordinat berpusat pada titik pergelangan tangan (*wrist-relative*, *landmark* 0) yang diskalakan oleh panjang telapak acuan, yaitu jarak *landmark* 0 ke pangkal jari tengah (*landmark* 9), dengan konsistensi orientasi tangan kanan atau kiri (*handedness*) sesuai standar kamus SIBI. Perlu ditegaskan bahwa keluaran XY merupakan proyeksi bidang dua dimensi kamera dan tidak secara eksplisit memuat kedalaman telapak; kepala regresi karena itu berperan sebagai supervisi geometri bentuk tangan pada bidang pengamatan, bukan rekonstruksi kinematika tiga dimensi penuh. Pilihan finalnya dipakai konsisten oleh guru dan murid [PERLU VALIDASI: sistem koordinat, normalisasi target regresi, dan konvensi *handedness*].")

# ============================================================
# E17 — 2.7: mask efektif (2.13a) + kerugian (2.13) dua koordinat (ISS-06)
# ============================================================
ganti("E17-2.7-mask",
"Kerugian bermask dihitung hanya pada titik yang terlihat:\n\n```rumus\nL~reg~ = ( Σ~i,t,j~ m~itj~ · SmoothL1~δ~( Q~itj~ − P~itj~ ) ) / ( Σ~i,t,j~ m~itj~ + ε ) (2.13)\n```\n\ndengan m~itj~ mask visibilitas dari guru yang bernilai satu jika titik j pada bingkai t terlihat dan nol jika terhalang, serta ε penahan pembagi nol; mask berlaku per *keypoint*, bukan per koordinat.",
"Untuk mencegah *padding* urutan temporal pada segmen pendek ikut terhitung ke dalam kerugian maupun evaluasi, mask visibilitas digabungkan dengan mask valid temporal menjadi mask efektif:\n\n```rumus\nm∗~itj~ = m~it~^valid^ · m~itj~^vis^ , m~it~^valid^ ∈ { 0, 1 } (2.13a)\n```\n\nsehingga kerugian regresi bermask dihitung pada kedua komponen koordinat c anggota {x, y}:\n\n```rumus\nL~reg~ = ( Σ~i,t,j~ m∗~itj~ · ( SmoothL1~δ~( Q~itj,x~ − P~itj,x~ ) + SmoothL1~δ~( Q~itj,y~ − P~itj,y~ ) ) ) / ( 2 · Σ~i,t,j~ m∗~itj~ + ε ) (2.13)\n```\n\ndengan m~itj~^vis^ mask visibilitas dari guru yang bernilai satu jika titik j pada langkah t terlihat dan nol jika terhalang, m~it~^valid^ penanda langkah valid (bukan *padding*), serta ε penahan pembagi nol; mask berlaku per *keypoint*, bukan per koordinat.")

# ============================================================
# E18 — 2.8: cosine similarity (2.14a) + referensi (2.15) (ISS-08)
# ============================================================
ganti("E18-2.8-cos",
"Konflik gradien antartugas dipantau lewat besar gradien tiap kepala; jika keduanya menarik representasi ke arah berlawanan, penyeimbangan gradien atau pelatihan bergantian dipertimbangkan dan perlakuannya dilaporkan. Pada baseline, pembaruan tetapan menyentuh seluruh tetapan di luar *encoder*:",
"Konflik gradien antartugas dipantau tidak hanya dari besar (*norm*) gradien tiap kepala, melainkan juga dari keselarasan arahnya pada parameter bersama θ~shared~ = { φ~adapter~, θ~temporal~ } melalui kemiripan kosinus:\n\n```rumus\ncos( g~c~, g~r~ ) = ( g~c~^T^ · g~r~ ) / ( || g~c~ || · || g~r~ || + ε ) (2.14a)\n```\n\ndengan g~c~ = ∇~θshared~ L~cls~ dan g~r~ = ∇~θshared~ L~reg~ berturut-turut gradien kerugian klasifikasi dan regresi terhadap parameter bersama. Nilai negatif yang konsisten (cos( g~c~, g~r~ ) < 0) menandakan tarikan arah gradien yang bertentangan dan menjadi dasar penyeimbangan gradien atau pelatihan bergantian; perlakuannya dilaporkan. Pada baseline, pembaruan tetapan menyentuh seluruh tetapan di luar *encoder*:")

ganti("E18-2.8-215prime",
"Θ~train~ = { φ~adapter~, θ~temporal~, θ~c~, θ~r~ }, θ~encoder~ = θ~0~ (2.15′)",
"Θ~train~ = { φ~adapter~, θ~temporal~, θ~c~, θ~r~ }, θ~encoder~ = θ~0~ (2.15)")

ganti("E18-2.8-215ref1",
"Parameter modul temporal ikut dilatih bersama kepala pada Persamaan 2.15′.",
"Parameter modul temporal ikut dilatih bersama kepala pada Persamaan (2.15).")

# ============================================================
# E19 — 2.10: konteks tolok ukur ESP-DL 69,2 ms (ISS-24)
# ============================================================
ganti("E19-2.10-espdl",
"Inferensi dirancang berjalan langsung di modul. ESP-DL membuktikan hal itu mungkin dengan contoh pengenalan gestur tangan int8 69,2 ms pada keluarga ESP32 [23]. TensorFlow Lite Micro menjadi alternatifnya.",
"Inferensi dirancang berjalan langsung di modul. ESP-DL menunjukkan kelayakan eksekusi jaringan terkuantisasi int8 pada ESP32-S3 lewat tolok ukur pengenalan gestur tangan berbasis citra RGB 128×128 (`MobileNetV2-0.5`, waktu inferensi model 69,2 ms dan total 73,9 ms pada 240 MHz dengan PSRAM) [23]; angka tersebut adalah referensi kemampuan *runtime* int8 citra pada perangkat keras ESP32-S3, bukan waktu inferensi model CSI; latensi model murid CSI-SIBI karenanya diukur langsung pada T2 dan gerbang G1. TensorFlow Lite Micro menjadi alternatifnya.")

# ============================================================
# E20 — 2.11: Kokoro tanpa suara Indonesia; MMS-TTS-ind utama (ISS-15)
# ============================================================
ganti("E20-2.11-tts",
"Mesin TTS yang direncanakan ialah Kokoro-82M ONNX berserta sekitar 82 juta parameter [24]; dengan keputusan D3, mesin itu diposisikan pada dua lokasi, yaitu server lokal sebagai jalur utama dan ponsel melalui ONNX Runtime sebagai jalur cadangan, dan keduanya memakai prasyarat suara Indonesia yang sama serta diverifikasi pada G3. *Model card* resminya mencantumkan delapan bahasa tanpa bahasa Indonesia, sehingga ketersediaan suara Indonesia perlu diverifikasi pada gerbang G3; jika memang belum tersedia, jalur beralih ke MMS-TTS-ind, model TTS Indonesia dari Meta [25]. Layanan TTS dan ASR awan hadir sebagai pembanding latensi dan mutu, dan pilihan finalnya ditetapkan setelah uji banding (Tabel 3.7).",
"Mesin TTS yang direncanakan menyeleksi tiga hal: dukungan bahasa Indonesia terverifikasi, jalur lokal dan *on-device* tersedia, serta biaya berkelanjutan yang masuk akal. Pemeriksaan dokumentasi resmi `hexgrad/Kokoro-82M` (`VOICES.md`, diakses 14 November 2026) mengonfirmasi bahwa rilis v1.0 mencakup delapan bahasa dengan sembilan varian lokal (Inggris AS, Inggris Britania, Jepang, Mandarin, Spanyol, Prancis, Hindi, Italia, dan Portugis Brasil) tanpa dukungan bahasa Indonesia, serta mencatat penurunan mutu pada ujaran sangat pendek di bawah 10 sampai 20 token [24]. Oleh sebab itu, `facebook/mms-tts-ind` (arsitektur VITS sekitar 36,3 juta parameter dari Meta) ditetapkan sebagai kandidat utama operasional TTS bahasa Indonesia pada server lokal (dikonversi ke ONNX jika uji latensi dan fidelitas memadai), sedangkan Kokoro-82M ONNX tetap diuji sebagai pembanding apabila paket suara atau G2P bahasa Indonesia terverifikasi tersedia sebelum G3 [24], [25]. Layanan TTS dan ASR awan hadir sebagai pembanding latensi dan mutu, dan pilihan finalnya ditetapkan setelah uji banding (Tabel 3.7).")

# ============================================================
# E21 — 2.12: ejaan jari J/Z wajib animasi (ISS-24)
# ============================================================
ganti("E21-2.12-jz",
"Kata di luar kamus dialihkan ke ejaan jari. Sebagai metrik utama arah ini,",
"Kata di luar kamus dialihkan ke ejaan jari. Pada *fallback* ejaan jari itu, 24 huruf statis ditampilkan sebagai gambar pose tangan statis, sedangkan huruf dinamis J dan Z wajib ditampilkan sebagai animasi atau urutan bingkai lintasan agar arah geraknya tidak hilang. Sebagai metrik utama arah ini,")

# ============================================================
# E22 — 2.13: Rust lapisan orkestrasi + runtime ML (ISS-25)
# ============================================================
ganti("E22-2.13-rust",
"Perangkat lunak server ditulis seluruhnya dalam Rust: konkurensi ditangani Tokio, Axum menyediakan HTTP dan WebSocket, Leptos membangun dasbor yang dikompilasi ke WASM, dan Tauri menjadi aplikasi klien ponsel.",
"Lapisan server orkestrasi, penelan bingkai UDP, dasbor, dan klien ditulis dalam Rust: konkurensi ditangani Tokio, Axum menyediakan HTTP dan WebSocket, Leptos membangun dasbor yang dikompilasi ke WASM, dan Tauri menjadi aplikasi klien ponsel, sedangkan mesin inferensi ucapan (`faster-whisper` dan ONNX Runtime untuk TTS) dijalankan pada server lokal melalui *runtime* atau antarmuka pustaka ML yang kompatibel dan diorkestrasi oleh server Rust tersebut.")

# ============================================================
# E23 — 2.14: TKT Permenristekdikti 42/2016 (ISS-23)
# ============================================================
ganti("E23-2.14-tkt",
"Rekomendasi akhirnya menyatakan posisi purwarupa pada skala kesiapterapan teknologi (TKT) yang mengikuti kerangka *technology readiness level* [27].",
"Rekomendasi akhirnya menyatakan posisi purwarupa pada skala Tingkat Kesiapterapan Teknologi (TKT) nasional yang merujuk pada Permenristekdikti Nomor 42 Tahun 2016 [31], yaitu TKT 3 untuk pembuktian konsep secara analitis dan eksperimental serta TKT 4 untuk validasi komponen atau subsistem dalam lingkungan laboratorium, bersama kerangka *technology readiness level* [27].")

# ============================================================
# E24 — 2.14: (2.21) dan (2.22) memakai mask efektif (ISS-06)
# ============================================================
ganti("E24-2.14-21",
"MPJPE = ( Σ~i,t,j~ m~itj~ · || Q~itj~ − P~itj~ || ) / Σ~i,t,j~ m~itj~ (2.21)",
"MPJPE = ( Σ~i,t,j~ m∗~itj~ · || Q~itj~ − P~itj~ || ) / ( Σ~i,t,j~ m∗~itj~ + ε ) (2.21)")

ganti("E24-2.14-22",
"PCK@α = ( Σ~i,t,j~ m~itj~ · 1( || Q~itj~ − P~itj~ || ≤ α · d~ref~ ) ) / Σ~i,t,j~ m~itj~ (2.22)",
"PCK@α = ( Σ~i,t,j~ m∗~itj~ · 1( || Q~itj~ − P~itj~ || ≤ α · d~ref~ ) ) / ( Σ~i,t,j~ m∗~itj~ + ε ) (2.22)")

ganti("E24-2.14-def22",
"dengan 1(·) bernilai satu jika kondisinya terpenuhi, α ambang relatif, dan d~ref~ skala acuan yang mengikuti sistem koordinat yang dibakukan (Subbab 2.7);",
"dengan m∗~itj~ mask efektif gabungan Persamaan (2.13a) sehingga langkah *padding* tidak terhitung, 1(·) bernilai satu jika kondisinya terpenuhi, α ambang relatif, dan d~ref~ skala acuan yang mengikuti sistem koordinat yang dibakukan (Subbab 2.7);")

# ============================================================
# E25 — 2.14: WER tanpa 1 - WER (ISS-16)
# ============================================================
ganti("E25-2.14-wer",
"dan akurasi kata dilaporkan sebagai 1 − WER.",
"Karena jumlah penyisipan (I) dapat melebihi jumlah kata acuan (N), nilai WER tidak dibatasi di bawah satu dan tidak boleh diubah menjadi rumus 1 − WER seolah-olah selalu merupakan akurasi dalam rentang [0, 1]. Pada penelitian ini, kinerja ASR dilaporkan langsung melalui WER beserta rincian jumlah substitusi (S), penghapusan (D), penyisipan (I), dan jumlah kata acuan (N); jika akurasi tingkat kalimat dibutuhkan, *exact-match rate* dihitung dan dilaporkan secara terpisah.")

# ============================================================
# E26 — 2.15: Tabel 2.3 enam baris + narasi kebaruan (ISS-14)
# ============================================================
ganti("E26-2.15-tabel",
"""| No. | Peneliti (Tahun) | Modalitas dan arah | Bahasa isyarat | Bebas kamera | Fokus |
|---|---|---|---|---|---|
| 1 | Ma dkk. (2018) [7] | CSI; isyarat menjadi teks | ASL, 276 isyarat | Ya | Pengenalan berskala besar |
| 2 | Zhang dkk. (2022) [14] | CSI; gestur lintas domain | Gestur umum | Ya | Generalisasi lintas orang dan ruang |
| 3 | Dwijayanti dkk. (2021) [5] | Citra; isyarat menjadi teks | BISINDO | Tidak | CNN pengenalan citra |
| 4 | Penelitian ini | CSI sepasang ESP32-S3; *encoder* terpralatih berkepala dua (klasifikasi dan regresi); supervisi guru visual; inferensi tepi; TTS *on-device* | SIBI, alfabet 26 huruf | Ya | Purwarupa penerjemah dua arah |""",
"""| No. | Peneliti (Tahun) | Modalitas dan arah | Bahasa isyarat | Bebas kamera | Fokus |
|---|---|---|---|---|---|
| 1 | Ma dkk. (2018) [7] | CSI; isyarat menjadi teks | ASL, 276 isyarat | Ya | Pengenalan berskala besar (SignFi) |
| 2 | Ahmed dkk. (2020) [29] | CSI; gestur statis dan dinamis menjadi kelas | ISL, 49 gestur (30 statis, 19 dinamis) | Ya | Pemisahan gestur statis-dinamis pada lingkungan rumah dan kantor (DF-WiSLR) |
| 3 | Zhang dkk. (2022) [14] | CSI; gestur lintas domain | Gestur umum | Ya | Generalisasi lintas orang dan ruang (Widar3.0) |
| 4 | Gao dkk. (2023) [30] | CSI; pengenalan multitugas (isyarat, pengguna, lingkungan) | ASL (dataset SignFi) | Ya | Kerangka multitugas CNN+KNN; mencatat keterbatasan CNN atas dinamika temporal (Wi-SignFi) |
| 5 | Dwijayanti dkk. (2021) [5] | Citra; isyarat menjadi teks | BISINDO | Tidak | CNN pengenalan citra |
| 6 | **Penelitian ini** | CSI sepasang ESP32-S3; kandidat *encoder* terpralatih + modul temporal + dua kepala (supervisi 21 *keypoint* guru visual); inferensi tepi + TTS/ASR | SIBI, alfabet 26 huruf (24 statis + J, Z) | Ya (produk akhir) | Studi kelayakan purwarupa penerjemah dua arah Indonesia |""")

ganti("E26-2.15-narasi",
"Dua kelompok penelitian bisa dibaca dari Tabel 2.3. Pengenalan isyarat dan gestur dari Wi-Fi [7], [14] berjalan tanpa kamera tetapi belum menjangkau SIBI. Riset Indonesia berbasis kamera [5] membuktikan tingginya minat, namun tetap terikat pencahayaan dan garis pandang. Dalam batas penelusuran, publikasi pengenalan isyarat SIBI dari CSI maupun purwarupa dua arah yang memadukannya dengan TTS dan ASR bahasa Indonesia pada ESP32-S3 belum ditemukan. Kebaruan penelitian ini karenanya bersifat kombinatif: CSI satu tautan pada sepasang ESP32-S3 untuk alfabet SIBI, dua kepala tugas di atas *encoder* terpralatih, supervisi lintas modalitas berpandu guru, inferensi tepi, serta integrasi dua arah dengan pemrosesan bahasa Indonesia. Di luar itu, kebaruan tidak diklaim untuk pengenalan kontinu maupun penerjemahan kalimat penuh.",
"Lima penelitian pembanding pada Tabel 2.3 menempatkan batas kebaruan penelitian ini secara presisi. Pengenalan bahasa isyarat berbasis Wi-Fi CSI telah lebih dulu dibuktikan pada SignFi [7]; cakupan kelas statis dan dinamis telah dikaji pada DF-WiSLR [29] untuk 49 isyarat ISL (30 statis dan 19 dinamis); generalisasi lintas domain dirumuskan pada Widar3.0 [14]; dan pendekatan *multitask learning* berbasis CSI telah diterapkan pada Wi-SignFi [30] untuk memprediksi kelas gestur, identitas pengguna, dan lingkungan secara bersamaan. Wi-SignFi secara eksplisit juga melaporkan bahwa CNN ringan belum cukup kuat memodelkan dinamika temporal kompleks dan menyarankan penguatan arsitektur sekuensial [30], yang sejalan dengan dimasukkannya modul temporal khusus untuk huruf dinamis J dan Z dalam penelitian ini. Sementara itu, riset pengenalan isyarat di Indonesia seperti Dwijayanti dkk. [5] masih bertumpu pada citra kamera untuk BISINDO.\n\nDengan demikian, penelitian ini tidak mengklaim kebaruan global atas konsep pengenalan isyarat berbasis CSI, pengenalan kelas statis-dinamis via Wi-Fi, maupun *multitask learning* secara umum. Kebaruan yang diuji bersifat terarah dan kombinatif pada empat titik: (1) studi kelayakan pengenalan 26 kelas alfabet manual SIBI menggunakan satu tautan CSI berbiaya rendah pada sepasang ESP32-S3; (2) pengujian empiris kemampuan transfer *encoder* CSI terpralatih RuView (`wifi-densepose-pretrained`) yang semula dilatih pada fitur lingkungan terhadap artikulasi jari SIBI; (3) formulasi supervisi bantu lintas modalitas berupa regresi 21 *hand keypoints* dari guru visual untuk menopang klasifikasi diskret (diuji lewat ablasi); serta (4) integrasi purwarupa komunikasi dua arah berbasis orkestrasi Rust dengan pemrosesan ucapan bahasa Indonesia (ASR dan TTS) serta kamus SIBI tingkat kata ditambah *fallback* ejaan jari. Di luar itu, kebaruan tidak diklaim untuk pengenalan kontinu maupun penerjemahan kalimat penuh.")

# ============================================================
# E27 — 2.17: narasi + Gambar 2.2 tiga subgraf (pelatihan vs deployment) (ISS-12)
# ============================================================
ganti("E27-2.17-narasi",
"Kerangka pemikiran penelitian ini mengalir dari data sampai perangkat, seperti dirangkum Gambar 2.2. Sinyal CSI dari sepasang ESP32-S3 melewati praproses dan, jika audit menemukannya perlu, adapter masukan yang menyamakan bentuk jendela CSI dengan ruang masukan *encoder* terpralatih. *Encoder* yang dibekukan menghasilkan barisan *embedding* 128 dimensi; modul temporal memproses barisan itu menjadi keadaan tersembunyi per langkah, lalu kepala klasifikasi membaca ringkasannya menjadi kelas huruf dan kepala regresi membaca tiap langkah menjadi 21 koordinat *keypoint*. Keduanya dilatih serentak dengan kerugian gabungan di bawah supervisi guru visual yang hanya aktif saat akuisisi data. Model terpilih lalu dikuantisasi dan dijalankan di modul, sementara arah kedua sistem tetap berjalan lewat ASR, kamus, dan TTS sebagaimana dirancang (Subbab 3.5).",
"Kerangka pemikiran penelitian ini mengalir dari data sampai perangkat, seperti dirangkum Gambar 2.2. Pada fase akuisisi dan pelatihan, sinyal CSI dari sepasang ESP32-S3 melewati praproses (pemeriksaan `first_word_invalid`, normalisasi *baseline* ruang, segmentasi *onset* dan tahan pose) lalu masuk rute masukan hasil audit T0 dan G0b, yaitu Jalur A (rekonstruksi delapan fitur), Jalur B1/B2 (adapter konvolusi satu dimensi), atau Pembanding C. *Encoder* yang dibekukan menghasilkan barisan *embedding* 128 dimensi; modul temporal memproses barisan itu menjadi keadaan tersembunyi per langkah, lalu kepala klasifikasi membaca ringkasannya menjadi kelas huruf dan kepala regresi membaca tiap langkah menjadi 21 koordinat *keypoint*. Keduanya dilatih serentak dengan kerugian gabungan di bawah supervisi guru visual yang hanya aktif saat akuisisi data. Pada graf *deployment* produk akhir (Pilihan 1), kepala regresi dilepas dan model terkuantisasi dijalankan di modul, sementara arah kedua sistem tetap berjalan lewat ASR, kamus, dan TTS sebagaimana dirancang (Subbab 3.5).")

MERMAID_22_LAMA = """```mermaid
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
    EMT["Embedding 128 per langkah jendela<br/>+ modul temporal"]
    HCL["Kepala klasifikasi<br/>(Persamaan 2.8)"]
    HRG["Kepala regresi per langkah<br/>(Subbab 2.8)"]
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
```"""

MERMAID_22_BARU = """```mermaid
flowchart TB
    accTitle: Graf pelatihan dua kepala dan graf deployment Pilihan 1 di atas encoder CSI terpralatih
    accDescr: Subgraf pelatihan dua kepala memuat jalur guru (kamera dan YOLO26m-Pose memberi pseudo-label 21 keypoint; kartu pemandu memberi label kelas) yang membentuk dataset berpasangan terpisah per blok, jalur model Wi-Fi dengan tiga rute masukan hasil audit (Jalur A delapan fitur, Jalur B adapter, Pembanding C), encoder beku, modul temporal, kepala klasifikasi dari ringkasan atensi, kepala regresi per langkah, serta kerugian gabungan dengan mask efektif dan pemantauan kosinus gradien. Subgraf deployment Pilihan 1 memperlihatkan graf inferensi tanpa kamera dan tanpa kepala regresi dengan keluaran label dan skor bermekanisme tolak. Simpul kuning jalur guru, biru jalur model Wi-Fi, hijau pelatihan dan deployment.

    subgraph S1["Pelatihan dua kepala"]
        direction TB
    YOLO["Kamera + YOLO26m-Pose<br/>(guru) [12]"]
    PROT["Kartu pemandu<br/>protokol"]
    DSET["Dataset berpasangan (Pers. 2.24),<br/>split per blok sebelum windowing"]
    CSI["CSI + praproses ESP32-S3<br/>(subcarrier valid) [9]"]
    ROUTE{"Rute masukan<br/>(audit T0, G0b)"}
    ENC["Encoder θ0 beku [11]"]
    TEMP["Modul temporal<br/>(1D-CNN)"]
    KCLS["Kepala klasifikasi<br/>26 huruf (Pers. 2.8)"]
    KREG["Kepala regresi<br/>(T × 21 × 2)"]
    LOSS["Kerugian gabungan + mask efektif<br/>+ cos gradien (Pers. 2.13a-2.15)"]
    YOLO -- "21 keypoint<br/>(pseudo-label)" --> DSET
    PROT --> DSET
    CSI -. "tersinkron penanda waktu" .-> DSET
    CSI --> ROUTE
    ROUTE -- "Jalur A:<br/>8 fitur" --> ENC
    ROUTE -- "Jalur B1/B2:<br/>adapter" --> ENC
    ROUTE -- "Pembanding C" --> TEMP
    ENC -- "barisan z1..zT" --> TEMP
    TEMP -- "ringkasan s_i" --> KCLS
    TEMP -- "keadaan h_t" --> KREG
    KCLS --> LOSS
    KREG --> LOSS
    end
    subgraph S2["Deployment Pilihan 1 (tanpa kamera, tanpa kepala regresi)"]
        direction TB
    DEP["Graf inferensi ESP32-S3 (int8/fp16):<br/>label 26 huruf + skor (dengan tolak)"]
    end
    S1 -- "lepas kepala regresi,<br/>kuantisasi int8/fp16" --> S2

    classDef guru fill:#fef9c3,stroke:#ca8a04,stroke-width:2px,color:#713f12
    classDef model fill:#dbeafe,stroke:#2563eb,stroke-width:2px,color:#1e3a5f
    classDef proses fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#14532d
    class YOLO,PROT guru
    class CSI,ROUTE,ENC,TEMP,KCLS,KREG model
    class DSET,LOSS,DEP proses
```"""

ganti("E27-2.17-mermaid", MERMAID_22_LAMA, MERMAID_22_BARU)

ganti("E27-2.17-caption",
"Gambar 2.2 Arsitektur model jalur isyarat menjadi teks: satu encoder CSI terpralatih yang dibekukan, modul temporal, dua kepala tugas yang berbagi representasi, jalur guru visual yang hanya aktif saat akuisisi data, dan jalur deployment ke ESP32-S3; simpul kuning = jalur guru visual, biru = jalur model Wi-Fi, hijau = pelatihan dan deployment",
"Gambar 2.2 Graf pelatihan dua kepala (akuisisi tersinkron, tiga rute masukan hasil audit, modul temporal, kerugian gabungan) dan graf deployment produk akhir Pilihan 1 tanpa kamera dan tanpa kepala regresi; simpul kuning = jalur guru visual, biru = jalur model Wi-Fi, hijau = pelatihan dan deployment")

# ============================================================
# E28 — 2.16 Tabel 2.4: baris TTS dan radio (audit tabel)
# ============================================================
ganti("E28-2.4tabel-tts",
"| 2 | Mesin TTS | Kokoro TTS ONNX luring; prasyarat suara Indonesia pada G3; alternatif MMS-TTS-ind [24], [25] | TTS awan, VITS/Tacotron penuh | Model 82 juta parameter diinferensikan luring di server lokal (utama) dan ponsel (cadangan) (Subbab 2.11) |",
"| 2 | Mesin TTS | MMS-TTS-ind ONNX luring (kandidat utama operasional); Kokoro ONNX pembanding jika suara Indonesia tersedia [24], [25] | TTS awan, VITS/Tacotron penuh | Verifikasi primer 14 Nov 2026: Kokoro v1.0 tanpa suara Indonesia; MMS-TTS-ind VITS 36,3 juta parameter luring di server lokal, ponsel cadangan (Subbab 2.11) |")

ganti("E28-2.4tabel-radio",
"| 4 | Penginderaan radio | CSI-Ratio 2,4 GHz kanal 20 MHz [13] | RSSI, radar khusus, *time of flight* | RSSI terlalu kasar; CSI-ratio membersihkan derau fase tanpa perangkat tambahan (Subbab 2.2) |",
"| 4 | Penginderaan radio | CSI 2,4 GHz kanal 20 MHz dengan normalisasi *baseline* ruang (Persamaan 2.5) [9], [13] | RSSI, radar khusus, *time of flight* | RSSI terlalu kasar; normalisasi *baseline* ruang membuang tanggapan statis tanpa perangkat tambahan; sisa *phase drift* diaudit T0 (Subbab 2.2) |")

# ============================================================
# E29 — 3.1: inti pelatihan menyebut adapter + modul temporal (ISS-01)
# ============================================================
ganti("E29-3.1",
"Inti pelatihannya adalah supervisi lintas modalitas berpandu guru (Subbab 3.7): label kelas dari protokol perekaman serta deret 21 *keypoint* dari guru kamera YOLO26m-Pose mengawasi pelatihan dua kepala tugas di atas *encoder* CSI terpralatih yang dibekukan.",
"Inti pelatihannya adalah supervisi lintas modalitas berpandu guru (Subbab 3.7): label kelas dari protokol perekaman serta deret 21 *keypoint* dari guru kamera YOLO26m-Pose mengawasi pelatihan adapter masukan (jika digunakan), modul temporal, dan kedua kepala tugas di atas *encoder* CSI terpralatih yang dibekukan pada baseline.")

# ============================================================
# E30 — 3.2: daftar uji T0 diperluas (ISS-11, temuan G0)
# ============================================================
ganti("E30-3.2-t0",
"Uji itu mencakup verifikasi 56 *subcarrier* stabil pada jarak baku 1 meter, uji Delta-CSI (Subbab 3.8.1), koeksistensi radio dengan *streaming* audio aktif, dan pengukuran laju pencuplikan.",
"Uji itu mencakup verifikasi himpunan *subcarrier* valid N~valid~ (pemeriksaan LLTF atau HT-LTF, *pilot*, dan `first_word_invalid`) stabil pada jarak baku 1 meter, audit sisa *phase drift* Persamaan (2.5), uji pilot keterpisahan awal beberapa pose tangan statis di samping pemisahan gerak dan diam, uji Delta-CSI (Subbab 3.8.1), koeksistensi radio dengan *streaming* audio aktif, dan pengukuran laju pencuplikan.")

# ============================================================
# E31 — Gambar 3.1: mermaid baru (kuantisasi di fase T2) + keterangan (ISS-26)
# ============================================================
MERMAID_31_LAMA = """```mermaid
flowchart LR
    accTitle: Tahapan penelitian T0 sampai T5 dengan gerbang keputusan G0 sampai G4
    accDescr: Diagram dua fase. Fase pembangunan data berisi T0 replikasi platform dan audit checkpoint encoder, gerbang G0 baseline, T1 kurasi isyarat, sub-gerbang G0b probe kompatibilitas representasi atas data pilot, dan T2 perekaman dataset serta pelatihan dua kepala. Fase pengujian berisi kuantisasi model, gerbang G1 model tepi, T3 uji generalisasi, gerbang G2 konsultasi tiga pilar, T4 pengemasan purwarupa, gerbang G3 integrasi mesin ucapan, gerbang G4 sintesis kelayakan, dan T5 analisis serta penulisan.

    subgraph KA["Fase pembangunan data (M1–M8)"]
        direction TB
    T0["T0 Replikasi platform, verifikasi<br/>CSI 56 subcarrier pada 1 m, uji Delta-CSI,<br/>koeksistensi, audit checkpoint encoder (M1–M2)"]
    G0("G0 akhir M2: baseline CSI-jaringan:<br/>UDP Rust tanpa kehilangan paket,<br/>akuisisi stabil, gerak terpisah")
    T1["T1 Kurasi isyarat, kalibrasi ruang,<br/>protokol, etika, rintisan separabilitas<br/>pasangan huruf mirip (M2–M4)"]
    T2["T2 Perekaman dataset dan<br/>pelatihan dua kepala di atas<br/>encoder beku (M4–M8)"]
    T0 --> G0
    G0 -- "lolos" --> T1
    G0b("G0b awal T2: probe linear embedding beku,<br/>keputusan jalur masukan")
    T1 --> G0b
    G0b -- "lolos" --> T2
    end
    subgraph KB["Fase pengujian dan penulisan (M8–M14)"]
        direction TB
    T2B["Kuantisasi model terpilih dan uji<br/>deployment jalur klasifikasi<br/>ke modul ESP32-S3"]
    G1("G1 akhir M8: model tepi terkuantisasi:<br/>akurasi skema, ablasi multitugas dilaporkan,<br/>inferensi di bawah 100 ms")
    T3["T3 Uji generalisasi: lintas sesi,<br/>partisipan, ruang, posisi<br/>berdiri/duduk (M8–M10)"]
    G2("G2 akhir M10: konsultasi 3 pilar<br/>pakar SIBI, RF, embedded AI<br/>tanpa temuan blok kritis")
    T4["T4 Pengemasan dua arah, full-stack<br/>Rust, TTS server lokal, uji penerimaan<br/>dan biaya (M10–M12)"]
    G3("G3 M11: integrasi Rust dan mesin<br/>ucapan dalam anggaran latensi")
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
```"""

MERMAID_31_BARU = """```mermaid
flowchart LR
    accTitle: Tahapan penelitian T0 sampai T5 dengan gerbang G0 sampai G4 dan sub-gerbang G0b
    accDescr: Diagram dua fase. Fase data, audit representasi, dan model (M1 sampai M8) berisi T0 replikasi platform, audit subcarrier valid dan first_word_invalid, uji Delta-CSI, koeksistensi audio-CSI, audit artefak RuView; gerbang G0 baseline; T1 kurasi, kalibrasi, protokol, etika, pilot G0b; sub-gerbang G0b uji permutasi probe untuk memilih Jalur A, B, atau Pembanding C; T2 perekaman dataset, split anti-kebocoran, pelatihan dua kepala, ablasi, kuantisasi, uji deployment Pilihan 1; gerbang G1 dengan cakupan diterima dan akurasi selektif. Fase pengujian dan penulisan (M8 sampai M14) berisi T3 uji generalisasi enam skema; G2 konsultasi tiga pilar; T4 pengemasan dua arah, TTS lokal utama MMS-TTS-ind, uji latensi; G3 latensi per arah dan TTFA; G4 sintesis kelayakan dan rekomendasi TKT 3-4 Permenristekdikti 42/2016; T5 analisis dan penulisan.

    subgraph KA["Fase data, audit, dan model (M1-M8)"]
        direction TB
    T0["T0 Replikasi platform, audit<br/>subcarrier valid, Delta-CSI,<br/>koeksistensi, artefak (M1-M2)"]
    G0("G0 akhir M2: laju ≥ 25 fps,<br/>paket hilang ≤ 0,1%,<br/>gerak terpisah")
    T1["T1 Kurasi 26 huruf, kalibrasi,<br/>protokol, etika,<br/>pilot G0b (M2-M4)"]
    G0b("G0b awal T2 (M4): probe linear +<br/>uji permutasi (p < 0,05);<br/>pilih jalur masukan")
    T2["T2 Perekaman dataset, split anti-<br/>leakage, pelatihan dua kepala,<br/>kuantisasi, uji deployment (M4-M8)"]
    G1("G1 akhir M8: akurasi ≥ 50%,<br/>F1 ≥ 0,45, cakupan +<br/>akurasi selektif, < 100 ms")
    T0 --> G0
    G0 -- "lolos" --> T1
    T1 --> G0b
    G0b -- "lolos" --> T2
    T2 --> G1
    end
    subgraph KB["Fase pengujian dan penulisan (M8-M14)"]
        direction TB
    T3["T3 Uji generalisasi enam skema:<br/>sesi, LOSO, LORO, pengguna<br/>baru, posisi (M8-M10)"]
    G2("G2 akhir M10: 3 pilar pakar<br/>tanpa temuan blok kritis")
    T4["T4 Pengemasan dua arah, Rust,<br/>TTS lokal MMS-TTS-ind, uji<br/>latensi, biaya (M10-M12)"]
    G3("G3 M11: Arah 1 ≤ 2 s, Arah 2 ≤ 3 s (p50/p95);<br/>TTFA < 100 ms; UDP < 0,2 ms; RAM < 40 MB")
    G4("G4 akhir M12: Likert, validator,<br/>BOM biaya, TKT 3-4<br/>(Permenristekdikti 42/2016)")
    T5["T5 Analisis dan penulisan<br/>laporan akhir (M12-M14)"]
    T3 --> G2
    G2 -- "lolos" --> T4
    T4 --> G3
    G3 -- "lolos" --> G4
    G4 -- "lolos" --> T5
    end
    KA -- "G1 lolos" --> KB
```"""

ganti("E31-3.1-mermaid", MERMAID_31_LAMA, MERMAID_31_BARU)

ganti("E31-3.1-caption",
"Gambar 3.1 Tahapan penelitian T0–T5 dan gerbang keputusan G0–G4 (jalur lolos; tindakan jika gagal pada Tabel 3.5)",
"Gambar 3.1 Tahapan penelitian T0–T5, gerbang keputusan G0–G4, dan sub-gerbang G0b (jalur lolos; kuantisasi dan uji deployment berada pada T2; tindakan jika gagal merujuk Tabel 3.5)")

# ============================================================
# E32 — 3.5: paragraf transport audio (ISS-19)
# ============================================================
ganti("E32-3.5-audio",
"Server lokal menjalankan server RuView, server Rust, faster-whisper sebagai ASR cadangan, serta TTS Kokoro/MMS sebagai jalur utama sintesis luring.",
"Server lokal menjalankan server RuView, server Rust, faster-whisper sebagai ASR cadangan, serta TTS MMS-TTS-ind sebagai jalur utama sintesis luring. Untuk menjamin aliran audio dua arah tidak melumpuhkan penangkapan CSI 50 bingkai per detik pada kanal Wi-Fi yang sama, spesifikasi protokol audio ditetapkan secara eksplisit sebelum G3. Jalur mikrofon Arah 2 (INMP441 I2S) menggunakan cuplikan PCM 16-bit mono 16 kHz yang dikirim dalam paket berukuran tetap melalui UDP berpenyangga atau aliran TCP/WebSocket saat tombol PTT ditekan, disertai nomor urut untuk mendeteksi paket hilang beserta batas waktu dan pengulangan pada server Rust. Jalur *speaker* Arah 1 (MAX98357A I2S) menerima aliran audio PCM 16-bit mono (atau berkas klip ter-*cache* untuk 26 huruf tunggal) ke penyangga cincin (*ring buffer*) di PSRAM modul RX guna mencegah *underrun* akibat jitter Wi-Fi. Dampak lalu lintas audio terhadap kestabilan laju CSI dan *packet loss* diukur langsung pada T0 dan G3; apabila koeksistensi pada satu modul RX menimbulkan degradasi CSI melampaui ambang G0, jalur cadangan C (memisahkan antarmuka audio ke modul ketiga atau pemutaran di ponsel) diaktifkan dan dilaporkan.")

# ============================================================
# E33 — 3.5: paragraf daya TP4056/regulator (ISS-19)
# ============================================================
ganti("E33-3.5-daya",
"Rantai dayanya tersusun atas baterai, BMS 1S, TP4056, dan regulator 3,3 volt papan; tegangan baterai diukur lewat pembagi tegangan sehingga persentase baterai bisa tampil di layar.",
"Rantai dayanya tersusun atas baterai, BMS 1S, TP4056, dan regulator 3,3 volt papan; tegangan baterai diukur lewat pembagi tegangan sehingga persentase baterai bisa tampil di layar. Pada rantai daya itu, regulator 3,3 V dipastikan memiliki kapasitas arus kontinu memadai (target 500 sampai 800 mA guna menampung lonjakan arus Wi-Fi TX dan penguat kelas D MAX98357A saat *speaker* 8 Ω 3 W aktif), serta modul TP4056 diuji untuk memastikan tidak terjadi gangguan pengisian akibat beban puncak sistem (*load-sharing* atau larangan operasi aktif saat pengisian jika modul tanpa *power-path*). Estimasi ketahanan baterai (Persamaan 3.4) didasarkan pada pengukuran arus aktual I~rata~ dalam kondisi diam, inferensi aktif, *streaming* audio, dan pemutaran *speaker*.")

# ============================================================
# E34 — 3.5: paragraf TTS/TTFA terukur (ISS-15)
# ============================================================
ganti("E34-3.5-tts",
"Mesin sintesis utamanya berjalan di server lokal dengan Kokoro-82M ONNX yang diinferensikan luring [24], sementara jalur cadangan *on-device* berjalan di ponsel lewat ONNX Runtime di dalam Tauri. Target latensinya didefinisikan sebagai waktu menuju audio pertama (*time-to-first-audio*, TTFA) di bawah 100 ms pada frasa uji paling banyak lima kata; durasi sintesis keseluruhan dilaporkan terpisah. Prasyaratnya hanya satu, yaitu tersedia suara bahasa Indonesia pada Kokoro; jika belum, jalur beralih ke MMS-TTS-ind [25] dan peralihan itu dilaporkan.",
"Mesin sintesis utama di server lokal memakai `facebook/mms-tts-ind` (dikonversi ke ONNX untuk evaluasi luring; sekitar 36,3 juta parameter) karena verifikasi resmi `hexgrad/Kokoro-82M` (`VOICES.md`, 14 November 2026) memastikan tidak tersedianya suara bahasa Indonesia pada rilis v1.0 [24], [25]; Kokoro-82M ONNX tetap disiapkan sebagai pembanding apabila rilis atau adapter bahasa Indonesia terverifikasi sebelum G3. Untuk menjaga konsistensi pengukuran, target waktu menuju audio pertama (*time-to-first-audio*, TTFA) di bawah 100 ms pada frasa uji hingga lima kata didefinisikan terpisah dari durasi sintesis total dan diukur pada kondisi terdokumentasi: perangkat keras laptop uji (CPU i7-11370H dan GPU RTX 3070), *execution provider* ONNX Runtime (CPU atau CUDA), presisi model (FP32, FP16, atau INT8), serta ukuran *chunk* penyangga audio pertama, dengan pelaporan persentil p50 dan p95. Untuk keluaran huruf tunggal pada Arah 1, klip audio 26 huruf di-*pre-cache* agar pemutaran tetap instan.")

# ============================================================
# E35 — Gambar 3.2 keterangan + 3.3 mermaid dan keterangan (ISS-27)
# ============================================================
ganti("E35-3.2-caption",
"Gambar 3.2 Perangkat keras penelitian; huruf pada tiap foto mengikuti baris Tabel 3.1 (foto produk sebagai pengenal bentuk, bukan acuan merek)",
"Gambar 3.2 Perangkat keras penelitian; huruf pada tiap foto mengikuti baris Tabel 3.1 (foto produk sebagai ilustrasi pengenal bentuk sementara sebelum perangkat dirakit, bukan acuan merek)")

MERMAID_33_LAMA = """```mermaid
flowchart TD
    accTitle: Arsitektur produk akhir tanpa kamera
    accDescr: Tiga rantai. Arah 1 mengalir dari beacon ESP-NOW node pemancar melalui zona isyarat ke node penerima yang menjalankan model klasifikasi terkuantisasi; label dan skor dikirim via UDP ke server Rust, teks tampil di layar modul dan aplikasi Tauri, teks disintesis mesin TTS Kokoro di server lokal, dan audio dialirkan kembali ke speaker node penerima. Arah 2 mengalir dari tombol tekan-untuk-bicara dan mikrofon I2S; audio dialirkan ke server lalu dikenali ASR, yaitu layanan awan saat daring atau faster-whisper di server saat luring, dan teks dipetakan ke representasi SIBI pada aplikasi Tauri. Jalur guru memakai webcam dan YOLO26m-Pose untuk supervisi pelatihan. Garis putus-putus menandai jalur cadangan TTS on-device pada ponsel jika server tidak tersedia.

    subgraph A1["Arah 1: isyarat menjadi teks dan suara"]
        TX["Node TX: beacon<br/>ESP-NOW"]
        ZN["Zona isyarat<br/>(satu pengisyarat)"]
        RX["Node RX: CSI promiscuous +<br/>model klasifikasi terkuantisasi<br/>+ antarmuka"]
        MAPL["Kamus label-teks<br/>di modul"]
        DSP1["Layar modul + aplikasi Tauri:<br/>teks hasil"]
        SPK["Speaker DAC I2S<br/>(node RX)"]
        TX --> ZN
        ZN --> RX
        RX --> MAPL
        MAPL --> DSP1
    end

    SVR["Server Rust di laptop:<br/>orkestrasi, TTS Kokoro utama,<br/>faster-whisper ASR luring"]
    TTSP["TTS on-device ponsel<br/>(Kokoro ONNX; cadangan)"]

    subgraph A2["Arah 2: ucapan menjadi representasi SIBI"]
        BTN["Tombol<br/>tekan-untuk-bicara"]
        MIC["Mikrofon<br/>I2S"]
        ASR["ASR: layanan awan saat daring,<br/>faster-whisper di server saat luring"]
        DSP2["Aplikasi Tauri: teks lalu<br/>representasi SIBI"]
        AST["Aset SIBI: glos,<br/>gambar, ejaan jari<br/>(Subbab 2.12)"]
        BTN --> MIC
        MIC -- "audio via UDP" --> SVR
        ASR -- "teks" --> DSP2
        AST --> DSP2
    end

    subgraph AG["Jalur guru (hanya akuisisi dan pelatihan)"]
        CAM["Webcam laptop"]
        Y26P["YOLO26m-Pose:<br/>21 keypoint pose tangan"]
        SUP["Supervisi pelatihan<br/>dua kepala (Subbab 3.7)"]
        CAM --> Y26P
        Y26P --> SUP
    end

    RX -- "label + skor via UDP" --> SVR
    SVR -- "audio dialirkan" --> SPK
    SVR -- "audio" --> ASR
    SVR -. "server tak tersedia" .-> TTSP
```"""

MERMAID_33_BARU = """```mermaid
flowchart TD
    accTitle: Arsitektur produk akhir tanpa kamera dengan cadangan TTS on-device pada Arah 1
    accDescr: Jalur guru hanya aktif saat akuisisi dan pelatihan; webcam dan YOLO26m-Pose menghasilkan 21 keypoint untuk supervisi dua kepala. Arah 1 mengalir dari beacon ESP-NOW melalui zona isyarat ke node RX yang menjalankan model klasifikasi terkuantisasi Pilihan 1; label dan skor dikirim via UDP ke server Rust, teks tampil di layar dan aplikasi Tauri, TTS server lokal menyintesis suara yang dialirkan ke speaker DAC I2S node RX; garis putus-putus adalah cadangan TTS on-device ponsel untuk Arah 1. Arah 2 mengalir dari tombol PTT dan mikrofon I2S ke server, dikenali ASR awan saat daring atau faster-whisper saat luring, dipetakan ke kamus kata SIBI dengan ejaan jari termasuk animasi J dan Z, lalu tampil di aplikasi Tauri.

    subgraph GURU["Jalur guru (akuisisi dan pelatihan saja)"]
        direction TB
    WC["Webcam laptop"]
    YP["YOLO26m-Pose:<br/>21 keypoint tangan"]
    SUP["Supervisi pelatihan<br/>(Subbab 3.7)"]
    WC --> YP
    YP --> SUP
    end
    subgraph A1["Arah 1: isyarat menjadi teks dan suara"]
        direction TB
    TX["Node TX: beacon ESP-NOW"]
    ZN["Zona isyarat"]
    RX["Node RX: CSI + model klasifikasi<br/>terkuantisasi (Pilihan 1)"]
    MAPL["Kamus label-teks di modul"]
    DSP1["Layar modul + Tauri:<br/>teks hasil + skor"]
    SPK["Speaker DAC I2S (node RX)"]
    TTSP["TTS on-device ponsel<br/>(cadangan Arah 1)"]
    TX --> ZN
    ZN --> RX
    RX --> MAPL
    MAPL --> DSP1
    end
    SRV["Server Rust (laptop):<br/>TTS MMS-TTS-ind utama +<br/>ASR faster-whisper"]
    subgraph A2["Arah 2: ucapan menjadi representasi SIBI"]
        direction TB
    PTT["Tombol tekan-untuk-bicara"]
    MIC["Mikrofon I2S (INMP441)"]
    ASR["ASR: awan (daring) /<br/>faster-whisper (luring)"]
    ASET["Kamus kata SIBI + ejaan jari<br/>(animasi J dan Z)"]
    TAU["Aplikasi Tauri:<br/>teks + representasi SIBI"]
    PTT --> MIC
    MIC -- "audio PCM via UDP/WS" --> SRV
    ASR -- "teks" --> ASET
    ASET --> TAU
    end
    RX -- "label + skor via UDP" --> SRV
    SRV -- "audio TTS dialirkan" --> SPK
    SRV -. "cadangan" .-> TTSP
    SRV -- "audio" --> ASR
```"""

ganti("E35-3.3-mermaid", MERMAID_33_LAMA, MERMAID_33_BARU)

ganti("E35-3.3-caption",
"Gambar 3.3 Arsitektur produk akhir tanpa kamera. Subgraf arah 1 = isyarat menjadi teks dan suara; subgraf arah 2 = ucapan menjadi representasi SIBI; subgraf jalur guru hanya aktif saat akuisisi dan pelatihan; garis putus-putus = jalur cadangan TTS *on-device* pada ponsel jika server tidak tersedia.",
"Gambar 3.3 Arsitektur produk akhir tanpa kamera. Subgraf Arah 1 = isyarat menjadi teks dan suara, dengan cadangan TTS *on-device* ponsel untuk Arah 1; subgraf Arah 2 = ucapan menjadi representasi SIBI; subgraf jalur guru hanya aktif saat akuisisi dan pelatihan; garis putus-putus = jalur cadangan.")

# ============================================================
# E36 — 3.5: paragraf Rust 3.5 selaras + Tabel 3.2 baris 8 dan 10
# ============================================================
ganti("E36-3.2tabel-8",
"| 8 | faster-whisper dan MMS-TTS-ind [26], [25]; layanan ucapan awan [PERLU DATA: layanan final hasil uji banding] | ASR cadangan lokal (faster-whisper); alternatif TTS lokal (MMS-TTS-ind); ASR utama saat daring |",
"| 8 | faster-whisper, MMS-TTS-ind ONNX (kandidat utama), Kokoro ONNX (pembanding) [26], [25], [24]; layanan ucapan awan [PERLU DATA: layanan final hasil uji banding] | ASR cadangan lokal (faster-whisper); TTS utama operasional di server lokal (MMS-TTS-ind); TTS pembanding (Kokoro); ASR utama saat daring |")

ganti("E36-3.2tabel-10",
"| 10 | Kokoro TTS ONNX dan ONNX Runtime [24] | Mesin TTS utama di server lokal dan cadangan *on-device* di ponsel; prasyarat suara Indonesia pada G3 |",
"| 10 | ONNX Runtime dan Kokoro TTS ONNX [24] | *Runtime* evaluasi TTS di server lokal dan ponsel (Tauri); Kokoro diuji sebagai pembanding jika suara Indonesia tersedia sebelum G3 |")

# ============================================================
# E37 — 3.6: prosedur butir 4-7 (ISS-20)
# ============================================================
ganti("E37-3.6-butir4",
"4. Menjalankan `scripts/collect-ground-truth.py` supaya perekaman CSI dan *webcam* berjalan sinkron dengan penanda waktu bersama, lalu memverifikasi ulang kualitas sinkronisasi lewat uji kejadian di awal sesi, misalnya satu ketukan tangan yang terbaca kedua sensor [PERLU DATA: toleransi sinkronisasi yang diterima].",
"4. Menjalankan `scripts/collect-ground-truth.py` menggunakan sumber penanda waktu monotonik tunggal pada laptop sebagai acuan penyelarasan *timestamp* bingkai kamera (target sekitar 30 fps) dan bingkai CSI (sekitar 50 fps). Kualitas sinkronisasi diverifikasi melalui uji ketukan tangan di awal dan akhir setiap sesi dengan batas galat selisih waktu maksimum [PERLU DATA: toleransi sinkronisasi akhir, misalnya 20 ms atau satu bingkai CSI]. Bingkai kamera yang hilang (*frame drop*) dicatat; jika jeda melebihi toleransi, segmen ditandai tidak valid untuk target regresi tanpa interpolasi paksa gerakan yang hilang.")

ganti("E37-3.6-butir5",
"5. Memunculkan kartu pemandu huruf target, merekam satu repetisi, memberi jeda, lalu mengulanginya sampai setiap huruf mencapai kurang lebih 30 repetisi.",
"5. Memunculkan kartu pemandu huruf target dengan urutan huruf yang diacak di dalam setiap blok guna mencegah efek urutan (*order effect*) dan akumulasi kelelahan pada kelas huruf tertentu, merekam satu repetisi, memberi jeda antarrepetisi, hingga tiap huruf mencapai sekitar 30 repetisi per sesi.")

ganti("E37-3.6-butir6",
"6. Membuang segmen yang tangan tidak terdeteksi model guru, yang mengalami *jitter* *keypoint* ekstrem, atau yang terpotong, lalu mencatat tingkat segmen terbuang dan skor kualitas anotasi tiap segmen.",
"6. Membuang segmen yang gagal deteksi tangan oleh model guru, mengalami *jitter* *keypoint* melampaui ambang, atau terpotong, serta melakukan audit kualitas *keypoint* khusus lintasan dinamis J dan Z (melaporkan *detection rate*, laju *frame drop*, dan konsistensi kelancaran lintasan selama gerak cepat, karena kinerja `exp11_huruf24` pada 24 huruf statis tidak otomatis menjamin keandalan *keypoint* pada gerakan J/Z); tingkat segmen terbuang dan skor kualitas anotasi tiap segmen dicatat.")

ganti("E37-3.6-butir7",
"7. Meminta validator mengambil sampel segmen untuk memeriksa kebenaran bentuk isyarat; label guru berstatus *pseudo-label* sampai pemeriksaan ini selesai.",
"7. Meminta validator penutur tunarungu memeriksa sampel acak terstratifikasi sebesar [PERLU DATA: proporsi sampel, misalnya sekurang-kurangnya 10% segmen per kelas atau minimal 3 repetisi per huruf per pengisyarat] dan menjalankan uji reliabilitas kesepakatan jika penilai lebih dari satu orang; label keluaran guru berstatus *pseudo-label* sampai audit validator selesai. Rujukan teknis model guru merujuk dokumentasi Ultralytics [12] serta artefak repositori WPC peneliti [PERLU DATA: tag rilis/commit dan hash *checkpoint* exp11_huruf24].")

# ============================================================
# E38 — 3.6: etika tata kelola data (ISS-21)
# ============================================================
ganti("E38-3.6-etika",
"Baru setelah persetujuan etik dari [PERLU DATA: lembaga atau komisi pemberi persetujuan etik] serta persetujuan tertulis setiap partisipan diperoleh, perekaman dimulai; partisipan berhak mengundurkan diri kapan saja. Formulir persetujuan menerangkan bahwa kamera hanya menyala pada sesi akuisisi jalur guru, produk akhir bebas kamera, dan mode privasi RuView aktif. Video semata-mata dipakai untuk verifikasi batas segmen, penyaringan kualitas, dan diagnosis; penyimpanannya terbatas dan tidak dipublikasikan. Karena audio arah kedua dikirim ke layanan awan, tujuannya diungkapkan pada formulir dan kebijakan penyimpanan layanan diperiksa sebelum dipakai. *Dataset* yang dipublikasikan hanya memuat CSI, label, *keypoint*, dan metadata tanpa identitas.",
"Baru setelah persetujuan etik dari [PERLU DATA: lembaga atau komisi pemberi persetujuan etik] serta persetujuan tertulis (*informed consent*) yang disajikan dalam format bahasa Indonesia yang jelas dan aksesibel bagi partisipan Tuli (didampingi juru bahasa isyarat atau panduan visual jika diperlukan) diperoleh, perekaman dimulai; partisipan berhak mengundurkan diri kapan saja. Apabila uji kegunaan (T4) melibatkan siswa di bawah usia 18 tahun, penelitian wajib memperoleh persetujuan tertulis orang tua atau wali sekaligus persetujuan sukarela anak (*child assent*); jika tidak, partisipan dibatasi pada kelompok dewasa (sedikitnya 18 tahun). Formulir persetujuan menerangkan batas ruang lingkup kamera (hanya saat akuisisi pelatihan), mode privasi RuView aktif, serta pengiriman audio Arah 2 ke layanan awan saat mode daring. Video mentah hanya disimpan pada media terenkripsi dengan akses terbatas peneliti untuk keperluan verifikasi batas segmen, penyaringan kualitas, dan peninjauan validator, lalu dihapus secara permanen dalam batas waktu [PERLU DATA: misalnya maksimal 30 hari] setelah seluruh validasi anotasi selesai. *Dataset* yang dibagikan tidak mencantumkan nama atau identitas langsung, namun penelitian mengakui bahwa pola kinematika tangan, audio, atau metadata sesi tetap berpotensi memiliki risiko identifikasi ulang sehingga tidak diklaim sepenuhnya anonim tanpa batas, dan tata kelolanya tunduk pada perjanjian akses terbatas.")

# ============================================================
# E39 — 3.7: persamaan (3.1) N_valid + segmentasi tiga fase (ISS-05, ISS-11)
# ============================================================
ganti("E39-3.7-31",
"d( t ) = ( 1 / 56 ) · Σ~n~ | h~n~(t) − h~n~( t − 1 ) | (3.1)",
"d( t ) = ( 1 / |N~valid~| ) · Σ~n~ | h~n~(t) − h~n~( t − 1 ) | , n ∈ N~valid~ (3.1)")

ganti("E39-3.7-seg",
"Segmen dianggap memuat gerak jika d(t) melampaui ambang τ selama sekurang-kurangnya panjang jendela minimum; J dan Z terpotong jelas dari energinya, sedangkan huruf statis memakai jendela tahan pose yang ambang dan panjangnya ditetapkan dari data validasi, bukan dari data uji (Tabel 3.7).",
"Segmentasi tidak mengandalkan ambang energi gerak τ semata karena huruf statis memperagakan pose yang ditahan diam, saat nilai energi gerak d(t) justru turun mendekati kondisi tenang. Alur segmentasi memisahkan tiga fase: (1) deteksi awal gerak (*onset*) saat d(t) melampaui ambang τ~onset~; (2) untuk 24 huruf statis, pencuplikan jendela tahan pose (*pose-hold window*) berdurasi L~hold~ sesudah *onset* mereda atau stabil, yang ambang dan durasinya ditala dari data validasi (bukan data uji); serta (3) untuk huruf dinamis J dan Z, penangkapan jendela lintasan penuh selama energi gerak melampaui ambang τ~dinamis~ hingga kembali tenang.")

ganti("E39-3.7-dH",
"d~|H|~( t ) = ( 1 / 56 ) · Σ~n~ | |h~n~(t)| − |h~n~( t − 1 )| |",
"d~|H|~( t ) = ( 1 / |N~valid~| ) · Σ~n~ | |h~n~(t)| − |h~n~( t − 1 )| | , n ∈ N~valid~")

# ============================================================
# E40 — 3.7: audit paragraph Jalur A/B/C
# ============================================================
ganti("E40-3.7-audit",
"Dua jalur penyelesaian karenanya disiapkan: menghitung ulang delapan fitur turunan bawaan RuView dari bingkai CSI, atau melatih adapter masukan kecil yang memetakan jendela CSI ke ruang masukan *encoder* [PERLU VALIDASI: bentuk masukan checkpoint dan rancangan adapter].",
"Empat rute evaluasi karenanya disiapkan sesuai Subbab 2.4: Jalur A (menghitung ulang delapan fitur turunan bawaan RuView beserta *standardizer*-nya), Jalur B1 (adapter rekonstruksi fitur), Jalur B2 (adapter terpandu tugas), serta Pembanding C (*baseline* CSI temporal lebih kaya tanpa penyempitan delapan fitur) [PERLU VALIDASI: bentuk masukan *checkpoint* dan rancangan adapter].")

# ============================================================
# E41 — 3.7: resolusi temporal dikoreksi (ISS-03)
# ============================================================
ganti("E41-3.7-temporal",
"Resolusi temporal dijaga dengan jendela bergulir berlompatan H = 0,25 detik (usulan; dikalibrasi pada T2) sehingga satu segmen huruf menghasilkan satu sampai sekitar tiga belas langkah *embedding* tergantung durasinya. Untuk J dan Z, kelas tidak dibaca dari satu jendela: barisan langkah diproses modul temporal secara berurutan dan klasifikasinya diambil dari ringkasan barisan tersebut. Dengan itu lintasan gerak J dan Z tetap tersedia pada laju empat langkah per detik, cukup untuk lintasan sekitar satu detik, tanpa melanggar kontrak masukan *encoder*. Kandidat modul temporal ialah 1D-CNN ringan dari rancangan lama yang memelihara urutan waktu per langkah; agregasi statistik hanya menjadi kandidat bagi jalur klasifikasi, dan pilihan di antara keduanya diambil dari hasil ablasi pada data yang sama (Subbab 2.8).",
"Pada rute *encoder* RuView (Jalur A dan Jalur B), setiap vektor masukan merangkum jendela sepanjang W = 1 detik dengan pergeseran (*hop*) H = 0,25 detik (usulan; dikalibrasi pada T2), menghasilkan tumpang tindih (*overlap*) sebesar 75%. Laju empat langkah per detik (1/H = 4 Hz) merupakan laju lompatan jendela yang saling tumpang tindih, bukan empat pengamatan temporal independen, karena setiap *embedding* tetap mengagregasi konteks satu detik. Untuk J dan Z, kelas tidak dibaca dari satu jendela: barisan langkah diproses modul temporal secara berurutan dan klasifikasinya diambil dari ringkasan barisan tersebut; lintasan gerak J dan Z karena itu tetap tersedia tanpa melanggar kontrak masukan *encoder*. Karena agregasi W = 1 detik berisiko mengaburkan lintasan cepat J dan Z, eksperimen wajib membandingkan konfigurasi (W = 1,0 s, H = 0,25 s) terhadap jendela lebih pendek (W = 0,5 s dengan H = 0,10 sampai 0,25 s) dan terhadap Pembanding C (*baseline* CSI temporal langsung pada W = 0,2 s atau laju bingkai asli tanpa penyempitan delapan fitur). Kandidat modul temporal ialah 1D-CNN ringan dari rancangan lama yang memelihara urutan waktu per langkah; agregasi statistik hanya menjadi kandidat bagi jalur klasifikasi, dan pilihan di antara keduanya diambil dari hasil ablasi pada data yang sama (Subbab 2.8).")

# ============================================================
# E42 — 3.7: G0b uji permutasi (ISS-09)
# ============================================================
ganti("E42-3.7-g0b",
"Rangkaiannya: *probe* 24 huruf statis pada skema blok temporal, *probe* sekuensial atas gabungan langkah tiap segmen, *probe* biner J terhadap Z, serta dua kontrol, yaitu *probe* pada fitur mentah ringkas dan kontrol label-acak (p < 0,05), agar hasilnya tidak menipu. Ambang usulannya: F1 makro *probe* sekurang-kurangnya 0,30 dan sekurang-kurangnya tiga kali peluang acak; *probe* J–Z sekurang-kurangnya 70%; seluruhnya difinalkan bersama pembimbing sebelum gerbang dinilai. Jalur fitur turunan dipakai jika lulus; jika gagal tetapi adapter lulus, adapter yang dipilih; jika keduanya gagal, *encoder* beku ditinggalkan menuju skema adaptasi LoRA dan pelatihan lanjutan (Subbab 2.5) dan hasilnya dilaporkan sebagai temuan.",
"Rangkaiannya: *probe* 24 huruf statis pada skema blok temporal, *probe* sekuensial atas gabungan langkah tiap segmen, *probe* biner J terhadap Z, serta perbandingan langsung terhadap Pembanding C (fitur CSI mentah atau lebih kaya). Untuk memvalidasi signifikansi statistik secara benar, dilakukan uji permutasi (*permutation test*): label kelas diacak pada level blok atau repetisi independen (bukan per *window* tumpang tindih) sebanyak M = 1.000 iterasi untuk membentuk distribusi *null* acak; pengujian dinyatakan signifikan apabila skor F1 makro *probe* berlabel asli melampaui persentil ke-95 distribusi *null* (p~perm~ < 0,05), sementara skor pada label teracak tetap berada di sekitar peluang acak. Ambang usulannya: F1 makro *probe* sekurang-kurangnya 0,30 dan sekurang-kurangnya tiga kali peluang acak; *probe* J–Z sekurang-kurangnya 70%; seluruhnya difinalkan bersama pembimbing sebelum gerbang dinilai. Jalur A dipakai jika lulus; jika gagal, diuji Jalur B1 (rekonstruksi) dan Jalur B2 (adapter terpandu tugas); jika seluruh jalur masukan delapan fitur tetap gagal, skema adaptasi LoRA dan pelatihan lanjutan (Subbab 2.5) diuji secara berdampingan dengan Pembanding C (CSI lebih kaya tanpa penyempitan delapan fitur), karena adaptasi bobot *encoder* tidak dapat memulihkan informasi jari yang hilang sebelum masuk *encoder*; seluruh hasilnya dilaporkan sebagai temuan.")

# ============================================================
# E43 — 3.7: MPJPE resolusi langkah + anti-leakage purge gap (ISS-04, ISS-10)
# ============================================================
ganti("E43-3.7-kp",
"Deret *keypoint* guru disampel ulang ke pusat tiap jendela fitur sehingga tiap langkah *embedding* memiliki satu target 21 × 2; keluaran regresi model didefinisikan pada laju yang sama. Untuk pelaporan galat lintasan J dan Z, deret prediksi diinterpolasi kembali ke laju kamera agar dapat dibandingkan bingkai demi bingkai dengan acuan guru, dan metode interpolasinya dinyatakan pada laporan.",
"Deret *keypoint* guru dipasangkan ke titik pusat waktu tiap jendela CSI dengan laju yang sama dengan keluaran modul temporal. Untuk mengevaluasi galat lintasan J dan Z secara jujur, metrik MPJPE dan PCK@α dilaporkan secara utama pada resolusi langkah model (dengan mask efektif m∗~itj~ sesuai Persamaan 2.13a agar langkah *padding* tidak terhitung). Apabila dilakukan interpolasi ke laju kamera untuk perbandingan visual bingkai demi bingkai dengan acuan guru, ditegaskan bahwa interpolasi tidak menciptakan informasi temporal baru yang tidak diamati dan hasilnya hanya berstatus pelaporan sekunder; metode interpolasinya dinyatakan pada laporan.")

ganti("E43-3.7-leak",
"Enam skema pada Tabel 3.4 mengukur kinerja; untuk skema dalam sesi, pembagiannya temporal per blok dan tidak acak.",
"Enam skema pada Tabel 3.4 mengukur kinerja; untuk skema dalam sesi, pembagiannya temporal per blok dan tidak acak. Untuk mencegah kebocoran data (*data leakage*) akibat tumpang tindih jendela sebesar 75%, seluruh pembagian data latih, validasi, dan uji pada keenam skema wajib dilakukan pada level rekaman mentah, sesi, atau blok/grup repetisi sebelum pembentukan jendela bergulir (*sliding windows*), disertai celah pemisah (*purge gap*) sekurang-kurangnya sepanjang W (satu detik) pada perbatasan blok agar tidak ada jendela yang memotong batas set latih dan uji.")

# ============================================================
# E44 — 3.7: rujukan persamaan pelatihan (2.14 dan 2.15)
# ============================================================
ganti("E44-3.7-ref215",
"kedua kepala beserta modul temporal dilatih serentak dengan kerugian gabungan Persamaan 2.14 dan 2.15′, memakai seed tetap",
"kedua kepala beserta modul temporal dilatih serentak dengan kerugian gabungan Persamaan (2.14) dan (2.15), memakai *seed* tetap")

# ============================================================
# E45 — 3.8.2: dua taraf kelayakan + pelaporan selektif (ISS-22)
# ============================================================
ganti("E45-3.8.2",
"Pembanding ablasi dilaporkan berdampingan: kepala klasifikasi saja, multitugas penuh, dan variasi bobot λ~reg~; manfaat supervisi *keypoint* dinyatakan dari selisihnya, termasuk jika manfaatnya nihil.",
"Pembanding ablasi dilaporkan berdampingan: kepala klasifikasi saja, multitugas penuh, dan variasi bobot λ~reg~; manfaat supervisi *keypoint* dinyatakan dari selisihnya, termasuk jika manfaatnya nihil. Evaluasi klasifikasi juga memisahkan dua taraf penilaian: (a) kelayakan ilmiah awal (*scientific feasibility*), yakni bukti adanya daya pisah sinyal CSI jauh di atas peluang acak maupun pembanding tunggal, dan (b) kegunaan operasional (*operational usability*) untuk komunikasi nyata di kelas. Untuk mekanisme penolakan [18], setiap eksperimen wajib melaporkan bersama-sama akurasi keseluruhan tanpa penolakan, cakupan diterima (*accepted coverage*), akurasi selektif (*selective accuracy*) pada segmen yang lolos ambang keyakinan, laju terima palsu (*false accept*), laju tolak palsu (*false reject*), serta waktu inferensi persentil p50 dan p95.")

# ============================================================
# E46 — 3.8.3: persamaan 3.3 pecah 3.3a/3.3b + BOM (ISS-17, ISS-18)
# ============================================================
ganti("E46-3.8.3-intro",
"Tiga perhitungan penunjang dirumuskan lebih dulu agar hasilnya bisa diperiksa ulang. Latensi ujung ke ujung ialah penjumlahan waktu tiap tahap:",
"Tiga perhitungan penunjang dirumuskan lebih dulu agar hasilnya bisa diperiksa ulang. Latensi ujung ke ujung dirumuskan terpisah untuk masing-masing arah karena perbedaan komponennya, dan keduanya diukur pada mode daring serta luring dengan pelaporan persentil p50 dan p95:")

ganti("E46-3.8.3-eq",
"t~total~ = t~segmentasi~ + t~inferensi~ + t~pemetaan~ + t~keluaran~ (3.3)",
"T~1~ = t~CSI-buf~ + t~seg~ + t~inf-tepi~ + t~tel~ + t~peta~ + t~TTS~ + t~audio-dl~ + t~putar~ (3.3a)\nT~2~ = t~rekam~ + t~audio-ul~ + t~ASR~ + t~kamus~ + t~tampil~ (3.3b)")

ganti("E46-3.8.3-follow",
"dengan t~inferensi~ mencakup seluruh model gabungan (Subbab 3.7) dan t~keluaran~ mencakup sintesis ucapan pada arah pertama serta tampilnya representasi isyarat pada arah kedua; anggaran per tahap dan ambang totalnya diuji pada G3 (Tabel 3.5).",
"dengan T~1~ mencakup latensi pasca-akhir segmen isyarat hingga awal pemutaran suara (termasuk varian klip ter-*cache* 26 huruf maupun sintesis langsung) dan T~2~ mencakup akhir ujaran PTT hingga tampilnya representasi SIBI di aplikasi Tauri; anggaran per tahap dan ambang totalnya diuji pada G3 (Tabel 3.5). Biaya purwarupa dihitung dari tabel BOM riil seluruh komponen dengan memisahkan harga pasangan modul ESP32-S3 inti dari total komponen antarmuka lengkap (Persamaan 3.5).")

# ============================================================
# E47 — 3.8.4: butir 2 dan 4 (ISS-15, ISS-16)
# ============================================================
ganti("E47-3.8.4-butir2",
"2. Merekam teks keluaran layanan ASR awan, lalu menghitung akurasi katanya terhadap teks acuan.",
"2. Merekam teks keluaran layanan ASR awan (daring) dan `faster-whisper` (luring) pada frasa uji bahasa Indonesia, lalu melaporkan WER beserta rincian (S, D, I, N) (Persamaan 2.23) dan *exact-match rate* tanpa memakai rumus 1 − WER.")

ganti("E47-3.8.4-butir4",
"4. Mengulang pengukuran pada kedua kandidat mesin (Kokoro ONNX dan MMS-TTS-ind) di server lokal maupun *on-device* ponsel serta jalur pembanding awan, lalu menimbang mutu dan latensinya.",
"4. Mengulang pengukuran pada kandidat mesin (MMS-TTS-ind ONNX sebagai kandidat utama dan Kokoro ONNX sebagai pembanding) di server lokal maupun *on-device* ponsel serta jalur pembanding awan, lalu menimbang mutu dan latensinya.")

# ============================================================
# E48 — Tabel 3.5: G0, G0b, G1, G3, G4 (ISS-09, ISS-22, ISS-23)
# ============================================================
ganti("E48-3.5-G0",
"| G0 | Baseline CSI dan jaringan, akhir M2 | Akuisisi 56 *subcarrier* 1 m ke UDP Rust terbaca stabil; laju sekurang-kurangnya 25 bingkai per detik; paket hilang tidak melampaui 0,1%; pola bergerak terpisah dari diam; audit *checkpoint encoder* selesai | Perbaikan penempatan satu kali; gagal lagi berarti jalur CSI dihentikan dan dilaporkan |",
"| G0 | Baseline CSI dan jaringan, akhir M2 | Akuisisi *subcarrier* valid N~valid~ (LLTF/HT-LTF, *pilot*, `first_word_invalid` diaudit) pada jarak 1 m ke UDP Rust terbaca stabil; laju sekurang-kurangnya 25 bingkai per detik; paket hilang tidak melampaui 0,1%; pola bergerak terpisah dari diam; keterpisahan awal beberapa pose tangan statis teramati; audit sisa *phase drift* Persamaan (2.5) dan audit artefak *encoder* (pemilihan berkas v1/v2, *standardizer*) selesai | Perbaikan penempatan satu kali; gagal lagi berarti jalur CSI dihentikan dan dilaporkan |")

ganti("E48-3.5-G0b",
"| G0b | Audit kompatibilitas representasi *encoder*, setelah G0 atas data pilot (awal T2) | *Probe* linear di atas *embedding* beku: F1 makro 24 huruf statis sekurang-kurangnya 0,30 dan sekurang-kurangnya tiga kali peluang acak; *probe* biner J–Z sekurang-kurangnya 70% [usulan]; kontrol label-acak signifikan (p < 0,05); keputusan jalur masukan tercatat | Jalur fitur turunan gagal maka jalur adapter diuji; keduanya gagal maka skema adaptasi LoRA/pelatihan lanjutan (Subbab 2.5) dan hasilnya dilaporkan sebagai temuan |",
"| G0b | Audit kompatibilitas representasi *encoder*, setelah G0 atas data pilot (awal T2) | *Probe* linear 24 huruf statis dan *probe* sekuensial di atas *embedding* beku: F1 makro sekurang-kurangnya 0,30 dan sekurang-kurangnya tiga kali peluang acak; *probe* biner J–Z sekurang-kurangnya 70% [usulan]; skor label asli melampaui persentil ke-95 distribusi *null* uji permutasi blok/repetisi (p~perm~ < 0,05); perbandingan langsung terhadap Pembanding C tercatat; keputusan jalur masukan tercatat | Jalur A gagal maka Jalur B1/B2 diuji; seluruh jalur delapan fitur gagal maka LoRA/pelatihan lanjutan dijalankan berdampingan dengan Pembanding C (CSI lebih kaya tanpa *bottleneck* 8 fitur) dan hasilnya dilaporkan sebagai temuan |")

ganti("E48-3.5-G1",
"| G1 | Model tepi terkuantisasi dan dua kepala, akhir M8 | Akurasi dalam sesi sekurang-kurangnya 50% (sekitar 13 kali acak 3,8%); F1 makro sekurang-kurangnya 0,45 [usulan]; tidak ada kelas dengan *recall* nol pada himpunan huruf terpilih; melampaui pembanding ablasi kepala tunggal dengan manfaat multitugas dilaporkan; *recall* J dan Z dilaporkan terpisah beserta *confusion* terhadap huruf paling mirip; MPJPE dilaporkan sebagai pemantauan; inferensi terkuantisasi di bawah 100 ms; seluruh ambang difinalkan bersama pembimbing sebelum G1 dinilai | Pangkas himpunan huruf pembeda terkuat, lalu nilai ulang |",
"| G1 | Model tepi terkuantisasi dan dua kepala, akhir M8 | Akurasi dalam sesi sekurang-kurangnya 50% (sekitar 13 kali acak 3,8%) sebagai ambang kelayakan ilmiah awal, bukan klaim siap pakai operasional; F1 makro sekurang-kurangnya 0,45 [usulan]; tidak ada kelas dengan *recall* nol pada himpunan huruf terpilih; melampaui pembanding ablasi kepala tunggal dengan manfaat multitugas dilaporkan; cakupan diterima dan akurasi selektif dilaporkan berpasangan; *recall* J dan Z dilaporkan terpisah beserta *confusion* terhadap huruf paling mirip; MPJPE pada resolusi langkah model dilaporkan sebagai pemantauan; inferensi terkuantisasi di bawah 100 ms; pemangkasan himpunan huruf dilarang memakai informasi data uji; seluruh ambang difinalkan bersama pembimbing sebelum G1 dinilai | Pangkas himpunan huruf pembeda terkuat berbasis data validasi, lalu nilai ulang |")

ganti("E48-3.5-G3",
"| G3 | Integrasi Rust dan mesin ucapan, M11 | Latensi arah 1 tidak melampaui 2 detik dan arah 2 tidak melampaui 3 detik pada jalur utama server lokal (5 detik untuk jalur cadangan *on-device*); TTFA TTS di bawah 100 ms pada frasa uji paling banyak lima kata; *parsing* UDP di bawah 0,2 ms; memori server di bawah 40 MB; suara Indonesia tersedia atau peralihan dilaporkan | Beralih ke mesin alternatif, lalu jalur *on-device* ponsel atau awan; melampaui berarti temuan |",
"| G3 | Integrasi Rust dan mesin ucapan, M11 | Latensi Persamaan (3.3a) Arah 1 tidak melampaui 2 detik dan Persamaan (3.3b) Arah 2 tidak melampaui 3 detik pada jalur utama server lokal (5 detik untuk jalur cadangan *on-device*), diukur daring dan luring dengan pelaporan p50 dan p95; TTFA di bawah 100 ms pada frasa uji paling banyak lima kata pada kondisi terdokumentasi; *parsing* UDP di bawah 0,2 ms; memori server di bawah 40 MB; konfigurasi TTS Indonesia default MMS-TTS-ind ONNX (dengan *pre-cache* 26 huruf tunggal) kecuali Kokoro mendukung bahasa Indonesia sebelum G3 | Beralih ke mesin alternatif, lalu jalur *on-device* ponsel atau awan; melampaui berarti temuan |")

ganti("E48-3.5-G4",
"| G4 | Sintesis kelayakan, akhir M12 | Skor persepsi rata-rata sekurang-kurangnya 3,0 dari 5; validator menyetujui kewajaran; biaya lengkap; rekomendasi TKT/TRL 3–4 tertulis | Hasil negatif tetap dilaporkan; rekomendasi menyatakan posisi lebih rendah beserta alasan |",
"| G4 | Sintesis kelayakan, akhir M12 | Skor persepsi rata-rata sekurang-kurangnya 3,0 dari 5 (dianalisis deskriptif: median, rentang, per partisipan); validator menyetujui kewajaran; BOM biaya lengkap; rekomendasi TKT 3–4 tertulis mengacu pada Permenristekdikti Nomor 42 Tahun 2016 [31] beserta indikator capaian Perdirjen Penguatan Risbang 603/E1.2/2016 | Hasil negatif tetap dilaporkan; rekomendasi menyatakan posisi lebih rendah beserta alasan |")

# ============================================================
# E49 — Tabel 3.6: G0b pada jadwal (ISS-26)
# ============================================================
ganti("E49-3.6-baris2",
"| 2 | T1 Kurasi alfabet SIBI dan kosakata, kalibrasi ruang, protokol, perizinan | | ■ | ■ | ■ | | | | | | | | | | | — |",
"| 2 | T1 Kurasi alfabet SIBI dan kosakata, kalibrasi ruang, protokol, perizinan, perekaman pilot G0b | | ■ | ■ | ■ | | | | | | | | | | | G0b (awal T2 / M4) |")

# ============================================================
# E50 — Tabel 3.7: baris 7, 17, 19 (ISS-07, keputusan terbuka)
# ============================================================
ganti("E50-3.7-baris7",
"| 7 | Sistem koordinat target regresi, skala acuan d~ref~, dan ambang α | Sebelum pelatihan | [PERLU VALIDASI: sistem koordinat dan ambang PCK] |",
"| 7 | Sistem koordinat target regresi, konvensi *handedness*, skala acuan d~ref~, dan ambang α | Sebelum pelatihan | [PERLU VALIDASI: sistem koordinat, *handedness*, dan ambang PCK] |")

ganti("E50-3.7-baris17",
"| 17 | Lokasi sintesis dan pemutaran TTS (keputusan D3: server lokal utama, ponsel cadangan), mesin final, layanan ASR, dan frasa uji | Pada G3 | [PERLU DATA: keputusan final lokasi, mesin, layanan, dan daftar frasa dari uji banding] |",
"| 17 | Prioritas mesin TTS operasional (verifikasi primer: Kokoro v1.0 tanpa suara Indonesia; kandidat utama MMS-TTS-ind ONNX dengan *pre-cache* 26 huruf), lokasi sintesis D3, layanan ASR, dan frasa uji | Pada G3 | [PERLU KONFIRMASI: pergeseran default ke MMS-TTS-ind menunggu persetujuan; keputusan final mesin, lokasi, layanan, dan daftar frasa dari uji banding G3] |")

ganti("E50-3.7-baris19",
"| 19 | Model *deployment* (Pilihan 1: klasifikator saja; Pilihan 2: dua kepala aktif) | Tujuan eksperimen dan hasil ablasi manfaat regresi | [PERLU DATA: keputusan dan dasarnya] |",
"| 19 | Model *deployment* (Pilihan 1: klasifikator saja, kepala regresi dilepas setelah pelatihan; Pilihan 2: dua kepala aktif) | Tujuan eksperimen dan hasil ablasi manfaat regresi | [PERLU KONFIRMASI: teks Subbab 3.5 dan 3.7 mengarah ke Pilihan 1 (klasifikator saja); penguncian final menunggu konfirmasi pembimbing dan hasil ablasi] |")

# ============================================================
# E51 — 3.10: pengelompokan kategori Tabel 3.7 (ISS-30)
# ============================================================
ganti("E51-3.10-intro",
"Sebagian parameter bergantung pada kesepakatan pembimbing, hasil tahap sebelumnya, atau data validasi. Parameter semacam itu dihimpun pada Tabel 3.7 dan ditetapkan lebih dulu sebelum dipakai menilai data uji maupun gerbang terkait.",
"Sebagian parameter bergantung pada kesepakatan pembimbing, hasil tahap sebelumnya, atau data validasi. Parameter semacam itu dihimpun pada Tabel 3.7 dan ditetapkan lebih dulu sebelum dipakai menilai data uji maupun gerbang terkait. Untuk memperjelas batas keputusan, Tabel 3.7 terbagi dua kelompok: baris 1, 13, 14, 16, 17, 19, dan 20 merupakan keputusan desain dan administratif inti yang memerlukan konfirmasi pembimbing, sedangkan baris 2 sampai 12, 15, dan 18 merupakan parameter teknis dan *hyperparameter* yang penetapannya berbasis hasil audit atau data validasi.")

# ============================================================
# E52 — Tabel 3.8: baris 3 dan 8
# ============================================================
ganti("E52-3.8-baris3",
"| 3 | *Embedding encoder* beku tidak memisahkan kelas huruf | Kepala tidak dapat belajar | Jalur adaptasi LoRA dan pelatihan lanjutan; hasilnya dibandingkan apa adanya |",
"| 3 | *Embedding* *encoder* beku tidak memisahkan kelas huruf | Kepala tidak dapat belajar | Uji Jalur B2 (adapter terpandu tugas), LoRA/pelatihan lanjutan, dan Pembanding C (*baseline* CSI temporal lebih kaya tanpa *bottleneck* 8 fitur) secara berdampingan untuk membedakan kegagalan representasi masukan dari kegagalan bobot *encoder*; hasilnya dilaporkan apa adanya |")

ganti("E52-3.8-baris8",
"| 8 | Layanan ucapan tidak memadai, termasuk suara Kokoro belum tersedia | Jalur ucapan terganggu | Beralih ke MMS-TTS-ind ONNX, lalu server lokal atau awan (cadangan D) |",
"| 8 | Layanan ucapan tidak memadai; Kokoro-82M v1.0 terkonfirmasi tanpa suara Indonesia [24] | Jalur ucapan terganggu | MMS-TTS-ind ONNX + *pre-cache* audio 26 huruf tunggal sebagai konfigurasi utama, lalu cadangan server lokal, ponsel, atau awan (cadangan D) |")

# ============================================================
# E53 — Batasan no. 6: TTS utama operasional
# ============================================================
ganti("E53-batasan6",
"6. Sintesis ucapan utama berjalan di server lokal dan audio diputar pada *speaker* node penerima, dengan mesin *on-device* pada ponsel sebagai cadangan; pengenalan ucapan memakai layanan awan dengan faster-whisper lokal sebagai cadangan; pilihan final mesin dan layanan tetap ditetapkan pada gerbang G3.",
"6. Sintesis ucapan utama operasional memakai MMS-TTS-ind di server lokal dan audio diputar pada *speaker* node penerima, dengan mesin *on-device* pada ponsel sebagai cadangan dan Kokoro sebagai pembanding; pengenalan ucapan memakai layanan awan dengan faster-whisper lokal sebagai cadangan; pilihan final mesin dan layanan tetap ditetapkan pada gerbang G3.")

# ============================================================
# E54 — Daftar Pustaka: tanggal akses + [12] WPC + entri 29-31
# ============================================================
ganti("E54-dp-10",
'repositori GitHub. [Online]. Available: https://github.com/ruvnet/RuView, diakses 13 Nov. 2026.',
'repositori GitHub. [Online]. Available: https://github.com/ruvnet/RuView, diakses 14 Nov. 2026.')

ganti("E54-dp-11",
'model card Hugging Face. [Online]. Available: https://huggingface.co/ruvnet/wifi-densepose-pretrained, diakses 13 Nov. 2026.',
'model card Hugging Face. [Online]. Available: https://huggingface.co/ruvnet/wifi-densepose-pretrained, diakses 14 Nov. 2026.')

ganti("E54-dp-12",
'Available: https://docs.ultralytics.com/tasks/pose/ dan https://docs.ultralytics.com/datasets/pose/hand-keypoints/, diakses 8 Nov. 2026.',
'Available: https://docs.ultralytics.com/tasks/pose/ dan https://docs.ultralytics.com/datasets/pose/hand-keypoints/, diakses 14 Nov. 2026. Artefak model juara eksperimen `exp11_huruf24` berasal dari repositori WPC peneliti [PERLU DATA: tag rilis/commit dan hash *checkpoint* exp11_huruf24] agar angka pra-penelitian 97,6% dan mAP50 0,9580 dapat diaudit terpisah dari dokumentasi umum Ultralytics.')

ganti("E54-dp-23",
'repositori GitHub. [Online]. Available: https://github.com/espressif/esp-dl, diakses 25 Okt. 2026.',
'repositori GitHub. [Online]. Available: https://github.com/espressif/esp-dl, diakses 14 Nov. 2026.')

ganti("E54-dp-24",
'dan https://doi.org/10.57967/hf/4329, diakses 25 Okt. 2026.',
'dan https://doi.org/10.57967/hf/4329, beserta berkas VOICES.md v1.0, diakses 14 Nov. 2026.')

ganti("E54-dp-baru",
'[28] R. Likert, "A technique for the measurement of attitudes," *Archives of Psychology*, no. 140, pp. 5–55, 1932.',
'''[28] R. Likert, "A technique for the measurement of attitudes," *Archives of Psychology*, no. 140, pp. 5–55, 1932.

[29] H. F. T. Ahmed, H. Ahmad, K. Narasingamurthi, H. Harkat, and S. K. Phang, "DF-WiSLR: Device-Free Wi-Fi-based Sign Language Recognition," *Pervasive and Mobile Computing*, vol. 69, art. 101289, Nov. 2020, doi: 10.1016/j.pmcj.2020.101289.

[30] Z.-J. Gao, C.-C. Lee, L.-H. Zheng, R.-G. Zhang, and X. Xu, "A Multitask Sign Language Recognition System Using Commodity Wi-Fi," *Mobile Information Systems*, vol. 2023, art. 7959916, pp. 1–11, Feb. 2023, doi: 10.1155/2023/7959916.

[31] Kementerian Riset, Teknologi, dan Pendidikan Tinggi Republik Indonesia, *Peraturan Menteri Riset, Teknologi, dan Pendidikan Tinggi Nomor 42 Tahun 2016 tentang Pengukuran dan Penetapan Tingkat Kesiapterapan Teknologi* (BN 2016 No. 1010) beserta Peraturan Dirjen Penguatan Riset dan Pengembangan Nomor 603/E1.2/2016 tentang Pedoman Indikator Capaian Tingkat Kesiapterapan Teknologi. Jakarta, Indonesia, 2016. [Online]. Available: https://peraturan.bpk.go.id/Details/140468/permenristekdikti-no-42-tahun-2016, diakses 14 Nov. 2026.''')

# ============================================================
# E55 — Log Perubahan gelombang 18 (setelah penanda AKHIR NASKAH)
# ============================================================
ganti("E55-log18",
"<!-- ===== AKHIR NASKAH (jangan hapus penanda ini) ===\n\n## Log Perubahan — Revisi 14 November 2026, gelombang 17",
"""<!-- ===== AKHIR NASKAH (jangan hapus penanda ini) ===

## Log Perubahan — Revisi 14 November 2026, gelombang 18 (revisi verifikasi sumber primer v17 ke v18: 30 isu, temuan audit, tabel, persamaan, diagram)

Permintaan: menerapkan paket perbaikan v17 ke v18 (issue ledger ISS-01 sampai ISS-30) yang seluruh klaim eksternalnya telah diverifikasi langsung ke sumber primer pada 14 November 2026; kaidah bahasa mengikuti skill sempro-mepet; nomor sitasi [1] sampai [28] dipertahankan dengan tiga rujukan baru [29] DF-WiSLR, [30] Wi-SignFi, [31] Permenristekdikti 42/2016; sembilan keputusan terbuka tidak diputuskan sepihak.

- Temuan primer masuk naskah: 2.4 paragraf audit artefak (dua keluarga berkas model.safetensors dan csi-embed-v2 dengan standardizer FP16; NUL-padding header; peringatan SISO; lupa EWC 32,97% pada 2.5); 2.2 struktur wifi_csi_info_t (LLTF 52 vs HT-LTF 56, first_word_invalid, pilot/null/guard); 2.11 dan 3.5 Kokoro-82M v1.0 tanpa suara Indonesia (VOICES.md 14 Nov 2026) sehingga MMS-TTS-ind menjadi kandidat utama operasional dengan pre-cache 26 huruf; 2.10 konteks tolok ukur ESP-DL 69,2 ms (MobileNetV2-0.5 RGB 128x128, bukan model CSI).
- Persamaan: (2.13a) mask efektif gabungan dan (2.13) dijumlahkan per koordinat; (2.14a) kemiripan kosinis konflik gradien; (2.15) menggantikan 2.15′; (2.21)-(2.22) memakai m∗ dengan penahan pembagi; (2.23) tanpa rumus 1 − WER; (2.1) dan (3.1) memakai N_valid; (3.3) dipecah (3.3a) Arah 1 dan (3.3b) Arah 2 dengan pelaporan p50/p95; total 33 persamaan bernomor.
- Metodologi: Jalur A/B1/B2 dan Pembanding C diformalkan pada 2.4 dan 3.7; segmentasi tiga fase (onset, tahan pose, lintasan dinamis); koreksi tafsir overlap 75% dan rentang T = 16 (3,75 s pusat ke pusat; 4,75 s sinyal mentah) beserta eksperimen wajib jendela lebih pendek; G0b uji permutasi blok/repetisi M = 1.000; MPJPE/PCK utama pada resolusi langkah model; anti-kebocoran wajib split sebelum windowing dengan purge gap ≥ W; 1.5.1, 2.5, 3.1 selaras dengan (2.15).
- Sistem: 3.5 spesifikasi protokol audio (PCM 16-bit mono 16 kHz, UDP/TCP-WS, ring buffer PSRAM) dan rantai daya (regulator 500-800 mA, TP4056 load-sharing); 2.13 lapisan Rust vs runtime ML; 2.12 ejaan jari J/Z wajib animasi; 1.1 klaim biaya dipisah (Rp300.000 pasangan inti vs BOM lengkap di G4); 2.15 Tabel 2.3 enam baris dengan kebaruan kombinatif dipersempit.
- Etika dan prosedur: 3.6 butir 4-7 (sinkronisasi dengan PERLU DATA toleransi, pengacakan urutan kartu per blok, audit keypoint khusus J/Z, validator terstratifikasi) dan paragraf etika (persetujuan aksesibel, wali + child assent, retensi video dengan tanggal hapus, risiko re-identifikasi diakui).
- Tabel: 2.3 (6 baris), 2.4 (baris 2 TTS dan 4 radio), 3.2 (baris 8 dan 10), 3.5 (G0, G0b permutasi + Pembanding C, G1 feasibility vs usability + cakupan/selektif, G3 persamaan per arah + MMS-TTS-ind default, G4 Permenristekdikti), 3.6 (baris 2 pilot G0b, gerbang G0b awal T2/M4), 3.7 (baris 7 handedness; baris 17 dan 19 berstatus PERLU KONFIRMASI), 3.8 (baris 3 dan 8); 3.10 pengelompokan keputusan inti vs parameter teknis.
- Diagram: Gambar 2.2 tiga subgraf (akuisisi, pelatihan tiga rute, deployment Pilihan 1); Gambar 3.1 kuantisasi dipindah ke fase T2 (M4-M8) dan keterangan menyebut G0b; Gambar 3.3 cadangan TTS on-device dipindah ke subgraf Arah 1; Gambar 3.5 alur inferensi diubah ke Pilihan 1 (tanpa kepala regresi, dengan mekanisme tolak); Gambar 2.1 dan 3.4 digambar ulang dengan kotak latar putih pada anotasi agar label tidak bertumpuk; keterangan Gambar 3.2 diperjelas ilustrasi sementara.
- Ekspor: sel tabel kini mendukung subskrip/superskrip (d_ref, lambda_cls, lambda_reg tidak lagi tampil mentah); keterangan gambar dirender melalui parser inline; lebar kolom tabel dijamin cukup untuk kata terpanjang (Jumlah, Gerbang, Parameter tidak terpecah); penanda [PERLU KONFIRMASI] ikut tersorot.
- Daftar pustaka: 28 menjadi 31 entri ([29] Ahmed dkk. 2020 DF-WiSLR; [30] Gao dkk. 2023 Wi-SignFi; [31] Permenristekdikti 42/2016 + Perdirjen 603/E1.2/2016); tanggal akses [10], [11], [12], [23], [24] diperbarui ke 14 Nov 2026; [12] ditambah penanda artefak WPC.
- Keputusan terbuka (Tabel 3.7): akhiran judul (#20), deployment Pilihan 1 vs 2 (#19), prioritas TTS (#17), lingkup BOM, komisi etik dan subjek anak, ambang final gerbang dan aturan pemangkasan, variasi (W, H) dan status wajib Pembanding C, perangkat keras final dan enclosure, identitas administratif; semuanya menunggu konfirmasi pembimbing.

## Log Perubahan — Revisi 14 November 2026, gelombang 17""")

# ============================================================
# E56 — Gambar 3.5: alur inferensi classifier-only (Pilihan 1) (ISS-12)
# ============================================================
MERMAID_35_LAMA = """```mermaid
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
```"""

MERMAID_35_BARU = """```mermaid
flowchart LR
    accTitle: Alur inferensi langsung pada ESP32-S3 menurut deployment Pilihan 1
    accDescr: Bingkai promiscuous masuk ke penyangga geser di PSRAM dengan pemeriksaan subcarrier valid dan first_word_invalid; segmentasi perangkat memisahkan onset Delta-CSI, jendela tahan pose untuk huruf statis, dan jendela lintasan untuk J dan Z; masukan diekstraksi sesuai rute hasil audit; model terkuantisasi berisi encoder, modul temporal, dan kepala klasifikasi saja karena kepala regresi dilepas sesuai Pilihan 1; keluaran di atas ambang ditampilkan dan dikirim via UDP ke server Rust, keluaran di bawah ambang ditolak tanpa memicu suara.

    subgraph R1["Akuisisi dan segmentasi"]
        direction TB
    CSI["Callback CSI promiscuous<br/>(subcarrier valid, filter MAC)"]
    BUF["Penyangga geser<br/>CSI di PSRAM"]
    SEG["Segmentasi: onset,<br/>tahan pose / lintasan"]
    FT["Masukan teraudit<br/>(Jalur A / B / C)"]
    CSI --> BUF
    BUF --> SEG
    SEG --> FT
    end
    subgraph R2["Inferensi Pilihan 1"]
        direction TB
    MOD["Model int8/fp16: encoder +<br/>temporal + klasifikasi"]
    DEC{"Keyakinan di<br/>atas ambang?"}
    OUT["Tampil + UDP label/skor<br/>ke server Rust"]
    RJ["Tolak: tidak dikenali<br/>(tanpa suara)"]
    MOD --> DEC
    DEC -- "ya" --> OUT
    DEC -- "tidak" --> RJ
    end
    R1 --> R2
```"""

ganti("E56-3.5-mermaid", MERMAID_35_LAMA, MERMAID_35_BARU)

ganti("E56-3.5-caption",
"Gambar 3.5 Inferensi langsung pada ESP32-S3 dengan model gabungan encoder, modul temporal, dan dua kepala; seluruh waktunya diukur, bukan dijanjikan",
"Gambar 3.5 Alur inferensi langsung pada ESP32-S3 menurut rancangan *deployment* Pilihan 1 tanpa kepala regresi, dengan segmentasi tiga fase dan mekanisme tolak; seluruh latensi dan memori diukur langsung pada perangkat, bukan dijanjikan")

# ============================================================
# E57 — 3.7: koreksi rentang T = 16 (3,75 s pusat-ke-pusat; 4,75 s mentah) (ISS-03)
# ============================================================
ganti("E57-3.7-t16",
"Panjang T ditetapkan 16 langkah per segmen (usulan; difinalkan dari distribusi durasi segmen pada data pilot T2), menutup segmen hingga sekitar empat detik pada lompatan 0,25 detik.",
"Panjang T ditetapkan 16 langkah per segmen (usulan; difinalkan dari distribusi durasi segmen pada data pilot T2 tanpa memakai data uji); pada lompatan H = 0,25 detik, selisih pusat jendela pertama ke langkah ke-16 adalah (16 − 1) × 0,25 = 3,75 detik, sedangkan rentang sinyal mentah yang tercakup dari awal jendela pertama hingga akhir jendela ke-16 mencapai 4,75 detik untuk segmen valid penuh.")

# ============================================================
# Selesai
# ============================================================
DST.write_text(s, encoding="utf-8")
print(f"OK — {len(log)} suntingan diterapkan -> {DST}")
for nama in log:
    print(" -", nama)
