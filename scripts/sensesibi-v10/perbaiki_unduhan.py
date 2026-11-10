#!/usr/bin/env python3
"""Putaran 2: perbaiki unduhan yang gagal dengan strategi alternatif."""
import subprocess, os, json, time

OUT = "/home/z/my-project/download/sensesibi-v10/referensi"
H = json.load(open("/home/z/my-project/scripts/sensesibi-v10/hasil_unduh.json"))
status = {x["no"]: dict(x) for x in H}

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"

def coba(n, key, ext, urls, catatan_ok="ok", min_size=1024, pdf_wajib=True):
    target = os.path.join(OUT, f"ref-{n:02d}_{key}.{ext}")
    for u in urls:
        try:
            r = subprocess.run(["curl", "-sL", "--max-time", "75", "-A", UA,
                                "-H", "Accept: */*",
                                "-H", "Referer: https://www.google.com/",
                                "--compressed",
                                "-o", target, "-w", "%{http_code}", u],
                               capture_output=True, text=True, timeout=100)
        except Exception:
            continue
        code = r.stdout.strip() if r.stdout else "000"
        size = os.path.getsize(target) if os.path.exists(target) else 0
        head = open(target, "rb").read(5) if size else b""
        if code.startswith("2") and size >= min_size and (not pdf_wajib or ext != "pdf" or head == b"%PDF-"):
            status[n].update(status="TERUNDUH", info=f"{size} byte ({ext}) — {catatan_ok}")
            return True
        if os.path.exists(target) and size < min_size:
            os.remove(target)
    return False

# EuropePMC untuk PDF PMC
coba(3,  "Lieberman-2022", "pdf", ["https://europepmc.org/articles/PMC10785677?pdf=render"], "EuropePMC render")
coba(27, "Mosleh-2022-BreatheSmart", "pdf", ["https://europepmc.org/articles/PMC9830631?pdf=render"], "EuropePMC render")
coba(86, "Bowen-2009", "pdf", ["https://europepmc.org/articles/PMC2859314?pdf=render"], "EuropePMC render")

# MDPI dengan header peramban
coba(30, "Zheng-2024-MeshID", "pdf", ["https://www.mdpi.com/1424-8220/24/6/1978/pdf"], "MDPI")
coba(64, "Cai-2024-Sensors", "pdf", ["https://www.mdpi.com/1424-8220/24/11/3414/pdf"], "MDPI")
coba(67, "Hao-2020-WiSL", "pdf", ["https://www.mdpi.com/1424-8220/20/14/4025/pdf"], "MDPI")

# cabang repo alternatif / README kecil tetap disimpan
coba(35, "esp-dl", "md", ["https://raw.githubusercontent.com/espressif/esp-dl/master/README.md",
                          "https://raw.githubusercontent.com/espressif/esp-dl/master/README.rst",
                          "https://raw.githubusercontent.com/espressif/esp-dl/main/README.md"], "GitHub raw", min_size=200, pdf_wajib=False)
coba(37, "axum", "md", ["https://raw.githubusercontent.com/tokio-rs/axum/main/README.md"], "GitHub raw", min_size=50, pdf_wajib=False)

# Hugging Face ulang (429 tadi)
coba(44, "MMS-TTS-ind", "md", ["https://huggingface.co/facebook/mms-tts-ind/raw/main/README.md",
                               "https://huggingface.co/facebook/mms-tts-ind/raw/main/modelcard.md"], "HF raw", min_size=200, pdf_wajih=False) if False else None
coba(44, "MMS-TTS-ind", "md", ["https://huggingface.co/facebook/mms-tts-ind/raw/main/README.md"], "HF raw", min_size=200, pdf_wajib=False)

# Springer terenkode
coba(90, "Wu-2022-CSIratio", "pdf", ["https://link.springer.com/content/pdf/10.1007%2Fs42486-021-00077-z.pdf",
                                     "https://link.springer.com/content/pdf/10.1007/s42486-021-00077-z.pdf"], "Springer")

# VCU ulang (http)
coba(68, "Hernandez-2020-WoWMoM", "pdf", ["https://www.people.vcu.edu/~ebulut/wowmom20-WiFiSensing.pdf",
                                          "http://www.people.vcu.edu/~ebulut/wowmom20-WiFiSensing.pdf"], "salinan penulis VCU")

# Sokolova ulang
coba(87, "Sokolova-2009", "pdf", ["https://engold.ui.ac.ir/~h.marateb/SokolovaLapalme-JIPM09.pdf"], "salinan dosen Isfahan")

# ACM IMWUT terbuka (FingerDraw) & garuda & UU & INMP441 via parsing
coba(29, "Wu-2020-FingerDraw", "pdf", ["https://dl.acm.org/doi/pdf/10.1145/3380981"], "ACM IMWUT terbuka")
coba(14, "Sanjaya-2023-IJCS", "html", ["https://garuda.kemdikbud.go.id/documents/detail/4094170"], "halaman Garuda", pdf_wajib=False)
coba(6,  "UU-8-2016", "html", ["https://www.peraturan.go.id/id/uu-no-8-tahun-2016",
                               "https://jdih.setneg.go.id/Produk"], "peraturan.go.id", pdf_wajib=False)

# INMP441: unduh halaman, cari tautan PDF
n, key = 94, "INMP441-datasheet"
target = os.path.join(OUT, f"ref-{n:02d}_{key}.html")
r = subprocess.run(["curl", "-sL", "--max-time", "60", "-A", UA, "-o", target,
                    "-w", "%{http_code}", "https://www.invensense.tdk.com/en-us/download-resource/ds-inmp441-00-inmp441-datasheet"],
                   capture_output=True, text=True, timeout=90)
if os.path.exists(target):
    s = open(target, encoding="utf-8", errors="ignore").read()
    import re
    m = re.search(r'href="([^"]+\.pdf)"', s, re.I)
    if m:
        u = m.group(1)
        if u.startswith("/"): u = "https://www.invensense.tdk.com" + u
        elif not u.startswith("http"): u = "https://www.invensense.tdk.com/en-us/" + u
        print("tautan PDF INMP441:", u)
        coba(n, key, "pdf", [u], "lembar data TDK")
    else:
        if os.path.getsize(target) > 2048:
            status[n].update(status="TERUNDUH", info=f"{os.path.getsize(target)} byte (html resmi) — halaman lembar data TDK")
        else:
            os.remove(target)

# tandai sisa yang memang peramban/berbayar
manual = {
    6:  "PERAMBAN (naskah resmi UU: https://www.peraturan.go.id/id/uu-no-8-tahun-2016)",
    12: "PERAMBAN (gratis di peramban: https://jurnal.poltekba.ac.id/index.php/jst/article/view/732)",
    13: "PERAMBAN (gratis di peramban: https://ijc.ilearning.co/TMJ/en/article/view/1690 atau https://www.academia.edu/85649556)",
    14: "PERAMBAN (halaman Garuda/portal: https://garuda.kemdikbud.go.id/documents/detail/4094170)",
    20: "PERAMBAN (Procedia akses terbuka: https://doi.org/10.1016/j.procs.2024.04.042)",
    22: "PERAMBAN (IMWUT akses terbuka: https://dl.acm.org/doi/10.1145/3191755)",
    26: "PERAMBAN (salinan resmi SIGMOBILE: https://www.sigmobile.org/mobicom/2015/papers/p90-aliA.pdf)",
    28: "PERAMBAN (ACM DL: https://dl.acm.org/doi/10.1145/2942358.2942393)",
    29: "PERAMBAN (IMWUT akses terbuka: https://dl.acm.org/doi/10.1145/3380981)",
    58: "PERAMBAN (OJS UMJ: https://jurnal.umj.ac.id/index.php/holistika/article/view/9355)",
    60: "PERAMBAN (OJS IPM2KPE: https://journal.ipm2kpe.or.id/index.php/INTECOMS/article/view/8326)",
    61: "PERAMBAN (Procedia akses terbuka: https://doi.org/10.1016/j.procs.2025.08.277)",
    63: "PERAMBAN (Procedia akses terbuka: https://doi.org/10.1016/j.procs.2025.09.042)",
    82: "PERAMBAN (OJS MDP: https://jurnal.mdp.ac.id/index.php/rabit/article/view/8340)",
    87: "PERAMBAN (salinan dosen: https://engold.ui.ac.ir/~h.marateb/SokolovaLapalme-JIPM09.pdf)",
    92: "PERAMBAN (ACM DL MobiSys'18: https://dl.acm.org/doi/10.1145/3210240.3210314)",
}
for n, ket in manual.items():
    if status[n]["status"] != "TERUNDUH":
        status[n].update(status="PERAMBAN", info=ket)

hasil = [status[x] for x in sorted(status)]
json.dump(hasil, open("/home/z/my-project/scripts/sensesibi-v10/hasil_unduh.json", "w"), ensure_ascii=False, indent=1)
t = [x for x in hasil if x["status"] == "TERUNDUH"]
p = [x for x in hasil if x["status"] == "PERAMBAN"]
b = [x for x in hasil if x["status"].startswith(("BERBAYAR", "TANPA", "LEWAT"))]
g = [x for x in hasil if x["status"] == "GAGAL-OTOMATIS"]
print(f"TERUNDUH={len(t)} PERAMBAN={len(p)} BERBAYAR/LEWAT={len(b)} GAGAL={len(g)}")
for x in g: print("  masih gagal:", x["no"], x["kunci"], x["info"])
