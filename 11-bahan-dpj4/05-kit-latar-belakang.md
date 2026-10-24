# 05 — KIT LATAR BELAKANG (rewriting §1.1 the human-centered way)

Purpose: paragraph-by-paragraph writing kit for the NEW `1.1 Latar Belakang`, honoring the owner's three requirements (field problem first; learner-first SIBI; empathy; fast learning). Style follows korpus TRSE UNM rules (skill proposal-writing v5 ref `03-language-patterns`): funnel structure, corong 4 lapis, one number per claim, sitasi [n], no "Perkembangan teknologi…" opener.

## 1. Funnel design (4 layers — invert of the old draft)

| Layer | Opens with | Key fact/citation | One sentence it must deliver |
|---|---|---|---|
| L1 Sosial (luar teknologi) | family & social reality of deafness | N1 (>90% born to hearing parents) | The burden of learning to communicate falls first on hearing families |
| L2 Pendidikan & layanan | school and service consequences | W4 (SIBI resmi SLB) + N4 (64,7% akses kurang mudah) | Society's answer is SIBI in schools, but service access stays hard because hearing counterparts cannot sign |
| L3 Bottleneck pembelajaran | how hearing people learn SIBI today | N2 (learning difficulties) + N5/W4 (dictionary-only aids) | Learning is slow because tools are input-only; no instant feedback on the learner's own gestures |
| L4 Solusi (teknologi paling akhir) | the device as practice partner | paradigm refs (SignFi, FSL'24) + ESP32 ref | Wi-Fi CSI on ESP32 = camera-free, private, cheap, instant-feedback practice tool; gap: never applied to SIBI |

## 2. Full paragraph skeleton (ID-READY — adapt freely, keep [n] mapping)

**P1 — L1 sosial** (3–5 sentences, no technology):
`Ketunarunguan bukan sekadar kehilangan pendengaran, melainkan ketidaksesuaian antara satu individu dan lingkungan yang sebagian besar berkomunikasi secara lisan. Lebih dari sembilan puluh persen anak tunarungu lahir dari orang tua yang mendengar [N1], sehingga keluarga justru menjadi pihak pertama yang dituntut mempelajari bahasa isyarat padahal mereka tidak memiliki pengalaman komunikasi visual. Kondisi ini menempatkan beban penyesuaian pada dua arah sekaligus: anak tunarungu harus berupaya memahami dunia yang berbicara, sementara orang-orang terdekatnya harus belajar berkomunikasi secara visual-manual yang sama sekali baru bagi mereka [N2].`

**P2 — L2 pendidikan** (3–5 sentences):
`Pemerintah telah menjawab kebutuhan komunikasi tersebut melalui pembakuan Sistem Isyarat Bahasa Indonesia (SIBI) sejak tahun 1994 melalui Keputusan Mendikbud Nomor 0190/P/1994, dan kini SIBI dipakai sebagai media komunikasi pembelajaran di sekolah luar biasa sesuai kaidah bahasa Indonesia yang baik dan benar [W4]. Namun, keberadaan bahasa pengantar resmi tidak otomatis menghadirkan orang yang mampu menggunakannya. Hambatan komunikasi masih mewarnai akses penyandang tunarungu terhadap layanan; survei pada penyandang disabilitas menunjukkan 64,7% responden menilai akses layanan kesehatan kurang mudah karena salah satu hambatan utamanya adalah komunikasi [N4]. Guru, calon guru, orang tua, dan teman sebaya adalah pihak yang paling dekat dengan persoalan ini, sekaligus pihak yang paling membutuhkan penguasaan SIBI.`

**P3 — L3 bottleneck (masalah pembelajaran)** (3–5 sentences):
`Proses belajar SIBI bagi orang mendengar sendirian menyimpan kesulitan yang khas. Penelitian terhadap orang tua mendengar yang belajar bahasa isyarat menunjukkan kesulitan khas bahasa berupa penguasaan urutan isyarat serta penyesuaian dari orientasi pendengaran ke orientasi visual [N2]. Di sisi lain, sarana belajar yang tersedia berhenti pada sisi masukan: Kamus SIBI Digital milik pemerintah dan aplikasi kamus semacam KASIBI memfasilitasi pencarian arti satu isyarat [W4, N5], tetapi tidak ada yang memberi tahu pembelajar apakah gerakan yang barusan dilakukan sudah benar. Akibatnya pembelajar bergantung pada kehadiran mitra latihan manusia yang tidak selalu tersedia, dan proses belajar menjadi lambat serta tidak pasti.`

**P4 — L4 solusi (teknologi masuk paling akhir)** (4–6 sentences):
`Berdasarkan permasalahan tersebut, penelitian ini mengusulkan sarana latihan bahasa isyarat SIBI berbasis Channel State Information (CSI) jaringan Wi-Fi pada mikrokontroler ESP32. CSI adalah informasi keadaan kanal pada sinyal Wi-Fi yang berubah ketika tubuh manusia bergerak di sekitarnya, sehingga gerakan lengan dan tangan pembelajar dapat diamati tanpa kamera dan tanpa sensor yang dipakaikan pada tubuh [ma2019_csur]. Pengenalan gestur terisolasi langsung dari pola CSI telah terbukti pada bahasa isyarat lain, antara lain 276 isyarat pada SignFi [ma2018_signfi] dan bahasa isyarat Filipina pada 2024 [baldeo2024_fsl], dengan perangkat sekelas ESP32 sebagai basis akuisisi [hernandez2020_esp32]. Kekurangan kamera justru menjadi keunggulan untuk konteks pembelajaran: latihan dapat dilakukan di rumah, ruang guru, atau pojok kelas tanpa keberatan privasi, dan biaya perangkat kecil sehingga mudah digandakan oleh sekolah. Hingga saat ini belum ada publikasi yang menerapkan pengenalan gestur berbasis Wi-Fi CSI untuk bahasa isyarat Indonesia, termasuk SIBI [gap refs].`

**P5 — empati (keunggulan kedua, setelah pembelajaran cepat)** (3–4 sentences):
`Sarana ini juga dimaksudkan sebagai jalan memahami sudut pandang tunarungu. Ketika pembelajar berlatih, mereka berada pada posisi yang selama ini dihuni tunarungu: mengandalkan gerakan visual sebagai sarana utama berkomunikasi dan menunggu umpan balik dari lawan bicara. Pengalaman langsung tersebut diharapkan menumbuhkan kepekaan terhadap kesulitan komunikasi yang dihadapi tunarungu sehingga kehadiran alat bantu teknologi berjalan seiring dengan tumbuhnya sikap inklusif pada lingkungan mendengar [N2, K4].`

**P6 — closing bridge ke rumusan** (2–3 sentences, corpus style):
`Berdasarkan uraian tersebut, diperlukan studi kelayakan yang menguji sejauh mana gestur SIBI dapat dikenali dari pola Wi-Fi CSI pada perangkat murah sekaligus sejauh mana sarana tersebut dapat dirasakan manfaatnya oleh pembelajar. Penelitian ini membatasi diri pada pengenalan gestur terisolasi pada kosakata SIBI dasar dan tidak menjanjikan penerjemahan kalimat secara kontinu. Rumusan masalah penelitian ini adalah ...`

## 3. Anti-patterns (do NOT do)

1. Jangan buka dengan "Perkembangan teknologi telah memengaruhi..." (the old draft's opener — explicitly rejected by owner).
2. Jangan mulai paragraf pertama dengan istilah teknis (CSI/ESP32/Doppler) — teknologi hanya masuk di P4.
3. Jangan menumpuk lebih dari satu angka dalam satu kalimat.
4. Jangan klaim alat ini "menumbuhkan empati" sebagai hasil terukur — posisikan sebagai harapan/desain intent (L5 empathy boundary in 01 §5).
5. Jangan tulis "penerjemah bahasa isyarat" tanpa kualifikasi studi kelayakan (claim discipline in 06).
6. Jangan sebut BISINDO lebih dari sekali sebagai konteks; lingkup adalah SIBI-only (06).

## 4. Title options (SIBI-only + learning-tool angle)

- **Utama**: `SARANA LATIHAN BAHASA ISYARAT SIBI BERBASIS WI-FI CHANNEL STATE INFORMATION PADA ESP32 UNTUK PEMBELAJAR MENDENGAR: STUDI KELAYAKAN PENGENALAN GESTUR TANPA KAMERA`
- **Alternatif 1**: `ALAT BANTU PEMBELAJARAN MANDIRI KOSAKATA SIBI DARI POLA WI-FI CSI: STUDI KELAYAKAN KLASIFIKASI GESTUR TERISOLASI PADA ESP32`
- **Alternatif 2**: `WI-FI CSI SEBAGAI UMPAN BALIK LATIHAN BAHASA ISYARAT SIBI BAGI KELUARGA DAN GURU PEMBELAJAR: STUDI KELAYAKAN TANPA KAMERA UNTUK LINGKUNGAN PENDIDIKAN`

Checklist for the final title: contains SIBI (not BISINDO), contains Wi-Fi CSI / Channel State Information, contains ESP32, contains studi kelayakan, does NOT promise "translasi/penerjemah" as deliverable, keeps "tanpa kamera" as differentiator.

## 5. Map to the old draft (what to replace in DPJ-4_Isyarat-SIBI-BISINDO.md)

| Old draft (current file) | New treatment |
|---|---|
| P1 opens "Perkembangan teknologi telah memengaruhi hampir semua sisi kehidupan..." | Replace with P1 sosial (kit §2) |
| P1 spends lines on SIBI vs BISINDO tension | Move to a single context clause; full handling in §1.4 batasan + 06 |
| No learner persona anywhere | Insert P3 bottleneck + P5 empathy |
| Solution paragraph starts from CSI physics | Solution paragraph now starts from field need, then names the device |
| Rumusan focused on "kelayakan translasi tanpa kamera" | Rumusan set in 03 §11 (learner-first wording) |
