#!/usr/bin/env python3
"""Ekstrak 3 blok mermaid dari v14 -> berkas .mmd untuk dirender mmdc."""
import re
from pathlib import Path

MD = Path("/home/z/my-project/download/sensesibi-v10/Proposal-SenseSIBI-v14.md")
OUT = Path("/home/z/my-project/download/sensesibi-v10/diagram-v14")
OUT.mkdir(exist_ok=True)

teks = MD.read_text(encoding="utf-8")
blok = re.findall(r"```mermaid\n(.*?)\n```\n\nGambar (\d+\.\d+)", teks, re.S)
assert len(blok) == 3, f"blok mermaid = {len(blok)}, harus 3"
for isi, num in blok:
    (OUT / f"G{num}.mmd").write_text(isi + "\n", encoding="utf-8")
    assert "accTitle:" in isi and "accDescr:" in isi, f"Gambar {num} tanpa anotasi aksesibilitas"
    print(f"Gambar {num} -> G{num}.mmd ({len(isi.splitlines())} baris, accTitle+accDescr ada)")
print("urutan:", [n for _, n in blok])
