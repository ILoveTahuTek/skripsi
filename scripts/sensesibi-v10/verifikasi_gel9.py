#!/usr/bin/env python3
"""Verifikasi integritas gelombang 9: sitasi, angka, struktur pra vs pasca."""
import re

def load(p, n=1290):
    with open(p, encoding="utf-8") as f:
        return f.readlines()[:n]

pra = load("/tmp/pra.md")
pas = load("/home/z/my-project/download/sensesibi-v10/Proposal-SenseSIBI-v10.md")

def body_citations(lines):
    """Sitasi unik di badan naskah (sebelum DAFTAR PUSTAKA)."""
    dp = next(i for i, l in enumerate(lines) if l.startswith("# DAFTAR PUSTAKA"))
    text = "".join(lines[:dp])
    cites = set()
    for m in re.finditer(r"\[(\d+(?:\s*,\s*\d+)*)\]", text):
        for c in m.group(1).split(","):
            cites.add(int(c.strip()))
    return cites

def numbers_multiset(lines):
    """Multiset token numerik di badan naskah (digit & persen & satuan)."""
    dp = next(i for i, l in enumerate(lines) if l.startswith("# DAFTAR PUSTAKA"))
    text = "".join(lines[:dp])
    text = re.sub(r"\[\d+(?:\s*,\s*\d+)*\]", "", text)  # buang sitasi
    toks = re.findall(r"\d+[.,]?\d*", text)
    from collections import Counter
    return Counter(toks)

def structure(lines):
    h2 = sum(1 for l in lines if l.startswith("## ") and not l.startswith("## Log"))
    h3 = sum(1 for l in lines if l.startswith("### "))
    bab = sum(1 for l in lines if re.match(r"^# BAB", l))
    tabel = sum(1 for l in lines if re.match(r"^\*\*Tabel \d", l) or re.match(r"^Tabel \d", l))
    gambar = sum(1 for l in lines if re.match(r"^\*\*Gambar G?3", l) or re.match(r"^Gambar G?3", l))
    mermaid = sum(1 for l in lines if l.strip().startswith("```mermaid"))
    perlu = sum(1 for l in lines if "PERLU DATA" in l)
    return dict(bab=bab, h2=h2, h3=h3, tabel=tabel, gambar=gambar, mermaid=mermaid, perlu_data=perlu)

cp, cs = body_citations(pra), body_citations(pas)
print(f"SITASI UNIK BADAN: pra={len(cp)} pasca={len(cs)} | hilang={sorted(cp-cs)} | baru={sorted(cs-cp)}")
assert cp == cs, "SITASI BERUBAH!"

np_, ns = numbers_multiset(pra), numbers_multiset(pas)
diff = {k: (np_.get(k,0), ns.get(k,0)) for k in set(np_) | set(ns) if np_.get(k,0) != ns.get(k,0)}
print(f"TOKEN NUMERIK berubah: {diff if diff else 'TIDAK ADA'}")

sp, ss = structure(pra), structure(pas)
print(f"STRUKTUR pra : {sp}")
print(f"STRUKTUR pasca: {ss}")
assert sp == ss, "STRUKTUR BERUBAH!"
print("\nLOLOS: sitasi, angka, dan struktur utuh.")
