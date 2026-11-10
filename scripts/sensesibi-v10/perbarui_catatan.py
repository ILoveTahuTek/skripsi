#!/usr/bin/env python3
"""Perbarui catatan-pengemasan.md untuk gelombang 10 (versi ringkas)."""
from pathlib import Path

P = Path("/home/z/my-project/download/sensesibi-v10/catatan-pengemasan.md")
s = P.read_text(encoding="utf-8")

header_lama = """# Catatan Pengemasan — sensesibi-v10

**Tanggal:** 10 November 2026 (gelombang 9) · **Pemicu:** Agent Brief v10 Master (gelombang 6, 9 Nov) + penyuntingan humanizer-id (gelombang 7–9, 10 Nov) · **Skill:** sempro-mepet + naskah-id (arah pakai pemilik), poteto-mode untuk alur kerja, GEPA pada kalimat kritis, humanizer-id Mode Akademik Ketat (gelombang 7–9)"""

header_baru = """# Catatan Pengemasan — sensesibi-v10

**Tanggal:** 10 November 2026 (gelombang 10) · **Pemicu:** permintaan pemilik "ringkas lagi menjadi sekitar 40 halaman docx dan pdf" dengan skill humanizer-id dan sempro-mepet · **Skill:** humanizer-id (Mode Akademik Ketat) + sempro-mepet (register korpus sempro BAB I-III, diunduh dari Google Drive) + naskah-id (arah pakai pemilik)"""

assert header_lama in s, "header lama tak ditemukan"
s = s.replace(header_lama, header_baru)

# Sisipkan dua baris berkas ringkas ke tabel isi paket (sesudah baris PDF lengkap)
baris_pdf = "| `Proposal-SenseSIBI-Studi-Kelayakan-v10.pdf` | Pratinjau PDF 91 hlm (nomor halaman daftar isi terisi setelah \"Update Field\" di Word/WPS — sama seperti perilaku pratinjau versi sebelumnya) |"
assert baris_pdf in s, "baris pdf tak ditemukan"
tambahan = baris_pdf + """
| `Proposal-SenseSIBI-v10-ringkas.md` | **Naskah ringkas sumber tunggal (gelombang 10):** BAB I–III + Daftar Pustaka [1]–[93] + Log Perubahan gelombang 1–10 |
| `Proposal-SenseSIBI-Studi-Kelayakan-v10-ringkas.docx` | **Deliverable utama versi ringkas** — 44 hlm A4, TNR 12 pt, spasi 1,5, sampul SenseSIBI, TOC bidang level 1-2, 12 tabel tiga-garis, 3 gambar inti 14 cm, Daftar Pustaka satu spasi 10 pt, 31 penanda `[PERLU DATA]`/`[PERLU ILUSTRASI]` tersorot |
| `Proposal-SenseSIBI-Studi-Kelayakan-v10-ringkas.pdf` | Pratinjau PDF versi ringkas 44 hlm |
| `assets-ringkas/gambar-3.1..3.3.png` | 3 diagram inti versi ringkas; Gambar 3.2 (arsitektur) dirender ulang agar rujukan "Subbab 2.7" di dalam gambar tetap sahih |
| `Review-Humanizer-Gelombang-10.md` | **Laporan gelombang 10 (versi ringkas):** perubahan struktur, integritas, keputusan pemadatan, poin konfirmasi |"""
s = s.replace(baris_pdf, tambahan)

# Sisipkan bagian gelombang 10 sebelum bagian gelombang 9
mark9 = "## 2. Perubahan gelombang 9 (review humanizer-id: ritme kalimat + deiksis sisa, 10 Nov) — ringkas"
assert mark9 in s, "marka gel 9 tak ditemukan"
gel10 = """## 2. Perubahan gelombang 10 (versi ringkas ±40 halaman, 10 Nov) — ringkas

Permintaan: padatkan naskah 91 hlm menjadi sekitar 40 hlm DOCX+PDF memakai skill humanizer-id (Mode Akademik Ketat) dan sempro-mepet (diunduh dari tautan Google Drive pemilik). Hasil akhir **44 hlm** (turun 52%), dibangun lewat pipeline terpisah (`scripts/sensesibi-v10/rakit_ringkas.py` + `build_docx_ringkas.sh` + salinan JS `parse_md_ringkas.js`/`generate_docx_ringkas.js`) sehingga versi lengkap 91-hlm tidak tersentuh. Struktur: BAB I tetap enam subbab; BAB II 13→11 subbab (2.1+2.2 digabung, 2.13 BoM dilebur ke Tabel 3.1, matriks komponen arsitektur lama dilebur ke Tabel 3.1-3.2 dan prosa 3.5); BAB III tetap 3.1-3.11 dengan subsubbab 3.2.x/3.5.x/3.6.x/3.7.x dilebur menjadi prosa mengalir dan 3.8 tetap enam subsubbab prosedur; gambar 10→3 inti (tahapan-gerbang, arsitektur akhir, inferensi tepi) dengan rujukan silang di dalam Gambar 3.2 dirender ulang ke "Subbab 2.7"; tabel BAB III 9→8 (dinomori ulang Tabel 3.1-3.8); tabel parameter 29→14 baris terkelompok; tabel risiko 12→9; tabel penelitian terdahulu 20→11. Format: Daftar Pustaka satu spasi 10 pt (konvensi kampus), daftar isi heading level 1-2, sel tabel 9 pt spasi rapat. Integritas terverifikasi `scripts/sensesibi-v10/verifikasi_ringkas.py`: 93 sitasi unik urut kemunculan 1-93 dengan seluruh entri DP identik dengan naskah asli (satu rujukan latar akuisisi CSI keluarga ESP32 keluar karena kalimatnya dipadatkan), token numerik tanpa temuan baru (satu positif palsu "91" berasal dari catatan penyusunan), cermin rumusan-tujuan 3:3, penanda PERLU 31 (dari 47, penggabungan butir tabel parameter sejenis), nol asterisk literal, nol halaman kosong. Perlu diperhatikan: versi ringkas memangkas pembukaan naratif dan merapatkan tabel; untuk pembimbingan yang membutuhkan ruang penjelasan lengkap, versi 91-hlm tetap tersedia di paket yang sama.

"""
s = s.replace(mark9, gel10 + "## 3. Perubahan gelombang 9 (review humanizer-id: ritme kalimat + deiksis sisa, 10 Nov) — ringkas")

# Geser nomor bagian riwayat lama (3→4, 4→5, dst.) agar konsisten
import re
for lama, baru in [(3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9)]:
    s = s.replace(f"## {lama}. Perubahan gelombang", f"## {baru}. Perubahan gelombang", 1)
s = s.replace("## 9. Perubahan gelombang 7 (humanizer-id, 10 Nov) — ringkas", "## 5. Perubahan gelombang 7 (humanizer-id, 10 Nov) — ringkas")

P.write_text(s, encoding="utf-8")
print("catatan pengemasan diperbarui")
# tampilkan struktur
for m in re.finditer(r"^## .*", s, re.M):
    print("  ", m.group(0)[:80])
