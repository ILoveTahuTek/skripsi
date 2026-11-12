#!/usr/bin/env bash
# Bangun DOCX+PDF v14 (gelombang 14): DP 22 entri, ±30 halaman, diagram v14.
set -e
V10=/home/z/my-project/download/sensesibi-v10
SCR=/home/z/my-project/scripts/sensesibi-v10
G14=$V10/_kerja-g14

# 1) salinan JS khusus g14 (idempoten: selin dari git setiap kali)
cd /home/z/my-project
git checkout -- scripts/sensesibi-v10/parse_md.js scripts/sensesibi-v10/generate_docx.js
cp scripts/sensesibi-v10/parse_md.js scripts/sensesibi-v10/parse_md_g14.js
cp scripts/sensesibi-v10/generate_docx.js scripts/sensesibi-v10/generate_docx_g14.js

python3 - <<'EOF'
from pathlib import Path
scr = Path("/home/z/my-project/scripts/sensesibi-v10")

p = scr / "parse_md_g14.js"
s = p.read_text(encoding="utf-8")
s = s.replace(
    "const SRC = '/home/z/my-project/download/sensesibi-v10/_kerja/split';",
    "const SRC = '/home/z/my-project/download/sensesibi-v10/_kerja-g14/split';")
s = s.replace(
    "const ASSETS = '/home/z/my-project/download/sensesibi-v10/assets';",
    "const ASSETS = '/home/z/my-project/download/sensesibi-v10/assets-v14';")
s = s.replace(
    "const OUTJSON = '/home/z/my-project/scripts/sensesibi-v10/parsed-final.json';",
    "const OUTJSON = '/home/z/my-project/scripts/sensesibi-v10/parsed-g14.json';")
p.write_text(s, encoding="utf-8")

g = scr / "generate_docx_g14.js"
s = g.read_text(encoding="utf-8")
s = s.replace(
    "const parsed = JSON.parse(fs.readFileSync('/home/z/my-project/scripts/sensesibi-v10/parsed-final.json', 'utf-8'));",
    "const parsed = JSON.parse(fs.readFileSync('/home/z/my-project/scripts/sensesibi-v10/parsed-g14.json', 'utf-8'));")
s = s.replace(
    "const OUT = '/home/z/my-project/download/sensesibi-v10/Proposal-SenseSIBI-Studi-Kelayakan-v10.docx';",
    "const OUT = '/home/z/my-project/download/sensesibi-v10/Proposal-SenseSIBI-Studi-Kelayakan-v14.docx';")
# DP satu spasi 10 pt (konvensi kampus, warisan g13)
s = s.replace(
    "function refPara(runs) {\n  return new Paragraph({\n    alignment: AlignmentType.LEFT,\n    indent: { left: 480, hanging: 480 },\n    spacing: { line: 360, after: 120 },\n    children: makeRuns(runs, 24),",
    "function refPara(runs) {\n  return new Paragraph({\n    alignment: AlignmentType.LEFT,\n    indent: { left: 480, hanging: 480 },\n    spacing: { line: 240, after: 40 },\n    children: makeRuns(runs, 20),")
# Sel tabel lebih rapat
s = s.replace(
    "const cellMargins = { top: 40, bottom: 40, left: 80, right: 80 };",
    "const cellMargins = { top: 30, bottom: 30, left: 80, right: 80 };")
s = s.replace(
    "spacing: { line: 276, before: 20, after: 20 },",
    "spacing: { line: 240, before: 16, after: 16 },")
# Heading & butir lebih rapat
s = s.replace("spacing: { before: 360, after: 240, line: 360 },", "spacing: { before: 240, after: 160, line: 360 },")
s = s.replace("spacing: { before: 240, after: 120, line: 360 },", "spacing: { before: 160, after: 80, line: 360 },")
s = s.replace("spacing: { line: 360, after: 60 },\n    children: [new TextRun({ text: n + ' '", "spacing: { line: 360, after: 40 },\n    children: [new TextRun({ text: n + ' '")
# Daftar isi hanya heading 1-2
s = s.replace(
    "new TableOfContents('Daftar Isi', { hyperlink: true, headingStyleRange: '1-3' }),",
    "new TableOfContents('Daftar Isi', { hyperlink: true, headingStyleRange: '1-2' }),")
# Deskripsi dokumen
s = s.replace(
    "description: 'Proposal penelitian BAB I-III + Daftar Pustaka v10 (full-stack Rust, Kokoro TTS on-device, BoM 11 komponen, G0-G4 tiga pilar pakar) \u2014 revisi 9 Nov 2026'",
    "description: 'Proposal penelitian BAB I-III + Daftar Pustaka v14 \u2014 DP 22 entri, \u00b130 halaman, diagram sahih aksesibel (scientific-agent-skills + humanizer-indonesia v1.7, tanpa mitra lembaga) 12 Nov 2026'")
g.write_text(s, encoding="utf-8")
assert "parsed-g14.json" in (scr / "generate_docx_g14.js").read_text(encoding="utf-8")
assert "v14.docx" in (scr / "generate_docx_g14.js").read_text(encoding="utf-8")
assert "assets-v14" in (scr / "parse_md_g14.js").read_text(encoding="utf-8")
print("JS g14 siap.")
EOF

# 2) naskah-untuk-docx = tubuh + DP (tanpa log di bawah penanda AKHIR NASKAH)
python3 - <<'EOF'
from pathlib import Path
src = Path("/home/z/my-project/download/sensesibi-v10/Proposal-SenseSIBI-v14.md").read_text(encoding="utf-8")
mark = "<!-- ===== AKHIR NASKAH"
body = src[:src.index(mark)].rstrip() + "\n"
out = Path("/home/z/my-project/download/sensesibi-v10/_kerja-g14/naskah-untuk-docx.md")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(body, encoding="utf-8")
print("naskah-untuk-docx.md:", len(body), "karakter")
EOF

# 3) split 4 berkas
python3 - <<'EOF'
from pathlib import Path
base = Path("/home/z/my-project/download/sensesibi-v10/_kerja-g14")
teks = (base / "naskah-untuk-docx.md").read_text(encoding="utf-8")
lines = teks.split("\n")
idx = {}
for i, l in enumerate(lines):
    if l.startswith("# "):
        if l.startswith("# BAB I "): idx["bab1"] = i
        elif l.startswith("# BAB II "): idx["bab2"] = i
        elif l.startswith("# BAB III "): idx["bab3"] = i
        elif l.startswith("# DAFTAR PUSTAKA"): idx["dp"] = i
assert set(idx) == {"bab1", "bab2", "bab3", "dp"}, idx
out = {
    "bab1-pendahuluan.md": lines[idx["bab1"]:idx["bab2"]],
    "bab2-kajian-pustaka.md": lines[idx["bab2"]:idx["bab3"]],
    "bab3-metodologi.md": lines[idx["bab3"]:idx["dp"]],
    "daftar-pustaka.md": lines[idx["dp"]:],
}
sd = base / "split"
sd.mkdir(parents=True, exist_ok=True)
for name, ls in out.items():
    (sd / name).write_text("\n".join(ls).rstrip() + "\n", encoding="utf-8")
    print(name, "->", len(ls), "baris")
EOF

# 4) parse + generate
cd "$SCR"
node parse_md_g14.js
node generate_docx_g14.js

# 5) patch gaya TOC1/TOC2 satu spasi di styles.xml (docx-js bawaan menimpa gaya kustom)
python3 - <<'PYEOF'
import zipfile, shutil, re
DOCX = "/home/z/my-project/download/sensesibi-v10/Proposal-SenseSIBI-Studi-Kelayakan-v14.docx"
TMP = DOCX + ".tmp"
with zipfile.ZipFile(DOCX) as zin, zipfile.ZipFile(TMP, "w", zipfile.ZIP_DEFLATED) as zout:
    for item in zin.infolist():
        data = zin.read(item.filename)
        if item.filename == "word/styles.xml":
            s = data.decode("utf-8")
            s = s.replace(
                '<w:style w:type="paragraph" w:styleId="TOC1"><w:name w:val="toc 1"/><w:basedOn w:val="Normal"/><w:next w:val="Normal"/><w:uiPriority w:val="39"/><w:semiHidden/><w:unhideWhenUsed/><w:pPr><w:spacing w:after="100"/></w:pPr></w:style>',
                '<w:style w:type="paragraph" w:styleId="TOC1"><w:name w:val="toc 1"/><w:basedOn w:val="Normal"/><w:next w:val="Normal"/><w:uiPriority w:val="39"/><w:pPr><w:spacing w:before="60" w:after="0" w:line="240" w:lineRule="auto"/></w:pPr></w:style>')
            s = s.replace(
                '<w:style w:type="paragraph" w:styleId="TOC2"><w:name w:val="toc 2"/><w:basedOn w:val="Normal"/><w:next w:val="Normal"/><w:uiPriority w:val="39"/><w:semiHidden/><w:unhideWhenUsed/><w:pPr><w:spacing w:after="100"/><w:ind w:left="240"/></w:pPr></w:style>',
                '<w:style w:type="paragraph" w:styleId="TOC2"><w:name w:val="toc 2"/><w:basedOn w:val="Normal"/><w:next w:val="Normal"/><w:uiPriority w:val="39"/><w:pPr><w:spacing w:after="0" w:line="240" w:lineRule="auto"/><w:ind w:left="240"/></w:pPr></w:style>')
            assert 'TOC1"><w:name w:val="toc 1"/><w:basedOn w:val="Normal"/><w:next w:val="Normal"/><w:uiPriority w:val="39"/><w:pPr><w:spacing w:before="60"' in s, "patch TOC1 gagal"
            data = s.encode("utf-8")
        zout.writestr(item, data)
shutil.move(TMP, DOCX)
print("styles.xml dipatch: TOC1/TOC2 satu spasi")
PYEOF

# 6) PDF via LibreOffice
cd "$V10"
rm -f Proposal-SenseSIBI-Studi-Kelayakan-v14.pdf
soffice --headless --convert-to pdf --outdir "$V10" Proposal-SenseSIBI-Studi-Kelayakan-v14.docx >/dev/null 2>&1
python3 - <<'EOF'
from pypdf import PdfReader
r = PdfReader("/home/z/my-project/download/sensesibi-v10/Proposal-SenseSIBI-Studi-Kelayakan-v14.pdf")
print("PDF halaman:", len(r.pages))
EOF
