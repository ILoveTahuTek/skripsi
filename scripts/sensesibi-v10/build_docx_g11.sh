#!/usr/bin/env bash
# Bangun DOCX+PDF v11 (gelombang 11): salin JS, patch jalur/aset/TOC/DP, split, parse, generate, PDF.
set -e
V10=/home/z/my-project/download/sensesibi-v10
SCR=/home/z/my-project/scripts/sensesibi-v10

# 1) salinan JS khusus g11 (idempoten: selin dari git setiap kali)
cd /home/z/my-project
git checkout -- scripts/sensesibi-v10/parse_md.js scripts/sensesibi-v10/generate_docx.js
cp scripts/sensesibi-v10/parse_md.js scripts/sensesibi-v10/parse_md_g11.js
cp scripts/sensesibi-v10/generate_docx.js scripts/sensesibi-v10/generate_docx_g11.js

python3 - <<'EOF'
from pathlib import Path
scr = Path("/home/z/my-project/scripts/sensesibi-v10")

p = scr / "parse_md_g11.js"
s = p.read_text(encoding="utf-8")
s = s.replace(
    "const SRC = '/home/z/my-project/download/sensesibi-v10/_kerja/split';",
    "const SRC = '/home/z/my-project/download/sensesibi-v10/_kerja-g11/split';")
s = s.replace(
    "const ASSETS = '/home/z/my-project/download/sensesibi-v10/assets';",
    "const ASSETS = '/home/z/my-project/download/sensesibi-v10/assets-ringkas';")
s = s.replace(
    "const OUTJSON = '/home/z/my-project/scripts/sensesibi-v10/parsed-final.json';",
    "const OUTJSON = '/home/z/my-project/scripts/sensesibi-v10/parsed-g11.json';")
p.write_text(s, encoding="utf-8")

g = scr / "generate_docx_g11.js"
s = g.read_text(encoding="utf-8")
s = s.replace(
    "const parsed = JSON.parse(fs.readFileSync('/home/z/my-project/scripts/sensesibi-v10/parsed-final.json', 'utf-8'));",
    "const parsed = JSON.parse(fs.readFileSync('/home/z/my-project/scripts/sensesibi-v10/parsed-g11.json', 'utf-8'));")
s = s.replace(
    "const OUT = '/home/z/my-project/download/sensesibi-v10/Proposal-SenseSIBI-Studi-Kelayakan-v10.docx';",
    "const OUT = '/home/z/my-project/download/sensesibi-v10/Proposal-SenseSIBI-Studi-Kelayakan-v11.docx';")
# DP satu spasi 10 pt (konvensi kampus)
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
    "description: 'Proposal penelitian BAB I-III + Daftar Pustaka v11 \u2014 revisi masukan dosen pembimbing (register mahasiswa, konteks Jawa Timur, DP 46 entri) 10 Nov 2026'")
g.write_text(s, encoding="utf-8")
assert "parsed-g11.json" in (scr / "generate_docx_g11.js").read_text(encoding="utf-8")
assert "v11.docx" in (scr / "generate_docx_g11.js").read_text(encoding="utf-8")
assert "line: 240, after: 40" in (scr / "generate_docx_g11.js").read_text(encoding="utf-8")
assert "makeRuns(runs, 20)" in (scr / "generate_docx_g11.js").read_text(encoding="utf-8")
assert "headingStyleRange: '1-2'" in (scr / "generate_docx_g11.js").read_text(encoding="utf-8")
print("JS g11 siap.")
EOF

# 2) naskah-untuk-docx = tubuh + DP (tanpa log di bawah penanda AKHIR NASKAH)
python3 - <<'EOF'
from pathlib import Path
src = Path("/home/z/my-project/download/sensesibi-v10/Proposal-SenseSIBI-v11.md").read_text(encoding="utf-8")
mark = "<!-- ===== AKHIR NASKAH"
body = src[:src.index(mark)].rstrip() + "\n"
out = Path("/home/z/my-project/download/sensesibi-v10/_kerja-g11/naskah-untuk-docx.md")
out.write_text(body, encoding="utf-8")
print("naskah-untuk-docx.md:", len(body), "karakter")
EOF

# 3) split 4 berkas
python3 - <<'EOF'
from pathlib import Path
base = Path("/home/z/my-project/download/sensesibi-v10/_kerja-g11")
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
node parse_md_g11.js
node generate_docx_g11.js

# 5) PDF via LibreOffice
cd "$V10"
rm -f Proposal-SenseSIBI-Studi-Kelayakan-v11.pdf
soffice --headless --convert-to pdf --outdir "$V10" Proposal-SenseSIBI-Studi-Kelayakan-v11.docx >/dev/null 2>&1
python3 - <<'EOF'
from pypdf import PdfReader
r = PdfReader("/home/z/my-project/download/sensesibi-v10/Proposal-SenseSIBI-Studi-Kelayakan-v11.pdf")
print("PDF halaman:", len(r.pages))
EOF
