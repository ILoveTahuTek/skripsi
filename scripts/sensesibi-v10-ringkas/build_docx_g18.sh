#!/usr/bin/env bash
# Bangun DOCX+PDF v18 (gelombang 18): paket perbaikan reviewer + ESP-NOW opsional + pemadatan.
# Mengikuti build_docx_g17.sh dengan patch tambahan: nomor persamaan berakhiran huruf (2.13a)
# dan pemadat tata letak (spasi tubuh 1,25; heading; rumus; tabel; daftar pustaka).
set -e
V10=/home/z/my-project/download/sensesibi-v10
SCR=/home/z/my-project/scripts/sensesibi-v10
G18=$V10/_kerja-g18

# 1) salinan JS khusus g18 (idempoten: selalu dari git, lalu patch v16 + v17 + v18)
cd /home/z/my-project
git checkout -- scripts/sensesibi-v10/parse_md.js scripts/sensesibi-v10/generate_docx.js
cp scripts/sensesibi-v10/parse_md.js scripts/sensesibi-v10/parse_md_g18.js
cp scripts/sensesibi-v10/generate_docx.js scripts/sensesibi-v10/generate_docx_g18.js

python3 - <<'EOF'
from pathlib import Path
scr = Path("/home/z/my-project/scripts/sensesibi-v10")

p = scr / "parse_md_g18.js"
s = p.read_text(encoding="utf-8")
s = s.replace(
    "const SRC = '/home/z/my-project/download/sensesibi-v10/_kerja/split';",
    "const SRC = '/home/z/my-project/download/sensesibi-v10/_kerja-g18/split';")
s = s.replace(
    "const ASSETS = '/home/z/my-project/download/sensesibi-v10/assets';",
    "const ASSETS = '/home/z/my-project/download/sensesibi-v10/assets-v18';")
s = s.replace(
    "const OUTJSON = '/home/z/my-project/scripts/sensesibi-v10/parsed-final.json';",
    "const OUTJSON = '/home/z/my-project/scripts/sensesibi-v10/parsed-g18.json';")

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
        const m = ln.match(/\\s*\\((\\d+\\.\\d+[a-z]?)\\)\\s*$/);
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
baru_perlu = "if ((m = rest.match(/^\\[PERLU (?:DATA|RUJUKAN|ILUSTRASI|VALIDASI|KONFIRMASI):[^\\]]*\\]/))) {"
assert lama_perlu in s, "anchor PERLU tidak ditemukan"
s = s.replace(lama_perlu, baru_perlu, 1)
p.write_text(s, encoding="utf-8")

g = scr / "generate_docx_g18.js"
s = g.read_text(encoding="utf-8")
s = s.replace(
    "const parsed = JSON.parse(fs.readFileSync('/home/z/my-project/scripts/sensesibi-v10/parsed-final.json', 'utf-8'));",
    "const parsed = JSON.parse(fs.readFileSync('/home/z/my-project/scripts/sensesibi-v10/parsed-g18.json', 'utf-8'));")
s = s.replace(
    "const OUT = '/home/z/my-project/download/sensesibi-v10/Proposal-SenseSIBI-Studi-Kelayakan-v10.docx';",
    "const OUT = '/home/z/my-project/download/sensesibi-v10/Proposal-SenseSIBI-Studi-Kelayakan-v18.docx';")

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
              children: [new Paragraph({ spacing: { line: 220, before: 4, after: 4 }, children: [] })] }),
            new TableCell({ width: { size: 70, type: WidthType.PERCENTAGE }, borders: noBorders, margins: cellM,
              children: [new Paragraph({ alignment: AlignmentType.CENTER, spacing: { line: 220, before: 4, after: 4 }, children: runs })] }),
            new TableCell({ width: { size: 18, type: WidthType.PERCENTAGE }, borders: noBorders, margins: cellM,
              children: [new Paragraph({ alignment: AlignmentType.RIGHT, spacing: { line: 220, before: 4, after: 4 },
                children: l.num ? [new TextRun({ text: '(' + l.num + ')', size: 24, color: BLACK, font: FONT })] : [] })] }),
          ],
        })],
      });
    });
}

"""
assert anchor_fn in s, "anchor fungsi rumus tidak ditemukan"
s = s.replace(anchor_fn, rumus_fn + anchor_fn, 1)

# PATCH v16g + v17 + v18: pemadat tata letak
s = s.replace(
    "function refPara(runs) {\n  return new Paragraph({\n    alignment: AlignmentType.LEFT,\n    indent: { left: 480, hanging: 480 },\n    spacing: { line: 360, after: 120 },\n    children: makeRuns(runs, 24),",
    "function refPara(runs) {\n  return new Paragraph({\n    alignment: AlignmentType.LEFT,\n    indent: { left: 480, hanging: 480 },\n    spacing: { line: 220, after: 24 },\n    children: makeRuns(runs, 20),")
s = s.replace(
    "const cellMargins = { top: 40, bottom: 40, left: 80, right: 80 };",
    "const cellMargins = { top: 20, bottom: 20, left: 80, right: 80 };")
s = s.replace("spacing: { line: 276, before: 20, after: 20 },", "spacing: { line: 200, before: 8, after: 8 },")
s = s.replace("spacing: { before: 360, after: 240, line: 360 },", "spacing: { before: 80, after: 30, line: 360 },")
s = s.replace("spacing: { before: 240, after: 120, line: 360 },", "spacing: { before: 80, after: 30, line: 360 },")
s = s.replace("spacing: { after: 240, line: 360 },", "spacing: { after: 90, line: 300 },")
s = s.replace("spacing: { before: 240, after: 60 },", "spacing: { before: 160, after: 40 },")
s = s.replace("spacing: { line: 360, after: 60 },\n    children: [new TextRun({ text: n + ' '", "spacing: { line: 300, after: 24 },\n    children: [new TextRun({ text: n + ' '")
s = s.replace(
    "new TableOfContents('Daftar Isi', { hyperlink: true, headingStyleRange: '1-3' }),",
    "new TableOfContents('Daftar Isi', { hyperlink: true, headingStyleRange: '1-2' }),")
s = s.replace(
    "const MAXH_PX = 780;",
    "const MAXH_PX = 620;")

# PATCH v18: kolom minimum menyesuaikan jumlah kolom (tabel jadwal 17 kolom)
lama_cw = "  let pct = w.map(x => Math.max(6, Math.round(x / sum * 100)));"
baru_cw = "  const mn = n > 10 ? 4 : 6;\n  let pct = w.map(x => Math.max(mn, Math.round(x / sum * 100)));"
assert lama_cw in s, "anchor colWidths tidak ditemukan"
s = s.replace(lama_cw, baru_cw)

# Deskripsi dokumen v18
s = s.replace(
    "description: 'Proposal penelitian BAB I-III + Daftar Pustaka v10 (full-stack Rust, Kokoro TTS on-device, BoM 11 komponen, G0-G4 tiga pilar pakar) — revisi 9 Nov 2026',",
    "description: 'Proposal v18 revisi terarah sekaligus pemadatan atas v17 — paket perbaikan reviewer (jalur masukan A/B1/B2 dan Pembanding C, uji permutasi G0b, subcarrier valid N_valid, mask gabungan 2.13a, gradien 2.14a, latensi T_1/T_2 p50-p95, BOM, Permenristekdikti 42/2016, DF-WiSLR, Wi-SignFi, DensePose From WiFi), ESP-NOW diturunkan menjadi fitur sinkronisasi opsional, BAB II 17 ke 12 subbab; DP 32 entri; 14 Nov 2026',")

cek = "v18.docx" in s and "rumusParas" in s and "subScript" in s
assert cek, "patch generate g18 gagal"
assert "parsed-g18.json" in s
assert "line: 220, after: 24" in s and "line: 300 },\n    children: makeRuns" not in s
g.write_text(s, encoding="utf-8")

cek_p = (scr / "parse_md_g18.js").read_text(encoding="utf-8")
assert "assets-v18" in cek_p and "parsed-g18.json" in cek_p
assert "rumus" in cek_p and "sub: true" in cek_p and "sup: true" in cek_p
assert "KONFIRMASI" in cek_p, "patch PERLU KONFIRMASI gagal"
assert "[a-z]?" in cek_p, "patch nomor persamaan berakhiran huruf gagal"
print("JS g18 siap (rumus + akhiran huruf 2.13a + sub/sup + gambar + PERLU VALIDASI/KONFIRMASI + pemadat).")
EOF

# 2) naskah-untuk-docx = tubuh + DP (tanpa log di bawah penanda AKHIR NASKAH)
python3 - <<'EOF'
from pathlib import Path
src = Path("/home/z/my-project/download/sensesibi-v10/Proposal-SenseSIBI-v18.md").read_text(encoding="utf-8")
mark = "<!-- ===== AKHIR NASKAH"
body = src[:src.index(mark)].rstrip() + "\n"
out = Path("/home/z/my-project/download/sensesibi-v10/_kerja-g18/naskah-untuk-docx.md")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(body, encoding="utf-8")
print("naskah-untuk-docx.md:", len(body), "karakter")
EOF

# 3) split 4 berkas
python3 - <<'EOF'
from pathlib import Path
base = Path("/home/z/my-project/download/sensesibi-v10/_kerja-g18")
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
node parse_md_g18.js
node generate_docx_g18.js

# 5) verifikasi parsed: rumus (akhiran huruf), gambar, sitasi, PERLU
python3 - <<'EOF'
import json, re
from pathlib import Path
doc = json.loads(Path("/home/z/my-project/scripts/sensesibi-v10/parsed-g18.json").read_text(encoding="utf-8"))
def hitung(arr, t): return sum(1 for b in arr if b.get("t") == t)
rumus = sum(hitung(v, "rumus") for v in doc.values())
figs = sum(hitung(v, "figure") for v in doc.values())
tables = sum(hitung(v, "table") for v in doc.values())
baris_rumus = [l for v in doc.values() for b in v if b.get("t") == "rumus" for l in b["lines"]]
nomor = [l["num"] for l in baris_rumus if l.get("num")]
huruf = [n for n in nomor if n and n[-1].isalpha()]
prima = [n for n in nomor if "\u2032" in n]
print("blok rumus:", rumus, "| baris rumus:", len(baris_rumus), "| bernomor:", len(nomor), "| berakhiran huruf:", huruf)
print("blok gambar:", figs, "| tabel:", tables)
tubuh = Path("/home/z/my-project/download/sensesibi-v10/_kerja-g18/naskah-untuk-docx.md").read_text(encoding="utf-8")
tubuh = tubuh[:tubuh.index("# DAFTAR PUSTAKA")]
nomor_sit = [int(x) for x in re.findall(r"\[(\d+)\]", tubuh)]
pertama = []
for n in nomor_sit:
    if n not in pertama: pertama.append(n)
print("sitasi unik:", len(set(nomor_sit)), "| monoton:", pertama == sorted(pertama), "| maks:", max(nomor_sit))
assert max(nomor_sit) <= 32 and pertama == sorted(pertama)
assert sorted(huruf) == ["2.13a", "2.14a", "3.3a", "3.3b"], huruf
assert prima == [], prima
perlu = len(re.findall(r"\[PERLU (?:DATA|VALIDASI|KONFIRMASI):", tubuh))
print("PERLU di tubuh:", perlu)
assert perlu >= 55, "penanda PERLU kurang"
EOF

# 6) patch gaya TOC1/TOC2 satu spasi di styles.xml
python3 - <<'PYEOF'
import zipfile, shutil
DOCX = "/home/z/my-project/download/sensesibi-v10/Proposal-SenseSIBI-Studi-Kelayakan-v18.docx"
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
rm -f Proposal-SenseSIBI-Studi-Kelayakan-v18.pdf
soffice --headless --convert-to pdf --outdir "$V10" Proposal-SenseSIBI-Studi-Kelayakan-v18.docx >/dev/null 2>&1
python3 - <<'EOF'
from pypdf import PdfReader
r = PdfReader("/home/z/my-project/download/sensesibi-v10/Proposal-SenseSIBI-Studi-Kelayakan-v18.pdf")
print("PDF halaman:", len(r.pages))
EOF
