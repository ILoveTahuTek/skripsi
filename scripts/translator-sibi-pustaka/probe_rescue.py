#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
probe_rescue.py — probe paralel kandidat PDF (range-request cek magic) lalu
unduh penuh yang lolos; plus API OA terarah (S2/DOAJ/Unpaywall) untuk DOI sulit.
"""
import concurrent.futures as cf
import json
import subprocess
import sys
import time
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).parent))
from unduh_pustaka import DIR_PDF, HDR, pdf_ok
from data_pustaka import REFS

AKAR = DIR_PDF.parent
HASIL_PATH = AKAR / "_hasil.json"
hasil = json.loads(HASIL_PATH.read_text(encoding="utf-8"))
KEY = {r["no"]: r["key"] for r in REFS}
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")

# kandidat deterministik (URL langsung, tanpa discovery)
KAND = {
    3: ["https://europepmc.org/backend/ftpmc/PMC10785677",
        "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10785677/fullTextPDF",
        "https://www.degruyterbrill.com/document/doi/10.1515/applirev-2021-0120/pdf"],
    14: ["https://ijcs.stmikindonesia.ac.id/ijcs/index.php/ijcs/article/viewFile/3539/298"],
    21: ["https://gzhou.pages.wm.edu/wp-content/blogs.dir/5736/files/sites/13/2017/12/SignFi_IMWUT18.pdf",
         "https://gzhou.pages.wm.edu/wp-content/blogs.dir/5736/files/sites/13/2019/03/SignFi_IMWUT18.pdf",
         "https://gzhou.pages.wm.edu/wp-content/blogs.dir/5736/files/sites/13/2018/10/SignFi_IMWUT18.pdf"],
    25: ["https://cdr.lib.unc.edu/downloads/bc386t01s"],
    48: ["https://jurnal.umj.ac.id/index.php/holistika/article/download/9355/5468"],
    56: ["https://people.math.harvard.edu/~ctm/home/text/ShannonNosie.pdf",
         "https://webusers.imj-prg.fr/~antoine.chambert-loir/enseignement/2020-21/shannon/shannon1949.pdf"],
    59: ["https://ebulutvcu.github.io/Wowmom20-Lightweight.pdf",
         "https://ebulutvcu.github.io/Lightweight20.pdf",
         "https://www.people.vcu.edu/~ebulut/wowmom20-WiFiSensing.pdf"],
    65: ["https://www.cs.temple.edu/~wu/robust17.pdf",
         "https://cis.temple.edu/~wu/robust17.pdf"],
    71: ["https://scispace.com/pdf/on-optimum-recognition-error-and-reject-tradeoff-4ugvowtm6a.pdf",
         "https://cs.nyu.edu/~roweis/csc4520-2006/notes/chow70.pdf"],
    73: ["https://jurnal.mdp.ac.id/index.php/rabit/article/download/8340/4101",
         "https://jurnal.univrab.ac.id/index.php/rabit/article/download/8340"],
    77: ["https://europepmc.org/backend/ftpmc/PMC2859314",
         "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2859314/fullTextPDF"],
    78: ["https://www.site.uottawa.ca/~stan/sokolova/papers/ipm2009.pdf",
         "https://www.site.uottawa.ca/~stan/sokolova/papers/2009-ipm.pdf"],
    69: ["https://www.esf.edu/faculty/mountrakis/Mountrakis_2011_ISPRS.pdf",
         "https://www.sciencedirect.com/science/article/pii/S0924279110001333/pdfft?isDTMRedir=true&download=true"],
}

# DOI yang dicari via API OA terarah
DOIS = {
    18: "10.1016/j.iswa.2024.200384",
    39: "10.1145/3570325",
    43: "10.1007/978-3-031-47362-3_14",
    44: "10.1145/3663547.3759693",
    51: "10.1016/j.procs.2025.08.277",
    53: "10.1016/j.procs.2025.09.042",
    58: "10.1016/j.procs.2024.04.042",
    67: "10.1016/j.measurement.2023.113125",
}


def catat(no, **kw):
    e = hasil.get(str(no), {})
    e.update(kw)
    e["key"] = KEY[no]
    hasil[str(no)] = e
    HASIL_PATH.write_text(json.dumps(hasil, ensure_ascii=False, indent=1, sort_keys=True),
                          encoding="utf-8")
    print(f"{no:02d} [{kw.get('status','?'):8}] {kw.get('sumber','')[:75]}", flush=True)


def curl_magic(u, t=30):
    """Range-request 0-1023 → magic bytes + content-type (file unik per probe)."""
    import uuid
    tmp = f"/tmp/probe_{uuid.uuid4().hex[:8]}.bin"
    try:
        r = subprocess.run(["curl", "-sL", "--max-time", str(t), "-A", UA,
                            "-r", "0-1023", "-o", tmp,
                            "-w", "%{http_code} %{content_type}", u],
                           capture_output=True, timeout=t + 12)
        b = Path(tmp).read_bytes()
        ct = (r.stdout or b"").decode("utf-8", "ignore")
        ok = b[:5].startswith(b"%PDF") or b[:2] == b"PK"
        if not ok:
            print(f"    gagal {u[:70]} | {ct} | {len(b)}B | {b[:40]!r}", flush=True)
        return (b[:5].startswith(b"%PDF"), b[:2] == b"PK", len(b))
    except Exception:
        return (False, False, 0)
    finally:
        Path(tmp).unlink(missing_ok=True)


def unduh_penuh(no, u, catatan):
    t = DIR_PDF / f"{no:02d} - {KEY[no]}.pdf"
    try:
        subprocess.run(["curl", "-sL", "--max-time", "240", "-A", UA,
                       "-o", str(t), u], capture_output=True, timeout=260)
    except Exception:
        return False
    if t.exists() and pdf_ok(t.read_bytes()):
        catat(no, status="pdf", berkas=str(t), sumber=u, catatan=catatan)
        return True
    if t.exists():
        t.unlink()
    return False


def sisa(no):
    return hasil.get(str(no), {}).get("status") != "pdf"


# ---------- 1. probe paralel kandidat deterministik ----------
print("=== PROBE DETERMINISTIK ===", flush=True)
pekerjaan = []
for no, urls in KAND.items():
    if not sisa(no):
        continue
    for u in urls:
        pekerjaan.append((no, u))

with cf.ThreadPoolExecutor(max_workers=10) as ex:
    hasil_probe = dict((i, u) for i, (no, u) in enumerate(pekerjaan))
    fut = {ex.submit(curl_magic, u): (no, u) for no, u in pekerjaan}
    lolos = []
    for f in cf.as_completed(fut, timeout=180):
        no, u = fut[f]
        try:
            pdf, pk, n = f.result()
        except Exception:
            continue
        if pdf or pk:
            lolos.append((no, u))
            print(f"  LULUS {no:02d}: {u[:85]}", flush=True)

print(f"lolos: {len(lolos)}", flush=True)
done = set()
for no, u in lolos:
    if no in done or not sisa(no):
        continue
    if unduh_penuh(no, u, "Salinan legal via repositori penulis/universitas"):
        done.add(no)

# ---------- 2. API OA terarah ----------
print("\n=== API OA (S2 / DOAJ / Unpaywall) ===", flush=True)
API_CAND = {}
for no, doi in DOIS.items():
    if not sisa(no):
        continue
    urls = []
    try:
        r = requests.get(f"https://api.semanticscholar.org/graph/v1/paper/DOI:{doi}",
                         params={"fields": "openAccessPdf"}, headers=HDR, timeout=20)
        oa = (r.json().get("openAccessPdf") or {}).get("url")
        if oa:
            urls.append(oa)
    except Exception:
        pass
    try:
        r = requests.get(f"https://doaj.org/api/search/articles/doi%3A{doi.replace('/', '%2F')}",
                         headers=HDR, timeout=20)
        for bil in r.json().get("results", []):
            for fl in bil.get("bibjson", {}).get("link", []):
                if fl.get("url"):
                    urls.append(fl["url"])
    except Exception:
        pass
    try:
        r = requests.get(f"https://api.unpaywall.org/v2/{doi}?email=peneliti.sibi@gmail.com",
                         headers=HDR, timeout=20)
        j = r.json()
        for loc in ([j.get("best_oa_location")] if j.get("best_oa_location") else []) + (j.get("oa_locations") or [])[:3]:
            if loc and loc.get("url_for_pdf"):
                urls.append(loc["url_for_pdf"])
    except Exception:
        pass
    API_CAND[no] = list(dict.fromkeys(urls))[:4]
    print(f"  {no:02d}: {len(urls)} kandidat API", flush=True)

for no, urls in API_CAND.items():
    for u in urls:
        if not sisa(no) or no in done:
            break
        if unduh_penuh(no, u, "Salinan akses-terbuka via API (S2/DOAJ/Unpaywall)"):
            done.add(no)

print("\n=== STATUS ===", flush=True)
import collections
c = collections.Counter(v.get("status") for k, v in hasil.items() if not k.startswith("_"))
print(c)
print("done:", sorted(done))
