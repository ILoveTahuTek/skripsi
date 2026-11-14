#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Diagnosis selisih verifikasi g20."""
import re
from pathlib import Path
from docx import Document

V10 = Path("/home/z/my-project/download/sensesibi-v10")
md = (V10 / "Proposal-SenseSIBI-v20.md").read_text(encoding="utf-8")
tubuh = md[: md.index("<!-- ===== AKHIR NASKAH")]
print("PERLU DATA: tubuh penuh =", len(re.findall(r"\[PERLU DATA:", tubuh)))
i1 = tubuh.index("# BAB I ")
i2 = tubuh.index("# DAFTAR PUSTAKA")
print("PERLU DATA: BAB I-DP =", len(re.findall(r"\[PERLU DATA:", tubuh[i1:i2])))

md19 = (V10 / "Proposal-SenseSIBI-v19.md").read_text(encoding="utf-8")
t19 = md19[: md19.index("<!-- ===== AKHIR NASKAH")]
print("v19: tubuh penuh =", len(re.findall(r"\[PERLU DATA:", t19)),
      "| BAB I-DP =", len(re.findall(r"\[PERLU DATA:", t19[t19.index("# BAB I "):t19.index("# DAFTAR PUSTAKA")])))

for m in re.finditer(r".{70} — .{70}", tubuh, re.S):
    print("EM DASH:", m.group(0).replace("\n", " | "))

doc = Document(str(V10 / "Proposal-SenseSIBI-Studi-Kelayakan-v20.docx"))
print("doc.tables =", len(doc.tables))
for i, t in enumerate(doc.tables):
    print(i, len(t.rows), "x", len(t.columns), "|", " / ".join(c.text.strip()[:20] for c in t.rows[0].cells)[:88])
