// parse_md.js — Parsing draft proposal Translator SIBI (markdown) menjadi blok JSON terstruktur.
// Adaptasi dari scripts/sempro/parse_md.js (pipeline DPJ-4 yang sudah terbukti).
// Sejak Task 28: membaca split hasil Claude (download/translator-sibi-final/_kerja/split/)
// dan menulis parsed-final.json.
// Mendukung: heading 1-3, paragraf dengan run inline (miring/tebal/kode/penanda PERLU),
// butir bernomor, tabel markdown + keterangan, blok mermaid -> gambar, entri daftar pustaka.
const fs = require('fs');
const path = require('path');

const SRC = '/home/z/my-project/download/translator-sibi-final/_kerja/split';
const ASSETS = '/home/z/my-project/download/translator-sibi-docx/assets';
const OUTJSON = '/home/z/my-project/scripts/translator-sibi-docx/parsed-final.json';

// ---------- Inline tokenizer ----------
// Jalankan token khusus dulu (PERLU), lalu tebal, miring, kode, lalu teks biasa.
function parseInline(text) {
  const runs = [];
  let buf = '';
  let i = 0;
  const pushPlain = () => { if (buf) { runs.push({ text: buf }); buf = ''; } };
  while (i < text.length) {
    const rest = text.slice(i);
    let m;
    if ((m = rest.match(/^\[PERLU (?:DATA|RUJUKAN):[^\]]*\]/))) {
      pushPlain();
      runs.push({ text: m[0], highlight: true });
      i += m[0].length;
    } else if ((m = rest.match(/^\*\*([^*]+)\*\*/))) {
      pushPlain();
      runs.push({ text: m[1], bold: true });
      i += m[0].length;
    } else if ((m = rest.match(/^\*([^*\n]+)\*/))) {
      pushPlain();
      runs.push({ text: m[1], italics: true });
      i += m[0].length;
    } else if ((m = rest.match(/^`([^`]+)`/))) {
      pushPlain();
      runs.push({ text: m[1], code: true });
      i += m[0].length;
    } else {
      buf += text[i];
      i += 1;
    }
  }
  pushPlain();
  return runs;
}

// ---------- Parser blok per berkas ----------
function parseFile(file, opts = {}) {
  const raw = fs.readFileSync(path.join(SRC, file), 'utf-8');
  const lines = raw.split('\n');
  const blocks = [];
  let i = 0;
  let mermaidCount = 0;
  while (i < lines.length) {
    const line = lines[i];
    const trimmed = line.trim();
    if (trimmed === '') { i += 1; continue; }

    if (trimmed.startsWith('```mermaid')) {
      // Lewati isi mermaid; keterangan Gambar 3.x menyusul setelah blok.
      let j = i + 1;
      while (j < lines.length && !lines[j].trim().startsWith('```')) j += 1;
      mermaidCount += 1;
      i = j + 1;
      // Baris keterangan "Gambar 3.x ..."
      let figCaption = null;
      while (i < lines.length && lines[i].trim() === '') i += 1;
      if (i < lines.length && /^Gambar \d+\.\d+ /.test(lines[i].trim())) {
        figCaption = lines[i].trim();
        i += 1;
      }
      const num = figCaption ? figCaption.match(/^Gambar (\d+\.\d+)/)[1] : `${opts.figBase || '3.'}${mermaidCount}`;
      blocks.push({ t: 'figure', caption: figCaption || `Gambar ${num}`, png: path.join(ASSETS, `gambar-${num}.png`) });
      continue;
    }

    if (trimmed.startsWith('# ')) {
      blocks.push({ t: 'h1', text: trimmed.slice(2).trim() });
      i += 1; continue;
    }
    if (trimmed.startsWith('## ')) {
      blocks.push({ t: 'h2', text: trimmed.slice(3).trim() });
      i += 1; continue;
    }
    if (trimmed.startsWith('### ')) {
      blocks.push({ t: 'h3', text: trimmed.slice(4).trim() });
      i += 1; continue;
    }

    // Tabel markdown
    if (trimmed.startsWith('|')) {
      const tbl = [];
      while (i < lines.length && lines[i].trim().startsWith('|')) {
        tbl.push(lines[i].trim());
        i += 1;
      }
      // tbl[0] = header, tbl[1] = pemisah
      const splitRow = (r) => r.replace(/^\|/, '').replace(/\|$/, '').split('|').map(c => c.trim());
      const header = splitRow(tbl[0]);
      const nCol = header.length;
      // Pengaman: samakan jumlah sel tiap baris dengan kepala (potong/padatkan)
      const rows = tbl.slice(2).map(r => {
        const cells = splitRow(r);
        if (cells.length === nCol) return cells;
        const fixed = cells.slice(0, nCol);
        while (fixed.length < nCol) fixed.push('');
        return fixed;
      });
      // Keterangan tabel: baris "Tabel x.y ..." sebelum tabel (blok terakhir caption)
      let caption = null;
      if (blocks.length && blocks[blocks.length - 1].t === 'tcaption') {
        caption = blocks.pop().caption;
      }
      blocks.push({ t: 'table', caption, header, rows });
      continue;
    }

    // Baris keterangan tabel ("Tabel x.y ...") — hanya bila langsung diikuti tabel
    if (/^Tabel \d+\.\d+ /.test(trimmed)) {
      let j = i + 1;
      while (j < lines.length && lines[j].trim() === '') j += 1;
      if (j < lines.length && lines[j].trim().startsWith('|')) {
        blocks.push({ t: 'tcaption', caption: trimmed });
        i += 1; continue;
      }
      // selain itu: kalimat rujukan biasa -> jatuh ke paragraf
    }

    // Entri daftar pustaka ("[n] ...")
    if (opts.refs && /^\[\d+\] /.test(trimmed)) {
      blocks.push({ t: 'ref', runs: parseInline(trimmed) });
      i += 1; continue;
    }

    // Butir bernomor ("1. ...")
    if (/^\d+\.\s+\S/.test(trimmed)) {
      const m = trimmed.match(/^(\d+)\.\s+(.*)$/);
      blocks.push({ t: 'li', n: m[1] + '.', runs: parseInline(m[2]) });
      i += 1; continue;
    }

    // Paragraf biasa (gabung baris sampai baris kosong)
    let para = trimmed;
    i += 1;
    while (i < lines.length && lines[i].trim() !== '' && !/^(#{1,3} |\||```|\d+\.\s|Tabel \d+\.\d+ |Gambar \d+\.\d+ )/.test(lines[i].trim()) && !(opts.refs && /^\[\d+\] /.test(lines[i].trim()))) {
      para += ' ' + lines[i].trim();
      i += 1;
    }
    blocks.push({ t: 'p', runs: parseInline(para) });
  }
  return blocks;
}

const doc = {
  bab1: parseFile('bab1-pendahuluan.md'),
  bab2: parseFile('bab2-kajian-pustaka.md'),
  bab3: parseFile('bab3-metodologi.md'),
  dp: parseFile('daftar-pustaka.md', { refs: true }),
};

fs.writeFileSync(OUTJSON, JSON.stringify(doc, null, 1));
const count = (arr, t) => arr.filter(b => b.t === t).length;
for (const [k, arr] of Object.entries(doc)) {
  console.log(`${k}: h1=${count(arr, 'h1')} h2=${count(arr, 'h2')} h3=${count(arr, 'h3')} p=${count(arr, 'p')} li=${count(arr, 'li')} table=${count(arr, 'table')} figure=${count(arr, 'figure')} ref=${count(arr, 'ref')}`);
}
// Statistik penanda
let perlu = 0;
const visit = (r) => { if (r.highlight) perlu += 1; };
for (const arr of Object.values(doc)) for (const b of arr) {
  if (b.runs) b.runs.forEach(visit);
  if (b.header) b.header.forEach(c => parseInline(c).forEach(visit));
  if (b.rows) b.rows.forEach(r => r.forEach(c => parseInline(c).forEach(visit)));
}
console.log('Penanda PERLU (run highlight):', perlu);
