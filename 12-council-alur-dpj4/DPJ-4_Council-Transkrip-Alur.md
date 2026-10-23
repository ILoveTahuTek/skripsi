# TRANSKRIP LLM COUNCIL — ALUR METODE DPJ-4 (SIBI-ONLY)

**Pertanyaan yang diaudit dewan:** Apakah alur dua tahap (vision pose estimation sebagai guru → distilasi/transfer ke model Wi-Fi CSI RuView) tepat untuk proposal skripsi studi kelayakan 1 semester (pengenalan 5–12 isyarat SIBI dari CSI ESP32, kamera hanya saat pelabelan dataset, tujuan non-teknis: alat belajar SIBI yang cepat bagi pendengar + menumbuhkan empati terhadap perspektif tunarungu)? Sub-pertanyaan: (a) MediaPipe vs YOLO; (b) finger keypoints & ekspresi wajah dari CSI realistis?; (c) distilasi pose vs klasifikasi langsung vs hybrid; (d) koneksi ke tujuan pembelajaran/empati; (e) risiko terbesar + gerbang go/no-go.

**Metode:** 5 advisor paralel (perspektif berbeda) → peer review anonim 5 penilai (A–E, pemetaan acak: A=Expansionist, B=Executor, C=Contrarian, D=Outsider, E=First Principles) → sintesis chairman. Putusan chairman terdokumentasi di `DPJ-4_Bahan-Proposal-SIBI.md` §7.

---

## RONDE 1 — RESPON ADVISOR

### The Contrarian (C)

Cacat #1 — guru hebat untuk murid yang buta pada materi itu. Alur memerintahkan guru vision (jari + wajah) mengajari CSI hal yang secara fisika tak bisa ia lihat. Resolusi 2–3 ESP32 tidak menembus artikulasi jari; bahkan pipeline RuView yang sudah jadi hanya mencapai PCK@20 59,5% pada 17 keypoint **tubuh**. DensePose-from-WiFi pun bekerja di level region tubuh, bukan sendi jari. Jawaban (b): **tidak realistis, titik.** (a): bila guru dipaksakan ada, MediaPipe — sudah terintegrasi RuView, nol biaya latihan; YOLO butuh pelatihan ulang yang tidak masuk anggaran waktu.

Cacat #2 — tujuan dan teknologi saling membantah. Alat belajar SIBI untuk **pendengar** tidak butuh bebas-kamera: penggunanya bukan tunarungu, argumen privasi gugur. Webcam + MediaPipe hari ini sudah menghasilkan alat belajar yang berfungsi. CSI menambah berbulan-bulan risiko demi kebutuhan yang tidak diminta siapa pun. Pertanyaan yang dihindari: *kenapa harus CSI?* (d): dengan desain sekarang, "alat pembelajaran + empati" hanyalah dekorasi di atas studi kelayakan pipeline — hubungan ini retak dan penguji akan menempel di situ.

Cacat #3 — SIBI 1,9%. Menumbuhkan empati lewat varian yang 98% komunitas tuli tidak pakai sehari-hari adalah jembatan ke pulau kosong. Siapkan pembelaan atas pilihan ini, jangan anggap final.

(c): distilasi pose penuh **tidak layak** satu semester; hybrid lebih tidak. Satu-satunya jalur jujur: klasifikasi langsung 5–12 isyarat yang **dibedakan lintasan lengan/tubuh**, bukan konfigurasi jari — di atas pipeline RuView yang sudah terbukti, tanpa membangun guru baru.

(e) Risiko terbesar: minggu terbuang melatih guru yang targetnya mustahil diprediksi muridnya. Gerbang minggu ke-6: PCK keypoint lengan < 60% atau akurasi 5 isyarat kasar < 80% → mundur ke kamera-supervised, tulis kelayakan apa adanya. Skripsi kecil yang benar lebih baik daripada proposal megah yang mati di BAB III.

### The First Principles Thinker (E)

Dewan bertanya arsitektur mana yang tepat. Pertanyaan pertamanya sudah salah: ini bukan soal arsitektur, tapi soal klaim minimum yang bisa diverifikasi jujur dalam satu semester. Studi kelayakan menghasilkan keputusan terukur, bukan sistem jadi.

Dari fondasi, tiga koreksi:

**1. Alur dua tahap itu bukan gagasan baru Anda — jangan duplikasi.** RuView sudah mempraktikkan persis skema itu: guru MediaPipe, murid CSI (PCK@20 59,5% vs baseline 50%). Jadi untuk (a): bukan MediaPipe vs YOLO; keduanya salah karena melatih guru baru = pemborosan semester. Pakai guru yang sudah diaudit; kontribusi Anda menginstansiasinya untuk SIBI.

**2. Pertanyaan (b) bertentangan dengan fisika.** Gelombang 2,4/5 GHz panjangnya 6–12 cm; dengan 2–3 node, konfigurasi jari dan ekspresi wajah berada jauh di bawah resolusi spasial. Jangan tanya "bagaimana memprediksi jari dari CSI" — tanya "isyarat SIBI mana yang terpisahkan hanya lewat lintasan lengan, torso, kepala". Kurasi 5–12 isyarat berbasis separabilitas fisik, bukan sekadar kurikulum.

**3. Untuk (c): klasifikasi langsung pada himpunan tertutup 5–12 kelas.** Itu jalur satu semester yang jujur. Hybrid minimal layak: CSI→pose atas-tubuh terawasi guru, klasifier di atasnya. Distilasi representasi penuh: tunda.

**(d)** Tujuan pemilik menentukan output alat: umpan balik benar/salah latihan tanpa kamera bagi orang tua pendengar (90–95% kasus). Itu butuh keputusan kelas, bukan skeleton utuh — arsitektur mengikuti tujuan, bukan sebaliknya.

**Risiko terbesar bukan teknis:** SIBI-only berlawanan dengan lapangan (77,7% BISINDO). Alat empati yang mengajarkan sistem yang tak dipakai komunitas adalah kontradiksi yang harus diakui terbuka di BAB I, bukan disembunyikan.

**Gerbang go/no-go:** setelah data terkumpul, ukur PCK@20 split terpisah sendiri. ≤55% (mendekati baseline) → pangkas ke isyarat lintasan-dominan atau klasifikasi langsung. Satu gerbang, satu angka, keputusan.

### The Expansionist (A)

Sudut yang tidak dilihat orang: ini bukan skripsi "pengenalan isyarat", ini **mesin penghasil dataset isyarat tanpa kamera**. Pipeline camera-supervised RuView berarti setiap sesi latihan otomatis menghasilkan data berlabel. Yang lain melihat "dataset kecil 5–12 isyarat" sebagai batasan; saya melihat infrastruktur yang setiap hari bertambah sendiri. Itu aset yang dinilai murah sekarang.

**The wedge untuk tujuan empati:** orang pendengar malu berlatih SIBI di depan kamera webcam. Bebas-kamera bukan sekadar syarat operasional — dia fitur pembunuh: latihan SIBI di kamar, tanpa diawasi, tanpa rasa dihakimi. Tidak ada produk berbasis vision yang bisa menawarkan ini. Jika alur dua tahap bekerja, kalian memegang positioning yang tidak bisa ditiru aplikasi kamera mana pun.

**Jawaban cepat (a)–(e) dari sisi upside:** MediaPipe sudah tertanam di RuView — pakai itu, jangan buang waktu ke YOLO. Jari & wajah dari CSI? Jangan diprediksi langsung dari CSI — pakai hybrid: CSI memprediksi pose tubuh/lengan kasar (PCK@20 59,5% sudah membuktikan sinyal ada), detail jari jadi lapisan pembelajaran terpisah. Pilih distilasi pose, bukan klasifikasi per-kelas: representasi pose berarti kosakata bisa tumbuh tanpa melatih ulang classifier dari nol — arsitektur yang siap skala.

**Yang diremehkan:** SIBI cuma 1,9% pengguna, tapi SIBI-only justru pantai landai yang tepat — sekolah formal punya kurikulum, guru, dan anggaran. Jika pipeline bekerja untuk SIBI, modul BISINDO tinggal retraining, bukan redisain.

**Jika berhasil lebih dari ekspektasi:** kontribusi upstream ke RuView (referensi implementasi camera-free pertama untuk isyarat), demo yang bisa direplikasi sekolah daerah dengan 2–3 ESP32 murah, dan pola distilasi vision→CSI yang bisa dipakai ulang untuk rehabilitasi, terapi wicara, gerak vokasional.

Next action: framing proposal sebagai "platform latihan mandiri SIBI berprivasi", dengan studi kelayakan sebagai Bukti Konsep 0 — bukan tujuan akhir.

### The Outsider (D)

Saya awam total. Ini pertanyaan-pertanyaan "bodoh" yang terbaca langsung dari proposal:

**1. Kenapa harus Wi-Fi?** Saya sebagai calon pengguna tidak peduli apakah alat memakai kamera atau radio. Saya isyarat, alat bilang benar/salah — pengalamannya identik. Webcam lebih murah, lebih akurat, dan sudah terbukti jalan (PCK 59,5% vs 50%). Kalau satu-satunya jawaban "karena RuView punya pipeline-nya", itu alasan teknisi, bukan alasan masalah. BAB I wajib memuat satu kalimat justifikasi bebas-kamera yang bisa dipahami pembimbing non-teknis — kalau tidak, ini teknologi mencari masalah.

**2. Di mana orang tuli di proyek ini?** Subjeknya guru/pembina (pendengar). Validatornya siapa? Sebuah alat belajar bahasa isyarat tanpa satu pun penutur aslinya ikut memvalidasi bentuk isyarat itu... ironi sekaligus pelanggaran terhadap tujuan empatinya sendiri. Minta minimal satu penutur sebagai validator isi — murah, dan menyelamatkan kredibilitas.

**3. Angka 1,9% itu membela SIBI atau membongkarnya?** Awam membaca survei BRIN begini: 77,7% komunitas pakai BISINDO, SIBI 1,9%. Kesimpulan spontan saya: alat ini mengajarkan bahasa yang tidak dipakai komunitasnya. Argumen "SIBI dipilih karena konteks pembelajaran formal bagi pendengar" harus eksplisit dan berdiri sendiri, bukan disimpan sebagai catatan kaki.

**4. Alat dengan 5–12 kata itu apa?** Kamus 12 kata — itu demo atau alat belajar? Setelah memakainya, apa yang saya bisa lakukan yang sebelumnya tidak bisa? Satu skenario pemakaian konkret (siapa, di mana, kapan) harus ada di BAB I.

**5. "Empati" itu diukur apa?** Kalau cuma klaim, hapus atau operasionalkan (misal pre/post kuesioner sederhana pada guru).

Saran alur teknis serahkan pada ahli; tugas proposal ini adalah menjawab lima pertanyaan di atas sebelum berani menyentuh ESP32.

### The Executor (B)

Alur dua tahap Anda bukan pertanyaan desain — itu sudah jalan setengah jadi di RuView. Pipeline ADR-079 (MediaPipe PoseLandmarker tersinkron dengan CSI, script collect-ground-truth.py) sudah ada. Jadi pekerjaan Senin pagi bukan merancang arsitektur: clone RuView, jalankan collect-ground-truth.py dengan 2 ESP32, replikasi hasil audit (PCK@20 59,5%) di ruang sendiri. Kalau tidak bisa direplikasi dalam 2 minggu, proposal ini mati sebelum ditulis.

(a) MediaPipe vs YOLO — pertanyaan salah. MediaPipe sudah terintegrasi RuView. Ganti guru = bangun ulang pipeline = bakar satu semester. Pakai MediaPipe, titik.

(b) Jari & ekspresi wajah dari CSI: tidak realistis. 2–3 node ESP32 tidak punya resolusi spasial untuk jari. Jangan jadikan target prediksi; tulis sebagai keterbatasan. Cakupan: tubuh atas + lengan.

(c) Satu semester = klasifikasi kelas isyarat langsung. 5–12 kelas × 30 repetisi adalah masalah klasifikasi standar, terukur, bisa dievaluasi jujur. Distilasi pose sudah "dibayar" RuView; hybrid berarti dua proyek sekaligus — gagal dua-duanya. Framing proposal: "klasifikasi isyarat SIBI dari CSI, pose vision sebagai ground truth pelabelan".

(d) Fitur pembelajaran SIBI: feedback loop minimal — pengguna mengisyaratkan, sistem menjawab "benar/salah, isyarat yang terdeteksi X". Itu sudah memenuhi tujuan pemilik. Jangan janji lebih dari itu di proposal.

(e) Gerbang keputusan: G1 (minggu 3) — data satu isyarat, sinyal CSI bisa membedakan antar repetisi? G2 (minggu 6) — akurasi klasifikasi di atas peluang (mis. >25% untuk 4 kelas) pada split terpisah. Gagal G2: turunkan ke 3–5 isyarat atau ubah penempatan node — jangan memaksakan alur.

Jangan tulis angka akurasi target di proposal (riwayat klaim 92,9% ditarik). Jual "bukti konsep". Jangan sentuh modul pose on-device yang masih stub — itu lubang waktu.

---

## RONDE 2 — PEER REVIEW (ANONIM A–E)

### Review 1 (lensa Contrarian)

1. Terkuat: **B** — satu-satunya yang mengubah debat arsitektur menjadi uji ketergantungan: replikasi PCK@20 dalam 2 minggu sebagai gerbang hidup-mati, G1/G2 terukur, dan larangan menulis target akurasi (pelajaran dari klaim 92,9% yang ditarik).
2. Blind spot terbesar: **A** — penuh overclaiming ("mesin penghasil dataset", "modul BISINDO tinggal retraining"), tanpa satu pun gerbang go/no-go; klaim "bebas-kamera = fitur pembunuh" hipotesis pasar yang tak pernah diuji.
3. Semua lewatkan: generalisasi lintas pengguna/ruangan (split temporal bisa lolos padahal alat gagal di kamar pengguna); segmentasi isyarat kontinu; ambang kualitas label guru.

### Review 2 (lensa First Principles)

1. Terkuat: **E** — menyerang akar masalah dengan fisika lalu mengubah kegagalan jadi metode (kurasi separabilitas); gerbang kuantitatif jelas; risiko non-teknis diakui.
2. Blind spot terbesar: **A** — tanpa gerbang; "jari lapisan terpisah" melanggar logika informasi; premis malu-kamera tak diuji.
3. Semua lewatkan: flywheel pelabelan otomatis cacat secara logika — pemula mengisyaratkan SALAH, MediaPipe memberi ground truth atas isyarat salah, model mempelajari kesalahan; tanpa validasi penutur asli atas data latih; tak ada protokol evaluasi lintas-pengguna/ruangan.

### Review 3 (lensa Expansionist)

1. Terkuat: **A** — flywheel dataset berlabel otomatis + wedge "berlatih tanpa diawasi" = diferensiator yang tak bisa ditawarkan produk vision.
2. Blind spot terbesar: **C** — isunya kenyamanan pendengar, bukan privasi tunarungu; fallback C menghapus satu-satunya pembeda proyek; lensa risiko membunuh peluang.
3. Semua lewatkan: generalisasi lintas-pengguna/ruang (gerbang "pengguna baru tanpa rekoleksi"); kurasi isyarat harus menggabungkan separabilitas fisik (E) + kosakata pedagogis divalidasi penutur tunarungu (D); tak ada yang mengukur hasil belajar pengguna.

### Review 4 (lensa Outsider)

1. Terkuat: **D** — lolos uji logika awam ("kenapa Wi-Fi?" dan "di mana orang tuli?").
2. Blind spot terbesar: **A** — menjual privasi padahal pengguna pendengar; kosakata tumbuh tanpa bukti; tanpa gerbang.
3. Semua lewatkan: paradoks privasi Wi-Fi (terasa "diintip lewat dinding" — wajib diuji persepsinya); tak ada uji pre/post hasil belajar; izin etik/persetujuan subjek tak disebut.

### Review 5 (lensa Executor)

1. Terkuat: **B** — aksi Senin pagi; gerbang bertanggal; rencana mundur konkret; larangan eksplisit. E nyaris setara tapi tanpa langkah minggu pertama.
2. Blind spot terbesar: **A** — tidak menjawab (e); "jari lapisan terpisah" tak dieksekusi dan terbantahkan fisika.
3. Semua lewatkan: protokol generalisasi CSI lintas ruang/pengguna (leave-one-room-out; jumlah ruangan & partisipan); anggaran minggu per gerbang dipetakan ke bab skripsi; metrik keberhasilan alat belajar sendiri (instrumen empati/belajar).

---

## RONDE 3 — PUTUSAN CHAIRMAN

Ringkasan putusan (versi lengkap dan rancangan turunannya terdokumentasi di dossier §4 dan §7):

- **Verdict:** alur dua tahap TEPAT sebagai infrastruktur pelabelan; TIDAK TEPAT sebagai tulang punggung metodologis satu semester. Guru visi (MediaPipe) mencetak label kelas; murid CSI = klasifikator langsung himpunan tertutup 5–8 kelas; distilasi pose penuh = kerja lanjutan.
- **Alur final:** T0 replikasi (G0 PCK@20 ≥ 55%) → T1 kurasi dua saringan + validator tunarungu → T2 pelabelan guru + klasifikasi langsung (G2 ≥ 70% dalam-partisipan) → T3 generalisasi (G3 ≥ 50%; leave-one-room-out + pengguna baru) → T4 kemasan alat belajar (G4 pre/post + persepsi privasi + persetujuan validator) → T5 penulisan temuan.
- **Satu hal pertama:** Senin pagi replikasi pipeline ADR-079; keputusan G0 dikunci Jumat pekan kedua; paralel: undang calon validator tunarungu.

**Pemetaan respons → persona:** A = The Expansionist; B = The Executor; C = The Contrarian; D = The Outsider; E = The First Principles Thinker.
