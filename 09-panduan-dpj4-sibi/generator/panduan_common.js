// panduan_common.js — Renderer DOCX untuk dokumen PANDUAN (gaya akademik dpj_common)
// Aturan: TNR 12pt, spasi 1,5 (line 360), tabel three-line, tanpa cover, tanpa TOC,
// tanpa page break di tengah isi, footer "- N -". Plus: quotePara (templat siap tempel)
// dan runsPara (paragraf dengan segmen bold).
"use strict";
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  Header, Footer, PageNumber, NumberFormat, AlignmentType, HeadingLevel,
  WidthType, BorderStyle, ShadingType,
} = require("docx");
const fs = require("fs");
const path = require("path");

const FONT_BODY = { ascii: "Times New Roman", eastAsia: "SimSun" };
const FONT_HEAD = { ascii: "Times New Roman", eastAsia: "SimHei" };

function safeText(v, ph) {
  if (v === undefined || v === null || v === "" || String(v) === "NaN" || String(v) === "undefined") {
    return ph || "\u3010Mohon diisi\u3011";
  }
  return String(v);
}

// ---------- Paragraph builders ----------
function bodyPara(text) {
  return new Paragraph({
    alignment: AlignmentType.JUSTIFIED,
    indent: { firstLine: 709 },
    spacing: { line: 360, after: 0 },
    children: [new TextRun({ text: safeText(text), size: 24, color: "000000", font: FONT_BODY })],
  });
}

function runsPara(segments, opts) {
  // segments: array of { t, b (bold), i (italics) }
  const o = opts || {};
  return new Paragraph({
    alignment: o.align || AlignmentType.JUSTIFIED,
    indent: o.noIndent ? undefined : { firstLine: 709 },
    spacing: { line: 360, after: o.after != null ? o.after : 0 },
    children: segments.map(s => new TextRun({
      text: safeText(s.t), bold: !!s.b, italics: !!s.i,
      size: o.size || 24, color: "000000", font: s.head ? FONT_HEAD : FONT_BODY,
    })),
  });
}

function numberedPara(text, n) {
  // Daftar bernomor eksplisit: rata kiri + hanging indent (pola DPJ yang lolos QA).
  return new Paragraph({
    alignment: AlignmentType.LEFT,
    indent: { left: 1069, hanging: 360 },
    spacing: { line: 360, after: 60 },
    children: [new TextRun({ text: n + ". " + safeText(text), size: 24, color: "000000", font: FONT_BODY })],
  });
}

function bulletPara(text) {
  return new Paragraph({
    alignment: AlignmentType.LEFT,
    bullet: { level: 0 },
    spacing: { line: 360, after: 60 },
    children: [new TextRun({ text: safeText(text), size: 24, color: "000000", font: FONT_BODY })],
  });
}

function quotePara(text) {
  // Templat kalimat siap tempel: menjorok + garis kiri (borders paragraf = aman lintas engine).
  return new Paragraph({
    alignment: AlignmentType.JUSTIFIED,
    indent: { left: 709, right: 354 },
    spacing: { line: 322, before: 60, after: 140 },
    border: { left: { style: BorderStyle.SINGLE, size: 6, color: "444444", space: 10 } },
    children: [new TextRun({ text: safeText(text), size: 22, color: "000000", font: FONT_BODY })],
  });
}

// ---------- Three-line table ----------
const NO_B = { style: BorderStyle.NONE };
function threeLineTable(spec) {
  const widths = spec.widths;
  const headerRow = new TableRow({
    tableHeader: true,
    cantSplit: true,
    children: spec.headers.map((h, i) => new TableCell({
      borders: { top: NO_B, bottom: { style: BorderStyle.SINGLE, size: 2, color: "000000" }, left: NO_B, right: NO_B },
      margins: { top: 60, bottom: 60, left: 120, right: 120 },
      width: { size: widths[i], type: WidthType.PERCENTAGE },
      shading: { type: ShadingType.CLEAR, fill: "F5F7FA" },
      children: [new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { line: 280 },
        children: [new TextRun({ text: safeText(h), bold: true, size: 21, color: "000000", font: FONT_BODY })],
      })],
    })),
  });
  const dataRows = spec.rows.map(r => new TableRow({
    cantSplit: true,
    children: r.map((cell, i) => new TableCell({
      borders: { top: NO_B, bottom: NO_B, left: NO_B, right: NO_B },
      margins: { top: 60, bottom: 60, left: 120, right: 120 },
      width: { size: widths[i], type: WidthType.PERCENTAGE },
      children: [new Paragraph({
        alignment: spec.centerCols && spec.centerCols.includes(i) ? AlignmentType.CENTER : AlignmentType.LEFT,
        spacing: { line: 280 },
        // Sel kosong eksplisit (string kosong) = pengelompokan visual yang disengaja,
        // bukan data hilang -> dirender kosong, BUKAN placeholder.
        children: [new TextRun({ text: cell === "" ? "" : safeText(cell), size: 21, color: "000000", font: FONT_BODY })],
      })],
    })),
  }));
  return new Table({
    width: { size: 100, type: WidthType.PERCENTAGE },
    borders: {
      top: { style: BorderStyle.SINGLE, size: 4, color: "000000" },
      bottom: { style: BorderStyle.SINGLE, size: 4, color: "000000" },
      left: NO_B, right: NO_B, insideHorizontal: NO_B, insideVertical: NO_B,
    },
    rows: [headerRow, ...dataRows],
  });
}

function tableCaption(text) {
  return new Paragraph({
    keepNext: true,
    alignment: AlignmentType.CENTER,
    spacing: { before: 200, after: 80, line: 300 },
    children: [new TextRun({ text: safeText(text), size: 21, color: "000000", font: FONT_BODY })],
  });
}

function tableSpacer() {
  return new Paragraph({ spacing: { after: 160, line: 240 }, children: [new TextRun({ text: " ", size: 12 })] });
}

// ---------- Title block (non-heading; tanpa cover) ----------
function titleBlock(doc) {
  const els = [];
  els.push(new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { line: 368, lineRule: "atLeast", after: 120 },
    children: [new TextRun({ text: safeText(doc.docLabel), bold: true, size: 32, color: "000000", font: FONT_HEAD })],
  }));
  if (doc.subjectLine) {
    els.push(new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { line: 340, lineRule: "atLeast", after: 120 },
      children: [new TextRun({ text: safeText(doc.subjectLine), size: 24, color: "000000", font: FONT_BODY })],
    }));
  }
  if (doc.metaLine) {
    els.push(new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { line: 300, after: 240 },
      children: [new TextRun({ text: safeText(doc.metaLine), size: 21, color: "333333", font: FONT_BODY, italics: true })],
    }));
  }
  return els;
}

// ---------- Chapter renderer ----------
function renderChapters(doc) {
  const els = [];
  for (const ch of doc.chapters) {
    if (ch.h1) {
      els.push(new Paragraph({
        heading: HeadingLevel.HEADING_1,
        alignment: AlignmentType.CENTER,
        spacing: { before: 480, after: 240, line: 360 },
        children: [new TextRun({ text: safeText(ch.h1), bold: true, size: 32, color: "000000", font: FONT_HEAD })],
      }));
    }
    for (const sub of (ch.subs || [])) {
      if (sub.h2) {
        els.push(new Paragraph({
          heading: HeadingLevel.HEADING_2,
          spacing: { before: 320, after: 160, line: 360 },
          children: [new TextRun({ text: safeText(sub.h2), bold: true, size: 30, color: "000000", font: FONT_HEAD })],
        }));
      }
      if (sub.h3) {
        els.push(new Paragraph({
          heading: HeadingLevel.HEADING_3,
          spacing: { before: 240, after: 120, line: 360 },
          children: [new TextRun({ text: safeText(sub.h3), bold: true, size: 26, color: "000000", font: FONT_HEAD })],
        }));
      }
      for (const p of (sub.paras || [])) els.push(bodyPara(p));
      for (const p of (sub.runParas || [])) els.push(runsPara(p.seg, p));
      for (const q of (sub.quotes || [])) els.push(quotePara(q));
      for (const p of (sub.paras2 || [])) els.push(bodyPara(p));
      if (sub.numbered) {
        sub.numbered.forEach((item, i) => els.push(numberedPara(item, i + 1)));
      }
      if (sub.bullets) {
        for (const item of sub.bullets) els.push(bulletPara(item));
      }
      for (const t of (sub.tables || [])) {
        els.push(tableCaption(t.caption));
        els.push(threeLineTable(t));
        els.push(tableSpacer());
      }
      for (const p of (sub.parasAfterTables || [])) els.push(bodyPara(p));
    }
    for (const p of (ch.paras || [])) els.push(bodyPara(p));
    for (const q of (ch.quotes || [])) els.push(quotePara(q));
    if (ch.numbered) {
      ch.numbered.forEach((item, i) => els.push(numberedPara(item, i + 1)));
    }
    if (ch.bullets) {
      for (const item of ch.bullets) els.push(bulletPara(item));
    }
    for (const t of (ch.tables || [])) {
      els.push(tableCaption(t.caption));
      els.push(threeLineTable(t));
      els.push(tableSpacer());
    }
  }
  return els;
}

// ---------- Document assembly ----------
function buildDoc(doc) {
  const header = new Header({
    children: [new Paragraph({
      alignment: AlignmentType.CENTER,
      border: { bottom: { style: BorderStyle.SINGLE, size: 1, color: "000000" } },
      spacing: { after: 60, line: 240 },
      children: [new TextRun({ text: safeText(doc.headerTitle), size: 18, color: "333333", font: FONT_BODY })],
    })],
  });
  const footer = new Footer({
    children: [new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { line: 240 },
      children: [
        new TextRun({ text: "- ", size: 21, font: FONT_BODY }),
        new TextRun({ children: [PageNumber.CURRENT], size: 21, font: FONT_BODY }),
        new TextRun({ text: " -", size: 21, font: FONT_BODY }),
      ],
    })],
  });

  const children = [...titleBlock(doc), ...renderChapters(doc)];

  return new Document({
    creator: "Mahasiswa",
    title: safeText(doc.docTitle),
    styles: {
      default: {
        document: {
          run: { font: FONT_BODY, size: 24, color: "000000" },
          paragraph: { spacing: { line: 360 } },
        },
        heading1: {
          run: { font: FONT_HEAD, size: 32, bold: true, color: "000000" },
          paragraph: { alignment: AlignmentType.CENTER, spacing: { before: 480, after: 240, line: 360 } },
        },
        heading2: {
          run: { font: FONT_HEAD, size: 30, bold: true, color: "000000" },
          paragraph: { spacing: { before: 320, after: 160, line: 360 } },
        },
        heading3: {
          run: { font: FONT_HEAD, size: 28, bold: true, color: "000000" },
          paragraph: { spacing: { before: 240, after: 120, line: 360 } },
        },
      },
    },
    sections: [{
      properties: {
        page: {
          size: { width: 11906, height: 16838 },
          margin: { top: 1440, bottom: 1440, left: 1701, right: 1417, header: 850, footer: 992 },
          pageNumbers: { start: 1, formatType: NumberFormat.DECIMAL },
        },
      },
      headers: { default: header },
      footers: { default: footer },
      children,
    }],
  });
}

async function renderDoc(doc, outDir) {
  fs.mkdirSync(outDir, { recursive: true });
  const outPath = path.join(outDir, doc.fileName);
  const buf = await Packer.toBuffer(buildDoc(doc));
  fs.writeFileSync(outPath, buf);
  console.log("OK  :", outPath, "(" + Math.round(buf.length / 1024) + " KB)");
  return outPath;
}

module.exports = { renderDoc, safeText };
