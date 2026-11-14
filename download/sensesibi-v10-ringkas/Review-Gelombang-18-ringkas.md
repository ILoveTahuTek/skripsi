# Review Gelombang 18 — v17 → v18 (paket perbaikan reviewer + ESP-NOW opsional + pemadatan + 4 rujukan baru)

Tanggal: 14 November 2026. Basis: Proposal-SenseSIBI-Studi-Kelayakan-v17.md (55 halaman) → v18 (52 halaman, DP 28 → 32 entri).

## A. Pemenuhan paket perbaikan reviewer (ISS-01 sampai ISS-25)

| Prioritas | Item | Status di v18 |
|---|---|---|
| P0-1 | Tetapan terlatih seragam (1.5.1, 2.3, 3.1 ↔ Pers. 2.15) | Diterapkan: "melatih hanya kedua kepala" dihapus; kini adapter (jika dipakai) + modul temporal + dua kepala, encoder beku θ0 |
| P0-2 | Jalur A/B1/B2 + Pembanding C | Diterapkan di 2.3 (definisi penuh), 3.7, Tabel 3.6 G0b, Tabel 3.9, Gambar 2.1, Tabel 2.4 |
| P0-3 | Temporal J/Z: hop rate overlap 75%, T=16 = 3,75 s (cakupan ~4,75 s), interpolasi sekunder | Diterapkan di 3.7 + [PERLU VALIDASI: finalisasi W, H, T dari pilot] |
| P0-4 | Onset vs pose-hold | Diterapkan di 3.7 + Gambar 3.5 + [PERLU VALIDASI: ambang] |
| P0-5 | Mask gabungan m* (2.13a), sumasi (x,y), cos(g_c,g_r) (2.14a), (2.15') → (2.15), Pers. 2.8 pakai s_i | Diterapkan; (2.21)/(2.22) memakai m* |
| P0-6 | G0b permutation test + split sebelum sliding window + purge gap ≥ W | Diterapkan di 3.7 + Tabel 3.6 |
| P0-7 | N_valid (LLTF 52 vs HT-LTF 56, first_word_invalid) + audit T0 + Pers. 2.5 baseline | Diterapkan di 2.2, 3.7 (Pers. 3.1 dan varian d_\|H\|), G0 |
| P0-8 | Pilihan 1 disinkronkan (Gambar 2.1 training/deployment terpisah, Gambar 3.5 classifier-only, Tabel 3.8 #19 preferensi menunggu konfirmasi) | Diterapkan |
| P1-9 | DF-WiSLR [31], Wi-SignFi [32], DensePose From WiFi [30], kebaruan kombinatif | Diterapkan di 2.10 + Tabel 2.3 (7 baris) |
| P1-10 | MMS-TTS-ind kandidat utama operasional (verifikasi VOICES.md 14 Nov 2026) + TTFA p50/p95 | Diterapkan di 2.7, 3.5, Tabel 3.3/3.8/3.9, G3 |
| P1-11 | WER tanpa 1−WER + (S,D,I,N); latensi T_1 (3.3a) / T_2 (3.3b) p50/p95 | Diterapkan |
| P1-12 | Biaya: modul inti ~Rp300.000 dipisah dari total BOM; Tabel 3.2 baru (tanpa harga tebakan) | Diterapkan di 1.1, 3.4, 3.8.3 |
| P1-13 | Protokol audio/pinout/daya sebagai butir audit T0/G3 [PERLU DATA] | Diterapkan di 3.2, 3.5 |
| P1-14 | Keypoint J/Z dievaluasi khusus, kartu diacak per blok, repetisi terpakai dicatat, commit/hash WPC | Diterapkan di 2.5, 3.6 |
| P1-15 | Coverage/selective accuracy, scientific vs operational, ESP-DL 69,2 ms konteks, orkestrator Rust, Permenristekdikti 42/2016 [29] | Diterapkan di 2.6, 2.8, 2.9, 3.8.2, G4 |
| P1-16 | G0b masuk Tabel 3.7 (jadwal, baris 2b) | Diterapkan |
| P2-17/18/19 | Label diagram, placeholder terbuka dipertahankan, typo d_ref/λ_cls/kehati-hatianya, klaim demografi diperlunak, log kueri [PERLU DATA] | Diterapkan; Gambar 2.1 fresnel dihapus (matematika tetap di teks), Gambar 2.2 → 2.1 |

## B. ESP-NOW diturunkan dari arsitektur inti (permintaan khusus pemilik)

- CSI dinyatakan tertangkap dari bingkai Wi-Fi biasa mode *promiscuous* sebagaimana implementasi RuView [10]; node TX hanya menyediakan lalu lintas Wi-Fi baku.
- ESP-NOW hanya kandidat fitur sinkronisasi opsional (kecocokan sinkron terukur 99,56% [10]) di 2.2, 2.8, 3.4, 3.5, Tabel 2.1, Tabel 3.1, Gambar 3.1 dan 3.3.
- Versi/commit RuView dan jenis bingkai TX dipin pada T0 [PERLU DATA].

## C. Rujukan baru (diverifikasi 14 Nov 2026)

- [29] Permenristekdikti No. 42/2016 tentang Pengukuran dan Penetapan Tingkat Kesiapterapan Teknologi (peraturan.bpk.go.id/Details/141280).
- [30] J. Geng, D. Huang, F. De la Torre, "DensePose From WiFi," arXiv:2301.00250, 2022 (permintaan pemilik; benang merah pose-dari-WiFi yang dilanjutkan model MM-Fi [15]).
- [31] H. F. T. Ahmed dkk., "DF-WiSLR," Pervasive and Mobile Computing, art. 101289, 2020.
- [32] Z. Gao dkk., "A multitask sign language recognition system using commodity Wi-Fi," Mobile Information Systems, vol. 2023, art. 7959916, 2023.
- Catatan: Perdirjen Penguatan Risbang 603/E1.2/2016 tidak dijadikan entri terpisah karena judul lengkap serinya belum terverifikasi dari sumber primer; Permen [29] memadai sebagai acuan TKT.

## D. Pemadatan (permintaan "ringkas lagi" + humanizer-indonesia v1.7)

- BAB II: 17 → 12 subbab (2.2+2.3; 2.4+2.5; 2.6+2.7+2.8; 2.11+2.12); Gambar 2.1 (fresnel) dihapus, Gambar 2.2 → 2.1; prosa dirapatkan dua gelombang + pemecahan 22 kalimat panjang.
- BAB III: tabel dinomori ulang (BOM baru sebagai Tabel 3.2; perangkat lunak 3.3; pinout 3.4; skema 3.5; gerbang 3.6; jadwal 3.7; parameter 3.8; risiko 3.9); seluruh referensi silang diverifikasi.
- Tata letak: spasi tubuh 1,25; heading, rumus, tabel, dan daftar pustaka dipadatkan; lebar kolom tabel jadwal diperbaiki (kolom Gerbang tidak lagi terpotong per karakter).
- Hasil: 55 → 52 halaman sambil menyerap seluruh paket wajib reviewer (senilai ~4 halaman); pemadatan bruto ~7 halaman. Metrik prosa: rerata kalimat 24,8 → 23,5 kata (korpus target 14-20; sisa berupa prosedur dan batasan teknis yang tidak boleh dipecah lebih jauh), 9 pola berambang humanizer = 0, "bila" = 0, dash prosa = 0. Kepadatan pemadat 38/1.000 di bawah rentang korpus 73-139: konsekuensi langsung permintaan pemadatan, bukan sasaran (penanda kualitas lain lulus).

## E. Verifikasi akhir

- Sitasi monoton [1]-[32], seluruhnya tersitasi; DP 32 entri berurut.
- Persamaan (2.1)-(2.24) dengan (2.13a), (2.14a); (3.1)-(3.5) dengan (3.3a), (3.3b); tanpa prima.
- Tabel 2.1-2.4, 3.1-3.9 berurutan sesuai kemunculan; Gambar 2.1, 3.1-3.5; G0b hadir di Gambar 3.1, Tabel 3.6, Tabel 3.7.
- Penanda: PERLU DATA 47, PERLU VALIDASI 12, PERLU KONFIRMASI 4, PERLU ILUSTRASI 2 (semua tersorot kuning di tubuh).
- DOCX: H1×4, H2×29, H3×8, 13 tabel isi + 32 blok rumus, 6 gambar; PDF 52 halaman; pemeriksaan visual VLM: sampul, persamaan, tabel BOM/jadwal/parameter, Gambar 2.1 dan 3.5 — semua rapi, tanpa tumpang-tindih, tanpa placeholder bocor.


## F. Catatan jalur paralel (penting)

Repositori utama (origin/main) saat sesi ini berjalan sudah maju ke v20 lewat sesi paralel (Task 49-51 sesi lain: v18 verifikasi sumber primer, v19 koreksi mekanisme akuisisi CSI "injeksi NDP", v20 disiplin penanda terbuka; 68 hlm, DP 33 entri). Jalur ringkas ini TIDAK menimpa jalur itu; ia disimpan terpisah di download/sensesibi-v10-ringkas/ dengan akhiran -ringkas. Perbedaan isi kedua jalur:

1. Rujukan DensePose From WiFi (Geng, Huang, De la Torre, 2022; permintaan pemilik di sesi ini): ADA di jalur ringkas ini sebagai [30] (arXiv:2301.00250, terverifikasi 14 Nov 2026); TIDAK ADA di v20 (dibuang saat pemangkasan DP gelombang 14 dan tidak pernah dimasukkan lagi).
2. Pemadatan (permintaan "ringkas lagi" di sesi ini): jalur ringkas 52 hlm (BAB II 17->12 subbab, tata letak dipadatkan, 55 -> 52 sambil menyerap paket perbaikan reviewer); v20 justru 68 hlm.
3. Koreksi mekanisme akuisisi v19 (sensing = injeksi NDP + callback CSI; transport = UDP ADR-018; ESP-NOW hanya sinkronisasi mesh opsional): v20 lebih presisi daripada jalur ringkas ini (yang menulis "bingkai Wi-Fi biasa mode promiscuous"). Jika jalur ringkas diadopsi, kalimat 2.2/3.4/3.5 dan Tabel 2.1 perlu diselaraskan ke mekanisme injeksi NDP.
4. Referensi [32]/[33] v19 (README firmware CSI dan panduan pengguna RuView) dan Batasan no. 12 / Tabel 3.7 no. 21 v19 belum ada di jalur ringkas.

Rekomendasi: pilih salah satu — (a) adopsi jalur ringkas lalu porting mekanisme NDP + [32]/[33] + butir v20 ke dalamnya (jalur ringkas sudah memuat sebagian besar disiplin penanda terbuka v20 secara bawaan), atau (b) pertahankan v20 sebagai jalur utama dan jalankan ulang pemadatan + penambahan DensePose From WiFi di atasnya.
