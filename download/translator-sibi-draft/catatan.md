# Catatan Penyusunan — Draft Proposal Utuh Penerjemah Dua Arah SIBI

**Paket:** `download/translator-sibi-draft/` · Disusun 26 Oktober 2026 · **Direvisi 26 Oktober 2026 (sesi 2): metodologi utama diganti menjadi distilasi guru–murid YOLO26-Pose → CSI atas permintaan pemilik ("ini yang seharusnya jadi proses metodologi utamanya"); diagram BAB I–II tetap di luar naskah sesuai revisi sesi 1.** · **27 Oktober 2026: JUDUL DIKUNCI FINAL oleh pemilik** (lihat §7 butir 2) — tidak ada perubahan teks naskah pada tanggal tersebut.
**Basis bahan:** `Bahan-Proposal-Translator-SIBI.md` (dossier Task 18, GEPA-validated) + `Proposal-Revisi-Translator-SIBI.md` (79 rujukan terverifikasi, Task 17) + 10 diagram Mermaid tervalidasi + 1 rujukan baru terverifikasi ([80] Hinton dkk., distilasi pengetahuan).
**Skill yang dipakai:** sempro-mepet (struktur & register korpus), naskah-id (EYD V + `periksa.py`), gepa-optimize-anything (optimasi kata kalimat kritis), K-Dense scientific-agent-skills (scientific-writing: ikatan bukti–klaim; experimental-design: pembanding/kontrol pada desain distilasi; scientific-critical-thinking: kekuatan klaim mengikuti bukti).

## 0. Revisi sesi 2 (26 Okt 2026): distilasi guru–murid menjadi metodologi utama

Atas permintaan pemilik, alur metodologi utama diganti mengikuti diagram yang diberikan pemilik: **YOLO26-Pose menjadi guru kamera (*camera teacher*)** yang mengekstrak pose/keypoint gerakan SIBI; hasilnya dipadankan dengan data Wi-Fi CSI untuk melatih **model murid (*student*)** yang berjalan langsung di ESP32-S3; **webcam dan YOLO26-Pose hanya dipakai saat akuisisi data dan pelatihan**, bukan pada perangkat akhir. Perubahan pokok:

| Aspek | Sebelum (Task 19–20) | Sesudah (revisi ini) |
|---|---|---|
| Peran YOLO26-Pose (§2.5, §3.7) | Alat bantu pelabelan (verifikasi batas segmen, saring segmen, diagnosis); "distilasi penuh diusulkan sebagai penelitian lanjutan" | **Model guru kamera**: di-*fine-tune* pada data visual SIBI (GPU Kaggle), dievaluasi kualitas keypoint-nya, deret pose menjadi supervisi tambahan pelatihan murid; saring/diagnosis tetap berjalan |
| Struktur §3.7 | 3.7.4 Klasifikasi (SVM + 1D-CNN dari fitur tersaring) | 3.7.4 **Model Guru Kamera YOLO26-Pose** + 3.7.5 **Dataset Murid dan Pelatihan Distilasi Guru–Murid** (skema pembagian, penolakan, kuantisasi bergeser ke 3.7.6–3.7.8) |
| Supervisi pelatihan | Label kelas saja | Label kelas (dari anotasi protokol) **+ suku supervisi guru** (bentuk dan bobot dari data validasi, Tabel 3.6 no. 27) + **pembanding ablasi** murid tanpa supervisi guru agar manfaat guru dinilai dari data, bukan diasumsikan |
| Masukan murid | Fitur segmen | **Jendela deret CSI** (bukan cuplikan tunggal) — gerak SIBI temporal |
| Pelatihan | Laptop RTX 3070 | **Layanan server GPU Kaggle** (laptop tetap untuk inferensi guru saat akuisisi, pengembangan, server lokal cadangan) |
| Jalur ucapan purwarupa | Server lokal laptop (MMS + faster-whisper) utama; awan opsional | **Layanan TTS/ASR awan utama**; server lokal (MMS + faster-whisper) **cadangan + pembanding**; latensi awan diukur sendiri (belum ada tolok ukur publik dari Indonesia — tetap tanpa klaim prapengukuran) |
| Antarmuka pengguna | Layar, speaker, mic | + **tombol tekan-untuk-bicara** (aktivasi mic arah 2) + **rotary encoder volume** |
| Kamus label–teks | Di server | **Salinan kecil dimuat di modul**; teks tampil di layar sebelum dikirim ke TTS awan |
| Rujukan | 79 | **80** — [80] Hinton, Vinyals, & Dean, "Distilling the knowledge in a neural network," arXiv:1503.02531, doi 10.48550/arXiv.1503.02531 (diverifikasi langsung ke halaman arXiv, 26 Okt 2026) |
| Diagram BAB III | 5 (Gambar 3.1–3.5) | **6 (Gambar 3.1–3.6)** — Gambar 3.2 baru: alur teacher–student; lihat §3 |

**Empat catatan teknis pemilik dipegang penuh:** (1) guru menghasilkan keypoint, bukan makna — label kelas tetap dari anotasi protokol; pengklasifikasi temporal atas keypoint disebut sebagai pengembangan lanjutan di luar cakupan (§2.5, §3.7.4, batasan no. 4 dan 9); (2) guru tidak dijalankan di ESP32-S3 — murid memprediksi dari CSI saja (§3.7.5); (3) jendela CSI temporal + validasi lintas sesi/pengguna + anggaran ukuran/RAM/latensi ESP32-S3 (§3.7.5–3.7.8, Gambar 3.5); (4) inferensi CSI→SIBI lokal; awan hanya TTS/STT; tanpa kamera saat operasi normal (§3.5.1, Gambar 3.3).

## 1. Jenis pekerjaan per bab

| Berkas | Jenis pekerjaan | Lingkup |
|---|---|---|
| `bab1-pendahuluan.md` | Sunting konsistensi (revisi sesi 2) | Rumusan/tujuan no. 1 (layanan ucapan awan + pelatihan murid dengan supervisi guru); batasan no. 3, 4, 5, 9; ¶purwarupa (tombol, rotary, Kaggle, peran laptop); ¶studi kelayakan (kalimat distilasi guru–murid); manfaat teoretis (deret pose guru; tepi-awan); sistematika BAB II–III |
| `bab2-kajian-pustaka.md` | Sunting konsistensi (revisi sesi 2) | §2.5 ditulis ulang inti (guru kamera + preseden [63][64] + distilasi [80]); §2.6 (1D-CNN = murid; pelatihan Kaggle); §2.7 (kriteria, TTS/ASR awan utama + lokal cadangan, alur dua arah baru); §2.9 (peran server lokal); §2.11 (kebaruan kombinatif + baris 17 tabel) |
| `bab3-metodologi.md` | Tulis ulang bagian metodologi (revisi sesi 2) | §3.1 (inti distilasi guru–murid); §3.2.3 T2 + **Gambar 3.2 baru**; §3.2.5 T4; §3.4 Tabel 3.1 (baris 4 tombol/rotary; peran laptop; AP internet) + Tabel 3.2 (guru, Kaggle, awan utama, lokal cadangan); §3.5.1–3.5.2 arsitektur & topologi baru (Gambar 3.3–3.4); §3.6.4 etika audio awan; **§3.7.4–3.7.5 baru**; §3.8.2 ablasi; §3.8.4 uji banding awan vs lokal; §3.9 jadwal; Tabel 3.6 (27 butir); Tabel 3.7 (9 risiko) |
| `daftar-pustaka.md` | Tambah 1 entri | [80] Hinton dkk. 2015 (terverifikasi ke arXiv); entri [1]–[79] tak tersentuh |
| `Draft-Proposal-Translator-SIBI.md` | Rakit ulang | 927 baris, ±16.800 kata, 80 rujukan, 6 diagram BAB III |
| `diagram/*.mmd` | Sunting + 1 baru + penomoran ulang | Lihat §3 |

## 2a. Revisi sesi 1 (26 Okt 2026): diagram BAB I–II dikeluarkan dari naskah

Atas permintaan pemilik ("aku tidak butuh diagram pada BAB 1 dan BAB 2, tapi jangan hapus itu dari sandbox"), lima blok diagram dikeluarkan dari naskah. Kalimat perujuk ditulis ulang: §1.1 "…Gambar 1.1 meringkas…" → "Kesenjangan-kesenjangan tersebut menjadi titik berangkat penelitian ini."; §1.1 "…sebagaimana ditunjukkan pada Gambar 1.2" dihapus; §2.2 "…taksonomi Gambar 2.1" dihapus; §2.7 "Alur lengkap arah pertama ditunjukkan pada Gambar 2.2. Modul pemancar…" → "Pada arah pertama, modul pemancar…"; §2.8 kalimat penutup Gambar 2.3 dihapus. **Kelima berkas `.mmd` tetap di `diagram/` sebagai konteks bacaan: G1.1, G1.2, G2.1, G2.2, G2.3.**

## 2. Perubahan penting lain sesi 2 (sebelum → sesudah)

1. "model pose YOLO26" → "**YOLO26-Pose**" di seluruh naskah (mengikuti istilah pemilik pada sesi ini; sebelumnya Task 19 menstandardkan sebaliknya — keputusan pemilik terbaru menang).
2. "jalur pelabelan" → "**jalur guru**" (bab 1–3 + label diagram).
3. Rumusan/tujuan no. 1: "…berkomunikasi dengan server lokal, termasuk protokol perekaman dataset isyarat terisolasi dengan pelabelan berbantuan model pose YOLO26?" → "…berkomunikasi dengan layanan ucapan awan, termasuk protokol perekaman dataset isyarat terisolasi serta pelatihan model murid CSI dengan supervisi model guru YOLO26-Pose?" (cermin 3:3 tetap terjaga).
4. Batasan no. 9: klausul pengecualian layanan *cloud* dihapus; diganti pengecualian "klasifikasi gerakan otomatis dari video oleh model guru".
5. §3.8.4: prosedur 4 langkah → 5 langkah (mengukur kedua jalur awan dan lokal; analisis keseimbangan mutu–latensi–koneksi).
6. Tabel 3.6: 25 → 27 butir (+no. 26 kriteria kualitas model guru; +no. 27 bentuk dan bobot suku supervisi guru); no. 22 diubah menjadi pilihan layanan ucapan awan dan ukuran model lokal.
7. Tabel 3.7: 8 → 9 risiko (no. 5 dibalik: kini "latensi/mutu layanan awan atau koneksi tidak tersedia" dengan mitigasi server lokal; +no. 9 kuota/aksesibilitas Kaggle dengan mitigasi data terkompresi dan pindah pelatihan murid ke laptop).
8. §3.6.4: +kalimat etika audio ke awan (diungkapkan di formulir persetujuan; kebijakan penyimpanan layanan diperiksa).
9. Kebaruan (§2.11): kini "…penginderaan CSI satu tautan antarmodul untuk SIBI, **distilasi guru–murid dari YOLO26-Pose ke model CSI**, inferensi pada perangkat, dan integrasi dua arah dengan pemrosesan bahasa Indonesia berbasis layanan awan" — tetap dinyatakan kombinatif, bukan klaim metode baru.

## 3. Diagram (11 berkas `.mmd` — semua lolos validasi mmdc)

**Status:** G3.1–G3.6 dimuat di naskah (BAB III, Gambar 3.1–3.6); G1.1–G2.3 berkas konteks (tidak dimuat, tetap di sandbox).

| Kode | Berkas | Gambar | Perubahan sesi 2 |
|---|---|---|---|
| G1.1 | `G1.1-peta-masalah.mmd` | — (konteks) | Tidak disentuh |
| G1.2 | `G1.2-visi-purwarupa.mmd` | — (konteks) | Tidak disentuh |
| G2.1 | `G2.1-taksonomi.mmd` | — (konteks) | Tidak disentuh |
| G2.2 | `G2.2-alur-arah1.mmd` | — (konteks) | Tidak disentuh |
| G2.3 | `G2.3-alur-arah2.mmd` | — (konteks) | Tidak disentuh |
| G3.1 | `G3.1-tahapan-gerbang.mmd` (was `G3.1-alur-pelatihan.mmd`) | 3.1 | Node T2: "pelatihan guru-murid … YOLO26-Pose tersinkron dengan CSI … server GPU Kaggle"; T2B: "murid ke modul" |
| G3.2 | `G3.2-alur-teacher-student.mmd` **(BARU)** | **3.2** | Alur metodologi utama: perekaman tersinkron → latih/evaluasi guru (loop kualitas keypoint) → ekstraksi keypoint → penyandingan berbasis waktu (loop cakupan) → dataset murid → latih murid + pembanding (SVM, ablasi) → gerbang G2/G3 → optimasi → deployment → perangkat akhir tanpa kamera |
| G3.3 | `G3.3-arsitektur-akhir.mmd` (was `G3.2-…`) | 3.3 | Dua jalur operasional: arah 1 (kamus kecil di modul → layar → TTS awan → speaker + rotary); arah 2 (tombol → mic → ASR awan → teks → representasi SIBI); jalur guru saat riset; server lokal cadangan (garis putus) |
| G3.4 | `G3.4-topologi-jaringan.mmd` (was `G3.3-…`) | 3.4 | AP dengan akses internet; subgraf layanan ucapan awan (jalur utama); server lokal = riset + cadangan |
| G3.5 | `G3.5-inferensi-tepi.mmd` (was `G3.4-…`) | 3.5 | Label node: "Model murid int8 TFLM / ESP-DL" |
| G3.6 | `G3.6-alur-dataset-evaluasi.mmd` (was `G3.5-…`) | 3.6 | +node "Latih dan evaluasi model guru"; dataset murid (jendela CSI + label + pose guru); node murid memuat "pembanding SVM dan ablasi tanpa supervisi guru" |

Sinkronisasi blok mermaid inline ↔ berkas `.mmd`: **6/6 identik** (berkas hanya menambah dua baris komentar `%%`). QA visual VLM (glm) atas G3.2 dan G3.3: **lolos** — tanpa teks terpotong, tanpa node/panah tumpang tindih, semua simpul keputusan berjalur ganda; catatan minor jarak label panah = perilaku bawaan mermaid, diterima.

## 4. Optimasi GEPA kalimat kritis (laporan jujur)

Kalimat kritis yang berubah pada sesi ini: rumusan no. 1, tujuan no. 1 (cermin), kalimat pembuka distilasi §3.1, dan kalimat topik ¶2 §2.5. Keempatnya dievaluasi dengan rubrik kebenaran (K) + formalitas + ketepatan + kealamian:

- rumusan/tujuan no. 1: 10/9/9/8 — kerangka kalimat sama dengan versi Task 17–19 (yang telah lolos 14 ronde GEPA adversarial); ekor klausa diganti (layanan ucapan awan + supervisi guru); tidak ada butir daftar periksa tertandai → **lolos gerbang saturasi, tanpa mutasi**.
- pembuka §3.1: 10/9/9/9 — dua kalimat pendek, subjek jelas → **saturasi**.
- topik §2.5: 10/9/9/9 → **saturasi**.

Sesuai gotcha #9 GEPA (mutasi tanpa kegagalan = derau), tidak ada mutasi dijalankan. Kalimat kritis lain (rumusan/tujuan no. 2–3, penutup latar belakang, sintesis §2.11) tidak berubah kerangkanya dari versi tervalidasi.

## 5. Hasil verifikasi

**`rakit_draft.py` (setelah revisi sesi 2): LOLOS — 13 OK, 2 peringatan diterima, 0 galat.**
- Daftar Pustaka lengkap 1..80; seluruh 80 entri dikutip minimal sekali; seluruh sitasi tubuh dalam 1..80.
- 6 blok mermaid + 6 keterangan Gambar (3.1–3.6, BAB III saja); setiap gambar dan setiap tabel (2.1, 2.2, 3.1–3.7) dirujuk prosa minimal sekali.
- Rumusan (3 butir) ↔ tujuan (3 butir) cermin 1:1; angka batasan BAB I identik BAB III.
- Struktur lengkap 6+11+11 subbab; akronim TTS/ASR tetap bersih dari prosa BAB I.
- Peringatan yang diterima: (a) satu kalimat sistematika §1.6 sepanjang 68 kata — peta isi bab satu baris per bab sesuai konvensi (vonis sama sejak Task 19); (b) informasi `PERLU RUJUKAN = 0`.

**`periksa.py` (naskah-id): 2 temuan — keduanya positif palsu yang diterima (vonis sama sejak Task 17):**
1. "F1 makro" — istilah metrik (macro-F1); tidak diganti.
2. "Respon" pada [9] — judul asli paper Mursita; judul karya tidak disunting.

**Validasi diagram: 11/11 lolos mmdc (6 dimuat + 5 konteks).** Satu galat EYD V baru (koma sebelum "sehingga" pada §3.7.4) ditemukan `periksa.py` dan langsung diperbaiki sebelum rakit final.

## 6. Penanda tersisa — 45 `PERLU DATA` (tidak satu pun diisi tebakan)

| Lokasi | Jumlah | Siapa pemegang keputusan |
|---|---|---|
| Sampul (nama, NIM, prodi, universitas, pembimbing, tahun) | 7 | Pemilik |
| §3.3 waktu dan lokasi | 2 | Pemilik + mitra |
| Tabel 3.1 (model layar, audio, baterai, access point) | 4 | Pemilik (uji arus T4) |
| Tabel 3.2 (layanan TTS awan final, layanan ASR awan final) | 2 | Pemilik + pembimbing (uji banding T4) |
| §3.6.2 daftar isyarat terpilih | 1 | Validator + pemilik |
| §3.6.4 lembaga persetujuan etik | 1 | Mitra |
| §3.8.4 daftar frasa uji | 1 | Pemilik + pembimbing |
| Tabel 3.6 parameter rancangan (27 butir, termasuk 2 baru: kriteria kualitas guru; bentuk dan bobot suku supervisi guru) | 27 | Pembimbing + hasil tahap T0/T2/T4 |

`PERLU RUJUKAN`: 0.

## 7. Yang perlu dikonfirmasi ke pembimbing (dossier §12.1 + tambahan sesi 2)

1. Gaya sitasi IEEE bernomor — konfirmasi akhir.
2. ~~Frasa judul "purwarupa" dan "kosakata terbatas" sebagai penanda klaim.~~ — **TUNTAS: dikunci final oleh pemilik, 27 Oktober 2026.** Judul final: *"Purwarupa Penerjemah Dua Arah Isyarat SIBI Berbasis Wi-Fi Channel State Information pada Modul ESP32-S3 dengan Inferensi Tepi dan Pemrosesan Bahasa pada Server: Studi Kelayakan Kosakata Terbatas"*. Frasa "purwarupa" dan "kosakata terbatas" dipertahankan sebagai penanda klaim (kejujuran cakupan); konsisten di sampul DOCX, tabel identitas, draft, dossier, dan seluruh dokumen pendukung.
3. Ambang G2 dan G3 yang dirumuskan relatif peluang acak — disepakati sebelum eksperimen.
4. Kesediaan atas rencana dua ruang mitra dan 3–4 pengisyarat.
5. Token apresiasi validator dan skala uji kegunaan 3–5 pengguna.
6. **(Baru)** Keputusan jalur ucapan awan sebagai jalur utama purwarupa (biaya kuota/jatah gratis layanan; kebijakan privasi audio ke awan untuk formulir etika).
7. **(Baru)** Layanan server GPU Kaggle sebagai mesin pelatihan guru dan murid (kuota mingguan; alternatif laptop bila kuota terbatas).

Satu butir dari skill sempro-mepet: **jumlah bab sistematika**. Draft memakai tiga bab; bila kampus mewajibkan lima, tambahkan baris BAB IV–V di §1.6.

## 8. Daftar istilah inti (satu istilah per konsep — jaga konsistensi saat menyunting)

modul pemancar (TX) · modul penerima (RX) · modul pengguna · zona isyarat · gerbang keputusan G0–G4 · **model guru / guru kamera** (*teacher*, *camera teacher*) · **model murid** (*student*) · **distilasi guru–murid** (*teacher–student*) · **YOLO26-Pose** (nama varian; menggantikan "model pose YOLO26") · **layanan server GPU Kaggle** · **layanan ucapan awan** (TTS/ASR awan, jalur utama) · **server lokal** (cadangan + riset) · tombol tekan-untuk-bicara · rotary encoder · kamus label-teks (salinan kecil di modul) · jendela CSI · suku supervisi guru · murid ablasi · penyaringan segmen · glos · ejaan jari · inferensi pada perangkat · model terkuantisasi int8 · laju bingkai · peluang acak · validator penutur tunarungu · pengisyarat kompeten · purwarupa · *elisitasi* (miring) · *deployment* (miring) · *dataset* (miring) · *subcarrier* (miring) · mikrokontroler (tegak, serapan KBBI).

## 9. Cara memakai paket ini

- **Baca cepat untuk sidang:** `Draft-Proposal-Translator-SIBI.md` + `Bahan-Proposal-Translator-SIBI.md` §11 (12 tanya-jawab sidang).
- **Sunting per bab:** sunting `bab1/bab2/bab3/daftar-pustaka.md`, lalu jalankan `python3 scripts/translator-sibi-draft/rakit_draft.py` (ekspektasi: 80 rujukan, 6 mermaid, Gambar 3.1–3.6).
- **Sunting diagram:** sunting blok mermaid di bab3 ATAU berkas `diagram/*.mmd`, lalu jalankan `python3 scripts/translator-sibi-draft/sinkron_diagram.py` untuk sinkronisasi dua arah + validasi mmdc.
- **Melihat kembali diagram BAB I–II:** buka `diagram/G1.1…G2.3` (konteks; render dengan `mmdc` atau mermaid.live).
- **Konversi DOCX:** pola generator Task 15–16 (`13-sempro-docx/generator/generate_docx.js`) dapat dipakai ulang bila pembimbing meminta format Word.
