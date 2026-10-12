# Skripsi — WiFi CSI (Ruang Kerja Konteks)

Repo ini adalah **backup konteks & dokumen kerja** untuk skripsi WiFi CSI (ESP32) agar tidak hilang saat sandbox/reset sesi agent. Dikelola bersama antara mahasiswa dan AI agent.

## Struktur

```
skripsi/
├── README.md                          ← Anda di sini
├── 00-handoff-spec/                   ← Konteks riset yang sudah jalan (jangan diubah, append-only)
│   ├── Handoff_Riset_BISINDO_WiFi_CSI.md     (handoff antar-sesi, 2026-10-12)
│   ├── Spec_Eksekusi_BISINDO_WiFi_CSI_v1.md  (spec eksekusi dari skill to-spec)
│   └── Laporan_Analisis_Referensi_dan_Kritik_Dewan_LLM_Ayam.md
│       (10 referensi terverifikasi + verdict dewan LLM garis ayam)
├── 01-ruview-exploration/             ← Hasil eksplorasi repo RuView (2026-10-12)
│   ├── 01_EKSPLORASI_DEEP_RUVIEW.md   ← Deep-dive: fitur nyata vs stub, arsitektur,
│   │                                     keterbatasan fisika ayam, cheat-sheet path
│   └── 02_PEMETAAN_FITUR_3_ALAT.md    ← Pemetaan fitur RuView → 3 opsi judul
│                                         (ayam broiler / kelas SLB / asrama SLB)
├── 02-skills-arsip/                   ← Arsip skill untuk restore sesi agent
│   ├── academicResearchSkill.zip      (academic-research v3)
│   └── mattpocock-skills.zip          (mattpocock skills-main, 31 skill)
└── worklog.md                         ← Log kerja append-only semua agent
```

## Ringkasan Keadaan (agar agent sesi berikutnya cepat nyambung)

- **2 garis riset:** (1) WiFi CSI ayam broiler — riset/kritik SELESAI, verdict: reformulasi ke level kawanan, uji Delta-CSI = gerbang minggu-1; (2) sensing manusia tanpa kamera via RuView (sebelumnya BISINDO; sekarang berevolusi ke konteks SLB).
- **3 opsi alat yang dieksplorasi:** ayam broiler · ruang kelas SLB · kamar asrama SLB. Pemetaan fitur & kandidat judul masing-masing ada di `01-ruview-exploration/02_PEMETAAN_FITUR_3_ALAT.md`.
- **RuView (github.com/ruvnet/RuView):** platform WiFi CSI ESP32 open-source. Yang NYATA: capture CSI, presence, motion, napas/jantung manusia (band hardcoded!), fall, kalibrasi ruangan, record→train adaptif, MQTT/HA, dashboard. Yang STUB: pose 17-keypoint (PCK@20 3%, confidence=0), person count lemah, sleep-stage/apnea tak tervalidasi. Jantung ayam (250–330 BPM) di luar band filter → detak jantung unggas mustahil tanpa ubah kode.
- **Langkah murah berikutnya:** cek kebaruan Scopus/DBLP (classroom/SLB/CSI) + uji Delta-CSI 2×ESP32 di lokasi target.

## Aturan repo

1. `worklog.md` append-only — setiap sesi agent menambah bagian baru, tidak mengubah riwayat.
2. Dokumen di `00-handoff-spec/` adalah rekam sejarah — revisi = file baru, bukan edit.
3. Kredensial tidak boleh masuk repo. (Token GitHub dipakai lewat remote URL sesi, tidak ditulis di file.)
4. Bahasa kerja: Indonesia.
