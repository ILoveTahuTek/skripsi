# 06 — DISIPLIN KLAIM & LINGKUP SIBI-ONLY (update for the new framing)

Purpose: keep the honesty discipline of the previous DPJ lines while adapting it to the learner-first, SIBI-only scope; includes the BRIN-data tension and its defense script.

## 1. The BRIN tension (prepare this BEFORE any examiner asks)

**The tension:** BRIN 2026 survey reports only **1.9%** of deaf respondents use SIBI vs **77.7%** BISINDO (W5; survey: 26 provinces, purposive, explicitly "tidak menggambarkan keterwakilan secara nasional"). An examiner may ask: "why build a SIBI tool nobody uses?"

**Defense (three honest arguments):**
1. **Official education anchor**: SIBI is the standardized system mandated for formal deaf education (SK Mendikbud 0190/P/1994; Surat 868/C/U/95; Kemendikdasmen's own KSD continues it — W4). BRIN itself states "SIBI berkembang di sektor pendidikan formal" (W5). The device targets the **learners around formal education** (teachers, teacher candidates, parents connected to schools) — exactly where SIBI lives.
2. **Measurability for a feasibility study**: SIBI has a single official dictionary (KSD) with discrete vocabulary units (E6), which makes gesture-class definitions unambiguous — necessary for a 1-semester classification study. A community/natural language with regional variation is a poor first target (this is why FSL 2024 chose a standardized corpus too).
3. **Long-term interoperability**: BRIN recommends BISINDO–SIBI interoperability (W5); an SIBI-trained pipeline with a documented dataset is the first brick; BISINDO adaptation is future work.

`ID-READY sentence for §1.4/§2.4: "Meskipun survei ekosistem bahasa isyarat menunjukkan BISINDO lebih dominan di komunitas tuli, SIBI tetap menjadi sistem yang dibakukan untuk pembelajaran formal di sekolah luar biasa dan memiliki kamus resmi, sehingga dipilih sebagai lingkup studi kelayakan ini [W4, W5]."`

## 2. Updated claim discipline statement (ID-READY — replaces the v1 statement)

> Penelitian ini merupakan studi kelayakan pengenalan gestur terisolasi bahasa isyarat SIBI dari pola Wi-Fi CSI pada ESP32, diposisikan sebagai sarana latihan bagi pembelajar mendengar (keluarga, guru, dan mahasiswa). Penelitian ini tidak mengklaim: (a) ekstraksi pose atau kerangka tangan; (b) penerjemahan kalimat bahasa isyarat secara kontinu; (c) pengenalan multi-penandatangan simultan; (d) keakuratan lintas-ruang tanpa kalibrasi ulang; (e) efektivitas pembelajaran atau pertumbuhan empati sebagai hasil terukur. Kosakata diuji pada 5–12 gestur SIBI dasar dari Kamus SIBI Digital yang dominan bergerakkan lengan, dengan satu penandatangan per sesi, di ruang terkalibrasi. Uji coba pembelajar (bila dilaksanakan) bersifat observasi awal penggunaan, bukan pengukuran efek pembelajaran. Gerbang fisik Delta-CSI dua ESP32 di lokasi target pada minggu awal tetap menjadi titik go/no-go.

## 3. Vocabulary of forbidden phrasings (carry + new)

| Forbidden | Use instead |
|---|---|
| "penerjemah bahasa isyarat" (as deliverable) | "sarana latihan pengenalan gestur terisolasi" / "studi kelayakan" |
| "mengenali SIBI dan BISINDO" | "mengenali gestur SIBI" (BISINDO only as context, once) |
| "alat ini membuat pengguna berempati" | "diharapkan menumbuhkan kepekaan" (design intent) |
| "pembelajaran lebih cepat terbukti" | "umpan balik seketika dirancang untuk mempercepat latihan" |
| "ekstraksi pose tangan dari WiFi" | "klasifikasi langsung dari pola CSI" |
| "akurasi tinggi di semua ruangan" | "akurasi pada ruang terkalibrasi; laporan antar-domain" |

## 4. Risk table (updated for learner-first scope)

| ID | Risk | Mitigation |
|---|---|---|
| R1 | Cross-domain collapse (room/person/device changes) | Two-domain experiment design; per-subject split; report cross-domain accuracy as core finding (chen2023_csurxdom, Widar3.0) |
| R2 | No existing SIBI CSI dataset/baseline | Produce protocol + mini-dataset as primary contribution; publish it |
| R3 | ESP32 CSI quality limits vs Intel5300-era studies | Claim acquisition feasibility only; off-device processing; Delta-CSI physical gate week-3 |
| R4 | Kinematically similar SIBI gestures inseparable | Vocabulary chosen for kinematic distinctness; confusion matrix reported (FSL'24, Wi-SL strategy) |
| R5 | Ethics of data with children/schools | Parent consent, teacher asentasi, anonymization, camera-free advantage (Rodríguez-Correa'23) |
| R6 | Learning-tool validity limited (pilot only) | Position as feasibility; learning claims limited to preliminary observation; empathy claims = design intent |
| R7 | Examiner challenge "SIBI used by only 1,9%" (BRIN) | Defense script §1 (education anchor + measurability + interoperability roadmap) |

## 5. Consistency checklist for the whole document

1. Title, rumusan, tujuan, batasan, and BAB III all say **SIBI** (no BISINDO in scope sentences).
2. The word "translasi" appears only inside qualified phrases ("arah pengembangan lanjutan", "tidak dibahas").
3. Every number has exactly one citation and matches the bank in `04-referensi-bahan.md`.
4. BRIN survey always cited **with** its non-representative caveat.
5. Empathy always framed as design intent/expected benefit, never as measured outcome.
6. The learner pilot (if included) appears as optional in batasan.
7. EYD-V clean per skill naskah-id (`periksa.py`) — run before delivery.
