// generate_panduan_dpj4_sibi.js — Rakit dan render Panduan Penulisan Proposal DPJ-4 (SIBI-only)
"use strict";
const { renderDoc } = require("./panduan_common.js");
const { chaptersA } = require("./panduan_content_a.js");
const { chaptersB } = require("./panduan_content_b.js");

const OUT_DIR = "/home/z/my-project/download/panduan-proposal";

const doc = {
  fileName: "PANDUAN_Penulisan_Proposal_DPJ-4_SIBI.docx",
  docTitle: "Panduan Penulisan Proposal Pengajuan Judul DPJ-4 SIBI (Wi-Fi CSI)",
  docLabel: "PANDUAN PENULISAN PROPOSAL PENGAJUAN JUDUL",
  subjectLine: "DPJ-4 — Pengenalan Gestur Bahasa Isyarat SIBI Berbasis Wi-Fi Channel State Information pada ESP32 untuk Prasarana Edukasi (Lingkup SIBI, tanpa BISINDO)",
  metaLine: "Disusun dari korpus Drive D4 TRSE Universitas Negeri Malang (69 dokumen), skill proposal-writing hasil GEPA, skill naskah-id, dan 22 referensi terverifikasi Crossref",
  headerTitle: "Panduan Penulisan Proposal — DPJ-4 SIBI (Wi-Fi CSI ESP32)",
  chapters: [...chaptersA, ...chaptersB],
};

renderDoc(doc, OUT_DIR)
  .then(p => console.log("Selesai:", p))
  .catch(e => { console.error("GAGAL:", e); process.exit(1); });
