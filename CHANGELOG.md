# Build history

A readable record of how this site was built, from the first version in February 2026 to launch on
17 August 2026.

**Why this file exists.** For most of the build, commit messages were not filled in — 57 commits say
only `Update index.html`, and others say `2`, `3` or `10x`. The changes themselves are all intact in
git; only the descriptions were missing. This file reconstructs them from the diffs so the history
can be read without opening every commit. Entries are grouped by day and dated by **commit date**,
which occasionally runs a day behind the work itself.

From 1 August the site sat behind a password gate while content was finished. It was opened to the
public on 16 August.

---

## August 2026 — content delivery, video, launch

### 16 August — launch preparation
- **Removed the pre-launch password gate and the search-engine block**, opening the site to the
  public and allowing it to be indexed. The other three pages keep their search block permanently.
- Rebuilt how captions break across lines. The site now measures the text and decides the breaks
  itself, because the CSS approach worked in Chrome but not in any browser on an iPhone, iPad or Mac.
- Added a "Make the window taller" prompt for desktop windows too short to fit the video controls —
  the counterpart to the existing sideways-phone prompt.
- Evened up the spacing on the sign-up confirmation page.
- Replaced four dead program links (CSU Stanislaus ×3, Focus 5, Studio Pathways) after checking all
  146 external links on the site for the first time.

### 14 August — sharing, printing, final copy
- **Each result page got its own web address** and a Copy Link button, so a result can be sent to
  someone or bookmarked.
- Made the printed page and saved PDF match the site's design rather than standing in for it, and
  stopped section headings printing alone at the foot of a page.
- The browser tab title now follows the pathway on result pages.
- Added the UCLA VAPAE CTE in Teaching Artistry program.
- Showed the CDEA credential checklist only on the Dance and Theatre pages.
- Shortened two landing-page testimonial quotes.

### 13 August — video framing and captions
- **Stopped iPads showing a second set of captions** behind the video controls. iPadOS switches
  subtitles on by itself for muted video; the site now switches them back.
- **Widened the desktop video by about 15%** and kept the word "SKIP" legible at every size.
- Kept captions clear of faces and controls inside the picture on short windows.
- Replaced the loading bar and spinner with a single gold disc that fills like a clock hand.

### 12 August — all clips live
- **The final four clips landed; all 11 questionnaire videos are now live.**
- Balanced caption line breaks so a cue no longer strands a word on its own line.
- Carried the mute setting from one video to the next.
- Added a brief hold at the start of each clip so people can orient before it plays, then replaced
  the poster hold with a navy loading screen.
- Re-split dense caption cues at phrase boundaries.
- Untracked internal notes from the public repository and removed the February archive folder.

### 10–11 August — presenters and controls
- Drew the speaker name strips, with a wipe between speakers on two-presenter clips.
- Switched on clips 1–7 and renamed the delivered files to match their node keys.
- Fixed the mute button pausing the video, and overlaps in the video control row.
- Added the "Turn your phone upright" prompt for phones held sideways.

### 8 August — first video
- **Wired up the first clip and the landing loop**, and reorganised the video folders into
  `clips/`, `stills/`, `captions/` and `transcripts/`.
- Applied the client's edits to the result-page summaries.

### 5–6 August — analytics, captions, regions
- **Installed Plausible analytics** and set up tracking for questionnaire steps and results.
- Added Spanish captions and the results-page summaries; added the favicon.
- Installed the client-approved V3 Spanish transcripts.
- Corrected four region assignments and removed the Statewide category.
- Fixed four defects found in a full code review.
- Kept every page except the front door out of search results, permanently.

### 1–4 August — domain, sign-up, privacy
- **Connected the custom domain** `artsedpathways.org`.
- **Moved fonts off Google and onto this site**, removing the last third-party dependency other
  than analytics.
- Renamed the cross-index to the **Program Index** and restyled it.
- **Wired up the email sign-up** via Buttondown and added the confirmation page.
- **Added the privacy policy page.**
- Added the four research PDFs linked from result pages.
- Installed client-approved Spanish transcripts and corrected an error in the CTE hours requirement.

---

## July 2026 — content moves out of the code

### 31 July
- **Created `data/content.en.json` and `data/transcripts.es.json`.** Interface and questionnaire
  copy moved out of `index.html` so it could be edited without touching code — the structure the
  site still uses.
- Built the transcript window.

### 30 July
- Added `scripts/srt2vtt.py`, converting Premiere's caption exports into the format the site needs.
- Wrote the video export specification.

### 24–25 July
- **Built the cross-index**, a filterable table of every program on the site — later renamed the
  Program Index.
- Started the build checklist and `scripts/build-scan.py`, which derives build status from the files.
- Completed the online-availability research covering all 92 programs.

### 8–21 July
- Added the landing-page testimonial headshots.
- Added a demonstration questionnaire preview video, standing in until the real clips arrived.

---

## June 2026 — the questionnaire

### 17 June — the rebuild that shaped the site
- **Rebuilt the questionnaire as a branching decision tree** and redesigned its screens around an
  autoplaying video with an end card. This is the structure the finished site is built on.
- **Created `data/programs.json`**, separating the program listings from the page.

### 18–19 June
- **Built the video player**: tap to pause, mute, captions, skip, replay, and cycling poster stills
  for clips that had not yet been delivered.

### 22–24 June
- Removed the placeholder styling the questionnaire had used before the player existed.
- Archived a snapshot of the February version.

### 3–5 June
- Fixed asset paths to lowercase and optimised the poster image.
- Added the hero slideshow, the footer, and stand-in headshots.

---

## February–May 2026 — first version

### 26 February
- **First version of the site**, a single static page of just under 400 lines.

### 21–28 May
- Image and asset work ahead of the June rebuild.
