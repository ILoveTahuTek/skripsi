#!/usr/bin/env python3
"""Unduh rujukan terbuka Daftar Pustaka v10 (94 entri) ke folder referensi/.
Status per entri: TERUNDUH / PERAMBAN (gratis tapi blokir unduhan otomatis) / BERBAYAR / HALAMAN."""
import subprocess, os, sys, json

OUT = "/home/z/my-project/download/sensesibi-v10/referensi"
os.makedirs(OUT, exist_ok=True)

def fn(n, key, ext): return f"ref-{n:02d}_{key}.{ext}"

# (nomor, kunci, ekstensi, [url fallback...], mode)
# mode: pdf -> simpan bila %PDF; html -> simpan apa adanya; readme -> simpan teks
R = [
    (1,  "Mitchell-2004", None, [], "BERBAYAR (Project MUSE)"),
    (2,  "Mitchell-2005", None, [], "BERBAYAR (Project MUSE)"),
    (3,  "Lieberman-2022", "pdf", ["https://pmc.ncbi.nlm.nih.gov/articles/PMC10785677/pdf/"], None),
    (4,  "Ritmeester-2025", None, [], "BERBAYAR (Oxford JDSDE)"),
    (5,  "KemenkoPMK-2025", "html", ["https://www.kemenkopmk.go.id/kemenko-pmk-bergerak-bersama-wujudkan-selaras-bahasa-isyarat"], None),
    (6,  "UU-8-2016", "html", ["https://www.peraturan.go.id/id/uu-no-8-tahun-2016"], None),
    (7,  "Rodriguez-Correa-2023", "pdf", ["https://www.frontiersin.org/journals/education/articles/10.3389/feduc.2023.1121597/pdf"], None),
    (8,  "BRIN-2026", "html", ["https://brin.go.id/news/130095/survei-ungkap-777-penyandang-tuli-menggunakan-bisindo"], None),
    (9,  "Mursita-2015", "pdf", ["https://ejournal.uin-suka.ac.id/pusat/inklusi/article/download/1109/1002"], None),
    (10, "KamusSIBI-Digital", "html", ["https://pkplk.kemendikdasmen.go.id/sibi"], None),
    (11, "AsSatillah-2024", "pdf", ["https://jurnal.uai.ac.id/index.php/AUDHI/article/download/2876/1380"], None),
    (12, "Zikky-2019-KASIBI", None, [], "PERAMBAN (gratis di peramban: https://jurnal.poltekba.ac.id/index.php/jst/article/view/732)"),
    (13, "Fatmawati-2022-OpenSIBI", None, [], "PERAMBAN (gratis di peramban: https://ijc.ilearning.co/TMJ/en/article/view/1690 atau https://www.academia.edu/85649556)"),
    (14, "Sanjaya-2023-IJCS", "html", ["https://garuda.kemdikbud.go.id/documents/detail/4094170"], None),
    (15, "Dwijayanti-2021", "pdf", ["https://thesai.org/Downloads/Volume12No10/Paper_46-Indonesia_Sign_Language_Recognition.pdf"], None),
    (16, "Soekarta-2024", "pdf", ["https://ejournal.um-sorong.ac.id/index.php/insect/article/download/4079/2085"], None),
    (17, "Maulana-2026-DBESTI", "pdf", ["https://journal.nurulfikri.ac.id/index.php/DBESTI/article/download/2081/486"], None),
    (18, "MLMSign-2024", None, [], "BERBAYAR (Elsevier ISWA)"),
    (19, "Bailenson-2021", "pdf", ["https://vhil.stanford.edu/sites/g/files/sbiybj29011/files/media/file/bailenson-apa-nonverbal-overload.pdf"], None),
    (20, "HandFi-2024", None, [], "PERAMBAN (Procedia akses terbuka: https://doi.org/10.1016/j.procs.2024.04.042)"),
    (21, "Ma-2019-CSUR", "pdf", ["https://gzhou.pages.wm.edu/wp-content/blogs.dir/5736/files/sites/13/2017/12/WiFiSenseSurvey_CSUR19.pdf"], None),
    (22, "Ma-2018-SignFi", None, [], "PERAMBAN (IMWUT akses terbuka: https://dl.acm.org/doi/10.1145/3191755)"),
    (23, "Ahmed-2020-DFWiSLR", None, [], "BERBAYAR (Elsevier PMC)"),
    (24, "Baldeo-2024-FSL", None, [], "BERBAYAR (IEEE TENCON)"),
    (25, "Zhang-2020-WiSign", None, [], "BERBAYAR (ACM TIST)"),
    (26, "Ali-2015-WiKey", None, [], "PERAMBAN (salinan resmi SIGMOBILE: https://www.sigmobile.org/mobicom/2015/papers/p90-aliA.pdf)"),
    (27, "Mosleh-2022-BreatheSmart", "pdf", ["https://pmc.ncbi.nlm.nih.gov/articles/PMC9830631/pdf/sensors-22-0peech.txt"], None),
    (28, "Tan-2016-WiFinger", None, [], "PERAMBAN (ACM DL: https://dl.acm.org/doi/10.1145/2942358.2942393)"),
    (29, "Wu-2020-FingerDraw", None, [], "PERAMBAN (IMWUT akses terbuka: https://dl.acm.org/doi/10.1145/3380981)"),
    (30, "Zheng-2024-MeshID", "pdf", ["https://www.mdpi.com/1424-8220/24/6/1978/pdf", "https://www.mdpi.com/1424-8220/24/6/1978/pdf?version=1"], None),
    (31, "esp-csi", "md", ["https://raw.githubusercontent.com/espressif/esp-csi/main/README.md", "https://raw.githubusercontent.com/espressif/esp-csi/master/README.md"], None),
    (32, "RuView", "md", ["https://raw.githubusercontent.com/ruvnet/RuView/main/README.md"], None),
    (33, "ESP32-S3-datasheet", "pdf", ["https://www.espressif.com/sites/default/files/documentation/esp32-s3_datasheet_en.pdf"], None),
    (34, "esp-nn", "md", ["https://raw.githubusercontent.com/espressif/esp-nn/main/README.md", "https://raw.githubusercontent.com/espressif/esp-nn/master/README.md"], None),
    (35, "esp-dl", "md", ["https://raw.githubusercontent.com/espressif/esp-dl/main/README.md"], None),
    (36, "tokio", "md", ["https://raw.githubusercontent.com/tokio-rs/tokio/master/README.md"], None),
    (37, "axum", "md", ["https://raw.githubusercontent.com/tokio-rs/axum/main/README.md"], None),
    (38, "leptos", "md", ["https://raw.githubusercontent.com/leptos-rs/leptos/main/README.md"], None),
    (39, "tauri", "md", ["https://raw.githubusercontent.com/tauri-apps/tauri/dev/README.md", "https://raw.githubusercontent.com/tauri-apps/tauri/main/README.md"], None),
    (40, "onnxruntime", "md", ["https://raw.githubusercontent.com/microsoft/onnxruntime/main/README.md"], None),
    (41, "kokoro-onnx", "md", ["https://raw.githubusercontent.com/thewh1teagle/kokoro-onnx/main/README.md"], None),
    (42, "Kokoro-82M", "md", ["https://huggingface.co/hexgrad/Kokoro-82M/raw/main/README.md"], None),
    (43, "Pratap-2023-MMS", "pdf", ["https://arxiv.org/pdf/2305.13516"], None),
    (44, "MMS-TTS-ind", "md", ["https://huggingface.co/facebook/mms-tts-ind/raw/main/README.md"], None),
    (45, "GoogleCloud-TTS", "html", ["https://cloud.google.com/text-to-speech/docs/list-voices-and-types"], None),
    (46, "Azure-Speech", "html", ["https://learn.microsoft.com/azure/ai-services/speech-service/language-support"], None),
    (47, "Radford-2022-Whisper", "pdf", ["https://arxiv.org/pdf/2212.04356"], None),
    (48, "faster-whisper", "md", ["https://raw.githubusercontent.com/SYSTRAN/faster-whisper/master/README.md"], None),
    (49, "Chen-2023-CSUR", None, [], "BERBAYAR (ACM CSUR)"),
    (50, "Zhang-2022-Widar3", "pdf", ["https://tns.thss.tsinghua.edu.cn/widar3.0/data/TPAMI_Widar3.0_paper.pdf"], None),
    (51, "Jocher-2026-YOLO26", "pdf", ["https://arxiv.org/pdf/2606.03748"], None),
    (52, "Ultralytics-pose-docs", "html", ["https://docs.ultralytics.com/tasks/pose/"], None),
    (53, "Picron-2024", None, [], "BERBAYAR (bab Springer)"),
    (54, "Hakozaki-2025", None, [], "BERBAYAR (ACM ASSETS)"),
    (55, "KamusSIBI-1994", None, [], "TANPA VERSI DIGITAL (cetak)"),
    (56, "Stokoe-2005", None, [], "BERBAYAR (Oxford JDSDE)"),
    (57, "Ong-2005-survey", "pdf", ["https://projectsweb.cs.washington.edu/research/projects/compression/sign_recognition/generals/survey.pdf"], None),
    (58, "Nugraheni-2023-Holistika", "html", ["https://jurnal.umj.ac.id/index.php/holistika/article/view/9355"], None),
    (59, "Malika-2025-Concept", "pdf", ["https://journal-stiayappimakassar.ac.id/index.php/Concept/article/download/2178/2251"], None),
    (60, "Rodhiyah-2024-INTECOMS", "html", ["https://journal.ipm2kpe.or.id/index.php/INTECOMS/article/view/8326"], None),
    (61, "Kindy-2025-BISINDO", None, [], "PERAMBAN (Procedia akses terbuka: https://doi.org/10.1016/j.procs.2025.08.277)"),
    (62, "Wiguna-2025-BISINDO", "pdf", ["https://thesai.org/Downloads/Volume16No9/Paper_41-Sentence_Level_Indonesian_Sign_Language_BISINDO_Recognition.pdf"], None),
    (63, "Sebastian-2025-BISINDO", None, [], "PERAMBAN (Procedia akses terbuka: https://doi.org/10.1016/j.procs.2025.09.042)"),
    (64, "Cai-2024-Sensors", "pdf", ["https://www.mdpi.com/1424-8220/24/11/3414/pdf", "https://www.mdpi.com/1424-8220/24/11/3414/pdf?version=1"], None),
    (65, "Nyquist-1928", "pdf", ["https://bayes.wustl.edu/Manual/CertainTopicsInTelegraphTransmissionTheory.pdf"], None),
    (66, "Shannon-1949", "pdf", ["https://webusers.imj-prg.fr/~antoine.chambert-loir/enseignement/2020-21/shannon/shannon1949.pdf"], None),
    (67, "Hao-2020-WiSL", "pdf", ["https://www.mdpi.com/1424-8220/20/14/4025/pdf", "https://www.mdpi.com/1424-8220/20/14/4025/pdf?version=1"], None),
    (68, "Hernandez-2020-WoWMoM", "pdf", ["https://www.people.vcu.edu/~ebulut/wowmom20-WiFiSensing.pdf"], None),
    (69, "Zheng-2023-PoseSurvey", "pdf", ["https://arxiv.org/pdf/2012.13392"], None),
    (70, "Sapkota-2025-YOLO26", "pdf", ["https://arxiv.org/pdf/2509.25164"], None),
    (71, "Lugaresi-2019-MediaPipe", "pdf", ["https://arxiv.org/pdf/1906.08172"], None),
    (72, "Wang-2019-PersonInWiFi", "pdf", ["https://openaccess.thecvf.com/content_ICCV_2019/papers/Wang_Person-in-WiFi_Fine-Grained_Person_Perception_Using_WiFi_ICCV_2019_paper.pdf"], None),
    (73, "Geng-2023-DensePoseWiFi", "pdf", ["https://arxiv.org/pdf/2301.00250"], None),
    (74, "Shang-2017-MobiArch", "pdf", ["https://cis.temple.edu/~wu/research/publications/Publication_files/Shang_MASS_2017.pdf"], None),
    (75, "Ahmed-2021-LSTM", None, [], "BERBAYAR (IEEE IAICT)"),
    (76, "Qin-2023-WiASL", None, [], "BERBAYAR (Elsevier Measurement)"),
    (77, "Cortes-1995-SVM", "pdf", ["https://web.engr.oregonstate.edu/~huanlian/teaching/ML/2018spring/extra/svn-1995.pdf"], None),
    (78, "Mountrakis-2011-SVM", "pdf", ["https://www.aboutgis.com/pdfs/Mountrakis_SVM_review_in_remote_sensing_ISPRS2010.pdf"], None),
    (79, "Kiranyaz-2021-1DCNN", "pdf", ["https://arxiv.org/pdf/1905.03554"], None),
    (80, "Chow-1970", None, [], "BERBAYAR (IEEE TIT)"),
    (81, "tflite-micro-esp-examples", "md", ["https://raw.githubusercontent.com/espressif/tflite-micro-esp-examples/master/README.md", "https://raw.githubusercontent.com/espressif/tflite-micro-esp-examples/main/README.md"], None),
    (82, "Safrida-2026-Rabit", "html", ["https://jurnal.mdp.ac.id/index.php/rabit/article/view/8340"], None),
    (83, "Rakun-2015-SIBI", None, [], "BERBAYAR (IEEE TIME-E)"),
    (84, "Anggraini-2019-SIBI", None, [], "BERBAYAR (IEEE ICEEI)"),
    (85, "Sagawa-2002-JSL", "pdf", ["https://vipl.ict.ac.cn/research/sign/hylw/202205/W020220524841131372266.pdf"], None),
    (86, "Bowen-2009", "pdf", ["https://pmc.ncbi.nlm.nih.gov/articles/PMC2859314/pdf/nihms187611.pdf", "https://pmc.ncbi.nlm.nih.gov/articles/PMC2859314/pdf/"], None),
    (87, "Sokolova-2009", "pdf", ["https://engold.ui.ac.ir/~h.marateb/SokolovaLapalme-JIPM09.pdf"], None),
    (88, "Likert-1932", "pdf", ["https://archive.org/download/likert-1932/Likert_1932.pdf"], None),
    (89, "Hinton-2015-Distill", "pdf", ["https://arxiv.org/pdf/1503.02531"], None),
    (90, "Wu-2022-CSIratio", "pdf", ["https://link.springer.com/content/pdf/10.1007/s42486-021-00077-z.pdf"], None),
    (91, "Mankins-2009-TRL", None, [], "BERBAYAR (Elsevier Acta Astronautica)"),
    (92, "Qian-2018-Widar2", "pdf", ["https://dl.acm.org/doi/pdf/10.1145/3210240.3210314"], None),
    (93, "Yang-2023-MMFi", "pdf", ["https://arxiv.org/pdf/2305.10345"], None),
    (94, "INMP441-datasheet", "pdf", ["https://www.invensense.tdk.com/wp-content/uploads/2015/02/INMP441.pdf", "https://invensense.tdk.com/en-us/download-resource/ds-inmp441-00-inmp441-datasheet"], None),
]

hasil = []
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"
for n, key, ext, urls, catatan in R:
    if not urls:
        hasil.append((n, key, "LEWAT", catatan))
        continue
    ok = False
    for u in urls:
        target = os.path.join(OUT, fn(n, key, ext))
        r = subprocess.run(["curl", "-sL", "--max-time", "60", "-A", UA,
                            "-o", target, "-w", "%{http_code}", u],
                           capture_output=True, text=True, timeout=90)
        code = r.stdout.strip() if r.stdout else "000"
        size = os.path.getsize(target) if os.path.exists(target) else 0
        head = open(target, "rb").read(5) if size else b""
        if code.startswith("2") and size > 2048 and (ext != "pdf" or head == b"%PDF-"):
            ok = True
            hasil.append((n, key, "TERUNDUH", f"{size} byte ({ext})"))
            break
        elif code.startswith("2") and size > 2048 and ext == "pdf":
            os.remove(target)  # PDF palsu (halaman HTML)
        elif os.path.exists(target) and size <= 2048:
            os.remove(target)
    if not ok and not any(h[0] == n and h[2] == "TERUNDUH" for h in hasil):
        hasil.append((n, key, "GAGAL-OTOMATIS", "; ".join(urls[:1]) + f" (http terakhir {code})"))

terunduh = [h for h in hasil if h[2] == "TERUNDUH"]
print(f"TERUNDUH: {len(terunduh)}/{len(R)}")
for n, key, st, info in hasil:
    print(f"[{n:02d}] {st:16} {key:26} {info}")
json.dump([{"no": n, "kunci": k, "status": s, "info": i} for n, k, s, i in hasil],
          open("/home/z/my-project/scripts/sensesibi-v10/hasil_unduh.json", "w"), ensure_ascii=False, indent=1)
