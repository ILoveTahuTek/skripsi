# 07 — Claim Discipline (WiFi-CSI / RuView lineage)

Purpose: the document never promises anything unproven — advisors test claims, not
hopes. Sources: RuView deep exploration (01-ruview-exploration/), code verification,
verified-literature gap analysis (06-referensi-isyarat/), owner scope decisions.

## 1. Core rules

1. **Every claim is bounded by "studi kelayakan"** (feasibility study). Write
   "menguji kelayakan", "mengevaluasi kemampuan", "menghasilkan dataset dan
   rekomendasi" — never "membangun sistem jadi yang …".
2. **RuView 17-keypoint pose = stub (PCK@20 ≈ 3%).** Forbidden: promising pose/hand-
   skeleton extraction. Correct paradigm: **classifying gestures directly from CSI
   patterns** (precedents: SignFi 2018; DF-WiSLR 2020; Widar3.0 2021; FSL-CSI TENCON 2024).
3. **Physical Delta-CSI gate (2×ESP32) = early go/no-go.** Every schedule must place
   the two-node physical test at the target location as a continue/stop/pivot decision
   point (week ~3).
4. **Risk + mitigation + fallback per risk** in the risk subsection (02 §BAB III).

## 2. Claim bounds per case

| Case | May claim | Must NOT claim |
|---|---|---|
| Broiler coop | flock activity index (feasibility), public dataset, change alerts | individual bird ID, disease diagnosis, chicken heart rate (band 2× off) |
| SLB classroom | class presence/motion, anomaly/fall detection (tuned threshold), privacy-preserving | accurate person count >2–3, individual identity, clinical behavior assessment |
| SLB dormitory | coarse sleep pattern, night anomaly alerts for companions | clinical hypnogram, apnea screening, multi-occupant |
| Sign language (**SIBI-only scope**) | feasibility of isolated-gesture classification, 5–12 dominant arm-motion classes, first CSI dataset for **SIBI** | continuous translator, hand-pose extraction, multi-signer, cross-space generalization without calibration |

## 3. SIBI-only decision (owner, current lineage)

The sign-language case is scoped to **SIBI only, without BISINDO** (owner decision):
formal standard code, word order follows Indonesian, manageable dataset load for one
semester. Writing rules that follow from it:

- Write `bahasa isyarat SIBI` throughout; do NOT alternate `SIBI/BISINDO` phrasings.
- **BISINDO is still citable** in BAB II as landscape/gap evidence (no CSI publication
  exists for either system) — but as background, not as the target system.
- Novelty claim stays two-layered: (a) no CSI-based research exists for SIBI **or**
  BISINDO (landscape), (b) this research targets SIBI specifically.
- Trap to avoid: any sentence that implies the system handles both systems.

## 4. Discipline statement template (insert at end of 1.4)

> Penelitian ini merupakan studi kelayakan [kasus] berbasis Wi-Fi Channel State Information pada platform RuView (capture, DSP, alert). Penelitian ini tidak mengklaim [daftar hal yang tidak diklaim]. Kelayakan diuji pada [lingkup terbatas], dengan [asumsi keras]. Uji fisik Delta-CSI 2×ESP32 pada lokasi target menjadi titik go/no-go penelitian.

## 5. Ethics (when humans involved, especially children)

Parent/guardian + institution consent + right to withdraw, stated in 1.4. System
position: condition detection for companions, NOT behavior surveillance. Camera only
for ground-truth labeling during dataset recording; runtime is camera-free. Wi-Fi
sensing does not identify individuals (gap ≈0.0005) — use as privacy-by-design evidence.

## 6. Permitted novelty claims (from verified gap analysis)

- Combinational firsts: [target language/case] + [platform] + [context].
- A public labeled dataset contribution.
- Calibration of sensing parameters for a new population (children, small flocks).

## 7. When writing about RuView

Describe as "platform open-source capture CSI + DSP + alert berbasis ESP32" with the
repo reference. MEASURED features may be cited; STUB features (pose, apnea) may only
appear as "tidak digunakan / di luar lingkup". Feature map:
repo `06-referensi-isyarat/ruview-fitur-isyarat.md`.
