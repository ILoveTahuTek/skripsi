#!/usr/bin/env bash
# Bangun DOCX+PDF v17 (gelombang 17): revisi terarah v16 -> v17 sesuai Dokumen Revisi Terarah.
set -e
V10=/home/z/my-project/download/sensesibi-v10
SCR=/home/z/my-project/scripts/sensesibi-v10
G17=$V10/_kerja-g17

# 1) salinan JS khusus g17 (idempoten: selin dari git setiap kali, lalu terapkan seluruh patch v16 + patch v17)
cd /home/z/my-project
git checkout -- scripts/sensesibi-v10/parse_md.js scripts/sensesibi-v10/generate_docx.js
cp scripts/sensesibi-v10/parse_md.js scripts/sensesibi-v10/parse_md_g17.js
cp scripts/sensesibi-v10/generate_docx.js scripts/sensesibi-v10/generate_docx_g17.js

python3 - <<'EOF'
from pathlib import Path
scr = Path("/home/z/my-project/scripts/sensesibi-v10")

p = scr / "parse_md_g17.js"
s = p.read_text(encoding="utf-8")
s = s.replace(
    "const SRC = '/home/z/my-project/download/sensesibi-v10/_kerja/split';",
    "const SRC = '/home/z/my-project/download/sensesibi-v10/_kerja-g17/split';")
s = s.replace(
    "const ASSETS = '/home/z/my-project/download/sensesibi-v10/assets';",
    "const ASSETS = '/home/z/my-project/download/sensesibi-v10/assets-v17';")
s = s.replace(
    "const OUTJSON = '/home/z/my-project/scripts/sensesibi-v10/parsed-final.json';",
    "const OUTJSON = '/home/z/my-project/scripts/sensesibi-v10/parsed-g17.json';")

# PATCH v16a: blok ```gambar diperlakukan seperti mermaid
s = s.replace(
    "    if (trimmed.startsWith('```mermaid')) {",
    "    if (trimmed.startsWith('```mermaid') || trimmed.startsWith('```gambar')) {")

# PATCH v16b: blok ```rumus -> {t:'rumus', lines:[{runs, num}]}
anchor = "    if (trimmed.startsWith('# ')) {"
rumus_handler = """    if (trimmed.startsWith('```rumus')) {
      let j = i + 1;
      const rl = [];
      while (j < lines.length && !lines[j].trim().startsWith('```')) {
        let ln = lines[j].trim();
        let num = null;
        const m = ln.match(/\\s*\\((\\d+\\.\\d+)\\)\\s*$/);
        if (m) { num = m[1]; ln = ln.slice(0, m.index); }
        rl.push({ runs: parseInline(ln), num });
        j += 1;
      }
      blocks.push({ t: 'rumus', lines: rl });
      i = j + 1;
      continue;
    }

"""
assert anchor in s, "anchor rumus tidak ditemukan"
s = s.replace(anchor, rumus_handler + anchor, 1)

# PATCH v17a (BARU): nomor persamaan boleh berakhiran prima (2.15')
lama_num = "const m = ln.match(/\\s*\\((\\d+\\.\\d+)\\)\\s*$/);"
baru_num = "const m = ln.match(/\\s*\\((\\d+\\.\\d+\\u2032?)\\)\\s*$/);"
assert lama_num in s, "anchor nomor rumus tidak ditemukan"
s = s.replace(lama_num, baru_num, 1)

# PATCH v16c: token subskrip ~x~ dan superskrip ^x^ pada parseInline
anchor2 = """      runs.push({ text: m[1], code: true });
      i += m[0].length;
    } else {"""
subsup = """      runs.push({ text: m[1], code: true });
      i += m[0].length;
    } else if ((m = rest.match(/^~([^~\\n]+)~/))) {
      pushPlain();
      runs.push({ text: m[1], sub: true });
      i += m[0].length;
    } else if ((m = rest.match(/^\\^([^\\^\\n]+)\\^/))) {
      pushPlain();
      runs.push({ text: m[1], sup: true });
      i += m[0].length;
    } else {"""
assert anchor2 in s, "anchor subsup tidak ditemukan"
s = s.replace(anchor2, subsup, 1)

# PATCH v16d: penanda PERLU VALIDASI ikut tersorot
lama_perlu = "if ((m = rest.match(/^\\[PERLU (?:DATA|RUJUKAN|ILUSTRASI):[^\\]]*\\]/))) {"
baru_perlu = "if ((m = rest.match(/^\\[PERLU (?:DATA|RUJUKAN|ILUSTRASI|VALIDASI):[^\\]]*\\]/))) {"
assert lama_perlu in s, "anchor PERLU tidak ditemukan"
s = s.replace(lama_perlu, baru_perlu, 1)
p.write_text(s, encoding="utf-8")

g = scr / "generate_docx_g17.js"
s = g.read_text(encoding="utf-8")
s = s.replace(
    "const parsed = JSON.parse(fs.readFileSync('/home/z/my-project/scripts/sensesibi-v10/parsed-final.json', 'utf-8'));",
    "const parsed = JSON.parse(fs.readFileSync('/home/z/my-project/scripts/sensesibi-v10/parsed-g17.json', 'utf-8'));")
s = s.replace(
    "const OUT = '/home/z/my-project/download/sensesibi-v10/Proposal-SenseSIBI-Studi-Kelayakan-v10.docx';",
    "const OUT = '/home/z/my-project/download/sensesibi-v10/Proposal-SenseSIBI-Studi-Kelayakan-v17.docx';")

# PATCH v16e: makeRuns mendukung subskrip/superskrip
s = s.replace(
    "    bold: !!r.bold,\n    italics: !!r.italics,\n    highlight: r.highlight ? 'yellow' : undefined,",
    "    bold: !!r.bold,\n    italics: !!r.italics,\n    subScript: !!r.sub,\n    superScript: !!r.sup,\n    highlight: r.highlight ? 'yellow' : undefined,")

# PATCH v16f: perender blok rumus
anchor_fig = "    else if (b.t === 'figure') out.push(...figureBlock(b));"
s = s.replace(anchor_fig, anchor_fig + "\n    else if (b.t === 'rumus') out.push(...rumusParas(b));")
anchor_fn = "// ---------- Rujukan ----------"
rumus_fn = """// ---------- Rumus (persamaan bernomor; rumus di tengah, nomor di kanan) ----------
function rumusParas(b) {
  const cellM = { top: 5, bottom: 5, left: 40, right: 40 };
  return b.lines
    .filter(l => (l.runs && l.runs.length) || l.num)
    .map(l => {
      const runs = (l.runs || []).map(r => new TextRun({
        text: r.text, italics: true,
        subScript: !!r.sub, superScript: !!r.sup,
        highlight: r.highlight ? 'yellow' : undefined,
        size: 24, color: BLACK, font: r.code ? FONT_CODE : FONT,
      }));
      return new Table({
        width: { size: 100, type: WidthType.PERCENTAGE },
        layout: TableLayoutType.FIXED,
        borders: allNoBorders,
        rows: [new TableRow({
          cantSplit: true,
          children: [
            new TableCell({ width: { size: 12, type: WidthType.PERCENTAGE }, borders: noBorders, margins: cellM,
              children: [new Paragraph({ spacing: { line: 240, before: 10, after: 10 }, children: [] })] }),
            new TableCell({ width: { size: 70, type: WidthType.PERCENTAGE }, borders: noBorders, margins: cellM,
              children: [new Paragraph({ alignment: AlignmentType.CENTER, spacing: { line: 240, before: 10, after: 10 }, children: runs })] }),
            new TableCell({ width: { size: 18, type: WidthType.PERCENTAGE }, borders: noBorders, margins: cellM,
              children: [new Paragraph({ alignment: AlignmentType.RIGHT, spacing: { line: 240, before: 10, after: 10 },
                children: l.num ? [new TextRun({ text: '(' + l.num + ')', size: 24, color: BLACK, font: FONT })] : [] })] }),
          ],
        })],
      });
    });
}

"""
assert anchor_fn in s, "anchor fungsi rumus tidak ditemukan"
s = s.replace(anchor_fn, rumus_fn + anchor_fn, 1)

# PATCH v16g + v16h (pemadat, gabungkan dua tahap v16 jadi satu)
s = s.replace(
    "function refPara(runs) {\n  return new Paragraph({\n    alignment: AlignmentType.LEFT,\n    indent: { left: 480, hanging: 480 },\n    spacing: { line: 360, after: 120 },\n    children: makeRuns(runs, 24),",
    "function refPara(runs) {\n  return new Paragraph({\n    alignment: AlignmentType.LEFT,\n    indent: { left: 480, hanging: 480 },\n    spacing: { line: 240, after: 40 },\n    children: makeRuns(runs, 20),")
s = s.replace(
    "const cellMargins = { top: 40, bottom: 40, left: 80, right: 80 };",
    "const cellMargins = { top: 30, bottom: 30, left: 80, right: 80 };")
s = s.replace("spacing: { line: 276, before: 20, after: 20 },", "spacing: { line: 220, before: 12, after: 12 },")
s = s.replace("spacing: { before: 360, after: 240, line: 360 },", "spacing: { before: 120, after: 60, line: 360 },")
s = s.replace("spacing: { before: 240, after: 120, line: 360 },", "spacing: { before: 120, after: 60, line: 360 },")
s = s.replace("spacing: { after: 240, line: 360 },", "spacing: { after: 160, line: 360 },")
s = s.replace("spacing: { before: 240, after: 60 },", "spacing: { before: 160, after: 40 },")
s = s.replace("spacing: { line: 360, after: 60 },\n    children: [new TextRun({ text: n + ' '", "spacing: { line: 360, after: 40 },\n    children: [new TextRun({ text: n + ' '")
s = s.replace(
    "new TableOfContents('Daftar Isi', { hyperlink: true, headingStyleRange: '1-3' }),",
    "new TableOfContents('Daftar Isi', { hyperlink: true, headingStyleRange: '1-2' }),")
s = s.replace(
    "const MAXH_PX = 780;",
    "const MAXH_PX = 620;")

# Deskripsi dokumen v17
s = s.replace(
    "description: 'Proposal v16 revisi additif \\u2014 encoder CSI terpralatih beku + dua kepala tugas (klasifikasi 26 huruf, regresi 21 keypoint) pada sistem dua arah utuh; 29 persamaan, 7 gambar, 12 tabel, DP 28 entri (humanizer-indonesia v1.7 + scientific-agent-skills) 13 Nov 2026'",
    "description: 'Proposal v17 revisi terarah atas v17 evaluasi kritis \\u2014 kontrak masukan encoder dikunci (8 fitur per jendela 1 detik, gerbang G0b), supervisi 24 huruf statis dan J/Z dipisah, Persamaan 2.15\\u2032 tetapan terlatih utuh, modul temporal dua cabang, deployment Pilihan 1, arsitektur audio disatukan (TTS server lokal utama), kriteria G1 diperkuat; DP 28 entri; skill sempro-mepet 14 Nov 2026'")

cek = "v17.docx" in s and "rumusParas" in s and "subScript" in s
assert cek, "patch generate g17 gagal"
assert "parsed-g17.json" in s
g.write_text(s, encoding="utf-8")

cek_p = (scr / "parse_md_g17.js").read_text(encoding="utf-8")
assert "assets-v17" in cek_p and "parsed-g17.json" in cek_p
assert "rumus" in cek_p and "sub: true" in cek_p and "sup: true" in cek_p
assert "VALIDASI" in cek_p, "patch PERLU VALIDASI gagal"
assert "\\u2032?" in cek_p, "patch prima gagal"
print("JS g17 siap (rumus + prima 2.15' + sub/sup + gambar + PERLU VALIDASI).")
EOF

# 2) naskah-untuk-docx = tubuh + DP (tanpa log di bawah penanda AKHIR NASKAH)
python3 - <<'EOF'
from pathlib import Path
src = Path("/home/z/my-project/download/sensesibi-v10/Proposal-SenseSIBI-v17.md").read_text(encoding="utf-8")
mark = "<!-- ===== AKHIR NASKAH"
body = src[:src.index(mark)].rstrip() + "\n"
out = Path("/home/z/my-project/download/sensesibi-v10/_kerja-g17/naskah-untuk-docx.md")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(body, encoding="utf-8")
print("naskah-untuk-docx.md:", len(body), "karakter")
EOF

# 3) split 4 berkas
python3 - <<'EOF'
from pathlib import Path
base = Path("/home/z/my-project/download/sensesibi-v10/_kerja-g17")
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
node parse_md_g17.js
node generate_docx_g17.js

# 5) verifikasi parsed: rumus (termasuk prima), gambar, sitasi, PERLU
python3 - <<'EOF'
import json, re
from pathlib import Path
doc = json.loads(Path("/home/z/my-project/scripts/sensesibi-v10/parsed-g17.json").read_text(encoding="utf-8"))
def hitung(arr, t): return sum(1 for b in arr if b.get("t") == t)
rumus = sum(hitung(v, "rumus") for v in doc.values())
figs = sum(hitung(v, "figure") for v in doc.values())
tables = sum(hitung(v, "table") for v in doc.values())
baris_rumus = [l for v in doc.values() for b in v if b.get("t") == "rumus" for l in b["lines"]]
nomor = [l["num"] for l in baris_rumus if l.get("num")]
prima = [n for n in nomor if "\u2032" in n]
sub = sum(1 for v in doc.values() for b in v if b.get("t") == "rumus" for l in b["lines"] for r in l["runs"] if r.get("sub"))
print("blok rumus:", rumus, "| baris rumus:", len(baris_rumus), "| bernomor:", len(nomor), "| bernomor prima:", prima)
print("blok gambar:", figs, "| tabel:", tables, "| run subskrip:", sub)
tubuh = Path("/home/z/my-project/download/sensesibi-v10/_kerja-g17/naskah-untuk-docx.md").read_text(encoding="utf-8")
tubuh = tubuh[:tubuh.index("# DAFTAR PUSTAKA")]
nomor_sit = [int(x) for x in re.findall(r"\[(\d+)\]", tubuh)]
pertama = []
for n in nomor_sit:
    if n not in pertama: pertama.append(n)
print("sitasi unik:", sorted(set(nomor_sit)), "| monoton:", pertama == sorted(pertama), "| maks:", max(nomor_sit))
assert max(nomor_sit) <= 28 and pertama == sorted(pertama)
perlu_v = len(re.findall(r"\[PERLU VALIDASI:", tubuh))
print("PERLU VALIDASI di tubuh:", perlu_v)
assert perlu_v >= 10, "PERLU VALIDASI kurang dari 10"
assert prima == ["2.15\u2032"], prima
EOF

# 6) patch gaya TOC1/TOC2 satu spasi di styles.xml
python3 - <<'PYEOF'
import zipfile, shutil
DOCX = "/home/z/my-project/download/sensesibi-v10/Proposal-SenseSIBI-Studi-Kelayakan-v17.docx"
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
                '<w:style w:type="paragraph" w:styleId="TOC2"><w:name w:val="toc 2"/><w:basedOn w:val="Normal"/><w:next w:val="Normal"/><w:uiPriority w:val="39"/><w:pPr><w:spacing w:after="100"/><w:ind w:left="240"/></w:pPr></w:style>',
                '<w:style w:type="paragraph" w:styleId="TOC2"><w:name w:val="toc 2"/><w:basedOn w:val="Normal"/><w:next w:val="Normal"/><w:uiPriority w:val="39"/><w:pPr><w:spacing w:after="0" w:line="240" w:lineRule="auto"/><w:ind w:left="240"/></w:pPr></w:style>')
            assert 'TOC1"><w:name w:val="toc 1"/><w:basedOn w:val="Normal"/><w:next w:val="Normal"/><w:uiPriority w:val="39"/><w:pPr><w:spacing w:before="60"' in s, "patch TOC1 gagal"
            data = s.encode("utf-8")
        zout.writestr(item, data)
shutil.move(TMP, DOCX)
print("styles.xml dipatch: TOC1/TOC2 satu spasi")
PYEOF

# 7) PDF via LibreOffice
cd "$V10"
rm -f Proposal-SenseSIBI-Studi-Kelayakan-v17.pdf
soffice --headless --convert-to pdf --outdir "$V10" Proposal-SenseSIBI-Studi-Kelayakan-v17.docx >/dev/null 2>&1
python3 - <<'EOF'
from pypdf import PdfReader
r = PdfReader("/home/z/my-project/download/sensesibi-v10/Proposal-SenseSIBI-Studi-Kelayakan-v17.pdf")
print("PDF halaman:", len(r.pages))
EOF
