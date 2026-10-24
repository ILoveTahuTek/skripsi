# Catatan Pengemasan Dokumen Terstruktur DPJ-4 SIBI-CSI

Dibuat 24 Oktober 2026. Pekerjaan: **pengemasan/kompilasi** — menyusun materi
`sempro/dpj4-sibi-csi` (23 Oktober 2026) menjadi satu dokumen terstruktur dalam dua format.
**Tidak ada satu kata pun teks bab yang diubah**; seluruh isi disalin verbatim dari materi
(kesetiaan diverifikasi otomatis, lihat bagian Verifikasi).

## 1. Berkas keluaran

| Berkas | Isi |
|---|---|
| `Proposal-Sempro-DPJ4-SIBI-CSI.docx` | Dokumen utuh: sampul → daftar isi (romawi kecil i–iii) → BAB I–III + Daftar Pustaka (arab mulai 1); 49 halaman A4 |
| `Proposal-Sempro-DPJ4-SIBI-CSI.md` | Markdown terpadu: blok identitas + BAB I–III + Daftar Pustaka, konten identik verbatim dengan DOCX |
| `assets/gambar-3.1.png`, `assets/gambar-3.2.png` | Kedua diagram BAB III siap cetak (hasil gambar ulang, struktur dan teks simpul sama dengan kode Mermaid sumber) |
| `catatan-pengemasan.md` | Berkas ini |

## 2. Keputusan pengemasan (docx)

- **Gaya**: skripsi Indonesia — Times New Roman 12pt, spasi 1,5, margin kiri 4 cm atas/kanan/bawah 3 cm, rata kiri-kanan dengan indentasi baris pertama 1,25 cm.
- **Sampul**: resep akademik R5 (Clean White): label "PROPOSAL PENELITIAN", judul kapital tiga baris, tabel identitas bergaris bawah. Seluruh nilai identitas berupa penanda `[PERLU DATA: …]` tersorot kuning karena belum tersedia di materi.
- **Daftar isi**: bidang TOC otomatis kedalaman BAB–subbab–anak subbab (55 entri). Nomor halaman pada berkas masih **estimasi placeholder** — di Word klik kanan daftar isi → *Update Field* → *Update entire table* agar mutakhir.
- **Nomor halaman**: sampul tanpa nomor; daftar isi romawi kecil (i, ii, iii) rata tengah; isi arab mulai 1 rata kanan.
- **Tabel** (8 buah): tiga-garis akademik — keterangan di atas rata kiri (nomor tebal), kepala 9pt tebal tengah, isi 9pt; baris tidak terpotong halaman, kepala berulang lintas halaman.
- **Gambar** (2 buah): dua jalur tata letak ulang dari kode Mermaid (perataan otomatis Mermaid menghasilkan rasio 1:7,7 yang tak muat halaman; sesuai catatan materi, "untuk Word, gambar ulang … dengan struktur yang sama"). Simpul, teks, jalur, dan label lolos/gagal/pelatihan identik.
- **Penanda** `[PERLU DATA: …]`/`[PERLU RUJUKAN: …]`: 98 kemunculan, semuanya **tersorot kuning** agar mudah dicari (Ctrl+F "PERLU") saat mengisi.
- **Sitasi IEEE `[n]`** dan **daftar pustaka 34 entri** (indentasi gantung) apa adanya.

## 3. Hasil verifikasi otomatis

- Sinkron konten sumber → DOCX: **568/568 unit teks ditemukan** (pemeriksaan pandoc round-trip).
- postcheck.py (skill docx): **0 error**; 1 peringatan spasi = desain tabel 9pt (pola yang sama dengan DPJ terdahulu yang lolos).
- Inspeksi visual halaman kunci (sampul, daftar isi, awal BAB I, Tabel 2.2, Gambar 3.1, Tabel 3.5, Daftar Pustaka): lolos tanpa cacat.
- Jumlah penanda: 98 kemunculan (16 BAB I, 39 BAB II, 39 BAB III, 4 Daftar Pustaka) — cocok dengan `laporan-penanda.md` materi.

## 4. Temuan lint bahasa (dilaporkan, TIDAK diubah)

Menjalankan `periksa.py` (skill naskah-id) pada 12.043 kata menghasilkan 8 temuan:

- **1 temuan kaidah genuin**: koma sebelum "sehingga" pada kalimat "…bentuk jari yang tepat**, sehingga** peragaan…" (Subbab 3.7.6). EYD V tidak memakai koma sebelum *sehingga* bila anak kalimat mengikuti induk. Siap diperbaiki satu hapusan koma bila pemilik setuju.
- 2 positif palsu: "di **antara** 5–8 kelas" (preposisi, bukan konjungsi antara…dan) dan "skor F1 **makro**" (kata mandiri, bukan bentuk terikat).
- 5 catatan gaya (AI-17): penghubung "Oleh karena itu" muncul 5 kali — berjauhan, bukan gerombolan; boleh dibiarkan.

## 5. Yang perlu dilakukan pemilik

1. Isi identitas sampul (nama, NIM, program studi, universitas, pembimbing, tahun) — semua tersorot kuning.
2. Di Word: perbarui bidang daftar isi setelah pengisian selesai.
3. Isi 98 penanda `[PERLU …]` sesuai prioritas `laporan-penanda.md` (termasuk 2 penanda di Daftar Pustaka: URL rilis Kemenko PMK dan data terbitan *Kamus SIBI*).
4. Bawa ke bimbingan 8 keputusan terbuka pada `catatan.md` materi (Subbab 6), khususnya redaksi rumusan masalah no. 3 dan istilah "separabilitas fisik".
