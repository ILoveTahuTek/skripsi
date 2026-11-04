#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""penyelamat8.py — penutup: Garuda utk Rabit, VCU http, DSpace retry, poltekba/polban."""
import html as mod_html
import json
import re
import sys
from pathlib import Path
from urllib.parse import urljoin

import requests

sys.path.insert(0, str(Path(__file__).parent))
from unduh_pustaka import DIR_PDF, HDR, get_url, pdf_ok
from data_pustaka import REFS

KEY = {r["no"]: r["key"] for r in REFS}
HASIL_PATH = DIR_PDF.parent / "_hasil.json"
hasil = json.loads(HASIL_PATH.read_text(encoding="utf-8"))


def catat(no, **kw):
    e = hasil.get(str(no), {})
    e.update(kw)
    e["key"] = KEY[no]
    hasil[str(no)] = e
    print(f"{no:02d} [{kw.get('status','?'):7}] {kw.get('cara','')[:78]}")


def simpan_pdf(no, data, sumber, cara):
    t = DIR_PDF / f"{no:02d} - {KEY[no]}.pdf"
    t.write_bytes(data)
    catat(no, status="pdf", berkas=str(t), sumber=sumber, cara=cara)
    return True


# ---------- 73 Rabit via Garuda ----------
if hasil.get("73", {}).get("status") != "pdf":
    kand = []
    for hal in ("https://garuda.kemdiktisaintek.go.id/journal/view/10473?page=20&issue=vol%2011%20no%202%20(2026):%20juli",
                "https://garuda.kemdiktisaintek.go.id/journal/view/10473"):
        b = get_url(hal, timeout=(15, 90))
        if not b:
            continue
        t = b[0].decode("utf-8", "ignore")
        for m in re.finditer(r'<a[^>]+href="([^"]+)"[^>]*>\s*Full\s*PDF', t, re.I):
            kand.append(urljoin(hal, m.group(1)))
        # blok artikel Safrida → tautan apa pun di dekatnya
        for m in re.finditer(r'safrida.{0,4000}?(href="([^"]+)")', t, re.I | re.S):
            u = mod_html.unescape(m.group(2))
            if re.search(r'(download|\.pdf|article/view/8340)', u, re.I):
                kand.append(urljoin(hal, u))
        if kand:
            break
    print(f"   garuda 73: {len(kand)} kandidat")
    for u in kand[:8]:
        print("      ", u[:112])
    ok = False
    for u in kand[:8]:
        b = get_url(u, timeout=(15, 120))
        if b and pdf_ok(b[0]):
            simpan_pdf(73, b[0], u, "garuda")
            ok = True
            break
    if not ok and kand:
        for u in kand[:4]:
            try:
                wq = requests.get("http://archive.org/wayback/available",
                                  params={"url": u}, headers=HDR, timeout=20)
                j = wq.json().get("archived_snapshots", {}).get("closest", {})
                if j.get("available"):
                    w = f"https://web.archive.org/web/{j['timestamp']}id_/{u}"
                    b = get_url(w, timeout=(15, 120))
                    if b and pdf_ok(b[0]):
                        simpan_pdf(73, b[0], w, "garuda-wayback")
                        ok = True
                        break
            except Exception:
                pass
    if not ok:
        catat(73, status="masih-gagal", cara=f"garuda({len(kand)})")

# ---------- 59 VCU http ----------
if hasil.get("59", {}).get("status") != "pdf":
    for u in ("http://www.people.vcu.edu/~ebulut/wowmom20-WiFiSensing.pdf",
              "https://www.people.vcu.edu/~ebulut/wowmom20-WiFiSensing.pdf"):
        b = get_url(u, timeout=(15, 90))
        if b and pdf_ok(b[0]):
            simpan_pdf(59, b[0], u, "penulis-vcu-http")
            break

# ---------- 71 DSpace retry ----------
if hasil.get("71", {}).get("status") != "pdf":
    for u in ("https://dspace.mit.edu/bitstream/handle/1721.1/6177/AIM-175.pdf?sequence=1&isAllowed=y",
              "https://dspace.mit.edu/bitstream/handle/1721.1/6177/AIM-175.pdf"):
        b = get_url(u, timeout=(15, 90))
        if b and pdf_ok(b[0]):
            simpan_pdf(71, b[0], u, "mit-dspace-2")
            break
    else:
        try:
            r = requests.get("https://web.archive.org/cdx/search/cdx",
                             params={"url": "dspace.mit.edu/bitstream/handle/1721.1/6177*",
                                     "output": "json", "limit": 8, "filter": "statuscode:200"},
                             headers=HDR, timeout=40)
            snap = [(row[1], row[2]) for row in r.json()[1:]] if (r.text or "").strip() else []
            print(f"   cdx 71: {len(snap)} snapshot")
            for ts, asli in snap[:5]:
                print("      ", asli[:104])
                w = f"https://web.archive.org/web/{ts}id_/{asli}"
                b = get_url(w, timeout=(15, 120))
                if b and pdf_ok(b[0]):
                    simpan_pdf(71, b[0], w, "cdx-dspace")
                    break
        except Exception as e:
            print("   cdx 71 err", type(e).__name__)

# ---------- 12 polban / poltekba alternatif ----------
if hasil.get("12", {}).get("status") != "pdf":
    kand = []
    for hal in ("https://jurnal.polban.ac.id/index.php/jst/article/view/732",
                "https://jurnal.polban.ac.id/index.php/jst/article/view/732/603"):
        b = get_url(hal, timeout=(15, 60))
        if b and b[0]:
            t = b[0].decode("utf-8", "ignore")
            for u in re.findall(r'href="([^"]+)"', t, re.I):
                if re.search(r'(/article/(view|download)/732(/\d+)?|\.pdf|viewFile)', u, re.I):
                    u2 = urljoin(hal, mod_html.unescape(u))
                    kand.append(u2.replace("/article/view/", "/article/download/"))
        if kand:
            break
    print(f"   polban 12: {len(kand)} kandidat")
    for u in kand[:8]:
        print("      ", u[:112])
    ok = False
    for u in kand[:8]:
        b = get_url(u, timeout=(15, 90))
        if b and pdf_ok(b[0]):
            simpan_pdf(12, b[0], u, "polban")
            ok = True
            break
    if not ok:
        catat(12, status="masih-gagal", cara="polban")

HASIL_PATH.write_text(json.dumps(hasil, ensure_ascii=False, indent=1, sort_keys=True),
                      encoding="utf-8")
n = {}
for v in hasil.values():
    n[v.get("status", "?")] = n.get(v.get("status", "?"), 0) + 1
print("\n=== RINGKASAN PUTARAN 8 ===")
for k in sorted(n):
    print(f"{k:16}: {n[k]}")
