// helpers.js — builders for the SenseSIBI v16->v17 revision brief (Indonesian)
const {
  Paragraph, TextRun, Table, TableRow, TableCell, HeadingLevel, AlignmentType,
  WidthType, BorderStyle, ShadingType, TableLayoutType, PageBreak,
} = require("docx");

// ---------- palette (DS-1 Deep Sea, from design-system.md) ----------
const PAL = {
  bg: "0B1C2C", primary: "0B1C2C", accent: "529286",
  cover: { titleColor: "FFFFFF", subtitleColor: "B0B8C0", metaColor: "90989F", footerColor: "687078" },
  table: { headerBg: "529286", headerText: "FFFFFF", accentLine: "529286", innerLine: "BECFCC", surface: "E8ECEB" },
  blockFill: "F4F8F7", body: "000000",
};
const FONT = { ascii: "Times New Roman", eastAsia: "SimSun" };
const FONT_H = { ascii: "Times New Roman", eastAsia: "SimHei" };

const NB = { style: BorderStyle.NONE, size: 0, color: "FFFFFF" };
const noBorders = { top: NB, bottom: NB, left: NB, right: NB };
const allNoBorders = { top: NB, bottom: NB, left: NB, right: NB, insideHorizontal: NB, insideVertical: NB };

// ---------- rich run markup ----------
function R(parts, base = {}) {
  if (typeof parts === "string") parts = [parts];
  return parts.map((p) => {
    if (typeof p === "string") return new TextRun({ text: p, size: base.size || 24, font: FONT, color: base.color || PAL.body, ...base.run });
    const o = { text: p.t, size: base.size || 24, font: FONT, color: base.color || PAL.body, ...base.run };
    if (p.b) o.bold = true;
    if (p.i) o.italics = true;
    if (p.sub) o.subScript = true;
    if (p.sup) o.superScript = true;
    if (p.c) o.color = p.c;
    if (p.size) o.size = p.size;
    return new TextRun(o);
  });
}
const B = (t) => ({ t, b: true });
const I = (t) => ({ t, i: true });
const SUB = (t) => ({ t, sub: true, i: true });
const SUP = (t) => ({ t, sup: true });
const V = (t) => ({ t, i: true }); // variable, italic

// ---------- paragraphs ----------
function h1(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_1,
    spacing: { before: 420, after: 180, line: 340, lineRule: "atLeast" },
    keepNext: true,
    children: [new TextRun({ text, bold: true, size: 30, color: PAL.primary, font: FONT_H })],
  });
}
function h2(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_2,
    spacing: { before: 280, after: 120, line: 312 },
    keepNext: true,
    children: [new TextRun({ text, bold: true, size: 26, color: PAL.primary, font: FONT_H })],
  });
}
function h3(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_3,
    spacing: { before: 220, after: 100, line: 312 },
    keepNext: true,
    children: [new TextRun({ text, bold: true, size: 24, color: PAL.primary, font: FONT_H })],
  });
}
function p(parts, opts = {}) {
  return new Paragraph({
    alignment: AlignmentType.JUSTIFIED,
    spacing: { line: 312, after: 120, ...(opts.spacing || {}) },
    keepNext: opts.keepNext || false,
    children: R(parts, opts),
  });
}
function bullet(parts) {
  return new Paragraph({
    bullet: { level: 0 },
    alignment: AlignmentType.JUSTIFIED,
    spacing: { line: 312, after: 80 },
    children: R(parts),
  });
}
function caption(text) {
  return new Paragraph({
    keepNext: true,
    alignment: AlignmentType.LEFT,
    spacing: { before: 160, after: 80, line: 280 },
    children: [new TextRun({ text, bold: true, size: 20, color: "444444", font: FONT })],
  });
}
function note(text) {
  return new Paragraph({
    alignment: AlignmentType.JUSTIFIED,
    spacing: { before: 40, after: 160, line: 280 },
    children: [new TextRun({ text, italics: true, size: 19, color: "555555", font: FONT })],
  });
}
// centered equation; label appended right-ish as " (2.15')" within the same line
function eq(parts, label) {
  const kids = R(parts, { run: { italics: true } });
  if (label) kids.push(new TextRun({ text: "        " + label, size: 22, font: FONT, color: "555555" }));
  return new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { before: 100, after: 140, line: 312 },
    children: kids,
  });
}

// ---------- insertion block (ready-to-paste text) ----------
// Returns [labelParagraph, table]; label is a keepNext paragraph so no empty
// spacers are needed between consecutive blocks, and one row per paragraph
// lets page breaks fall between paragraphs.
function block(label, paras) {
  const edge = { style: BorderStyle.SINGLE, size: 4, color: PAL.table.innerLine };
  const left = { style: BorderStyle.SINGLE, size: 16, color: PAL.accent };
  const labelPara = new Paragraph({
    keepNext: true,
    spacing: { before: 200, after: 60, line: 280 },
    border: { left: { style: BorderStyle.SINGLE, size: 16, color: PAL.accent, space: 8 } },
    indent: { left: 60 },
    children: [new TextRun({ text: label, bold: true, size: 20, color: PAL.primary, font: FONT_H })],
  });
  const rows = [];
  for (const parts of paras) {
    rows.push(new TableRow({
      cantSplit: true,
      children: [new TableCell({
        shading: { type: ShadingType.CLEAR, fill: PAL.blockFill },
        margins: { top: 60, bottom: 60, left: 160, right: 160 },
        width: { size: 100, type: WidthType.PERCENTAGE },
        children: [new Paragraph({
          alignment: AlignmentType.JUSTIFIED,
          spacing: { line: 300, after: 40 },
          children: R(parts, { size: 22 }),
        })],
      })],
    }));
  }
  const table = new Table({
    width: { size: 100, type: WidthType.PERCENTAGE },
    borders: { top: edge, bottom: edge, right: edge, left, insideHorizontal: NB, insideVertical: NB },
    rows,
  });
  return [labelPara, table];
}
function spacer(h = 120) {
  return new Paragraph({ spacing: { after: h }, children: [] });
}

// ---------- data table ----------
// headers: string[]; rows: (string | parts[])[][]; widths: percentage numbers
function tbl(captionText, headers, rows, widths, opts = {}) {
  const cellSize = opts.cellSize || 20;
  const mkCell = (content, isHeader, w, alignCenter) => new TableCell({
    width: { size: w, type: WidthType.PERCENTAGE },
    shading: isHeader ? { type: ShadingType.CLEAR, fill: PAL.table.headerBg } : undefined,
    margins: { top: 60, bottom: 60, left: 110, right: 110 },
    verticalAlign: "top",
    children: [new Paragraph({
      alignment: alignCenter ? AlignmentType.CENTER : AlignmentType.LEFT,
      spacing: { line: 276 },
      children: R(content, { size: cellSize, color: isHeader ? PAL.table.headerText : PAL.body, run: isHeader ? { bold: true } : {} }),
    })],
  });
  const trows = [new TableRow({
    tableHeader: true, cantSplit: true,
    children: headers.map((hd, i) => mkCell(hd, true, widths[i], opts.centerHeader !== false)),
  })];
  for (const r of rows) {
    trows.push(new TableRow({
      cantSplit: true,
      children: r.map((c, i) => mkCell(c, false, widths[i], false)),
    }));
  }
  return new Table({
    width: { size: 100, type: WidthType.PERCENTAGE },
    borders: {
      top: { style: BorderStyle.SINGLE, size: 6, color: PAL.table.accentLine },
      bottom: { style: BorderStyle.SINGLE, size: 6, color: PAL.table.accentLine },
      left: NB, right: NB,
      insideHorizontal: { style: BorderStyle.SINGLE, size: 2, color: PAL.table.innerLine },
      insideVertical: NB,
    },
    rows: trows,
  });
}

// ---------- cover (Recipe R1, Latin-width adaptation) ----------
function splitTitleLines(title, charsPerLine) {
  if (title.length <= charsPerLine) return [title];
  const breakAfter = new Set([..."\u3001\u3002\uFF0C\uFF1A\uFF1B\uFF01\uFF1F", ..."-_\u2014\u2013\u00B7/", ..." \t"]);
  const lines = [];
  let remaining = title;
  while (remaining.length > charsPerLine) {
    let breakAt = -1;
    for (let i = charsPerLine; i >= Math.floor(charsPerLine * 0.6); i--) {
      if (i < remaining.length && breakAfter.has(remaining[i - 1])) { breakAt = i; break; }
    }
    if (breakAt === -1) {
      const limit = Math.min(remaining.length, Math.ceil(charsPerLine * 1.3));
      for (let i = charsPerLine + 1; i < limit; i++) {
        if (breakAfter.has(remaining[i - 1])) { breakAt = i; break; }
      }
    }
    if (breakAt === -1) breakAt = charsPerLine;
    lines.push(remaining.slice(0, breakAt).trim());
    remaining = remaining.slice(breakAt).trim();
  }
  if (remaining) lines.push(remaining);
  if (lines.length > 1 && lines[lines.length - 1].length <= 2) {
    const last = lines.pop();
    lines[lines.length - 1] += " " + last;
  }
  return lines;
}
function calcTitleLayout(title, maxWidthTwips, preferredPt = 40, minPt = 24) {
  const charWidth = (pt) => pt * 11; // Latin-dominant text
  const charsPerLine = (pt) => Math.floor(maxWidthTwips / charWidth(pt));
  let titlePt = preferredPt, lines;
  while (titlePt >= minPt) {
    const cpl = charsPerLine(titlePt);
    if (cpl < 2) { titlePt -= 2; continue; }
    lines = splitTitleLines(title, cpl);
    if (lines.length <= 3) break;
    titlePt -= 2;
  }
  if (!lines || lines.length > 3) {
    lines = splitTitleLines(title, charsPerLine(minPt));
    titlePt = minPt;
  }
  return { titlePt, titleLines: lines };
}
function calcCoverSpacing(params) {
  const { titleLineCount = 1, titlePt = 36, hasSubtitle = false, hasEnglishLabel = false,
    metaLineCount = 0, fixedHeight = 800, pageHeight = 16838, marginTop = 0, marginBottom = 0 } = params;
  const SAFETY = 1200;
  const usableHeight = pageHeight - marginTop - marginBottom - SAFETY;
  const titleHeight = titleLineCount * (titlePt * 23 + 200);
  const subtitleHeight = hasSubtitle ? (12 * 23 + 600) + 320 : 0; // +320: subtitle wraps to 2 lines
  const englishLabelHeight = hasEnglishLabel ? (9 * 23 + 600) : 0;
  const metaHeight = metaLineCount * (10 * 23 + 100);
  const implicitParaHeight = 3 * 300;
  const contentHeight = titleHeight + subtitleHeight + englishLabelHeight + metaHeight + fixedHeight + implicitParaHeight;
  const remainingSpace = usableHeight - contentHeight;
  const safeRemaining = Math.max(remainingSpace, 400);
  const FOOTER_MIN = 800;
  const rawTop = Math.floor(safeRemaining * 0.45);
  const rawBottom = Math.floor(safeRemaining * 0.45);
  const bottomSpacing = Math.max(rawBottom, FOOTER_MIN);
  const topSpacing = Math.max(rawTop - Math.max(0, FOOTER_MIN - rawBottom), 400);
  const midSpacing = Math.max(safeRemaining - topSpacing - bottomSpacing, 0);
  return { topSpacing, midSpacing, bottomSpacing };
}
function buildCoverR1(config) {
  const P = config.palette;
  const padL = 1200, padR = 800;
  const availableWidth = 11906 - padL - padR - 300;
  const { titlePt, titleLines } = calcTitleLayout(config.title, availableWidth, 40, 24);
  const titleSize = titlePt * 2;
  const spacing = calcCoverSpacing({
    titleLineCount: titleLines.length, titlePt,
    hasSubtitle: !!config.subtitle, hasEnglishLabel: !!config.englishLabel,
    metaLineCount: (config.metaLines || []).length, fixedHeight: 400,
  });
  const accentLeft = { style: BorderStyle.SINGLE, size: 8, color: P.accent, space: 12 };
  const children = [];
  children.push(new Paragraph({ spacing: { before: spacing.topSpacing } }));
  if (config.englishLabel) {
    children.push(new Paragraph({
      indent: { left: padL, right: padR }, spacing: { after: 500 },
      border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: P.accent, space: 8 } },
      children: [new TextRun({ text: config.englishLabel.split("").join("  "), size: 18, color: P.accent, font: { ascii: "Calibri", eastAsia: "SimHei" }, characterSpacing: 40 })],
    }));
  }
  for (let i = 0; i < titleLines.length; i++) {
    children.push(new Paragraph({
      indent: { left: padL },
      spacing: { after: i < titleLines.length - 1 ? 100 : 300, line: Math.ceil(titlePt * 23), lineRule: "atLeast" },
      children: [new TextRun({ text: titleLines[i], size: titleSize, bold: true, color: P.cover.titleColor, font: { eastAsia: "SimHei", ascii: "Arial" } })],
    }));
  }
  if (config.subtitle) {
    children.push(new Paragraph({
      indent: { left: padL, right: padR }, spacing: { after: 800, line: 340, lineRule: "atLeast" },
      children: [new TextRun({ text: config.subtitle, size: 24, color: P.cover.subtitleColor, font: { eastAsia: "Microsoft YaHei", ascii: "Arial" } })],
    }));
  }
  for (const line of (config.metaLines || [])) {
    children.push(new Paragraph({
      indent: { left: padL + 200, right: padR }, spacing: { after: 80, line: 300, lineRule: "atLeast" },
      border: { left: accentLeft },
      children: [new TextRun({ text: line, size: 22, color: P.cover.metaColor, font: { eastAsia: "Microsoft YaHei", ascii: "Arial" } })],
    }));
  }
  children.push(new Paragraph({ spacing: { before: spacing.bottomSpacing } }));
  children.push(new Paragraph({
    indent: { left: padL, right: padR },
    border: { top: { style: BorderStyle.SINGLE, size: 2, color: P.accent, space: 8 } },
    spacing: { before: 200 },
    children: [
      new TextRun({ text: config.footerLeft || "", size: 16, color: P.cover.footerColor, font: { ascii: "Arial" } }),
      new TextRun({ text: "                                        " }),
      new TextRun({ text: config.footerRight || "", size: 16, color: P.cover.footerColor, font: { ascii: "Arial" } }),
    ],
  }));
  return [new Table({
    width: { size: 100, type: WidthType.PERCENTAGE },
    layout: TableLayoutType.FIXED,
    borders: allNoBorders,
    rows: [new TableRow({
      height: { value: 16838, rule: "exact" },
      children: [new TableCell({
        shading: { type: ShadingType.CLEAR, fill: P.bg }, borders: noBorders,
        children,
      })],
    })],
  })];
}

module.exports = { PAL, FONT, FONT_H, R, B, I, SUB, SUP, V, h1, h2, h3, p, bullet, caption, note, eq, block, spacer, tbl, buildCoverR1 };
