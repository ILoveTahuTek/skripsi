# Catatan Penyusunan Proposal DPJ-4

**Judul:** Alat Pembelajaran Isyarat SIBI Tanpa Kamera Berbasis Wi-Fi Channel State Information pada ESP32: Studi Kelayakan Umpan Balik Latihan bagi Pembelajar Pendengar

Disusun 23 Oktober 2026 dengan bantuan AI (Claude). Semua isi berasal dari bahan pemilik (draf DPJ-4, dossier, transkrip council) dan dari metadata DOI yang dicek langsung. Data, angka, atau rujukan yang tidak tersedia tidak dikarang, tetapi ditandai `[PERLU DATA: …]` atau `[PERLU RUJUKAN: …]`.

## 1. Isi folder

| Berkas | Isi |
|---|---|
| `bab1-pendahuluan.md` | BAB I, sitasi IEEE bernomor |
| `bab2-kajian-pustaka.md` | BAB II, sitasi IEEE bernomor |
| `bab3-metodologi.md` | BAB III, sitasi IEEE bernomor, dua diagram Mermaid |
| `daftar-pustaka.md` | 34 rujukan, urut sesuai kemunculan pertama |
| `_berkunci/` | Salinan ketiga bab dengan sitasi berupa kunci `[@kunci]`. Pakai versi ini bila menambah atau menghapus sitasi, lalu nomori ulang. |
| `_lembar-fakta.md` | Sumber fakta, istilah, dan desain penelitian yang dipakai semua bab |
| `_metadata-doi.json` | Metadata DOI hasil pengecekan |
| `_nomori-sitasi.py` | Skrip penomoran ulang sitasi dan pembuat daftar pustaka |
| `laporan-penanda.md` | Daftar semua penanda `[PERLU …]` yang tersisa |
| `_laporan-penanda.py` | Skrip pembuat `laporan-penanda.md` |
| `_berkunci/bab3-metodologi.sebelum-padat.md` | Cadangan BAB III sebelum dipadatkan; hapus bila versi padat sudah disetujui |

## 2. Jenis pekerjaan per bab

Ketiga bab berjenis **Tulis**, yaitu teks baru yang disusun dari bahan pemilik. Setiap bab ditulis, lalu ditinjau dari tiga sudut (kesetiaan fakta, bahasa dan register, sudut pandang penguji), direvisi, dan terakhir dicek konsistensinya lintas bab.

## 3. Keputusan yang dikunci pemilik

- Cakupan **SIBI saja**. BISINDO disebut sebagai konteks dan kerja lanjutan.
- Framing: alat latihan bagi pembelajar pendengar. Latar belakang berangkat dari masalah sosial dan pendidikan, bukan dari teknologi.
- Format sempro standar tiga bab: tanpa tabel usulan judul, rencana biaya, dan tabel risiko.
- Sitasi IEEE numerik.

## 4. Perubahan penting dibanding draf DPJ-4 lama

| Aspek | Draf lama | Sekarang |
|---|---|---|
| Bahasa | SIBI dan BISINDO | SIBI saja, angka 1,9% (BRIN) dibuka di BAB I beserta alasan memilih SIBI |
| Orientasi | Pengenalan gestur untuk prasarana edukasi | Umpan balik latihan bagi pembelajar pendengar |
| Peran kamera | "Pelabelan *ground truth*" | Label kelas berasal dari kartu pemandu; MediaPipe hanya memverifikasi batas segmen, menyaring kualitas, dan membantu diagnosis |
| Makna "benar" | Tidak dibatasi | "Cocok" hanya berarti lintasan lengan, tubuh atas, dan kepala sesuai; bentuk jari tidak dinilai; ada penolakan berbasis skor keyakinan |
| Gerbang | Satu gerbang Delta-CSI di minggu ke-3 | G0–G4; ambang numerik tidak ditulis sebagai janji |
| Pembagian data | Validasi silang per sesi | Pembagian data temporal per blok, lintas sesi, *leave-one-subject-out*, *leave-one-room-out*, dan pengguna baru |
| Uji pengguna | Tidak ada | 3–5 pemula; uji awal dan akhir dinilai validator; kuesioner persepsi pada kondisi kamera menyala dan mati (urutan acak); analisis deskriptif |
| Keterlibatan tunarungu | Tidak ada | Validator penutur tunarungu wajib |
| MQTT/Home Assistant | Dipakai | Dihapus; umpan balik ditampilkan di *dashboard* |

## 5. Koreksi rujukan hasil pengecekan DOI

Semua DOI dicek langsung lewat doi.org pada 23 Oktober 2026.

- **BlazePose:** DOI di dossier (`arXiv:2004.03486`) ternyata menunjuk ke paper lain. Yang benar `arXiv:2006.10204`.
- **Judul yang keliru di draf lama:**
  - Shang dan Wu: judul benarnya "…with Multiple Wi-Fi Devices".
  - Sanjaya dkk.: judul benarnya "…Deep Learning Techniques for Image Processing". Karena itu tinjauan ini tidak dipakai untuk klaim "belum ada pendekatan nirkabel".
  - Judul Cai dkk., Kindy dkk., Sebastian dkk., Wiguna dan Rojali, dan MediaPipe juga diperbaiki.
- **Daftar penulis:** Rodríguez-Correa dkk. dan SignFi diperbaiki.
- **Volume:** DF-WiSLR terbit di vol. 69, bukan 68.
- **Isi:** WiASL memakai perangkat Wi-Fi komersial, bukan kamera.
- **Widar3.0:** Crossref hanya menyimpan versi *early access* (2021). Daftar pustaka memakai data terbitan cetak (vol. 44, no. 11, pp. 8671–8685, 2022), yang tidak tercatat di metadata DOI. **Cocokkan dengan IEEE Xplore.**
- **Belum dicek ulang di sesi ini:**
  - URL berita BRIN (dari dossier);
  - rilis Kemenko PMK (URL belum ada);
  - fakta teknis RuView (ADR-018, ADR-079, kalibrasi 600 *frame* + 8 *anchor*, mode privasi), yang semuanya berasal dari dossier dan belum dicocokkan langsung dengan repositori.
- **Kamus SIBI** masih berupa penanda, karena data terbitan resminya belum ada.

## 6. Keputusan yang masih terbuka (bawa ke bimbingan)

1. **5–8 isyarat versus pemangkasan 3–5 isyarat.** Rumusan masalah dan batasan menyebut 5–8, sedangkan cabang gagal G2 memangkas menjadi 3–5. Perlu diputuskan apakah rumusan cukup menyebut "5–8, dapat dipangkas menjadi 3–5".
2. **Klausa empati pada batasan 6.** Kalimat aspirasi empati di bagian manfaat sudah dihapus, jadi klausa "empati tidak diukur secara psikometrik" kini tidak punya acuan lain di BAB I. Pilihannya: hapus klausa itu, atau kembalikan satu kalimat aspirasi empati.
3. **Istilah "separabilitas fisik".** Kata ini tidak ada di KBBI. Alternatifnya "keterpisahan fisik", dan bila diganti, harus diganti di ketiga bab sekaligus.
4. **"Tunarungu" versus "Tuli".** Proposal memakai "tunarungu" sesuai KBBI. Komunitas sering lebih memilih "Tuli", jadi sebaiknya dikonfirmasi dengan pembimbing dan validator.
5. **Subbab Kerangka Berpikir di BAB II.** Belum dibuat, karena tergantung pedoman prodi.
6. **Sistematika tiga bab.** Perlu dikonfirmasi bahwa proposal di prodi memang cukup BAB I–III.
7. **Uji sinkronisasi T0 tanpa partisipan.** Ini keputusan rancangan yang ditambahkan saat revisi lintas bab dan perlu disetujui pembimbing.
8. **Redaksi rumusan masalah no. 3.** Redaksi saat ini mengikuti lembar fakta. Peninjau menilai frasa "umpan balik latihan" belum operasional dan mengusulkan tiga alternatif. Ketiganya mengubah objek, jadi tujuan no. 3 harus ikut diubah:
   - a) "…ditinjau dari perubahan skor peragaan sebelum dan sesudah latihan, latensi umpan balik, persepsi kenyamanan pengguna, dan penilaian validator penutur tunarungu?"
   - b) "…ditinjau dari kesesuaian keputusan sistem dengan penilaian validator penutur tunarungu pada peragaan pemula, latensi, laju deteksi palsu, dan persepsi kenyamanan pengguna?" (paling selaras dengan BAB III saat ini)
   - c) "…ditinjau dari perubahan ketepatan peragaan menurut rubrik validator penutur tunarungu, latensi dan keandalan operasional sistem, serta persepsi kenyamanan pengguna?"

## 7. Penanda yang masih harus diisi

Daftar lengkapnya ada di `laporan-penanda.md`, dikelompokkan menurut pihak yang mengisi dan disertai lokasi berkas:baris. Laporan itu dibuat ulang dengan `python _laporan-penanda.py` setiap kali ada penanda yang diisi. Per 23 Oktober 2026 masih ada 77 penanda unik (98 kemunculan): 53 PERLU DATA dan 24 PERLU RUJUKAN.

Parameter rancangan BAB III yang baru ditetapkan menjelang eksperimen, seperti ambang gerbang, pembagian data, durasi, rubrik, dan kuesioner, kini terkumpul di **Tabel 3.6 (Subbab 3.10)**. Prosa cukup merujuk "(Tabel 3.6, butir n)".

## 8. Daftar istilah yang dipakai

Wi-Fi *Channel State Information* (CSI) · Sistem Isyarat Bahasa Indonesia (SIBI) · Bahasa Isyarat Indonesia (BISINDO) · tunarungu · pengisyarat · pembelajar pendengar · validator penutur tunarungu · isyarat terisolasi · umpan balik · *dataset* · *subcarrier* · estimasi pose · *keypoint* / *landmark* · klasifikator · *Support Vector Machine* (SVM) · *one-dimensional Convolutional Neural Network* (1D-CNN) · gerbang keputusan · node pemancar (TX) / node penerima (RX) · *dashboard* · sumber terbuka · pembagian data temporal · *leave-one-subject-out* · *leave-one-room-out* · laju pencuplikan (*sampling rate*).

## 9. Catatan teknis

- **Menomori ulang sitasi** setelah mengedit:
  1. Sunting berkas di `_berkunci/` (sitasi `[@kunci]`).
  2. Salin berkas itu ke folder `penomoran/` (atau folder kosong lain).
  3. Jalankan `python _nomori-sitasi.py penomoran`.

  Skrip menulis ulang ketiga bab di folder tersebut dengan nomor IEEE dan membuat `daftar-pustaka.md`. Daftar kunci dan entri IEEE-nya ada di dalam skrip. Kunci baru harus ditambahkan dulu ke kamus `REF` di skrip. Kalau mengedit langsung versi bernomor, nomor dan urutan daftar pustaka harus disesuaikan manual.
- **Diagram Mermaid** (Gambar 3.1 dan 3.2) tampil di penampil Markdown yang mendukung Mermaid. Untuk Word, gambar ulang di draw.io dengan struktur yang sama.
- **Panjang naskah:** BAB I sekitar 2.400 kata, BAB II sekitar 4.000 kata, BAB III sekitar 5.100 kata termasuk tabel dan diagram (prosa saja sekitar 2.900 kata).
- **Pemadatan BAB III:** Sebelum dipadatkan, BAB III sekitar 6.300 kata. Bagian yang mengulang BAB II diganti rujukan subbab, daftar prosedur dirampingkan, dan penanda keputusan rancangan dipindah ke Tabel 3.6. Hasilnya diverifikasi dari tiga sudut: kesetiaan isi, bahasa, dan konsistensi lintas bab. Kunci sitasi, angka wajib, tabel, dan diagram tetap utuh.
- **Kalimat *dashboard* di BAB I 1.1:** "skor keyakinannya" dihapus agar sama dengan lembar fakta dan BAB III, yang hanya menyebut isyarat terdeteksi dan kecocokannya.
- **Rujukan yang tidak dipakai:** Chadha dkk. (laporan WHO) dihapus dari BAB I karena dinilai sebagai angka hiasan yang memutus alur, sehingga tidak masuk daftar pustaka.
