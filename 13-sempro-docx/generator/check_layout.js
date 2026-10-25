// check_layout.js — Pemeriksa geometri deterministik untuk fig31.html & fig32.html.
// Versi lama (check_overflow.js) hanya memeriksa luapan teks; tumpang tindih blok
// (diamond rotasi vs kotak, label vs garis) tidak terdeteksi. Skrip ini memeriksa:
//   1. Luapan teks dari kotaknya (scroll vs client + anak keluar induk)
//   2. Irisan antarbentuk: kotak-vs-kotak, diamond(rotasi)-vs-kotak, label-vs-bentuk
//   3. Garis panah menembus interior bentuk (lebih dari 8px) atau menimpa label
//   4. Semua elemen berada di dalam kanvas dengan margin >= 4px
//   5. Node di dalam panel tidak menempel border panel (margin >= 6px dari border)
const { chromium } = require('/home/z/.npm-global/lib/node_modules/playwright');

// ---------- util geometri ----------
const sub = (a, b) => [a[0] - b[0], a[1] - b[1]];
const cross = (o, a, b) => (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0]);
const dist = (a, b) => Math.hypot(a[0] - b[0], a[1] - b[1]);

function convexPts(kind, s) {
  if (kind === 'rect') return [[s.x, s.y], [s.x + s.w, s.y], [s.x + s.w, s.y + s.h], [s.x, s.y + s.h]];
  return s.pts; // poly
}
function pointInPoly(p, pts) {
  let sgn = 0;
  for (let i = 0; i < pts.length; i++) {
    const c = cross(pts[i], pts[(i + 1) % pts.length], p);
    if (c !== 0) { if (sgn === 0) sgn = Math.sign(c); else if (Math.sign(c) !== sgn) return false; }
  }
  return true;
}
function projRange(pts, n) {
  let lo = Infinity, hi = -Infinity;
  for (const p of pts) { const d = p[0] * n[0] + p[1] * n[1]; lo = Math.min(lo, d); hi = Math.max(hi, d); }
  return [lo, hi];
}
function polysIntersect(A, B) { // SAT untuk poligon cembung
  for (const P of [A, B]) {
    for (let i = 0; i < P.length; i++) {
      const e = sub(P[(i + 1) % P.length], P[i]);
      const n = [-e[1], e[0]];
      const [aLo, aHi] = projRange(A, n), [bLo, bHi] = projRange(B, n);
      if (aHi <= bLo || bHi <= aLo) return false;
    }
  }
  return true;
}
function shrinkPoly(pts, inset) { // skala ke pusat sejauh ~inset px
  const c = pts.reduce((a, p) => [a[0] + p[0] / pts.length, a[1] + p[1] / pts.length], [0, 0]);
  return pts.map(p => { const d = sub(p, c); const L = Math.hypot(...d) || 1; const k = Math.max(0, (L - inset) / L); return [c[0] + d[0] * k, c[1] + d[1] * k]; });
}
function clipSegPoly(a, b, pts) { // Liang–Barsky umum untuk poligon cembung
  let t0 = 0, t1 = 1;
  for (let i = 0; i < pts.length; i++) {
    const P = pts[i], Q = pts[(i + 1) % pts.length];
    const fa = cross(P, Q, a), fb = cross(P, Q, b); // >= 0 di dalam
    if (fa < 0 && fb < 0) return 0;
    if (fa < 0 || fb < 0) {
      const t = fa / (fa - fb);
      if (fa < 0) t0 = Math.max(t0, t); else t1 = Math.min(t1, t);
      if (t0 > t1) return 0;
    }
  }
  return (t1 - t0) * Math.hypot(b[0] - a[0], b[1] - a[1]);
}

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ deviceScaleFactor: 1 });
  let fail = 0;
  for (const f of ['fig31.html', 'fig32.html']) {
    await page.goto('file:///home/z/my-project/scripts/sempro/' + f);
    await page.waitForTimeout(300);
    const data = await page.evaluate(() => {
      const fig = document.querySelector('.fig');
      const R = (el) => { const r = el.getBoundingClientRect(); return { x: r.left, y: r.top, w: r.width, h: r.height }; };
      const shapes = [], segs = [];
      document.querySelectorAll('.node').forEach(el => shapes.push({ kind: 'rect', cls: 'node', ...R(el), label: el.textContent.trim() }));
      document.querySelectorAll('.elabel').forEach(el => shapes.push({ kind: 'rect', cls: 'elabel', ...R(el), label: el.textContent.trim() }));
      document.querySelectorAll('.panel-title').forEach(el => shapes.push({ kind: 'rect', cls: 'title', ...R(el), label: el.textContent.trim() }));
      document.querySelectorAll('.panel').forEach(el => shapes.push({ kind: 'panel', cls: 'panel', ...R(el) }));
      document.querySelectorAll('.gate').forEach(el => {
        const r = el.getBoundingClientRect(); // AABB setelah rotasi
        const cx = r.left + r.width / 2, cy = r.top + r.height / 2;
        const w = parseFloat(el.style.width) / 2, h = parseFloat(el.style.height) / 2;
        const c = Math.SQRT1_2, pts = [[-w, -h], [w, -h], [w, h], [-w, h]]
          .map(([x, y]) => [cx + (x - y) * c, cy + (x + y) * c]); // rotasi 45deg
        shapes.push({ kind: 'poly', cls: 'gate', pts, label: el.textContent.trim(), aabb: { x: r.left, y: r.top, w: r.width, h: r.height } });
      });
      document.querySelectorAll('svg.edges line, svg.edges path').forEach(el => {
        const d = el.getAttribute('d');
        if (d) { // parse "M x y H a V b ..." -> ruas-ruas ortogonal
          let x = null, y = null, prev = null;
          for (const t of d.split(/(?=[MHV])/)) {
            const cmd = t[0], nums = t.slice(1).trim().split(/[ ,]+/).map(Number);
            if (cmd === 'M') { x = nums[0]; y = nums[1]; prev = [x, y]; }
            else if (cmd === 'H') { const nx = nums[0]; segs.push([prev, [nx, y]]); prev = [nx, y]; x = nx; }
            else if (cmd === 'V') { const ny = nums[0]; segs.push([prev, [x, ny]]); prev = [x, ny]; y = ny; }
          }
        } else {
          segs.push([[+el.getAttribute('x1'), +el.getAttribute('y1')],
                     [+el.getAttribute('x2'), +el.getAttribute('y2')]]);
        }
      });
      return { shapes, segs, W: fig.clientWidth, H: fig.clientHeight,
               overflow: (() => {
        const out = [];
        document.querySelectorAll('.node, .gate-inner, .panel-title, .elabel').forEach(el => {
          const tag = el.className + ': "' + (el.textContent || '').trim().slice(0, 38) + '"';
          if (el.scrollHeight > el.clientHeight + 1 || el.scrollWidth > el.clientWidth + 1)
            out.push(`OVERFLOW ${tag} scroll=${el.scrollWidth}x${el.scrollHeight} client=${el.clientWidth}x${el.clientHeight}`);
          const pb = el.getBoundingClientRect();
          for (const ch of el.children) {
            const cb = ch.getBoundingClientRect();
            if (cb.bottom > pb.bottom + 1 || cb.top < pb.top - 1 || cb.right > pb.right + 1 || cb.left < pb.left - 1)
              out.push(`CHILD-OUT ${tag}`);
          }
        });
        return out;
      })() };
    });

    const issues = [...data.overflow];
    const S = data.shapes, segs = data.segs;

    // 2. irisan antarbentuk (panel = wadah: keberadaan di dalamnya sah, cek terpisah)
    for (let i = 0; i < S.length; i++) for (let j = i + 1; j < S.length; j++) {
      const a = S[i], b = S[j];
      if (a.cls === 'panel' || b.cls === 'panel') continue;
      const A = convexPts(a.kind, a), B = convexPts(b.kind, b);
      if (polysIntersect(A, B)) issues.push(`IRISAN ${a.cls}"${(a.label||'').slice(0,26)}" × ${b.cls}"${(b.label||'').slice(0,26)}"`);
    }
    // 5. node/label di dalam panel tidak menempel border (>= 6px dari border dalam)
    for (const p of S.filter(s => s.cls === 'panel')) {
      const bi = { x: p.x + 3, y: p.y + 3, w: p.w - 6, h: p.h - 6 };
      for (const s of S.filter(s => s.cls === 'node' || s.cls === 'title' || s.cls === 'elabel')) {
        const inside = s.x >= p.x && s.y >= p.y && s.x + s.w <= p.x + p.w && s.y + s.h <= p.y + p.h;
        if (!inside) continue;
        const m = Math.min(s.x - bi.x, bi.x + bi.w - (s.x + s.w), s.y - bi.y, bi.y + bi.h - (s.y + s.h));
        if (m < 6) issues.push(`MENEMPEL-BORDER ${s.cls}"${(s.label||'').slice(0,26)}" margin=${m.toFixed(1)}px (panel @${p.x},${p.y})`);
      }
    }
    // 3. garis menembus interior bentuk > 8px; garis menimpa label sama sekali
    for (const [p, q] of segs) {
      for (const s of S) {
        if (s.cls === 'panel') continue;
        const pts = s.kind === 'rect'
          ? [[s.x + 8, s.y + 8], [s.x + s.w - 8, s.y + 8], [s.x + s.w - 8, s.y + s.h - 8], [s.x + 8, s.y + s.h - 8]]
          : shrinkPoly(s.pts, 8);
        const pen = clipSegPoly(p, q, pts);
        const limit = s.cls === 'elabel' ? 2 : 8;
        if (pen > limit) issues.push(`GARIS-MENEMBUS ${s.cls}"${(s.label||'').slice(0,26)}" dalam=${pen.toFixed(1)}px seg=[${p.map(v=>v.toFixed(0))}]->[${q.map(v=>v.toFixed(0))}]`);
      }
    }
    // 4. batas kanvas
    for (const s of S) {
      const bb = s.kind === 'poly' ? s.aabb : s;
      if (bb.x < 4 || bb.y < 4 || bb.x + bb.w > data.W - 4 || bb.y + bb.h > data.H - 4)
        issues.push(`LUAR-KANVAS ${s.cls}"${(s.label||'').slice(0,26)}" aabb=${bb.x.toFixed(0)},${bb.y.toFixed(0)},${(bb.x+bb.w).toFixed(0)},${(bb.y+bb.h).toFixed(0)} kanvas=${data.W}x${data.H}`);
    }

    console.log(`=== ${f} ===`);
    if (issues.length) { fail++; console.log(issues.join('\n')); }
    else console.log('BERSIH — 0 luapan, 0 irisan blok, 0 garis menembus, 0 di luar kanvas');
  }
  await browser.close();
  process.exit(fail ? 1 : 0);
})();
