# 6 — Format Output Final (WAJIB diikuti persis)

## Bentuk jawaban

SATU jawaban dengan dua bagian berurutan: (1) naskah final lengkap, (2) log dan temuan. Format:

````
<draft-final.md LENGKAP — mulai dari baris judul "# Purwarupa ..." sampai rujukan [80]>

<!-- ===== AKHIR NASKAH — DI BAWAH INI LOG, TIDAK DIKONVERSI KE DOCX ===== -->

## Log Perubahan
| Lokasi (subbab) | Sebelum | Sesudah | Alasan |
|---|---|---|---|
| ... | ... | ... | ... |

## Daftar Temuan (inkonsistensi ambigu — TIDAK diperbaiki, hanya dilaporkan)
| Lokasi | Temuan | Usulan |
|---|---|---|
| ... | ... | ... |

## Pernyataan verifikasi
- Jumlah penanda [PERLU DATA] = 44: YA/TIDAK
- 80 sitasi utuh + Daftar Pustaka verbatim: YA/TIDAK
- 8 blok mermaid verbatim (kecuali koreksi rujukan silang Poin 4): YA/TIDAK
- Judul tidak berubah: YA/TIDAK
- Tidak ada angka yang berubah: YA/TIDAK
````

Bila jawaban terpotong batas panjang pesan, lanjutkan dengan baris "LANJUTAN draft-final.md — bagian N" tanpa mengulang bagian yang sudah terkirim.

## Konvensi markdown yang WAJIB dijaga (parser konversi DOCX bergantung pada ini)

1. `#` untuk baris judul dokumen, `# BAB I PENDAHULUAN`, `# BAB II KAJIAN PUSTAKA`, `# BAB III METODE PENELITIAN`, `# DAFTAR PUSTAKA`.
2. `##` untuk subbab (`## 1.1 ...`), `###` untuk sub-subbab (`### 3.2.1 ...`). Jangan mengubah level heading, menambah, atau menghapus heading.
3. Figur: blok ` ```mermaid ... ``` `, lalu satu baris kosong, lalu caption sebagai paragraf biasa yang dimulai dengan "Gambar 3.x ...". Jangan memberi heading pada figur atau caption.
4. Tabel: format pipe markdown (baris header + baris pemisah). Isi tabel tidak berubah.
5. Sitasi `[n]`, penanda `[PERLU DATA: ...]`, dan italik `*...*` — persis seperti sumber.
6. Tanpa YAML frontmatter, tanpa penomoran baris, tanpa emoji, tanpa kata pengantar sebelum naskah.

## Aturan tambahan

- `draft-final.md` adalah hasil suntingan `naskah-sumber.md` **seluruhnya** — jumlah baris boleh berubah karena suntingan bahasa, tetapi tidak boleh ada subbab, paragraf, gambar, atau tabel yang hilang atau baru.
- Log perubahan: cantumkan SEMUA suntingan substantif (perbaikan kaidah, penggantian istilah, pemecahan/penggabungan kalimat). Perbaikan tipografi massal boleh diringkas satu baris per jenis (mis. "tanda pisah rentang diseragamkan di 12 tempat").
- Bila terpaksa mengubah sesuatu di luar whitelist Poin 1, tandai baris log itu dengan **[LANGGAR]** — lebih baik jujur dan mudah ditemukan daripada disembunyikan.

## Kriteria diterima (diverifikasi otomatis setelah kembali ke asisten Z.ai)

1. 44 penanda `[PERLU DATA]` utuh — jumlah dan teks persis.
2. 80 sitasi tubuh + Daftar Pustaka `[1]`–`[80]` verbatim.
3. 8 blok mermaid verbatim; satu-satunya perubahan figur = koreksi rujukan silang di prosa.
4. Baris judul verbatim (terkunci).
5. Struktur utuh: BAB I 6 subbab, BAB II 11 subbab, BAB III 11 subbab, 8 gambar, 7 tabel, Daftar Pustaka 80 entri.
6. Seluruh angka jangkar (Poin 3) tidak berubah.
7. Log perubahan + pernyataan verifikasi terisi.
