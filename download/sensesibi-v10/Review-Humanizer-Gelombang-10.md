# Review Humanizer Gelombang 10 — Versi Ringkas ±40 Halaman

**Tanggal:** 10 November 2026 · **Pemicu:** permintaan pemilik — "ringkas lagi menjadi sekitar 40 halaman docx dan pdf. pakai skill 'https://github.com/apissaj/humanizer-id' dan 'https://drive.google.com/file/d/1dzISJm-6gsqKGI-JHXIMk93duPbwnKUO'" · **Jenis pekerjaan (taksonomi sempro-mepet):** Tulis ulang + pemadatan struktur; register korpus dan kaidah humanizer-id Mode Akademik Ketat dijaga pada seluruh prosa baru.

## 1. Lingkup dan metode

1. Skill dari Google Drive diunduh dan diekstrak: **sempro-mepet** (register korpus 87 proposal, struktur BAB I–III, anatomi blok teori, prosedur me- pasif, QC). Skill humanizer-id tetap memakai repo `/tmp/humanizer-id` (gelombang 7–9).
2. Seluruh naskah 91-hlm dibaca ulang; rencana pemadatan disusun agar nomor subbab BAB II dan penanda integritas (angka, sitasi, [PERLU]) tidak berubah makna.
3. Pemadatan dilakukan pada tingkat paragraf, gambar, tabel, dan format — bukan pada fakta. Pipeline build versi lengkap tidak tersentuh (salinan JS terpisah `parse_md_ringkas.js`/`generate_docx_ringkas.js`).

## 2. Perubahan struktur (dengan justifikasi)

| Elemen | Versi 91-hlm | Versi ringkas | Justifikasi |
|---|---|---|---|
| Halaman | 91 | **44** | target "sekitar 40"; dibawah 40 menuntut pelepasan sitasi/prosedur |
| Subbab BAB II | 13 | 11 | 2.1+2.2 digabung (satu tema domain); 2.13 BoM ganda dengan Tabel 3.1 |
| Subbab BAB III | 3.1–3.11 + 34 subsubbab | 3.1–3.11 + 6 subsubbab prosedur | subsubbab tahap/protokol/pengolahan dilebur jadi prosa mengalir; prosedur pengujian 3.8.1–3.8.6 dipertahankan (register korpus: langkah bernomor) |
| Gambar | 10 | 3 inti | jalur gagal, alur evaluasi, distilasi data, distilasi pelatihan, topologi, enclosure, alur perangkat lunak diwakili Tabel 3.5, prosa 3.2/3.5/3.7, dan Tabel 3.3 pinout |
| Tabel BAB III | 9 | 8 (Tabel 3.1–3.8) | matriks komponen arsitektur ganda dengan Tabel 3.1-3.2 + prosa 3.5 |
| Tabel parameter | 29 baris | 14 baris terkelompok | butir sejenis digabung; seluruh kebutuhan data tetap terwakil (penanda PERLU 47→31) |
| Tabel penelitian terdahulu | 20 baris | 11 baris | baris yang dikutip di prosa dipertahankan |
| Daftar Pustaka | 94 entri, 1,5 spasi 12 pt | 93 entri, 1 spasi 10 pt | [71] keluar karena kalimat latar akuisisi dipadatkan; klaim dukungan CSI resmi tetap dari esp-csi [31] |
| Daftar isi | heading 1-3 | heading 1-2 | versi ringkas |

## 3. Integritas (verifikasi skrip `verifikasi_ringkas.py`)

- **Sitasi:** 268 kutipan, 93 unik, urut kemunculan 1–93 ✓; seluruh entri DP identik karakter-per-karakter dengan naskah asli ✓.
- **Angka:** token numerik multiset dibandingkan — nol temuan baru (satu positif palsu "91" berasal dari frasa meta "(91 halaman)" pada catatan penyusunan yang tidak diekspor ke DOCX).
- **Cermin rumusan–tujuan:** 3:3, urutan dan objek konsisten ✓.
- **Penanda [PERLU DATA]/[PERLU ILUSTRASI]:** 31 (dari 47) — penurunan murni dari penggabungan butir tabel parameter sejenis; tidak ada kebutuhan data yang hilang.
- **Kebocoran format:** nol asterisk literal (ditemukan 3 pada draf, dibersihkan), nol halaman kosong (cek piksel 13 halaman kunci), gambar tertanam 3/3, tabel jadwal M1–M14 + 20 tanda ■ utuh lintas halaman, nol rujukan nomor lama (Subbab 2.12/2.13, Tabel 3.9, Gambar 3.4–3.10) di tubuh naskah.

## 4. Keputusan pemadatan yang perlu diketahui pemilik

1. **44 hlm, bukan tepat 40.** Turun 52% dari 91 hlm. Menembus 40 menuntut salah satu: memotong sitasi (dari 93), memotong prosedur pengujian 3.8, atau memotong baris tabel parameter/risiko — semuanya menurunkan kekuatan sempro. Bila pemilik tetap ingin ≤40, kandidat potongan berikutnya: 8–10 sitasi preseden kepekaan (dipertahankan di prosa ringkas), tabel jadwal 3.6 digabung dengan gerbang, atau daftar pustaka 9 pt.
2. **Dua versi kini hidup berdampingan** — ringkas 44-hlm untuk pengumpulan/sempro dan lengkap 91-hlm untuk pembimbingan; keduanya dari sumber markdown berbeda dan pipeline build terpisah.
3. **Rujukan silang di dalam Gambar 3.2 dirender ulang** ("Subbab 2.7") karena penggabungan subbab BAB II; dua varian .mmd tersimpan di `diagram/`.
4. **Penanda PERLU di tabel parameter digabung** (mis. tiga butir kriteria pemangkasan menjadi satu baris); daftar lengkap kebutuhan data versi 91-hlm tetap ada di naskah lengkap.

## 5. Rekomendasi tindak lanjut

1. Isi identitas sampul (`[PERLU DATA: nama penulis]` dsb.) sebelum pengumpulan.
2. Jalankan "Update Field" pada daftar isi setelah penyuntingan di Word/WPS (nomor halaman TOC).
3. Bila dosen menilai 44 hlm masih panjang, bawa laporan ini ke diskusi: potongan berikutnya berada pada daftar sitasi dan prosedur, bukan pada redaksi.
