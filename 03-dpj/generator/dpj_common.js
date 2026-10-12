// dpj_common.js — Renderer DOCX Proposal Pengajuan Judul (akademik formal Indonesia)
// Aturan: TNR 12pt, spasi 1,5 (line 360), tabel three-line, sitasi [n] bernomor,
// daftar referensi hanging indent, TANPA cover identitas, TANPA TOC, TANPA page break.
// Halaman: A4, margin 2,54/2,54/3,0/2,5 cm, nomor halaman Arab mulai 1 di footer.
"use strict";
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  Header, Footer, PageNumber, NumberFormat, AlignmentType, HeadingLevel,
  WidthType, BorderStyle, ShadingType, LevelFormat,
} = require("docx");
const fs = require("fs");
const path = require("path");

const OUT_DIR = "/home/z/my-project/download/proposal-pengajuan-judul";

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

function listPara(text, refName, level) {
  // Daftar: rata kiri (bukan justify) sesuai aturan tata letak
  return new Paragraph({
    alignment: AlignmentType.LEFT,
    numbering: { reference: refName, level: level || 0 },
    spacing: { line: 360, after: 60 },
    children: [new TextRun({ text: safeText(text), size: 24, color: "000000", font: FONT_BODY })],
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

// ---------- Title block (non-heading; tanpa cover) ----------
function titleBlock(doc) {
  const els = [];
  els.push(new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { line: 368, lineRule: "atLeast", after: 120 },
    children: [new TextRun({ text: safeText(doc.docLabel, "PROPOSAL PENGAJUAN JUDUL SKRIPSI"), bold: true, size: 32, color: "000000", font: FONT_HEAD })],
  }));
  els.push(new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { line: 360, after: 240 },
    children: [new TextRun({ text: safeText(doc.subjectLine, ""), size: 24, color: "333333", font: FONT_BODY, italics: true })],
  }));
  els.push(new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { line: 322, lineRule: "atLeast", before: 120, after: 120 },
    children: [new TextRun({ text: "Judul Utama yang Diusulkan", bold: true, size: 24, color: "000000", font: FONT_HEAD })],
  }));
  els.push(new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { line: 322, lineRule: "atLeast", after: 240 },
    children: [new TextRun({ text: safeText(doc.judulUtama), bold: true, size: 28, color: "000000", font: FONT_HEAD })],
  }));
  return els;
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
        children: [new TextRun({ text: safeText(cell), size: 21, color: "000000", font: FONT_BODY })],
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

// ---------- Chapter renderer ----------
let listCounter = 0;
function makeListRefName() {
  listCounter += 1;
  return "list-dpj-" + listCounter;
}

function renderChapters(doc) {
  const els = [];
  let tableNo = 0;
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
      for (const p of (sub.paras || [])) els.push(bodyPara(p));
      if (sub.numbered) {
        const refName = makeListRefName();
        for (const item of sub.numbered) els.push(listPara(item, refName, 0));
      }
      if (sub.bullets) {
        for (const item of sub.bullets) els.push(bulletPara(item));
      }
      for (const t of (sub.tables || [])) {
        tableNo += 1;
        els.push(tableCaption(t.caption.replace("Tabel N", "Tabel " + tableNo)));
        els.push(threeLineTable(t));
        els.push(tableSpacer());
      }
    }
    for (const p of (ch.paras || [])) els.push(bodyPara(p));
    if (ch.numbered) {
      const refName = makeListRefName();
      for (const item of ch.numbered) els.push(listPara(item, refName, 0));
    }
    if (ch.bullets) {
      for (const item of ch.bullets) els.push(bulletPara(item));
    }
    for (const t of (ch.tables || [])) {
      tableNo += 1;
      els.push(tableCaption(t.caption.replace("Tabel N", "Tabel " + tableNo)));
      els.push(threeLineTable(t));
      els.push(tableSpacer());
    }
    if (ch.refs) {
      for (const r of ch.refs) {
        els.push(new Paragraph({
          alignment: AlignmentType.LEFT,
          indent: { left: 480, hanging: 480 },
          spacing: { line: 300, after: 60 },
          children: [new TextRun({ text: safeText(r), size: 21, color: "000000", font: FONT_BODY })],
        }));
      }
    }
  }
  return els;
}

// ---------- Document assembly ----------
function buildDoc(doc) {
  listCounter = 0;
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
    title: safeText(doc.judulUtama),
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

async function renderDoc(doc) {
  fs.mkdirSync(OUT_DIR, { recursive: true });
  const outPath = path.join(OUT_DIR, doc.fileName);
  const buf = await Packer.toBuffer(buildDoc(doc));
  fs.writeFileSync(outPath, buf);
  console.log("OK  :", outPath, "(" + Math.round(buf.length / 1024) + " KB)");
  return outPath;
}

module.exports = { renderDoc, OUT_DIR };
