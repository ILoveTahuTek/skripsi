// generate_dpj.js — Entry point: render 3 Dokumen Pengajuan Judul (DOCX)
// Jalankan: node /home/z/my-project/scripts/generate_dpj.js
"use strict";
const { renderDoc } = require("./dpj_common");

(async () => {
  const docs = [
    require("./dpj_content_1_ayam"),
    require("./dpj_content_2_kelas"),
    require("./dpj_content_3_asrama"),
    require("./dpj_content_4_isyarat"),
  ];
  for (const d of docs) {
    await renderDoc(d);
  }
  console.log("SELESAI: 4 dokumen DPJ dibuat.");
})().catch(err => { console.error(err); process.exit(1); });
