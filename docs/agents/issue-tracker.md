# Issue tracker: GitHub

Issues and specs for this repo live as GitHub issues at **`ILoveTahuTek/skripsi`**. Use the GitHub REST API v3 via `curl` for all operations (the `gh` CLI is not installed in this sandbox; if a future session has `gh`, prefer it and update this file).

## Authentication

The token is provided by the user per-session (classic PAT, repo scope). **Never write the token to any file.** Load it into the environment first:

```bash
export GH_TOKEN="<token-dari-user>"
REPO="ILoveTahuTek/skripsi"
```

## Conventions (curl equivalents)

- **Create an issue**: `curl -s -X POST -H "Authorization: Bearer $GH_TOKEN" https://api.github.com/repos/$REPO/issues -d '{"title":"...","body":"...","labels":["..."]}'`
- **Read an issue**: `curl -s -H "Authorization: Bearer $GH_TOKEN" https://api.github.com/repos/$REPO/issues/<n>` (comments: append `/comments`)
- **List issues**: `curl -s -H "Authorization: Bearer $GH_TOKEN" "https://api.github.com/repos/$REPO/issues?state=open&labels=<label>"`
- **Comment on an issue**: `curl -s -X POST .../issues/<n>/comments -d '{"body":"..."}'`
- **Apply / remove labels**: `curl -s -X POST .../issues/<n>/labels -d '{"labels":["..."]}'` / `DELETE` with body
- **Close**: `curl -s -X PATCH .../issues/<n> -d '{"state":"closed"}'`

## Pull requests as a triage surface

**PRs as a request surface: no.** _(Set to `yes` if this repo treats external PRs as feature requests; `/triage` reads this flag.)_

## When a skill says "publish to the issue tracker"

Create a GitHub issue.

## When a skill says "fetch the relevant ticket"

Fetch the issue + its comments via the REST API.

## Wayfinding operations

Used by `/wayfinder`. The **map** is a single issue with **child** issues as tickets.

- **Map**: a single issue labelled `wayfinder:map`, holding the Notes / Decisions-so-far / Fog body.
- **Child ticket**: an issue linked to the map as a GitHub sub-issue via REST (`POST /repos/{owner}/{repo}/issues/{parent}/sub_issues` with `{"sub_issue_id": <db-id>}`). Where sub-issues aren't available, add the child to a task list in the map body and put `Part of #<map>` at the top of the child body. Labels: `wayfinder:<type>` (`research`/`prototype`/`grilling`/`task`). Once claimed, the ticket is assigned to the driving dev.
- **Blocking**: GitHub's **native issue dependencies** (UI-visible). Add an edge with `POST /repos/{owner}/{repo}/issues/<child>/dependencies/blocked_by` with `{"issue_id": <blocker-db-id>}` where the db-id is the issue's `.id` field (NOT the `#number`). Where dependencies aren't available, fall back to a `Blocked by: #<n>, #<n>` line at the top of the child body. A ticket is unblocked when every blocker is closed.
- **Frontier query**: list the map's open children, drop any with an open blocker (`issue_dependencies_summary.blocked_by > 0`) or an assignee; first in map order wins.
- **Claim**: `PATCH /repos/{owner}/{repo}/issues/<n>` with assignees — the session's first write.
- **Resolve**: post the answer as a comment, close the issue, then append a context pointer (gist + link) to the map's Decisions-so-far.
