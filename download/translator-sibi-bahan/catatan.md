# Catatan Pengiriman — Dossier Bahan Translator SIBI Dua Arah (Topik Diperbarui)

Tanggal: 26 Oktober 2026. Paket ini menindaklanjuti perintah pemilik: **"eksekusi bahan, tanpa menulis ulang draft, dengan topik yang diperbarui, dengan skill"** (sempro-mepet + naskah-id + gepa-optimize-anything dari tiga tautan Drive). Draf `Proposal-Revisi-Translator-SIBI.md` (Task 17) TIDAK disentuh sama sekali; yang dieksekusi adalah bahan kerjanya.

## 1. Isi paket

| Berkas | Isi |
|---|---|
| `Bahan-Proposal-Translator-SIBI.md` | Dossier bahan penulisan — penerus topik-lama `DPJ-4_Bahan-Proposal-SIBI.md` (23 Okt) — kini selaras visi purwarupa penerjemah dua arah 2–3 modul ESP32-S3. 13 seksi: ringkasan eksekutif; arah latar belakang (corong 4 paragraf + anti-pola); peta masalah (lapangan, celah riset, teknis jujur); bank fakta siap kutip F1–F45 bernomor rujukan; bank rujukan 8 kelompok dipetakan ke nomor Daftar Pustaka proposal; perangkat-aset-peta diagram; tabel gerbang G0–G4 dan risiko-cadangan A–D; konsep penyelesaian (pemetaan masalah→fitur→bukti, skenario pemakaian, disiplin klaim); kit BAB I (bata kalimat ID-READY + rumusan/tujuan final); kit BAB II–III (pola blok teori, sintesis penelitian terdahulu, register prosedural, walkthrough); antisipasi sidang 12 tanya-jawab; keputusan terbuka + langkah pertama senin pagi; lampiran jejak |
| `gepa/` | Jejak lengkap optimisasi GEPA: evaluator, kontrak jangkar, benih, pelari, log iterasi (`run.log`, `run_log.txt`), kolam kandidat (`candidates.json`) |

## 2. Bagaimana dossier ini disusun dan dioptimalkan (skill gepa-optimize-anything)

Dokumen dipecah menjadi **8 komponen mudah-mutasi** (ringkasan, arah latar, peta masalah, konsep, kit BAB I, kit BAB II–III, antisipasi sidang, keputusan) dan **bagian tetap** yang dilindungi dari mutasi (bank fakta, bank rujukan, tabel perangkat, tabel gerbang/risiko, lampiran) agar angka terverifikasi tidak bisa dirusak mesin. Optimisasi memakai `optimize_anything` (paket gepa 0.1.4, backend gepa, mode single-task, kandidat multi-komponen, LM refleksi glm-4-plus via z-ai) dengan evaluator hibrida:

- **Cek objektif deterministik** — jangkar fakta wajib per komponen (38 angka/istilah kunci), klaim terlarang bertuas-negasi (penerjemah kalimat, kontinu, bentuk jari, menggantikan juru bahasa, dan kawanannya sah hanya dengan "bukan/tidak/di luar cakupan"), frasa AI terlarang mutlak, batas kemunculan ("hal ini" maks 1, dsb.), penanda `[PERLU DATA]` minimal, dan panjang antar-komponen.
- **Juri LLM lima dimensi** (D1 kesesuaian topik, D2 kegunaan bahan, D3 bahasa baku, D4 disiplin klaim, D5 koherensi) atas dokumen terakit penuh, keluaran JSON dengan kritik per bagian yang dirutekan ke komponen terkait.
- **Skor = fraksi komponen bersih × rata-rata juri/10** — gerbang ganda: mutasi yang menjatuhkan jangkar atau penanda otomatis dihukum.

**Hasil lari (jujur):** 14 iterasi penuh dalam ~13 menit. Benih meraih skor 0,82 (objektif 8/8 bersih; juri D1–D5 = 8,0/7,5/8,0/8,5/8,0). Enam proposal lolos gerbang subsampel dan dinilai penuh (0,50–0,81) dan delapan ditolak di subsampel (0,68–0,81) — **tidak satu pun mengalahkan benih**, sehingga kandidat terbaik = benih itu sendiri. Ini pola "sinyal mendekati jenuh" yang didokumentasikan skill GEPA (gotcha #9): benih memang ditulis langsung pada register sasaran dengan seluruh fakta terjangkar, sehingga refleksi tidak menemukan kegagalan yang bisa dieksploitasi. Satu proposal iterasi-14 sempat diterima di subsampel (0,80→0,82) tetapi ditolak evaluasi penuh dengan skor 0,50 karena menjatuhkan kontrak objektif — bukti penjagaan bekerja. Kesimpulan yang dilaporkan apa adanya: dossier hasil = benih yang telah melewati validasi adversarial 14 ronde, bukan hasil mutasi yang diterima.

## 3. Hasil verifikasi akhir

- Cek objektif seluruh 8 komponen: **0 masalah** (jangkar, klaim, penanda, panjang).
- Spot-check 38 angka/istilah kunci terhadap Matriks-Literatur: seluruhnya hadir dan tak satu pun di luar sumbernya; 69 nomor rujukan unik [1]–[79] terpakai.
- Lint `periksa.py` (naskah-id): **0 temuan kaidah (K)** tersisa. Temuan gaya (G) yang sengaja diterima untuk dokumen kerja internal: nama merek/produk tidak dijabarkan (RTX, TUF, KASIBI, OpenSIBI — nama diri menurut kaidah istilah); "CC-BY-NC" terbaca dua singkatan oleh linter (identitas lisensi, false positive); sejumlah kalimat butir bernomor memuat 36–44 kata (dipertahankan karena mengikat satu fakta kompleks per butir — pada naskah proposal final, pemenggalan dilakukan saat menempel kit).
- Penanda `[PERLU DATA: ...]`: 20 buah, seluruhnya keputusan manusia (pembimbing, hasil T0/T2/T4, validator, mitra, etika) — daftar lengkap pada seksi 12 dossier.

## 4. Yang perlu dikonfirmasi ke pembimbing (dari seksi 12 dossier)

Gaya sitasi IEEE bernomor; frasa judul "purwarupa" dan "kosakata terbatas"; ambang G2/G3 relatif peluang acak; kesediaan atas dua ruang mitra dan 3–4 pengisyarat; token apresiasi validator dan skala uji kegunaan 3–5 pengguna.

## 5. Cara memakai

Bila pemilik ingin menulis sendiri: seksi 1–2 memberi arah argumen, seksi 3–5 bahan terverifikasi, seksi 9–10 bata kalimat siap tempel, seksi 11 latihan pembelaan. Bila memakai `Proposal-Revisi` langsung: dossier ini peta sumbernya — setiap klaim naskah tertelusur ke bank fakta dan bank rujukan. Bila naskah diubah, catat balik perubahannya ke seksi 3 agar jejak verifikasi tetap utuh. Diagram tetap memakai sepuluh berkas `diagram/*.mmd` pada paket revisi Task 17 (peta perannya di seksi 5.4 dossier).
