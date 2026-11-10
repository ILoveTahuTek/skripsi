# Review Gelombang 12 — Parafrase anti-ai-writer (mchardyan/anti-ai-writer v2)

**Tanggal:** 11 November 2026 · **Pemicu:** permintaan pemilik memparafrasekan ketiga dokumen (md, docx, pdf) memakai skill https://github.com/mchardyan/anti-ai-writer.git · **Jenis pekerjaan:** parafrase menyeluruh atas naskah v11 tanpa perubahan isi; kaidah naskah-id (EYD V) dan register mahasiswa D4/S1 tetap dijaga.

## 1. Lingkup dan metode

1. Skill diunduh ke `skills/anti-ai-writer/` (SKILL.md + blacklisted-words.md) dan seluruh aturannya diterapkan pada prosa BAB I–III: daftar hitam kosakata/frasa/pembuka, larangan tiga kalimat beruntun berpanjang seragam, larangan parataksis, larangan rule-of-three retoris, batas em dash, suara aktif, dan variasi struktur paragraf.
2. Bekerja pada salinan sumber terpisah `_kerja-g12/src/` dengan kunci sitasi semantik utuh; gelombang 7–11 tidak tersentuh. Pipeline g12 (`rakit_g12.py` + `build_docx_g12.sh`) diturunkan dari g11 sehingga keluaran DOCX/PDF memakai tata letak yang sudah teruji.
3. Kalibrasi register: skill ditulis untuk prosa Inggris umum, tetapi README-nya menyasar tulisan akademik Indonesia; karena itu kontraksi dan fragmen kalimat ekstrem tidak dipakai (EYD V dan register skripsi diutamakan), sementara seluruh aturan statistik (ritme, kosakata, tanda baca, struktur) diterapkan penuh.

## 2. Hasil audit sebelum vs sesudah

| Butiran | v11 | v12 | Dasar |
|---|---|---|---|
| Kosakata terlarang di prosa | menegaskan 2x, mencakup 4x, menampilkan 8x | **0** (semua diganti padanan konkret bervariasi: memunculkan, muncul, memuat, meliputi, memperlihatkan, menunjukkan) | blacklisted-words.md |
| Deretan 3 kalimat berpanjang seragam (toleransi ±2 kata) | **10 deret** | **0** | SKILL.md "No uniform sentence length" |
| Parataksis (≥3 kalimat ≤8 kata beruntun) | 0 | 0 | dipertahankan |
| Em dash | 0 di prosa (2 di kolom data jadwal, tetap) | 0 di prosa (idem) | batas 1/500 kata |
| Enumerasi retoris "Pertama, ... Kedua, ..." di 1.1 | ada | diubah menjadi prosa mengalir | frasa terlarang |
| Distribusi panjang kalimat | rata-rata 19,5; terpusat 17–20 | rata-rata 21,0; rentang 3–53; 14% ≤10 kata, 23% ≥28 kata | variasi ritme |
| Pembuka/penghubung klise | minim (warisan gelombang 7–11) | tetap nol; ditambah variasi: pertanyaan retoris pembuka ("Mengapa bergerbang?"), jawaban pendek ("Angkanya timpang."), paragraf berhenti tiba-tiba | SKILL.md struktur paragraf |

## 3. Integritas (diverifikasi skrip)

- **Sitasi:** 46 kunci semantik terpakai dengan urutan kemunculan identik dengan v11 sehingga penomoran 1–46 dan isi Daftar Pustaka tidak bergeser sedikit pun; nol kunci bocor ke DOCX/PDF; nol sitasi numerik lama.
- **Angka:** token angka pada prosa BAB I–III identik dengan v11 (mAP50 0,8944/0,9580, akurasi 97,6%, 2.300 ms→54 ms, 69,2 ms, 13 menit/59 detik, Rp150.000, Rp350.000, 1,92 juta, 500 juru bahasa, 77,7%/1,9%/91%, 3,362/4, 99,8%/86,66%, 56 subcarrier, 600 bingkai/8 anchor, M1–M14, G0–G4). Selisih token hanya pada "Catatan penyusunan" sampul yang memang mendeskripsikan gelombang baru.
- **Struktur:** 39 heading, 12 tabel (isi sel data tidak diubah), 3 gambar + blok mermaid, 25 penanda [PERLU DATA]/[PERLU ILUSTRASI] di tubuh, 6 butir identitas sampul, keenam prosedur, dan cermin rumusan–tujuan 3:3 dipertahankan.
- **Dokumen:** DOCX 40 heading + 12 tabel + 3 gambar (identik v11); PDF **37 hlm** (v11 36 hlm; +1,5% kata dari parafrase), nol halaman kosong, sitasi [1]–[46] lengkap, DP berakhir [46] di hlm 37; nol sisa `**`/`|---|`/kunci semantik.

## 4. Keputusan yang perlu diketahui pemilik

1. **Prosedur bernomor dibiarkan paralel.** Langkah "Me-..." pada keenam prosedur memakai struktur paralel karena konvensi korpus sempro; aturan "no parallel structure" diterapkan pada prosa, bukan pada butir prosedur yang memang harus seragam agar bisa diikuti.
2. **Rule of three yang tersisa adalah isi, bukan gaya.** Rangkaian seperti "latensi, cakupan kamus, keandalan operasional, dan biaya" atau "Google Scholar, Crossref, dan OpenAlex" adalah daftar nyata; SKILL.md membolehkan tigaan bila memang berisi tiga.
3. **Istilah asing tetap asing** (sandbox, on-device, fallback, deploy, beacon, enclosure, dsb.) sesuai masukan dosen; parafrase tidak memperkenalkan padanan paksaan baru.
4. **Kata kerja lapor tetap ada** ("Model juara mencatat...") karena verba pelaporan standar; yang dihapus adalah kosakata bergaya AI, bukan konvensi ilmiah.

## 5. Rekomendasi tindak lanjut

1. Isi `[PERLU DATA: nama SLB atau lembaga mitra di Jawa Timur]` (1.1, 3.3, dan identitas sampul) — satu-satunya data lokasi yang belum ada.
2. Jalankan "Update Field" pada daftar isi setelah menyunting di Word/WPS.
3. Bila dosen masih menemukan kalimat yang terasa kaku, kandidat penyebabnya kini bukan pola AI melainkan pilihan istilah teknis; tunjuk kalimatnya dan akan diganti langsung tanpa membangun ulang gelombang.
