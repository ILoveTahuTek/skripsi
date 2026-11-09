#!/usr/bin/env bash
# Bangun DOCX v10: pisahkan naskah, patch jalur pipeline, parse, generate.
set -e
V10=/home/z/my-project/download/sensesibi-v10
SCR=/home/z/my-project/scripts/sensesibi-v10
MD="$V10/Proposal-SenseSIBI-v10.md"

# 1) naskah-untuk-docx.md = tubuh + DP (tanpa log di bawah penanda AKHIR NASKAH)
python3 - <<'EOF'
from pathlib import Path
src = Path("/home/z/my-project/download/sensesibi-v10/Proposal-SenseSIBI-v10.md").read_text(encoding="utf-8")
mark = "<!-- ===== AKHIR NASKAH"
body = src[:src.index(mark)].rstrip() + "\n"
Path("/home/z/my-project/download/sensesibi-v10/_kerja/naskah-untuk-docx.md").write_text(body, encoding="utf-8")
print("naskah-untuk-docx.md:", len(body), "karakter")
EOF

# 2) split 4 berkas
python3 - <<'EOF'
from pathlib import Path
base = Path("/home/z/my-project/download/sensesibi-v10/_kerja")
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

# 3) patch jalur + regex PERLU ILUSTRASI pada parse_md.js dan generate_docx.js
python3 - <<'EOF'
from pathlib import Path
scr = Path("/home/z/my-project/scripts/sensesibi-v10")
p = scr / "parse_md.js"
s = p.read_text(encoding="utf-8")
s = s.replace(
    "const SRC = '/home/z/my-project/download/translator-sibi-final/_kerja/split';",
    "const SRC = '/home/z/my-project/download/sensesibi-v10/_kerja/split';")
s = s.replace(
    "const ASSETS = '/home/z/my-project/download/translator-sibi-docx/assets';",
    "const ASSETS = '/home/z/my-project/download/sensesibi-v10/assets';")
s = s.replace(
    "const OUTJSON = '/home/z/my-project/scripts/translator-sibi-docx/parsed-final.json';",
    "const OUTJSON = '/home/z/my-project/scripts/sensesibi-v10/parsed-final.json';")
s = s.replace(
    "if ((m = rest.match(/^\\[PERLU (?:DATA|RUJUKAN):[^\\]]*\\]/))) {",
    "if ((m = rest.match(/^\\[PERLU (?:DATA|RUJUKAN|ILUSTRASI):[^\\]]*\\]/))) {")
p.write_text(s, encoding="utf-8")

g = scr / "generate_docx.js"
s = g.read_text(encoding="utf-8")
s = s.replace(
    "const parsed = JSON.parse(fs.readFileSync('/home/z/my-project/scripts/translator-sibi-docx/parsed-final.json', 'utf-8'));",
    "const parsed = JSON.parse(fs.readFileSync('/home/z/my-project/scripts/sensesibi-v10/parsed-final.json', 'utf-8'));")
s = s.replace(
    "const OUT = '/home/z/my-project/download/translator-sibi-final/Proposal-Studi-Kelayakan-Purwarupa-SIBI-CSI-ESP32S3.docx';",
    "const OUT = '/home/z/my-project/download/sensesibi-v10/Proposal-SenseSIBI-Studi-Kelayakan-v10.docx';")
s = s.replace(
    "if ((m = rest.match(/^\\[PERLU (?:DATA|RUJUKAN):[^\\]]*\\]/))) { push(); runs.push({ text: m[0], highlight: true }); i += m[0].length; }",
    "if ((m = rest.match(/^\\[PERLU (?:DATA|RUJUKAN|ILUSTRASI):[^\\]]*\\]/))) { push(); runs.push({ text: m[0], highlight: true }); i += m[0].length; }")
s = s.replace(
    "description: 'Proposal penelitian BAB I-III + Daftar Pustaka (guru YOLO26-Pose pose tangan 21 keypoint dari repo WPC ke murid CSI) \u2014 judul SenseSIBI 8 Nov 2026'",
    "description: 'Proposal penelitian BAB I-III + Daftar Pustaka v10 (full-stack Rust, Kokoro TTS on-device, BoM 11 komponen, G0-G4 tiga pilar pakar) \u2014 revisi 9 Nov 2026'")
g.write_text(s, encoding="utf-8")
print("pipeline dipatch.")
EOF

# 4) parse + generate
cd "$SCR"
node parse_md.js
node generate_docx.js
