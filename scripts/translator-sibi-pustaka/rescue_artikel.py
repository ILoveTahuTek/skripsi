#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
rescue_artikel.py — ubah rujukan yang masih 'halaman penerbit'/'gagal' menjadi
berkas artikel sungguhan (PDF/DOCX) via cermin legal deterministik:
halaman penulis, repositori universitas, PMC/Europe PMC, OJS via jina.
"""
import html as mod_html
import json
import re
import subprocess
import sys
import time
from pathlib import Path
from urllib.parse import urljoin

import requests

sys.path.insert(0, str(Path(__file__).parent))
from unduh_pustaka import DIR_PDF, DIR_WEB, HDR, get_url, pdf_ok
from data_pustaka import REFS

AKAR = DIR_PDF.parent
HASIL_PATH = AKAR / "_hasil.json"
hasil = json.loads(HASIL_PATH.read_text(encoding="utf-8"))
KEY = {r["no"]: r["key"] for r in REFS}
CITE = {r["no"]: r["cite"] for r in REFS}

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")


def catat(no, **kw):
    e = hasil.get(str(no), {})
    e.update(kw)
    e["key"] = KEY[no]
    hasil[str(no)] = e
    HASIL_PATH.write_text(json.dumps(hasil, ensure_ascii=False, indent=1, sort_keys=True),
                          encoding="utf-8")
    print(f"{no:02d} [{kw.get('status', '?'):8}] {kw.get('sumber', '')[:80]}", flush=True)


def curl_ok(url, path, referer=None):
    cmd = ["curl", "-sL", "--max-time", "100", "-A", UA, "-o", str(path)]
    if referer:
        cmd += ["-e", referer]
    cmd.append(url)
    try:
        subprocess.run(cmd, capture_output=True, timeout=130)
    except Exception:
        return False
    return path.exists() and path.stat().st_size > 15000


def unduh_pdf(no, kandidat, catatan_ok):
    """Coba daftar URL -> simpan PDF pertama yang valid."""
    if hasil.get(str(no), {}).get("status") == "pdf":
        return True
    t = DIR_PDF / f"{no:02d} - {KEY[no]}.pdf"
    for u in kandidat:
        if curl_ok(u, t):
            b = t.read_bytes()
            if b[:5].startswith(b"%PDF"):
                catat(no, status="pdf", berkas=str(t), sumber=u, catatan=catatan_ok)
                return True
        time.sleep(1)
    return False


def unduh_docx(no, kandidat, catatan_ok):
    """Coba daftar URL -> simpan DOCX pertama yang valid (PK header)."""
    if hasil.get(str(no), {}).get("status") in ("pdf", "docx"):
        return True
    t = AKAR / "docx" / f"{no:02d} - {KEY[no]}.docx"
    t.parent.mkdir(exist_ok=True)
    for u in kandidat:
        if curl_ok(u, t):
            b = t.read_bytes()
            if b[:2] == b"PK":
                catat(no, status="docx", berkas=str(t), sumber=u, catatan=catatan_ok)
                return True
        time.sleep(1)
    return False


def jina(url):
    """Baca halaman via r.jina.ai, kembalikan teks."""
    try:
        r = requests.get(f"https://r.jina.ai/{url}", headers=HDR, timeout=(15, 80))
        return r.text if r.status_code == 200 else ""
    except Exception:
        return ""


# ================= 3 Lieberman 2022 (PMC) =================
unduh_pdf(3, [
    "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10785677/fullTextPDF",
    "https://europepmc.org/backend/ftpmc/PMC10785677",
    "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10785677/pdf/alr-15-1-applirev-2021-0120.pdf",
    "https://www.degruyterbrill.com/document/doi/10.1515/applirev-2021-0120/pdf",
], "Salinan terbuka resmi via Europe PMC (PMC10785677)")

# ================= 21 SignFi (gzhou) =================
unduh_pdf(21, [
    "https://gzhou.pages.wm.edu/wp-content/blogs.dir/5736/files/sites/13/2017/12/SignFi_IMWUT18.pdf",
    "https://gzhou.pages.wm.edu/wp-content/blogs.dir/5736/files/sites/13/2019/03/SignFi_IMWUT18.pdf",
    "https://gzhou.pages.wm.edu/wp-content/blogs.dir/5736/files/sites/13/2018/10/SignFi_IMWUT18.pdf",
], "Salinan penulis (Zimu Zhou, William & Mary)")

# ================= 24 WiSign — scrape publikasi gzhou =================
if hasil.get("24", {}).get("status") != "pdf":
    kand = []
    for hal in ("https://gzhou.pages.wm.edu/publication/", "https://gzhou.pages.wm.edu/"):
        b = get_url(hal, timeout=(15, 60))
        if not b:
            continue
        t = b[0].decode("utf-8", "ignore")
        for m in re.finditer(r'href="([^"]+\.pdf)"', t, re.I):
            u = urljoin(hal, mod_html.unescape(m.group(1)))
            if re.search(r"(wisign|tist)", u, re.I) or "WiSign" in t[max(0, m.start() - 300):m.start()]:
                kand.append(u)
        if kand:
            break
    unduh_pdf(24, kand[:4], "Salinan penulis (William & Mary)")

# ================= 25 Ali MobiCom (UNC CDR) =================
unduh_pdf(25, [
    "https://cdr.lib.unc.edu/downloads/bc386t01s",
    "https://cdr.lib.unc.edu/downloads/bc386t01s?locale=en",
    "https://cdr.lib.unc.edu/downloads/bc386t01s?locale=en-US",
], "Salinan resmi via Carolina Digital Repository (UNC)")

# ================= 56 Shannon 1949 — cermin kuliah =================
unduh_pdf(56, [
    "https://people.math.harvard.edu/~ctm/home/text/ShannonNosie.pdf",
    "https://webusers.imj-prg.fr/~antoine.chambert-loir/enseignement/2020-21/shannon/shannon1949.pdf",
    "https://www.cs.cmu.edu/~allenw/CommunicationTheoryShannon.pdf",
], "Cermin legal karya klasik di halaman kuliah universitas (domain publik distribusi edukatif)")

# ================= 59 Hernandez & Bulut (VCU) =================
unduh_pdf(59, [
    "https://ebulutvcu.github.io/Wowmom20-Lightweight.pdf",
    "https://ebulutvcu.github.io/Lightweight20.pdf",
    "https://www.people.vcu.edu/~ebulut/wowmom20-WiFiSensing.pdf",
    "https://stevenmhernandez.com/papers/wowmom20.pdf",
], "Salinan penulis (Bulut, VCU / Hernandez)")

# ================= 65 Shang & Wu (Temple) =================
unduh_pdf(65, [
    "https://www.cs.temple.edu/~wu/robust17.pdf",
    "https://cis.temple.edu/~wu/robust17.pdf",
    "https://www.temple.edu/cis/wu/robust17.pdf",
], "Salinan penulis (Jie Wu, Temple University)")

# ================= 71 Chow 1970 — cermin kuliah =================
unduh_pdf(71, [
    "https://scispace.com/pdf/on-optimum-recognition-error-and-reject-tradeoff-4ugvowtm6a.pdf",
    "https://www.cse.iitm.ac.in/~vplab/courses/2016_f pageTitle.pdf",
    "https://cs.nyu.edu/~roweis/csc4520-2006/notes/chow70.pdf",
], "Cermin legal karya klasik di repositori kuliah universitas")

# ================= 77 Bowen 2009 (PMC) =================
unduh_pdf(77, [
    "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2859314/fullTextPDF",
    "https://europepmc.org/backend/ftpmc/PMC2859314",
    "https://europepmc.org/articles/PMC2859314?pdf=render",
], "Salinan terbuka resmi via Europe PMC (PMC2859314)")

# ================= 12 KASIBI (poltekba/polban, jina) =================
if hasil.get("12", {}).get("status") not in ("pdf", "docx"):
    kand = []
    for hal in ("https://jurnal.poltekba.ac.id/index.php/jst/article/view/732",
                "https://jurnal.polban.ac.id/index.php/jst/article/view/732"):
        txt = jina(hal)
        for u in re.findall(r'\((https?://[^\s)]+)\)', txt):
            if "/article/" in u:
                kand.append(u.replace("/article/view/", "/article/download/"))
        b = get_url(hal, timeout=(15, 60))
        if b:
            t = b[0].decode("utf-8", "ignore")
            for m in re.finditer(r'href="([^"]+/article/download/[^"]+)"', t, re.I):
                kand.append(urljoin(hal, mod_html.unescape(m.group(1))))
            if "/article/download/732/" not in " ".join(kand):
                for gal in re.findall(r'/article/view/732/(\d+)', t):
                    kand.append(urljoin(hal, f"/article/download/732/{gal}"))
    sukses = unduh_pdf(12, list(dict.fromkeys(kand))[:8],
                       "PDF akses-terbuka OJS (Jurnal Sains Terapan)")
    if not sukses:
        unduh_docx(12, [u for u in kand if ".doc" in u.lower()][:4],
                   "DOCX galley OJS (Jurnal Sains Terapan)")

# ================= 14 IJCS 3539 (jina + galley) =================
if hasil.get("14", {}).get("status") not in ("pdf", "docx"):
    kand = ["https://ijcs.stmikindonesia.ac.id/ijcs/index.php/ijcs/article/viewFile/3539/298",
            "https://ijcs.stmikindonesia.ac.id/ijcs/index.php/ijcs/article/download/3539/298"]
    txt = jina("https://ijcs.stmikindonesia.ac.id/ijcs/index.php/ijcs/article/view/3539")
    for u in re.findall(r'\((https?://[^\s)]+)\)', txt):
        if "/article/" in u:
            kand.append(u.replace("/article/view/", "/article/download/"))
    b = get_url("https://ijcs.stmikindonesia.ac.id/ijcs/index.php/ijcs/article/view/3539",
                timeout=(15, 60))
    if b:
        t = b[0].decode("utf-8", "ignore")
        for gal in re.findall(r'/article/view/3539/(\d+)', t):
            kand.append(f"https://ijcs.stmikindonesia.ac.id/ijcs/index.php/ijcs/article/download/3539/{gal}")
    unduh_pdf(14, list(dict.fromkeys(kand))[:8], "PDF akses-terbuka OJS IJCS")
    unduh_docx(14, [], "DOCX galley OJS IJCS")

# ================= 48 Holistika 9355 =================
if hasil.get("48", {}).get("status") not in ("pdf", "docx"):
    kand = ["https://jurnal.umj.ac.id/index.php/holistika/article/download/9355/5468",
            "https://jurnal.umj.ac.id/index.php/holistika/article/viewFile/9355/5468"]
    txt = jina("https://jurnal.umj.ac.id/index.php/holistika/article/view/9355")
    for u in re.findall(r'\((https?://[^\s)]+)\)', txt):
        if "/article/" in u:
            kand.append(u.replace("/article/view/", "/article/download/"))
    unduh_pdf(48, list(dict.fromkeys(kand))[:8], "PDF akses-terbuka OJS Holistika (UMJ)")

# ================= 73 Safrida Rabit 8340 (mdp + garuda + jina) =================
if hasil.get("73", {}).get("status") not in ("pdf", "docx"):
    kand = ["https://jurnal.mdp.ac.id/index.php/rabit/article/download/8340/4101",
            "https://jurnal.univrab.ac.id/index.php/rabit/article/download/8340",
            "https://jurnal.univrab.ac.id/index.php/rabit/article/viewFile/8340/298"]
    for hal in ("https://jurnal.mdp.ac.id/index.php/rabit/article/view/8340",
                "https://jurnal.univrab.ac.id/index.php/rabit/article/view/8340",
                "https://garuda.kemdiktisaintek.go.id/journal/view/10473?page=20&issue=vol%2011%20no%202%20(2026):%20juli"):
        b = get_url(hal, timeout=(15, 90))
        if not b:
            continue
        t = b[0].decode("utf-8", "ignore")
        for m in re.finditer(r'href="([^"]+(?:download|viewFile)[^"]*)"', t, re.I):
            kand.append(urljoin(hal, mod_html.unescape(m.group(1))))
        txtj = jina(hal)
        for u in re.findall(r'\((https?://[^\s)]+)\)', txtj):
            if re.search(r'/article/(download|view)/8340', u):
                kand.append(u.replace("/article/view/", "/article/download/"))
    unduh_pdf(73, list(dict.fromkeys(kand))[:10], "PDF akses-terbuka OJS RABIT / Garuda")

# ================= 35 kartu HF mms-tts-ind =================
if hasil.get("35", {}).get("status") not in ("halaman", "pdf"):
    t = DIR_WEB / "35 - Meta-AI-kartu-model-facebook-mms-tts-ind (halaman penerbit).html"
    if curl_ok("https://huggingface.co/facebook/mms-tts-ind", t):
        catat(35, status="halaman", berkas=str(t),
              sumber="https://huggingface.co/facebook/mms-tts-ind",
              catatan="Kartu model — kanon berbentuk halaman web, tidak ada PDF penerbit")

print("\n=== STATUS SETELAH RESCUE ===", flush=True)
import collections
c = collections.Counter(v.get("status") for k, v in hasil.items() if not k.startswith("_"))
print(c)
