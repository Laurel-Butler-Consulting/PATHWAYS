# PATHWAYS — project notes for Claude

## Working style — read before doing anything

- Communicate functionally — no pleasantries, sign-offs, or human-framing.
- **Build only what is explicitly requested or approved.** Offer suggestions — a likely oversight,
  a better approach, or a conflict with best practice — as proposals, and wait for a yes. Do not
  widen scope on your own initiative; that includes "helpful" extra tooling, refactors, or notes.
  Verifying and testing the requested change is part of the request. Building new tooling to
  verify it is not.
- **Ask approval before creating or writing any file.**
- Plain, concise English. The user is an experienced designer, **not** an experienced coder.
  Explain a technical term only where they'd need it with a client or another developer
  (captions/WebVTT, bitrate, aspect ratio, faststart, fallback, accessibility). Skip
  code-internals vocabulary entirely — DOM APIs, event names, browser-engine behaviour, function
  names. Describe what they'll see and do, not how the code achieves it. Lead with the outcome and
  the decision they need to make.
- Keep output short. Long technical reports are hard to act on — summarise, then offer detail.

Static single-page site: **"Arts Educator Pathways"** (renamed 2026-08-02 from "Pathways for Arts
Educator Development" — the old name survives only in `archive/260226/`, a historical snapshot).
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
   python3 -m http.server 8765 --bind 127.0.0.1
   ```
   (run it in the background). Confirm with `curl -s -o /dev/null -w "%{http_code}" http://localhost:8765/index.html` → `200`.

   ⚠ **Keep `--bind 127.0.0.1`.** Without it the server publishes the entire project folder to
   the whole local network — every file, not just `index.html`. On a café or client network
   anyone nearby can read `notes/`, `data/`, and the drafts. The pre-launch password gate does
   **not** cover this: it is JavaScript inside `index.html`, so fetching any other file directly
   walks straight past it. `--bind 127.0.0.1` restricts the server to this Mac and changes
   nothing about previewing.

2. Open the browser pane by **attaching** to that server — do not spawn:
   - `preview_start` with the `pathways` config (in `.claude/launch.json`) attaches to
     `http://localhost:8765` and reports *"no process was started"*, **or**
   - `preview_start` with `{url: "http://localhost:8765/index.html"}`.

3. If port 8765 is busy from a stale run, free it:
   `lsof -nP -iTCP:8765 -sTCP:LISTEN -t | xargs kill`

`.claude/launch.json` is intentionally an **attach** config (`url` + `port`, **no**
`runtimeExecutable`/`runtimeArgs`, no hardcoded path) so copying it forward each day is
harmless. Keep it that way — never restore a config that hardcodes a dated folder path.

## Permission prompts — what is pre-approved, and what is not

Set up 2026-08-02 to stop the constant approval prompts. Lives in `.claude/settings.json`, which is
gitignored: it travels with the daily folder copy but **not** with a fresh clone.

**Pre-approved** (all local to this Mac): the browser-preview tools — screenshots, reading the page
and its errors and network traffic, resizing, clicking, page inspection, listing tabs — plus
`python3 -m http.server 8765 --bind 127.0.0.1` and `python3 scripts/build-scan.py`.

**Still prompts, deliberately.** Navigating the preview to an address, attaching the preview pane,
and `curl`. These are the ones that reach *outside* this machine: they reveal the IP address, and
anything placed in the address travels with it. That prompt is the checkpoint that stops text found
in a web page, an error message or a file from turning into an outbound request. Keeping it is worth
far more than keeping a prompt on "take a screenshot". Don't pre-approve them for convenience.

File edits also still prompt, by choice — on a single-file site where one bad character blanks the
page, the per-edit look is the checkpoint.

**Removed 2026-08-02:** `Bash(python3 -c ' *)` and `Bash(node -e ' *)`, both previously approved.
They allowed running any code at all without asking — far broader than anything else on the list.
Don't let them back in; approve the specific command instead.

Also cleaned out 76 dead entries pinned to old dated folders (`PATHWAYS_260602/…`). Approvals saved
as one exact command with a dated path can never match again, which is why the file grew without
reducing the prompts. Prefer a pattern over an exact long command when approving.

## Open work items

**Master checklist (canonical): [`notes/BUILD-CHECKLIST.md`](notes/BUILD-CHECKLIST.md)** — keep it
updated as work is done. For live mechanical status derived from the files, run
`python3 scripts/build-scan.py`. The guardrails below still apply (don't wire in gated items early).

### Video playback — BUILT 2026-07-27, waiting on content

The player is wired and verified; nothing is switched on because no clips exist yet.

- Clips go in `video/nodes/`, named after the **node key** (`welcome.mp4`, `lifeTA.mp4`, …) —
  **not** per persona: 11 videos, 8 presenters, Laurel and Ricky each have three, so persona
  names collide. Full table + export settings: [`notes/video-export-spec.md`](notes/video-export-spec.md).
- Switch a node on with `v:1` on its `NODES` entry in index.html, and `cc:1` once a `.vtt` sits
  beside the clip. A `v:1` with no file falls back to the placeholder still — it can't show a
  broken player. Mute/CC buttons only render when there's actually a clip/caption file.
- **Captions are drawn by the site**, not the browser (the native caption box renders underneath
  the Skip/CC/mute row and can't be moved). Styled in CSS as `.qv-caps`. Do **not** add cue
  positioning to the `.vtt` files — it's ignored.
- Captions default **off** (`PW_CC`). Playback starts muted, so turning them on by default is
  worth deciding — raised, not decided.
- Landing preview: `video/preview/find-your-path.mp4` is already the first `<source>`; the demo
  clip covers it until that file exists, then swaps automatically.

**Captions workflow:** Premiere exports **SRT only** (no WebVTT option). Export SRT with
"include SRT styling" **OFF** → `python3 scripts/srt2vtt.py video/nodes/*.srt`. Premiere stays the
source of truth; never hand-edit a `.vtt` (the next run overwrites it).
- **Video transcripts** — the `welcome` node holds lorem-ipsum placeholder; other video nodes have
  no transcript text. Agreed plan: Option A (fill each node's `text:[…]` → existing Transcript
  modal) + Option C (short 2–4 bullet summaries on result pages/PDF, drafted from transcripts).
  Fill-in template: [`notes/video-transcripts-TODO.md`](notes/video-transcripts-TODO.md).
  ⚠ **Before filling these in:** transcript text sits inside JS quote marks, so an apostrophe
  ("I'm a teaching artist") breaks the page — blank screen, whole site down. Move transcripts to
  their own data file (like `data/programs.json`) first. Offered, not yet approved.

### Pending client review
- **PROVISIONAL region assignments** (`SCHOOL_REGION` in index.html) — school→region mappings
  inferred from campus location, NOT independently verified (carries an in-code "review before
  launch" flag). Confirm before launch.
- **"Stay in touch" button** — non-functional placeholder on result pages; email opt-in awaiting
  client decision on platform + placement before wiring.
- **UCLA Extension CTE in Teaching Artistry** — client asked to add to Teaching Artist + CTE lists
  (url: uclaextension.edu/…/course/artist-educator-explore-ucla); implemented then REVERTED,
  awaiting client answer on (a) region — Southern California vs Online — and (b) whether it
  duplicates the existing "University of California, Los Angeles" CTE entry.

### Online-availability marking
- **(client request):** research done for all 92 programs; NOT yet on the live site — awaiting
  client sign-off on the marker threshold. See
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
