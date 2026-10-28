# Catatan Pengemasan — translator-sibi-final

**Tanggal:** 28 Oktober 2026 · **Sumber:** `draft-final.md` hasil suntingan Claude (dikembalikan pemilik via Drive) + skill `sempro-mepet` & `naskah-id` (arah pakai dari pemilik)

## 1. Isi paket

| Berkas | Keterangan |
|---|---|
| `draft-final.md` | Naskah final hasil Claude: baris 1–981 = naskah (judul baru + BAB I–III + DP [1]–[80]); setelah penanda `AKHIR NASKAH` = Log Perubahan + Daftar Temuan + Pernyataan verifikasi (TIDAK dikonversi ke DOCX) |
| `Proposal-Studi-Kelayakan-Purwarupa-SIBI-CSI-ESP32S3.docx` | **Deliverable utama** — 68 hlm A4, TNR 12 pt, spasi 1,5, margin 4-3-3-3, sampul judul baru 5 baris, TOC 64 entri, 9 tabel tiga-garis, 8 gambar 14 cm, 44 penanda `[PERLU DATA]` tersorot (6 sampul + 38 tubuh), DP 80 entri |
| `Pratinjau-Proposal-Studi-Kelayakan-Purwarupa-SIBI.pdf` | Pratinjau PDF 68 hlm |
| `_kerja/` | Jejak Claude (`_kerja/draft-final.sebelum-selaras.md`, hasil-workflow.json, chunk c0–c8, cek.py) + `naskah-untuk-docx.md` (naskah murni hasil pemisahan dari log) + `split/` (4 berkas bab untuk generator) |

## 2. Judul baru (keputusan pemilik, 28 Okt 2026)

STUDI KELAYAKAN PURWARUPA SISTEM PENERJEMAHAN DUA ARAH ANTARA SISTEM ISYARAT BAHASA INDONESIA (SIBI) DAN TEKS ATAU UJARAN BAHASA INDONESIA BERBASIS WI-FI CHANNEL STATE INFORMATION (CSI) DENGAN INFERENSI MODEL PADA ESP32-S3 DAN PEMROSESAN BAHASA PADA SERVER UNTUK KOSAKATA TERBATAS

Terpasang: sampul (5 baris, menggantikan judul terkunci lama) — mengikuti `draft-final.md`. Penutup latar belakang, rumusan no. 1 & 3, tujuan no. 1 & 3 sudah diselaraskan Claude dengan judul baru.

## 3. Verifikasi sebelum dan sesudah bangun DOCX

**Invarian mandiri (naskah vs naskah-sumber):** 44 penanda `[PERLU DATA]` · DP [1]–[80] lengkap · 8 blok mermaid verbatim · caption Gambar 3.1–3.8 urut · judul baru di baris 1 · angka jangkar identik (`26+9` = singkatan prompt; bentuk naskah "26 huruf … 9 angka" identik di 4 lokasi) · diff 76 baris (7,8%) konsisten dengan Log Perubahan Claude.

**Skill `naskah-id` (`periksa.py`):** 6 temuan — 4× penghubung gaya (AI-17) + 2 positif palsu lama yang diterima sejak Task 17 ("F1 makro" istilah metrik; "Respon" judul asli paper [9]). **Tidak ada galat EYD baru.**

**Skill `sempro-mepet`:** standar struktur/register — naskah sudah memenuhinya (disusun dengannya); pekerjaan sesi ini adalah *pengemasan*, bukan penulisan.

**Ekspor:** postcheck 0 galat (1 peringatan lama: spasi tabel 9 pt) · qa_ekspor 8/8 gambar 14,0 cm tanpa pemangkasan (hlm 31–50) + 14 spot-check teks OK · VLM: sampul bersih (judul 5 baris utuh), halaman Tabel 3.6 bersih.

## 4. Sisa keputusan pemilik (tidak disentuh siapa pun)

1. **44 penanda `[PERLU DATA]`** — 6 sampul + 32 BAB I–III (identitas, perangkat, layanan awan, dst.) + 27 Tabel 3.6 (parameter rancangan, menunggu pembimbing/hasil T0–T4).
2. **Tabel 2.2 baris 17 + 2.11 ¶3** masih frasa judul lama — sel tabel terkunci saat penyuntingan Claude (lihat Daftar Temuan draft-final.md).
3. **"ujaran" (judul) vs "ucapan" (prosa)** — sinonim; menunggu keputusan pemilik untuk penyeragaman.
4. **±40 temuan Claude** di Daftar Temuan `draft-final.md` (istilah *kata-level*/*chip*/*router*, urutan tampil-kirim, ketidakseragaman diagram↔prosa, dst.) — semuanya dibiarkan sesuai protokol minimal-intervensi.
5. **6+1 konfirmasi pembimbing** (gaya sitasi IEEE, ambang G2/G3, dua ruang mitra, token validator, jalur ucapan awan, Kaggle, jumlah bab sistematika).
6. **Update Field** daftar isi di Word/WPS setelah dokumen diedit (petunjuk tercetak di bawah daftar isi).
