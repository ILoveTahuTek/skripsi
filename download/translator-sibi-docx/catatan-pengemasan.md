# Catatan Pengemasan — DOCX Proposal Penerjemah Dua Arah SIBI

**Paket:** `download/translator-sibi-docx/` · Disusun 26 Oktober 2026
**Berkas utama:** `Proposal-Penerjemah-Dua-Arah-SIBI-CSI-ESP32S3.docx` (66 halaman A4, 2,9 MB)
**Pratinjau:** `Pratinjau-Proposal-Penerjemah-Dua-Arah-SIBI.pdf` (hasil konversi LibreOffice; pembagian halaman di MS Word dapat sedikit bergeser)
**Sumber isi:** `download/translator-sibi-draft/` (Task 21 — draft final dengan metodologi utama distilasi guru–murid YOLO26-Pose → model murid CSI → inferensi tepi ESP32-S3). Seluruh angka, sitasi, dan fakta TIDAK diubah satu pun; pekerjaan ini murni pengemasan DOCX.

## 1. Struktur dokumen

| Bagian | Nomor halaman | Keterangan |
|---|---|---|
| Sampul | tanpa nomor | Judul kapital 3 baris + tabel identitas 5 baris (nilai `[PERLU DATA]` disorot kuning) + baris tahun |
| Daftar Isi | romawi kecil i–iii | Bidang TOC otomatis (klik kanan → *Update Field* setelah menyunting); 64 entri H1–H3 |
| BAB I–III + Daftar Pustaka | arab 1–63 | Tanpa pemisah halaman paksa antarbab (mengikuti keputusan Task 19–21 dan proposal DPJ-4 sebelumnya) |

Format: Times New Roman 12pt, spasi 1,5 (line 360), margin 4-3-3-3 cm, paragraf rata kanan-kiri berindentasi baris pertama 1,25 cm, tabel tiga-garis 9pt dengan keterangan di atas (kiri), keterangan gambar di bawah (tengah), daftar pustaka indentasi gantung 80 entri [1]–[80], sitasi IEEE `[n]` apa adanya, penanda `[PERLU DATA: ...]` disorot kuning agar mudah dicari-ganti di Word.

## 2. Diagram BAB III — penting: varian tata letak khusus DOCX

Diagram di `translator-sibi-draft/diagram/` (sandbox, tak tersentuh) memakai rantai `flowchart TD` yang **sangat tinggi** (aspek 1:5 sampai 1:9). Diratakan ke halaman A4, teks simpulnya menjadi tak terbaca (perkiraan huruf efektif 1–4 px). Karena itu lima diagram dirender ulang dari **varian tata letak** yang disimpan di `scripts/translator-sibi-docx/diagram-docx/`:

| Gambar | Varian tata letak | Isi vs sandbox | Huruf efektif |
|---|---|---|---|
| 3.1 Tahapan T0–T5 | 3 kolom seimbang (6/8/7) + sisi klaster antarkolom | node/sisi/label identik | ±5 px (setara proposal DPJ-4 yang diterima) |
| 3.2 Alur guru–murid | 2 kolom + sisi klaster `KA--"ya"-->KB` (DQ→SD) | identik | ±7,5 px |
| 3.3 Arsitektur | tanpa varian (aspek sandbox sudah sehat 1,03) | identik | ±6 px |
| 3.4 Topologi | arah luar dibalik LR→TB | identik | ±8,5 px |
| 3.5 Inferensi tepi | pola ular 2 baris + sisi klaster `R1-->R2` (FT→MOD) | identik | ±11 px |
| 3.6 Alur dataset | 3 kolom + sisi klaster antarkolom | identik | ±9 px |

Keterbukaan teknis: pada varian berkolom, sisi yang menyeberangi batas kolom digambar sebagai **sisi klaster** (panah antarkotak-kolom) karena mermaid mengabaikan `direction` subgraf ketika ada sisi antarsimpul yang menyeberang (masalah dikenal mermaid #2539; diuji juga pada mmdc 12.0.0 dan renderer ELK — hasil sama). Pemenggalan kolom dipilih tepat di titik sisi tersebut sehingga sebagian besar sisi klaster tetap eksak secara semantik (misal DQ "ya" → SD pada Gambar 3.2). Dua pengecualian yang perlu diketahui pembaca: (1) Gambar 3.1 — sisi `S0 → T5` (jalur gagal G0 menuju tahap penulisan) digambar sebagai panah klaster kolom 1 → kolom 3 tanpa label, dan dua jalur "lolos" G1/G1U → T2 diwakili satu panah klaster berlabel "lolos"; (2) Gambar 3.6 — dua cabang `DEP → OP` dan `DEP → COVER` diwakili satu panah klaster kolom 2 → kolom 3. Rincian tepat seluruh sisi tetap tercantum pada prosa Subbab 3.2, 3.5.2, 3.7.8, dan 3.8. **Berkas `.mmd` sandbox di `translator-sibi-draft/diagram/` tidak diubah sama sekali** dan tetap menjadi sumber kanonik; varian docx memakai viewport Puppeteer lebar (`puppeteer-wide.json`) agar mmdc tidak memeras diagram ke ±800 px logis.

## 3. Hasil verifikasi

- `postcheck.py` (skill docx): **0 galat**, 1 peringatan diterima — spasi baris campuran 360 (badan, 1,5 spasi) vs 276 (sel tabel, rapat) memang disengaja mengikuti konvensi skripsi; profil spasi identik dengan proposal DPJ-4 yang sudah diterima.
- Peta halaman PDF: 6 gambar masing-masing **sehalaman penuh dengan keterangannya** (hlm. 31, 34, 39, 40, 47, 48) — pengikat `keepNext` gambar→keterangan ditambahkan setelah ditemukan keterangan Gambar 3.2 terlempar ke halaman berikutnya pada draf pertama.
- QA visual VLM (glm-5v-turbo) atas halaman sampul, daftar isi, BAB I, keenam halaman diagram, dan halaman daftar pustaka: **seluruhnya PASS** (sampul: judul 3 baris utuh; daftar pustaka: indentasi gantung seragam; tabel jadwal 17 kolom muat dengan tanda ■ terbaca).
- Jumlah penanda di DOCX: **44 `[PERLU DATA]`** (38 badan naskah + 6 sampul), **0 `[PERLU RUJUKAN]`** — penanda ke-45 pada berkas gabungan markdown hanyalah sebutan di blok catatan penyusunan yang memang tidak ikut dikemas.
- Daftar pustaka: 80 entri [1]–[80] utuh, semuanya dikutip di badan naskah (diverifikasi `rakit_draft.py`, LOLOS 13 ok / 0 galat).
- Perbaikan kecil pada sumber: baris T3 pada Tabel 3.5 (jadwal) di `bab3-metodologi.md` memuat satu sel kosong berlebih (18 vs 17 kolom) sehingga kolom Gerbang bergeser; sel berlebih dihapus dan dokumen gabungan dirakit ulang — verifikasi otomatis tetap LOLOS. Isi data tidak berubah.

## 4. Sisa pekerjaan pemilik (human-owned)

- Mengisi 44 penanda `[PERLU DATA]` (sorotan kuning): identitas sampul (6), keputusan Tabel 3.6 (27), spesifikasi layar/audio/baterai/AP (4), layanan awan TTS+ASR (2), waktu-lokasi (2), isyarat terpilih (1), etika (1), frasa uji kegunaan (1).
- 7 konfirmasi pembimbing yang tercantum pada `translator-sibi-draft/catatan.md` (5 lama + kebijakan jalur awan + kuota Kaggle). **Pembaruan 27 Okt 2026: butir 2 (frasa judul) sudah dikunci final oleh pemilik** — judul final *"Purwarupa Penerjemah Dua Arah Isyarat SIBI Berbasis Wi-Fi Channel State Information pada Modul ESP32-S3 dengan Inferensi Tepi dan Pemrosesan Bahasa pada Server: Studi Kelayakan Kosakata Terbatas"* — sehingga sisa konfirmasi tinggal 6 butir; judul pada sampul DOCX sudah sesuai dan tidak perlu di-render ulang.
- Meninjau dua generalisasi sisi klaster pada Gambar 3.1 dan 3.6 (§2 di atas) — bila pembimbing meminta ketepatan penuh, kedua gambar dapat dirender ulang dari sandbox dengan konsekuensi teks sangat kecil, atau dipecah menjadi dua gambar terpisah.

## 5. Cara regenerasi

```bash
bash /home/z/my-project/scripts/translator-sibi-docx/render_diagrams.sh   # 6 PNG -> assets/
cd /home/z/my-project/scripts/translator-sibi-docx
node parse_md.js            # markdown draft -> parsed.json
node generate_docx.js       # parsed.json -> DOCX
python3 patch_footer.py     # patch field halaman (kompatibilitas WPS)
python3 /home/z/my-project/skills/docx/scripts/add_toc_placeholders.py \
  /home/z/my-project/download/translator-sibi-docx/Proposal-Penerjemah-Dua-Arah-SIBI-CSI-ESP32S3.docx --auto
```
