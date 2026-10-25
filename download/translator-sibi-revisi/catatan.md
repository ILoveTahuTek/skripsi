# Catatan Pengiriman — Paket Revisi Translator SIBI Dua Arah

Tanggal: 25 Oktober 2026. Paket ini merupakan keluaran tugas pengumpul bahan untuk revisi proposal sesuai visi produk terbaru pemilik penelitian (penerjemah dua arah portabel berbasis 2–3 modul ESP32-S3, YOLO26-Pose hanya untuk riset, produk akhir tanpa kamera).

## 1. Jenis pekerjaan per dokumen

| Dokumen | Jenis pekerjaan | Isi |
|---|---|---|
| `Proposal-Revisi-Translator-SIBI.md` | Tulis ulang total dari `Proposal-Sempro-DPJ4-SIBI-CSI.md` | BAB I–III + Daftar Pustaka; struktur subbab mengikuti dokumen sumber dengan subbab baru untuk TTS/ASR, pemetaan representasi SIBI, komunikasi perangkat-server, dan risiko |
| `Audit-Arsitektur-Translator-SIBI.md` | Tulis baru | Vonis kelayakan 10 komponen, audit pertahankan/revisi/hapus, arsitektur utama + cadangan A–D, batas MVP, uji validasi awal |
| `Matriks-Literatur-dan-Bukti.md` | Tulis baru | Matriks ±80 rujukan per kelompok dengan status verifikasi dan peran; kontradiksi; metodologi penelusuran |
| `Rencana-Visual-Proposal.md` + `diagram/*.mmd` | Tulis baru | Rencana 10 visual tersebar 2/3/5 per bab + 10 sumber Mermaid tervalidasi |
| `catatan.md` | Dokumen ini | Log perubahan, penanda tersisa, verifikasi |

## 2. Perubahan penting proposal lama menjadi revisi

1. Kerangka produk berubah dari alat latihan umpan balik menjadi purwarupa penerjemah dua arah; seluruh rumusan masalah, tujuan, batasan, manfaat, dan sistematika ditulis ulang mengikuti kerangka baru.
2. Perangkat berubah dari dua node ESP32 + laptop menjadi 2–3 modul ESP32-S3 (layar, baterai, speaker, mikrofon) dengan laptop ASUS TUF Dash F15 FX516PR sebagai mesin pelatihan dan server lokal; spesifikasi laptop kini eksplisit di batasan dan alat-bahan.
3. Inferensi pengenalan dipindah ke perangkat: model 1D-CNN dilatih di laptop, dikuantisasi int8, lalu dijalankan di modul melalui TensorFlow Lite Micro atau ESP-DL; subbab deployment baru ditambahkan.
4. Dua subbab kajian baru: TTS dan ASR Bahasa Indonesia (temuan utama: Kokoro tidak mendukung Indonesia; MMS-TTS-ind dipakai lokal; faster-whisper untuk ASR) dan pemetaan teks ke representasi SIBI (kamus kata-level + ejaan jari; bukan substitusi kata).
5. Uji persepsi kamera menyala/mati dihapus; kamera hanya tinggal di jalur pelabelan riset bersama YOLO26.
6. Enam rujukan lama dikeluarkan (Sigrist dkk. 2013; Zajonc 1965; Daniel dkk. 2024; Hassan dkk. 2026; dan dua entri pendukung) dan 21 rujukan baru terverifikasi ditambahkan, termasuk WiSign (kalimat ASL kontinu — membatasi klaim kebaruan), WiKey dan Mosleh dkk. (bukti gerak halus), Mursita 2015 (91% BISINDO), Rakun dkk. 2015 dan Anggraini dkk. 2019 (kata berinfleksi SIBI), serta dokumen resmi ESP32/layanan ucapan.
7. Tabel 3.6 dipangkas dan diperbarui (27 menjadi 25 butir) menyesuaikan rancangan baru; subbab risiko dan alternatif cadangan A–D ditambahkan (3.11).

## 3. Penanda tersisa

41 penanda `[PERLU DATA: ...]`, seluruhnya keputusan pemilik penelitian, pembimbing, atau hasil tahap sebelumnya (daftar isyarat terpilih, ambang gerbang, kanal dan jarak antarmodul, model perangkat final, indikator latensi layak, kuesioner, identitas mitra, dan sebagainya; daftar lengkap ada pada Tabel 3.6 dan bagian identitas). Tidak ada `[PERLU RUJUKAN: ...]`.

## 4. Hasil verifikasi

Evaluator rubrik D1–D6 (skill proposal-writing): skor 1,0 seluruh dimensi. Lint bahasa `periksa.py` (naskah-id): dua temuan tersisa dan keduanya diputuskan dipertahankan, yaitu frasa "skor F1 makro" yang merupakan istilah pengukuran baku dan kata "Respon" pada judul paper Mursita yang dikutip apa adanya sesuai kontrak kejujuran. Verifikasi struktur: 10 blok Mermaid selaras dengan 10 berkas `diagram/*.mmd`, 79 rujukan bernomor 1–79 seluruhnya dirujuk dari teks (207 rujukan sitasi), semua gambar dan tabel dirujuk dari prosa, dan seluruh diagram lolos validasi sintaks `mmdc`.

## 5. Yang perlu dikonfirmasi ke pembimbing

Gaya sitasi (IEEE bernomor dipakai mengikuti dokumen sumber); kata "purwarupa" dan frasa "kosakata terbatas" pada judul sebagai penanda klaim; kesediaan pembimbing atas rencana dua ruang pengujian dan 3–4 pengisyarat; serta pilihan TTS/ASR final yang memang ditunda ke T4 sesuai rancangan.

## 6. Jejak riset

Catatan riset lengkap tersimpan pada `riset-translator-sibi/` (T17-R2 teknis ESP32-S3+CSI, T17-R3 representasi SIBI) dan metadata Crossref rujukan baru pada `scripts/translator-sibi/meta_rujukan_baru.json`; riset TTS/ASR serta bukti gerak halus dan konektivitas dikerjakan langsung oleh agent utama setelah dua subagent pertama kehabisan waktu, dengan URL sumber tercatat pada `Matriks-Literatur-dan-Bukti.md`.
