# AGENTS.md — skripsi (WiFi CSI)

Sandbox kerja agent untuk skripsi WiFi CSI (ESP32 + RuView). Repo ini backup konteks + issue tracker.

## Agent skills

### Issue tracker

Issues dilacak di GitHub Issues `ILoveTahuTek/skripsi`, dioperasikan via REST API `curl` (gh CLI tidak terpasang). See `docs/agents/issue-tracker.md`.

### Triage labels

Label triage default mattpocock dipakai apa adanya (`needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`). See `docs/agents/triage-labels.md`.

### Domain docs

Single-context: `GLOSSARY.md` di root + `docs/adr/`. See `docs/agents/domain.md`.

## Keputusan setup (dibuat `/setup-matt-pocock-skills` 2026-10-12, default yang direkomendasikan skill)

1. **Issue tracker = GitHub Issues** — remote memang GitHub; issue bertahan di server walau sandbox reset (lebih tahan dari file lokal). Ubah dengan edit `docs/agents/issue-tracker.md`.
2. **AGENTS.md dipilih** (bukan CLAUDE.md) — repo ini multi-agent (GLM/Claude/Codex), AGENTS.md vendor-neutral dan sudah jadi konvensi repo mattpocock.
3. **Triage labels default** — triage skill terpasang, jadi Section B jalan dengan label default.
4. **Single-context domain docs** — repo bukan monorepo.

## Konteks kerja (baca dulu sebelum bekerja)

1. `GLOSSARY.md` — kosakata terkunci (flock-level, Delta-CSI, evidence-state, dst.)
2. `00-handoff-spec/` — handoff riset, spec eksekusi, laporan dewan LLM garis ayam
3. `01-ruview-exploration/` — deep-dive RuView + pemetaan 3 alat (ayam broiler / kelas SLB / asrama SLB)
4. `worklog.md` — log append-only; setiap sesi menambah bagian
5. `docs/adr/` — keputusan terkunci (lazy)

## Aturan kerja

- Bahasa kerja: Indonesia.
- Semua klaim kebaruan berlabel evidence-state (VERIFIED / SUPPORTED / SEARCH-LIMITED).
- Jangan pernah menuliskan token/kredensial ke file.
- Human-owned decisions (pemilihan topik final, judul, etika) tidak diambil oleh agent — jadi tiket `wayfinder:grilling`, bukan keputusan agent.
- Skill wayfinder/grilling/domain-modeling/research/... terpasang di sistem skill (31 mattpocock + academic-research; total 101).
