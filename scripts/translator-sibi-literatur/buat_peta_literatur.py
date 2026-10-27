# -*- coding: utf-8 -*-
"""Bangun peta literatur kanban (HTML) lalu render ke PNG via Playwright.
Output:
  - download/translator-sibi-literatur/Peta-Literatur-Titik-Temu.png
  - download/translator-sibi-literatur/Peta-Literatur-Titik-Temu.html (sumber editable)
"""
import asyncio, os, sys, html as H

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data_literatur import (COLUMNS, TITLE, SUBTITLE, META_LINE, MASALAH,
                            KESENJANGAN, TITIK_TEMU, STRIP_NOTE, FOOTER_NOTES)

BASE = '/home/z/my-project/download/translator-sibi-literatur'
HTML_OUT = os.path.join(BASE, 'Peta-Literatur-Titik-Temu.html')
PNG_OUT = os.path.join(BASE, 'Peta-Literatur-Titik-Temu.png')

ROLE_STYLE = {  # warna_peran -> (label, latar, teks, border)
    'blue':   ('Konteks & eksisting',    '#EFF6FF', '#1E40AF', '#93C5FD'),
    'green':  ('Bukti kelayakan',        '#F0FDF4', '#065F46', '#6EE7B7'),
    'amber':  ('Keterbatasan & risiko',  '#FFF7ED', '#92400E', '#FCD34D'),
    'purple': ('Preseden desain',        '#F5F3FF', '#5B21B6', '#C4B5FD'),
    'cyan':   ('Alat & sumber teknis',   '#ECFEFF', '#155E75', '#67E8F9'),
    'gray':   ('Metode & evaluasi',      '#F1F5F9', '#334155', '#CBD5E1'),
}

CSS = """
* { margin: 0; padding: 0; box-sizing: border-box; }
body { background: #FFFFFF; color: #111827;
  font-family: 'Carlito', 'Liberation Sans', 'DejaVu Sans', system-ui, sans-serif;
  -webkit-font-smoothing: antialiased; }
#root { width: fit-content; min-width: 2400px; padding: 44px 48px 36px; background: #FFFFFF; }

/* ---------- Kepala papan ---------- */
.board-title { font-size: 27px; font-weight: 700; color: #1E293B; text-align: center; }
.board-sub   { font-size: 14.5px; color: #475569; text-align: center; margin-top: 6px; font-weight: 600; }
.board-meta  { font-size: 11.5px; color: #94A3B8; text-align: center; margin-top: 6px;
  padding-bottom: 18px; border-bottom: 1px solid #E2E8F0; margin-bottom: 20px; }

/* ---------- Strip konvergensi (titik temu) ---------- */
.strip { display: flex; align-items: stretch; gap: 0; margin-bottom: 10px; }
.strip-box { border-radius: 12px; padding: 16px 18px; flex-shrink: 0; }
.strip-box.masalah { background: #FFFFFF; border: 2px solid #64748B; width: 360px; }
.strip-box.temu { background: linear-gradient(135deg, #1E3A5F, #2D4A6F);
  box-shadow: 0 4px 12px rgba(30,58,95,0.25); width: 400px; }
.strip-label { font-size: 11px; font-weight: 700; letter-spacing: 1.2px; margin-bottom: 7px; }
.masalah .strip-label { color: #64748B; }
.temu .strip-label { color: #93C5FD; }
.masalah .strip-text { font-size: 13px; color: #334155; line-height: 1.5; }
.temu .strip-text { font-size: 13.5px; color: #FFFFFF; line-height: 1.5; font-weight: 600; }
.strip-arrow { display: flex; align-items: center; justify-content: center;
  width: 44px; color: #94A3B8; font-size: 24px; flex-shrink: 0; }
.gaps-wrap { flex: 1; border: 1.5px dashed #CBD5E1; border-radius: 12px;
  padding: 12px 14px; background: #F8FAFC; display: flex; flex-direction: column; }
.gaps-title { font-size: 11px; font-weight: 700; letter-spacing: 1.2px; color: #64748B; margin-bottom: 8px; }
.gaps-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 7px; flex: 1; }
.gap-chip { background: #FFFFFF; border: 1px solid #E2E8F0; border-left: 3px solid #F59E0B;
  border-radius: 7px; padding: 7px 10px; font-size: 11.5px; color: #475569; line-height: 1.4;
  display: flex; align-items: center; gap: 8px; }
.gap-k { font-size: 10.5px; font-weight: 700; color: #B45309; background: #FEF3C7;
  border-radius: 10px; padding: 1px 8px; flex-shrink: 0; }
.strip-note { font-size: 12px; color: #64748B; text-align: center; margin: 10px 0 22px; line-height: 1.5; }

/* ---------- Kanban ---------- */
.kanban { display: flex; gap: 13px; align-items: flex-start; }
.col { width: 254px; flex-shrink: 0; background: #F8FAFC; border: 1px solid #E2E8F0;
  border-radius: 11px; padding: 10px; display: flex; flex-direction: column; gap: 8px; }
.col-head { border-radius: 8px; padding: 10px 11px; }
.col-no { font-size: 10.5px; font-weight: 700; letter-spacing: 1.5px; color: #64748B; }
.col-tanya { font-size: 13.5px; font-weight: 700; line-height: 1.35; margin-top: 3px; }
.col-meta { font-size: 10.5px; color: #64748B; margin-top: 5px; line-height: 1.4;
  padding-top: 6px; border-top: 1px solid rgba(100,116,139,0.18); }
.col-count { font-size: 10.5px; font-weight: 700; color: #475569; }

/* progresi satu rona biru-abu (terang -> gelap), 9 kolom */
.h1 { background: #F4F7FA; color: #334155; border-left: 4px solid #94A3B8; }
.h2 { background: #F0F4F8; color: #2F4256; border-left: 4px solid #8497AC; }
.h3 { background: #ECF1F6; color: #2B3E52; border-left: 4px solid #7489A1; }
.h4 { background: #E8EDF2; color: #273A4E; border-left: 4px solid #64748B; }
.h5 { background: #E4EAEF; color: #23364A; border-left: 4px solid #5B7A99; }
.h6 { background: #E0E7EF; color: #1F3050; border-left: 4px solid #4A6B8A; }
.h7 { background: #DCE3EC; color: #1B2A46; border-left: 4px solid #3E5E80; }
.h8 { background: #D8E0EA; color: #172540; border-left: 4px solid #345276; }
.h9 { background: #D4DDE8; color: #13203A; border-left: 4px solid #2B5473; }

/* ---------- Kartu ---------- */
.card { background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 8px;
  padding: 9px 10px 8px; box-shadow: 0 1px 2px rgba(15,23,42,0.04); }
.card-top { display: flex; align-items: baseline; gap: 7px; }
.ref-no { font-size: 11px; font-weight: 700; color: #FFFFFF; background: #475569;
  border-radius: 5px; padding: 1px 6px; flex-shrink: 0; font-variant-numeric: tabular-nums; }
.card-author { font-size: 12.5px; font-weight: 700; color: #1E293B; }
.card-year { font-size: 11px; color: #94A3B8; font-weight: 600; }
.card-grp { margin-left: auto; font-size: 10px; font-weight: 700; color: #CBD5E1; flex-shrink: 0; }
.card-venue { font-size: 10.5px; color: #94A3B8; font-style: italic; margin-top: 2px; }
.card-claim { font-size: 11.5px; color: #475569; line-height: 1.42; margin-top: 5px; }
.card-tags { display: flex; flex-wrap: wrap; gap: 4px; margin-top: 7px; }
.tag { font-size: 10px; font-weight: 700; padding: 1.5px 7px; border-radius: 9px; border: 1px solid; }
.tag-type { background: #F8FAFC; color: #64748B; border-color: #E2E8F0; font-weight: 600; }

/* ---------- Catatan celah ---------- */
.gap-note { border: 1.5px dashed #F59E0B; background: #FFFBF3; border-radius: 8px;
  padding: 9px 10px; font-size: 11px; color: #92400E; line-height: 1.45; }
.gap-note b { font-size: 10px; letter-spacing: 1px; }

/* ---------- Kaki papan ---------- */
.board-footer { margin-top: 24px; border-top: 1px solid #E2E8F0; padding-top: 14px; }
.legend-row { display: flex; align-items: center; gap: 10px; flex-wrap: wrap; margin-bottom: 10px; }
.legend-title { font-size: 11px; font-weight: 700; color: #64748B; width: 130px; flex-shrink: 0; }
.foot-note { font-size: 11px; color: #64748B; line-height: 1.55; margin-top: 6px; max-width: 1500px; }
.foot-note b { color: #475569; }
"""


def card_html(k):
    num, grp, author, year, venue, claim, role, jenis = k
    label, bg, fg, bd = ROLE_STYLE[role]
    y = f"({year})" if year else ""
    return f'''      <div class="card">
        <div class="card-top"><span class="ref-no">[{num}]</span><span class="card-author">{H.escape(author)}</span> <span class="card-year">{y}</span><span class="card-grp">grup {grp}</span></div>
        <div class="card-venue">{H.escape(venue)}</div>
        <div class="card-claim">{H.escape(claim)}</div>
        <div class="card-tags"><span class="tag" style="background:{bg};color:{fg};border-color:{bd};">{label}</span><span class="tag tag-type">{H.escape(jenis)}</span></div>
      </div>'''


def build_html():
    total = sum(len(c['kartu']) for c in COLUMNS)
    assert total == 79, f'jumlah kartu {total} != 79'

    gap_chips = '\n'.join(
        f'          <div class="gap-chip"><span class="gap-k">{k}</span><span>{H.escape(t)}</span></div>'
        for k, t in KESENJANGAN)

    cols = []
    for i, col in enumerate(COLUMNS, 1):
        cards = '\n'.join(card_html(k) for k in col['kartu'])
        cols.append(f'''    <div class="col">
      <div class="col-head h{i}">
        <div class="col-no">KOLOM {col['no']}</div>
        <div class="col-tanya">{H.escape(col['tanya'])}</div>
        <div class="col-meta">{H.escape(col['meta'])}<br/><span class="col-count">{len(col['kartu'])} rujukan</span></div>
      </div>
{cards}
      <div class="gap-note"><b>CELAH / IMPLIKASI</b><br/>{H.escape(col['celah'])}</div>
    </div>''')
    kanban = '\n'.join(cols)

    legend = ' '.join(
        f'<span class="tag" style="background:{bg};color:{fg};border-color:{bd};">{label}</span>'
        for label, bg, fg, bd in ROLE_STYLE.values())
    foot = '\n'.join(f'    <div class="foot-note">{n+1}. {H.escape(t)}</div>'
                     for n, t in enumerate(FOOTER_NOTES))

    return f'''<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8"/>
<title>{TITLE}</title>
<style>{CSS}</style>
</head>
<body>
<div id="root">
  <div class="board-title">{TITLE}</div>
  <div class="board-sub">{SUBTITLE}</div>
  <div class="board-meta">{META_LINE}</div>

  <div class="strip">
    <div class="strip-box masalah">
      <div class="strip-label">{MASALAH[0]}</div>
      <div class="strip-text">{H.escape(MASALAH[1])}</div>
    </div>
    <div class="strip-arrow">&#10132;</div>
    <div class="gaps-wrap">
      <div class="gaps-title">EMPAT KESENJANGAN (PETA MASALAH)</div>
      <div class="gaps-grid">
{gap_chips}
      </div>
    </div>
    <div class="strip-arrow">&#10132;</div>
    <div class="strip-box temu">
      <div class="strip-label">{TITIK_TEMU[0]}</div>
      <div class="strip-text">{H.escape(TITIK_TEMU[1])}</div>
    </div>
  </div>
  <div class="strip-note">{H.escape(STRIP_NOTE)}</div>

  <div class="kanban">
{kanban}
  </div>

  <div class="board-footer">
    <div class="legend-row"><span class="legend-title">Peran rujukan:</span>{legend}</div>
    <div class="legend-row"><span class="legend-title">Jenis sumber:</span><span class="tag tag-type">Jurnal</span><span class="tag tag-type">Prosiding</span><span class="tag tag-type">arXiv</span><span class="tag tag-type">Buku/bab</span><span class="tag tag-type">Dok. resmi</span><span class="tag tag-type">Model card</span><span class="tag tag-type">Repo</span><span class="tag tag-type">Regulasi</span><span class="tag tag-type">Kamus resmi</span></div>
{foot}
  </div>
</div>
</body>
</html>'''


async def render():
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={'width': 2600, 'height': 1600},
                                      device_scale_factor=1.5)
        await page.goto(f'file://{HTML_OUT}', wait_until='networkidle')
        await page.wait_for_timeout(400)
        el = page.locator('#root')
        bbox = await el.bounding_box()
        fit_w = max(2600, int(bbox['width'] + 60))
        fit_h = int(bbox['height'] + 60)
        await page.set_viewport_size({'width': fit_w, 'height': fit_h})
        await page.wait_for_timeout(250)
        bbox = await el.bounding_box()   # ukur ulang setelah viewport diubah
        await el.screenshot(path=PNG_OUT)
        await browser.close()
        print(f'viewport: {fit_w}x{fit_h}; elemen: {bbox["width"]:.0f}x{bbox["height"]:.0f}')
        print(f'OK {PNG_OUT} ({os.path.getsize(PNG_OUT)/1024:.0f} KB)')


if __name__ == '__main__':
    doc = build_html()
    os.makedirs(BASE, exist_ok=True)
    with open(HTML_OUT, 'w', encoding='utf-8') as f:
        f.write(doc)
    print(f'OK {HTML_OUT} ({len(doc)} karakter)')
    asyncio.run(render())
