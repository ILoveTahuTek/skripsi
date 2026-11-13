#!/usr/bin/env python3
"""patch_footers.py — WPS compatibility post-processing per docx skill toc.md:
1. Footer PAGE fields get explicit format switches (ROMAN for front matter, arabic for body).
2. Remove empty <w:pgNumType/> from document.xml (cover section).
Usage: python3 patch_footers.py <file.docx> <roman_footer_idx> <arabic_footer_idx>
Footer indexes refer to footerN.xml files that contain PAGE instrText, in document order.
Simpler robust approach: patch every footerN.xml — if the section uses Roman fmt, we cannot know
from the footer alone; instead we rely on ordering: docx-js writes footers in section order.
We therefore accept explicit indexes found by scanning document.xml sectPr references.
"""
import re, shutil, sys, zipfile, os, tempfile

def main():
    path = sys.argv[1]
    tmp = tempfile.mkdtemp()
    with zipfile.ZipFile(path) as z:
        z.extractall(tmp)

    docxml_path = os.path.join(tmp, "word", "document.xml")
    with open(docxml_path, encoding="utf-8") as f:
        doc = f.read()
    # 1. strip empty pgNumType
    doc, n_removed = re.subn(r"<w:pgNumType/>", "", doc)

    # 1b. dedupe TOC first entry: the field paragraph (with hyperlink) already
    # renders entry #1; the injected plain duplicate right after it is removed,
    # and the unresolved PAGEREF gets a cached page result.
    def dedupe_toc(xml):
        m = re.search(
            r'(<w:p>(?:(?!</w:p>).)*?instrText[^>]*>\s*TOC[^<]*</w:instrText>(?:(?!</w:p>).)*?</w:p>)',
            xml, flags=re.S)
        if not m:
            return xml, "no TOC field para"
        field_para = m.group(1)
        texts = re.findall(r"<w:t[^>]*>([^<]*)</w:t>", field_para)
        entry_text = texts[0].strip() if texts else ""
        # the inner PAGEREF is one merged run (begin+instr+separate+end) — split it
        # into valid runs and add a cached page result "1"
        fp2, n_cached = re.subn(
            r'<w:r>(<w:fldChar w:fldCharType="begin"[^>]*/>)'
            r'(<w:instrText[^>]*>\s*PAGEREF[^<]*</w:instrText>)'
            r'(<w:fldChar w:fldCharType="separate"/>)'
            r'(<w:fldChar w:fldCharType="end"/>)</w:r>',
            r'<w:r>\1</w:r><w:r>\2</w:r><w:r>\3</w:r>'
            r'<w:r><w:t>1</w:t></w:r><w:r>\4</w:r>',
            field_para, count=1)
        # find the paragraph immediately following and drop it if text matches
        after = xml[m.end():]
        pm = re.match(r"\s*<w:p>(?:(?!</w:p>).)*?</w:p>", after, flags=re.S)
        msg = f"PAGEREF split+cached: {n_cached}"
        if pm:
            cand = pm.group(0)
            cand_texts = [t.strip() for t in re.findall(r"<w:t[^>]*>([^<]*)</w:t>", cand)]
            if cand_texts and cand_texts[0] == entry_text:
                xml = xml[:m.start()] + fp2 + after[pm.end():]
                return xml, msg + f"; deduped '{entry_text}'"
        xml = xml[:m.start()] + fp2 + xml[m.end():]
        return xml, msg + f" (no dup for '{entry_text}')"

    doc, toc_msg = dedupe_toc(doc)

    # map: section order -> footer rIds (default footer)
    sect_footers = []
    for sect in re.findall(r"<w:sectPr.*?</w:sectPr>|<w:sectPr[^>]*/>", doc, flags=re.S):
        m = re.search(r'<w:footerReference w:type="default" r:id="(rId\d+)"', sect)
        sect_footers.append(m.group(1) if m else None)
    with open(docxml_path, "w", encoding="utf-8") as f:
        f.write(doc)

    rels_path = os.path.join(tmp, "word", "_rels", "document.xml.rels")
    with open(rels_path, encoding="utf-8") as f:
        rels = f.read()
    rid2file = dict(re.findall(r'Id="(rId\d+)"[^>]*Target="(footer\d+\.xml)"', rels))

    # sections: index 0 = cover (no footer), 1 = TOC (roman), 2 = body (arabic)
    def patch(fname, fmt):
        fpath = os.path.join(tmp, "word", fname)
        if not os.path.exists(fpath):
            return False
        with open(fpath, encoding="utf-8") as f:
            xml = f.read()
        xml, n = re.subn(
            r"(<w:instrText[^>]*>)\s*PAGE\s*(</w:instrText>)",
            r"\1 PAGE \\* " + fmt + r" \\* MERGEFORMAT \2",
            xml)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(xml)
        return n > 0

    done = []
    if len(sect_footers) >= 3:
        roman_rid, arabic_rid = sect_footers[1], sect_footers[2]
        if roman_rid and rid2file.get(roman_rid):
            done.append((rid2file[roman_rid], "ROMAN", patch(rid2file[roman_rid], "ROMAN")))
        if arabic_rid and rid2file.get(arabic_rid):
            done.append((rid2file[arabic_rid], "arabic", patch(rid2file[arabic_rid], "arabic")))

    # rezip
    out = path
    if os.path.exists(out):
        os.remove(out)
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for root, _, files in os.walk(tmp):
            for fn in files:
                full = os.path.join(root, fn)
                z.write(full, os.path.relpath(full, tmp))
    shutil.rmtree(tmp)
    print(f"pgNumType removed: {n_removed}; TOC patch: {toc_msg}; footer patches: {done}")

if __name__ == "__main__":
    main()
