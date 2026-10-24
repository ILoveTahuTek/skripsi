#!/usr/bin/env python3
"""Post-process pandoc GFM output for DPJ markdown files.

Transforms pandoc's blockquote-wrapped explicit numbered paragraphs
(`> 1\\.` / `>` separator lines) into plain GFM ordered lists, so the
markdown reads naturally:
  > 1\\. Bagaimana ...   ->  1. Bagaimana ...
  >                      ->  (empty line)

Everything else is left untouched.
"""
import glob
import re

FILES = sorted(glob.glob("/home/z/my-project/download/markdown/DPJ-*.md"))
PAT_ITEM = re.compile(r"^> (\d+)\\\.")
PAT_SEP = re.compile(r"^>$")

total_items = 0
total_seps = 0

for path in FILES:
    with open(path, encoding="utf-8") as fh:
        lines = fh.read().split("\n")
    out = []
    items = seps = 0
    for ln in lines:
        m = PAT_ITEM.match(ln)
        if m:
            out.append(f"{m.group(1)}. " + PAT_ITEM.sub("", ln).strip())
            items += 1
        elif PAT_SEP.match(ln):
            out.append("")
            seps += 1
        else:
            out.append(ln)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(out))
    total_items += items
    total_seps += seps
    print(f"{path}: {items} list items fixed, {seps} separators cleaned")

print(f"TOTAL: {total_items} items, {total_seps} separators across {len(FILES)} files")
