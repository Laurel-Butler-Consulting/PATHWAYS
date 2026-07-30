# PATHWAYS — master build checklist

Single source of truth for remaining site-build work.

**How this stays current**
- Claude ticks items off and adds new ones as part of doing the work (Option 1: living file).
- For the mechanical items, run the auto-scan anytime to derive live status from the actual files
  (Option 2): `python3 scripts/build-scan.py`
- Lives in the repo, so it travels with the daily-folder copy. Soft items (client sign-offs, design
  calls) are tracked here by hand; the scan only covers things detectable in the files.

Legend: `[ ]` to do · `[x]` done · `[~]` in progress / partial

---

## 1. Video & transcript content — awaiting final content upload
Per-node detail: [`notes/video-upload-checklist.md`](video-upload-checklist.md) ·
transcript text template: [`notes/video-transcripts-TODO.md`](video-transcripts-TODO.md)

- [x] **Video-playback wiring built** in `index.html` (2026-07-27) — verified end to end against a
      stand-in clip: autoplay-muted, tap to pause, mute, CC, end-of-video → questions, replay, skip,
      transcript modal, and fallback to the still when a flagged clip is missing
- [x] **Gate the "CC" button on caption presence** — CC and mute now only render when the files exist
- [x] **Caption positioning** — captions are drawn by the site above the Skip/CC/mute row; the
      browser's own caption box sat underneath it and couldn't be moved
- [x] **SRT→VTT converter** (`scripts/srt2vtt.py`) — Premiere exports SRT only
- [x] Landing preview wired to swap in `video/preview/find-your-path.mp4` automatically when delivered
- [ ] 11 presenter videos recorded & final → `video/nodes/<node-key>.mp4`
- [ ] Landing "Find Your Path" preview video — final clip + poster (muted loop; no transcript)
- [ ] Poster stills finalized (placeholders currently in `images/video placeholder stills/`)
- [ ] Switch each node on as its clip lands (`v:1`, plus `cc:1` once its `.vtt` is beside it)
- [ ] Captions (`.srt` → `.vtt`) for all narrated videos
- [ ] Transcripts written for all 11 nodes (Option A) — replace `welcome` lorem-ipsum placeholder
      ⚠ **move transcripts to a data file first** — an apostrophe in the text blanks the whole page
- [ ] Result-page video summaries drafted (Option C) — 7 result pages, from the transcripts
- [ ] Decide: captions on by default? (`PW_CC` currently off; playback starts muted)

## 2. Pending client review
- [ ] **REVIEW: dagger footnotes removed (2026-07-30)** — the `†` marks and the "State-approved program.
      This link opens the school's general credential page rather than a discipline-specific one — confirm
      program specifics with the school" note were removed from all result pages to reduce visual noise.
      **22 programs still carry the `f` flag in `data/programs.json`**, so this is display-only and fully
      reversible. Decide before launch whether that caveat needs to reach users some other way — it warns
      people that a link may not land on the program they're looking for.
- [ ] PROVISIONAL region assignments (`SCHOOL_REGION`) — verify before launch
- [ ] **"Stay in touch" email opt-in — BUILT but NOT WIRED (2026-07-30). MUST NOT SHIP AS-IS.** The navy
      band at the foot of every result page accepts an address and silently discards it — no confirmation,
      no error, and it looks like it worked. Needs the client's platform (assume **Constant Contact**,
      pending their confirmation) before it can do anything. Two requirements to raise with them:
      (a) the confirmation must appear on our page, not a redirect to theirs — verify in their form
      settings, their own docs don't state it; (b) their embedded form's styling has to be overridden to
      match the band. Also still to design: success / failure / already-subscribed states, and the
      confirmation must be announced for screen readers, not just displayed.
- [ ] UCLA Extension CTE in Teaching Artistry — client to confirm region (Southern vs Online) + whether it
      duplicates the existing UCLA CTE entry; then re-add to Teaching Artist + CTE lists

## 3. Online-availability marking
- [ ] Client sign-off on marker threshold, then wire in (research done for all 92 programs)
      [`notes/online-availability-README.md`](online-availability-README.md) · `notes/online-availability-review.json`

## 4. Launch / general
- [ ] (add pre-launch items here — QA pass, cross-browser/device check, analytics, final content review, etc.)
- [ ] Play one real clip through in a normal browser — the preview pane suspends video, so
      continuous playback is the one thing never confirmed on a real file
- [ ] Delete unused `images/createca_logo_color.png` (48K; only the `_EDIT` version is referenced)?
- [ ] Wire the "Civil Cyber Arts" credit link — placeholder `href="#"` in two places (footer + result pages).
      Confirmed still unresolved in the 2026-07-30 code review; clicking either one jumps to the top of the page.
- [ ] **Welcome transcript is lorem ipsum** — the `welcome` node's `text:[…]` is placeholder Latin, and it's
      reachable from the first questionnaire screen via the Transcript button. Most user-visible of the
      placeholder items. See [`notes/video-transcripts-TODO.md`](video-transcripts-TODO.md) — and move the
      transcripts to a data file first (an apostrophe in the text blanks the whole page).

### From the 2026-07-27 code inspection — your call, none started
- [ ] **Base text size overrides browser settings** (`html{font-size:20px}`) — people who enlarge
      their default text get overridden. Fixing means re-checking every size sitewide.
- [ ] **Moving content can't be paused** — hero photos crossfade continuously with no stop control;
      neither hero nor quote carousel respects the OS "reduce motion" setting (only the scroll arrow
      does). Quote carousel does pause on hover and has arrows, so it's the milder case.
- [ ] Note for local previews: the site must be served over http (`python3 -m http.server 8765`),
      not opened by double-clicking — the program list can't load from a `file://` page.

Clean at that inspection: no dead code, no unused functions, every asset and link resolves, all 11
questionnaire screens and 7 result pages render, heading order correct, all images have alt text,
all buttons named, program data valid with every school region-mapped.

---

## Recently completed (this build cycle)
- [x] `escapeHTML()` for program-data injection
- [x] Landing landmark (`<main>`) + heading-order fix (h4 → h3)
- [x] Merged duplicated CSS link-arrow rule
- [x] Additional Resources section (collapsible subsections + print-expand)
- [x] Supplementary Authorization page copy update + italic note
- [x] Footer design credit (Civil Cyber Arts; placeholder link)
- [x] DPP section / subsection title styling
