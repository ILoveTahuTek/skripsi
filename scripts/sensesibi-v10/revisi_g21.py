#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Revisi gelombang 21: integrasi audit teknis + rencana QA (brief SENSESIBI-PROPOSAL-AUDIT-QA-001).
Basis: Proposal-SenseSIBI-v20.md -> Proposal-SenseSIBI-v21.md
Suntingan berjangkar (asersi tepat satu) + sisipan subbab 3.12/3.13 + DP [34][35] + log gelombang 21.
"""
from pathlib import Path

V10 = Path("/home/z/my-project/download/sensesibi-v10")
SRC = V10 / "Proposal-SenseSIBI-v20.md"
OUT = V10 / "Proposal-SenseSIBI-v21.md"
G21 = Path("/home/z/my-project/scripts/sensesibi-v10/_kerja-g21")

s = SRC.read_text(encoding="utf-8")
n_edit = 0

def ganti(lama: str, baru: str, label: str):
    global s, n_edit
    assert s.count(lama) == 1, f"[{label}] jangkar ditemukan {s.count(lama)}x (harus 1x)"
    s = s.replace(lama, baru)
    n_edit += 1
    print(f"  [{n_edit:02d}] {label}")

# ---- E1: baris identitas Jenis dokumen ----
ganti(
    "| Jenis dokumen | Proposal penelitian (seminar proposal), BAB I sampai III + Daftar Pustaka; revisi koreksi mekanisme akuisisi CSI atas v18: tiga mekanisme *firmware* RuView dipisahkan (*sounding* NDP dengan *callback* CSI, transport UDP ADR-018, ESP-NOW hanya sinkronisasi *mesh* opsional), versi *firmware* dikunci dan konfigurasi dua node diverifikasi pada G0; 33 rujukan |",
    "| Jenis dokumen | Proposal penelitian (seminar proposal), BAB I sampai III + Daftar Pustaka; integrasi Brief Audit Teknis dan Rencana Penjaminan Mutu atas audit enam sumber implementasi per 15 November 2026 (register temuan AUD-01 sampai AUD-20; 54 uji QA pada sembilan lapisan terikat gerbang G0 sampai G4); mekanisme akuisisi CSI dikoreksi dari injeksi NDP yang masih *stub* ADR-029 menjadi trafik OFDM *self-ping* dengan *callback* CSI *promiscuous*; 35 rujukan |",
    "identitas jenis dokumen",
)

# ---- E2: catatan penyusunan ----
ganti(
    "> Catatan penyusunan: versi ini menyunting naskah v18 sebagai revisi terarah atas koreksi pemilik mengenai mekanisme akuisisi CSI RuView; tidak ada bab yang ditulis ulang dan ruang lingkup sistem tidak berubah. Tiga mekanisme yang selama ini tercampur dipisahkan: jalur penginderaan memakai injeksi NDP dan *callback* CSI, jalur pengangkutan memakai UDP dengan format biner ADR-018, dan ESP-NOW hanya menjadi jalur sinkronisasi *mesh* opsional, bukan prasyarat akuisisi CSI. ESP-NOW karenanya dikeluarkan dari arsitektur inti dan tetap tercatat sebagai fitur sinkronisasi yang diuji hanya jika konfigurasi *mesh* memerlukannya. Gerbang G0 kini mewajibkan penguncian versi atau komit *firmware* RuView, verifikasi konfigurasi dua node dengan peran tetap tanpa implementasi ESP-NOW tambahan, serta uji kestabilan CSI mentah saat *sounding* dan UDP berjalan bersamaan; keberhasilan instalasi dan terkirimnya bingkai CSI tidak diperlakukan sebagai bukti akurasi penginderaan maupun kestabilan jangka panjang. Dua rujukan baru ditambahkan, yaitu dokumentasi *firmware* CSI RuView dan panduan penggunaannya; nomor sitasi lama 1 sampai 31 dipertahankan tanpa penomoran ulang. Keputusan terbuka pada Tabel 3.7 tetap tidak diputuskan sepihak; rincian perubahan per subbab ada pada Log Perubahan gelombang 19 di ujung naskah.",
    "> Catatan penyusunan: versi ini menyunting naskah v20 sebagai integrasi Brief Audit Teknis dan Rencana Penjaminan Mutu atas mandat pemilik tertanggal 15 November 2026; tidak ada bab yang ditulis ulang dan ruang lingkup sistem tidak berubah. Audit atas enam sumber implementasi (repositori RuView pada komit terkunci, kartu model *encoder* terpralatih, repositori WPC, *kit* wifi-sensing-kit, makalah *DensePose From WiFi*, dan naskah v20 sendiri) menghasilkan register dua puluh temuan AUD-01 sampai AUD-20 yang dirangkum pada Subbab 3.12. Dua temuan berat diikuti koreksi: mekanisme akuisisi CSI dinyatakan ulang karena injeksi NDP pada *firmware* masih berstatus *stub* tanpa pemanggil, sehingga jalur penginderaan kini memakai trafik OFDM terjadwal (*self-ping*) dengan *callback* CSI *promiscuous*; dan kebijakan mask visibilitas diketatkan karena label visibilitas dataset guru bernilai konstan. Subbab 3.13 menambahkan rencana penjaminan mutu sembilan lapisan dengan 54 uji berpengenal yang terikat pada gerbang G0 sampai G4 tanpa menambah gerbang baru; seluruh status uji pada saat penyusunan ialah belum diuji dan tidak ada hasil yang dikarang. Dua rujukan baru ditambahkan, yaitu repositori *wifi-sensing-kit* dan makalah *DensePose From WiFi*; nomor sitasi lama 1 sampai 33 dipertahankan tanpa penomoran ulang. Keputusan terbuka pada Tabel 3.7 tetap tidak diputuskan sepihak; rincian perubahan per subbab ada pada Log Perubahan gelombang 21 di ujung naskah.",
    "catatan penyusunan",
)

# ---- E3: 1.6 sistematika ----
ganti(
    "skenario pengujian, jadwal, parameter yang ditetapkan kemudian, serta risiko dan cadangannya.",
    "skenario pengujian, jadwal, parameter yang ditetapkan kemudian, serta risiko dan cadangannya, lalu ditutup dengan brief audit teknis atas sumber implementasi serta rencana penjaminan mutu yang mengikat pengujian pada gerbang G0 sampai G4.",
    "1.6 sistematika",
)

# ---- E4: Batasan no. 12 ----
ganti(
    "12. Akuisisi CSI mengikuti mekanisme bawaan *firmware* RuView, yaitu injeksi NDP, *callback* CSI, dan transport UDP dengan format ADR-018; mekanisme radio tidak dibangun ulang, ESP-NOW tidak dijadikan prasyarat, dan sinkronisasi *mesh* hanya diuji jika konfigurasi node memerlukannya.",
    "12. Akuisisi CSI mengikuti mekanisme bawaan *firmware* RuView yang terverifikasi dari kode, yaitu *self-ping* OFDM terjadwal ke *gateway*, *callback* CSI pada mode *promiscuous*, dan transport UDP dengan format ADR-018; injeksi NDP masih berstatus *stub* ADR-029 sehingga tidak dipakai; mekanisme radio tidak dibangun ulang, ESP-NOW tidak dijadikan prasyarat, dan sinkronisasi *mesh* hanya diuji jika konfigurasi node memerlukannya.",
    "Batasan no. 12",
)

# ---- E5: Tabel 2.1 baris 2 ----
ganti(
    "| *Station* Wi-Fi + *callback* CSI + injeksi NDP + UDP pada satu *chip*; ESP-NOW hanya sinkronisasi *mesh* opsional | Dasar topologi satu kanal (Subbab 3.5) |",
    "| *Station* Wi-Fi + *callback* CSI mode *promiscuous* + trafik OFDM terjadwal (*self-ping* 10–50 Hz) + UDP pada satu *chip*; injeksi NDP masih *stub* ADR-029; ESP-NOW hanya sinkronisasi *mesh* opsional | Dasar topologi satu kanal (Subbab 3.5) |",
    "Tabel 2.1 baris 2",
)

# ---- E6: paragraf mekanisme 2.3 ----
ganti(
    "Peran tiga mekanisme radio pada *firmware* RuView dibedakan agar fungsinya tidak tertukar [32], [33]. Jalur penginderaan memakai injeksi NDP (*Null Data Packet*) beserta *callback* CSI: node pemancar menyuntikkan bingkai *sounding* Wi-Fi, lalu node penerima menangkap CSI dari bingkai tersebut. Jalur pengangkutan memakai UDP dengan format biner ADR-018 [32]. Adapun ESP-NOW bukan jalur pengiriman bingkai CSI; protokol itu hanya muncul sebagai sinkronisasi *mesh* opsional pada implementasi tertentu [33]. Purwarupa satu tautan dengan satu penerima karenanya tidak menjadikan ESP-NOW prasyarat akuisisi CSI, sedangkan sinkronisasi kamera dan CSI ditangani terpisah lewat penanda waktu (Subbab 3.6).",
    "Peran mekanisme radio pada *firmware* RuView dibedakan agar fungsinya tidak tertukar [32], [33], dan pemetaannya kini mengikuti audit kode pada Subbab 3.12. Jalur penginderaan memakai *callback* CSI pada mode *promiscuous* dengan sumber trafik OFDM terjadwal: *firmware* melakukan *self-ping* ke *gateway* pada rentang 10 sampai 50 Hz (baku 50 Hz) sehingga balasan ICMP OFDM beserta bingkai data lain ditangkap dan CSI-nya dilaporkan, dengan pembatasan laju pelaporan paling tinggi 50 bingkai per detik. Injeksi NDP (*Null Data Packet*) yang dijanjikan diagram arsitektur dokumentasi masih berupa *stub* ADR-029: fungsinya tersedia pada antarmuka dan mengirim bingkai Null Data 24 byte sebagai penampung, tetapi belum dipanggil pengendali mana pun pada kode yang diaudit, jadi mekanisme itu tidak dipakai pada *baseline* penelitian ini (AUD-01). Jalur pengangkutan memakai UDP dengan format biner ADR-018 [32]. Adapun ESP-NOW bukan jalur pengiriman bingkai CSI; protokol itu hanya muncul sebagai sinkronisasi *mesh* opsional pada implementasi tertentu [33]. Purwarupa satu tautan dengan satu penerima karenanya tidak menjadikan ESP-NOW prasyarat akuisisi CSI, sedangkan sinkronisasi kamera dan CSI ditangani terpisah lewat penanda waktu (Subbab 3.6). Konsekuensi praktisnya ada dua. Pertama, node TX berperan sebagai penjana trafik OFDM terjadwal, bukan penyuntik NDP. Kedua, bingkai ADR-018 baku tidak memuat MAC pengirim sehingga atribusi bingkai ke tautan TX-RX memerlukan penandaan MAC pengirim menurut pola yang telah didemonstrasikan *kit* komunitas di atas *firmware* yang sama [34]; tambahan minimal itu diaudit dan diuji pada T0 (AUD-03).",
    "paragraf mekanisme 2.3",
)

# ---- E7: kalimat G0 pada 2.3 ----
ganti(
    "dan kestabilan CSI mentah diuji saat *sounding* dan UDP berjalan bersamaan (Tabel 3.5).",
    "dan kestabilan CSI mentah diuji saat trafik OFDM terjadwal serta UDP berjalan bersamaan (Tabel 3.5).",
    "kalimat G0 2.3",
)

# ---- E8: paragraf audit 2.4 (NUL + SISO) ----
ganti(
    "Audit dokumentasi repositori RuView dan Hugging Face per 14 November 2026 menemukan dua hal teknis yang wajib diverifikasi pada tahap T0. Pertama, kartu model memuat dua keluarga berkas, yaitu `model.safetensors`/`model.rvf.jsonl` dan keluarga `csi-embed-v2` (`csi-embed-v2.safetensors`, `csi-embed-v2-int4.bin`, serta `csi-embed-v2.py` yang menyertakan *standardizer* FP16), sedangkan berkas `model.safetensors` tercatat memiliki *NUL-padding* pada *header* sehingga ditolak oleh `safetensors.torch.load_file` [10], [11]. Kedua, catatan teknis RuView secara eksplisit memperingatkan bahwa aliran CSI antena tunggal (SISO) 56 *subcarrier* pada ESP32 tidak menyimpan informasi spasial sehalus NIC multi-antena, dan percobaan awal estimasi sendi distal pada satu perangkat mendekati acak; angka triplet-temporal 82,3% juga hanya diukur pada satu ruangan, satu rekaman, dan dua node [10], [11]. Karena itu, audit T0 mencakup pemilihan keluarga berkas yang dimuat, verifikasi *standardizer*, serta pembatasan klaim ke kondisi terukur tersebut.",
    "Audit dokumentasi repositori RuView dan Hugging Face, diperbarui per 15 November 2026, menemukan beberapa hal teknis yang wajib diverifikasi pada tahap T0. Pertama, kartu model memuat dua keluarga berkas, yaitu `model.safetensors` beserta `model.rvf.jsonl` dan keluarga `csi-embed-v2` (`csi-embed-v2.safetensors`, `csi-embed-v2-int4.bin`, serta `csi-embed-v2.py` yang menyertakan *standardizer* FP16); metadata kedua keluarga tidak saling cocok pada sejumlah angka seperti jumlah epoch, temperatur InfoNCE, jendela pasangan temporal, dan peringkat LoRA, sementara berkas `model.rvf.jsonl` tidak didokumentasikan pada kartunya, jadi pemilihan keluarga berkas direkonsiliasi secara eksplisit pada T0 (AUD-08). Kedua, cacat *NUL-padding* pada *header* `model.safetensors` yang pernah tercatat sebagai isu RuView #1522 telah diperbaiki pada 13 Oktober 2026; verifikasi ulang atas berkas saat ini menunjukkan *header* tanpa byte NUL dan bobot termuat utuh sebagai 17 tensor, tetapi audit T0 tetap memverifikasi pemuatan langsung di lingkungan penelitian (AUD-07). Ketiga, catatan teknis RuView secara eksplisit memperingatkan bahwa aliran CSI antena tunggal (SISO) 56 *subcarrier* pada ESP32 tidak menyimpan informasi spasial sehalus NIC multi-antena, dan percobaan awal estimasi sendi distal pada satu perangkat mendekati acak; angka triplet-temporal 82,3% juga hanya diukur pada satu ruangan, satu rekaman, dan dua node [10]. Karena itu, audit T0 mencakup pemilihan keluarga berkas yang dimuat, verifikasi *standardizer*, serta pembatasan klaim ke kondisi terukur tersebut.",
    "paragraf audit 2.4",
)

# ---- E9: catatan mask 2.7 ----
ganti(
    "mask berlaku per *keypoint*, bukan per koordinat. Jika prediksi visibilitas juga diinginkan,",
    "mask berlaku per *keypoint*, bukan per koordinat. Hasil audit menambahkan satu kehati-hatian: label visibilitas pada dataset guru bernilai konstan untuk seluruh titik (AUD-12), jadi komponen visibilitas tidak diwarisi mentah dari label, melainkan diturunkan dari kualitas deteksi tangan dan verifikasi sampel anotasi sebelum mask efektif dipakai (Subbab 3.13). Jika prediksi visibilitas juga diinginkan,",
    "catatan mask 2.7",
)

# ---- E10: 2.9 visibilitas guru (kalimat pertama paragraf pertama) ----
ganti(
    "pada tiap bingkai, YOLO26m-Pose [12] menghasilkan kelas isyarat beserta 21 *keypoint* tangan dan visibilitasnya.",
    "pada tiap bingkai, YOLO26m-Pose [12] menghasilkan kelas isyarat beserta 21 *keypoint* tangan dan visibilitasnya; nilai visibilitas itu dibaca sebagai skor keyakinan deteksi, bukan kebenaran oklusi, karena label dataset guru menetapkannya konstan (AUD-12).",
    "2.9 visibilitas kalimat pertama",
)

# ---- E11: 2.9 cakupan exp11 (J/Z) ----
ganti(
    "tidak dikutip sebagai kemampuan guru mengenali J dan Z, yang supervisinya diambil dari lintasan *keypoint* dan label protokol.",
    "tidak dikutip sebagai kemampuan guru mengenali J dan Z, yang supervisinya diambil dari lintasan *keypoint* dan label protokol; audit 15 November 2026 menegaskan cakupannya karena label eksperimen itu dipetakan ulang ke 24 kelas huruf A sampai Y tanpa J dan Z (AUD-15).",
    "2.9 cakupan exp11",
)

# ---- E12: 2.9 penanda J/Z diselesaikan ----
ganti(
    "guru tidak diposisikan sebagai pengklasifikasi kedua huruf gerak itu kecuali model guru terbukti memuat kelasnya [PERLU VALIDASI: kelas J dan Z pada model juara WPC]. Dengan pemisahan ini,",
    "guru tidak diposisikan sebagai pengklasifikasi kedua huruf gerak itu karena audit atas repositori WPC menegaskan model juara tidak memuat kelas J dan Z (AUD-15). Dengan pemisahan ini,",
    "2.9 penanda J/Z diselesaikan",
)

# ---- E13: 2.9 kebijakan mask supervisi ----
ganti(
    "sedangkan guru menyumbang deret 21 *keypoint* beserta visibilitasnya. Untuk J dan Z,",
    "sedangkan guru menyumbang deret 21 *keypoint* beserta visibilitasnya; sesuai temuan AUD-12, mask efektif regresi menggabungkan penanda langkah valid dengan saringan kualitas deteksi serta verifikasi sampel alih-alih mewarisi nilai label (Subbab 2.7 dan 3.13). Untuk J dan Z,",
    "2.9 kebijakan mask",
)

# ---- E14: 3.4 kalimat TX ----
ganti(
    "TX menyuntikkan bingkai *sounding* NDP, sedangkan RX menangkap CSI 56 *subcarrier* pada 2,4 GHz kanal 20 MHz melalui *callback* CSI sekaligus memuat antarmuka.",
    "TX menjana trafik OFDM terjadwal (*self-ping* ke *gateway*) sebagai sumber bingkai, sedangkan RX menangkap CSI 56 *subcarrier* pada 2,4 GHz kanal 20 MHz melalui *callback* CSI mode *promiscuous* sekaligus memuat antarmuka.",
    "3.4 kalimat TX",
)

# ---- E15: Tabel 3.1 baris 1 keterangan ----
ganti(
    "| 2 unit | Node TX (pemancar bingkai *sounding* NDP) dan node RX (penerima CSI dan antarmuka) |",
    "| 2 unit | Node TX (penjana trafik OFDM *self-ping*) dan node RX (penerima CSI dan antarmuka) |",
    "Tabel 3.1 baris 1",
)

# ---- E16: 3.5 arah pertama ----
ganti(
    "Pada arah pertama, bingkai *sounding* NDP yang disuntikkan node pemancar melintasi zona isyarat,",
    "Pada arah pertama, bingkai OFDM trafik *self-ping* yang dipancarkan node TX melintasi zona isyarat,",
    "3.5 arah pertama",
)

# ---- E17: G3.3 accDescr ----
ganti(
    "Arah 1 mengalir dari bingkai sounding NDP node TX melalui zona isyarat ke node RX",
    "Arah 1 mengalir dari bingkai OFDM trafik self-ping node TX melalui zona isyarat ke node RX",
    "G3.3 accDescr",
)

# ---- E18: G3.3 simpul TX ----
ganti(
    'TX["Node TX: injeksi NDP"]',
    'TX["Node TX: penjana trafik OFDM"]',
    "G3.3 simpul TX",
)

# ---- E19: 3.5 topologi ----
ganti(
    "Node pemancar menyuntikkan bingkai *sounding* NDP sebagai sumber bingkai CSI,",
    "Node TX menjana trafik OFDM terjadwal sebagai sumber bingkai CSI,",
    "3.5 topologi",
)

# ---- E20: 3.8 rujukan silang ke 3.12/3.13 ----
ganti(
    "dibaca sebagai indikasi ketahanan awal, bukan bukti generalisasi populasi (Subbab 1.4).",
    "dibaca sebagai indikasi ketahanan awal, bukan bukti generalisasi populasi (Subbab 1.4). Rincian prasyarat, metrik, ambang, dan bukti setiap uji dirinci pada Rencana Penjaminan Mutu Subbab 3.13, sedangkan temuan audit atas sumber implementasi yang mendasari rancangan ini dirangkum pada Subbab 3.12.",
    "3.8 rujukan silang",
)

# ---- E21: kriteria G0 Tabel 3.5 ----
ganti(
    "terbaca stabil saat injeksi NDP dan pengiriman UDP berjalan bersamaan; laju sekurang-kurangnya 25 bingkai per detik;",
    "terbaca stabil saat trafik OFDM terjadwal dan pengiriman UDP berjalan bersamaan; atribusi bingkai CSI ke tautan TX-RX terverifikasi lewat penandaan atau penyaringan MAC pengirim; laju sekurang-kurangnya 25 bingkai per detik;",
    "kriteria G0 Tabel 3.5",
)

# ---- E22: pengantar Tabel 3.7 kelompok baris ----
ganti(
    "sedangkan baris 2 sampai 12, 15, 18, dan 21 merupakan parameter teknis dan *hyperparameter* yang penetapannya berbasis hasil audit atau data validasi.",
    "sedangkan baris 2 sampai 12, 15, 18, serta 21 sampai 22 merupakan parameter teknis dan *hyperparameter* yang penetapannya berbasis hasil audit atau data validasi.",
    "pengantar Tabel 3.7",
)

# ---- E23: Tabel 3.7 baris 6 diperluas ----
ganti(
    "| 6 | Pilihan jalur masukan *encoder* (fitur turunan atau adapter), parameter normalisasi masukan, dan panjang barisan T | Hasil audit T0 dan gerbang G0b | [PERLU VALIDASI: parameter normalisasi masukan checkpoint; keputusan jalur G0b; finalisasi T dari data pilot] |",
    "| 6 | Pilihan jalur masukan *encoder* (fitur turunan atau adapter), parameter normalisasi masukan, panjang barisan T, serta pemilihan keluarga berkas *checkpoint* (`model.safetensors` lawan `csi-embed-v2`) beserta rekonsiliasi metadata kartu model (AUD-07, AUD-08) | Hasil audit T0 dan gerbang G0b | [PERLU VALIDASI: parameter normalisasi masukan checkpoint; pemilihan keluarga berkas; keputusan jalur G0b; finalisasi T dari data pilot] |",
    "Tabel 3.7 baris 6",
)

# ---- E24: Tabel 3.7 baris 22 baru ----
ganti(
    "| 21 | Peran ESP-NOW dan konfigurasi node akuisisi CSI (ESP-NOW dikeluarkan dari jalur inti; dua node peran tetap diverifikasi tanpa implementasi ESP-NOW tambahan; sinkronisasi *mesh* hanya jika diperlukan) | Keputusan pemilik 14 Nov 2026 atas audit dokumentasi *firmware* RuView [32], [33] | Ditetapkan; ESP-NOW diaktifkan kembali hanya jika konfigurasi *mesh* TDM memerlukannya dan penggunaannya dilaporkan |",
    "| 21 | Peran ESP-NOW dan konfigurasi node akuisisi CSI (ESP-NOW dikeluarkan dari jalur inti; dua node peran tetap diverifikasi tanpa implementasi ESP-NOW tambahan; sinkronisasi *mesh* hanya jika diperlukan) | Keputusan pemilik 14 Nov 2026 atas audit dokumentasi *firmware* RuView [32], [33] | Ditetapkan; ESP-NOW diaktifkan kembali hanya jika konfigurasi *mesh* TDM memerlukannya dan penggunaannya dilaporkan |\n| 22 | Mekanisme akuisisi CSI *baseline* (trafik OFDM terjadwal *self-ping* 10–50 Hz ke *gateway*, *callback* CSI mode *promiscuous*, transport UDP ADR-018; injeksi NDP masih *stub* ADR-029 sehingga tidak dipakai; atribusi bingkai ke tautan TX-RX lewat penandaan MAC pengirim) | Audit kode *firmware* 15 Nov 2026 (Subbab 3.12, AUD-01 sampai AUD-04) | Ditetapkan; injeksi NDP dievaluasi ulang hanya jika *controller PR* RuView mendarat sebelum T2 dan perubahannya dilaporkan |",
    "Tabel 3.7 baris 22",
)

# ---- E25: Tabel 3.8 baris 13 ditulis ulang + baris 14 baru ----
ganti(
    "| 13 | Konfigurasi dua node peran tetap tidak terverifikasi pada *firmware* RuView yang dipakai; dokumentasi standarnya memakai *mesh* multistatik 3–6 node dengan TDM [33] | G0 tidak dapat dinilai atau CSI tidak stabil | Kunci versi atau komit *firmware*, uji dua node tanpa ESP-NOW tambahan pada perangkat nyata; jika bermasalah, ikuti konfigurasi node pada dokumentasi *firmware* termasuk pengaturan TDM, lalu laporkan sebagai penyimpangan rancangan yang disengaja |",
    "| 13 | Mekanisme akuisisi dua node tidak berjalan seperti dirancang: injeksi NDP masih *stub* (AUD-01), bingkai baku belum memuat MAC pengirim (AUD-03), dan dokumentasi standarnya memakai *mesh* multistatik 3–6 node dengan TDM [33] | G0 tidak dapat dinilai atau CSI tidak stabil | Jalankan *baseline* trafik OFDM *self-ping* dengan tangkapan *promiscuous*; tambahkan penandaan MAC pengirim menurut pola *kit* [34] atau tambahan minimal setara yang diaudit; jika tetap bermasalah, ikuti konfigurasi node pada dokumentasi *firmware* termasuk pengaturan TDM, lalu laporkan sebagai penyimpangan rancangan yang disengaja |\n| 14 | Visibilitas label guru bernilai konstan untuk seluruh *keypoint* sehingga tidak mencerminkan oklusi nyata (AUD-12) | Supervisi regresi mengandung derau titik terhalang | Mask visibilitas tidak diwarisi dari label; saringan kualitas deteksi, verifikasi sampel validator, dan laporan tingkat segmen terbuang dijalankan (QA-DS-02, QA-DS-03); perbaikan pipeline anotasi guru didokumentasikan sebelum label dipakai |",
    "Tabel 3.8 baris 13-14",
)

# ---- E26: sisip 3.12 + 3.13 sebelum DAFTAR PUSTAKA ----
b312 = (G21 / "bagian-312.md").read_text(encoding="utf-8").strip()
b313 = (G21 / "bagian-313.md").read_text(encoding="utf-8").strip()
ganti(
    "# DAFTAR PUSTAKA",
    b312 + "\n\n" + b313 + "\n\n# DAFTAR PUSTAKA",
    "sisipan 3.12 + 3.13",
)

# ---- E27: DP [34] [35] ----
ganti(
    '[33] ruvnet, "RuView User Guide," panduan pengguna RuView, repositori GitHub. [Online]. Available: https://github.com/ruvnet/RuView/blob/main/docs/user-guide.md, diakses 14 Nov. 2026.',
    '[33] ruvnet, "RuView User Guide," panduan pengguna RuView, repositori GitHub. [Online]. Available: https://github.com/ruvnet/RuView/blob/main/docs/user-guide.md, diakses 14 Nov. 2026.\n\n[34] A. Gauracs, "wifi-sensing-kit," repositori GitHub, 2026. [Online]. Available: https://github.com/andrisgauracs/wifi-sensing-kit, diakses 15 Nov. 2026.\n\n[35] J. Geng, D. Huang, and F. De la Torre, "DensePose From WiFi," arXiv preprint arXiv:2301.00250, 2022, doi: 10.48550/arXiv.2301.00250. [Online]. Available: https://arxiv.org/abs/2301.00250, diakses 15 Nov. 2026.',
    "DP [34] [35]",
)

# ---- E28: Log gelombang 21 ----
LOG = """## Log Perubahan — Revisi 15 November 2026, gelombang 21 (integrasi audit teknis dan rencana penjaminan mutu; koreksi mekanisme akuisisi CSI atas bukti kode)

Permintaan: brief pemilik SENSESIBI-PROPOSAL-AUDIT-QA-001; audit enam sumber pada 15 November 2026 (RuView komit 3bae24a dengan firmware v0.8.18, kartu model wifi-densepose-pretrained sha 98b29a35, WPC komit 249a63d, wifi-sensing-kit komit 7fb77fc, makalah arXiv 2301.00250v1, naskah v20 komit a0f2d7a); kaidah bahasa skill sempro-mepet; nomor sitasi [1] sampai [33] dipertahankan dengan dua rujukan baru [34] wifi-sensing-kit dan [35] DensePose From WiFi.

- AUD-01 KRITIS: injeksi NDP pada firmware RuView masih stub tanpa satu pun pemanggil (csi_collector.c:940-982, komentar ADR-029; rv_radio_ops_esp32.c:84-88 menyatakan menunggu controller PR); narasi dikoreksi dari "TX menyuntikkan bingkai sounding NDP" menjadi trafik OFDM self-ping 10-50 Hz + callback CSI promiscuous pada Batasan no. 12, Tabel 2.1 baris 2, 2.3, 3.4, Tabel 3.1 baris 1, 3.5, Gambar 3.3 (simpul TX + accDescr dirender ulang), dan kriteria G0; Tabel 3.7 no. 22 baru menetapkan mekanisme baseline; Tabel 3.8 no. 13 ditulis ulang.
- AUD-03: bingkai ADR-018 baku tidak memuat MAC pengirim; atribusi tautan TX-RX lewat patch penandaan MAC pola kit [34] diuji pada T0 (QA-FW-04); dikutip pada 2.3, G0, dan Tabel 3.8.
- AUD-07: cacat NUL-padding model.safetensors (isu RuView #1522) telah diperbaiki 13 Okt 2026 pada komit 98b29a35; paragraf 2.4 diperbarui dari "ditolak safetensors" menjadi status diperbaiki dengan verifikasi T0 tetap wajib.
- AUD-08: inkonsistensi metadata dua keluarga berkas kartu model (epoch 20 lawan 60, temperatur 0,07 lawan 0,1, jendela pasangan temporal, peringkat LoRA 4 lawan 8, model.rvf.jsonl tak terdokumentasi, klaim "12 minutes" lawan 34,9 menit) dicatat pada 2.4; Tabel 3.7 no. 6 diperluas ke pemilihan keluarga berkas.
- AUD-09: catatan SISO (isu #509) hanya berada pada README utama RuView, bukan kartu model; kutipan 2.4 dikoreksi dari [10], [11] menjadi [10].
- AUD-12 KRITIS: write_label() WPC (convert_sibi_v2.py:286-297) menulis visibilitas konstan 2 untuk seluruh 21 keypoint; kebijakan mask diperjelas pada 2.7, 2.9 (dua lokasi), Tabel 3.8 no. 14 baru, dan QA-DS-02: mask efektif tidak mewarisi label, melainkan penanda langkah valid + saringan kualitas deteksi + verifikasi sampel.
- AUD-13, AUD-14: flip_idx identitas terverifikasi empiris dan komposisi dataset v2 (9.953; dedup md5 -2.215; leak-guard dHash -18; 7.210 sukses / 510 gagal; 7.627 objek; split 6.231/650/329; Roboflow CC BY 4.0) terkonfirmasi mendukung klaim 2.9 tanpa suntingan.
- AUD-15: penanda [PERLU VALIDASI: kelas J dan Z pada model juara WPC] terjawab: exp11_huruf24 dilatih pada label yang dipetakan ulang ke 24 kelas huruf A sampai Y tanpa J dan Z (val 333 instance; mAP50 0,9580; mAP50-95 0,7235; box 0,9942/0,8918; conf 0,25 membaca 325/333 atau 97,6% dengan 5 pertukaran dan 3 deteksi hilang); 2.9 diperbarui menjadi fakta audit tanpa memperluas klaim.
- AUD-16: bobot exp11 belum diarsipkan di repositori WPC (folder eksperimen memuat metrik dan kernel saja; MANIFEST memuat exp00-exp10 dan exp06b sha256 073ccf71); penanda [PERLU DATA: tag dan hash exp11] pada rujukan [12] tetap terbuka dengan bukti baru.
- AUD-18: wifi-sensing-kit diaudit sebagai kit orkestrasi di atas firmware RuView v0.8.8 dengan patch MAC (tanpa NDP, tanpa peran TX/RX tetap, laju sekitar 50 Hz dibagi antar tautan, hanya ESP32-S3, ESP-IDF v5.4/5.5, MIT, 4 komit); dicatat sebagai pola atribusi AUD-03 dan opsi jalur pembanding pasif, bukan komponen inti; rujukan [34] baru.
- AUD-19: makalah DensePose From WiFi diverifikasi pracetak tanpa telaah sejawat (3 antena TX × 3 RX, 30 subcarrier, 100 Hz, keluaran IUV 24 wilayah tubuh + 17 keypoint tubuh, tanpa konten tangan, inkonsistensi internal tabel); nama wifi-densepose-pretrained dicatat sebagai penamaan lini riset, bukan warisan teknis; dikutip sebagai latar pada 3.12 dengan rujukan [35] baru.
- Subbab baru: 3.12 Brief Audit Teknis (Tabel 3.9 artefak terkunci; Tabel 3.10 register AUD-01 sampai AUD-20 berstatus PASS/CONDITIONAL/FAIL/NOT VERIFIED; bukti baris kode; dampak; tiga keputusan baru pada Tabel 3.7) dan 3.13 Rencana Penjaminan Mutu (Tabel 3.11 pemetaan lapisan-gerbang; Tabel 3.12 sampai 3.20 katalog 54 uji berpengenal QA-FW/QA-ACQ/QA-DS/QA-MDL/QA-EVL/QA-SRV/QA-EDGE/QA-SPC/QA-UAT; seluruh status awal belum diuji; ambang berstatus usulan menunggu finalisasi Tabel 3.7 no. 1).
- Rujukan silang ditambahkan (1.6, 2.7, 2.9, 3.8); identitas dan catatan penyusunan diperbarui; DP 33 menjadi 35 entri; tabel konten 13 menjadi 25; subbab H2 34 menjadi 36; H3 8 menjadi 22.
- Berkas pendamping: Register-Audit-Teknis-v21.md (register lengkap + kutipan bukti + tautan) dan SenseSIBI-v21-Audit-QA.xlsx (register, matriks uji 9 kolom yang dapat diisi, traceability kebutuhan-desain-implementasi-uji-bukti, daftar keputusan terbuka, changelog).
- Yang tidak berubah: ruang lingkup 26 huruf SIBI satu tangan (24 statis + J dan Z), arsitektur dua kepala pada encoder beku, guru YOLO26m-Pose, gerbang G0 sampai G4 beserta sub-gerbang G0b, deployment Pilihan 1, arsitektur audio D3, seluruh persamaan bernomor 2.1-2.24 dan 3.1-3.5, jadwal M1-M14, dan seluruh keputusan terbuka lain pada Tabel 3.7 (tidak diputuskan sepihak).

"""
ganti(
    "<!-- ===== AKHIR NASKAH (jangan hapus penanda ini) ===\n",
    "<!-- ===== AKHIR NASKAH (jangan hapus penanda ini) ===\n\n" + LOG,
    "log gelombang 21",
)

OUT.write_text(s, encoding="utf-8")
print(f"\nTotal suntingan berjangkar: {n_edit}")
print(f"Panjang naskah baru: {len(s)} karakter (v20: {len(SRC.read_text(encoding='utf-8'))})")
print(f"Tersimpan: {OUT}")
