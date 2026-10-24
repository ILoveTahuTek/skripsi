#!/usr/bin/env python3
"""verify_sync_dpj.py — Verifikasi sinkronitas DOCX <-> markdown.

Alur: DOCX (hasil regenerasi) -> pandoc GFM -> pembersihan blockquote
(logika sama dengan md_postprocess.py) -> diff terhadap markdown final.
Diff kosong = konten DOCX identik dengan markdown tersunting.
"""
import glob
import re
import subprocess
import sys

TMP = "/home/z/my-project/tmp/sync-check"
OUT = "/home/z/my-project/download/proposal-pengajuan-judul"
MD = "/home/z/my-project/download/markdown"

PAIRS = [
    (f"{OUT}/DPJ-1_Proposal_Judul_Kandang_Ayam_Broiler.docx", f"{MD}/DPJ-1_Kandang-Broiler.md"),
    (f"{OUT}/DPJ-2_Proposal_Judul_Ruang_Kelas_SLB.docx", f"{MD}/DPJ-2_Kelas-SLB.md"),
    (f"{OUT}/DPJ-3_Proposal_Judul_Kamar_Asrama_SLB.docx", f"{MD}/DPJ-3_Asrama-SLB.md"),
    (f"{OUT}/DPJ-4_Proposal_Judul_Translasi_Isyarat_SIBI_BISINDO.docx", f"{MD}/DPJ-4_Isyarat-SIBI-BISINDO.md"),
]

subprocess.run(["mkdir", "-p", TMP], check=True)

PAT_ITEM = re.compile(r"^> (\d+)\\\.")
PAT_SEP = re.compile(r"^>$")

def norm(text):
    """Normalisasi kosmetik: padding kolom tabel (spasi berjalan) tidak dianggap perbedaan konten."""
    out = []
    for ln in text.split("\n"):
        if "|" in ln:
            ln = re.sub(r" {2,}", " ", ln).strip()
            if re.fullmatch(r"[|:\- ]+", ln):
                ln = re.sub(r"-{2,}", "-", ln)
        out.append(ln)
    return "\n".join(out)


fail = False
for docx, mdref in PAIRS:
    name = mdref.split("/")[-1]
    raw = f"{TMP}/{name}"
    subprocess.run(
        ["pandoc", "-f", "docx", "-t", "gfm", "--wrap=none", docx, "-o", raw],
        check=True,
    )
    lines = open(raw, encoding="utf-8").read().split("\n")
    cleaned = []
    for ln in lines:
        m = PAT_ITEM.match(ln)
        if m:
            cleaned.append(f"{m.group(1)}. " + PAT_ITEM.sub("", ln).strip())
        elif PAT_SEP.match(ln):
            cleaned.append("")
        else:
            cleaned.append(ln)
    rebuilt = norm("\n".join(cleaned))
    expected = norm(open(mdref, encoding="utf-8").read())
    if rebuilt == expected:
        print(f"SYNC OK   : {name}")
    else:
        fail = True
        print(f"SYNC FAIL : {name}")
        exp_lines = expected.split("\n")
        new_lines = rebuilt.split("\n")
        shown = 0
        for i, (a, b) in enumerate(zip(exp_lines, new_lines)):
            if a != b:
                print(f"  line {i+1}:")
                print(f"    md : {a[:120]}")
                print(f"    doc: {b[:120]}")
                shown += 1
                if shown >= 5:
                    break
        if len(exp_lines) != len(new_lines):
            print(f"  panjang beda: md={len(exp_lines)} doc={len(new_lines)}")

sys.exit(1 if fail else 0)
