# SOURCES — proposal-writing v5

Sumber resmi yang dipelajari untuk membangun skill v5 (panduan agent menulis
proposal). Skill menyalin **cara menulis (bahasa)**, bukan isi korpus.

| # | Sumber | Lokasi | Peran |
|---|--------|--------|-------|
| 1 | Korpus 69 dokumen (proposal TA, naskah, semhas, paten) D4 TRSE Universitas Negeri Malang | Drive folder `1Dk8kygzZZkFQE9uc-Z2zPbltToQMz-lF` (lokal: `/home/z/my-project/drive-proposal-contoh`, 120 MB) | Pola bahasa & struktur (03/02) — analisis awal: `05-analisis-korpus/analisis-korpus-proposal.md` |
| 2 | Panduan Penulisan Laporan Penelitian — Prodi Teknik Informatika, Fakultas Ilmu Komputer, **Universitas Bina Darma**, 2022, 33 hal. | Drive file `1sdvz1Mq0qWgyFeqcz3P_iFSclhWH5Xoa` (arsip teks: `sources/panduan-bina-darma-2022.txt`) | Aturan format (margin/font/style/penomoran/kutipan APA-Harvard/mekanika EYD) → profil BD-2022 (05/04) |
| 3 | Skill **to-tickets** (arsip `skills-main`, mattpocock) | Drive file `1z7a-xaBauhyo8ygxXpoNIUFR5s_qqOzc` | Slicing pekerjaan besar menjadi tiket tracer-bullet + blocking edges (09) |
| 4 | Skill **naskah-id** | github.com/nothinx/naskah-id (dikloning; versi GitHub lebih baru dari arsip zip lama: ada `istilah.md`, `singkatan.md`, `CHANGELOG.md`, `evals/jalankan.py`) | Pola EYD-V/kata-baku/kalimat-efektif/pola-AI + etika verifikasi rujukan (06); `periksa.py` sebagai lint |
| 5 | Skill **gepa-optimize-anything** | Drive file `1KZiprYato5B4pEJ69E70tYuwvgZZthQW` (arsip: `sources/gepa-skill-arsip.md`) | Loop optimalisasi kata-per-kata `optimize_anything` (08); preseden run nyata: Task 4 (seed 0,7196 → 1,0) |

## Keputusan desain v5

1. **Bahasa**: isi skill berbahasa Inggris (hemat token), semua keluaran ke pengguna
   berbahasa Indonesia — kontrak di `references/00-output-language.md`. Templat
   kalimat Indonesia di referensi dipertahankan verbatim sebagai bahan keluaran.
2. **Profil format dua arah**: DPJ-UNM (bawaan, sejajar 4 DPJ yang lolos QA) vs
   BD-2022 (font Cambria, margin 4/3/3/3, penomoran `1. Sub Bab`, caption tabel di
   atas, istilah asing miring) — dipilih sekali per dokumen.
3. **Rumusan masalah**: korpus memakai pertanyaan "Bagaimana …?"; BD mengizinkan
   pernyataan — bawaan tetap pertanyaan.
4. **Evaluator dibawa dari v4** dengan dua patch: `REF_FILES` menunjuk 10 referensi
   baru; kriteria selesai menerima `Selesai bila` maupun `Done when`.
5. **Sinkronisasi**: naskah-id terpasang & arsip repo diperbarui ke versi GitHub;
   catatan: markdown DPJ milik pengguna mengandung suntingan pengguna sendiri
   (mis. "bertujuan menguji" tanpa "untuk" di DPJ-1) — variasi sah, evaluator 0,96.

## Tiket eksekusi (to-tickets)

Issue #22 (T-a prefactor) → #27 (T-f mirror/push), semuanya ditutup `completed`;
edge native `blocked-by` 6/6 HTTP 201.
