#!/usr/bin/env bash
# Bangun DOCX+PDF v18 (gelombang 18): revisi verifikasi sumber primer (ISS-01..ISS-30).
# Patch di atas g17: nomor persamaan berakhiran huruf (2.13a), sel tabel sub/sup,
# caption gambar lewat parser inline, lebar kolom anti-pemenggalan, PERLU KONFIRMASI.
set -e
V10=/home/z/my-project/download/sensesibi-v10
SCR=/home/z/my-project/scripts/sensesibi-v10
G18=$V10/_kerja-g18

cd /home/z/my-project
git checkout -- scripts/sensesibi-v10/parse_md.js scripts/sensesibi-v10/generate_docx.js
cp scripts/sensesibi-v10/parse_md.js scripts/sensesibi-v10/parse_md_g18.js
cp scripts/sensesibi-v10/generate_docx.js scripts/sensesibi-v10/generate_docx_g18.js

python3 - <<'EOF'
from pathlib import Path
scr = Path("/home/z/my-project/scripts/sensesibi-v10")

p = scr / "parse_md_g18.js"
s = p.read_text(encoding="utf-8")
s = s.replace("const SRC = '/home/z/my-project/download/sensesibi-v10/_kerja/split';",
              "const SRC = '/home/z/my-project/download/sensesibi-v10/_kerja-g18/split';")
s = s.replace("const ASSETS = '/home/z/my-project/download/sensesibi-v10/assets';",
              "const ASSETS = '/home/z/my-project/download/sensesibi-v10/assets-v18';")
s = s.replace("const OUTJSON = '/home/z/my-project/scripts/sensesibi-v10/parsed-final.json';",
              "const OUTJSON = '/home/z/my-project/scripts/sensesibi-v10/parsed-g18.json';")

# blok ```gambar seperti mermaid
s = s.replace("    if (trimmed.startsWith('```mermaid')) {",
              "    if (trimmed.startsWith('```mermaid') || trimmed.startsWith('```gambar')) {")

# blok ```rumus
anchor = "    if (trimmed.startsWith('# ')) {"
rumus_handler = """    if (trimmed.startsWith('```rumus')) {
      let j = i + 1;
      const rl = [];
      while (j < lines.length && !lines[j].trim().startsWith('```')) {
        let ln = lines[j].trim();
        let num = null;
        const m = ln.match(/\\s*\\((\\d+\\.\\d+(?:\\u2032|[ab])?)\\)\\s*$/);
        if (m) { num = m[1]; ln = ln.slice(0, m.index); }
        rl.push({ runs: parseInline(ln), num });
        j += 1;
      }
      blocks.push({ t: 'rumus', lines: rl });
      i = j + 1;
      continue;
    }

"""
assert anchor in s
s = s.replace(anchor, rumus_handler + anchor, 1)

# subskrip/superskrip parseInline
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
assert anchor2 in s
s = s.replace(anchor2, subsup, 1)

# PERLU VALIDASI + KONFIRMASI tersorot
lama_perlu = "if ((m = rest.match(/^\\[PERLU (?:DATA|RUJUKAN|ILUSTRASI):[^\\]]*\\]/))) {"
baru_perlu = "if ((m = rest.match(/^\\[PERLU (?:DATA|RUJUKAN|ILUSTRASI|VALIDASI|KONFIRMASI):[^\\]]*\\]/))) {"
assert lama_perlu in s
s = s.replace(lama_perlu, baru_perlu, 1)

# v18: caption gambar disimpan juga sebagai runs (untuk render italic)
lama_cap = """      if (i < lines.length && /^Gambar \\d+\\.\\d+ /.test(lines[i].trim())) {
        figCaption = lines[i].trim();"""
baru_cap = """      if (i < lines.length && /^Gambar \\d+\\.\\d+ /.test(lines[i].trim())) {
        figCaption = lines[i].trim();
        figCaptionRuns = parseInline(figCaption.replace(/^(Gambar \\d+\\.\\d+)\\s+/, ' '));"""
assert lama_cap in s, "anchor caption tidak ditemukan"
s = s.replace(lama_cap, baru_cap, 1)
# deklarasi variabel figCaptionRuns dan pemakaian di blocks.push
s = s.replace("      let figCaption = null;", "      let figCaption = null;\n      let figCaptionRuns = null;")
s = s.replace("blocks.push({ t: 'figure', caption: figCaption || `Gambar ${num}`, png: path.join(ASSETS, `gambar-${num}.png`) });",
              "blocks.push({ t: 'figure', caption: figCaption || `Gambar ${num}`, captionRuns: figCaptionRuns, png: path.join(ASSETS, `gambar-${num}.png`) });")
p.write_text(s, encoding="utf-8")

g = scr / "generate_docx_g18.js"
s = g.read_text(encoding="utf-8")
s = s.replace("const parsed = JSON.parse(fs.readFileSync('/home/z/my-project/scripts/sensesibi-v10/parsed-final.json', 'utf-8'));",
              "const parsed = JSON.parse(fs.readFileSync('/home/z/my-project/scripts/sensesibi-v10/parsed-g18.json', 'utf-8'));")
s = s.replace("const OUT = '/home/z/my-project/download/sensesibi-v10/Proposal-SenseSIBI-Studi-Kelayakan-v10.docx';",
              "const OUT = '/home/z/my-project/download/sensesibi-v10/Proposal-SenseSIBI-Studi-Kelayakan-v18.docx';")

# makeRuns sub/sup
s = s.replace("""    bold: !!r.bold,
    italics: !!r.italics,
    highlight: r.highlight ? 'yellow' : undefined,""",
"""    bold: !!r.bold,
    italics: !!r.italics,
    subScript: !!r.sub,
    superScript: !!r.sup,
    highlight: r.highlight ? 'yellow' : undefined,""")

# renderer rumus
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
assert anchor_fn in s
s = s.replace(anchor_fn, rumus_fn + anchor_fn, 1)

# v18a: inlineCellRuns mendukung sub/sup + KONFIRMASI
lama_icr = """    if ((m = rest.match(/^\\[PERLU (?:DATA|RUJUKAN|ILUSTRASI):[^\\]]*\\]/))) { push(); runs.push({ text: m[0], highlight: true }); i += m[0].length; }"""
baru_icr = """    if ((m = rest.match(/^\\[PERLU (?:DATA|RUJUKAN|ILUSTRASI|VALIDASI|KONFIRMASI):[^\\]]*\\]/))) { push(); runs.push({ text: m[0], highlight: true }); i += m[0].length; }
    else if ((m = rest.match(/^~([^~\\n]+)~/))) { push(); runs.push({ text: m[1], sub: true }); i += m[0].length; }
    else if ((m = rest.match(/^\\^([^\\^\\n]+)\\^/))) { push(); runs.push({ text: m[1], sup: true }); i += m[0].length; }"""
assert lama_icr in s, "anchor inlineCellRuns tidak ditemukan"
s = s.replace(lama_icr, baru_icr, 1)
s = s.replace("""  return runs.map(r => new TextRun({
    text: r.text, bold: bold || !!r.bold, italics: !!r.italics,
    highlight: r.highlight ? 'yellow' : undefined,
    size: 18, color: BLACK, font: r.code ? FONT_CODE : FONT,
  }));""",
"""  return runs.map(r => new TextRun({
    text: r.text, bold: bold || !!r.bold, italics: !!r.italics,
    subScript: !!r.sub, superScript: !!r.sup,
    highlight: r.highlight ? 'yellow' : undefined,
    size: 18, color: BLACK, font: r.code ? FONT_CODE : FONT,
  }));""")

# v18b: caption (tabel dan gambar) memakai runs hasil parser (miring, bukan asterisk mentah)
lama_capgen = "        ...(m ? [new TextRun({ text: ' ' + m[2], size: 24, color: BLACK, font: FONT })] : []),"
baru_capgen = "        ...(m ? (block.captionRuns || []).map(r => new TextRun({ text: r.text, italics: !!r.italics, bold: !!r.bold, subScript: !!r.sub, superScript: !!r.sup, highlight: r.highlight ? 'yellow' : undefined, size: 24, color: BLACK, font: FONT })) : []),"
assert s.count(lama_capgen) == 2, f"caption anchor: {s.count(lama_capgen)}"
s = s.replace(lama_capgen, baru_capgen)

# v18c: colWidths dijamin cukup untuk kata terpanjang (anti Jumla-h, Gerb-ang)
lama_cw = """function colWidths(header, rows) {
  const n = header.length;
  const lens = header.map((h, c) => {
    let mx = Math.min(h.length, 60);
    for (const r of rows) mx = Math.max(mx, Math.min((r[c] || '').length, 60));
    return Math.max(mx, 3);
  });
  // Bobot sublinear agar kolom panjang tidak menelan semua ruang
  const w = lens.map(l => Math.pow(l, 0.62));
  const sum = w.reduce((a, b) => a + b, 0);
  let pct = w.map(x => Math.max(6, Math.round(x / sum * 100)));
  // Normalisasi ke 100
  let s = pct.reduce((a, b) => a + b, 0);
  pct = pct.map(x => Math.round(x * 100 / s));
  s = pct.reduce((a, b) => a + b, 0);
  pct[n - 1] += 100 - s;
  return pct;
}"""
baru_cw = """function colWidths(header, rows) {
  const n = header.length;
  const bersih = (t) => String(t || '').replace(/[*~^`\\[\\]]/g, '');
  const lens = header.map((h, c) => {
    let mx = Math.min(h.length, 60);
    for (const r of rows) mx = Math.max(mx, Math.min((r[c] || '').length, 60));
    return Math.max(mx, 3);
  });
  const maxWord = header.map((h, c) => {
    let mw = 3;
    for (const w of bersih(h).split(/\\s+/)) mw = Math.max(mw, Math.min(w.length, 14));
    for (const r of rows) for (const w of bersih(r[c]).split(/\\s+/)) mw = Math.max(mw, Math.min(w.length, 14));
    return mw;
  });
  // Bobot sublinear agar kolom panjang tidak menelan semua ruang
  const w = lens.map(l => Math.pow(l, 0.62));
  const sum = w.reduce((a, b) => a + b, 0);
  let pct = w.map(x => Math.max(6, Math.round(x / sum * 100)));
  // v18: jamin kolom cukup untuk kata terpanjangnya (anti pemenggalan Jumla-h, Gerb-ang)
  const wmin = maxWord.map(l => Math.pow(l + 1.5, 0.62));
  const smin = wmin.reduce((a, b) => a + b, 0);
  const pctMin = wmin.map(x => Math.max(6, Math.round(x / smin * 100)));
  pct = pct.map((x, c) => Math.max(x, pctMin[c]));
  // Normalisasi ke 100
  let s = pct.reduce((a, b) => a + b, 0);
  pct = pct.map(x => Math.round(x * 100 / s));
  s = pct.reduce((a, b) => a + b, 0);
  pct[n - 1] += 100 - s;
  return pct;
}"""
assert lama_cw in s, "anchor colWidths tidak ditemukan"
s = s.replace(lama_cw, baru_cw, 1)

# pemadat g16/g17
s = s.replace("""function refPara(runs) {
  return new Paragraph({
    alignment: AlignmentType.LEFT,
    indent: { left: 480, hanging: 480 },
    spacing: { line: 360, after: 120 },
    children: makeRuns(runs, 24),""",
"""function refPara(runs) {
  return new Paragraph({
    alignment: AlignmentType.LEFT,
    indent: { left: 480, hanging: 480 },
    spacing: { line: 240, after: 40 },
    children: makeRuns(runs, 20),""")
s = s.replace("const cellMargins = { top: 40, bottom: 40, left: 80, right: 80 };",
              "const cellMargins = { top: 30, bottom: 30, left: 80, right: 80 };")
s = s.replace("spacing: { line: 276, before: 20, after: 20 },", "spacing: { line: 220, before: 12, after: 12 },")
s = s.replace("spacing: { before: 360, after: 240, line: 360 },", "spacing: { before: 120, after: 60, line: 360 },")
s = s.replace("spacing: { before: 240, after: 120, line: 360 },", "spacing: { before: 120, after: 60, line: 360 },")
s = s.replace("spacing: { after: 240, line: 360 },", "spacing: { after: 160, line: 360 },")
s = s.replace("spacing: { before: 240, after: 60 },", "spacing: { before: 160, after: 40 },")
s = s.replace("spacing: { line: 360, after: 60 },\n    children: [new TextRun({ text: n + ' '", "spacing: { line: 360, after: 40 },\n    children: [new TextRun({ text: n + ' '")
s = s.replace("new TableOfContents('Daftar Isi', { hyperlink: true, headingStyleRange: '1-3' }),",
              "new TableOfContents('Daftar Isi', { hyperlink: true, headingStyleRange: '1-2' }),")
s = s.replace("const MAXH_PX = 780;", "const MAXH_PX = 620;")

# deskripsi dokumen v18
old_desc_marker = "description: 'Proposal"
i = s.index(old_desc_marker)
j = s.index("'", s.index("2026'", i) if "2026'" in s[i:i+900] else i) # fallback
# ganti seluruh baris description dengan cara aman
import re as _re
s = _re.sub(r"description: 'Proposal[^']*'", "description: 'Proposal v18 revisi verifikasi sumber primer 14 Nov 2026 atas v17: audit artefak encoder (NUL-padding, csi-embed-v2, EWC 32,97%, SISO), subcarrier valid LLTF/HT-LTF + first_word_invalid, Jalur A/B1/B2 + Pembanding C, mask efektif 2.13a + kosinus gradien 2.14a, G0b uji permutasi, segmentasi tiga fase, overlap 75% dikoreksi, latensi 3.3a/3.3b, WER tanpa 1-WER, MMS-TTS-ind utama operasional, etika tata kelola data, TKT Permenristekdikti 42/2016; DP 31 entri; 94 suntingan terarah; skill sempro-mepet'", s, count=1)

cek = "v18.docx" in s and "rumusParas" in s and "subScript" in s and "captionRuns" in s and "pctMin" in s
assert cek, "patch generate g18 gagal"
assert "parsed-g18.json" in s
g.write_text(s, encoding="utf-8")

cek_p = (scr / "parse_md_g18.js").read_text(encoding="utf-8")
assert "assets-v18" in cek_p and "parsed-g18.json" in cek_p
assert "rumus" in cek_p and "sub: true" in cek_p and "sup: true" in cek_p
assert "VALIDASI" in cek_p and "KONFIRMASI" in cek_p
assert "(?:\\u2032|[ab])?" in cek_p, "patch nomor huruf gagal"
assert "captionRuns" in cek_p
print("JS g18 siap (rumus a/b + sub/sup sel tabel + caption runs + colWidths + KONFIRMASI).")
EOF

# 2) naskah-untuk-docx
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

# 5) verifikasi parsed
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
print("blok rumus:", rumus, "| baris rumus:", len(baris_rumus), "| bernomor:", len(nomor))
print("nomor:", nomor)
harus = ['2.1','2.2','2.3','2.4','2.5','2.6','2.7','2.8','2.9','2.10','2.11','2.12','2.13a','2.13','2.14','2.14a','2.15','2.16','2.17','2.18','2.19','2.20','2.21','2.22','2.23','2.24','3.1','3.2','3.3a','3.3b','3.4','3.5']
assert nomor == harus, [x for x, y in zip(nomor, harus) if x != y] or f"panjang {len(nomor)} vs {len(harus)}"
print("urutan persamaan: OK (33 bernomor, termasuk 2.13a/2.14a/3.3a/3.3b)")
print("blok gambar:", figs, "| tabel:", tables)
tubuh = Path("/home/z/my-project/download/sensesibi-v10/_kerja-g18/naskah-untuk-docx.md").read_text(encoding="utf-8")
tubuh = tubuh[tubuh.index("# BAB I "):tubuh.index("# DAFTAR PUSTAKA")]
nomor_sit = [int(x) for x in re.findall(r"\[(\d+)\]", tubuh)]
# monoton utk 1..28 menurut kemunculan pertama; 29-31 tambahan
pos = {}
for k, n in enumerate(nomor_sit):
    if n not in pos: pos[n] = k
urut_lama = [pos[n] for n in range(1, 29) if n in pos]
assert urut_lama == sorted(urut_lama), "sitasi 1-28 tidak monoton"
assert max(nomor_sit) <= 31 and {29, 30, 31} <= set(nomor_sit)
print("sitasi: [1]-[28] monoton; [29]-[31] ada; maks =", max(nomor_sit))
dp = Path("/home/z/my-project/download/sensesibi-v10/_kerja-g18/split/daftar-pustaka.md").read_text(encoding="utf-8")
entri = re.findall(r"^\[(\d+)\]", dp, re.M)
print("DP entri:", len(entri), "| terakhir:", entri[-3:])
assert len(entri) == 31 and entri == [str(i) for i in range(1, 32)]
perlu_v = len(re.findall(r"\[PERLU VALIDASI:", tubuh))
perlu_k = len(re.findall(r"\[PERLU KONFIRMASI:", tubuh))
perlu_d = len(re.findall(r"\[PERLU DATA:", tubuh))
print(f"PERLU DATA: {perlu_d} | PERLU VALIDASI: {perlu_v} | PERLU KONFIRMASI: {perlu_k}")
assert perlu_k >= 2
EOF

# 6) patch gaya TOC satu spasi
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
