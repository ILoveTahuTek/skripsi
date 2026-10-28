# 0 — Cara Pakai Paket Bahan Ini (untuk Claude)

**Tujuan paket:** memberi Claude seluruh bahan yang diperlukan untuk merapikan draft proposal penelitian menjadi **draft final markdown**, tanpa kehilangan satu pun fakta, angka, rujukan, diagram, atau penanda keputusan yang sudah terverifikasi.

## Isi paket (baca berurutan)

| # | Berkas | Isi | Wajib dibaca |
|---|---|---|---|
| 1 | `1-PERAN-DAN-MISI.md` | Peran Claude, misi, whitelist/blacklist penyuntingan | Ya |
| 2 | `2-KONTEKS-PROYEK.md` | Judul final, metodologi terkunci, fakta dokumen | Ya |
| 3 | `3-STANDAR-BAHASA-DAN-KEJUJURAN.md` | Kaidah EYD V/KBBI, daftar istilah inti, larangan mengarang | Ya |
| 4 | `4-ATURAN-DIAGRAM.md` | Status 8 diagram (sudah tervalidasi — jangan redesain), peta figur, aturan verifikasi | Ya |
| 5 | `5-HAL-TERBUKA.md` | 44 penanda `[PERLU DATA]` + konfirmasi pembimbing — bukan wewenang Claude | Ya |
| 6 | `6-FORMAT-OUTPUT-FINAL.md` | Bentuk output yang harus dikembalikan + konvensi markdown | Ya |
| — | `naskah-sumber.md` | Draft utuh saat ini (16.906 kata) — **basis penyuntingan** | Ya |
| — | `PROMPT-SATU-PESAN.md` | Gabungan poin 1–6 dalam satu prompt | Alternatif |
| — | `PROMPT-SATU-FILE-LENGKAP.md` | **Prompt + naskah utuh dalam SATU berkas** — cukup satu tempel, tanpa lampiran | Termudah |

## Dua cara memakai

**Cara A (disarankan, satu pesan):** salin seluruh isi `PROMPT-SATU-FILE-LENGKAP.md` (prompt + naskah sudah menyatu dalam satu berkas) sebagai satu pesan — **tanpa lampiran apa pun**. Bila antarmuka tempelmu terpotong karena panjang, gunakan `PROMPT-SATU-PESAN.md` sebagai pesan dan lampirkan `naskah-sumber.md`.

**Cara B (bertahap per poin):** tempel berkas 1–6 berurutan sebagai pesan terpisah (konteks tetap terjaga per poin), lampirkan `naskah-sumber.md` sejak pesan pertama, lalu perintahkan Claude mulai bekerja.

## Alur keseluruhan

1. Pemilik → berikan paket ini ke Claude.
2. Claude → menyunting `naskah-sumber.md` menjadi **`draft-final.md`** + log perubahan + daftar temuan (format: Poin 6).
3. Pemilik → kembalikan hasil Claude ke asisten Z.ai (tempel atau unggah `draft-final.md`).
4. Asisten Z.ai → verifikasi otomatis (jumlah penanda, rujukan, blok diagram, angka kunci) → mengembalikan yang dilanggar Claude → bangun **DOCX** (Times New Roman 12 pt, spasi 1,5, margin 4-3-3-3 cm, daftar isi, 80 rujukan) → pratinjau PDF → unggah GitHub.

## Tiga hal yang tidak boleh terjadi di Claude

1. Claude **mengisi** penanda `[PERLU DATA: ...]` (44 buah) — itu keputusan pemilik/pembimbing/mitra, bukan tebakan AI.
2. Claude **mengubah** angka, klaim, sitasi `[n]`, Daftar Pustaka, atau blok diagram Mermaid.
3. Claude **menambah** konten baru atau menghapus konten lama.

Jika hasil Claude mencantumkan pelanggaran tersebut di log, kirim saja hasilnya apa adanya — asisten akan memverifikasi dan memulihkan bagian yang berubah.
