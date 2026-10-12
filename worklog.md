# Worklog — Multi-Agent Shared Log (append-only)

---
Task ID: 1
Agent: Super Z (main agent, sesi web)
Task: Unduh skill & handoff/spec dari Google Drive, eksplorasi mendalam repo RuView, siapkan repo GitHub ILoveTahuTek/skripsi sebagai backup konteks.

Work Log:
- Install gdown (venv) → unduh 2 file skill Drive (academicResearchSkill.zip, mattpocock-skills.zip) ke /home/z/my-project/skills-drive/.
- Unduh folder Drive handoff (3 file: Handoff, Spec v1, New Text Document) ke /home/z/my-project/drive-handoff/proposal/.
- Baca lengkap: Handoff_Riset_BISINDO_WiFi_CSI.md, Spec_Eksekusi_BISINDO_WiFi_CSI_v1.md, laporan dewan LLM garis ayam (16 hal).
- Clone https://github.com/ruvnet/RuView.git (depth 1) ke /home/z/my-project/ruview-repo.
- Baca README.md (fisik/BOM/tabel fitur), PROOF.md, docs/proof-of-capabilities.md, ADR-079, firmware README.
- Delegasikan eksplorasi very-thorough ke agent Explore: python package, v2 Rust workspace, firmware C, edge modules, kalibrasi, training workflow, semantic states, tutorials, limitasi, sleep monitoring.
- Verifikasi mandiri file kunci: v2/crates/wifi-densepose-wasm-edge/src/ind_livestock_monitor.rs (poultry 15–30 BPM, event 530–533), direktori semantic/ (14 FSM).
- Temuan kunci: bandpass napas/jantung HARDCODE manusia di semua lapisan; jantung ayam 250–330 BPM di luar band; pose on-device = stub (PCK@20 3%, confidence=0); person count lemah; sleep-stage/apnea tak tervalidasi; kalibrasi ruangan 600 frame + 8 anchor nyata; workflow record→train adaptif nyata.
- Tulis 2 dokumen analisis (Indonesia): 01_EKSPLORASI_DEEP_RUVIEW.md (deep-dive 11 bagian + cheat-sheet path) dan 02_PEMETAAN_FITUR_3_ALAT.md (pemetaan fitur→3 alat + 9 kandidat judul + rekomendasi keputusan).
- Susun struktur repo skripsi: README.md (ringkasan keadaan + aturan), 00-handoff-spec/, 01-ruview-exploration/, 02-skills-arsip/ (zip skill), worklog.md.
- Setup git + push ke https://github.com/ILoveTahuTek/skripsi.git (token via remote URL sesi, tidak ditulis ke file).

Stage Summary:
- Artefak utama: /home/z/my-project/download/skripsi-repo/ (terpush ke GitHub).
- Keputusan/posisi: RuView = infrastruktur capture+DSP+alert (bukan mesin pengenalan); 3 alat = 1 platform, 3 deployment; kandidat judul per alat tersedia (9 total) dengan rekomendasi prioritas kelas SLB → ayam (Opsi-1 dewan) → asrama, menunggu keputusan user+pembimbing.
- Langkah murah berikutnya: cek kebaruan Scopus/DBLP + uji Delta-CSI 2×ESP32 (berlaku utk ketiga opsi karena platform sama).
- Catatan keamanan: token GitHub TIDAK disimpan di file repo; hanya di remote URL sesi git.

---
Task ID: 2
Agent: Super Z (main agent, sesi web)
Task: Eksekusi penuh /setup-matt-pocock-skills + /wayfinder pada repo skripsi.

Work Log:
- Install 31 skill mattpocock (engineering 20 + misc 4 + productivity 7) + academic-research → /skills/ → total 101 SKILL.md (match handoff).
- Buat 10 label GitHub (5 triage default + 5 wayfinder:*); wontfix 422 (sudah ada bawaan).
- setup-matt-pocock-skills: tulis AGENTS.md (blok ## Agent skills + keputusan setup + aturan kerja), docs/agents/issue-tracker.md (GitHub REST via curl, gh tak terpasang), docs/agents/triage-labels.md (default), docs/agents/domain.md (single-context), GLOSSARY.md (kosakata domain terkunci: flock-level, Delta-CSI, evidence-state, dst.), docs/adr/README.md. Commit 1b6daf0.
- wayfinder chart: map #1 (wayfinder:map) + 4 tiket child: #2 research kebaruan kelas SLB, #3 research kebaruan tidur/asrama+vital anak, #4 task uji Delta-CSI 3 lokasi, #5 grilling kunci judul (blocked_by #2,#3,#4 via native dependencies 3/3; sub-issue 4/4).
- Fire 2 subagent riset paralel (web-search). Hasil #2: classroom-CSI umum VERIFIED (tipis); SLB-specific SEARCH-LIMITED condong kosong → kebaruan alat 2 di konteks+privasi. Hasil #3: CSI tidur dewasa VERIFIED ramai (2014–2025); anak/kebutuhan-khusus asrama SEARCH-LIMITED condong kosong → kebaruan alat 3 di populasi; band napas 6–30 BPM aman utk anak sekolah tidur tapi tepi atas 0,5 Hz kritis (rekomendasi ±0,66–0,77 Hz); rujukan vital anak: Fleming 2011 Lancet, Herbert 2020, PALS 2015.
- Arsipkan 2 laporan riset ke 02-wayfinder-research/; posting komentar resolusi; tutup #2 & #3; update map #1 (Decisions so far).
- README diperbarui (struktur + status tracker). Push final.

Stage Summary:
- Frontier sekarang = tiket #4 (uji Delta-CSI fisik, HITL: beli 2×ESP32-S3, flash RuView v0.8.8, 3 lokasi).
- Setelah #4 selesai → #5 (grilling kunci judul, human-owned) → keluar map → /to-spec.
- Kedua riset menyimpulkan gap condong kosong tapi berlabel SEARCH-LIMITED; verifikasi Scopus/IEEE Xplore dititipkan di #5.

---
Task ID: 3
Agent: Super Z (main agent, sesi web)
Task: Susun 3 Dokumen Pengajuan Judul (DPJ) berbeda judul — eksekusi /grill-with-docs (grilling + domain-modeling) + riset referensi baru garis SLB + generate 3 DOCX penuh.

Work Log:
- Eksekusi nyata /grill-with-docs: 31 skill mattpocock diinstall ulang dari zip (101 SKILL.md di sistem); rantai grill-with-docs → grilling + domain-modeling dibaca penuh.
- Grilling round-1 (8 pertanyaan): jawaban terkunci — 3 dokumen per alat, tiap dokumen 1 judul utama + 2 alternatif; DOCX; penuh 10+ hal; full paket (tabel fitur + risiko/fallback + jadwal + anggaran + batasan); referensi DICARI BARU utk garis SLB; RuView eksplisit; tanpa cover identitas; jadwal 1 semester (4,5 bln).
- domain-modeling: 3 istilah baru terkunci di GLOSSARY.md (DPJ, Judul utama+alternatif, Jadwal semester). Tidak ada ADR baru (tidak lolos tiga gerbang).
- Riset referensi baru (pilihan user): 10 kueri web + verifikasi Crossref (scripts/verify_slb_refs.py, verify_slb_refs2.py) → 13 kandidat terverifikasi (RT-Fall TMC 2017, TCS-Fall Digital Health 2024, Brena Electronics 2021, Jiang IEEE Access 2018, Zou CVPRW 2019, Al-qaness GIS 2019, Galdino IEEE Access 2023, Mosharaf Sensors 2024, Wi-Sleep RTSS 2014, Tataraidze EMBC 2019, Burimas Applied Sciences 2024, Kontou JBHI 2024, Chang VTC 2023, Pich ICCMA 2025, Touhiduzzaman MobiCom 2024).
- Generator persisten: scripts/dpj_common.js (renderer akademik: TNR 12pt, spasi 1,5, three-line table, sitasi [n], refs hanging indent, header/footer, tanpa page break) + 3 file konten + generate_dpj.js.
- 3 DOCX dibuat di download/proposal-pengajuan-judul/ (12/11/11 halaman); postcheck.py 0 error per file; PDF conversion check + inspeksi visual halaman judul & tabel OK.
- Artefak dibackup ke repo: 03-dpj/ (3 docx + generator), 04-referensi-slb/ (hasil verifikasi Crossref).

Stage Summary:
- 3 DPJ siap dibawa ke pembimbing: DPJ-1 ayam (judul Opsi-1 dewan), DPJ-2 kelas SLB, DPJ-3 asrama SLB — masing-masing 10 bab + 5 tabel + 10 referensi terverifikasi DOI.
- Semua klaim dibatasi "studi kelayakan"; pose stub & apnea eksperimental tidak dijanjikan; Delta-CSI = gerbang go/no-go minggu-3 di ketiga dokumen.
- Keputusan judul final tetap human-owned (#5 grilling di issues).
