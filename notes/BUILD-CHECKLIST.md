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

- [ ] Landing "Find Your Path" preview video — replace demo clip + final poster (muted loop; no transcript)
- [ ] 11 presenter videos recorded & final
- [ ] Poster stills finalized (placeholders currently in `images/video placeholder stills/`)
- [ ] Video-playback wiring built in `index.html` (personas currently render as stills only)
- [ ] Transcripts written for all 11 nodes (Option A) — replace `welcome` lorem-ipsum placeholder
- [ ] Result-page video summaries drafted (Option C) — 7 result pages, from the transcripts
- [ ] Captions (`.vtt`) added for all narrated videos
- [ ] Gate the "CC" button on caption presence (currently toggles nonexistent tracks)

## 2. Pending client review
- [ ] PROVISIONAL region assignments (`SCHOOL_REGION`) — verify before launch
- [ ] "Stay in touch" email opt-in — client to confirm platform + placement, then wire (button is a stub)
- [ ] UCLA Extension CTE in Teaching Artistry — client to confirm region (Southern vs Online) + whether it
      duplicates the existing UCLA CTE entry; then re-add to Teaching Artist + CTE lists

## 3. Online-availability marking
- [ ] Client sign-off on marker threshold, then wire in (research done for all 92 programs)
      [`notes/online-availability-README.md`](online-availability-README.md) · `notes/online-availability-review.json`

## 4. Launch / general
- [ ] (add pre-launch items here — QA pass, cross-browser/device check, analytics, final content review, etc.)

---

## Recently completed (this build cycle)
- [x] `escapeHTML()` for program-data injection
- [x] Landing landmark (`<main>`) + heading-order fix (h4 → h3)
- [x] Merged duplicated CSS link-arrow rule
- [x] Additional Resources section (collapsible subsections + print-expand)
- [x] Supplementary Authorization page copy update + italic note
- [x] Footer design credit (Civil Cyber Arts; placeholder link)
- [x] DPP section / subsection title styling
