#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Revisi terarah v18 -> v19 (gelombang 19): koreksi mekanisme akuisisi CSI RuView.

Dasar: telaah pemilik 14 Nov 2026 — ESP-NOW tercampur dengan mekanisme Wi-Fi
sounding untuk CSI. Tiga mekanisme firmware RuView dipisahkan:
  1) sensing  : injeksi NDP (Null Data Packet) + callback CSI;
  2) transport: UDP, bingkai CSI terserialisasi format biner ADR-018;
  3) ESP-NOW  : hanya sinkronisasi mesh opsional, bukan jalur CSI, bukan prasyarat.
Seluruh klaim mekanisme telah diverifikasi langsung ke repositori RuView lokal
(firmware/esp32-csi-node/README.md dan docs/user-guide.md) pada 14 Nov 2026:
  - arsitektur firmware: WiFi STA + CSI callback, channel hopping, NDP injection,
    TDM slot management, DSP lokal, UDP sender (README "Firmware Architecture");
  - UDP target default 5005, format ADR-018, magic 0xC5110001 (README);
  - ESP-NOW tidak muncul di README firmware; di user guide hanya sebagai
    "optional sync object" pada mesh + rilis historis v0.7.0;
  - mesh multistatik 3-6 node, tiap node TX sekaligus RX, protokol TDM (user guide);
  - mode promiscuous memang disyaratkan callback CSI (troubleshooting README),
    sehingga kata "promiscuous" tetap sahih dan dipertahankan pada konteks callback;
  - WIFI_PS_NONE (modem sleep dimatikan) disyaratkan CSI kontinu; hop_count=1
    mendukung mode satu kanal;
  - injeksi NDP = esp_wifi_80211_tx() bingkai 24 byte (csi_collector.c) — node TX
    memancarkan bingkai sounding;
  - peringatan akurasi: "accuracy is still synthetic until real-data validation",
    PCK@20 2,5% dengan fase evaluasi masih tertunda (README utama) — keberhasilan
    instalasi + terkirimnya CSI != bukti akurasi sensing.

Kaidah bahasa: skill sempro-mepet (jika bukan bila, tanpa em dash prosa baru,
tanpa koma-sebelum-sehingga baru, signifikan hanya bersama uji statistik).
Semua suntingan berjangkar; setiap jangkar wajib ditemukan tepat 1 kali.
"""
from pathlib import Path

SRC = Path("/home/z/my-project/download/sensesibi-v10/Proposal-SenseSIBI-v18.md")
DST = Path("/home/z/my-project/download/sensesibi-v10/Proposal-SenseSIBI-v19.md")

s = SRC.read_text(encoding="utf-8")
log = []

def ganti(nama, lama, baru, n=1):
    global s
    hitung = s.count(lama)
    assert hitung == n, f"[{nama}] jangkar ditemukan {hitung}x (harusnya {n})"
    s = s.replace(lama, baru)
    log.append(nama)

# ============================================================
# E01 — Identitas sampul: ringkasan gelombang 19
# ============================================================
ganti("E01-jenis-dokumen",
"| Jenis dokumen | Proposal penelitian (seminar proposal), BAB I sampai III + Daftar Pustaka; revisi verifikasi sumber primer atas v17: audit artefak *encoder* (NUL-padding, keluarga csi-embed-v2, lupa EWC 32,97%, batasan SISO), himpunan *subcarrier* valid (LLTF/HT-LTF, `first_word_invalid`), formalisasi Jalur A/B1/B2 dan Pembanding C, mask efektif serta uji permutasi G0b, TTS MMS-TTS-ind sebagai kandidat utama operasional, latensi terpisah per arah, tata kelola data etik; 31 rujukan |",
"| Jenis dokumen | Proposal penelitian (seminar proposal), BAB I sampai III + Daftar Pustaka; revisi koreksi mekanisme akuisisi CSI atas v18: tiga mekanisme *firmware* RuView dipisahkan (*sounding* NDP dengan *callback* CSI, transport UDP ADR-018, ESP-NOW hanya sinkronisasi *mesh* opsional), versi *firmware* dikunci dan konfigurasi dua node diverifikasi pada G0; 33 rujukan |")

# ============================================================
# E02 — Catatan penyusunan
# ============================================================
ganti("E02-catatan",
"> Catatan penyusunan: versi ini menyunting naskah v17 sebagai revisi terarah atas paket perbaikan yang seluruh klaim eksternalnya telah diverifikasi langsung ke sumber primer pada 14 November 2026; tidak ada bab yang ditulis ulang dan ruang lingkup sistem tidak berubah. Temuan verifikasi dimasukkan sebagai bukti: audit artefak *encoder* (NUL-padding `model.safetensors`, keluarga `csi-embed-v2` dengan *standardizer* FP16, tingkat lupa EWC 32,97%, peringatan SISO), struktur *subcarrier* ESP32-S3 (52 LLTF atau 56 HT-LTF serta penanganan `first_word_invalid`), ketiadaan suara Indonesia pada Kokoro-82M v1.0 (sehingga MMS-TTS-ind menjadi kandidat utama operasional TTS), dan konteks tolok ukur ESP-DL 69,2 ms. Perbaikan metodologis meliputi: formalisasi Jalur A, Jalur B1/B2, dan Pembanding C; mask efektif gabungan (Persamaan 2.13a); uji permutasi G0b; koreksi tafsir *overlap* jendela 75% dan rentang T = 16; pemisahan latensi Arah 1 dan Arah 2 (Persamaan 3.3a dan 3.3b); segmentasi tiga fase (onset, tahan pose, lintasan dinamis); penghapusan rumus 1 − WER; pelaporan cakupan diterima dan akurasi selektif; penguatan etika (retensi video, persetujuan wali dan *assent*); serta rujukan TKT nasional Permenristekdikti No. 42/2016. Tiga rujukan baru ditambahkan, yaitu DF-WiSLR, Wi-SignFi, dan Permenristekdikti Nomor 42 Tahun 2016; nomor sitasi lama 1 sampai 28 dipertahankan tanpa penomoran ulang. Sembilan keputusan terbuka tetap dicatat pada Tabel 3.7 dan tidak diputuskan sepihak; rincian perubahan per subbab ada pada Log Perubahan gelombang 18 di ujung naskah.",
"> Catatan penyusunan: versi ini menyunting naskah v18 sebagai revisi terarah atas koreksi pemilik mengenai mekanisme akuisisi CSI RuView; tidak ada bab yang ditulis ulang dan ruang lingkup sistem tidak berubah. Tiga mekanisme yang selama ini tercampur dipisahkan: jalur penginderaan memakai injeksi NDP dan *callback* CSI, jalur pengangkutan memakai UDP dengan format biner ADR-018, dan ESP-NOW hanya menjadi jalur sinkronisasi *mesh* opsional, bukan prasyarat akuisisi CSI. ESP-NOW karenanya dikeluarkan dari arsitektur inti dan tetap tercatat sebagai fitur sinkronisasi yang diuji hanya jika konfigurasi *mesh* memerlukannya. Gerbang G0 kini mewajibkan penguncian versi atau komit *firmware* RuView, verifikasi konfigurasi dua node dengan peran tetap tanpa implementasi ESP-NOW tambahan, serta uji kestabilan CSI mentah saat *sounding* dan UDP berjalan bersamaan; keberhasilan instalasi dan terkirimnya bingkai CSI tidak diperlakukan sebagai bukti akurasi penginderaan maupun kestabilan jangka panjang. Dua rujukan baru ditambahkan, yaitu dokumentasi *firmware* CSI RuView dan panduan penggunaannya; nomor sitasi lama 1 sampai 31 dipertahankan tanpa penomoran ulang. Keputusan terbuka pada Tabel 3.7 tetap tidak diputuskan sepihak; rincian perubahan per subbab ada pada Log Perubahan gelombang 19 di ujung naskah.")

# ============================================================
# E03/E04 — Tabel 2.1: baris firmware dan baris mekanisme radio
# ============================================================
ganti("E03-tabel21-baris-firmware",
"| *Firmware* penangkap CSI (UDP) | Mengalirkan CSI dan label ke server |",
"| *Firmware* penangkap CSI (UDP, format ADR-018) | Mengalirkan bingkai CSI mentah saat akuisisi serta label dan skor sebagai telemetri saat *deployment* |")

ganti("E04-tabel21-baris-mekanisme",
"| Station + UDP + CSI *promiscuous* + ESP-NOW pada satu *chip* | Dasar topologi satu kanal (Subbab 3.5) |",
"| *Station* Wi-Fi + *callback* CSI + injeksi NDP + UDP pada satu *chip*; ESP-NOW hanya sinkronisasi *mesh* opsional | Dasar topologi satu kanal (Subbab 3.5) |")

# ============================================================
# E05 — 2.3 paragraf koeksistensi -> dua paragraf pemisahan mekanisme
# ============================================================
ganti("E05-2.3-paragraf",
"Fakta paling menentukan justru koeksistensi radio pada satu *chip*. *Firmware* RuView mampu menangkap CSI sambil memelihara koneksi *station* UDP serta sinkronisasi ESP-NOW secara serentak. Dua syaratnya: seluruh perangkat berada pada satu kanal dan mode hemat daya dimatikan [10]. Purwarupa karenanya tidak memerlukan modul gerbang khusus, tetapi ada satu catatan penting: RuView belum melalui telaah sejawat, jadi fungsinya diverifikasi sendiri pada gerbang G0.",
"""Peran tiga mekanisme radio pada *firmware* RuView dibedakan agar fungsinya tidak tertukar [32], [33]. Jalur penginderaan memakai injeksi NDP (*Null Data Packet*) beserta *callback* CSI: node pemancar menyuntikkan bingkai *sounding* Wi-Fi, lalu node penerima menangkap CSI dari bingkai tersebut. Jalur pengangkutan memakai UDP dengan format biner ADR-018 [32]. Adapun ESP-NOW bukan jalur pengiriman bingkai CSI; protokol itu hanya muncul sebagai sinkronisasi *mesh* opsional pada implementasi tertentu [33]. Purwarupa satu tautan dengan satu penerima karenanya tidak menjadikan ESP-NOW prasyarat akuisisi CSI, sedangkan sinkronisasi kamera dan CSI ditangani terpisah lewat penanda waktu (Subbab 3.6).

Koeksistensi radio pada satu *chip* tetap menjadi fakta yang menentukan: *firmware* menangkap CSI sambil memelihara koneksi *station* UDP. Dua syaratnya ialah seluruh perangkat berada pada satu kanal serta mode hemat daya dimatikan [10], [32]; purwarupa karenanya tidak memerlukan modul gerbang khusus. Dua catatan verifikasi tetap menyertai pemakaian *framework* ini. Pertama, dokumentasi RuView menggambarkan konfigurasi *mesh* multistatik dengan tiga sampai enam node yang masing-masing berperan sebagai pemancar sekaligus penerima dan bergiliran memancar melalui pengaturan TDM [33], sedangkan purwarupa memakai dua node dengan peran tetap; kesesuaian konfigurasi dua node itu karenanya diverifikasi langsung pada *firmware* yang dipakai. Kedua, keberhasilan instalasi dan terkirimnya bingkai CSI belum membuktikan akurasi penginderaan maupun kestabilan jangka panjang [33], jadi keduanya tetap dibuktikan lewat pengujian sendiri. Status RuView yang belum melalui telaah sejawat memperkuat perlunya verifikasi tersebut. Pada gerbang G0, verifikasi *firmware* menjadi pekerjaan wajib: versi atau komit *firmware* dikunci dan dicatat, konfigurasi dua node dijalankan tanpa implementasi ESP-NOW tambahan, dan kestabilan CSI mentah diuji saat *sounding* dan UDP berjalan bersamaan (Tabel 3.5).""")

# ============================================================
# E06 — 2.13: kalimat sinkronisasi ESP-NOW diluruskan
# ============================================================
ganti("E06-2.13-sinkronisasi",
"Sinkronisasi antarmodul memakai ESP-NOW, sedangkan aliran data ke server memakai UDP [10].",
"Aliran bingkai CSI dari node penerima ke server memakai UDP [10], sedangkan sinkronisasi antara kamera dan CSI ditangani lewat penanda waktu yang diuji terpisah (Subbab 3.6); ESP-NOW tidak menjadi prasyarat akuisisi CSI dan hanya dipakai sebagai jalur sinkronisasi *mesh* opsional jika konfigurasi node memerlukannya [33].")

# ============================================================
# E07 — 3.4: peran TX/RX + penguncian versi firmware
# ============================================================
ganti("E07a-3.4-peran-txrx",
"TX memancarkan *beacon* ESP-NOW, sedangkan RX mengekstrak CSI 56 *subcarrier* pada 2,4 GHz kanal 20 MHz sekaligus memuat antarmuka.",
"TX menyuntikkan bingkai *sounding* NDP, sedangkan RX menangkap CSI 56 *subcarrier* pada 2,4 GHz kanal 20 MHz melalui *callback* CSI sekaligus memuat antarmuka.")

ganti("E07b-3.4-versi-perangkat-lunak",
"Supaya eksperimen bisa diulang, versi perangkat lunak dicatat bersama log pelatihan.",
"Supaya eksperimen bisa diulang, versi atau komit *firmware* RuView serta perangkat lunak lain dicatat bersama log pelatihan.")

# ============================================================
# E08 — Tabel 3.1 baris 1: keterangan node TX
# ============================================================
ganti("E08-tabel31-baris1",
"| 2 unit | Node TX (pemancar *beacon*) dan node RX (penerima CSI dan antarmuka) |",
"| 2 unit | Node TX (pemancar bingkai *sounding* NDP) dan node RX (penerima CSI dan antarmuka) |")

# ============================================================
# E09 — 3.5 prosa arah pertama
# ============================================================
ganti("E09-3.5-arah-pertama",
"Pada arah pertama, *beacon* ESP-NOW node pemancar melintasi zona isyarat, gerak pengisyarat mengubah deret CSI yang ditangkap node penerima, dan model berkepala klasifikasi yang terkuantisasi dijalankan langsung di modul menghasilkan label beserta skor keyakinan.",
"Pada arah pertama, bingkai *sounding* NDP yang disuntikkan node pemancar melintasi zona isyarat, gerak pengisyarat mengubah deret CSI yang ditangkap node penerima, dan model berkepala klasifikasi yang terkuantisasi dijalankan langsung di modul menghasilkan label beserta skor keyakinan.")

# ============================================================
# E10 — Gambar 3.3 accDescr
# ============================================================
ganti("E10-g33-accdescr",
"Arah 1 mengalir dari beacon ESP-NOW melalui zona isyarat ke node RX yang menjalankan model klasifikasi terkuantisasi Pilihan 1;",
"Arah 1 mengalir dari bingkai sounding NDP node TX melalui zona isyarat ke node RX yang menjalankan model klasifikasi terkuantisasi Pilihan 1;")

# ============================================================
# E11 — Gambar 3.3 simpul TX
# ============================================================
ganti("E11-g33-simpul-tx",
'    TX["Node TX: beacon ESP-NOW"]',
'    TX["Node TX: injeksi NDP"]')

# ============================================================
# E12 — 3.5 paragraf topologi
# ============================================================
ganti("E12-3.5-topologi",
"Node pemancar memancarkan *beacon* sebagai sumber bingkai CSI, sedangkan node penerima mengirim bingkai, label, dan skor melalui UDP kepada server Rust sebagai telemetri riset.",
"Node pemancar menyuntikkan bingkai *sounding* NDP sebagai sumber bingkai CSI, sedangkan node penerima mengirim bingkai CSI mentah saat akuisisi serta label dan skor saat *deployment* melalui UDP kepada server Rust sebagai telemetri riset.")

# ============================================================
# E13 — 3.7 prosa inferensi: bingkai promiscuous -> hasil callback CSI
# ============================================================
ganti("E13-3.7-bingkai-promiscuous",
"Bingkai *promiscuous* masuk ke penyangga geser, segmen terdeteksi dari energi gerak, dan masukan *encoder* disiapkan sesuai hasil audit.",
"Bingkai hasil *callback* CSI masuk ke penyangga geser, segmen terdeteksi dari energi gerak, dan masukan *encoder* disiapkan sesuai hasil audit.")

# ============================================================
# E14 — Gambar 3.5 accDescr
# ============================================================
ganti("E14-g35-accdescr",
"Bingkai promiscuous masuk ke penyangga geser di PSRAM dengan pemeriksaan subcarrier valid dan first_word_invalid",
"Bingkai hasil callback CSI masuk ke penyangga geser di PSRAM dengan pemeriksaan subcarrier valid dan first_word_invalid")

# ============================================================
# E15 — Gambar 3.1 accDescr: T0 menambah penguncian versi firmware
# ============================================================
ganti("E15-g31-accdescr",
"T0 replikasi platform, audit subcarrier valid dan first_word_invalid, uji Delta-CSI, koeksistensi audio-CSI, audit artefak RuView",
"T0 replikasi platform, penguncian versi firmware RuView, audit subcarrier valid dan first_word_invalid, uji Delta-CSI, koeksistensi audio-CSI, audit artefak RuView")

# ============================================================
# E16 — Batasan no. 12 baru
# ============================================================
ganti("E16-batasan-12",
"11. Seluruh hasil dilaporkan sebagai bukti awal pada populasi terbatas, yaitu 3–4 pengisyarat, sedikitnya dua ruang, dan satu konfigurasi perangkat; skema *leave-one-subject-out*, pengguna baru, dan *leave-one-room-out* dibaca sebagai indikasi ketahanan awal, bukan bukti generalisasi populasi; klaim lintas populasi tidak dibuat.",
"""11. Seluruh hasil dilaporkan sebagai bukti awal pada populasi terbatas, yaitu 3–4 pengisyarat, sedikitnya dua ruang, dan satu konfigurasi perangkat; skema *leave-one-subject-out*, pengguna baru, dan *leave-one-room-out* dibaca sebagai indikasi ketahanan awal, bukan bukti generalisasi populasi; klaim lintas populasi tidak dibuat.
12. Akuisisi CSI mengikuti mekanisme bawaan *firmware* RuView, yaitu injeksi NDP, *callback* CSI, dan transport UDP dengan format ADR-018; mekanisme radio tidak dibangun ulang, ESP-NOW tidak dijadikan prasyarat, dan sinkronisasi *mesh* hanya diuji jika konfigurasi node memerlukannya.""")

# ============================================================
# E17 — Tabel 3.5 baris G0: kriteria verifikasi firmware
# ============================================================
ganti("E17-tabel35-g0",
"Akuisisi *subcarrier* valid N~valid~ (LLTF/HT-LTF, *pilot*, `first_word_invalid` diaudit) pada jarak 1 m ke UDP Rust terbaca stabil; laju sekurang-kurangnya 25 bingkai per detik;",
"Versi atau komit *firmware* RuView dikunci dan tercatat; konfigurasi dua node peran tetap terverifikasi berjalan tanpa implementasi ESP-NOW tambahan; akuisisi *subcarrier* valid N~valid~ (LLTF/HT-LTF, *pilot*, `first_word_invalid` diaudit) pada jarak 1 m ke UDP Rust terbaca stabil saat injeksi NDP dan pengiriman UDP berjalan bersamaan; laju sekurang-kurangnya 25 bingkai per detik;")

# ============================================================
# E18 — 3.10 kalimat pengelompokan Tabel 3.7 memuat baris 21
# ============================================================
ganti("E18-3.10-pengelompokan",
"baris 1, 13, 14, 16, 17, 19, dan 20 merupakan keputusan desain dan administratif inti yang memerlukan konfirmasi pembimbing, sedangkan baris 2 sampai 12, 15, dan 18 merupakan parameter teknis",
"baris 1, 13, 14, 16, 17, 19, dan 20 merupakan keputusan desain dan administratif inti yang memerlukan konfirmasi pembimbing, sedangkan baris 2 sampai 12, 15, 18, dan 21 merupakan parameter teknis")

# ============================================================
# E19 — Tabel 3.7 baris 21: keputusan peran ESP-NOW
# ============================================================
ganti("E19-tabel37-baris21",
"| 20 | Akhiran judul (PEMROSESAN SERVER atau CLOUD PROCESSING) | Kesesuaian dengan arsitektur aktual yang berpusat di server | [PERLU DATA: keputusan akhiran judul bersama pembimbing] |",
"""| 20 | Akhiran judul (PEMROSESAN SERVER atau CLOUD PROCESSING) | Kesesuaian dengan arsitektur aktual yang berpusat di server | [PERLU DATA: keputusan akhiran judul bersama pembimbing] |
| 21 | Peran ESP-NOW dan konfigurasi node akuisisi CSI (ESP-NOW dikeluarkan dari jalur inti; dua node peran tetap diverifikasi tanpa implementasi ESP-NOW tambahan; sinkronisasi *mesh* hanya jika diperlukan) | Keputusan pemilik 14 Nov 2026 atas audit dokumentasi *firmware* RuView [32], [33] | Ditetapkan; ESP-NOW diaktifkan kembali hanya jika konfigurasi *mesh* TDM memerlukannya dan penggunaannya dilaporkan |""")

# ============================================================
# E20 — Tabel 3.8 baris 13: risiko konfigurasi dua node
# ============================================================
ganti("E20-tabel38-baris13",
"| 12 | Huruf sangat mirip tak terpisahkan CSI | Himpunan kelas menyempit | Pangkas himpunan pada G1 sesuai Tabel 3.7; laporkan pasangan gagal |",
"""| 12 | Huruf sangat mirip tak terpisahkan CSI | Himpunan kelas menyempit | Pangkas himpunan pada G1 sesuai Tabel 3.7; laporkan pasangan gagal |
| 13 | Konfigurasi dua node peran tetap tidak terverifikasi pada *firmware* RuView yang dipakai; dokumentasi standarnya memakai *mesh* multistatik 3–6 node dengan TDM [33] | G0 tidak dapat dinilai atau CSI tidak stabil | Kunci versi atau komit *firmware*, uji dua node tanpa ESP-NOW tambahan pada perangkat nyata; jika bermasalah, ikuti konfigurasi node pada dokumentasi *firmware* termasuk pengaturan TDM, lalu laporkan sebagai penyimpangan rancangan yang disengaja |""")

# ============================================================
# E21 — Daftar Pustaka: [32] firmware README + [33] user guide
# ============================================================
ganti("E21-dp-32-33",
"https://peraturan.bpk.go.id/Details/140468/permenristekdikti-no-42-tahun-2016, diakses 14 Nov. 2026.",
"""https://peraturan.bpk.go.id/Details/140468/permenristekdikti-no-42-tahun-2016, diakses 14 Nov. 2026.

[32] ruvnet, "ESP32 CSI Node Firmware," README *firmware* RuView, repositori GitHub. [Online]. Available: https://github.com/ruvnet/RuView/blob/main/firmware/esp32-csi-node/README.md, diakses 14 Nov. 2026.

[33] ruvnet, "RuView User Guide," panduan pengguna RuView, repositori GitHub. [Online]. Available: https://github.com/ruvnet/RuView/blob/main/docs/user-guide.md, diakses 14 Nov. 2026.""")

# ============================================================
# E22 — Log Perubahan gelombang 19
# ============================================================
ganti("E22-log-gelombang-19",
"<!-- ===== AKHIR NASKAH (jangan hapus penanda ini) ===\n\n## Log Perubahan — Revisi 14 November 2026, gelombang 18",
"""<!-- ===== AKHIR NASKAH (jangan hapus penanda ini) ===

## Log Perubahan — Revisi 14 November 2026, gelombang 19 (koreksi mekanisme akuisisi CSI RuView: NDP, UDP ADR-018, peran ESP-NOW)

Permintaan: memperbaiki pencampuran ESP-NOW dengan mekanisme *sounding* Wi-Fi pada naskah v18 sesuai telaah pemilik atas dokumentasi RuView; seluruh klaim mekanisme diverifikasi langsung ke repositori RuView (README *firmware* esp32-csi-node dan panduan pengguna) pada 14 November 2026; kaidah bahasa mengikuti skill sempro-mepet; nomor sitasi [1] sampai [31] dipertahankan dengan dua rujukan baru [32] README *firmware* CSI dan [33] panduan pengguna RuView; keputusan terbuka tidak diputuskan sepihak.

- Mekanisme dipisahkan pada 2.3: jalur penginderaan memakai injeksi NDP dan *callback* CSI; jalur pengangkutan memakai UDP dengan format biner ADR-018; ESP-NOW hanya sinkronisasi *mesh* opsional, bukan jalur pengiriman bingkai CSI dan bukan prasyarat akuisisi; sinkronisasi kamera dan CSI tetap lewat penanda waktu (2.13, Subbab 3.6).
- ESP-NOW dikeluarkan dari arsitektur inti: Tabel 2.1 baris 2, kalimat *beacon* ESP-NOW pada 3.4 dan 3.5, Tabel 3.1 baris 1, topologi 3.5, serta simpul TX dan accDescr Gambar 3.3 diganti ke bingkai *sounding* NDP; frasa "bingkai *promiscuous*" pada 3.7 dan Gambar 3.5 diluruskan menjadi bingkai hasil *callback* CSI (mode *promiscuous* tetap sahih sebagai syarat *callback* CSI pada ESP-IDF menurut dokumentasi *firmware*); Batasan no. 12 baru menegaskan mekanisme radio tidak dibangun ulang.
- Gerbang G0 diperkuat (Tabel 3.5, Gambar 3.1, 2.3, 3.4): versi atau komit *firmware* RuView dikunci dan dicatat; konfigurasi dua node peran tetap diverifikasi tanpa implementasi ESP-NOW tambahan; kestabilan CSI mentah diuji saat injeksi NDP dan UDP berjalan bersamaan.
- Catatan kehati-hatian ditambah: dokumentasi RuView memakai *mesh* multistatik 3–6 node dengan TDM sehingga konfigurasi dua node peran tetap perlu verifikasi pada *firmware* yang dipakai; keberhasilan instalasi dan terkirimnya bingkai CSI belum membuktikan akurasi penginderaan maupun kestabilan jangka panjang (2.3, Tabel 3.8 no. 13 baru).
- Keputusan dicatat: Tabel 3.7 no. 21 (peran ESP-NOW: dikeluarkan dari jalur inti, diaktifkan kembali hanya jika konfigurasi *mesh* TDM memerlukannya) masuk kelompok parameter teknis berbasis audit; identitas sampul dan catatan penyusunan diperbarui.
- Yang tidak berubah: arsitektur dua arah, gerbang G0b sampai G4, jadwal M1–M14, seluruh persamaan bernomor, batasan no. 1 sampai 11, seluruh angka pra-penelitian, dan penanda [PERLU DATA]/[PERLU VALIDASI]/[PERLU KONFIRMASI].

## Log Perubahan — Revisi 14 November 2026, gelombang 18""")

# ============================================================
# Pemeriksaan pasca-sunting (hanya tubuh naskah; area Log boleh
# mengutip istilah lama sebagai catatan historis)
# ============================================================
tubuh = s[:s.index("<!-- ===== AKHIR NASKAH")]
assert "beacon" not in tubuh.lower(), "sisa kata beacon di tubuh naskah"
assert tubuh.count("ESP-NOW") >= 6, "ESP-NOW hilang seluruhnya (harusnya tersisa sebagai fitur opsional)"
masalah = ["beacon ESP-NOW", "sinkronisasi ESP-NOW secara serentak", "memancarkan *beacon*", "beacon sinkronisasi antarnode"]
for frasa in masalah:
    assert frasa not in tubuh, f"frasa bermasalah tersisa: {frasa}"
assert "[32]" in tubuh and "[33]" in tubuh, "sitasi baru tidak masuk tubuh naskah"
assert tubuh.count("[32]") >= 1 and tubuh.count("[33]") >= 2, "sitasi [32]/[33] belum tersebar"
# kaidah bahasa prosa baru (kata "bila" berdiri sendiri, bukan substring "apabila"/"sembilan")
paragraf_baru = s[s.index("Peran tiga mekanisme radio"):s.index("## 2.4")]
import re
assert not re.search(r"\bbila\b", paragraf_baru), "konjungsi bila dipakai"
assert "—" not in paragraf_baru, "em dash prosa baru"
assert ", sehingga" not in paragraf_baru, "koma-sebelum-sehingga baru"
assert not re.search(r"\bhal ini\b|\byang mana\b", paragraf_baru), "pola AI tersisa"

DST.write_text(s, encoding="utf-8")
print(f"revisi_g19 selesai: {len(log)} suntingan -> {DST.name}")
for nama in log:
    print(" -", nama)
