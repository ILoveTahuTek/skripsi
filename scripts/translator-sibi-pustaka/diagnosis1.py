#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Diagnosis kegagalan putaran 1: GitHub, MDPI, EPMC, metadata OA, OJS."""
import html as H
import re
import time

import requests

HDR = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                     "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
       "Accept-Language": "en-US,en;q=0.9,id;q=0.8"}
EMAIL = "pustaka.sibi.riset@gmail.com"

print("== GITHUB ==")
try:
    r = requests.get("https://api.github.com/rate_limit", headers=HDR, timeout=15)
    print("rate_limit:", r.status_code, r.json().get("resources", {}).get("core"))
except Exception as e:
    print("rate_limit ERR", type(e).__name__)
for repo in ["espressif/esp-csi", "espressif/esp-nn", "espressif/esp-dl",
             "espressif/tflite-micro-esp-examples", "SYSTRAN/faster-whisper"]:
    for br in ("master", "main"):
        try:
            with requests.get(f"https://codeload.github.com/{repo}/zip/refs/heads/{br}",
                              headers=HDR, timeout=(10, 25), stream=True) as r:
                print(f"  {repo.split('/')[-1]} {br}:", r.status_code,
                      r.headers.get("Content-Length", "?"))
        except Exception as e:
            print(f"  {repo.split('/')[-1]} {br} ERR", type(e).__name__)

print("\n== MDPI ==")
for u in ["https://www.mdpi.com/1424-8220/24/11/3414/pdf",
          "https://www.mdpi.com/1424-8220/20/14/4025/pdf"]:
    try:
        r = requests.get(u, headers=HDR, timeout=30)
        print(" ", u[24:50], r.status_code, (r.headers.get("Content-Type") or "")[:30],
              repr(r.content[:40]))
    except Exception as e:
        print(" ", u[24:50], "ERR", type(e).__name__)

print("\n== EPMC ==")
for doi in ["10.1016/j.amepre.2009.02.002", "10.3390/s24113414",
            "10.3390/s20144025", "10.1037/tmb0000030"]:
    try:
        r = requests.get("https://www.ebi.ac.uk/europepmc/webservices/rest/search",
                         params={"query": f'DOI:"{doi}"', "format": "json", "pageSize": 1},
                         headers=HDR, timeout=20)
        res = (r.json().get("resultList") or {}).get("result") or []
        if res:
            print(" ", doi, "->", res[0].get("pmcid"), "| OA:", res[0].get("isOpenAccess"),
                  "| inEPMC:", res[0].get("inEPMC"))
        else:
            print(" ", doi, "-> tidak terindeks")
    except Exception as e:
        print(" ", doi, "ERR", type(e).__name__)

DOIS = ["10.1353/sls.2004.0005", "10.1353/sls.2005.0004", "10.1515/applirev-2021-0120",
        "10.1093/jdsade/enaf059", "10.1016/j.iswa.2024.200384", "10.1037/tmb0000030",
        "10.1145/3310194", "10.1145/3191755", "10.1109/TENCON61640.2024.10903008",
        "10.1145/3377553", "10.1145/2789168.2790109", "10.1109/ACCESS.2022.3230003",
        "10.1145/3570325", "10.1109/TPAMI.2021.3105387", "10.1145/3663547.3759693",
        "10.1093/deafed/eni001", "10.1016/j.procs.2025.08.277", "10.1016/j.procs.2025.09.042",
        "10.1016/j.procs.2024.04.042", "10.1109/WoWMoM49955.2020.00056",
        "10.1145/3097620.3097624", "10.1109/IAICT52856.2021.9532548",
        "10.1016/j.measurement.2023.113125", "10.1007/BF00994018",
        "10.1016/j.isprsjprs.2010.11.001", "10.1109/TIT.1970.1054406",
        "10.36341/rabit.v11i2.8340", "10.1109/TIMEE.2015.7389747",
        "10.1109/ICEEI47359.2019.8988806", "10.1145/641007.641035",
        "10.1016/j.amepre.2009.02.002", "10.1016/j.ipm.2009.03.002",
        "10.1109/T-AIEE.1928.5055024", "10.1109/JRPROC.1949.232969",
        "10.14421/ijds.2202", "10.33022/ijcs.v12i6.3539", "10.24853/holistika.5.1.28-33"]

print("\n== METADATA OA (pdf|landing) ==")
for doi in DOIS:
    upw, oa, s2u = [], [], None
    try:
        r = requests.get(f"https://api.unpaywall.org/v2/{doi}",
                         params={"email": EMAIL}, headers=HDR, timeout=20)
        if r.status_code == 200:
            for l in (r.json().get("oa_locations") or []):
                if l.get("url_for_pdf"):
                    upw.append(l["url_for_pdf"])
                elif l.get("url"):
                    upw.append("(l)" + l["url"])
    except Exception:
        pass
    try:
        r = requests.get(f"https://api.openalex.org/works/doi:{doi}",
                         params={"mailto": EMAIL}, headers=HDR, timeout=20)
        if r.status_code == 200:
            for l in (r.json().get("locations") or []):
                if l.get("pdf_url"):
                    oa.append(l["pdf_url"])
                elif l.get("landing_page_url"):
                    oa.append("(l)" + l["landing_page_url"])
    except Exception:
        pass
    try:
        r = requests.get(f"https://api.semanticscholar.org/graph/v1/paper/DOI:{doi}",
                         params={"fields": "openAccessPdf"}, headers=HDR, timeout=20)
        if r.status_code == 200:
            s2u = (r.json().get("openAccessPdf") or {}).get("url")
    except Exception:
        pass
    time.sleep(1.0)
    print(f"[{doi}]")
    print("   upw:", " ; ".join(upw[:3])[:170] or "-")
    print("   oa :", " ; ".join(oa[:3])[:170] or "-")
    print("   s2 :", (s2u or "-")[:150])

print("\n== OJS LANDING ==")
for doi in ["10.14421/ijds.2202", "10.32487/jst.v5i2.732", "10.33022/ijcs.v12i6.3539",
            "10.24853/holistika.5.1.28-33", "10.36341/rabit.v11i2.8340"]:
    try:
        r = requests.get(f"https://doi.org/{doi}", headers=HDR,
                         timeout=(10, 60), allow_redirects=True)
        kand = []
        m = re.search(r'citation_pdf_url[^>]*content=["\']([^"\']+)["\']', r.text, re.I)
        if m:
            kand.append("META:" + H.unescape(m.group(1)))
        for u in re.findall(r'href=["\']([^"\']+)["\']', r.text, re.I):
            if re.search(r'(viewFile|/download/|\.pdf)', u, re.I):
                kand.append(u[:100])
        print(" ", doi, r.status_code, r.url[:78])
        for k in kand[:6]:
            print("     ", k[:115])
    except Exception as e:
        print(" ", doi, "ERR", type(e).__name__, str(e)[:70])
