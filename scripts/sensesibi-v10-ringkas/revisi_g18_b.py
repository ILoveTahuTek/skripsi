#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gelombang 18 bagian B: mermaid G3.1/G3.3, jadwal G0b, tabel parameter/risiko/gerbang,
subbab 3.8, daftar pustaka [29]-[32], header identitas, log perubahan."""
import sys
from pathlib import Path

V10 = Path("/home/z/my-project/download/sensesibi-v10")
MARK = "<!-- ===== AKHIR NASKAH"
src = (V10 / "_v18 Intermediate.md").read_text(encoding="utf-8")
naskah, log = src[:src.index(MARK)], src[src.index(MARK):]

EDITS = []
def G(old, new, n=1):
    EDITS.append((old, new, n))

# ---------- Persamaan 2.15' -> 2.15 ----------
G("kerugian gabungan Persamaan 2.14 dan 2.15′", "kerugian gabungan Persamaan 2.14 dan 2.15")

# ---------- G3.1 mermaid: T2B + G1 pindah ke fase M1-M8 ----------
OLD_G31 = """    subgraph KA["Fase pembangunan data (M1–M8)"]
        direction TB
    T0["T0 Replikasi platform, verifikasi<br/>CSI 56 subcarrier pada 1 m, uji Delta-CSI,<br/>koeksistensi, audit checkpoint encoder (M1–M2)"]
    G0("G0 akhir M2: baseline CSI-jaringan:<br/>UDP Rust tanpa kehilangan paket,<br/>akuisisi stabil, gerak terpisah")
    T1["T1 Kurasi isyarat, kalibrasi ruang,<br/>protokol, etika, rintisan separabilitas<br/>pasangan huruf mirip (M2–M4)"]
    T2["T2 Perekaman dataset dan<br/>pelatihan dua kepala di atas<br/>encoder beku (M4–M8)"]
    T0 --> G0
    G0 -- "lolos" --> T1
    G0b("G0b awal T2: probe linear embedding beku,<br/>keputusan jalur masukan")
    T1 --> G0b
    G0b -- "lolos" --> T2
    end
    subgraph KB["Fase pengujian dan penulisan (M8–M14)"]
        direction TB
    T2B["Kuantisasi model terpilih dan uji<br/>deployment jalur klasifikasi<br/>ke modul ESP32-S3"]
    G1("G1 akhir M8: model tepi terkuantisasi:<br/>akurasi skema, ablasi multitugas dilaporkan,<br/>inferensi di bawah 100 ms")
    T3["T3 Uji generalisasi: lintas sesi,<br/>partisipan, ruang, posisi<br/>berdiri/duduk (M8–M10)"]"""
NEW_G31 = """    subgraph KA["Fase pembangunan data, audit, dan model (M1–M8)"]
        direction TB
    T0["T0 Replikasi platform, verifikasi<br/>CSI N_valid subcarrier pada 1 m, uji Delta-CSI,<br/>koeksistensi, audit checkpoint encoder (M1–M2)"]
    G0("G0 akhir M2: baseline CSI-jaringan:<br/>UDP Rust tanpa kehilangan paket,<br/>akuisisi stabil, gerak terpisah")
    T1["T1 Kurasi isyarat, kalibrasi ruang,<br/>protokol, etika, rintisan separabilitas<br/>pasangan huruf mirip (M2–M4)"]
    G0b("G0b awal T2: probe linear embedding beku,<br/>keputusan rute masukan")
    T2["T2 Perekaman dataset dan<br/>pelatihan dua kepala di atas<br/>encoder beku (M4–M8)"]
    T2B["Kuantisasi model terpilih dan uji<br/>deployment jalur klasifikasi<br/>ke modul ESP32-S3 (M6–M8)"]
    G1("G1 akhir M8: model tepi terkuantisasi:<br/>akurasi skema, ablasi multitugas dilaporkan,<br/>inferensi di bawah 100 ms")
    T0 --> G0
    G0 -- "lolos" --> T1
    T1 --> G0b
    G0b -- "lolos" --> T2
    T2 --> T2B
    T2B --> G1
    end
    subgraph KB["Fase pengujian dan penulisan (M8–M14)"]
        direction TB
    T3["T3 Uji generalisasi: lintas sesi,<br/>partisipan, ruang, posisi<br/>berdiri/duduk (M8–M10)"]"""
G(OLD_G31, NEW_G31)
G("accTitle: Tahapan penelitian T0 sampai T5 dengan gerbang keputusan G0 sampai G4",
  "accTitle: Tahapan penelitian T0 sampai T5 dengan gerbang keputusan G0 sampai G4 dan sub-gerbang G0b")
G("accDescr: Diagram dua fase. Fase pembangunan data berisi T0 replikasi platform dan audit checkpoint encoder, gerbang G0 baseline, T1 kurasi isyarat, sub-gerbang G0b probe kompatibilitas representasi atas data pilot, dan T2 perekaman dataset serta pelatihan dua kepala. Fase pengujian berisi kuantisasi model, gerbang G1 model tepi, T3 uji generalisasi, gerbang G2 konsultasi tiga pilar, T4 pengemasan purwarupa, gerbang G3 integrasi mesin ucapan, gerbang G4 sintesis kelayakan, dan T5 analisis serta penulisan.",
  "accDescr: Diagram dua fase. Fase pembangunan data, audit, dan model berisi T0 replikasi platform dan audit checkpoint encoder, gerbang G0 baseline, T1 kurasi isyarat, sub-gerbang G0b probe kompatibilitas representasi atas data pilot, T2 perekaman dataset dan pelatihan dua kepala, kuantisasi model terpilih, serta gerbang G1 model tepi. Fase pengujian dan penulisan berisi T3 uji generalisasi, gerbang G2 konsultasi tiga pilar, T4 pengemasan purwarupa, gerbang G3 integrasi mesin ucapan, gerbang G4 sintesis kelayakan, dan T5 analisis serta penulisan.")
G("Gambar 3.1 Tahapan penelitian T0–T5 dan gerbang keputusan G0–G4 (jalur lolos; tindakan jika gagal pada Tabel 3.6)",
  "Gambar 3.1 Tahapan penelitian T0–T5 dan gerbang keputusan G0–G4 beserta sub-gerbang G0b (jalur lolos; tindakan jika gagal pada Tabel 3.6)")

# ---------- G3.3 mermaid: ESP-NOW turun grade, label server orkestrasi ----------
G("accDescr: Tiga rantai. Arah 1 mengalir dari beacon ESP-NOW node pemancar melalui zona isyarat ke node penerima yang menjalankan model klasifikasi terkuantisasi; label dan skor dikirim via UDP ke server Rust, teks tampil di layar modul dan aplikasi Tauri, teks disintesis mesin TTS Kokoro di server lokal, dan audio dialirkan kembali ke speaker node penerima.",
  "accDescr: Tiga rantai. Arah 1 mengalir dari lalu lintas Wi-Fi node pemancar melalui zona isyarat ke node penerima yang menjalankan model klasifikasi terkuantisasi; label dan skor dikirim via UDP ke server orkestrasi Rust, teks tampil di layar modul dan aplikasi Tauri, teks disintesis mesin TTS di server lokal, dan audio dialirkan kembali ke speaker node penerima.")
G('        TX["Node TX: beacon<br/>ESP-NOW"]',
  '        TX["Node TX: sumber frame<br/>Wi-Fi baku (ESP-NOW<br/>opsional utk sinkronisasi)"]')
G('    SVR["Server Rust di laptop:<br/>orkestrasi, TTS Kokoro utama,<br/>faster-whisper ASR luring"]',
  '    SVR["Server orkestrasi Rust:<br/>TTS utama (MMS-TTS-ind),<br/>faster-whisper ASR luring"]')
G('    TTSP["TTS on-device ponsel<br/>(Kokoro ONNX; cadangan)"]',
  '    TTSP["TTS on-device ponsel<br/>(cadangan)"]')
G("Gambar 3.3 Arsitektur produk akhir tanpa kamera. Subgraf arah 1 = isyarat menjadi teks dan suara; subgraf arah 2 = ucapan menjadi representasi SIBI; subgraf jalur guru hanya aktif saat akuisisi dan pelatihan; garis putus-putus = jalur cadangan TTS *on-device* pada ponsel jika server tidak tersedia.",
  "Gambar 3.3 Arsitektur produk akhir tanpa kamera. Subgraf arah 1 = isyarat menjadi teks dan suara; subgraf arah 2 = ucapan menjadi representasi SIBI; subgraf jalur guru hanya aktif saat akuisisi dan pelatihan; garis putus-putus = jalur cadangan TTS on-device pada ponsel jika server tidak tersedia.")

# ---------- Jadwal: baris G0b ----------
G("| 2 | T1 Kurasi alfabet SIBI dan kosakata, kalibrasi ruang, protokol, perizinan | | ■ | ■ | ■ | | | | | | | | | | | — |\n",
  "| 2 | T1 Kurasi alfabet SIBI dan kosakata, kalibrasi ruang, protokol, perizinan | | ■ | ■ | ■ | | | | | | | | | | | — |\n| 2b | G0b Probe linear kompatibilitas representasi *encoder* atas data pilot (Subbab 3.7) | | | | ■ | | | | | | | | | | | G0b (awal T2) |\n")

# ---------- Tabel 3.8 (parameter): typo + status ----------
G("| 7 | Sistem koordinat target regresi, skala acuan d~ref~, dan ambang α | Sebelum pelatihan | [PERLU VALIDASI: sistem koordinat dan ambang PCK] |",
  "| 7 | Sistem koordinat target regresi, skala acuan d_ref, konvensi *handedness*, dan ambang α | Sebelum pelatihan | [PERLU VALIDASI: sistem koordinat, handedness, dan ambang PCK] |")
G("| 9 | Bobot λ~cls~, λ~reg~, normalisasi skala kerugian, dan ambang keyakinan | Dari data validasi | [PERLU DATA: nilai bobot, skema normalisasi, dan ambang] |",
  "| 9 | Bobot λ_cls, λ_reg, normalisasi skala kerugian, dan ambang keyakinan | Dari data validasi | [PERLU DATA: nilai bobot, skema normalisasi, dan ambang] |")
G("| 17 | Lokasi sintesis dan pemutaran TTS (keputusan D3: server lokal utama, ponsel cadangan), mesin final, layanan ASR, dan frasa uji | Pada G3 | [PERLU DATA: keputusan final lokasi, mesin, layanan, dan daftar frasa dari uji banding] |",
  "| 17 | Lokasi sintesis dan pemutaran TTS (server lokal utama, ponsel cadangan), mesin final, layanan ASR, dan frasa uji | Pada G3 | [PERLU KONFIRMASI: keputusan final mesin; MMS-TTS-ind kandidat utama operasional setelah verifikasi Kokoro tanpa bahasa Indonesia; daftar frasa dari uji banding] |")
G("| 19 | Model *deployment* (Pilihan 1: klasifikator saja; Pilihan 2: dua kepala aktif) | Tujuan eksperimen dan hasil ablasi manfaat regresi | [PERLU DATA: keputusan dan dasarnya] |",
  "| 19 | Model *deployment* (Pilihan 1: klasifikator saja; Pilihan 2: dua kepala aktif) | Tujuan eksperimen dan hasil ablasi manfaat regresi | [PERLU DATA: keputusan final; Pilihan 1 rancangan utama naskah menunggu hasil ablasi dan konfirmasi] |")

# ---------- Tabel 3.9 (risiko) ----------
G("| 2 | Bentuk masukan *checkpoint* tidak sesuai jendela CSI (delapan fitur turunan lawan 56 *subcarrier*) | *Encoder* tidak bisa dipakai langsung | Hitung fitur turunan bawaan RuView atau latih adapter masukan; hasil audit T0 dilaporkan |",
  "| 2 | Bentuk masukan *checkpoint* tidak sesuai jendela CSI (delapan fitur turunan lawan N_valid *subcarrier*) | *Encoder* tidak bisa dipakai langsung | Jalur A (fitur turunan), Jalur B1/B2 (adapter), atau Pembanding C (CSI tanpa penyempitan); hasil audit T0 dan G0b dilaporkan |")
G("| 3 | *Embedding encoder* beku tidak memisahkan kelas huruf | Kepala tidak dapat belajar | Jalur adaptasi LoRA dan pelatihan lanjutan; hasilnya dibandingkan apa adanya |",
  "| 3 | *Embedding encoder* beku tidak memisahkan kelas huruf | Kepala tidak dapat belajar | Pembanding C dijalankan berdampingan dengan adaptasi LoRA dan pelatihan lanjutan; hasilnya dibandingkan apa adanya |")
G("| 8 | Layanan ucapan tidak memadai, termasuk suara Kokoro belum tersedia | Jalur ucapan terganggu | Beralih ke MMS-TTS-ind ONNX, lalu server lokal atau awan (cadangan D) |",
  "| 8 | Layanan ucapan tidak memadai (Kokoro terverifikasi tanpa bahasa Indonesia, 14 Nov. 2026) | Jalur ucapan terganggu | MMS-TTS-ind sebagai kandidat utama operasional, lalu server lokal atau awan (cadangan D) |")

# ---------- 3.8 ----------
G("G0 berdiri di atas uji Delta-CSI dan koeksistensi, G1 di atas uji model pada Subbab 3.8.2, G2 di atas konsultasi tiga pilar, G3 di atas uji operasional dan jalur ucapan, serta G4 di atas uji kegunaan, penilaian validator, dan analisis biaya. Satu uji lagi, cakupan kamus, melengkapi analisis tanpa menjadi syarat gerbang. Seluruh hasil klasifikasi, regresi, dan operasional dilaporkan sebagai bukti awal pada populasi terbatas 3–4 pengisyarat, sedikitnya dua ruang, dan satu konfigurasi perangkat; skema *leave-one-subject-out*, pengguna baru, dan *leave-one-room-out* dibaca sebagai indikasi ketahanan awal, bukan bukti generalisasi populasi (Subbab 1.4).",
  "G0 berdiri di atas uji Delta-CSI dan koeksistensi, G1 di atas uji model pada Subbab 3.8.2, G2 di atas konsultasi tiga pilar, G3 di atas uji operasional dan jalur ucapan, serta G4 di atas uji kegunaan, penilaian validator, dan analisis biaya; cakupan kamus melengkapi analisis tanpa menjadi syarat gerbang. Seluruh hasil dilaporkan sebagai bukti awal pada populasi terbatas sesuai Batasan no. 11 (Subbab 1.4).")
G("2. Merekam CSI dalam tiga kondisi: ruang kosong, pengisyarat diam, dan pengisyarat bergerak.",
  "2. Merekam CSI dalam tiga kondisi (ruang kosong, pengisyarat diam, dan pengisyarat bergerak) serta beberapa konfigurasi tangan statis, orientasi telapak berbeda, dan lintasan J dan Z sebagai rintisan separabilitas.")
G("Keenam skema Tabel 3.5 diuji dengan metrik Subbab 2.9, selalu dibandingkan terhadap peluang acak sekitar 3,8% untuk 26 kelas; angka acak itu dihitung ulang jika cakupan dipangkas. Akurasi dilaporkan dalam dua versi, yaitu tanpa penolakan pada seluruh segmen uji dan dengan penolakan pada segmen yang diterima. *Recall* tiap kelas dilaporkan, dengan *recall* J dan Z terpisah beserta *confusion* terhadap huruf paling mirip. Kinerja kepala regresi dilaporkan dengan MPJPE, NME, PCK@α, dan galat per *keypoint* (Subbab 2.9), dan galat itu dirinci untuk pasangan huruf paling mirip serta lintasan J dan Z. Pembanding ablasi dilaporkan berdampingan: kepala klasifikasi saja, multitugas penuh, dan variasi bobot λ~reg~; manfaat supervisi *keypoint* dinyatakan dari selisihnya, termasuk jika manfaatnya nihil.",
  "Keenam skema Tabel 3.5 diuji dengan metrik Subbab 2.9, selalu dibandingkan terhadap peluang acak sekitar 3,8% untuk 26 kelas; angka acak itu dihitung ulang jika cakupan dipangkas. Kelayakan ilmiah, yaitu apakah sinyal memuat informasi kelas, dibedakan dari kebergunaan operasional, yaitu apakah mekanisme penolakan menghasilkan alat yang bisa dipakai. Akurasi dilaporkan dalam dua versi (tanpa penolakan pada seluruh segmen uji, dan dengan penolakan pada segmen yang diterima) bersama *accepted coverage*, akurasi pada segmen diterima, akurasi keseluruhan, serta laju terima-salah dan tolak-salah. *Recall* tiap kelas dilaporkan, dengan *recall* J dan Z terpisah beserta *confusion* terhadap huruf paling mirip. Kinerja kepala regresi dilaporkan dengan MPJPE, NME, PCK@α, dan galat per *keypoint* (Subbab 2.9), dirinci untuk pasangan huruf paling mirip serta lintasan J dan Z. Pembanding ablasi dilaporkan berdampingan: kepala klasifikasi saja, multitugas penuh, variasi bobot λ_reg, dan Pembanding C; manfaat supervisi *keypoint* dinyatakan dari selisihnya, termasuk jika manfaatnya nihil.")
G("t~total~ = t~segmentasi~ + t~inferensi~ + t~pemetaan~ + t~keluaran~ (3.3)",
  "T~1~ = t~CSI-buf~ + t~segmentasi~ + t~inferensi~ + t~telemetri~ + t~pemetaan~ + t~TTS~ + t~pengaliran-audio~ + t~pemutaran~ (3.3a)\nT~2~ = t~penangkapan~ + t~pengunggahan-audio~ + t~ASR~ + t~pemetaan-kamus~ + t~penampilan~ (3.3b)")
G("dengan t~inferensi~ mencakup seluruh model gabungan (Subbab 3.7) dan t~keluaran~ mencakup sintesis ucapan pada arah pertama serta tampilnya representasi isyarat pada arah kedua; anggaran per tahap dan ambang totalnya diuji pada G3 (Tabel 3.6).",
  "dengan T~1~ latensi arah pertama (isyarat menjadi teks dan suara) dan T~2~ latensi arah kedua (ucapan menjadi representasi isyarat); keduanya dilaporkan menurut persentil p50 dan p95 pada jalur daring dan luring, dan anggaran per tahap serta ambang totalnya diuji pada G3 (Tabel 3.6).")
G("5. Menghitung biaya purwarupa dari harga komponen serta perkiraan biaya layanan ucapan per jam pemakaian.",
  "5. Menghitung biaya purwarupa dari Tabel 3.2 (BOM) serta perkiraan biaya layanan ucapan per jam pemakaian.")
G("3. Mengukur waktu pengenalan, pemetaan, waktu menuju audio pertama (TTFA) sintesis TTS, serta total ujung ke ujung pada kedua arah.",
  "3. Mengukur waktu pengenalan, pemetaan, waktu menuju audio pertama (TTFA) sintesis TTS menurut p50 dan p95, serta total ujung ke ujung pada kedua arah.")
G("4. Mengulang pengukuran pada kedua kandidat mesin (Kokoro ONNX dan MMS-TTS-ind) di server lokal maupun *on-device* ponsel serta jalur pembanding awan, lalu menimbang mutu dan latensinya.",
  "4. Mengulang pengukuran pada kedua kandidat mesin (MMS-TTS-ind sebagai kandidat utama dan Kokoro ONNX sebagai pembanding) di server lokal maupun *on-device* ponsel serta jalur pembanding awan, lalu menimbang mutu dan latensinya.")
G("Uji kegunaan diposisikan sebagai uji kelayakan skala kecil: hasilnya dianalisis secara deskriptif untuk menemukan hambatan pemakaian dan mengarahkan perbaikan purwarupa, bukan sebagai bukti efektivitas pada populasi pengguna; rumusan ini selaras dengan Batasan no. 9.",
  "Uji kegunaan diposisikan sebagai evaluasi formatif skala kecil: hasilnya dianalisis secara deskriptif (median, sebaran, skor tiap partisipan, dan catatan kualitatif) untuk menemukan hambatan pemakaian dan mengarahkan perbaikan purwarupa, tanpa klaim efektivitas populasi maupun kesimpulan kausal; rumusan ini selaras dengan Batasan no. 9.")
G("Kewajaran keluaran kedua arah dinilai validator penutur tunarungu; keluaran sistem dan penilaian independennya dicatat dalam tabel silang, sedangkan kasus yang dinilai keliru dilaporkan tersendiri.",
  "Kewajaran keluaran kedua arah dinilai validator penutur tunarungu; keluaran sistem dan penilaian independennya dicatat dalam tabel silang, sedangkan kasus yang dinilai keliru dilaporkan tersendiri. Rubrik penilaian tertulis, identitas dan kompetensi pakar, serta batas temuan kritis difinalkan sebelum G2 dan T4 dijalankan [PERLU DATA: rubrik pakar, nama dan kompetensi, kuesioner, dan kriteria temuan kritis].")

# ---------- Tabel 3.6 (gerbang) ----------
G("| G0 | Baseline CSI dan jaringan, akhir M2 | Akuisisi 56 *subcarrier* 1 m ke UDP Rust terbaca stabil; laju sekurang-kurangnya 25 bingkai per detik; paket hilang tidak melampaui 0,1%; pola bergerak terpisah dari diam; audit *checkpoint encoder* selesai | Perbaikan penempatan satu kali; gagal lagi berarti jalur CSI dihentikan dan dilaporkan |",
  "| G0 | Baseline CSI dan jaringan, akhir M2 | Akuisisi N_valid *subcarrier* hasil audit (tipe LTF, *pilot/null/guard*, *first_word_invalid*) stabil 1 m ke UDP Rust; laju sekurang-kurangnya 25 bingkai per detik; paket hilang tidak melampaui 0,1%; pola bergerak terpisah dari diam; audit *checkpoint encoder* dan versi/commit RuView selesai | Perbaikan penempatan satu kali; gagal lagi berarti jalur CSI dihentikan dan dilaporkan |")
G("*probe* biner J–Z sekurang-kurangnya 70% [usulan]; kontrol label-acak signifikan (p < 0,05); keputusan jalur masukan tercatat | Jalur fitur turunan gagal maka jalur adapter diuji; keduanya gagal maka skema adaptasi LoRA/pelatihan lanjutan (Subbab 2.3) dan hasilnya dilaporkan sebagai temuan |",
  "*probe* biner J–Z sekurang-kurangnya 70% [usulan]; uji permutasi label pada unit blok repetisi (p_perm < 0,05, skor label asli melampaui distribusi nol permutasi); keputusan rute masukan tercatat | Jalur fitur turunan gagal maka jalur adapter diuji; keduanya gagal maka Pembanding C dijalankan berdampingan dengan skema adaptasi LoRA/pelatihan lanjutan (Subbab 2.3) dan hasilnya dilaporkan sebagai temuan |")
G("melampaui pembanding ablasi kepala tunggal dengan manfaat multitugas dilaporkan; *recall* J dan Z dilaporkan terpisah beserta *confusion* terhadap huruf paling mirip; MPJPE dilaporkan sebagai pemantauan; inferensi terkuantisasi di bawah 100 ms;",
  "melampaui pembanding ablasi kepala tunggal, variasi bobot, dan Pembanding C dengan manfaat multitugas dilaporkan; *recall* J dan Z terpisah beserta *confusion* terhadap huruf paling mirip; laporan *coverage* dan akurasi selektif; MPJPE dilaporkan sebagai pemantauan; inferensi terkuantisasi di bawah 100 ms;")
G("| G3 | Integrasi Rust dan mesin ucapan, M11 | Latensi arah 1 tidak melampaui 2 detik dan arah 2 tidak melampaui 3 detik pada jalur utama server lokal (5 detik untuk jalur cadangan *on-device*); TTFA TTS di bawah 100 ms pada frasa uji paling banyak lima kata; *parsing* UDP di bawah 0,2 ms; memori server di bawah 40 MB; suara Indonesia tersedia atau peralihan dilaporkan | Beralih ke mesin alternatif, lalu jalur *on-device* ponsel atau awan; melampaui berarti temuan |",
  "| G3 | Integrasi Rust dan mesin ucapan, M11 | Latensi arah 1 (T_1) tidak melampaui 2 detik dan arah 2 (T_2) tidak melampaui 3 detik pada jalur utama server lokal, dilaporkan p50 dan p95 (5 detik untuk jalur cadangan *on-device*); TTFA p50 di bawah 100 ms pada frasa uji paling banyak lima kata; *parsing* UDP di bawah 0,2 ms; memori server di bawah 40 MB; status mesin TTS (MMS-TTS-ind atau Kokoro) tercatat | Beralih ke mesin alternatif, lalu jalur *on-device* ponsel atau awan; melampaui berarti temuan |")
G("| G4 | Sintesis kelayakan, akhir M12 | Skor persepsi rata-rata sekurang-kurangnya 3,0 dari 5; validator menyetujui kewajaran; biaya lengkap; rekomendasi TKT/TRL 3–4 tertulis | Hasil negatif tetap dilaporkan; rekomendasi menyatakan posisi lebih rendah beserta alasan |",
  "| G4 | Sintesis kelayakan, akhir M12 | Skor persepsi rata-rata sekurang-kurangnya 3,0 dari 5; validator menyetujui kewajaran; biaya lengkap dari BOM; rekomendasi posisi TKT 3–4 menurut Permenristekdikti 42/2016 [29] dan TRL [27] tertulis | Hasil negatif tetap dilaporkan; rekomendasi menyatakan posisi lebih rendah beserta alasan |")

# ---------- Daftar Pustaka [29]-[32] ----------
G('[28] R. Likert, "A technique for the measurement of attitudes," *Archives of Psychology*, no. 140, pp. 5–55, 1932.',
  '[28] R. Likert, "A technique for the measurement of attitudes," *Archives of Psychology*, no. 140, pp. 5–55, 1932.\n\n[29] Peraturan Menteri Riset, Teknologi, dan Pendidikan Tinggi Republik Indonesia, Nomor 42 Tahun 2016 tentang Pengukuran dan Penetapan Tingkat Kesiapterapan Teknologi. Jakarta, Indonesia, 2016. [Online]. Available: https://peraturan.bpk.go.id/Details/141280/permen-ristekdikti-no-42-tahun-2016, diakses 14 Nov. 2026.\n\n[30] J. Geng, D. Huang, and F. De la Torre, "DensePose From WiFi," arXiv:2301.00250, 2022, doi: 10.48550/arXiv.2301.00250.\n\n[31] H. F. T. Ahmed, H. Ahmad, K. Narasingamurthi, H. Harkat, and S. K. Phang, "DF-WiSLR: Device-free Wi-Fi-based sign language recognition," *Pervasive and Mobile Computing*, art. 101289, 2020, doi: 10.1016/j.pmcj.2020.101289.\n\n[32] Z. Gao et al., "A multitask sign language recognition system using commodity Wi-Fi," *Mobile Information Systems*, vol. 2023, art. 7959916, 2023, doi: 10.1155/2023/7959916.')

# ---------- Header identitas + catatan ----------
G("| Jenis dokumen | Proposal penelitian (seminar proposal), BAB I sampai III + Daftar Pustaka; revisi terarah dan aditif atas v16: kontrak masukan *encoder* dikunci, supervisi 24 huruf statis dan J/Z dipisahkan, persamaan pembaruan tetapan disatukan, *deployment* mengikuti Pilihan 1, arsitektur audio disatukan, kriteria gerbang diperkuat; 55 halaman (naik dari 49 pada v16) |",
  "| Jenis dokumen | Proposal penelitian (seminar proposal), BAB I sampai III + Daftar Pustaka; revisi v18 atas v17: paket perbaikan reviewer diterapkan (jalur masukan A/B1/B2 dan Pembanding C, uji permutasi G0b, *subcarrier* valid N_valid, mask gabungan 2.13a, kemiripan arah gradien 2.14a, latensi T_1/T_2 p50 dan p95, WER tanpa 1−WER, tabel BOM, Permenristekdikti 42/2016, DF-WiSLR, Wi-SignFi, DensePose From WiFi), ESP-NOW diturunkan menjadi fitur sinkronisasi opsional, BAB II dipadatkan dari 17 menjadi 12 subbab; {{HALAMAN}} |")
G("> Catatan penyusunan: versi ini menyunting naskah v16 sebagai revisi terarah dan aditif atas evaluasi kritis; tidak ada bab yang ditulis ulang dan ruang lingkup sistem tidak berubah. Kontrak masukan *encoder* dikunci menjadi delapan fitur turunan per jendela satu detik dan diuji gerbang G0b; supervisi 24 huruf statis dipisahkan dari huruf gerak J dan Z; himpunan tetapan terlatih dirumuskan utuh pada Persamaan 2.15′ dengan modul temporal dua cabang; *deployment* mengikuti Pilihan 1 (kepala klasifikasi saja, kepala regresi sebagai supervisi tambahan); arsitektur audio disatukan dengan sintesis TTS di server lokal sebagai jalur utama (keputusan D3); kriteria gerbang G1 diperkuat; beban perekaman dihitung ke dalam protokol. Tiga keputusan terbuka, yaitu akhiran judul, model *deployment*, dan lokasi TTS, dicatat pada Tabel 3.8. Penanda [PERLU DATA] dan [PERLU VALIDASI] tetap menandai hal yang belum dapat ditetapkan; rincian perubahan per subbab ada pada Log Perubahan gelombang 17 di ujung naskah.",
  "> Catatan penyusunan: versi ini menyunting naskah v17 sebagai revisi terarah sekaligus pemadatan menyeluruh; ruang lingkup sistem, objek 26 huruf, gerbang G0 sampai G4, dan seluruh komponen terkunci tidak berubah, dan tidak ada klaim yang dinaikkan. Mekanisme akuisisi CSI diluruskan: CSI ditangkap dari bingkai Wi-Fi biasa dalam mode *promiscuous* sebagaimana implementasi RuView, sedangkan ESP-NOW diturunkan menjadi fitur sinkronisasi opsional. Jalur masukan *encoder* dibedakan menjadi Jalur A, B1, dan B2 dengan Pembanding C; statistik G0b diganti uji permutasi; segmentasi memisahkan fase *onset* dan *pose-hold*; pembagian data dilakukan sebelum jendela bergulir dengan jeda pembersih; MMS-TTS-ind menjadi kandidat TTS utama operasional setelah verifikasi Kokoro tanpa bahasa Indonesia; tabel BOM ditambahkan tanpa harga tebakan; BAB II dipadatkan dari 17 menjadi 12 subbab dan tabel BAB III dinomori ulang menyusul penyisipan BOM. Penanda [PERLU DATA], [PERLU VALIDASI], dan [PERLU KONFIRMASI] tetap menandai hal yang belum dapat ditetapkan; rincian perubahan per subbab ada pada Log Perubahan gelombang 18 di ujung naskah.")

print("total suntingan terdaftar:", len(EDITS))
gagal = []
for old, new, n in EDITS:
    c = naskah.count(old)
    if c != n:
        gagal.append((old[:100], c, n))
    else:
        naskah = naskah.replace(old, new)
if gagal:
    for g_, c, n in gagal:
        print(f"GAGAL (ditemukan {c}, harapan {n}): {g_}...")
    sys.exit(1)
print("seluruh suntingan diterapkan:", len(EDITS))

# ---------- Log Perubahan gelombang 18 ----------
LOG18 = """
## Log Perubahan — Revisi 14 November 2026, gelombang 18 (paket perbaikan reviewer v17, ESP-NOW opsional, pemadatan, empat rujukan baru)

Permintaan: pemilik menugaskan revisi v17 ke v18 sesuai paket perbaikan reviewer (issue ledger ISS-01 sampai ISS-25, prioritas P0/P1/P2), koreksi mekanisme akuisisi CSI (ESP-NOW bukan sumber CSI, hanya kandidat fitur sinkronisasi), penambahan rujukan DensePose From WiFi, serta pemadatan menyeluruh memakai kaidah humanizer-indonesia v1.7 register akademik. Identitas SenseSIBI, ruang lingkup 26 huruf, gerbang G0 sampai G4, dan seluruh komponen terkunci dipertahankan; tidak ada asumsi yang dinaikkan menjadi fakta.

Perubahan utama:

1. ESP-NOW dikeluarkan dari arsitektur inti (Tabel 2.1, Subbab 2.2, 2.8, 3.4, 3.5, Tabel 3.1, Gambar 3.1 dan 3.3): CSI ditangkap node RX dari bingkai Wi-Fi biasa dalam mode promiscuous sebagaimana implementasi RuView [10]; node TX menyediakan lalu lintas Wi-Fi baku sebagai sumber bingkai; ESP-NOW hanya kandidat fitur sinkronisasi opsional (kecocokan sinkron terukur 99,56% pada dokumentasi RuView). Jenis bingkai TX dan versi/commit RuView diaudit pada T0 [PERLU DATA].
2. Jalur masukan encoder dibedakan eksplisit (Subbab 2.3, 3.7, Tabel 3.9, Gambar 2.1): Jalur A (rekonstruksi 8 fitur bawaan), Jalur B1 (adapter rekonstruksi), Jalur B2 (adapter tugas), dan Pembanding C (baseline CSI temporal tanpa penyempitan 8 fitur); keputusan pada G0b. Temuan audit primer 14 Nov 2026 dicatat: dua set artefak checkpoint (model.* dan csi-embed-v2.*), NUL-padding model.safetensors (isu #1522), peringatan SISO #509, tingkat lupa EWC 32,97%, konteks triplet 82,3% satu ruangan satu rekaman dua node. Pernyataan "melatih hanya kedua kepala" (1.5.1, 2.5 lama, 3.1) diluruskan konsisten dengan Persamaan 2.15.
3. Persamaan: (2.1) dan (3.1) memakai himpunan subcarrier valid N_valid dengan audit T0 (tipe LTF LLTF 52 vs HT-LTF 56, pilot/null/guard, first_word_invalid); (2.5) didefinisikan sempit sebagai normalisasi baseline kalibrasi ruang; (2.8) memakai vektor ringkasan atensi temporal s_i; baru (2.13a) mask gabungan m* = m_valid x m_vis yang dipakai (2.13), (2.21), (2.22) dengan sumasi koordinat (x,y); baru (2.14a) kemirian arah gradien cos(g_c, g_r); (2.15') dirapikan menjadi (2.15); (2.23) WER tanpa "1 - WER" dengan pelaporan (S, D, I, N); (3.3) dipecah menjadi (3.3a) T_1 dan (3.3b) T_2 dengan pelaporan p50 dan p95.
4. Temporal J/Z diluruskan (Subbab 3.7): 4 langkah per detik adalah laju awal jendela dengan tumpang-tindih 75%, bukan empat observasi independen; T=16 berjarak jendela awal-akhir 3,75 detik dengan cakupan data mentah sampai sekitar 4,75 detik (usulan, difinalkan dari pilot); metrik interpolasi ke laju kamera diturunkan menjadi pembanding sekunder; segmentasi memisahkan onset gerak dan jendela pose-hold untuk 24 huruf statis.
5. Statistik G0b (Subbab 3.7, Tabel 3.6): kontrol label-acak (p < 0,05) diganti uji permutasi label pada unit blok repetisi (p_perm < 0,05, skor label asli melampaui distribusi nol); G0b dinyatakan penyaringan awal satu pengisyarat satu sesi; kegagalan jalur 8 fitur kini memicu Pembanding C berdampingan LoRA/pelatihan lanjutan. Pembagian data wajib pada level rekaman mentah/sesi/blok sebelum jendela bergulir dengan jeda pembersih >= W.
6. Deployment Pilihan 1 disinkronkan (Subbab 3.7, Gambar 2.1 dan 3.5, Tabel 3.8 #19): Pilihan 1 menjadi rancangan utama naskah (klasifikator saja, regresi dilepas), keputusan final menunggu hasil ablasi dan konfirmasi; Gambar 3.5 digambar ulang classifier-only dengan catatan Pilihan 2.
7. TTS Indonesia (Subbab 2.7, 3.5, Tabel 3.3 dan 3.8, 3.9): hasil verifikasi primer 14 Nov 2026 (berkas VOICES.md resmi) dicatat; Kokoro-82M v1.0 memuat sembilan kelompok suara delapan bahasa tanpa bahasa Indonesia dan lemah pada ujaran pendek, sehingga MMS-TTS-ind menjadi kandidat utama operasional [PERLU KONFIRMASI: Tabel 3.8 #17]; TTFA dilaporkan p50 dan p95 dengan konfigurasi uji terdokumentasi.
8. Biaya diluruskan (1.1, 3.4, 3.8.3): klaim "di bawah Rp350.000" diganti pemisahan pasangan modul inti (sekitar Rp300.000) dari total BOM node lengkap; Tabel 3.2 baru (kerangka BOM rencana, seluruh harga [PERLU DATA]); tabel BAB III berikutnya dinomori ulang (3.3 perangkat lunak sampai 3.9 risiko).
9. BAB II dipadatkan dari 17 menjadi 12 subbab: 2.2+2.3 menjadi 2.2 (CSI, ESP32-S3, akuisisi RuView), 2.4+2.5 menjadi 2.3 (encoder, transfer learning, jalur masukan), 2.6+2.7+2.8 menjadi 2.4 (dua kepala, modul temporal, kerugian gabungan), 2.11+2.12 menjadi 2.7 (TTS, ASR, pemetaan representasi); Gambar 2.1 (ilustrasi zona Fresnel) dihapus dan perhitungan radius tetap di teks; Gambar 2.2 menjadi Gambar 2.1 dengan pemisahan eksplisit graf akuisisi, pelatihan, dan deployment; seluruh referensi silang dinomori ulang satu kali dan diverifikasi.
10. Kajian pustaka diperkuat (Subbab 2.10, Tabel 2.3): ditambah [30] DensePose From WiFi (Geng dkk., 2022), [31] DF-WiSLR (Ahmed dkk., 2020; 49 gestur ISL 30 statis 19 dinamis), [32] Wi-SignFi (Gao dkk., 2023; multitugas CNN dan KNN pada dataset SignFi); klaim kebaruan dipersempit menjadi kombinatif (CSI satu tautan ESP32-S3 untuk SIBI, encoder RuView beku, supervisi 21 keypoint lintas modalitas, integrasi dua arah Indonesia); acuan TKT ditambah [29] Permenristekdikti 42/2016; klaim demografi 1.1 diperlunak dan batas penelusuran dinyatakan dengan log kueri [PERLU DATA].
11. Protokol dan etika (Subbab 3.6): sumber penanda waktu tunggal; urutan kartu diacak per blok; pencatatan repetisi terpakai; evaluasi kualitas keypoint khusus J/Z (laju deteksi, jitter, bingkai hilang); commit/hash checkpoint WPC [PERLU DATA]; persetujuan format aksesibel, persetujuan wali dan assent anak, masa retensi dan penghapusan permanen video, kontrol akses, dan pengakuan risiko identifikasi ulang.
12. Jadwal (Tabel 3.7): baris G0b disisipkan (awal T2, M4) sinkron dengan Gambar 3.1 dan Tabel 3.6; kuantisasi dan G1 dipindah ke fase M1-M8 pada Gambar 3.1; jadwal, gerbang, parameter, dan risiko selaras.
13. Pemadatan menyeluruh (1.1, 2.1-2.12, 3.1, 3.2, 3.5, 3.7, 3.8): prosa dirapatkan mengikuti kaidah humanizer-indonesia register akademik (satu gagasan per kalimat, verba kerja, tanpa nominalisasi menumpuk); seluruh angka, sitasi, persamaan bernomor, tabel, gerbang, penanda PERLU, dan batasan klaim dipertahankan; uji kegunaan ditegaskan formatif dan deskriptif; G1 menambah pelaporan coverage dan akurasi selektif.

Verifikasi: sitasi monoton [1] sampai [32] seluruhnya tersitasi; 32 entri daftar pustaka ([29] Permenristekdikti, [30] DensePose From WiFi, [31] DF-WiSLR, [32] Wi-SignFi terverifikasi 14 Nov 2026); persamaan (2.1) sampai (2.24) dengan (2.13a) dan (2.14a) serta (3.1) sampai (3.5) dengan (3.3a)/(3.3b) lengkap dan berurutan; tabel 2.1-2.4 dan 3.1-3.9 berurutan sesuai kemunculan; gambar 2.1 dan 3.1-3.5; G0b hadir di Gambar 3.1, Tabel 3.6, dan Tabel 3.7; tidak ada sisa "beacon ESP-NOW", "Persamaan 2.15'", "1 - WER", "( 1 / 56 )", "kehati-hatianya", "lambda~cls~", "d~ref~".
"""
log_baru = log.replace("\n\n## Log Perubahan — Revisi 14 November 2026, gelombang 17", LOG18 + "\n## Log Perubahan — Revisi 14 November 2026, gelombang 17", 1)
assert log_baru != log, "anchor log gelombang 17 tidak ditemukan"

out = V10 / "Proposal-SenseSIBI-Studi-Kelayakan-v18.md"
out.write_text(naskah + log_baru, encoding="utf-8")
(V10 / "_v18 Intermediate.md").unlink()
print("v18 tersimpan:", out, "|", len(naskah) + len(log_baru), "karakter")
