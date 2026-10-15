# Pemetaan Fitur RuView → Translasi Bahasa Isyarat (SIBI/BISINDO)

**Sumber:** eksplorasi deep RuView (`01-ruview-exploration/01_EKSPLORASI_DEEP_RUVIEW.md`), verifikasi mandiri `ind_livestock_monitor.rs`, `semantic/` (14 FSM), docs/proof-of-capabilities.md, ADR-018/ADR-079.
**Fungsi dokumen:** dasar penulisan proposal #4 — fitur mana yang boleh dirujuk, mana yang wajib dihindari, apa yang harus diadaptasi.

## 1. Fitur RuView yang RELEVAN dan boleh dirujuk (status jujur)

| Fitur RuView | Fungsi untuk kasus isyarat | Status | Adaptasi yang jujur ditulis di proposal |
|---|---|---|---|
| Capture CSI ESP32 + streaming UDP (ADR-018) | Pengambilan data mentah CSI saat penandatangan bergerak | ✅ MEASURED | Tidak perlu kode baru; node dipasang berhadapan penandatangan |
| Buffer CSI frekuensi tinggi + motion level + motion energy | Segmentasi awal durasi gestur (kapan gerak mulai/berhenti) | ✅ MEASURED | Ambang gerak perlu disetel ulang: gestur = gerak tubuh/tangan 0,5–3 s, jauh lebih besar dari napas |
| Presence heuristik | Deteksi penandatangan masuk zona capture | ✅ MEASURED | FP dari kipas/AC/kepala orang lewat harus jadi item pengujian |
| Kalibrasi 600 frame + enrollment 8 anchor | Kalibrasi per ruang kelas/ruang praktik | ✅ MEASURED | Prosedur tetap dipakai per lokasi edukasi |
| Workflow record → train adaptif | Membangun dataset gestur berlabel per kelas | ✅ MEASURED (untuk presence) | Diadaptasi: rekam N repetisi per gestur (5–12 kelas SIBI/BISINDO terpilih) → pelatihan klasifikator offline/lokal |
| Pipeline DSP (filtering, subcarrier, Doppler) | Ekstraksi fitur amplitudo/fase/Doppler CSI | ✅ MEASURED | Band analisis berpindah dari napas (0,1–0,5 Hz) ke gerak tubuh (≈1–60 Hz komponen Doppler) |
| MQTT → Home Assistant → dashboard/notifikasi | Penyaluran hasil klasifikasi ke guru/pendamping | ✅ MEASURED | Entitas baru semacam "gesture terdeteksi" — desain mirip 21 entitas HA yang ada |
| Pola arsitektur FSM semantik (`semantic/`, 14 file) | Tempat menempel modul klasifikasi gestur sebagai FSM baru | ✅ MEASURED | Contoh preseden arsitektur, bukan janji fitur jadi |
| Privacy mode (strip biometrik) | Etika ruang edukasi anak tunarungu | ✅ MEASURED | Aktifkan; identitas individu tidak terdeteksi dari WiFi (gap 0,0005) = keunggulan etis |
| OTA + multi-node | Deploy 1–2 node di ruang kelas | ✅ MEASURED | Opsional; bukan inti studi kelayakan |

## 2. Fitur RuView yang DILARANG dirujuk sebagai kemampuan

| Fitur | Status nyata | Konsekuensi penulisan |
|---|---|---|
| Pose 17-keypoint (kerangka tangan/tubuh) | ❌ STUB — PCK@20 ≈ 3%, confidence = 0 | Proposal TIDAK boleh menulis "ekstraksi pose tangan". Paradigma yang benar: **klasifikasi gestur langsung dari pola CSI** (preseden SignFi 2018, DF-WiSLR 2020, Widar3.0 2021, FSL-CSI TENCON 2024) |
| Person count akurat | Degradasi >2–3 subjek | Asumsi 1 penandatangan per sesi capture, dinyatakan eksplisit di batasan |
| Penerjemah kontinu (continuous sign language) | Tidak ada | Klaim dibatasi **klasifikasi gestur terisolasi (isolated)** 5–12 kelas; "translasi" diposisikan sebagai cetak biru pengembangan lanjutan |
| Sleep-stage/apnea | Eksperimental tak tervalidasi | Tidak relevan untuk kasus ini; sekadar jangan terseret masuk klaim |

## 3. Perbedaan fisika kasus isyarat vs kasus sebelumnya (pendukung kelayakan)

1. **Sinyal jauh lebih kuat dari napas ayam/manusia.** Gerakan lengan, tangan, dan kepala penandatangan memindahkan massa tubuh bagian atas belasan kilogram — modulasi Doppler CSI berorde puluhan kali lebih besar daripada dada bernapas, dan jauh di atas RCS "very low" unggas 1,5–2,5 kg. Risiko garis ayam (sinyal lemah) praktis hilang di garis ini.
2. **Lingkungan terkendali.** Ruang kelas/ruang praktik edukasi: penandatangan statis di zona, komponen gerak utama hanya penandatangan — lebih bersih daripada kandang (kipas ventilasi) atau asrama (multi subjek).
3. **Tantangan baru yang jujur:** (a) micromotion jari jarang terpisah dari gerak lengan pada CSI ESP32 single-link → pilih gestur yang dominan gerak lengan/tubuh; (b) setiap kelas gestur butuh dataset berlabel — beban pelabelan; (c) cross-person generalization terbatas → model per-sesi atau kalibrasi ulang (preseden Widar3.0 menangani ini dengan domain adaptation — sumber strategi, bukan janji).
4. **SIBI vs BISINDO**: SIBI lebih formal/terstandar (kamus resmi), BISINDO lebih alami dan bervariasi regional → studi kelayakan memilih **subset gestur yang sama artinya pada keduanya** untuk beberapa kelas, dan mendokumentasikan variannya; ini justru nilai riset edukasi (guru SIBI vs komunitas BISINDO).

## 4. Pernyataan disiplin klaim untuk proposal #4 (ikonik, wajib masuk dokumen)

> Penelitian ini merupakan **studi kelayakan** pengenalan gestur terisolasi dari pola Wi-Fi CSI pada platform RuView (capture + DSP + alert). Penelitian ini **tidak** mengklaim: (a) ekstraksi pose atau kerangka tangan; (b) penerjemahan kalimat bahasa isyarat kontinu; (c) pengenalan multi-penandatangan simultan; (d) keakuratan lintas-ruang tanpa kalibrasi ulang. Kelayakan diuji pada subset 5–12 gestur SIBI/BISINDO yang dominan gerak lengan, dengan satu penandatangan per sesi, di ruang edukasi yang terkalibrasi. **Gerbang fisik Delta-CSI 2×ESP32 di lokasi target (minggu awal) tetap menjadi titik go/no-go** — konsisten dengan tiga DPJ sebelumnya.

## 5. Referensi pendukung (sudah terverifikasi DOI di verified_refs.json)

- SignFi — IMWUT 2018, `10.1145/3191755` (CSI → 276 isyarat ASL, bukti paradigma)
- DF-WiSLR — Pervasive and Mobile Computing 2020, `10.1016/j.pmcj.2020.101289`
- Widar3.0 — IEEE TPAMI 2021, `10.1109/tpami.2021.3105387` (cross-domain)
- Filipino SL via Wi-Fi CSI — IEEE TENCON 2024, `10.1109/tencon61640.2024.10903008` (preseden bahasa isyarat nasional non-ASL via CSI)
- ESP32-CSI-Tool — IEEE WoWMoM 2020, `10.1109/wowmom49955.2020.00056` (basis perangkat)
- ACM Computing Surveys 2019, `10.1145/3310194` (survei CSI sensing)
