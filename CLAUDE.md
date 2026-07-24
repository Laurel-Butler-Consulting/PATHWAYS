# PATHWAYS — project notes for Claude

Static single-page site: **"Pathways for Arts Educator Development."**
Everything lives in `index.html` (HTML + CSS + JS inline), with `images/`, `video/`,
and `data/programs.json`. No build step. Git remote: `ZZ72Z7Z7/PATHWAYS`.

## Daily-folder workflow (read this first)

Each workday the user **copies** the whole project into a new dated folder under
`/Users/jzk/Desktop/PATHWAYS/BUILDS/` — e.g. `PATHWAYS_260724`, then `PATHWAYS_260725`, …
and starts a fresh chat pointing here. The copy carries `.claude/` and this `CLAUDE.md`
along with it (both are gitignored/untracked, so they survive the copy, not a fresh clone).
The current working directory is always the new dated folder — treat it as the repo root.

## Previewing the site — USE THIS EXACT PROCESS

**Do NOT let `preview_start` spawn the server.** The preview harness sandboxes any server
it launches, and that sandbox cannot read the freshly-copied dated folder: `os.getcwd()`
returns `PermissionError: Operation not permitted`, and file reads silently 404. This is a
known, expected limitation of the daily-copy setup — **do not re-investigate it each time.**
A Bash-launched server has no such restriction.

Locked-in steps:

1. Start the server with **Bash**, from the repo root (cwd is already the repo root):
   ```bash
   python3 -m http.server 8765
   ```
   (run it in the background). Confirm with `curl -s -o /dev/null -w "%{http_code}" http://localhost:8765/index.html` → `200`.

2. Open the browser pane by **attaching** to that server — do not spawn:
   - `preview_start` with the `pathways` config (in `.claude/launch.json`) attaches to
     `http://localhost:8765` and reports *"no process was started"*, **or**
   - `preview_start` with `{url: "http://localhost:8765/index.html"}`.

3. If port 8765 is busy from a stale run, free it:
   `lsof -nP -iTCP:8765 -sTCP:LISTEN -t | xargs kill`

`.claude/launch.json` is intentionally an **attach** config (`url` + `port`, **no**
`runtimeExecutable`/`runtimeArgs`, no hardcoded path) so copying it forward each day is
harmless. Keep it that way — never restore a config that hardcodes a dated folder path.

## Open work items
- **Online-availability marking** (client request): research done for all 92 programs; NOT
  yet on the live site — awaiting client sign-off on the marker threshold. See
  [`notes/online-availability-README.md`](notes/online-availability-README.md) and
  `notes/online-availability-review.json`. Do not wire it in until the threshold is chosen.

## Reaching result views quickly

The site is a questionnaire SPA. Result pages render via `renderProfile(<key>)` into `#app`
(keys in the `PROFILES` map, e.g. `'ta'` = Teaching Artist). To inspect a result without
clicking through the quiz, run in the browser console:
```js
(async()=>{ if(typeof PROGRAMS_READY!=='undefined') await PROGRAMS_READY;
  document.getElementById('app').innerHTML = renderProfile('ta'); })()
```
Then read the DOM (`.prog-intro`, `.prog-region-title`) for authoritative text — screenshots
show the full-height hero on top, so trust the DOM read over the screenshot.
