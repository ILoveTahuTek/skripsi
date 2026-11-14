// gen.js — assembles Dokumen Revisi Terarah SenseSIBI v16 -> v17
const {
  Document, Packer, Paragraph, TextRun, Header, Footer, AlignmentType,
  PageNumber, NumberFormat, SectionType, TableOfContents, PageBreak,
} = require("docx");
const fs = require("fs");
const { PAL, buildCoverR1 } = require("./helpers");

const content1 = require("./content1");
const content2 = require("./content2");
const content3 = require("./content3");

const pgSize = { width: 11906, height: 16838 };
const pgMargin = { top: 1440, bottom: 1440, left: 1701, right: 1417 };

function pageHeader() {
  return new Header({
    children: [new Paragraph({
      alignment: AlignmentType.RIGHT,
      spacing: { after: 0 },
      border: { bottom: { style: "single", size: 2, color: "BECFCC", space: 4 } },
      children: [new TextRun({ text: "Dokumen Revisi Terarah \u2014 SenseSIBI v16 menuju v17", size: 16, color: "888888", font: { ascii: "Times New Roman", eastAsia: "SimSun" } })],
    })],
  });
}
function pageFooter() {
  return new Footer({
    children: [new Paragraph({
      alignment: AlignmentType.CENTER,
      children: [new TextRun({ children: [PageNumber.CURRENT], size: 18, color: "808080", font: { ascii: "Times New Roman" } })],
    })],
  });
}

const coverConfig = {
  title: "Revisi Terarah Proposal SenseSIBI v16 menuju v17",
  subtitle: "Perbaikan aditif dan terarah atas evaluasi kritis v16 \u2014 disusun mengikuti urutan enam langkah",
  englishLabel: "REVISION BRIEF",
  metaLines: [
    "Objek revisi: Proposal-SenseSIBI-Studi-Kelayakan-v16.pdf (49 halaman)",
    "Basis: evaluasi kritis 13 November 2026 dan audit kartu model checkpoint RuView",
    "Prinsip: aditif dan terarah \u2014 struktur proposal dipertahankan, definisi terbuka dikunci",
  ],
  footerLeft: "SenseSIBI \u2014 dokumen kerja internal",
  footerRight: "13 November 2026",
  palette: { bg: PAL.bg, accent: PAL.accent, cover: PAL.cover },
};

const bodyChildren = [...content1.build(), ...content2.build(), ...content3.build()];

const doc = new Document({
  creator: "SenseSIBI",
  title: "Dokumen Revisi Terarah Proposal SenseSIBI (v16 menuju v17)",
  styles: {
    default: {
      document: {
        run: { font: { ascii: "Times New Roman", eastAsia: "SimSun" }, size: 24, color: "000000" },
        paragraph: { spacing: { line: 312 } },
      },
      heading1: {
        run: { font: { ascii: "Times New Roman", eastAsia: "SimHei" }, size: 30, bold: true, color: PAL.primary },
        paragraph: { spacing: { before: 420, after: 180, line: 340 }, outlineLevel: 0 },
      },
      heading2: {
        run: { font: { ascii: "Times New Roman", eastAsia: "SimHei" }, size: 26, bold: true, color: PAL.primary },
        paragraph: { spacing: { before: 280, after: 120, line: 312 }, outlineLevel: 1 },
      },
      heading3: {
        run: { font: { ascii: "Times New Roman", eastAsia: "SimHei" }, size: 24, bold: true, color: PAL.primary },
        paragraph: { spacing: { before: 220, after: 100, line: 312 }, outlineLevel: 2 },
      },
    },
  },
  sections: [
    { // Section 1: cover — margin 0, no footer, no page number
      properties: { page: { size: pgSize, margin: { top: 0, bottom: 0, left: 0, right: 0 } } },
      children: buildCoverR1(coverConfig),
    },
    { // Section 2: TOC — Roman numerals
      properties: {
        type: SectionType.NEXT_PAGE,
        page: { size: pgSize, margin: pgMargin, pageNumbers: { start: 1, formatType: NumberFormat.UPPER_ROMAN } },
      },
      headers: { default: pageHeader() },
      footers: { default: pageFooter() },
      children: [
        new Paragraph({
          alignment: AlignmentType.CENTER,
          spacing: { before: 480, after: 360 },
          children: [new TextRun({ text: "DAFTAR ISI", bold: true, size: 30, font: { ascii: "Times New Roman", eastAsia: "SimHei" }, color: PAL.primary })],
        }),
        new TableOfContents("Daftar Isi", { hyperlink: true, headingStyleRange: "1-2" }),
        new Paragraph({
          spacing: { before: 200 },
          children: [new TextRun({
            text: "Catatan: Daftar isi ini dibuat dengan kode field. Agar nomor halaman akurat setelah penyuntingan, klik kanan daftar isi lalu pilih \u201CUpdate Field\u201D.",
            italics: true, size: 18, color: "888888", font: { ascii: "Times New Roman", eastAsia: "SimSun" },
          })],
        }),
        // no trailing PageBreak here: the body section below is SectionType.NEXT_PAGE;
        // a PageBreak + section break would create a blank page
      ],
    },
    { // Section 3: body — Arabic, restart at 1
      properties: {
        type: SectionType.NEXT_PAGE,
        page: { size: pgSize, margin: pgMargin, pageNumbers: { start: 1, formatType: NumberFormat.DECIMAL } },
      },
      headers: { default: pageHeader() },
      footers: { default: pageFooter() },
      children: bodyChildren,
    },
  ],
});

const OUT = process.argv[2] || "/home/z/my-project/download/sensesibi-v10/Dokumen-Revisi-Terarah-SenseSIBI-v16-ke-v17.docx";
Packer.toBuffer(doc).then((buf) => {
  fs.writeFileSync(OUT, buf);
  console.log("WROTE", OUT, buf.length, "bytes");
});
