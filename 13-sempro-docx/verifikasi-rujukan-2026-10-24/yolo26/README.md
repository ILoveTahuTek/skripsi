# Verifikasi rujukan YOLO26 (ralat MediaPipe -> YOLO26 pose, 25 Okt 2026)

Tiga rujukan baru dipakai menggantikan BlazePose / MediaPipe Hands / Kim dkk. 2023
(yang dihapus dari daftar pustaka karena tidak lagi relevan dengan metode).

## [33] jocher2026 — Ultralytics YOLO26 (paper resmi)
- Sumber: laman abstrak arXiv https://arxiv.org/abs/2606.03748 (dilihat 25 Okt 2026).
- Judul: "Ultralytics YOLO26: Unified Real-Time End-to-End Vision Models".
- Penulis: Glenn Jocher, Jing Qiu, Mengyu Liu, Shuai Lyu, Fatih Cagatay Akyon,
  Muhammet Esat Kalfaoglu (tim Ultralytics).
- Dikirim 2 Juni 2026; DOI 10.48550/arXiv.2606.03748.
- Kutipan abstrak (terkait pose): "Beyond detection, YOLO26 introduces task-specific
  head and loss designs for instance segmentation, pose estimation, and oriented
  detection, producing consistent gains across tasks and scales. The family spans
  five scales (n/s/m/l/x) and supports detection, instance segmentation, pose
  estimation, classification, and oriented detection in a single pipeline."
- Klaim di naskah yang bersandar: keluarga model visi waktu nyata Ultralytics,
  multi-tugas termasuk estimasi pose, inferensi NMS-free.
- Verifikasi tambahan: Roboflow "What Is YOLO26?" (Jan 2026) — YOLO26 keluarga
  multi-tugas NMS-free ukuran Nano..Extra Large, sampel benchmark konsisten.

## [52] sapkota2025 — analisis arsitektur independen
- Sumber: laman abstrak arXiv https://arxiv.org/abs/2509.25164 (dilihat 25 Okt 2026).
- Judul: "YOLO26: Key Architectural Enhancements and Performance Benchmarking for
  Real-Time Object Detection".
- Penulis: Ranjan Sapkota, Rahul Harsha Cheppally, Ajay Sharda, Manoj Karkee.
- v1 29 Sep 2025 (v5 16 Mar 2026); DOI 10.48550/arXiv.2509.25164.
- Kutipan abstrak (terkait klaim naskah): "YOLO26, released in September 2025, ...
  purpose-built to deliver efficiency, accuracy, and deployment readiness on edge
  and low-power devices." + "positions YOLO26 as a multi-task framework, supporting
  object detection, instance segmentation, pose/keypoints estimation, oriented
  detection, and classification."
- Klaim di naskah yang bersandar: dirancang untuk efisiensi inferensi dan
  kesiapan penerapan pada perangkat tepi (edge).

## [51] ultralyticspose — dokumentasi resmi tugas pose
- Sumber: https://docs.ultralytics.com/tasks/pose/ (diambil 25 Okt 2026).
- Kutipan verbatim: "The default YOLO26 Pose models predict the 17 COCO keypoints";
  "YOLO26 Pose models pretrained on the COCO keypoints dataset"; varian tercantum
  YOLO26n/s/m/l/x-pose; "Exported models can be deployed on edge devices for
  real-time applications".
- Klaim di naskah yang bersandar: 17 keypoint tubuh format COCO per orang,
  tanpa keypoint jari; varian model; terlatih pada dataset keypoint COCO.

## Fakta pendukung RuView (tidak berubah, commit fefb0f9)
- scripts/collect-ground-truth.py (ADR-079) memakai MediaPipe PoseLandmarker dan
  mengonversi 33 landmark -> 17 keypoint COCO per frame (baris 2-7, 49 skrip):
  "Captures webcam keypoints via MediaPipe PoseLandmarker (Tasks API) ...
  Output: JSONL file in data/ground-truth/ with per-frame 17-keypoint COCO poses."
- Konsekuensi bagi naskah: penggantian estimator ke YOLO26 mempertahankan format
  keluaran (17 keypoint COCO) sehingga pola sinkronisasi ADR-079 tetap berlaku;
  MediaPipe kini hanya disebut sebagai fakta repositori (rujukan [49]).

## Catatan metode
- arXiv API (export.arxiv.org) terblokir dari lingkungan kerja (respons kosong);
  metadata kedua paper diverifikasi dari laman abstrak arXiv yang ditampilkan
  lengkap (judul, penulis, tanggal, DOI) pada hasil penelusuran web 25 Okt 2026.
- Dokumentasi Ultralytics diverifikasi dengan pengambilan laman langsung.
