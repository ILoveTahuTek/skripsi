// generate_dpj4.js — Render DPJ-4 (Translasi Isyarat SIBI/BISINDO) saja
// Jalankan: node /home/z/my-project/scripts/generate_dpj4.js
"use strict";
const { renderDoc } = require("./dpj_common");

(async () => {
  const docs = [require("./dpj_content_4_isyarat")];
  for (const d of docs) {
    await renderDoc(d);
  }
  console.log("SELESAI: DPJ-4 dibuat.");
})().catch(err => { console.error(err); process.exit(1); });
