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
