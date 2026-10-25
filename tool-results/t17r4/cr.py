#!/usr/bin/env python3
"""Helper riset T17-R4: kueri Crossref + OpenAlex single-GET, output ringkas."""
import json, sys, time, urllib.request, urllib.parse

UA = {"User-Agent": "Mozilla/5.0 (research subagent T17-R4; mailto:riset.t17r4@example.com)"}

def get(url, tries=3, wait=6):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=40) as r:
                return r.read().decode("utf-8", "replace")
        except Exception as e:
            print(f"  [retry {i+1}] {e}", file=sys.stderr)
            time.sleep(wait)
    return None

def cr_search(q, rows=6, flt=None):
    u = "https://api.crossref.org/works?query.bibliographic=" + urllib.parse.quote(q) + f"&rows={rows}"
    if flt:
        u += "&filter=" + flt
    raw = get(u)
    if not raw:
        return []
    out = []
    for it in json.loads(raw)["message"]["items"]:
        auth = ", ".join(f"{a.get('family','?')}" for a in it.get("author", [])[:4])
        out.append({
            "doi": it.get("DOI"), "title": (it.get("title") or [""])[0],
            "container": (it.get("container-title") or [""])[0], "year": (it.get("issued", {}).get("date-parts", [[None]])[0][0]),
            "authors": auth, "type": it.get("type"), "page": it.get("page"),
        })
    return out

def cr_doi(doi):
    raw = get("https://api.crossref.org/works/" + urllib.parse.quote(doi))
    if not raw:
        return None
    return json.loads(raw)["message"]

def oa_doi(doi):
    """OpenAlex single-work GET: judul + abstrak (inverted index)."""
    raw = get(f"https://api.openalex.org/works/https://doi.org/{doi}?mailto=riset.t17r4@example.com")
    if not raw:
        return None
    d = json.loads(raw)
    inv = d.get("abstract_inverted_index")
    abstract = None
    if inv:
        pos = {}
        for w, ps in inv.items():
            for p in ps:
                pos[p] = w
        abstract = " ".join(pos[i] for i in sorted(pos))
    return {
        "title": d.get("title"), "year": d.get("publication_year"),
        "authors": [a["author"]["display_name"] for a in d.get("authorships", [])],
        "cited_by": d.get("cited_by_count"), "abstract": abstract,
        "oa": (d.get("open_access") or {}).get("is_oa"),
        "venue": ((d.get("primary_location") or {}).get("source") or {}).get("display_name"),
    }

if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "search":
        for r in cr_search(" ".join(sys.argv[2:])):
            print(json.dumps(r, ensure_ascii=False))
    elif cmd == "doi":
        m = cr_doi(sys.argv[2])
        if m:
            print(json.dumps({
                "doi": m.get("DOI"), "title": (m.get("title") or [""])[0],
                "container": (m.get("container-title") or [""])[0],
                "year": m.get("issued", {}).get("date-parts", [[None]])[0][0],
                "authors": [f"{a.get('given','')} {a.get('family','')}" for a in m.get("author", [])],
                "abstract": m.get("abstract"), "page": m.get("page"),
                "event": (m.get("event") or {}).get("name"),
            }, ensure_ascii=False))
    elif cmd == "oa":
        d = oa_doi(sys.argv[2])
        print(json.dumps(d, ensure_ascii=False) if d else "GAGAL")
