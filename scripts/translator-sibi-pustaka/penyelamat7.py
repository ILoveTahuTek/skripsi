#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""penyelamat7.py — sentuhan akhir: VCU via get_url (SSL fallback), DSpace entity, jina poltekba."""
import json
import re
import sys
from pathlib import Path

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


# 59 VCU (get_url punya fallback verify=False)
if hasil.get("59", {}).get("status") != "pdf":
    b = get_url("https://www.people.vcu.edu/~ebulut/wowmom20-WiFiSensing.pdf", timeout=(15, 90))
    if b and pdf_ok(b[0]):
        simpan_pdf(59, b[0], b[2], "penulis-vcu")
    else:
        print("   vcu 59: gagal via get_url")

# 71 MIT DSpace entity via get_url (SSL fallback)
if hasil.get("71", {}).get("status") != "pdf":
    kand = []
    b = get_url("https://dspace.mit.edu/entities/publication/3d09633b-df6a-4051-8915-66bb2ae5b236",
                timeout=(15, 90))
    if b:
        t = b[0].decode("utf-8", "ignore")
        print(f"   dspace entity 71: len={len(t)}")
        for u in re.findall(r'(?:href|src)="([^"]+)"', t, re.I):
            if "bitstream" in u.lower() or "aim-175" in u.lower():
                kand.append(u if u.startswith("http") else "https://dspace.mit.edu" + u)
        for u in kand[:6]:
            print("      ", u[:110])
    for u in kand[:6]:
        b2 = get_url(u, timeout=(15, 90))
        if b2 and pdf_ok(b2[0]):
            simpan_pdf(71, b2[0], u, "mit-dspace")
            break

# 12 poltekba via jina — dump teks 600 karakter tengah
try:
    r = requests.get("https://r.jina.ai/https://jurnal.poltekba.ac.id/index.php/jst/article/view/732",
                     headers=HDR, timeout=(15, 90))
    print(f"   jina poltekba: {r.status_code} len={len(r.text or '')}")
    if r.status_code == 200 and r.text:
        t = r.text
        for u in re.findall(r'\((https?://[^\s)]+)\)', t):
            if re.search(r'/article/(view|download)/732(/\d+)?|\.pdf', u, re.I):
                print("      jina-link:", u[:110])
        i = t.lower().find("pdf")
        if i >= 0:
            print("      konteks:", t[max(0, i - 150):i + 150].replace("\n", " ")[:280])
except Exception as e:
    print("   jina poltekba err", type(e).__name__)

HASIL_PATH.write_text(json.dumps(hasil, ensure_ascii=False, indent=1, sort_keys=True),
                      encoding="utf-8")
n = {}
for v in hasil.values():
    n[v.get("status", "?")] = n.get(v.get("status", "?"), 0) + 1
print("\n=== RINGKASAN ===")
for k in sorted(n):
    print(f"{k:16}: {n[k]}")
