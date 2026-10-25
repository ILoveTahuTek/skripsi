// check_overflow.js — ukur objektif: apakah ada teks yang meluber dari kotaknya?
const { chromium } = require('/home/z/.npm-global/lib/node_modules/playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ deviceScaleFactor: 1 });
  for (const f of ['fig31.html', 'fig32.html']) {
    await page.goto('file:///home/z/my-project/scripts/sempro/' + f);
    await page.waitForTimeout(300);
    const issues = await page.evaluate(() => {
      const out = [];
      const els = document.querySelectorAll('.node, .gate-inner, .panel-title, .elabel');
      els.forEach((el, i) => {
        const tag = el.className + '#' + i + ': "' + (el.textContent || '').trim().slice(0, 40) + '..."';
        // overflow konten vs kotak (flex center menengahkan teks; cek scroll vs client + bounding)
        const sh = el.scrollHeight, ch = el.clientHeight;
        const sw = el.scrollWidth, cw = el.clientWidth;
        if (sh > ch + 1 || sw > cw + 1) {
          out.push(`OVERFLOW ${tag} scroll=${sw}x${sh} client=${cw}x${ch}`);
        }
        // cek juga anak-anak (italic dsb.) keluar bounding parent
        const pb = el.getBoundingClientRect();
        for (const child of el.children) {
          const cb = child.getBoundingClientRect();
          if (cb.bottom > pb.bottom + 1 || cb.top < pb.top - 1 || cb.right > pb.right + 1 || cb.left < pb.left - 1) {
            out.push(`CHILD-OUT ${tag} childDelta b=${(cb.bottom-pb.bottom).toFixed(1)} t=${(pb.top-cb.top).toFixed(1)} r=${(cb.right-pb.right).toFixed(1)} l=${(pb.left-cb.left).toFixed(1)}`);
          }
        }
      });
      return out;
    });
    console.log('===', f, '===');
    console.log(issues.length ? issues.join('\n') : 'TIDAK ADA OVERFLOW — semua teks muat di kotaknya');
  }
  await browser.close();
})();
