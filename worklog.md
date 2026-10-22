# Worklog — Multi-Agent Shared Log (append-only)

---
Task ID: 1
Agent: Super Z (main agent, sesi web)
Task: Unduh skill & handoff/spec dari Drive; eksplorasi mendalam repo RuView; analisis 3 opsi judul proposal (ayam broiler / kelas SLB / asrama SLB); push konteks ke GitHub ILoveTahuTek/skripsi sebagai backup anti-reset.

Work Log:
- Install gdown → unduh 2 file skill Drive + folder handoff (3 file) → /home/z/my-project/skills-drive/ & /home/z/my-project/drive-handoff/proposal/.
- Baca lengkap handoff, spec eksekusi BISINDO v1, laporan dewan LLM garis ayam (16 hal, 10 referensi DOI terverifikasi).
- Clone ruvnet/RuView (depth 1) → /home/z/my-project/ruview-repo.
- Baca README (72KB), PROOF.md, docs/proof-of-capabilities.md, ADR-079, firmware README.
- Delegasikan eksplorasi very-thorough ke agent Explore: Python package, Rust v2 workspace (~60 crate), firmware C, 65+ edge modules, kalibrasi, training workflow, 21 entitas HA + 10 FSM semantik, tutorials, limitasi jujur, sleep monitoring.
- Verifikasi mandiri: ind_livestock_monitor.rs (poultry 15–30 BPM, event 530–533), direktori semantic/ (14 file FSM).
- Temuan kunci RuView: (a) NYATA = capture CSI ADR-018, presence heuristik, motion, napas/jantung manusia (band HARDCODE 0.1–0.5 Hz / 0.8–2.0 Hz di semua lapisan), fall, kalibrasi 600 frame + 8 anchor, record→train adaptif <1 dtk, MQTT/HA 21 entitas, dashboard, OTA; (b) STUB/LEMAH = pose 17-kp (PCK@20 3%, confidence=0), person count (degradasi >2–3 subjek), sleep-stage/apnea (eksperimental tak tervalidasi), 6/21 entitas HA tak dipublikasikan; (c) AYAM = jantung 250–330 BPM di luar band 2× (mustahil tanpa ubah kode), napas 15–30 BPM di tepi atas band, RCS "very low" utk 1,5–2,5 kg.
- Tulis 2 dokumen utama (Indonesia) di /home/z/my-project/download/skripsi-repo/01-ruview-exploration/: 01_EKSPLORASI_DEEP_RUVIEW.md (11 bagian + cheat-sheet path) & 02_PEMETAAN_FITUR_3_ALAT.md (matriks fitur×3 alat + 9 kandidat judul + 3 skenario keputusan + langkah berikutnya).
- Susun repo skripsi (README ringkasan keadaan + aturan, 00-handoff-spec/, 02-skills-arsip/ zip skill, worklog), commit, rebase di atas README placeholder remote ("sandbox buat glm agent" — dipertahankan dalam sejarah), push sukses ke main (68952c7..d49beeb).

Stage Summary:
- Repo GitHub terisi: github.com/ILoveTahuTek/skripsi (branch main) — konteks handoff + spec + laporan ayam + 2 dokumen eksplorasi RuView + arsip skill + worklog. Reset sandbox tidak akan menghilangkan konteks lagi.
- Posisi analisis: RuView = infrastruktur capture+DSP+alert; 3 alat = 1 platform, 3 deployment (beda penempatan node/threshold/protokol); rekomendasi prioritas: kelas SLB (fit terbaik RuView) → ayam Opsi-1 dewan (bukti paling matang) → asrama SLB (izin paling sensitif) — keputusan final milik user+pembimbing.
- Gerbang berikutnya yang mengikat ketiga opsi: cek kebaruan Scopus/DBLP (murah, jam pertama) + uji Delta-CSI fisik 2×ESP32 di lokasi target (minggu-1).
- Keamanan: token GitHub hanya di URL remote sesi, tidak ditulis ke file manapun di repo.

---
Task ID: 2
Agent: Super Z (main agent, sesi web)
Task: Eksekusi penuh /setup-matt-pocock-skills + /wayfinder (lanjutan Task 1 setelah user minta perintah dieksekusi, bukan sekadar diarsipkan).

Work Log:
- Install 31 skill mattpocock + academic-research ke /home/z/my-project/skills/ → 101 SKILL.md total (match handoff sesi sebelumnya).
- setup-matt-pocock-skills di skripsi-repo: AGENTS.md, docs/agents/{issue-tracker,triage-labels,domain}.md, GLOSSARY.md, docs/adr/README.md; 9 label baru di GitHub (5 triage + 4 wayfinder).
- wayfinder chart: map issue #1 + 4 tiket child (#2 research kelas SLB, #3 research tidur/asrama, #4 task Delta-CSI, #5 grilling kunci judul), sub-issue 4/4, native dependencies 3/3.
- 2 subagent riset paralel (web-search ~50 query): #2 SLB classroom gap SEARCH-LIMITED condong kosong (classroom-CSI umum VERIFIED tipis); #3 tidur/asrama anak gap SEARCH-LIMITED condong kosong (CSI sleep dewasa VERIFIED ramai; band 0,5 Hz tepi kritis utk anak — rekomendasi ±0,66–0,77 Hz).
- Resolusi: komentar + close #2 #3, map Decisions-so-far terisi; laporan di 02-wayfinder-research/ (terpush); README+worklog repo diperbarui.

Stage Summary:
- Script persisten: scripts/install_skills.sh, scripts/wayfinder_chart.py, scripts/wayfinder_resolve.py.
- Frontier tracker = #4 (Delta-CSI fisik, butuh manusia beli ESP32); lalu #5 grilling (human-owned).
- Semua pushed ke github.com/ILoveTahuTek/skripsi (3 commit: setup, wayfinder+riset).

---
Task ID: 3
Agent: Super Z (main agent, sesi web)
Task: Susun 3 Dokumen Pengajuan Judul (DPJ) berbeda judul via eksekusi nyata /grill-with-docs + riset referensi SLB + generate 3 DOCX penuh.

Work Log:
- Eksekusi /grill-with-docs sungguhan: 31 skill mattpocock diinstall ulang dari zip (101 SKILL.md); rantai grill-with-docs → grilling (interview frontier) + domain-modeling (GLOSSARY/ADR) dimuat penuh.
- Grilling round-1 via AskUserQuestion (8 pertanyaan): 3 dokumen per alat; 1 judul utama + 2 alternatif per dokumen; DOCX; penuh 10+ hal; full paket; referensi dicari baru; RuView eksplisit; tanpa cover; jadwal 1 semester.
- domain-modeling: 3 istilah baru terkunci di GLOSSARY.md repo (DPJ, Judul utama+alternatif, Jadwal semester); 0 ADR (tidak lolos tiga gerbang).
- Riset referensi (pilihan user): 10 kueri web (scripts/search_slb_refs.sh) + verifikasi Crossref (scripts/verify_slb_refs.py, verify_slb_refs2.py) → 15 entri terverifikasi DOI utk garis SLB; disimpan tool-results/slb-refs/.
- Generator persisten: scripts/dpj_common.js + dpj_content_{1_ayam,2_kelas,3_asrama}.js + generate_dpj.js (renderer akademik: TNR 12pt, line 360, three-line table, sitasi [n], refs hanging indent, tanpa page break, footer "- N -").
- 3 DOCX: download/proposal-pengajuan-judul/DPJ-{1,2,3}_*.docx (12/11/11 hal); postcheck 0 error; cek PDF 11-12 hal; inspeksi visual halaman judul + tabel OK.
- Backup: skripsi-repo/03-dpj/ (+generator) & 04-referensi-slb/; README diperbarui; commit 478d564 push sukses (4110ac5..478d564).

Stage Summary:
- 3 DPJ siap dibawa ke pembimbing; semua klaim dibatasi "studi kelayakan"; pose stub/apnea tidak dijanjikan; Delta-CSI = gerbang minggu-3 di ketiga dokumen.
- Keputusan judul final tetap human-owned (issue #5).

---
Task ID: T2-a
Agent: general-purpose subagent
Task: Riset literatur WiFi-CSI isyarat utk judul baru (WiFi-CSI human presence sensor high-frequency pengenalan gerakan translasi SIBI/BISINDO di prasarana edukasi, platform RuView) — GitHub issue #10 repo ILoveTahuTek/skripsi. Output: referensi terverifikasi + gap-analisis, tanpa DOCX/PDF.

Work Log:
- Baca worklog.md (Task 1-3) + contoh format 04-referensi-slb/verified_refs.json (tidak diubah isinya).
- 14 kueri web_search (12 wajib + 2 tambahan: SignFi, classroom CSI; 2 retry varian kueri utk 422/429) → /home/z/my-project/tool-results/isyarat-refs/search-{1..16}.json (search-15/16 utk verifikasi web paper ESP32).
- Seleksi 22 kandidat (prioritas IEEE/ACM/Elsevier/MDPI terindeks 2017-2025; 5 entri SIBI/BISINDO lokal-ber-DOI).
- Verifikasi SEMUA 22 via Crossref API (curl works/<DOI> + query.bibliographic utk DOI tak diketahui; ~30 panggilan, arsip di tool-results/isyarat-refs/crossref/): koreksi DOI Widar3.0 MobiSys 10.1145/3307334.3326081, temukan DOI Sebastian Procedia 10.1016/j.procs.2025.09.042 & SLR BISINDO IJCS 10.33022/ijcs.v12i6.3539; paper ESP32 Hernandez-Bulut akhirnya ketemu DOI Crossref resmi 10.1109/wowmom49955.2020.00056 (WoWMoM 2020) — bukan PerCom (DOI "9150562" tidak terdaftar).
- Tulis download/skripsi-repo/06-referensi-isyarat/verified_refs.json: 22 entri (22 verified DOI, 0 web-only). Isi: SignFi IMWUT'18, DF-WiSLR PMC'20, IAICT'21 LSTM SLR, WiSign MobiArch'17, FSL TENCON'24, WiASL Measurement'23, Widar3.0 TPAMI'21+MobiSys'19, CSUR'19+CSUR'23 surveys, EAAI'20 survey gesture, InfoSci'23 dynamic gesture, Wi-SL Sensors'20, HandFi Procedia'24, Cai Sensors'24 amp+phase, ESP32 WoWMoM'20, IJACSA'21 BISINDO CNN, IJACSA'25 sentence-level, WL-BISINDO Procedia'25, Sebastian Procedia'25, BISINDO SLR IJCS'23, Frontiers Edu'23 assistive deaf.
- Tulis gap-analisis.md (8 paragraf): keadaan seni CSI gesture; SLR-CSI tanpa pose (konsisten dgn pose-RuView stub PCK@20~3%); posisi SIBI/BISINDO 100% vision tanpa satu pun publikasi CSI (celah); kebaruan kombinatif bahasa+platform+konteks edukasi; disiplin klaim = klasifikasi per-gestur tersegmentasi 5-12 kelas, bukan penerjemah kontinu; 5 risiko+mitigasi (R1 cross-domain, R2 tak ada dataset CSI SIBI/BISINDO, R3 keterbatasan ESP32/RuView→gerbang Delta-CSI, R4 gestur ambigu, R5 etika anak); ringkasan posisi.
- Belum push git (sesuai batasan; push oleh agent lain).

Stage Summary:
- Issue #10: dikomentari ringkasan lalu ditutup (closed). File deliverable ada di repo lokal skripsi-repo/06-referensi-isyarat/ (verified_refs.json 22 entri + gap-analisis.md).
- Klaim aman: semua 22 referensi punya DOI terverifikasi Crossref → tinggal dipakai langsung di DPJ baru; 0 entri web-only.
- Pesan kunci utk pembimbing: preseden CSI-SLR internasional kuat (SignFi/DF-WiSLR/FSL-TENCON) tetapi padanan SIBI/BISINDO = nol publikasi; proposal harus dijaga pada klaim kelayakan klasifikasi per-gestur, pose RuView TIDAK dijanjikan.

---
Task ID: 4 (Tugas 1+2: skill proposal-writing + DPJ-4)
Agent: Super Z (main agent, sesi web)
Task: Push backup GitHub; Tugas 1 = buat skill baru aturan proposal dari korpus Drive (pakai to-tickets, implement, GEPA); Tugas 2 = riset + proposal ke-4 (WiFi-CSI SIBI/BISINDO, RuView); semua dipecah ticket #6-#14 dan dieksekusi ke worklog. Skip cover.

Work Log:
- Push backup sukses (478d564..6d862f3) dengan token baru (token hanya di URL remote sesi).
- gdown folder Drive 1Dk8kygzZZkFQE9uc-Z2zPbltToQMz-lF → 69 dokumen (120 MB): proposal TA, naskah, semhas, paten — korpus D4 TRSE Universitas Negeri Malang (terkonfirmasi dari sampul+NIM).
- to-tickets: 9 ticket dipublikasikan sebagai issue #6-#14 (quiz-user di-skip karena user memerintahkan eksekusi langsung).
- [#6 T1-a] Analisis 12 dokumen korpus (teks penuh via pdftotext/pandoc): struktur 5-BAB kanonik 8/8 konsisten, pola bahasa literal (corong, pembuka subbab, narasi tahapan, sitasi APA 7, abstrak, mekanika PUEBI) → 05-analisis-korpus/analisis-korpus-proposal.md + rubric.json (D1-D6 berbobot).
- [#7 T1-b] Seed skill v1: SKILL.md (6 langkah + kriteria selesai) + 3 references (struktur-dpj, bahasa-korpus, disiplin-klaim) + scripts/evaluator.py.
- [#8 T1-c] GEPA ASLI: pip gepa 0.1.4, optimize_anything single-task, reflection_lm = callable z-ai chat (glm-4-plus; deviasi dari openai/gpt-5.1 didokumentasikan), max_metric_calls=24. Hasil: seed 0.7196 → 4 kandidat → iterasi 5 kandidat 3 diterima skor 1.0 (engine berhenti dini oleh lingkungan; artefak run1 terselamatkan). Kurasi anti reward-hacking (term-dump dihapus, diganti checklist fungsional) → v3-final skor 1.0 legitim. Evaluator diperbaiki: line-wrap normalize + regex alternasi.
- [#9 T1-d] Skill final terinstall /home/z/my-project/skills/proposal-writing/ (smoketest exit 0). Issue #7 #8 #9 closed.
- [#10 T2-a] Subagent riset literatur: 22 referensi verified-DOI Crossref (SignFi, DF-WiSLR, Widar3.0 TPAMI, FSL-CSI TENCON 2024, ESP32-CSI-Tool, 5 SIBI/BISINDO) + gap-analisis (SIBI/BISINDO 100% vision, celah kombinatif nyata, klaim terbatas gestur terisolasi) → 06-referensi-isyarat/. Issue #10 closed.
- [#11 T2-b] Pemetaan fitur RuView → isyarat (MEASURED vs STUB; fisika Doppler gestur >> napas; pernyataan disiplin klaim) → 06-referensi-isyarat/ruview-fitur-isyarat.md. Issue #11 closed.
- [#12 T2-c] Outline DPJ-4 dikunci via Outline tool (11 seksi konsisten DPJ 1-3, tanpa cover).
- [#13 T2-d] dpj_content_4_isyarat.js + generate_dpj4.js (reuse dpj_common.js) → DPJ-4 DOCX 15 halaman, 6 tabel, 19 referensi terverifikasi; evaluator doc-mode skor 1.0; PDF preview + inspeksi visual OK. Issue #12 #13 closed.
- [#14 T2-e] Semua artefak dikommit: 05-analisis-korpus (analisis + rubric + skill 3 versi), 06-referensi-isyarat, 07-dpj-4 (docx+preview+generator+evaluator), scripts; push GitHub; issue #6-#14 semua closed.

Stage Summary:
- Skill baru "proposal-writing" (model-invoked, mattpocock format) siap dipakai untuk proposal berikutnya: membawa struktur + bahasa korpus TRSE UNM + disiplin klaim WiFi-CSI + evaluator rubrik D1-D6.
- DPJ-4 melengkapi set jadi 4 proposal: judul utama "Pengenalan Gestur Bahasa Isyarat SIBI dan BISINDO Berbasis Wi-Fi CSI pada ESP32 untuk Prasarana Edukasi: Studi Kelayakan Translasi Tanpa Kamera" + 2 alternatif.
- Disiplin tetap: studi kelayakan, gestur terisolasi 5-12 kelas, 1 penandatangan, pose stub terlarang, gerbang Delta-CSI minggu-3.
- GEPA: nilai metodologis terverifikasi (seed→accept lineage tersimpan run1/candidates.json); pelajaran reward-hacking terdokumentasi.

---
Task ID: 5
Agent: Super Z (main agent, sesi web)
Task: Remake 4 proposal (DPJ-1..4) ke struktur BAB I-III menggunakan skill proposal-writing hasil GEPA + push GitHub (ticket #15-#21, perintah user: "proposal hanya mencakup bab 1-3; gunakan skill yang telah dibuat + GEPA; push github repoku").

Work Log:
- to-tickets: 7 ticket #15-#21 dipublikasikan ke GitHub Issues dengan blocked-by native (R-a skill, R-b renderer+DPJ-1, R-c DPJ-2, R-d DPJ-3, R-e DPJ-4, R-f loop GEPA+QA, R-g push/worklog/close).
- [#15 R-a] Skill diperbarui: struktur-dpj.md + SKILL.md (langkah 3 & checklist D1) kini mengunci ruang lingkup proposal = BAB I-III + DAFTAR PUSTAKA — jadwal/biaya/risiko menjadi subbab BAB III (3.9-3.11), pernyataan disiplin klaim disisipkan di 1.4; evaluator --skill = 1.0 setelah perubahan.
- [#16-#19 R-b..R-e] Renderer dpj_common.js ditingkatkan: judul utama KAPITAL semua + blok Judul Alternatif 1/2 pada title block, heading BAB dua baris (BAB I / PENDAHULUAN), dukungan sub-subbab 1.5.1 Manfaat Teoretis/1.5.2 Praktis, penomoran tabel per bab passthrough. Empat konten ditulis ulang penuh: BAB I (1.1 Latar Belakang corong 4 lapis + Tabel 1.1 usulan judul; 1.2 Rumusan "Bagaimana...?"; 1.3 Tujuan frasa kerja mirror; 1.4 Batasan + item "tidak membahas" + disiplin klaim; 1.5 Teoretis/Praktis), BAB II KAJIAN PUSTAKA (2.1 CSI; 2.2 ESP32; 2.3 RuView + Tabel 2.1; 2.4-2.5 domain; 2.6 Penelitian Terdahulu + Tabel 2.2 perbandingan baru + gap), BAB III METODE PENELITIAN (3.1 tahapan naratif korpus; 3.2 studi literatur + verifikasi Crossref; 3.3-3.5 perancangan; 3.6 lokasi/etika; 3.7 rencana pengujian; 3.8 evaluasi + go/no-go; 3.9 jadwal semester Tabel 3.1; 3.10 biaya Rupiah Tabel 3.2; 3.11 risiko+fallback Tabel 3.3) + DAFTAR PUSTAKA.
- Bug #1 (metrik) ditemukan: salinan evaluator di skill dir masih versi lama — re.escape mematikan alternasi "|" sehingga semua istilah regex (KAJIAN PUSTAKA|TINJAUAN PUSTAKA, Delta-CSI|go/no-go, memengaruhi|mempengaruhi, (\d{4})) gagal palsu (skor 0,585 untuk semua dokumen). Fix: sinkronkan versi regex yang benar dari scripts/evaluator.py (artefak GEPA T1-c) ke skill dir; --skill tetap 1,0.
- Bug #2 (render) ditemukan via inspeksi visual: daftar bernomor tidak dirender (numbering reference tanpa config). Fix: numberedPara eksplisit "1. ..." + hanging indent; diregenerasi ulang semua dokumen; verifikasi visual halaman 3 DPJ-1 menunjukkan nomor tampil.
- [#20 R-f] Loop GEPA doc-mode: 4/4 dokumen skor 1.0 (D1-D6 penuh) — hasil evaluasi di 03-dpj/evaluasi-gepa/; PDF (soffice) 15/14/14/16 halaman; visual halaman judul (judul kapital + alternatif, tanpa cover), tabel tiga garis 2.1/1.1, dan daftar bernomor semua OK.
- [#21 R-g] Artefak remake dikommit: 03-dpj (4 DOCX baru + generator v2 + evaluasi-gepa), 07-dpj-4 (DOCX+konten baru), 05-analisis-korpus/skill-proposal-writing (SKILL.md v4 + referensi + evaluator tetap + versions/v4-bab123); push ke GitHub main; ticket #15-#21 ditutup.

Stage Summary:
- 4 proposal kini resmi berformat PROPOSAL (BAB I-III + Daftar Pustaka, tanpa bab rencana terpisah) sesuai klarifikasi user; aturan itu sendiri sudah terekam di skill untuk run berikutnya.
- Semua dokumen skor evaluator GEPA 1,0; dua bug (evaluator regex alternasi, numbering DOCX) ditemukan dan diperbaiki lewat loop inspeksi — pelajaran: perbaiki metrik dan renderer sebelum menghukum konten.
- Disiplin tetap terjaga di keempat dokumen: studi kelayakan, gestur terisolasi 5-12 kelas (DPJ-4), pose stub terlarang, gerbang Delta-CSI 2xESP32 minggu-3, placeholder eksplisit.

---
Task ID: 8
Agent: Super Z (main agent, sesi web)
Task: Panduan penulisan proposal DPJ-4 lingkup SIBI-only (tanpa BISINDO) — DOCX 20 hal + markdown + generator; folder 09-panduan-dpj4-sibi; commit a527270.

Work Log:
- Sumber: analisis korpus Drive TRSE UNM (05-analisis-korpus), skill proposal-writing GEPA v4, skill naskah-id, DPJ-4 md, gap-analisis + 22 referensi terverifikasi (06-referensi-isyarat).
- Generator persisten 4 file JS (panduan_common + konten A/B + generate) disalin ke 09-panduan-dpj4-sibi/generator/.
- QA: postcheck 0 error; PDF 20 hal; lint periksa.py bersih (2 temuan tersisa = kutipan pedagogis disengaja); pandoc mirror + md_postprocess (0 residu).
- README diperbarui (bullet folder 05-09); push b29f283..a527270.

Stage Summary:
- Panduan berisi: argumen SIBI-only utk pembimbing, struktur wajib BAB I-III, templat bahasa korpus, ejaan baku, disiplin klaim SIBI-only, peta revisi 16 titik + templat siap tempel (judul/rumusan/tujuan/batasan 7 butir), 19 referensi dgn peran, checklist D1-D6 + alat QA.
- Referensi BISINDO tetap dipakai sebagai bukti celah; klaim kebaruan dua lapis tetap sah utk SIBI.
