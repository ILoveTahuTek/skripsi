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
Task ID: 6
Agent: Super Z (main agent, sesi web)
Task: Konversi 4 Google Docs (DPJ-1..4 versi BAB I-III) menjadi 4 file Markdown terpisah; backup ke GitHub.

Work Log:
- Unduh 4 doc via endpoint export docs.google.com (format=docx, HTTP 200, 26-29 KB; verifikasi `file` = Microsoft Word 2007+; 0 media/gambar). ID: 1QdfLfVD (DPJ-1 broiler), 1WARmt9x (DPJ-2 kelas SLB), 17vku-HV (DPJ-3 asrama SLB), 1yK3LkJe (DPJ-4 isyarat) — judul terkonfirmasi dari docProps/core.xml.
- pandoc 3.1.11.1: docx -> GFM (--wrap=none) -> download/markdown/DPJ-{1..4}_*.md (243-269 baris; heading BAB I-III + subbab utuh, tabel GFM utuh, sitasi [n] & DOI utuh, placeholder 【...】 utuh).
- Post-process scripts/md_postprocess.py: blockquote bawaan pandoc utk daftar bernomor eksplisit ("> 1\\.") -> ordered list GFM polos; 59 item + 43 separator dibersihkan; 0 blockquote residu di 4 file.
- Backup GitHub: 08-markdown-dpj/ (4 md) + 42 file mode-only (100644->100755, 0 delta konten) dikommit 4f64df6, push main sukses (434861e..4f64df6).

Stage Summary:
- 4 markdown terpisah siap di download/markdown/ dan mirror di repo GitHub folder 08-markdown-dpj/.
- Struktur markdown identik dgn DOCX remake BAB I-III (tanpa cover); siap dipakai sebagai korpus pembanding/diff utk revisi proposal berikutnya.

---
Task ID: 7
Agent: Super Z (main agent, sesi web)
Task: Perbaiki penulisan & bahasa 4 proposal DPJ (markdown upload user di Drive) dengan skill naskah-id (file Drive 1aK3y8Ah..., path /naskah-id); regenerasi DOCX; push GitHub.

Work Log:
- gdown 6 file Drive: 1 zip = skill naskah-id (dipasang ke skills/naskah-id + diarsip ke repo skills-arsip/), 1 handoff (bukan proposal), 4 markdown DPJ — md5 identik dengan salinan lokal download/markdown/.
- Baca lengkap SKILL.md + KONTRAK.md + 8 references (pola-ai, kalimat-efektif, ejaan-eyd-v, kata-baku, pertahankan, sitasi, bagian-naskah, alat-riset) → pekerjaan = level SUNTING; angka/sitasi/klaim tidak disentuh.
- periksa.py awal: 44 temuan (EJ-10 koma-sehingga 41, KB-01 kontinyu, AI-14 di mana, EJ-05 multi). Penandaan manual menyeluruh 4 berkas (4×~250 baris): + kalke Inggris (kecil-kecil banyak, kontak-less, dewasa-ke-anak, lintas-person, ter-update, mendeploy), kata depan per- (21), blok-waktu, et al.→dkk. (46), nominalisasi, verba tujuan "Mengetahui"→"Menguji", kalimat >35 kata dipecah, splice koma di 2.6 (4 file), antar-/lintas- serangkai & terpisah, Doppler kapital, entropy→entropi, threshold→ambang, milidetik→ms, dsb.
- scripts/fix_bahasa_dpj.py: ~62 pasangan (old,new) global+per-file diterapkan IDENTIK ke 4 md DAN 4 modul konten JS (sinkron); 2 perbaikan susulan (antar-sesi→antarsesi; ", karena" 2×).
- Keputusan desain: cetak miring istilah asing DITUNDA (aturan lokal didahulukan — pedoman kampus belum dicek; konsistensi > sebagian); istilah teknis asing lazim + judul + angka + daftar pustaka dipertahankan (pertahankan.md).
- Regenerasi 4 DOCX (node generate_dpj.js) → QA: periksa.py 0 temuan; evaluator GEPA D1-D6 = 4/4 skor 1.0; postcheck.py 0 error (1 warning spasi = desain tabel, sama dgn versi lolos); sync-verify pandoc round-trip 4/4 identik (scripts/verify_sync_dpj.py, normalisasi padding tabel); PDF 15/14/14/16 hal; visual hal-3 & hal-12 OK.
- CATATAN-PERUBAHAN.md (sebelum→sesudah per kategori + verifikasi + tindak lanjut) di download/markdown/ & repo 08-markdown-dpj/.
- Commit b29f283 push main sukses (4f64df6..b29f283): DOCX 03-dpj/07-dpj-4, generator+script QA, markdown+catatan, arsip skill naskah-id.

Stage Summary:
- 4 proposal versi bahasa-final: markdown (download/markdown/) + DOCX (download/proposal-pengajuan-judul/) — konten kedua format terjamin sinkron.
- Skill naskah-id kini terpasang di skills/naskah-id dan bisa dipakai ulang (periksa.py sbg lint bahasa).
- Sisa keputusan human-owned: miring istilah asing menunggu konfirmasi pedoman kampus; placeholder 【…】 masih kosong.

---
Task ID: 8
Agent: Super Z (main agent, sesi web)
Task: Susun panduan penulisan proposal DPJ-4 lingkup SIBI-only (tanpa BISINDO) dari hasil pembelajaran korpus Drive TRSE UNM; DOCX + markdown + push GitHub.

Work Log:
- Rangkum sumber: worklog Task 1-7, analisis korpus 69 dokumen Drive (05-analisis-korpus), skill proposal-writing GEPA v4 (struktur/bahasa/disiplin), skill naskah-id, DPJ-4 markdown (peta 28 kemunculan BISINDO), gap-analisis + pemetaan RuView + 22 referensi terverifikasi.
- Keputusan desain dokumen: Template-Following Mode gaya DPJ (TNR 12pt, spasi 1,5, tanpa cover/TOC, footer "- N -", tabel three-line) — konsisten ekosistem 4 DPJ yang lolos QA; rantai skill docx dibaca penuh (SKILL.md, create.md, academic.md, common-rules.md, docx-js-core.md, design-system.md).
- Generator persisten: scripts/panduan_common.js (renderer + quotePara templat + runsPara) + panduan_content_a.js (Bagian 1-4) + panduan_content_b.js (Bagian 5-8) + generate_panduan_dpj4_sibi.js.
- Konten panduan 8 bagian: (1) tentang panduan; (2) keputusan lingkup SIBI-only + 3 argumen + jebakan frasa dua-sistem; (3) struktur wajib BAB I-III (Tabel 2.1 kerangka 23 subbab); (4) pola bahasa korpus + templat literal; (5) ejaan/kata baku Tabel 4.1 old->new; (6) disiplin klaim SIBI-only + tabel batas + pernyataan templat; (7) peta revisi per bagian Tabel 6.1 (16 titik) + judul utama/2 alternatif baru + rumusan/tujuan/batasan 7 butir siap tempel + kebijakan referensi; (8) referensi Tabel 7.1 (19 entri + DOI + peran); (9) checklist D1-D6 + alat QA + keputusan human-owned.
- QA loop: postcheck 0 error (1 warning spasi tabel = desain, sama dgn DPJ lolos); PDF 21->20 hal setelah perbaikan; bug visual diperbaiki: sel tabel kosong dirender placeholder (safeText) -> dibiarkan kosong, kolom Bab 16->23% agar PENDAHULUAN tidak terpotong kata; lint periksa.py: 7 temuan -> 5 koma-sehingga + 1 typo (isvat->isyarat) dibersihkan di sumber JS, regenerasi; sisa 2 temuan = kutipan pola keliru yang disengaja (Tabel 4.1).
- Mirror markdown: pandoc -> GFM + md_postprocess.py (diperluas agar menerima argv; 25 item numbered + 22 separator dibersihkan; 0 residu blockquote rusak).
- Push GitHub: 09-panduan-dpj4-sibi/ (DOCX + PDF pratinjau + markdown + generator 4 file) + README diperbarui (bullet folder 05-09) -> commit a527270, push main sukses (b29f283..a527270).

Stage Summary:
- Panduan 20 halaman tersimpan di download/panduan-proposal/ (DOCX + PDF + markdown mirror) dan mirror repo GitHub folder 09-panduan-dpj4-sibi/.
- Inti panduan: keputusan SIBI-only dibela dengan 3 argumen (formal-terstandar, beban dataset 1 semester, kebaruan kombinatif tetap sah); referensi BISINDO TETAP disitasi sebagai bukti lanskap-celah; klaim kebaruan dua lapis ("belum ada CSI untuk SIBI maupun BISINDO" + "penelitian ini menargetkan SIBI").
- Sisa human-owned: konfirmasi judul ke pembimbing, isi placeholder, miring istilah asing, uji fisik Delta-CSI W3, lalu revisi DPJ-4 sesuai peta Bagian 6.

---
Task ID: 9
Agent: Super Z (main agent, sesi web)
Task: Buat skill/panduan agent "proposal-writing v5" (markdown terpecah per bagian, isi EN, keluaran ID) dari korpus skripsi Drive + panduan Bina Darma + integrasi to-tickets, naskah-id (GitHub), GEPA; eksekusi via to-tickets #22-#27; push GitHub.

Work Log:
- Unduh 3 file Drive baru: panduan Bina Darma 2022 (PDF 33 hal, file 1sdvz1Mq...), arsip skills-main/to-tickets (1z7a-xaB...), skill gepa-optimize-anything (1KZiprYa...) -> tmp/refs3/; verifikasi tipe via `file`.
- Clone github.com/nothinx/naskah-id -> versi GitHub LEBIH BARU dari arsip zip lama (tambahan istilah.md, singkatan.md, CHANGELOG.md, evals/jalankan.py); sinkronkan skills/naskah-id + arsip repo ke versi GitHub.
- Baca lengkap semua sumber: PDF Bina Darma (struktur laporan, margin/font Cambria/style Word, penomoran, kutipan APA-Harvard signal-phrase vs parenthetical + larangan "oleh (Nama, Tahun)", sumber sekunder, kutipan >=40 kata, caption tabel-atas/gambar-bawah, mekanika tanda baca), SKILL.md gepa + to-tickets.md, skill v4 + 3 referensi + rubric.json D1-D6.
- to-tickets: 6 tiket #22-#27 dipublikasikan (blockers first, edge native blocked-by 6/6 HTTP 201 via REST dependencies API); #22 prefactor ditutup segera (sudah selesai).
- Tulis skill v5: SKILL.md (EN, 158 baris, 9 langkah, semua "Done when") + 10 referensi terpecah per bagian: 00 kontrak bahasa keluaran (EN->ID + glosarium istilah tak-terjemahkan), 01 lingkup proposal=BAB I-III, 02 struktur kanonik + tabel wajib + switch profil, 03 pola bahasa korpus (templat ID verbatim), 04 sitasi (aturan Bina Darma + APA 7 + pipeline verifikasi Crossref/OpenAlex), 05 format dua profil (DPJ-UNM vs BD-2022) + PUEBI + tanda baca, 06 jembatan naskah-id (load-when map + tabel perbaikan rutin Task 7), 07 disiplin klaim + lingkup SIBI-only, 08 loop GEPA (kontrak evaluator, anti reward-hacking, budget, preseden reflection_lm z-ai), 09 workflow (pipeline + integrasi + gerbang mutu).
- Bawa evaluator v4 ke scripts/ + 2 patch: REF_FILES -> 10 referensi baru; kriteria selesai menerima "Selesai bila|Done when". Sinkron kedua salinan (skill dir + scripts/).
- QA: evaluator --skill = 1.0 (D1-D6 coverage 1.0, 9 langkah/9 done-when, 0 fail); audit token: SKILL.md 158 baris, referensi 54-79 baris/file, total 1.027; 0 pointer menggantung; smoke test --doc pada DPJ-1 = 0.96 (0,8 D2 karena suntingan sendiri pengguna "bertujuan menguji" tanpa "untuk" di Google Docs - variasi sah, bukan cacat skill).
- Kemas: download/skill-proposal-writing-v5.zip (15 file); mirror repo 10-skill-proposal-v5/ (skill + SOURCES.md + sources/panduan-bina-darma-2022.txt + gepa-skill-arsip.md); commit + push.

Stage Summary:
- Skill proposal-writing v5 terpasang di skills/proposal-writing/ dan terarsip di repo (10-skill-proposal-v5/): panduan agent markdown terpecah 10 bagian, isi EN hemat token, keluaran wajib ID; integrasi to-tickets (slicing), naskah-id (EYD-V lint + etika rujukan), GEPA (optimalisasi kata-per-kata).
- Sumber terdokumentasi di SOURCES.md: korpus TRSE UNM (folder Drive), panduan Bina Darma 2022 (file Drive), to-tickets + GEPA (file Drive), naskah-id (GitHub) - "menyalin cara menulis, bukan isinya".
- Pemakaian: arahkan agent ke folder skill (atau pakai zip); SKILL.md memuat proses 9 langkah; untuk dokumen kampus Bina Darma pilih profil BD-2022.

---
Task ID: 10
Agent: Super Z (main agent, sesi web)
Task: Ekstraksi mendalam bahan/metode/masalah/penyelesaian untuk penulisan proposal DPJ-4 dengan sudut pandang baru human-centered (masalah lapangan di luar teknologi; alat = sarana belajar SIBI bagi pembelajar mendengar; empati perspektif tunarungu; belajar cepat) → folder markdown terpecah per bagian; push GitHub.

Work Log:
- Baca worklog Task 1-9 + DPJ-4 markdown lama + 06-referensi-isyarat (verified_refs.json 22 entri, gap-analisis, ruview-fitur) + panduan 09 sebagai basis.
- Riset web (4 batch): WHO World Report on Hearing 2021 (1,5 miliar/430 juta); BPS SUPAS2025 (prevalensi disabilitas 2,17%, kesulitan mendengar 0,41%); BPS Long Form SP2020 (22,97 juta; persen perlu verifikasi); BRIN-Kemenko PMK-UMM survei ekosistem bahasa isyarat 26 provinsi (BISINDO 77,7%, SIBI 1,9%, campuran 14,9%, lainnya 5,6%; "SIBI berkembang di sektor pendidikan formal"); Kamus SIBI Digital Kemendikdasmen (SK Mendikbud 0190/P/1994, Surat 868/C/U/95, KSD 2020, struktur kosakata Abjad/Imbuhan/Angka).
- Skrip persisten scripts/verify_dpj4_refs.py (Crossref bibliographic + retry backoff 429; save inkremental) → 8 DOI baru terverifikasi: Mitchell&Karchmer 2004 SLS 10.1353/sls.2004.0005 (>90% anak tunarungu lahir dari ortu mendengar); Ritmeester 2026 JDSDE 10.1093/jdsade/enaf059 (kesulitan orang mendengar belajar isyarat: urutan isyarat, pergeseran orientasi visual); Hassan 2026 CHI 10.1145/3772318.3791928 (permintaan belajar isyarat naik, AI feedback); Varry 2025 Galenical 10.29103/jkkmm.v4i3.22396 (akses kesehatan 64,7% kurang mudah); Zikky 2019 KASIBI 10.32487/jst.v5i2.732 (kamus SIBI input-only); Tristianto 2024 10.33506/insect.v10i2.4079 + JIKSI 2024 10.24912/jiksi.v12i2.31559 + Rabit 2026 10.36341/rabit.v11i2.8340 (SIBI 100% vision). Arsip: tool-results/dpj4-bahan/crossref/ + salinan di folder deliverable.
- Tulis 7 markdown di download/bahan-dpj4/ (isi EN hemat token, kalimat templat ID-READY untuk tempel ke proposal): 00-INDEX (peta + kebijakan bahasa + legenda status sumber); 01-masalah-lapangan (demografi, hambatan komunikasi keluarga/kesehatan, posisi resmi SIBI, bottleneck pembelajaran, lapisan empati + 4 kalimat masalah ID); 02-solusi-konsep-alat (3 persona, loop latihan cepat, tabel perbandingan pendekatan, non-klaim, one-liner manfaat); 03-metode-bahan (tahapan, gerbang Delta-CSI, kriteria pemilihan kosakata dari KSD, protokol dua kelompok G-A fasih/G-B pilot pembelajar opsional, pipeline CNN/LSTM, metrik, jadwal 16 minggu, biaya Rp300-700rb, risiko R1-R7, rumusan-tujuan-batasan baru); 04-referensi-bahan (8 DOI baru + rekap 22 lama per peran + 6 sumber resmi + peta klaim→sitasi); 05-kit-latar-belakang (corong 4 lapis, 6 paragraf ID-READY lengkap P1-P6, anti-pola, 3 opsi judul baru, peta penggantian draft lama); 06-disiplin-klaim-sibi (tensi BRIN 1,9% + 3 argumen pembelaan, pernyataan disiplin klaim v2, tabel frasa terlarang, risiko R7, checklist konsistensi).
- Mirror repo 11-bahan-dpj4/ (7 md + crossref JSON) + README diperbarui (bullet Folder 10-11); commit e6a9bef push main sukses (eaf1b84..e6a9bef).

Stage Summary:
- Bahan DPJ-4 human-centered lengkap: corong latar belakang baru berangkat dari masalah sosial/pendidikan (bukan "perkembangan teknologi"), alat diposisikan sebagai mitra latihan SIBI dengan umpan balik seketika bagi keluarga/guru/mahasiswa, empati diposisikan sebagai design intent (bukan klaim terukur).
- 8 referensi DOI baru melengkapi bank 22 lama; data resmi (BPS/BRIN/Kemendikdasmen/WHO) terkumpul dengan status verifikasi; tensi "SIBI hanya 1,9%" sudah punya skrip jawaban 3 argumen.
- Sisa human-owned: verifikasi persen BPS LFSP2020 22,97 juta sebelum dikutip, konfirmasi judul baru ke pembimbing, keputusan pilot pembelajar diadakan atau tidak, lalu regenerasi DPJ-4 DOCX dari kit ini.
