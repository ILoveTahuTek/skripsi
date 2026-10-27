# -*- coding: utf-8 -*-
"""Verifikasi objektif peta literatur: luapan teks, elemen keluar batas #root, jumlah kartu."""
import asyncio, os
from playwright.async_api import async_playwright

HTML_OUT = '/home/z/my-project/download/translator-sibi-literatur/Peta-Literatur-Titik-Temu.html'

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={'width': 2600, 'height': 2800}, device_scale_factor=1)
        await page.goto(f'file://{HTML_OUT}', wait_until='networkidle')
        await page.wait_for_timeout(300)
        res = await page.evaluate('''() => {
          const root = document.getElementById('root');
          const rRect = root.getBoundingClientRect();
          const problems = [];
          // 1. elemen yang keluar dari batas #root
          for (const el of root.querySelectorAll('.card,.col-head,.gap-note,.strip-box,.gap-chip,.tag')) {
            const r = el.getBoundingClientRect();
            if (r.left < rRect.left - 1 || r.right > rRect.right + 1 ||
                r.top < rRect.top - 1 || r.bottom > rRect.bottom + 1) {
              problems.push('KELUAR BATAS: ' + el.className + ' -> ' + el.textContent.slice(0, 40));
            }
          }
          // 2. luapan teks horizontal (scrollWidth > clientWidth)
          for (const el of root.querySelectorAll('.card-claim,.card-author,.card-venue,.col-tanya,.col-meta,.gap-note,.strip-text,.gap-chip,.tag,.foot-note')) {
            if (el.scrollWidth > el.clientWidth + 2) {
              problems.push('LUAPAN TEKS: ' + el.className + ' (' + el.scrollWidth + '>' + el.clientWidth + ') -> ' + el.textContent.slice(0, 40));
            }
          }
          // 3. jumlah kartu & catatan celah
          const nCard = root.querySelectorAll('.card').length;
          const nGap = root.querySelectorAll('.gap-note').length;
          const nCol = root.querySelectorAll('.col').length;
          // 4. tinggi kolom (info keseimbangan)
          const heights = [...root.querySelectorAll('.col')].map(c => Math.round(c.getBoundingClientRect().height));
          // 5. cek tumpang tindih antar kartu (defensif; layout flex seharusnya mustahil)
          let overlap = 0;
          const cards = [...root.querySelectorAll('.card')];
          for (let i = 0; i < cards.length; i++) {
            const a = cards[i].getBoundingClientRect();
            for (let j = i + 1; j < cards.length; j++) {
              const b = cards[j].getBoundingClientRect();
              if (a.left < b.right - 2 && b.left < a.right - 2 &&
                  a.top < b.bottom - 2 && b.top < a.bottom - 2) overlap++;
            }
          }
          const refs = [...root.querySelectorAll('.ref-no')].map(e => e.textContent);
          const nums = refs.map(t => parseInt(t.slice(1, -1)));
          const missing = [];
          for (let n = 1; n <= 79; n++) if (!nums.includes(n)) missing.push(n);
          const dup = nums.filter((v, i) => nums.indexOf(v) !== i);
          return { problems, nCard, nGap, nCol, heights, overlap, missing, dup, refCount: refs.length };
        }''')
        await browser.close()
        print(f"kolom={res['nCol']} kartu={res['nCard']} catatan-celah={res['nGap']} ref-no={res['refCount']}")
        print(f"tinggi kolom: {res['heights']}")
        print(f"nomor hilang: {res['missing'] or 'tidak ada'}; ganda: {res['dup'] or 'tidak ada'}")
        print(f"tumpang tindih antar kartu: {res['overlap']}")
        if res['problems']:
            print('MASALAH:')
            for x in res['problems'][:30]:
                print('  -', x)
        else:
            print('MASALAH: tidak ada (0 luapan, 0 keluar batas)')

asyncio.run(main())
