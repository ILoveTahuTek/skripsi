#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""probe_kedua.py — probe cepat sumber-sumber spesifik utk rujukan tersisa."""
import json
import re
import subprocess
import sys
import time
from pathlib import Path
from urllib.parse import urljoin

import requests

sys.path.insert(0, str(Path(__file__).parent))
from unduh_pustaka import DIR_PDF, HDR, get_url, pdf_ok
from data_pustaka import REFS

AKAR = DIR_PDF.parent
HASIL_PATH = AKAR / "_hasil.json"
hasil = json.loads(HASIL_PATH.read_text(encoding="utf-8"))
KEY = {r["no"]: r["key"] for r in REFS}
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")


def catat(no, **kw):
    e = hasil.get(str(no), {})
    e.update(kw)
    e["key"] = KEY[no]
    hasil[str(no)] = e
    HASIL_PATH.write_text(json.dumps(hasil, ensure_ascii=False, indent=1, sort_keys=True),
                          encoding="utf-8")
    print(f"{no:02d} [{kw.get('status','?'):8}] {kw.get('sumber','')[:80]}", flush=True)


def sudah(no):
    return hasil.get(str(no), {}).get("status") in ("pdf", "docx")


def unduh_curl(no, url, catatan, referer=None):
    t = DIR_PDF / f"{no:02d} - {KEY[no]}.pdf"
    cmd = ["curl", "-sL", "--max-time", "90", "-A", UA, "-o", str(t)]
    if referer:
        cmd += ["-e", referer]
    cmd.append(url)
    subprocess.run(cmd, capture_output=True, timeout=110)
    if t.exists() and pdf_ok(t.read_bytes()):
        catat(no, status="pdf", berkas=str(t), sumber=url, catatan=catatan)
        return True
    if t.exists():
        t.unlink()
    return False


# ---------- 77 Bowen + 3 Lieberman via pmc.ncbi.nlm.nih.gov ----------
if not sudah(77):
    for u in ("https://pmc.ncbi.nlm.nih.gov/articles/PMC2859314/pdf/",
              "https://pmc.ncbi.nlm.nih.gov/articles/PMC2859314/pdf/nihms195094.pdf",
              "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2859314/pdf/"):
        if unduh_curl(77, u, "Salinan terbuka resmi via PubMed Central (PMC2859314)",
                      referer="https://pmc.ncbi.nlm.nih.gov/articles/PMC2859314/"):
            break
if not sudah(3):
    for u in ("https://pmc.ncbi.nlm.nih.gov/articles/PMC10785677/pdf/alr-15-1-applirev-2021-0120.pdf",
              "https://pmc.ncbi.nlm.nih.gov/articles/PMC10785677/pdf/",
              "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10785677/pdf/alr-15-1-applirev-2021-0120.pdf"):
        if unduh_curl(3, u, "Salinan terbuka resmi via PubMed Central (PMC10785677)",
                      referer="https://pmc.ncbi.nlm.nih.gov/articles/PMC10785677/"):
            break

# ---------- 73 Safrida via Garuda ----------
if not sudah(73):
    kand = []
    for q in ("OPTIMASI+KLASIFIKASI+CITRA+ALFABET+SISTEM+ISYARAT",
              "Safrida+MobileNetV2+SIBI"):
        b = get_url(f"https://garuda.kemdiktisaintek.go.id/documents?q={q}", timeout=(15, 60))
        if not b:
            continue
        t = b[0].decode("utf-8", "ignore")
        for m in re.finditer(r'href="([^"]+)"', t):
            u = urljoin("https://garuda.kemdiktisaintek.go.id/", m.group(1))
            if "/documents/" in u:
                kand.append(u)
        if kand:
            break
    print(f"73 kandidat garuda: {kand[:3]}", flush=True)
    for u in kand[:4]:
        b = get_url(u, timeout=(15, 60))
        if not b:
            continue
        t = b[0].decode("utf-8", "ignore")
        for m in re.finditer(r'href="([^"]*download[^"]*)"', t, re.I):
            u2 = urljoin(u, m.group(1))
            if unduh_curl(73, u2, "PDF akses-terbuka via Garuda"):
                break
        if sudah(73):
            break

# ---------- 12 KASIBI polban/poltekba ----------
if not sudah(12):
    kand = []
    for hal in ("https://jurnal.polban.ac.id/index.php/jst/article/view/732",
                "https://jurnal.poltekba.ac.id/index.php/jst/article/view/732"):
        b = get_url(hal, timeout=(15, 60))
        if not b:
            continue
        t = b[0].decode("utf-8", "ignore")
        for m in re.finditer(r'href="([^"]*article/(?:download|viewFile)/[^"]+)"', t, re.I):
            u = urljoin(hal, m.group(1))
            kand.append(u)
    print(f"12 kandidat galley: {kand[:4]}", flush=True)
    for u in kand[:6]:
        if unduh_curl(12, u, "PDF akses-terbuka OJS (Jurnal Sains Terapan Polban)"):
            break

# ---------- 14 IJCS ----------
if not sudah(14):
    kand = []
    b = get_url("https://ijcs.stmikindonesia.ac.id/ijcs/index.php/ijcs/article/view/3539",
                timeout=(15, 60))
    if b:
        t = b[0].decode("utf-8", "ignore")
        for m in re.finditer(r'href="([^"]*article/(?:download|viewFile)/[^"]+)"', t, re.I):
            kand.append("https://ijcs.stmikindonesia.ac.id/ijcs/index.php/ijcs" + m.group(1))
        for gal in re.findall(r'/article/view/3539/(\d+)', t):
            kand.append(f"https://ijcs.stmikindonesia.ac.id/ijcs/index.php/ijcs/article/download/3539/{gal}")
    print(f"14 kandidat galley: {kand[:4]}", flush=True)
    for u in kand[:6]:
        if unduh_curl(14, u, "PDF akses-terbuka OJS IJCS"):
            break

# ---------- 25 Ali via UNC CDR ----------
if not sudah(25):
    b = get_url("https://cdr.lib.unc.edu/downloads/bc386t01s", timeout=(15, 90))
    print(f"25 cdr bytes: {len(b[0]) if b else 0}", flush=True)
    if b and b[0][:5].startswith(b"%PDF"):
        t = DIR_PDF / "25 - Ali-2015-Keystroke-WiFi-MobiCom.pdf"
        t.write_bytes(b[0])
        catat(25, status="pdf", berkas=str(t), sumber="https://cdr.lib.unc.edu/downloads/bc386t01s",
              catatan="Salinan resmi via Carolina Digital Repository (UNC)")
    else:
        # cari bitstream path dari record
        b2 = get_url("https://cdr.lib.unc.edu/catalog?search_field=all_fields&q=Keystroke+Recognition+Using+WiFi+Signals",
                     timeout=(15, 90))
        print(f"25 catalog bytes: {len(b2[0]) if b2 else 0}", flush=True)

# ---------- 59 Hernandez & Bulut — cari path benar ----------
if not sudah(59):
    for hal in ("https://stevenmhernandez.com/", "https://www.people.vcu.edu/~ebulut/"):
        b = get_url(hal, timeout=(15, 60))
        if not b:
            continue
        t = b[0].decode("utf-8", "ignore")
        for m in re.finditer(r'href="([^"]+\.pdf)"', t, re.I):
            u = urljoin(hal, m.group(1))
            if re.search(r"(wowmom|lightweight|reposition)", u, re.I):
                if unduh_curl(59, u, "Salinan penulis (Hernandez/Bulut)"):
                    break

# ---------- 44 Hakozaki via arXiv API ----------
if not sudah(44):
    try:
        r = requests.get("https://export.arxiv.org/api/query",
                         params={"search_query": 'all:"mouthing" AND all:"sign language" AND all:"avatar"',
                                 "max_results": 20}, headers=HDR, timeout=30)
        t = r.text
        for m in re.finditer(r"<id>(https?://arxiv.org/abs/[^<]+)</id>", t):
            judul = t[m.end():m.end() + 600]
            if re.search(r"mouthing", judul, re.I) and re.search(r"news|avatar", judul, re.I):
                absu = m.group(1)
                pdfu = absu.replace("/abs/", "/pdf/")
                print(f"44 arXiv kandidat: {absu}", flush=True)
                if unduh_curl(44, pdfu, "Preprint resmi arXiv (SLTAT 2025)"):
                    break
    except Exception as e:
        print("44 arXiv err:", e, flush=True)

# ---------- 71 Chow via dspace MIT ----------
if not sudah(71):
    b = get_url("https://dspace.mit.edu/entities/publication/3d09633b-df6a-4051-8915-66bb2ae5b236",
                timeout=(15, 90))
    if b:
        t = b[0].decode("utf-8", "ignore")
        links = [m for m in re.findall(r'href="([^"]+bitstream[^"]+)"', t, re.I)]
        print(f"71 dspace bitstreams: {links[:3]}", flush=True)
        for l in links[:3]:
            if unduh_curl(71, urljoin("https://dspace.mit.edu/", l),
                          "Salinan via MIT DSpace (repository terbuka)"):
                break

print("\n=== STATUS KINI ===", flush=True)
import collections
c = collections.Counter(v.get("status") for k, v in hasil.items() if not k.startswith("_"))
print(c)
