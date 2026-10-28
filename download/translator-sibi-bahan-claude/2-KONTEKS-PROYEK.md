# 2 — Konteks Proyek dan Keputusan Terkunci

## Judul final (TERKUNCI — jangan ubah satu huruf pun)

> Purwarupa Penerjemah Dua Arah Isyarat SIBI Berbasis Wi-Fi Channel State Information pada Modul ESP32-S3 dengan Inferensi Tepi dan Pemrosesan Bahasa pada Server: Studi Kelayakan Kosakata Terbatas

Frasa "purwarupa" dan "kosakata terbatas" adalah **penanda klaim** (kejujuran cakupan) — wajib dipertahankan di seluruh naskah.

## Ringkasan proyek (satu paragraf)

Purwarupa penerjemah dua arah antara SIBI dan Bahasa Indonesia. Arah pertama: Wi-Fi CSI dari 2–3 modul ESP32-S3 dikenali model murid yang berjalan langsung di modul (inferensi tepi), label dipetakan ke teks lewat kamus kecil di modul, lalu disuarakan layanan TTS awan. Arah kedua: ucapan dikenali layanan ASR awan, teks dipetakan ke representasi SIBI di layar modul. Seluruhnya adalah studi kelayakan kosakata terbatas untuk konteks pendidikan formal.

## Delapan keputusan metodologi TERKUNCI (pemilik sudah memutuskan)

1. Metodologi utama = **distilasi guru–murid**: YOLO26-Pose = **guru kamera**; murid 1D-CNN = **model CSI**.
2. Guru kamera **hanya aktif saat akuisisi data dan pelatihan** (di-*fine-tune* di layanan server GPU Kaggle); **tidak ada kamera pada perangkat akhir**.
3. Murid memprediksi dari **jendela deret CSI** dengan supervisi label kelas + **suku supervisi deret pose guru**; tersedia **pembanding ablasi** (murid tanpa supervisi guru) dan pembanding SVM.
4. **Inferensi CSI→SIBI berjalan lokal di ESP32-S3** (model terkuantisasi int8, TensorFlow Lite Micro / ESP-DL).
5. **Awan hanya TTS/ASR** (jalur utama); server lokal laptop (MMS-TTS-ind + faster-whisper) = cadangan + pembanding; tidak ada inferensi isyarat di awan.
6. Label kelas berasal dari **anotasi protokol** — guru menghasilkan *keypoint*, bukan makna.
7. **Kamus label-teks kecil dimuat di modul**; teks tampil di layar sebelum dikirim ke TTS.
8. Antarmuka: layar, baterai, *speaker*, mikrofon, **tombol tekan-untuk-bicara**, **rotary encoder volume**.

## Kualifikasi kejujuran (jangan dilebih-lebihkan)

- Ini **studi kelayakan**, bukan penerjemahan kontinu kosakata penuh (preseden WiSign sudah mengenali kalimat ASL kontinu — klaim kebaruan naskah bersifat kombinatif saja).
- Kosakata 5–8 isyarat terisolasi, dibedakan lintasan lengan/tubuh atas/kepala — bukan bentuk jari.
- Pemetaan arah kedua = kamus kata-level + ejaan jari (26 huruf + 9 angka), bukan tata bahasa penuh.
- Setiap tahap ditutup gerbang keputusan G0–G4; kegagalan dilaporkan sebagai temuan kelayakan.

## Fakta dokumen (status saat ini)

| Aspek | Nilai |
|---|---|
| Panjang | 981 baris, 16.906 kata |
| Struktur | BAB I (6 subbab) + BAB II (11 subbab) + BAB III (11 subbab) + Daftar Pustaka |
| Rujukan | 80, gaya IEEE bernomor, semuanya dikutip minimal sekali di tubuh naskah |
| Gambar | 8 (Gambar 3.1–3.8, hanya di BAB III, blok Mermaid inline) |
| Tabel | Tabel 3.1–3.7 (7 tabel) + tabel identitas di kepala naskah |
| Penanda `[PERLU DATA]` | 44 (peta lokasi di Poin 5) |
| Status verifikasi | Lolos 13 pemeriksaan rakit otomatis; kalimat kritis lolos optimasi adversarial 14 ronde; 0 galat kaidah EYD |

## Dari mana naskah ini berasal

Disusun bertahap dari dossier bahan tervalidasi (optimasi GEPA), peta literatur 80 rujukan yang diverifikasi langsung ke sumber primer (Crossref/arXiv/penerbit), dan audit diagram 27 Oktober 2026 yang meredesain 8 figur hingga terbaca pada cetak 14 cm. **Setiap angka dan rujukan sudah dibayar mahal dengan verifikasi — jangan sentuh.**
