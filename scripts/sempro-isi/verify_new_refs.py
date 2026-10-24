#!/usr/bin/env python3
"""Verifikasi rujukan baru untuk pengisian penanda sempro DPJ-4 SIBI-CSI.

Sumber: Crossref (metadata bibliografis) + Semantic Scholar (abstrak).
Skema keluaran: JSON per kunci, mirip verify_dpj4_refs.py sesi sebelumnya.
Jalankan: python3 /home/z/my-project/scripts/sempro-isi/verify_new_refs.py
"""
import json
import os
import time
import urllib.request
import urllib.error

OUT_DIR = "/home/z/my-project/scripts/sempro-isi/crossref"
SS_DIR = "/home/z/my-project/scripts/sempro-isi/ss"
os.makedirs(OUT_DIR, exist_ok=True)
os.makedirs(SS_DIR, exist_ok=True)

# DOI yang akan diverifikasi bibliografinya (rujukan BARU + beberapa lama yang perlu detail).
DOI_LIST = {
    "stokoe2005_reprint": "10.1093/deafed/eni001",
    "cortes1995_svm": "10.1007/BF00994018",
    "kiranyaz2021_1dcnn": "10.1016/j.ymssp.2020.107398",
    "sigrist2013_feedback": "10.3758/s13423-012-0333-8",
    "bowen2009_feasibility": "10.1016/j.amepre.2009.02.002",
    "sokolova2009_metrics": "10.1016/j.ipm.2008.09.017",
    "chow1970_reject": "10.1109/TIT.1970.1054508",
    "mountrakis2011_svm": "10.1016/j.isprsjprs.2010.11.001",
    "zheng2023_pose_survey": "10.1145/3542695",
    "shannon1949_nyquist": "10.1109/JRPROC.1949.232969",
    "nyquist1928": "10.1109/T-AIEE.1928.5055024",
    "hassan2026_asl_ai": "10.1145/3772318.3791928",
    "likert1932_attitudes": None,  # monograf, tanpa DOI - sitasi klasik
    "kamus_sibi_1994": None,      # terbitan resmi Depdikbud, tanpa DOI
    "kemenko2025_selaras": None,  # rilis web resmi, tanpa DOI
}

# DOI yang abstraknya dibutuhkan (perangkat/bahasa/kosakata).
SS_LIST = {
    "shang2017_wisign": "10.1145/3097620.3097624",
    "handfi2024": "10.1016/j.procs.2024.04.042",
    "dfwislr2020": "10.1016/j.pmcj.2020.101289",
    "dwijayanti2021": "10.14569/IJACSA.2021.0121046",
    "hao2020_wisl": "10.3390/s20144025",
    "ma2018_signfi": "10.1145/3191755",
}

HDRS = {"User-Agent": "SemproDPJ4-RefVerifier/1.0 (mailto:peneliti@example.org)"}


def get_json(url, tries=4):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers=HDRS)
            with urllib.request.urlopen(req, timeout=40) as r:
                return json.loads(r.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code in (429, 503):
                wait = 15 * (i + 1)
                print(f"  429/503, tunggu {wait}s ...")
                time.sleep(wait)
            else:
                print(f"  HTTP {e.code}")
                return None
        except Exception as e:  # noqa: BLE001
            print(f"  ERR {e}")
            time.sleep(5)
    return None


def crossref_one(key, doi):
    out = os.path.join(OUT_DIR, f"{key}.json")
    if os.path.exists(out):
        print(f"[skip] {key} sudah ada")
        return
    d = get_json(f"https://api.crossref.org/works/{doi}")
    if d and "message" in d:
        m = d["message"]
        rec = {
            "DOI": doi,
            "title": (m.get("title") or [""])[0],
            "container": (m.get("container-title") or [""])[:1],
            "authors": [
                f"{a.get('family','')}, {a.get('given','')}".strip(", ")
                for a in m.get("author", [])
            ],
            "year": (m.get("issued", {}).get("date-parts") or [[None]])[0][0],
            "volume": m.get("volume"),
            "issue": m.get("issue"),
            "pages": m.get("page"),
            "publisher": m.get("publisher"),
        }
        with open(out, "w") as f:
            json.dump(rec, f, ensure_ascii=False, indent=1)
        print(f"[ok] {key}: {rec['title'][:70]}")
    else:
        with open(out, "w") as f:
            json.dump({"DOI": doi, "error": "gagal ambil"}, f)
        print(f"[GAGAL] {key} ({doi})")


def ss_one(key, doi):
    out = os.path.join(SS_DIR, f"{key}.json")
    if os.path.exists(out):
        print(f"[skip] {key} sudah ada")
        return
    d = get_json(
        f"https://api.semanticscholar.org/graph/v1/paper/DOI:{doi}"
        "?fields=title,abstract,year,authors,venue"
    )
    if d:
        with open(out, "w") as f:
            json.dump(d, f, ensure_ascii=False, indent=1)
        ab = (d.get("abstract") or "")[:80].replace("\n", " ")
        print(f"[ok] {key}: {d.get('title','')[:60]} | abstrak: {ab}")
    else:
        with open(out, "w") as f:
            json.dump({"DOI": doi, "error": "gagal ambil"}, f)
        print(f"[GAGAL] {key} ({doi})")


def main():
    print("=== Crossref ===")
    for key, doi in DOI_LIST.items():
        if doi is None:
            print(f"[tanpa-doi] {key}")
            continue
        crossref_one(key, doi)
        time.sleep(1.2)
    print("=== Semantic Scholar ===")
    for key, doi in SS_LIST.items():
        ss_one(key, doi)
        time.sleep(2.5)
    print("selesai")


if __name__ == "__main__":
    main()
