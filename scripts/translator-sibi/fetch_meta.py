import json, urllib.request, time

DOIS = {
    "wisign2020": "10.1145/3377553",
    "wikey2015": "10.1145/2789168.2790109",
    "mosleh2022": "10.1109/access.2022.3230003",
    "mursita2015": "10.14421/ijds.2202",
    "picron2024": "10.1007/978-3-031-47362-3_14",
    "hakozaki2025": "10.1145/3663547.3759693",
    "rabit2026": "10.36341/rabit.v11i2.8340",
}

out = {}
for key, doi in DOIS.items():
    try:
        with urllib.request.urlopen(f"https://api.crossref.org/works/{doi}", timeout=30) as r:
            d = json.load(r)["message"]
        out[key] = {
            "doi": d["DOI"],
            "title": d.get("title", [""])[0],
            "container": d.get("container-title", [""])[0] if d.get("container-title") else "",
            "volume": d.get("volume", ""),
            "issue": d.get("issue", ""),
            "pages": d.get("page", "") or d.get("article-number", ""),
            "year": d.get("issued", {}).get("date-parts", [[None]])[0][0],
            "authors": [(a.get("family", ""), a.get("given", "")) for a in d.get("author", [])],
            "type": d.get("type", ""),
        }
    except Exception as e:
        out[key] = {"error": str(e)}
    time.sleep(0.4)

# Rakun search
try:
    url = "https://api.crossref.org/works?query.bibliographic=heuristic+hidden+markov+model+inflectional+words+SIBI+Rakun&rows=5"
    with urllib.request.urlopen(url, timeout=30) as r:
        items = json.load(r)["message"]["items"]
    out["rakun_search"] = [{"doi": i.get("DOI"), "title": (i.get("title") or [""])[0][:100],
                            "container": (i.get("container-title") or [""])[0][:60] if i.get("container-title") else "",
                            "year": i.get("issued", {}).get("date-parts", [[None]])[0][0],
                            "authors": [a.get("family", "") for a in i.get("author", [])][:4]} for i in items]
except Exception as e:
    out["rakun_search"] = {"error": str(e)}

with open("meta_rujukan_baru.json", "w") as f:
    json.dump(out, f, indent=1, ensure_ascii=False)
print(json.dumps(out, indent=1, ensure_ascii=False))
