// generate_docx.js — Proposal Penerjemah Dua Arah SIBI (Wi-Fi CSI + ESP32-S3, distilasi guru–murid)
// Struktur: [Sampul R5 akademik] -> [Daftar Isi (romawi kecil)] -> [BAB I-III + Daftar Pustaka (arab)]
// Gaya: Times New Roman 12pt, spasi 1,5 (line 360), margin 4-3-3-3 cm,
//       tabel tiga-garis 9pt, keterangan tabel di atas (kiri) & gambar di bawah (tengah),
//       penanda [PERLU ...] disorot kuning, sitasi IEEE [n] apa adanya.
// Basis: scripts/sempro/generate_docx.js (pipeline DPJ-4, sudah teruji) — diadaptasi untuk
//       paket translator-sibi-draft (80 rujukan, 10 tabel, 6 gambar BAB III).
const fs = require('fs');
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  ImageRun, PageBreak, Header, Footer, PageNumber, NumberFormat,
  AlignmentType, HeadingLevel, WidthType, BorderStyle, ShadingType,
  SectionType, TableOfContents, TableLayoutType, VerticalAlign,
} = require('/home/z/.npm-global/lib/node_modules/docx');

const parsed = JSON.parse(fs.readFileSync('/home/z/my-project/scripts/translator-sibi-docx/parsed-final.json', 'utf-8'));
const OUT = '/home/z/my-project/download/translator-sibi-final/Proposal-Studi-Kelayakan-Purwarupa-SIBI-CSI-ESP32S3.docx';

// ---------- Konstanta ----------
const FONT = { ascii: 'Times New Roman', hAnsi: 'Times New Roman', eastAsia: 'Times New Roman' };
const FONT_CODE = { ascii: 'Courier New', hAnsi: 'Courier New', eastAsia: 'Courier New' };
const BLACK = '000000';
const NB = { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' };
const noBorders = { top: NB, bottom: NB, left: NB, right: NB };
const allNoBorders = { top: NB, bottom: NB, left: NB, right: NB, insideHorizontal: NB, insideVertical: NB };
const PAGE = { width: 11906, height: 16838 };
const MARGIN = { top: 1701, bottom: 1701, left: 2268, right: 1701, header: 850, footer: 992 };
const CONTENT_W_TW = PAGE.width - MARGIN.left - MARGIN.right; // 7937 twips
const CONTENT_W_PX = Math.floor(CONTENT_W_TW / 1440 * 96);   // ~529 px @96dpi

function safeText(v, ph) {
  if (v === undefined || v === null || v === '' || String(v) === 'NaN' || String(v) === 'undefined') return ph || '[kosong]';
  return String(v);
}

// ---------- Run inline ----------
function makeRuns(runs, sizeHalf) {
  return runs.map(r => new TextRun({
    text: r.text,
    bold: !!r.bold,
    italics: !!r.italics,
    highlight: r.highlight ? 'yellow' : undefined,
    size: sizeHalf,
    color: BLACK,
    font: r.code ? FONT_CODE : FONT,
  }));
}

// ---------- Paragraf & heading ----------
function bodyPara(runs) {
  return new Paragraph({
    alignment: AlignmentType.JUSTIFIED,
    indent: { firstLine: 709 },
    spacing: { line: 360, after: 0 },
    children: makeRuns(runs, 24),
  });
}

function listItem(n, runs) {
  return new Paragraph({
    alignment: AlignmentType.LEFT,
    indent: { left: 1069, hanging: 360 },
    spacing: { line: 360, after: 60 },
    children: [new TextRun({ text: n + ' ', size: 24, color: BLACK, font: FONT }), ...makeRuns(runs, 24)],
  });
}

function h1(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_1,
    alignment: AlignmentType.CENTER,
    spacing: { before: 480, after: 360, line: Math.ceil(14 * 23), lineRule: 'atLeast' },
    children: [new TextRun({ text, bold: true, size: 28, color: BLACK, font: FONT })],
  });
}

function h2(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_2,
    alignment: AlignmentType.LEFT,
    spacing: { before: 360, after: 240, line: 360 },
    children: [new TextRun({ text, bold: true, size: 24, color: BLACK, font: FONT })],
  });
}

function h3(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_3,
    alignment: AlignmentType.LEFT,
    spacing: { before: 240, after: 120, line: 360 },
    children: [new TextRun({ text, bold: true, size: 24, color: BLACK, font: FONT })],
  });
}

// ---------- Tabel tiga-garis ----------
function colWidths(header, rows) {
  const n = header.length;
  const lens = header.map((h, c) => {
    let mx = Math.min(h.length, 60);
    for (const r of rows) mx = Math.max(mx, Math.min((r[c] || '').length, 60));
    return Math.max(mx, 3);
  });
  // Bobot sublinear agar kolom panjang tidak menelan semua ruang
  const w = lens.map(l => Math.pow(l, 0.62));
  const sum = w.reduce((a, b) => a + b, 0);
  let pct = w.map(x => Math.max(4, Math.round(x / sum * 100)));
  // Normalisasi ke 100
  let s = pct.reduce((a, b) => a + b, 0);
  pct = pct.map(x => Math.round(x * 100 / s));
  s = pct.reduce((a, b) => a + b, 0);
  pct[n - 1] += 100 - s;
  return pct;
}

function inlineCellRuns(text, bold) {
  // Parser inline untuk isi sel: penanda PERLU, tebal, miring, kode
  const runs = [];
  let buf = '', i = 0;
  const push = () => { if (buf) { runs.push({ text: buf }); buf = ''; } };
  while (i < text.length) {
    const rest = text.slice(i);
    let m;
    if ((m = rest.match(/^\[PERLU (?:DATA|RUJUKAN):[^\]]*\]/))) { push(); runs.push({ text: m[0], highlight: true }); i += m[0].length; }
    else if ((m = rest.match(/^\*\*([^*]+)\*\*/))) { push(); runs.push({ text: m[1], bold: true }); i += m[0].length; }
    else if ((m = rest.match(/^\*([^*\n]+)\*/))) { push(); runs.push({ text: m[1], italics: true }); i += m[0].length; }
    else if ((m = rest.match(/^`([^`]+)`/))) { push(); runs.push({ text: m[1], code: true }); i += m[0].length; }
    else { buf += text[i]; i += 1; }
  }
  push();
  return runs.map(r => new TextRun({
    text: r.text, bold: bold || !!r.bold, italics: !!r.italics,
    highlight: r.highlight ? 'yellow' : undefined,
    size: 18, color: BLACK, font: r.code ? FONT_CODE : FONT,
  }));
}

function threeLineTable(block) {
  const pct = colWidths(block.header, block.rows);
  const cellMargins = { top: 40, bottom: 40, left: 80, right: 80 };

  const headerRow = new TableRow({
    tableHeader: true, cantSplit: true,
    children: block.header.map((h, c) => new TableCell({
      width: { size: pct[c], type: WidthType.PERCENTAGE },
      borders: { top: NB, left: NB, right: NB, bottom: { style: BorderStyle.SINGLE, size: 4, color: BLACK } },
      margins: cellMargins,
      verticalAlign: VerticalAlign.CENTER,
      children: [new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { line: 276, before: 20, after: 20 },
        children: h === '' ? [] : inlineCellRuns(h, true),
      })],
    })),
  });

  const dataRows = block.rows.map(row => new TableRow({
    cantSplit: true,
    children: row.map((cell, c) => new TableCell({
      width: { size: pct[c], type: WidthType.PERCENTAGE },
      borders: noBorders,
      margins: cellMargins,
      children: [new Paragraph({
        alignment: AlignmentType.LEFT,
        spacing: { line: 276, before: 20, after: 20 },
        children: cell === '' ? [] : inlineCellRuns(cell, false),
      })],
    })),
  }));

  const table = new Table({
    width: { size: 100, type: WidthType.PERCENTAGE },
    layout: TableLayoutType.FIXED,
    borders: {
      top: { style: BorderStyle.SINGLE, size: 6, color: BLACK },
      bottom: { style: BorderStyle.SINGLE, size: 6, color: BLACK },
      left: NB, right: NB, insideHorizontal: NB, insideVertical: NB,
    },
    rows: [headerRow, ...dataRows],
  });

  const out = [];
  if (block.caption) {
    const m = block.caption.match(/^(Tabel \d+\.\d+)\s+(.*)$/);
    out.push(new Paragraph({
      keepNext: true,
      alignment: AlignmentType.LEFT,
      spacing: { before: 240, after: 120, line: 360 },
      children: [
        new TextRun({ text: m ? m[1] : block.caption, bold: true, size: 24, color: BLACK, font: FONT }),
        ...(m ? [new TextRun({ text: ' ' + m[2], size: 24, color: BLACK, font: FONT })] : []),
      ],
    }));
  }
  out.push(table);
  out.push(new Paragraph({ spacing: { after: 120, line: 240 }, children: [] }));
  return out;
}

// ---------- Gambar ----------
function pngSize(p) {
  const b = fs.readFileSync(p);
  return { w: b.readUInt32BE(16), h: b.readUInt32BE(20) };
}

function figureBlock(block) {
  const { w, h } = pngSize(block.png);
  let dispW = CONTENT_W_PX; // 529
  let dispH = Math.round(dispW * h / w);
  // Pengaman: tinggi tampil maksimum ~20,6 cm (780 px @96dpi) agar gambar +
  // keterangan selalu muat satu halaman; jika lebih, kecilkan proporsional.
  const MAXH_PX = 780;
  if (dispH > MAXH_PX) {
    dispH = MAXH_PX;
    dispW = Math.round(dispH * w / h);
  }
  const m = block.caption.match(/^(Gambar \d+\.\d+)\s+(.*)$/);
  return [
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { before: 240, after: 60 },
      keepNext: true, // kaitkan gambar dengan keterangannya agar tidak terpisah halaman
      children: [new ImageRun({ data: fs.readFileSync(block.png), transformation: { width: dispW, height: dispH }, type: 'png' })],
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { after: 240, line: 360 },
      children: [
        new TextRun({ text: m ? m[1] : block.caption, bold: true, size: 24, color: BLACK, font: FONT }),
        ...(m ? [new TextRun({ text: ' ' + m[2], size: 24, color: BLACK, font: FONT })] : []),
      ],
    }),
  ];
}

// ---------- Rujukan ----------
function refPara(runs) {
  return new Paragraph({
    alignment: AlignmentType.LEFT,
    indent: { left: 480, hanging: 480 },
    spacing: { line: 360, after: 120 },
    children: makeRuns(runs, 24),
  });
}

// ---------- Susun isi ----------
function renderBlocks(blocks) {
  const out = [];
  for (const b of blocks) {
    if (b.t === 'h1') out.push(h1(b.text));
    else if (b.t === 'h2') out.push(h2(b.text));
    else if (b.t === 'h3') out.push(h3(b.text));
    else if (b.t === 'p') out.push(bodyPara(b.runs));
    else if (b.t === 'li') out.push(listItem(b.n, b.runs));
    else if (b.t === 'table') out.push(...threeLineTable(b));
    else if (b.t === 'figure') out.push(...figureBlock(b));
    else if (b.t === 'ref') out.push(refPara(b.runs));
  }
  return out;
}

const bodyChildren = [
  ...renderBlocks(parsed.bab1),
  ...renderBlocks(parsed.bab2),
  ...renderBlocks(parsed.bab3),
  // parsed.dp sudah memuat heading H1 "DAFTAR PUSTAKA" dari berkas sumber
  ...renderBlocks(parsed.dp),
];

// ---------- Sampul (R5 Clean White, adaptasi Indonesia) ----------
function estimateTextWidth(text, pt) {
  let w = 0;
  for (const ch of text) {
    const code = ch.codePointAt(0);
    const isCJK = (code >= 0x4E00 && code <= 0x9FFF) || (code >= 0x3000 && code <= 0x303F) || (code >= 0xFF00 && code <= 0xFFEF);
    if (isCJK) w += pt * 20;
    else if (ch >= 'A' && ch <= 'Z') w += pt * 13; // huruf kapital Latin lebih lebar
    else w += pt * 11;
  }
  return w;
}

// Pecah judul Latin pada batas kata agar <= 3 baris pada ukuran font tertentu
function wrapLatin(title, pt, maxW) {
  const words = title.split(/\s+/);
  const lines = [];
  let cur = '';
  for (const wd of words) {
    const trial = cur ? cur + ' ' + wd : wd;
    if (estimateTextWidth(trial, pt) <= maxW || !cur) cur = trial;
    else { lines.push(cur); cur = wd; }
  }
  if (cur) lines.push(cur);
  return lines;
}

function calcTitleLayoutMixed(title, maxW, preferredPt, minPt, maxLines = 3) {
  let pt = preferredPt, lines;
  while (pt >= minPt) {
    lines = wrapLatin(title, pt, maxW);
    if (lines.length <= maxLines) break;
    pt -= 1;
  }
  if (!lines || lines.length > maxLines) { pt = minPt; lines = wrapLatin(title, pt, maxW); }
  // cegah baris yatim (1 kata pendek di baris terakhir)
  if (lines.length > 1) {
    const last = lines[lines.length - 1];
    if (last.split(' ').length === 1 && last.length <= 12) {
      const prev = lines[lines.length - 2].split(' ');
      const moved = prev.pop();
      lines[lines.length - 2] = prev.join(' ');
      lines[lines.length - 1] = moved + ' ' + last;
    }
  }
  return { titlePt: pt, titleLines: lines };
}

function buildCover() {
  const simMarginLR = 1701, simMarginT = 1200;
  const contentW = PAGE.width - simMarginLR * 2;

  // Judul baru pemilik (28 Okt 2026) — panjang (~270 karakter) sehingga izinkan hingga 5 baris sampul
  const fullTitle = 'STUDI KELAYAKAN PURWARUPA SISTEM PENERJEMAHAN DUA ARAH ANTARA SISTEM ISYARAT BAHASA INDONESIA (SIBI) DAN TEKS ATAU UJARAN BAHASA INDONESIA BERBASIS WI-FI CHANNEL STATE INFORMATION (CSI) DENGAN INFERENSI MODEL PADA ESP32-S3 DAN PEMROSESAN BAHASA PADA SERVER UNTUK KOSAKATA TERBATAS';
  const { titlePt, titleLines } = calcTitleLayoutMixed(fullTitle, contentW, 14, 10, 5);
  const titleSize = titlePt * 2;

  const metaEntries = [
    { label: 'Diajukan oleh', value: '[PERLU DATA: nama penulis]' },
    { label: 'NIM', value: '[PERLU DATA: NIM penulis]' },
    { label: 'Program Studi', value: '[PERLU DATA: program studi]' },
    { label: 'Universitas', value: '[PERLU DATA: nama universitas]' },
    { label: 'Pembimbing', value: '[PERLU DATA: nama pembimbing, bila sudah ditetapkan]' },
  ];

  // Anggaran tinggi (twips) — target total <= 15638
  const labelPt = 12;
  const docTypeH = 16 * 23 + 500;
  const titleH = titleLines.length * (titlePt * 23 + 160);
  const metaRowH = 560;
  const metaH = metaEntries.length * metaRowH;
  const footerH = 12 * 23 + 200;
  const spacers = 3 * 350;
  const fixedH = docTypeH + titleH + metaH + footerH + spacers;
  const remaining = Math.max(15638 - fixedH, 600);
  const topSpacing = Math.min(Math.floor(remaining * 0.30) + simMarginT, 4200);
  const midSpacing = Math.min(Math.floor((remaining - simMarginT) * 0.22), 2400);
  const bottomSpacing = Math.max(Math.min(remaining - (topSpacing - simMarginT) - midSpacing, 5600), 800);

  const children = [];
  children.push(new Paragraph({ spacing: { before: topSpacing }, children: [] }));

  // Jenis dokumen
  children.push(new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { after: 500, line: Math.ceil(16 * 23), lineRule: 'atLeast' },
    children: [new TextRun({ text: 'PROPOSAL PENELITIAN', bold: true, size: 32, color: BLACK, font: FONT, characterSpacing: 60 })],
  }));

  // Judul (2-3 baris, kapital, tebal)
  titleLines.forEach((ln, idx) => {
    children.push(new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { after: idx < titleLines.length - 1 ? 100 : 400, line: Math.ceil(titlePt * 23), lineRule: 'atLeast' },
      children: [new TextRun({ text: ln, bold: true, size: titleSize, color: BLACK, font: FONT })],
    }));
  });

  children.push(new Paragraph({ spacing: { before: midSpacing }, children: [] }));

  // Tabel meta 2 kolom (persentase; label kiri, nilai kiri bergaris bawah)
  const maxLabel = Math.max(...metaEntries.map(e => e.label.length));
  const labelNeedTw = (maxLabel + 3) * labelPt * 11;
  const valueNeedTw = 5600;
  const tablePct = Math.min(75, Math.max(55, Math.ceil((labelNeedTw + valueNeedTw) / 11906 * 100)));
  const labelPct = Math.max(22, Math.min(40, Math.ceil(labelNeedTw / (tablePct / 100 * 11906) * 100)));

  const metaTable = new Table({
    width: { size: tablePct, type: WidthType.PERCENTAGE },
    alignment: AlignmentType.CENTER,
    layout: TableLayoutType.FIXED,
    borders: allNoBorders,
    rows: metaEntries.map(e => new TableRow({
      cantSplit: true,
      children: [
        new TableCell({
          width: { size: labelPct, type: WidthType.PERCENTAGE },
          borders: noBorders,
          margins: { top: 60, bottom: 60, left: 0, right: 0 },
          children: [new Paragraph({
            alignment: AlignmentType.LEFT,
            spacing: { before: 60, after: 60, line: 400, lineRule: 'atLeast' },
            children: [new TextRun({ text: e.label + ' :', size: 24, color: BLACK, font: FONT })],
          })],
        }),
        new TableCell({
          width: { size: 100 - labelPct, type: WidthType.PERCENTAGE },
          borders: { top: NB, left: NB, right: NB, bottom: { style: BorderStyle.SINGLE, size: 4, color: BLACK } },
          margins: { top: 60, bottom: 60, left: 80, right: 0 },
          children: [new Paragraph({
            alignment: AlignmentType.LEFT,
            spacing: { before: 60, after: 60, line: 400, lineRule: 'atLeast' },
            children: [new TextRun({ text: e.value, size: 22, color: BLACK, font: FONT, highlight: 'yellow' })],
          })],
        }),
      ],
    })),
  });
  children.push(metaTable);

  children.push(new Paragraph({ spacing: { before: bottomSpacing }, children: [] }));

  // Baris tahun
  children.push(new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { line: Math.ceil(12 * 23), lineRule: 'atLeast' },
    children: [new TextRun({ text: 'TAHUN [PERLU DATA: tahun penyusunan]', size: 24, color: BLACK, font: FONT })],
  }));

  // Pembungkus 16838 exact
  return [new Table({
    width: { size: 100, type: WidthType.PERCENTAGE },
    layout: TableLayoutType.FIXED,
    borders: allNoBorders,
    rows: [new TableRow({
      height: { value: 16838, rule: 'exact' },
      children: [new TableCell({
        shading: { type: ShadingType.CLEAR, fill: 'FFFFFF' },
        borders: noBorders,
        verticalAlign: VerticalAlign.TOP,
        margins: { left: simMarginLR, right: simMarginLR },
        children,
      })],
    })],
  })];
}

// ---------- Footer ----------
function romanFooter() {
  return new Footer({
    children: [new Paragraph({
      alignment: AlignmentType.CENTER,
      children: [new TextRun({ children: [PageNumber.CURRENT], size: 20, color: BLACK, font: FONT })],
    })],
  });
}
function arabicFooter() {
  return new Footer({
    children: [new Paragraph({
      alignment: AlignmentType.RIGHT,
      children: [new TextRun({ children: [PageNumber.CURRENT], size: 20, color: BLACK, font: FONT })],
    })],
  });
}

// ---------- Daftar isi ----------
const tocChildren = [
  new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { before: 240, after: 360, line: Math.ceil(14 * 23), lineRule: 'atLeast' },
    children: [new TextRun({ text: 'DAFTAR ISI', bold: true, size: 28, color: BLACK, font: FONT })],
  }),
  new TableOfContents('Daftar Isi', { hyperlink: true, headingStyleRange: '1-3' }),
  new Paragraph({
    spacing: { before: 200 },
    children: [new TextRun({
      text: 'Catatan: daftar isi dibuat dengan kode bidang. Setelah dokumen diedit, klik kanan pada daftar isi lalu pilih "Update Field" agar nomor halaman mutakhir.',
      italics: true, size: 18, color: '888888', font: FONT,
    })],
  }),
];

// ---------- Dokumen ----------
const doc = new Document({
  creator: 'Penyusun',
  title: 'Proposal Studi Kelayakan Purwarupa Penerjemah Dua Arah SIBI — Wi-Fi CSI pada ESP32-S3',
  description: 'Proposal penelitian BAB I-III + Daftar Pustaka (distilasi guru-murid YOLO26-Pose ke model murid CSI) — judul baru 28 Okt 2026',
  styles: {
    default: {
      document: {
        run: { font: FONT, size: 24, color: BLACK },
        paragraph: { spacing: { line: 360 } },
      },
      heading1: {
        run: { font: FONT, size: 28, bold: true, color: BLACK },
        paragraph: { alignment: AlignmentType.CENTER, spacing: { before: 480, after: 360, line: 360 }, outlineLevel: 0 },
      },
      heading2: {
        run: { font: FONT, size: 24, bold: true, color: BLACK },
        paragraph: { spacing: { before: 360, after: 240, line: 360 }, outlineLevel: 1 },
      },
      heading3: {
        run: { font: FONT, size: 24, bold: true, color: BLACK },
        paragraph: { spacing: { before: 240, after: 120, line: 360 }, outlineLevel: 2 },
      },
    },
  },
  sections: [
    { // 1. Sampul — tanpa nomor halaman
      properties: { page: { size: PAGE, margin: { top: 0, bottom: 0, left: 0, right: 0 } } },
      children: buildCover(),
    },
    { // 2. Daftar isi — romawi kecil mulai i
      properties: {
        type: SectionType.NEXT_PAGE,
        page: { size: PAGE, margin: MARGIN, pageNumbers: { start: 1, formatType: NumberFormat.LOWER_ROMAN } },
      },
      footers: { default: romanFooter() },
      children: tocChildren,
    },
    { // 3. Isi — arab mulai 1
      properties: {
        type: SectionType.NEXT_PAGE,
        page: { size: PAGE, margin: MARGIN, pageNumbers: { start: 1, formatType: NumberFormat.DECIMAL } },
      },
      footers: { default: arabicFooter() },
      children: bodyChildren,
    },
  ],
});

Packer.toBuffer(doc).then(buf => {
  fs.writeFileSync(OUT, buf);
  console.log('DOCX ditulis:', OUT, buf.length, 'bytes');
});
