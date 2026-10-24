# 02 — SOLUSI: KONSEP ALAT (learning-tool framing)

Purpose: material for BAB I §1.1 layer 4 + §1.2–1.5, and the concept sections of BAB II/III. The device is presented as a **practice partner / learning tool for SIBI learners**, not primarily as a communication aid for deaf people.

## 1. Concept statement (ID-READY, for §1.1 closing paragraph)

`Berdasarkan permasalahan tersebut, penelitian ini mengusulkan sebuah sarana latihan bahasa isyarat SIBI yang memanfaatkan Channel State Information (CSI) jaringan Wi-Fi pada mikrokontroler ESP32. Perangkat memantau gerakan tubuh dan tangan pembelajar melalui gangguan pada sinyal Wi-Fi, kemudian memberikan umpan balik seketika apakah gestur yang dilakukan cocok dengan kelas gestur yang sedang dilatih. Sarana ini tidak memakai kamera sehingga dapat dipakai di ruang kelas, musala sekolah, atau rumah tanpa keberatan privasi, dan perangkatnya murah sehingga berpotensi digandakan untuk sekolah-sekolah luar biasa.`

## 2. Three user personas (write ONE of these into §1.1; keep others in manfaat)

| Persona | Situation | What the device gives them | Empathy effect |
|---|---|---|---|
| P1 — Anggota keluarga mendengar (orang tua/saudara anak tunarungu) | >90% deaf children born to hearing parents (Mitchell & Karchmer 2004); must learn to sign while managing jobs/household | Practice at home, any hour, without scheduling a human partner; instant feedback on each gesture | Learns how much effort a "simple" conversation costs in a visual-manual language |
| P2 — Calon/pemula guru SLB dan mahasiswa PLB | SIBI is the mandated classroom medium (SK 0190/P/1994, Surat 868/C/U/95); teachers need fluency fast | Repetition-drill of the SIBI dictionary vocabulary with objective per-gesture feedback; can practice in the school itself | Internalizes the visual orientation of the classroom they will run |
| P3 — Mahasiswa umum / publik yang ingin belajar SIBI | Rising interest in sign-language education (Hassan 2026 CHI documents rising ASL enrollment; Indonesian analog) | Low-cost starter kit (2 ESP32) instead of camera rigs; privacy-safe in dorm/library | Steps into deaf communication mode as a learner, not as an observer |

## 3. The fast-learning loop (core mechanism to describe in §1.1 / §2.3)

```
[pilih kata SIBI dari daftar latihan]
   → [lakukan gestur di depan pasangan node Wi-Fi]
   → [ESP32 menangkap CSI → DSP → klasifikasi gestur]
   → [umpan balik seketika: benar / kelas lain / tidak terdeteksi]
   → [ulangi hingga akurat → lanjut kata berikutnya]
```

Why the loop is fast (arguments, each with a citation anchor):
1. **Feedback immediacy** — the learning bottleneck documented for hearing parents is adapting to a visual language without guidance (Ritmeester 2026); instant classification feedback directly addresses it.
2. **Zero setup friction** — no camera aiming, no lighting, no wearable; the learner just stands in the calibrated zone (consistent with RuView presence + calibration workflow).
3. **Privacy → willingness to practice** — camera-free sensing removes recording discomfort; this is the same privacy argument used for classroom RF sensing (Rodríguez-Correa 2023 for deaf AT; CSI surveys ma2019_csur / chen2023_csurxdom for privacy-preserving sensing).
4. **Availability** — dictionaries (KSD, KASIBI) give input only; a partner is not always available; the device is always-on and local (Zikky 2019 for the dictionary-only limitation; E5 for KSD book criticism).

## 4. Why Wi-Fi CSI and not the alternatives (comparison table for BAB II or §1.1)

| Approach | Examples in literature | Failure mode for THIS use case |
|---|---|---|
| Camera/vision recognition | All SIBI/BISINDO works (Sanjaya 2023 review; Tristianto 2024; JIKSI 2024; Rabit 2026; Dwijayanti 2021; Wiguna 2025) | Needs lighting + line-of-sight; records faces (children/classmates); makes home practice awkward |
| Data gloves / wearables | Classic SLR literature | Cost per learner, hygiene, unnatural for spontaneous practice |
| Kinect/depth or radar | High-end gesture studies | Expensive, single-device setup, not replicable per classroom |
| **Wi-Fi CSI (chosen)** | SignFi (276 ASL signs), DF-WiSLR (30+19), FSL-TENCON 2024, Widar3.0 | Chosen: commodity ESP32 (~tens of thousands Rupiah/node), camera-free, private, already proven for isolated gesture classification — but never applied to SIBI (gap) |

`ID-READY gap sentence: "Hingga saat ini belum ada publikasi yang menerapkan pengenalan gestur berbasis Wi-Fi CSI untuk bahasa isyarat Indonesia, termasuk SIBI yang menjadi bahasa pengantar resmi pembelajaran di sekolah luar biasa."`

## 5. Non-claims (carry from ruview-fitur-isyarat.md, adapted to learning-tool scope)

The device in this proposal is a **feasibility-stage classification tool**:
- It classifies **isolated gestures** (5–12 SIBI vocabulary items), one signer per session, in a calibrated room.
- It does NOT: translate continuous sentences, extract hand skeletons, identify persons, count people, or guarantee cross-room accuracy without recalibration.
- "Translasi/penerjemah" appears only as the long-term direction; the semester deliverable is feasibility + mini-dataset + confusion-matrix report.
Full updated statement: see `06-disiplin-klaim-sibi.md`.

## 6. Solution one-liners (ID-READY, per persona — for §1.5 manfaat praktis)

- P1: `Bagi keluarga mendengar yang memiliki anggota tunarungu, alat ini menjadi mitra latihan isyarat di rumah yang tersedia setiap saat tanpa menuntut kehadiran orang lain.`
- P2: `Bagi guru dan calon guru SLB, alat ini menjadi sarana penguatan kosakata SIBI dengan umpan balik objektif sehingga penguasaan isyarat pembelajaran dapat ditingkatkan lebih cepat.`
- P3: `Bagi masyarakat umum yang tertarik belajar SIBI, alat ini menawarkan pengalaman berlatih yang memperkenalkan cara komunikasi visual yang menjadi keseharian tunarungu.`

## 7. What "success" looks like for the feasibility study (bridges to BAB III)

1. Technical: per-gesture classification accuracy ≥ 80–90% in-domain (literature benchmark range), confusion matrix reported per class.
2. Data contribution: documented protocol + mini-dataset CSI SIBI (first of its kind — R2 in gap analysis).
3. Learning-side (optional small pilot): 3–5 hearing learners, qualitative usability notes + time-to-first-correct-recognition per session; reported as preliminary observation, NOT a learning-effect claim.
4. Empathy-side: reported only as design intent with literature support (see 01 §5); explicitly listed in "tidak membahas" if pembimbing pushes for measurement.
