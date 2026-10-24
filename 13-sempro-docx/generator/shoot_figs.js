// Screenshot kedua figur HTML menjadi PNG resolusi tinggi (Playwright, deviceScaleFactor 2)
const { chromium } = require('/home/z/.npm-global/lib/node_modules/playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ deviceScaleFactor: 2 });
  const jobs = [
    ['fig31.html', 'gambar-3.1.png', '#fig31'],
    ['fig32.html', 'gambar-3.2.png', '#fig32'],
  ];
  for (const [src, out, sel] of jobs) {
    await page.goto('file:///home/z/my-project/scripts/sempro/' + src);
    await page.waitForTimeout(400);
    const el = page.locator(sel);
    await el.screenshot({ path: '/home/z/my-project/download/sempro-dpj4-sibi-csi/assets/' + out });
    console.log('OK', out);
  }
  await browser.close();
})();
