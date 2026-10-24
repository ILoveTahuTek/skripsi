# HANDOFF — Riset Judul Skripsi WiFi CSI → BISINDO

**Untuk:** Agent/sesi berikutnya · **Dibuat:** 2026-10-12 · **Oleh:** sesi web (skill `handoff`)
**Fokus sesi berikutnya (inferred):** finalisasi keputusan topik oleh user, lalu persiapan uji kelayakan fisik & proposal skripsi.

---

## 1. Keadaan Lingkungan (PENTING — baca dulu)

- **Environment reset terjadi antara 23–24 Sep.** Seluruh skill hasil instalasi user (167+1: cursor-*, taste pack, llm-council, gepa, academic-research, dsb.) HILANG; hanya 69 skill bawaan yang tersisa.
- Sudah dipulihkan dari arsip `upload/`: **paket mattpocock skills-main terbaru (31 skill: engineering/productivity/misc, termasuk `handoff` & `to-spec`)** + **academic-research v3.3.0**. Total sekarang **101 skill**.
- `gdown` perlu diinstal ulang (`uv pip install gdown`) setiap sesi baru untuk unduh Google Drive.
- Arsip zip yang masih ada di `upload/` (alphaear, archify, autoresearch, book-to-skil, cursor-pstack-skills, gepa, last30days, llm-council, stop-slop, taste-skill-skills, ui-ux-pro-max) **belum** dipulihkan — lakukan bila user minta.

## 2. Konteks Proyek (dua garis kerja)

1. **Skripsi WiFi CSI ayam** (selesai riset/kritik): 10 referensi terverifikasi + sidang dewan LLM; verdict: reformulasi ke level kawanan; deliverable docx/pdf di `download/Analisis_Referensi_WiFi_CSI.docx|pdf`. User belum konfirmasi arah skripsi ini — tampak beralih ke ide baru (garis 2).
2. **Ide baru (AKTIF):** visualisasi WiFi CSI via repo **RuView** (github.com/ruvnet/RuView) untuk membaca bahasa isyarat/postur/komunikasi visual "lebih efisien dari kamera". Sudah diriset penuh dengan skill `academic-research` (route: field → gap-audit → topic-arena → question-design). **Laporan final sudah disampaikan ke user di chat.**

## 3. Hasil Riset RuView (ringkas — detail di artifacts, JANGAN diulang)

- **Verdict 3 koreksi premis:** (1) modality WiFi→bahasa isyarat BUKAN baru (SignFi, ACM IMWUT 2018, doi:10.1145/3191755; WiSign 2020; DF-WiSLR 2020; WiASL 2023); (2) pose on-device RuView = **stub** (PCK@20 3,0% vs target 35%, runtime `confidence=0`; CSI SISO 1-antena tak memuat artikulasi halus — issue #509) — yang terukur hanya presence/napas/HR/fall/counting; (3) "lebih efisien dari kamera" harus DIUKUR (RQ3), bukan diasumsikan.
- **Gap hidup:** GAP-1 BISINDO×WiFi-CSI belum ada di mana pun (semua karya BISINDO berbasis kamera; tetangga terdekat: dataset word-level WiFi-CSI Bahasa Isyarat Bangladesh); GAP-2 ADR-079 RuView (baseline pose on-device ≥35%); GAP-3 benchmark kamera-vs-WiFi di edge (lemah).
- **Rekomendasi arena topik: T1** (studi kelayakan kosakata inti BISINDO via CSI ESP32 + dataset percontohan) **+ graft T4** (validasi instrumen RuView sebagai go/no-go minggu 1–2) **+ graft T3** (perbandingan empiris kamera sebagai bab evaluasi). T2 (pose baseline) = future work. **User BELUM memilih** — keputusan human-owned.
- **3 RQ** sudah dirumuskan (kontras CSI; akurasi top-1/top-3 dgn split blok-waktu & antar-penandatangan; tabel akurasi-latensi-energi-biaya-privasi vs kamera). 3 kandidat judul tersedia di laporan.
- Spec eksekusi sudah dibuat dengan skill `to-spec`: `download/Spec_Eksekusi_BISINDO_WiFi_CSI_v1.md`.

## 4. Artifacts (referensi — jangan duplikasi)

| Artefak | Path |
|---|---|
| Research state resumable | `research/ruview_judul/research_state.yaml` |
| Decision trail | `research/ruview_judul/decision_log.tsv` |
| 17 bukti pencarian JSON | `research/ruview_judul/search_results/` |
| Verifikasi 13 DOI (Crossref/arXiv) | `research/ruview_judul/verify_refs.json` |
| Snapshot README RuView | `/tmp/ruview_readme.md` (sementara — re-fetch bila perlu) |
| Skrip search & verify | `scripts/search_swarm_ruview.mjs`, `scripts/verify_ruview_refs.py` |
| Laporan skripsi ayam (docx/pdf) | `download/Analisis_Referensi_WiFi_CSI.docx|pdf` |
| Worklog lengkap semua task | `worklog.md` |

## 5. Langkah Berikutnya (urutan)

1. **User memilih topik** (rekomendasi: T1-graft). Jangan ditawari pertanyaan berulang — cukup konfirmasi sekali.
2. Jika T1: jalankan protokol uji kontras 5 kata BISINDO (MAKAN, MINUM, TIDAK, AKU, KAMU — pending konfirmasi komunitas) vs kondisi diam, 2 ESP32 — go/no-go minggu ini; uji fisik dulu sebelum menulis pipeline.
3. Cek Scopus/DBLP + literatur Mandarin untuk memastikan BISINDO-CSI benar kosong SEBELUM klaim "pertama" ditulis di proposal (anti-pattern: gap-on-low-yield).
4. Kontak komunitas Tuli (Gerkatin/PGBISINDO): pemilihan kosakata, BISINDO vs SIBI, etika/persetujuan — keputusan human-owned, bukan agent.
5. Bila user setuju: pecah spec jadi tiket dengan `to-tickets`, atau langsung eksekusi protokol.

## 6. Suggested Skills (panggil via Skill tool di sesi berikutnya)

- `academic-research` — resume riset dari checkpoint (`recall` route; baca dulu `research_state.yaml`)
- `to-tickets` — pecah spec menjadi tiket terurut bila user ingin eksekusi terstruktur
- `implement` / `tdd` — bila masuk fase kode (capture CSI, pipeline, analisis)
- `literature-survey` — bila bab 2 tinjauan pustaka perlu digarisbesarkan dari 13 referensi terverifikasi
- `docx` / `pdf` — bila proposal/laporan perlu dikemas jadi dokumen (user pernah gagal unduh docx ber-nama panjang → pakai nama file pendek)
- `interrogate` (dari academic-research) — bila user ingin stress-test keputusan topik lagi

## 7. Redaksi & Batasan

- Tidak ada kredensial/API key dalam konteks ini. Link Google Drive user boleh disimpan di `upload/`.
- Bahasa kerja: **Indonesia**. Semua klaim kebaruan harus berlabel evidence-state (VERIFIED/SUPPORTED/SEARCH-LIMITED) sesuai disiplin `academic-research`.
- Jangan pernah menyebut klaim "RuView bisa baca bahasa isyarat" sebagai fakta — gunakan batas versi repo sendiri.
