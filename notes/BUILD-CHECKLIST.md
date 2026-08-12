# PATHWAYS — master build checklist

Single source of truth for remaining site-build work.

**How this stays current**
- Claude ticks items off and adds new ones as part of doing the work (Option 1: living file).
- For the mechanical items, run the auto-scan anytime to derive live status from the actual files
  (Option 2): `python3 scripts/build-scan.py`
- Lives in the repo, so it travels with the daily-folder copy. Soft items (client sign-offs, design
  calls) are tracked here by hand; the scan only covers things detectable in the files.

Legend: `[ ]` to do · `[x]` done · `[~]` in progress / partial

**Blocking order.** Final English copy → translation. Result addresses → useful analytics. Platform
choice → email wiring. Domain verified → domain connected. Everything → hosting transfer → launch.

---

## 0. Needed from the client — ask list
Everything below is blocked on one of these. Grouped by who has to act.

**Decisions**
- [x] **The domain — SETTLED 2026-08-01, off the client's list.** We bought `artsedpathways.org` on
      their behalf rather than wait on them. Live, verified and on HTTPS the same day. (§7)
- [x] ~~**Analytics: what do they want to know?**~~ — **ANSWERED AND BUILT 2026-08-05.** Plausible on
      the Starter plan, $9/mo; all six custom events and eight pathway goals live and verified. See
      the two Analytics entries below and §5.
- [x] **Spanish scope settled 2026-07-31: captions and transcripts only.** No interface translation,
      no `/es/` address, no language toggle. The site's own text stays English. (§6)
- [x] **Repository stays PUBLIC** (decided 2026-08-01). Who keeps write access after handover is
      still open — see §7 Phase A.
- [x] **Dagger caveat — CLOSED 2026-08-01: not needed.** The removal stands; the warning does not
      have to reach users another way. (§2)
- [x] ~~**Online-availability markers**~~ — **DECIDED 2026-08-06: NO markers on the result pages.**
      The delivery data stays where it is, on the Program Index, which is linked from every result
      page. Off the client's list. (§3)
- [~] **UCLA Extension CTE — mostly resolved by research 2026-08-03 (§2).** Not a duplicate; the URL
      on file is only an info session; the real pathway launches Fall 2026 and needs its URL from
      UCLA Extension. Nothing needed from the client except the pathway URL when it exists. A separate
      decision was needed from us on the UCLA name collision — made and built 2026-08-03 (§2).
- [x] **Captions on by default — YES, in English** (decided 2026-08-01). (§1)

**Accounts + access**
- [x] **GitHub organisation — DONE BY US 2026-08-01, off the client's list.** `Laurel-Butler-Consulting`,
      created and the site transferred into it, so the domain only ever had to be verified once. What
      remains is ours: turn on organisation-wide two-factor, and add a client Owner at handover (needs
      them to have a GitHub account). (§7)
- [x] **Registrar access — not needed from them.** The Porkbun account is ours; it moves to the client
      account-to-account at handover, with no downtime. (§7)
- [x] **Email capture — DONE 2026-08-03, off the client's list.** Moved from Constant Contact to
      Buttondown over the Google reCAPTCHA problem, wired and tested end to end with real addresses,
      and the privacy policy that was gating it is written and live. (§4, §8)
- [x] **Analytics — DONE 2026-08-05, off the client's list.** Plausible, installed in the `<head>` of
      all four pages (index, privacy, subscribed, program-index) and verified loading on each.
      **The client owns the account; we set it up and administer it for now**, so admin access is
      the only thing left to hand over — the account itself does not move. No cookies, no IP
      addresses stored, processed in the EU; already named in the privacy policy, which must be
      updated in step if the service is ever changed. It is the site's only outside dependency,
      a deliberate exception to the 2026-08-01 removal of Google Fonts.
      ⚠ Figures are meaningless until launch (2026-08-17): they count our own visits and every hit
      on the password gate, and ad-blockers hide a real share of traffic.
- [x] **Questionnaire tracking — DONE and VERIFIED END TO END 2026-08-05 on the live site.** Every
      goal fired and was seen in Plausible: the 6 custom events, all 8 pathway pageview goals
      including the `/result/*` overall rate, plus Plausible's own File Download and Outbound Link.
      Five of the seven pathway goals were exercised separately at the end, by sending their result
      addresses through the site's own reporting code — clicking through only ever reached Music and
      CTE Credential, so the rest would otherwise have been assumed rather than tested.
      Plan chosen: **Starter, $9/mo at the 10k-pageview tier**, single login, no team
      sharing. Custom properties and funnels are Business-only ($19) and were deliberately declined;
      per-step drop-out is read instead from the pages report, because each questionnaire step and
      result is now reported as its own address (`/q/…`, `/result/…`). Route-following — which path
      a group took, not just how many hit each step — is the one thing Starter cannot answer; that
      is the trigger to reconsider the plan. Moving up later loses nothing already collected.
      ⚠ Sizing: one completed questionnaire is roughly 6–12 pageviews, not 1. 10k/month is about
      1,000 completions. Check the tier once real traffic starts.
      Two things caught during verification, both fixed — worth knowing if this is ever extended:
      • The result page's "Restart Questionnaire" button called `pwStart()` directly, so it reported
        a fresh start and never a restart. Both restart controls now route through `pwRestart()`.
        Any NEW control that starts the questionnaire must pick the right one of the two.
      • A goal that fires locally but never appears is almost always a stale cached page, not a
        naming error. Hard-reload the live site before suspecting the dashboard.
      ⚠ Reporting to the client: Plausible calculates conversion rate against ALL site visitors, not
      against people who started the questionnaire, so the headline percentages look far higher than
      "share who finished". Pick one framing and stay with it (see step 4).
      Steps that were carried out in the Plausible dashboard, kept for the record and for re-setup:
      1. Subscribe to Starter.
      2. Website Settings → General → Site Installation: switch on **Outbound links** and
         **File downloads**. Both create their own goals; nothing to type, no site change needed.
      3. Website Settings → Goals → Add Goal → Custom Event, six times, spelled EXACTLY:
         `Questionnaire Started` · `Questionnaire Restarted` · `Questionnaire Exited` ·
         `Result Page Saved` · `Transcript Opened` · `Video Skipped`
         (A mismatched name means the event arrives and is displayed nowhere.)
         ⚠ `Result Page Saved` was called `PDF Downloaded` until 2026-08-05. Renamed because
         Plausible's own automatic `File Download` goal covers the four research reports in the
         resources block, and the two names side by side read as the same thing. Ours means a
         visitor saved their OWN results; Plausible's means they downloaded a report.
      4. Goals → Add Goal → **Pageview** (not Custom Event), 8 times, to get conversion rates per
         pathway. Use the Display Name field so the client reads a label, not a path:
         `/result/*` → "Reached any result" (overall completion rate, the headline number) ·
         `/result/music` → "Result: Music" · `/result/theatre` · `/result/dance` ·
         `/result/visual-art` · `/result/teaching-artist` · `/result/cte-credential` ·
         `/result/supplementary-authorization`
         ⚠ Plausible calculates conversion rate against ALL site visitors, not against people who
         started the questionnaire. 100 visit → 40 start → 10 reach Music shows as 10%, not 25%.
         For the second figure, filter the dashboard to the `Questionnaire Started` goal first.
         Agree with the client WHICH of the two goes in reports and stay consistent — the same
         month reported both ways looks like a contradiction.
      5. Verify against the Realtime view while clicking the live questionnaire.
      6. Set up the weekly/monthly email summary for the client, who owns the account but does not
         hold the login.
      The 11 steps and 7 result pages need NO goals to be COUNTED — they arrive as pages, and the
      pageview goals in step 4 exist only to add a conversion rate on top. Email sign-ups need no
      goal either: `/subscribed/` is a real page and appears on its own.

**Content the client must supply**
- [x] ~~**Review the Spanish transcripts**~~ — **DONE. Superseded twice: client-approved V2 installed
      2026-08-04, then a new translator version (V3) installed 2026-08-06. V3 is current.**
- [x] ~~**Answer the 12 transcript queries**~~ — **CLOSED 2026-08-06 by the arrival of V3.** The
      client worked with her translator on new Spanish rather than answering query by query, and V3
      landed 2026-08-06. Of the two meaning items raised, one (the real-world/classroom reversal)
      came back unchanged and was corrected here; the other (how CTE is translated) is now used
      consistently, which settles it in practice. The rework this created — all 11 caption files,
      `data/transcripts.es.json` and `video/transcripts/esp/` — is **done** (§6).
- [x] ~~**CTE experience: paid vs unpaid**~~ — **RESOLVED 2026-08-06: "work experience" everywhere,
      both languages.** The Commission counts three years "full-time or part-time, paid or unpaid" at
      1000 clock hours a year, verified by employers (CL-888), so the word *paid* was turning away
      people who qualify.
      **No re-record was needed** — the requirement is never spoken. The narration says "Here's the
      key requirement:" and stops; an on-screen graphic carries the rest, which is why the English
      captions have a 7-second gap there. Only the graphic said *paid*, and it has been re-cut to read
      WORK EXPERIENCE. Timings unchanged, so all 11 English caption exports remain valid.
      Corrected to match: the English transcript (file and `data/content.en.json`), the Spanish
      transcript, and the Spanish subtitle cue.
      ⚠ **One place still says "paid or unpaid" and must stay** — the rule statement in the CTE
      summary. There the phrase does the opposite job: it tells people unpaid work counts.
- [x] ~~Confirmation of the PROVISIONAL region assignments~~ — **RESOLVED 2026-08-05, off the
      client's list.** Every flagged row settled, including the one that genuinely needed her call
      (Santa Barbara counts as Southern, not Central). (§2)
- [x] ~~**A privacy policy**, or a decision about who writes one~~ — **WRITTEN AND CLIENT-APPROVED
      2026-08-06.** Live at `/privacy/`, linked from all four footers. Off their list. (§4, §8)
- [x] **Email confirmation page — CLIENT-APPROVED 2026-08-06.** `/subscribed/`, the page a new
      subscriber lands on after clicking the confirmation link. Off their list. (§4)
- [ ] **Approval** of the media below once delivered

**Media — our purview, client approves** *(not a client deliverable; do not put on their ask list)*
- [~] 11 presenter videos, final — **1 in (`welcome`), 10 to come** (§1)
- [x] ~~Landing "Find Your Path" preview clip + poster~~ — **IN AND VERIFIED 2026-08-08** (§1)
- [x] ~~Final poster stills~~ — **CLIENT-APPROVED 2026-08-06.** The eight `vp_*.jpg` in use are the
      final ones. ℹ They still sit in a folder called `images/video placeholder stills/`; the name is
      now wrong but nothing depends on it. (§1)
- [x] ~~Captions — Premiere SRT export → `scripts/srt2vtt.py`~~ — **ALL 11 CONVERTED, both languages,
      22 files, confirmed 2026-08-10.** Converted is not switched on: a file only reaches a visitor
      once its clip lands and the node carries `cc:`. Today that is `welcome` alone. (§1)
- **CTE Intro is the ONE file where English and Spanish cue counts differ on purpose — 22 vs 25.
  Do not "fix" it.** From 18.6s to 25.9s the video shows a text graphic spelling out the 1,000-hour
  requirement, over a new Ricky voice-over, so the English captions leave that stretch empty: an
  English viewer reads it off the graphic. A Spanish viewer cannot — the graphic is in English — so
  the Spanish track carries three extra cues (11–13) covering that sentence. Asymmetric, deliberate,
  and the only way the key requirement reaches a Spanish reader at all. If the graphic is ever
  re-cut with Spanish text, these three become redundant and should go.
- [x] ~~**FOR THE EDITOR: spell it "theatre", not "theater", in the caption source.**~~ — **ALL THREE
      FILES CLEAN, confirmed 2026-08-06.** The site was made uniform on 2026-08-05 — every word a
      visitor reads says *theatre* — and the caption exports now match: `09_theatre_260805.srt`
      (6 instances, Eric's video), plus `03_discipline_260805.srt` and `07_suppauth_260805.srt`, both
      re-exported on 08-05. No caption file in either language contains "theater".
      ⚠ **This can still drift back.** Premiere is the source of truth and the next export overwrites
      anything corrected by hand here, so it has to stay right in Premiere. Re-check after any
      re-export. Spanish captions are unaffected (they say *teatro*), and the corrected files kept
      their timings exactly, so the Spanish sidecars still line up cue for cue.
      NOT to be changed: the internal name `mTheater` in index.html and data/content.en.json (a code
      label, never shown, and the two files must keep matching), and the San Diego State link in
      data/programs.json, whose web address contains "theater".
- [x] English transcripts for all 11 videos — written and final 2026-07-31 (§1)
- [x] Spanish transcripts — **client-approved V3 installed 2026-08-06**, 11 files, superseding V2 (§6)
- [x] **"Civil Cyber Arts" credit link — DONE 2026-08-03.** Points at an alias address, deliberately
      disposable. Detail in §9.

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
- [x] **Playback-speed control — BUILT 2026-07-31 (client request).** Button paired with mute on the
      right, showing the current rate; tap opens a list above it. Speeds **0.75x / 1x (default) /
      1.25x / 1.5x** — the client asked for 1x–2x, narrowed here to 1.5x max with 0.75x added for
      people who need it slower. Range lives in `PW_SPEEDS` in index.html; adding a value is a
      one-line edit. Choice persists between videos. Pitch is preserved, so voices stay natural.
      Only renders over a real clip, never over a placeholder still.
      ⚠ Above ~1.5x captions change too fast to read comfortably — relevant if the client expects
      speed and captions to work together.
- [x] **Skip button label shortened to "Skip" (2026-07-31)** to make room for the speed control.
      The spoken name stays "Skip video" for screen-reader users. Row slack measured at 137px
      before and after, so the new control costs nothing in crowding.
- [x] **Landing-preview overlay for client preview (2026-07-31)** —
      `video/preview-overlays/landing-preview-overlay.svg`. Shows the "Find Your Path" loop as it
      appears in place: blue frame, gold hairline, vignette, and the Take the Questionnaire button.
      Canvas 1148×1988 with the video area as a transparent hole at x=34, y=34, 1080×1920 — drop a
      1080×1920 clip in at 100% and it registers exactly. Button geometry verified against the live
      page at zero difference. Keep-clear: the button covers y 1199–1365 (61–69% of clip height),
      and the vignette darkens the centre.
- [x] **Player-chrome overlay templates for client preview (2026-07-31)** —
      `video/preview-overlays/*.svg`, 1080×1920 with a transparent video area, for compositing over
      rough cuts in Premiere. Two states: playing, and playing with a two-line caption. Geometry
      measured against the live player at phone width and confirmed within 2px. Keep-clear: bottom
      156px, or bottom 335px when captions are on. **Regenerated after the Skip/speed changes above —
      re-export if you composited against the earlier versions.**
- [~] **11 presenter videos recorded & final → `video/clips/<node-key>.mp4`. 1 of 11 in: `welcome`,
      switched on and verified 2026-08-08.** Folders were reorganised the same day —
      `video/clips` · `video/stills` · `video/captions/eng|esp` · `video/transcripts/eng|esp` — and
      the site was repointed at them. **Site filenames are node keys; Premiere's dated export names
      stay on the source files only.** Full layout and naming rules:
      [`notes/video-export-spec.md`](video-export-spec.md).
      Encoding settled the same day: **3 Mbps target / 5 max**, down from 4/6, holding the repository
      near 265 MB instead of 345 MB. `welcome` came in at 3.12 Mbps, 21.5 MB, 54.93s.
      ⚠ **Commit only the cut you intend to keep.** Git stores every version of a video whole and
      forever; deleting one later frees nothing, and undoing it means rewriting history and breaking
      every dated build folder.
      ℹ **`welcome` has been through three exports (08-08, then twice on 08-10/11) and all three are
      in history.** Reframed to clear the caption line, then re-exported once more because the first
      attempt went out with the safe-zone overlay still enabled on a track. Every version came in at
      exactly 54.930s / 1317 frames / 23.976fps, which is why the captions and the speaker cut times
      survived each one untouched — check that before assuming the next re-export is as harmless.
      Poster re-exported to match, 2026-08-11.
- [x] **Desktop video column is NARROWER than a phone's — BOTH CONSEQUENCES CLOSED 2026-08-08**, on
      the first real clip. The cause is unchanged and worth keeping: in the landscape card the video is
      sized by HEIGHT (`--vidH: min(70vh, 800px, 100dvh - 280px)`) and the width follows from 9:16, so
      a shorter browser window makes a NARROWER video. A phone gives the full 375; a laptop window
      gives less: 700px tall → 236 wide · 760 → 270 · 800 → 293 · 900 → 349.
      • **Controls overlapped — FIXED.** Worse than the 21px estimated here: measured at 50px on a
        1024×700 window, with Skip running into the CC button. Fixed with two compact tiers in the
        landscape rules — under 820px of window height the buttons drop to 34px and Skip shows its
        icon alone; under 660px they go to 30px. Nothing is removed, every control stays operable,
        and Skip keeps its "Skip video" name for screen readers even where the label is hidden.
        Verified with no overlap at 1440×900 (349px column), 1366×768 (275), 1024×700 (236) and
        1024×600 (180), and unchanged on a phone at 375.
        ⚠ **Floor: below ~570px of window height it crowds again** (measured: 3px overlap at
        1024×560, where the column is 158px). Judged not worth a third tier — at that size the video
        is smaller than a playing card and the layout has bigger problems.
        ⚠ The 820/660 thresholds are derived from the `280` allowance in `--vidH`. Change one and
        recheck the other; there is a comment beside the CSS saying so.
      • **Captions wrapping — NOT A PROBLEM, withdrawn.** The prediction was 4 lines at 236px, 86px
        tall. Measured against the real welcome captions: they stay 2 lines, 45px, about 11% of the
        video. Premiere's exports carry their own line breaks and keep cues short, so nothing
        reflows. Assumes the other ten export the same way — recheck if any cue looks long.
      • **The width itself — ALSO ADDRESSED, later the same day.** Two changes, both measured:
        the "Pathways Questionnaire" label was dropped in landscape (it was 59px of card furniture)
        and the reserve in `--vidH` came down with it, 280 → 225; then the height cap went 70vh → 78vh.
        Result: 1024×700 → 267px (was 236) · 1366×768 → 305 (275) · **1440×900 → 380 (349)** ·
        1512×950 → 408 (374) · 1920×1080 → 450 (425). A phone gets 375, so **an ordinary laptop now
        beats a phone**, where before it needed a ~950px-tall window. The crossover is now ~890px.
        ⚠ Short windows gained from the label removal only — 78vh never binds below ~1025px, where
        the reserve governs instead. That is why raising vh alone would have looked like it did
        nothing on a laptop. The three limits and which one governs when are documented in the CSS.
        ⚠ **REVERSED 2026-08-10 on request — the label is back in landscape**, and the reserve went
        with it, 225 → 284. The trade-off recorded here (a card with no header naming it) is what the
        client chose not to accept. Cost, measured: 1440×900 → 347px wide, down from 380, so a laptop
        is under a phone's 375 again. Current widths are in the CSS comment beside `--vidH`.
        ⚠ **Restored at the WRONG SIZE and fixed 2026-08-11.** It went back as a flat `.62rem`, which
        renders 12.4px — less than half what this label had always been. Its original size is FLUID,
        3.14% of the card's inner width, so it holds its proportion from a 1024px window to 1920:
        22.6px at 1024×700, 26.4px at 1440×900, 29.6px at 1920×1080. Weight 600, tracking .18em.
        Header height and video width are unchanged by the fix, so the 284 reserve still holds.
        ℹ If this label is ever moved or restyled again, take the rule out of git history rather than
        re-typing one — that is exactly how the size was lost.
        ℹ The claim that the label "survives only on tablets in portrait" was wrong even on 08-08 —
        it was hidden globally, and nothing re-showed it anywhere. It now shows in landscape only.
      • **Control ORDER made consistent 2026-08-08.** Landscape had pinned Skip left and moved CC to
        the right cluster, so CC and Skip swapped ends between phone and desktop, with no recorded
        reason. Now one arrangement everywhere: **CC → Skip → Speed → Mute**, Skip centred.
        ⚠ In the compact tiers, an anchor must only ever set the side it belongs to — giving CC a
        `right` or Skip a `left` is exactly what reversed the order before.
      • **CC button restyled 2026-08-08 (client request).** When a language is showing and there is
        more than one to choose from, it is a split pill: "CC" navy-on-gold, the live language
        gold-on-navy, halves meeting down the middle. The border is dropped in that state only — a
        button has one border and the gold one was drawing a ring around the navy half. Off and
        single-language nodes keep the plain button, unchanged.
- [~] **Clips 01-07 DELIVERED AND SWITCHED ON 2026-08-11 — 7 of 11 live.** `welcome` · `taVsCred` ·
      `discipline` · `lifeTA` · `cteIntro` · `cteVideo` · `suppAuth`. Each carries `v:1`,
      `cc:['en','es']` and its own poster. Remaining: `mMusic` · `mTheater` · `mDance` · `mArt`.
      **Checked on delivery, all seven:** 1080×1920 · faststart · 3.12–3.15 Mbps, on the 3/5 spec ·
      durations 46.1s to 100.0s, each agreeing with the caption files built against it · both caption
      tracks parse with the expected cue counts (380 English / 383 Spanish across all 11; `cteIntro`
      22 vs 25 as designed) · CC, mute and speed render on every node · speaker strips name the right
      people, `discipline` correctly Ricky then Laurel.
      🔴 **FILENAME TRAP, FOUND AND FIXED ON DELIVERY — this one would have passed every local test
      and broken the live site.** Five clips arrived lowercase (`cteintro.mp4`, `lifeta.mp4`,
      `suppauth.mp4`, `tavscred.mp4`) and one under its Premiere name (`ctepath.mp4`). **macOS disks
      are case-INSENSITIVE and GitHub Pages is case-SENSITIVE**, so `cteIntro.mp4` resolves locally to
      `cteintro.mp4` and 404s in production — where the player would quietly fall back to the
      placeholder still. Renamed to the node keys, along with their stills. Done BEFORE committing,
      which matters: git stores each video whole and forever, so renaming afterwards would have kept
      both copies for good.
      ⚠ **The node key is ONE name doing THREE jobs** — clip, poster and both caption files are all
      looked up from it. The caption files were already node-key named, which is why the clips had to
      move rather than the captions.
      ⚠ **THE LAST FOUR MUST BE EXPORTED AS `mMusic.mp4` · `mTheater.mp4` · `mDance.mp4` ·
      `mArt.mp4`** — not `music.mp4`, not `08_music_260806.mp4`. Note **`mTheater` is the American
      spelling on purpose**: it is an internal key that no visitor ever sees, and index.html and
      `data/content.en.json` must keep matching. Everything a visitor reads still says *theatre*.
      ⚠ **Not yet checked on the delivered footage, and only checkable by eye:** whether every chin
      clears the y1090 caption line. `04_lifeta_02` was one of the five framings that failed the
      2026-08-10 measurement and `lifeTA` is now live; `07_suppauth_01` and `04_lifeta_03` were both
      close. The preview pane cannot seek reliably, so this needs a real browser.
      ⚠ **`discipline`'s speaker cut (23.209s) is still unconfirmed against the export** — it came off
      the Premiere timeline, the reading that was ~20% out on `welcome`. The clip is 46.129s, so the
      cut lands almost exactly halfway, which is consistent with what was supplied.
      **Size, measured 2026-08-11:** the seven clips are **184 MB**; the four still to come are 274.7s
      of footage between them, so about **107 MB more at 3.13 Mbps — roughly 291 MB of clips in all**,
      against the 265 MB this was estimated at. Comfortably inside GitHub Pages' 1 GB published-site
      limit. `.git` is already 158 MB, a third of it the three `welcome` exports.
      ✔ **All six are final as delivered — nothing is waiting on a re-cut.** `cteIntro` was briefly
      held back on the assumption its 1000-hour graphic still needed re-framing; it did not. The
      graphic was corrected in Premiere before the 20:58 export, so the delivered file already
      carries the fix (see the closed red item below). Commit all six.
- [x] **"Turn your phone upright" prompt — BUILT 2026-08-11 (approved the same day).** Found while
      answering how common a sub-590px window really is: the answer is **a phone held sideways**, and
      the control row was the least of it.
      **What landscape actually did on a phone, measured:** at 844×390 (an iPhone 14/15 on its side)
      the picture came out **60×106px** — the card reserves 284px of window height for its header,
      questions and footer, leaving 106px — with the control row needing 166px in a 60px column and
      113px of it cut off by the picture edge. A smaller phone (667×375) falls below the 720px
      landscape rules instead and gets a 667×168 letterbox: nothing clipped, but a 9:16 video cropped
      to a slot. Neither is watchable. **This predates the 08-11 row work; it was never right.**
      **Built:** on a touchscreen in landscape under 500px tall, the questionnaire card is replaced by
      a navy panel — turning-phone icon, "Turn your phone upright", one line of explanation, and a
      **Continue anyway** button. Copy lives in `data/content.en.json` → `ui.rotateTitle` /
      `rotateBody` / `rotateContinue`, per the rule that questionnaire text is not in index.html.
      ⚠ **"Continue anyway" is a WCAG 1.3.4 (Orientation, AA) requirement, not a nicety.** Locking
      content to one orientation fails that rule: a mounted device, or rotation locked for someone's
      own reasons, must not become a dead end. Pressing it sets `.rot-ok` for the rest of the visit,
      so the reader is asked once rather than on all eleven nodes; a later visit asks again.
      ⚠ **`(pointer:coarse)` is what keeps it off desktop.** A desktop window under 500px tall is rare
      but real, and "turn your phone upright" would be nonsense there. Do not simplify the query.
      **Verified** with the shipped rule on an emulated touchscreen at 740×360: message shown and card
      hidden; Continue anyway restores the card and moves focus to Skip (the pressed button is now
      hidden, and focus left on a hidden control strands a keyboard user); the choice carries to the
      next node. Hidden as intended in phone portrait, on tablet, and on desktop at every size; result
      pages and the landing page carry none of it. No console errors.
      ℹ The 12px of page scroll at 844×390 is pre-existing and identical with the message or the card —
      measured both ways, not introduced here.
      ℹ First attempt put white type straight on the ice page background, because hiding the card also
      hides the navy it was written for. The panel now wears the card's own navy, radius and shadow.
- [x] 🔴 **Speed button overlapped Skip — FIXED 2026-08-11 by rebuilding the control row.** Reported
      as "at certain resolutions the speed control overlaps the skip button when activated".
      **Cause:** "1.25x" is 20px wider than "1x". The button was pinned to the right, so a longer
      label grew LEFTWARD into Skip, which was pinned to the exact centre. Nothing was too big — the
      centre pinning meant one gap absorbed every extra pixel while the other sat unused. Measured
      before the fix, at 0.75x/1.25x: **9.2px of overlap at 1440×860 · 9.7px at 1024×700 · 7.3px at
      1024×640**, and the sizes that passed did so by as little as 2.1px (1440×900). Phones were
      always clear. Because the speed choice is remembered between videos and between visits, one
      person picking 1.25x once had a broken row from then on.
      **Fix: the four controls are now ONE FLEX ROW of three cells** (CC · Skip · speed+mute)
      instead of four independently pinned items. The side cells share the spare space equally, so
      Skip holds the true centre line while there is room and slides off it only as far as it must.
      Two controls can no longer overlap at any width — this was the third overlap bug in this row.
      The speed button also reserves the width of its widest label, so it no longer changes size
      when a speed is picked and the row stops shifting under the reader's finger.
      **After, measured at ten sizes** — 1920×1080 · 1440×900 · 1440×860 · 1366×768 · 1024×700 ·
      1024×640 · 1024×600 · 768×1024 · 375×812 · 375×667 — **no overlap at any of the four speeds,
      nothing clipped, gaps 8px (5px on the smallest tier)**. Skip stays exactly centred at 1920,
      1366, both phones and tablet; it gives way by 6.6px at 1440×900 and 16.9px at 1440×860.
      Also confirmed unchanged: both pop-up menus open inside the picture 6px above their button,
      a tap in the gaps between controls still pauses the video, the mute fix below still holds, and
      a missing clip still leaves Skip alone and dead centre.
      ✔ **Tab and screen-reader order now match what is on screen** (CC → Skip → speed → mute). The
      old DOM order was Skip, mute, speed, CC — a consequence of the pinning, and nobody's choice.
      ⚠ **Two traps for anyone editing this row.**
      • **Never put `min-width:0` on `.qv-ctlcell`.** It lets a cell shrink past its own buttons and
        reproduces the exact overlap the row exists to prevent — done by accident on 08-11 and
        measured at 9.9px before it was caught. A comment in the CSS says so.
      • **Never restore `position:absolute` on a control.** Placement comes from the cell now.
      ⚠ **New floor, measured: below about 590px of window height the row is wider than the video**
      and the picture's edge clips it — 5.8px at 1024×580. The smallest tier was tightened (gap,
      edge inset, CC half-padding, Skip padding, speed reserve) to buy ~37px and hold 1024×600
      exactly. This is still a large improvement on the old behaviour, which at 1024×580 overlapped
      by 8px at 1x and 24px at 1.25x. The old note put this floor at ~570px; 590 is the real number.
- [x] 🔴 **Mute button also paused the video — FOUND AND FIXED 2026-08-11.** Reported as "pressing
      mute usually just pauses the video, sometimes it works". It was a real fault, not a small
      icon, and it had been live on `welcome` since 08-08.
      **Cause:** pressing mute swaps the icon for the other one. The video's own tap-to-pause check
      then asks "did this press come from a control?" — but the icon it came from had just been
      replaced, so the check matched nothing and treated it as a press on the picture. One press =
      mute AND pause; two presses = back to muted with the video stopped, which is why it read as
      "nothing happens but the video pauses".
      **Measured on the live player before the fix** (40×40 button): **19% of its face landed on the
      icon and broke**, dead centre where people aim · 62% worked · the remaining 19% was the corners
      of the square box falling outside the round pill and hitting the video. So roughly **4 presses
      in 10 moved the video.** On a short laptop window (1024×700, button 37px) the broken centre
      grew to 24%, the icon staying 17px at every size.
      **Two fixes, both in the CSS beside `.qv-mute`, both commented there:** the icon no longer
      takes presses, and a square hit area sits behind the round button. After: **0% hits the icon,
      94% reaches the button**, and the last 6% is a one-pixel line along two edges — a rounding
      artefact of the button's fractional position, not a dead zone. Holds at every control size,
      down to the smallest tier (31px button at 1024×640: 0% / 91.5%).
      Verified with the real handlers: pressing mute now changes only the sound and makes no
      play/pause call at all, at the centre and in the corners, while a press on the picture still
      pauses as before.
      ⚠ **Mute is the only control that rewrites its own contents mid-press**, which is why it alone
      was affected — CC, Skip and Speed were all checked and pass. The single-language CC button is
      safe for a different reason: its label is plain text, so the press lands on the button itself.
      **Any NEW control that redraws itself when pressed needs the same `pointer-events:none`.**
- [x] **Speaker name/title strips — BUILT 2026-08-10.** Names and job titles live in
      `data/content.en.json` → `speakers`; each node's `sp:[…]` in index.html says WHO and, on a
      two-presenter clip, WHEN. Verbatim copy and the node mapping stay in
      [`notes/speaker-names-and-titles.txt`](speaker-names-and-titles.txt).
      **Not an overlay — page furniture**, which is the decision that took the longest to land. On a
      phone it is a navy band ABOVE the picture; on desktop it fills the column beside the video.
      Nothing sits on the presenter, so the caption line and the control row never move, and the crop
      question below stopped competing with it.
      **The four decisions, all answered 2026-08-10:**
      • **Name + first title on the phone; both titles on desktop.** The phone band is 67px either
        way; a second line would have cost another ~20px of picture on the smallest screen.
      • **The strip switches as the presenters alternate** (`welcome`: four turns).
      • **It holds for the whole clip.** Fading was only ever needed to get it off the picture.
      • **On desktop the right column is SHARED** — name while the clip runs, questions when it ends.
        Nobody can answer during playback any more; accepted because Skip jumps straight there.
      **Measured:** band 67px · phone 375×812 video 667 → 643 (2.4%) · phone 375×667 video 565 → 498
      (11.9%, the full band, because that screen has no slack) · desktop unchanged at 347×616 on a
      1440×900 window, the column being space that was empty anyway · name movement between speakers
      0px at both sizes.
      **How the name is anchored:** every speaker on a node is rendered and stacked in ONE grid cell,
      so the box is as tall as the tallest and the name sits at a fixed height — only the lines under
      the gold rule change. Hidden slots use `visibility`, which keeps their height and keeps them out
      of the screen-reader path, so one name is announced, not all of them.
      **Only over a real clip.** A node showing placeholder stills renders no strip — a two-presenter
      node shows both stills at once, so there is nobody to name — and a flagged-but-missing clip has
      its strips removed with the rest of the clip-only controls, which hands the desktop column back
      to the questions on its own. Verified by simulating an absent file.
      ✔ **`discipline` cut times supplied 2026-08-11 and in place.** One cut, and the order is the
      REVERSE of `welcome`: **Ricky from zero, Laurel from 23:05** (frame 5 of second 23 on a
      23.976 timebase) = `at:23.209`. The clip itself has not landed, so the strip stays hidden
      until it does — the map cannot be watched through until then, and the timing came off the
      Premiere timeline rather than a finished export, which is the reading that went wrong on
      `welcome`. **Check it against the export on the day the clip goes in.**
      **TRANSITION — a left-to-right WIPE, built 2026-08-11.** A crossfade was tried in principle and
      rejected: the objection is that both names are semi-transparent through the middle of it. The
      wipe has one travelling edge, with the incoming block uncovered at exactly the rate the outgoing
      one is clipped away, so the type is solid on both sides. 190ms — it happens four times inside
      55 seconds, and anything slower starts asking for attention.
      It covers the WHOLE block, not just the name, because the two presenters have a different number
      of title lines and wiping the name alone would leave the lines beneath it to pop.
      ⚠ **Under `prefers-reduced-motion` it is a straight cut, by design** — same rule the hero photos
      and the quote carousel follow. This is not a bug, and it is the first thing to check if someone
      reports the wipe "not working": iOS Reduce Motion was exactly that on 08-11.
      ⚠ Cleanup runs on a timer, not on the animation finishing, so a throttled background tab still
      lands in the right state rather than sticking half-wiped. A change arriving mid-wipe completes
      the one in flight first.
      ℹ Visible artefact, accepted: while the edge crosses, the tail of the taller block's last line
      hangs to the right of it with nothing beneath. Inherent to a wipe; gone in 190ms.
      ⚠ **Read cut times off the FINISHED EXPORT, not the Premiere timeline.** `welcome`'s sequence
      displayed 30-per-second timecode on a 23.976 timebase, so every number read off it was ~20%
      short — the last cut read as 43:26 on a clip that is 54.93s long. Re-read on 08-11 with the
      display format set to 23.976 (17:10 · 34:18 · 50:09) and the two readings agree within one
      frame. Current values: 17.417 · 34.751 · 50.375.
      ⚠ **Do not verify a speaker map against a fast-forwarded video.** At 8× the painted frame trails
      `currentTime` by 1–2 seconds, which made a correct map look wrong for half an hour on 08-11.
      **Why it is drawn in the site rather than burned into the video** — unchanged, and still the
      reason: on a small phone the bottom 423px of a 1080×1920 export is cropped away before the
      player's own furniture takes another 335px, so a burned-in strip would have to sit above y≈1163
      to survive, 60% up the frame. Drawing it also means a misspelled name is a text edit rather than
      a re-cut, and the job title can be translated.
- [x] **Video crop position — SETTLED 2026-08-10: it STAYS at `object-position:50% 0`.** The proposal
      was `50% 35%`, to lift the presenter out of the empty sky above their head. Killed by real
      footage: 24 test frames covering every framing in all 11 clips put the top of the head anywhere
      from y58 to y212, because the clips cut between wide shots and tight close-ups. One crop rule
      governs every clip, so a 35% crop — 170px off the top on a small phone — would slice into the
      tightest shot in seven of the eleven. Even a gentle 20% clips three of them.
      **What `50% 0` means in practice, and it is the reassuring half:** the picture is pinned to the
      TOP of the player, so nothing is EVER cut from the top. Headroom cannot clip a head, whatever
      the framing. Everything lost comes off the bottom, and how much depends on the screen: 68px of
      1920 on a 375×812 phone, 486px on a 375×667 one, nothing at all on a laptop.
      ⚠ The consequence is that **headroom consistency is now an aesthetic question, not a technical
      one** — presenters sitting at different heights reads as less considered when you move between
      videos, but nothing breaks. The binding rule moved to the BOTTOM of the frame: see the caption
      line item below.
      ℹ The old figure of `35%` came from `vp_laurel.jpg`, a PLACEHOLDER still, and was wrong the
      moment real footage existed. Superseded, not merely revised.
- [~] **THE CAPTION LINE IS THE FRAMING RULE — keep every chin above y1090.** Established 2026-08-10
      from 24 test frames, one per distinct framing across all 11 clips. Client's instruction:
      captions over a presenter's face are not acceptable.
      Measured on the live player, in source pixels of a 1080×1920 export:
      • **y1090** — where the caption box starts on the smallest phone (375×667) with a two-line cue.
        THE binding number. Everything above it is clear on every screen.
      • **y1273** — the Skip/CC/speed/mute row on that phone, with captions off.
      • **y1434** — where the picture ends on that phone. y1852 on a 375×812 phone. A laptop shows all 1920.
      **Overlay to check against: [`video/preview-overlays/master-safe-zones.svg`](../video/preview-overlays/master-safe-zones.svg)**
      — 1080×1920, drop at 100%, no repositioning. Premiere will not import SVG; open it in Photoshop
      and save a PNG. It supersedes the earlier `headroom-check.svg`, which was built around a head
      band that the crop decision above made advisory.
      **Five framings failed when measured (08-10), all in clips not yet delivered:**
      `01_welcome_02` · `01_welcome_04` · `04_lifeta_02` · `08_music_02` · `09_theatre_01` — the line
      fell on a lip, chin or jaw. **`welcome` has since been re-cut and passes**; the other three clips
      still carry it. Five more sat within a hand's breadth of the line and are worth a second look:
      `01_welcome_05` · `04_lifeta_03` · `07_suppauth_01` · `09_theatre_02` · `10_dance_02`.
      ⚠ Judged from one frame per framing. A shot that reads clear can still drop below the line when
      the presenter shifts, so check against the overlay across the whole take, not a single frame.
      ⚠ The test stills themselves were deleted after measuring — 13MB of one-off frames, deliberately
      never committed. Re-export from Premiere if this needs redoing.
- [x] ~~🔴 **CTE requirement graphic sits too low**~~ — **RE-FRAMED AND RE-EXPORTED 2026-08-11, and
      the corrected export is the one now in the repo.** Re-framed in Premiere against
      `master-safe-zones.svg` so the text block ends above y1090, then exported at 20:58 as part of
      the 01-07 delivery — so the fix arrived with the first delivery rather than after it.
      Kept as the record of what was wrong: the full-frame "1000 HOURS WORK EXPERIENCE PER YEAR FOR
      AT LEAST 3 YEARS" card used to run from y370 to y1308. On a small phone the control row starts
      at y1273, so the bottom of "3 YEARS" sat behind the buttons even with captions off — and for a
      Spanish viewer the caption box covered the bottom 218px for a full 7 seconds, because the
      Spanish track carries three cues across the exact window (18.643–25.900s) where the English
      track is deliberately silent. Those three cues are the ONLY route a Spanish reader has to the
      requirement, and they were landing on top of the thing they exist to replace.
      ✔ **Timings did NOT change** — the export is still 47.464s and the caption grid is untouched,
      so the three Spanish cues still sit over the graphic and no rebuild is needed. Verified on the
      delivered file, along with 1080×1920, faststart and 3.12 Mbps.
      ⚠ **The y1090 clearance itself was confirmed in Premiere against the overlay, not re-measured
      from the export.** Nothing here can measure it: the preview pane will not seek, so no frame
      from inside the graphic window can be read. Worth one look on a real phone during the QA pass,
      in Spanish, where the caption box is doing the most covering.
      ℹ The y1308 figure was measured on 2026-08-10 from an earlier cut. It was quoted against the
      delivered file on 08-11 and that was wrong — **the number on record described a superseded
      export.** Re-measure before repeating a figure like this against a new delivery.
- [x] **Landing "Find Your Path" preview video — DONE 2026-08-08.** `video/clips/questprev.mp4` with
      `video/stills/questprev.jpg`. On spec throughout: 1080×1920, 1.52 Mbps, 1.85 MB, no audio
      track, faststart, and first and last frame pixel-identical so the loop seam is invisible.
      ⚠ **It has no fallback.** The stand-in demo clip was removed in the reorganisation, so if
      either file is missing or misnamed the landing page shows an empty frame — the first thing
      anyone sees. `build-scan.py` checks both files exist.
- [x] ~~Poster stills finalized~~ — **CLIENT-APPROVED 2026-08-06**, the eight already in use. The
      folder is still named `images/video placeholder stills/`, which now misdescribes its contents.
- [~] Switch each node on as its clip lands — `v:1`, `cc:['en','es']`, and `poster:` pointing at its
      still in `video/stills/`. **1 of 11 done: `welcome`, 2026-08-08.** Verified end to end: clip,
      poster and both caption files serve, playback runs, English captions default on, the Español
      switch works and is marked as Spanish for screen readers, and Skip / CC / speed / mute all
      render without overlapping at phone, laptop and short-window sizes.
      ℹ Posters are **chosen frames, not frame 1** — the client picks the most flattering frame.
      Don't report the difference as a defect.
      ℹ **`welcome.jpg` was re-exported 2026-08-11 to match the re-framed clip.** It had been left
      alone deliberately when the clip was first reframed on 08-10 — raised then and declined — and
      that decision was reversed once the framing changed again. Poster and clip are now in step.
- [x] Captions (`.srt` → `.vtt`) for all narrated videos — **ALL 11 CONVERTED AND NODE-KEY NAMED, in
      BOTH languages: 22 files, confirmed in the folders 2026-08-10.** They sit in
      `video/captions/eng/` and `video/captions/esp/` beside the dated Premiere SRT exports
      (`…_260806.srt`), which stay as the source. Cue counts match language for language on all 11
      nodes — 380 English cues, 383 Spanish — the only difference being `cteIntro` (22 vs 25), which
      is deliberate and documented in §0.
      ⚠ **Converted is not switched on.** A caption file only reaches a visitor when its node carries
      `cc:['en','es']` and its clip is present — today that is `welcome` alone. The other ten are
      staged and waiting on their clips, not on any further caption work.
      ⚠ If a re-export changes any TIMECODE, the Spanish sidecar was built on the old timings and must
      be rebuilt — check before assuming it still lines up.
- [x] **Questionnaire + results copy moved out of `index.html` into `data/content.en.json`
      (2026-07-31)** — transcripts, node labels, questions, answer buttons, result titles, resource
      headings, the Supplementary Authorization page, and all button/label text. `index.html` keeps
      only structure: routing keys, image paths, link URLs, video flags. Apostrophes are now harmless.
- [x] ~~**Extract the landing page copy (~480 words) into the content file**~~ — **STRUCK FROM THE
      LIST 2026-08-01. Not doing it.** The landing page is plain HTML that paints immediately; the
      questionnaire and results copy could move because those screens are drawn after the content
      file loads anyway. Moving the landing copy would make the first page anyone sees wait on that
      file — a blank moment on the busiest page, or a fallback to build. Real trade-off, not a tidy-up.
      Nothing depends on it since the 2026-07-31 Spanish scope cut. Landing copy stays inline; there
      is no apostrophe risk there. Reopen only if the landing page ever needs translating.
- [x] ~~`08_music_eng.txt` contradicts itself~~ — fixed 2026-07-31. The "three ways to get there"
      claim was removed from paragraph 1, so the transcript now promises only the single route it
      actually describes. Spanish draft and both data files updated to match.
- [x] **English transcripts written and FINAL for all 11 nodes (2026-07-31)** — live in
      `video/transcripts/eng/`, 2,342 words total (lifeTA and music edited 2026-07-31). Note: these are standalone `.txt` files, so
      `build-scan.py` (which only reads `index.html`) still reports them missing — see §9.
- [x] **English transcripts live on the site (2026-07-31)** — all 11 in the Transcript modal; the
      `welcome` lorem ipsum is gone. Apostrophes verified safe (11 render in the welcome text alone).
- [x] **Result-page summaries — CLIENT EDITS RECEIVED AND APPLIED 2026-08-08. FINAL.** The
      2026-08-01 plan had the client writing these; that changed — we drafted all seven from the video
      transcripts, checked against the Commission's own leaflets (CL-560C, CL-603, CL-629, CL-888 and
      coded correspondence 21-05). Full text and the audit trail:
      [`notes/results-page-summaries-for-client.txt`](results-page-summaries-for-client.txt).
      Five headings per pathway — Description, Requirements, Qualifications, Process, Notes.
      Three queries went to the client with the draft; **all three answered 2026-08-06**: the US
      Constitution course and the formal programme recommendation cut from the four discipline pages
      ("stick to what the videos cover"), the dance video's 32-unit figure confirmed accurate and
      added, and the CTE "paid" wording resolved in favour of "work experience".
      **Her own edits arrived 2026-08-08** as tracked changes in a Word copy of the 08-05 draft, so
      five of her deletions had already been made on 08-06 and needed no action. Six were new and all
      six are in: three wording changes on Supplementary Authorization plus a new sentence on
      pre-2022 English and PE credential holders (her copy, the one line in the summaries not
      traceable to the videos or the leaflets — confirmed by her 08-07); the CTE PROCESS entry cut
      back to its first sentence, on her note that process should cover only how to get in; the
      "Programs run statewide…" sentence cut from Dance; and "may add" ➜ "may include" on Visual Art.
      **The `placeholder` flag and its note are gone from `data/content.en.json`** — the scan now
      reads "7 of 7 pages have copy". ⚠ **Nothing guards this copy any more.** The on-page warning
      band came off on 08-01 and the flag was the last safeguard; further edits change the live text
      with no check in front of them.
      ⚠ **The CTE page no longer states that the preliminary credential expires after three years.**
      Putting it in NOTES was proposed and **decided against 2026-08-08.** Deliberate, not an
      oversight — don't add it back without asking.
- [x] **Container for those summaries BUILT 2026-08-01**, so the copy is a paste, not a build. Sits
      between the pathway title and the programme list, inside `#resultDoc` so it carries into the
      printed page and the saved PDF. White card, gold left rule, heading "In Short" (editable).
      Copy lives in `data/content.en.json` under `summaries`.
      **Real copy went in 2026-08-05 and the client's edits on 2026-08-08** (see the entry above).
      The `"placeholder"` flag and its note were deleted the same day, so the block is now ordinary
      finished copy. ⚠ The on-page red warning band was **removed on request 2026-08-01**, so with the
      flag gone there is nothing left — on the page, in the printed version or in the scan — marking
      this copy as anything other than final. That is correct today; it also means any FUTURE change
      to these bullets ships unguarded.
      A page with no bullets renders no block at all, so a partial delivery just omits those pages.
      Verified on all 7 result pages, both states, phone and desktop, and with the section absent.
- [x] **Captions default ON, in English — DECIDED AND BUILT 2026-08-01.** Playback starts muted, so
      captions carry the video for anyone who doesn't unmute. A visitor who turns them off keeps them
      off, and any choice made before this change is respected either way. Verified on a first visit,
      on a bilingual node and an English-only node, and for returning visitors in both prior states.

## 2. Pending client review
- [x] **Dagger footnotes stay removed — CONFIRMED 2026-08-01, no replacement needed.** The `†` marks
      and the "confirm program specifics with the school" note came off all result pages on 2026-07-30
      to reduce visual noise, and that is now the final answer.
      The 22 `f` flags stay in `data/programs.json`, unused — harmless, and they make the caveat one
      display change away if it is ever wanted back. Nothing to do here before launch.
- [x] ~~PROVISIONAL region assignments (`SCHOOL_REGION`)~~ — **ALL FLAGGED ROWS RESOLVED 2026-08-05**,
      and the in-code "review before launch" flag is gone. The rule that had never been written down is
      now recorded above `SCHOOL_REGION` in index.html: **region is where the ORGANISATION is, never
      how the programme is delivered.** The empty fourth region ("Online", displayed "Statewide") was
      removed.
      ⚠ Two residual caveats, neither a task: the other **84 rows were assigned the same way and never
      checked one by one** — nothing is known to be wrong, and they are mostly self-evident (CSU Chico
      → Northern). And **Focus 5 → Southern is a snapshot, not a fact**: it is a Washington DC
      organisation whose only California offering was one 2025 intensive hosted at UCSB. A touring
      organisation could hold the next one elsewhere.
- [x] ~~**UCLA CTE entries**~~ — **CLOSED HERE 2026-08-05. Moved to §10 Post-launch, off the client's
      ask list.** She agreed to hold it until UCLA Extension publishes the pathway page (Autumn 2026).
      Everything needed to add it is recorded in §10; the detail below is the working that got there.
      Note the name-collision problem referenced further down was FIXED on 2026-08-03 by splitting
      `UCLA Extension` (CTE) from `University of California, Los Angeles` (Music).
      <details><summary>Original entry, kept as the record</summary>

      Client answered 2026-07-30: keep BOTH, not a duplicate. Link text to read
      exactly: `University of California, Los Angeles` (existing) and `UCLA VAPAE CTE in Teaching Artistry`
      (new). Still blocked on three things before it can be built:
      1. **Region for the new entry** — the original open question (Southern California vs Online) was
         never answered. It needs its own `SCHOOL_REGION` mapping or it falls into "Unsorted" on the
         live page. The existing UCLA entry is mapped to Southern California.
      2. **Which lists** — the original client request was Teaching Artist *and* CTE. "Keep both CTE
         options" only confirms the CTE list. Confirm whether the new entry also goes in Teaching Artist.
      3. **The URL, and a naming discrepancy.** The URL on file is `uclaextension.edu/…/course/
         artist-educator-explore-ucla` (truncated in notes — need the full address). But the client's
         label says **VAPAE**, which is UCLA's Visual and Performing Arts Education Program in the
         Graduate School of Education (`centerx.gseis.ucla.edu`) — a different unit from UCLA Extension.
         The existing CTE entry already points at UCLA Extension. Either the course is run by Extension
         in partnership with VAPAE, or the label and the link don't match. Confirm before publishing —
         a mislabelled link sends people to the wrong part of a very large university.

      **RESEARCHED 2026-08-03 — three of the unknowns above are now answered, and the URL on file
      should NOT be published.**
      - **That URL is a free information session, not a programme.** It resolves to "From Artist to
        Educator: Explore UCLA Extension's New CTE Teaching Artistry Credential" (EDUC 769) — a
        complimentary, non-credit xOpen session, currently listed as *"Not available this quarter."*
        Publishing it puts a recruitment event, and a dormant one, alongside real credential
        programmes.
        `uclaextension.edu/education/k-12-california-teacher-credentialing-authorizations/course/artist-educator-educ-769`
      - **The programme it advertises is real but not launched: a CTE Teaching Artistry credential
        pathway, launching Fall 2026.** No dedicated page for it is findable yet — searches return
        only the info session and the general CTE specialization. ➜ **ASK UCLA EXTENSION FOR THE
        PATHWAY URL ONCE IT IS LIVE, then add.** Launch is weeks away as of this note.
      - **Not a duplicate — confirmed from the pages themselves.** The existing CTE entry links UCLA
        Extension's *general* CTE credential: eight courses (instructional strategies, technology,
        curriculum design, inclusion, portfolio/practicum, health education) with nothing
        arts-specific. The Teaching Artistry pathway is a separate, arts-specific route.
      - **VAPAE is not a candidate for this site.** `vapae.arts.ucla.edu` is an 18-unit arts education
        **minor for current UCLA undergraduates**, plus community arts programmes and internships.
        Not a credential, not a route for working artists, wrong audience. The client's "VAPAE" label
        appears to be a mix-up with UCLA Extension, which is where the Teaching Artistry pathway sits.
      - **Region was blocked on a data-model problem — the UCLA name collision, since fixed (§2).**

      </details>

- [x] ~~🔴 **UCLA name collision**~~ — **FIXED 2026-08-03 (commit `496013c`), confirmed in the files
      2026-08-06.** `University of California, Los Angeles` had covered TWO offerings — **CTE** (UCLA
      Extension, delivered online) and **Music** (CenterX, a full-time in-person credential inside an
      undergraduate degree). Region and delivery are keyed by school NAME, so each field was right for
      one and wrong for the other, and changing either would have broken the one it fixed.
      **Resolved by splitting the name**, as planned: `UCLA Extension` now carries the CTE entry and
      `University of California, Los Angeles` the Music entry. Both appear in `data/programs.json`,
      `SCHOOL_REGION` and the Program Index.
      **One thing went differently from the plan above, and correctly.** The plan gave UCLA Extension
      `r: Online`. It is mapped to **Southern California** instead, because the 2026-08-05 region work
      established the rule that region is WHERE THE ORGANISATION IS, never how a programme is
      delivered — and UCLA Extension's four campuses are all in Los Angeles. Delivery does its own
      work in the Program Index, where an online-deliverable programme answers to every region filter.
      The "Online" region no longer exists.
      Consequences, as predicted: the Program Index gained a row (90 ➜ 91) and the CTE result pages
      now read "UCLA Extension". It also gives the Teaching Artistry pathway a correct home when it
      launches (§10), since that is also UCLA Extension.

## 3. Online-availability marking — SETTLED 2026-08-06
- [x] **DECIDED: the markers stay on the Program Index and do NOT go on the result pages.**
      The research was finished long ago — all 91 schools classified into four delivery categories
      (In-person only 35 · Online only 30 · Hybrid 18 · In person or online 8), live in
      `program-index/index.html` on the `d:` field. What was open was only *where it should appear*.
      **Why this is the right answer, not just the cheap one:** the Program Index already carries it
      and is linked from every result page, and the largest category is the least informative to
      label — tagging 35 of 91 entries "in-person only" would add a lot of noise to say the ordinary
      thing. The result pages stay clean.
- [x] ~~🔴 **The cross-index link publishes the online-availability data ahead of sign-off**~~ —
      **CLOSED by the same decision.** The link in `resourcesHTML()` was flagged because it exposed
      this research before the client had agreed to any of it. She has now agreed where it lives, so
      the row stays and the ⚠ comment beside it in index.html is spent.
      ⚠ Second-order item still live: the Program Index carries its own `noindex`. Decide whether
      that stays once the main site is meant to be found by search (§9).
      Background on how the research was done: [`notes/online-availability-README.md`](online-availability-README.md)
      — note its own header warns it is a superseded snapshot; the live data is the Index.

## 4. Email capture — Buttondown  *(was Constant Contact — replaced 2026-08-03)*
- [x] **WIRED AND TESTED END TO END 2026-08-03.** Multiple real addresses submitted, confirmation
      emails received, confirmation-link redirect verified. No longer a launch blocker.
- [x] **Platform changed: Constant Contact ➜ Buttondown.** Built against Constant Contact first, then
      removed. Their widget pulls in Google reCAPTCHA, which loaded for EVERY visitor from the moment
      the homepage opened, and cannot be disabled from the site side — its pass/fail token is part of
      the submission, so stripping it makes sign-ups fail silently. Unacceptable given the client's
      position that data privacy is the deciding factor.
- [x] **Route: our own form, posted straight to Buttondown.** No embed widget, no third-party script
      anywhere on the site. Their endpoint returns permissive cross-origin headers, so the submission
      is made in our own code and the visitor stays on their results page — no redirect, no iframe.
- [x] Post-submission behaviour: success message on our own page, form replaced so nobody submits
      twice. Confirmation link lands on `/subscribed/`, our page, not Buttondown's archive.
- [x] States built: sending, invalid address, failure (address kept), success.
- [x] Confirmation **announced** to screen readers — the status line is a live region.
- [x] Honeypot field catches bots before anything leaves the browser. No captcha, by design.
- [x] **Privacy policy page** — built 2026-08-03 at `/privacy/`, linked from all four footers. See §8.
- [x] ~~⚠ **Buttondown settings**~~ — **BOTH CONFIRMED 2026-08-06.** Double opt-in is ON, matching the
      success copy that tells people to check their inbox, and "Embed fingerprinting" is OFF.
- [x] ~~⚠ **Deletion requests need an owner**~~ — **CLOSED 2026-08-06, client's call: not a concern.**
      Recorded for the record, since the underlying facts have not changed: the privacy policy promises
      deletion on request, and unsubscribing does NOT delete — Buttondown keeps the record so a later
      import cannot re-add the person. If a request ever arrives at `info@createca.org`, someone needs
      Buttondown access to action it.

## 5. Analytics — DONE 2026-08-05
**Settled and built. Plausible, Starter plan at $9/mo, installed on all four pages and verified goal
by goal against the live site. The full record — every goal name, the six dashboard setup steps, the
two bugs found during verification, and the reporting caveat about how conversion rates are
calculated — is in §0 under "Analytics" and "Questionnaire tracking". Read that, not this section.**

Nothing here is outstanding. The rest is kept as the reasoning that led to the choice, in case the
tool is ever reconsidered.

<details><summary>How the decision was made, kept as the record</summary>

⚠ **The deciding factor was custom events, not privacy.** All the credible options are equally
private. But the whole site is one page with one address — every questionnaire screen and every
result renders without the address changing. A tool that only counts page visits would report one
visit per person and nothing else. To learn completion rate, drop-off, or which pathway anyone
reached, the site has to send its own signals, which the tool has to support. That ruled out the
free options.

| Tool | Cost | Custom events | Notes |
|---|---|---|---|
| **Plausible** *(chosen)* | from ~$9/mo | Yes | Open source, EU-hosted, cookie-free, small script; script can be served from our own domain, which reduces exposure (§8) |
| Fathom | from ~$15/mo | Yes | Cookie-free, EU data isolation, long retention |
| GoatCounter | Free | Limited | Open source, admirably minimal; thin event support and effectively a one-person project — sustainability risk for a client site |
| Cloudflare Web Analytics | Free | Very limited | Fine for basic traffic counts; not enough for questionnaire data |

Plausible was the cheapest tool that could answer the client's likely questions. No cookies means
**no consent banner**, so nobody meets a popup before they meet the site. It is the site's only
outside dependency — a deliberate exception to the 2026-08-01 removal of Google Fonts (§8).

</details>

## 6. Spanish language — CAPTIONS AND TRANSCRIPTS ONLY
**SCOPE CUT 2026-07-31, agreed with the client.** For the time being the only Spanish on the site is
**video closed captioning and video transcripts**. The interface stays English throughout — landing
page, questionnaire, result pages, resources, footer.

**What this removes from the plan** (keep the reasoning here; the decision may be revisited):
- ~~~1,100 words of interface copy for the client to translate~~ — off their list entirely.
- ~~A Spanish address (`/es/`) or an on-page language toggle~~ — not needed. One site, English chrome.
- ~~Extracting the landing-page copy as a Spanish prerequisite~~ — no longer blocking anything. It
  survives only as optional tidy-up (§1), not as a dependency.
- ~~Translating region names, setting per-page `lang`, a second set of result pages~~ — all moot.

**What remains, in order:**
1. ~~Client reviews / edits the 11 Spanish transcripts~~ — **DONE. V3 installed 2026-08-06**,
   superseding V2 (which had superseded the drafts). See the V3 record below.
2. ~~Build the Spanish subtitle files from the approved transcripts~~ — **DONE 2026-08-06.** All 11
   built and rebuilt against V3. Timecodes untouched, cue counts matching the English exactly.
3. **Move the files into place and switch the nodes on — the only step left, and it waits on the
   clips.** The built files are STAGED, not deployed: they live in `video/captions/esp/` under dated
   names (`05_cteintro_260805.vtt`), while the player reads `video/nodes/<node-key>.es.vtt` beside
   `<node-key>.mp4`. So each one gets copied and renamed to its node key as its clip lands, and the
   node's `cc:` flag set. Nothing is switched on today: no node carries `v:1` or `cc:`, by design.

**Spanish subtitles — BUILT 2026-08-06. Method below, kept for reference and for the next language.**

The audio is English only, so the Spanish files are **subtitles** (a translation for readers), not
captions (a transcription for deaf/HoH viewers). Use that word with the client; nothing in the code
or the filenames changes.

**Do not use Premiere's caption translation.** All of Premiere's caption tools start from the audio.
The audio is English, so its auto-translate produces *its own* Spanish, not the client's approved
wording — which means proofreading a machine translation against the approved text, line by line,
eleven times. There is no "fit this Spanish text to this English audio" function, because the words
don't match the sound.

**Do this instead — reuse the English timings.** The English SRT already holds every timecode, and
the approved Spanish says the same things in the same order. So: keep the timecodes exactly, swap the
English words in each cue for the matching Spanish. No re-timing, no listening to audio.

Agreed 2026-08-04 that **Claude does this pass**: hand over `<key>.srt`, get back `<key>.es.srt` with
identical timecodes and the approved Spanish distributed across the cues. Then `scripts/srt2vtt.py`
as usual → `<key>.es.vtt`, and the CC button becomes the Off/English/Español menu on its own.

⚠ **Reading speed is the real complication, and it is now measured.** The "Spanish runs 20–25%
longer" figure written here on 2026-08-04 was an estimate and turned out to be wrong — measured
against the actual files, V3 is within a couple of percent of V2 and most nodes are the same length.
But the density problem is real, because the timings come from English speech: **102 of the 380
Spanish cues run above the usual 21-characters-per-second reading guideline.** The worst is
`02_tavscred` cue 6 — 50 characters in 1.09 seconds, 46 c/s, more than double.
Line lengths are all fine: nothing over 42 characters, nothing over two lines.
This cannot be judged properly until there is footage to read them against. **Take a pass over the
densest dozen once the clips are in.** Fix by moving the split point between neighbouring cues, which
shifts words without touching a timecode; merge two short adjacent cues only as a fallback. Do
**not** trim the Spanish — it is approved copy, and shortening it means going back to the client.

⚠ **Caption text is NOT the transcript text.** The captions deliberately drop the English-term glosses
the transcripts carry — "(California Subject Examinations for Teachers…)", "(Single Subject
Credential)", "(transcript evaluation)". Unreadable at subtitle speed, fine in a transcript read at
the reader's own pace. Keep that rule for any future rebuild; a verbatim paste from the transcript
will reintroduce them.

Manual alternatives if this ever needs doing without Claude: Subtitle Edit (free) or Aegisub load the
English timings and let you type the translation cue by cue. Same job, by hand.

✔ **No longer blocked on the videos** — this section said it was, which was out of date. The English
caption exports are in `video/captions/eng/`, all 11, and the Spanish sidecars were built against
them. `video/nodes/` is still empty, but that only gates step 3 above, not the subtitle work itself.

**Design decided 2026-07-31:**
- [x] **Transcript modal EN/ES switch — BUILT 2026-07-31.** Two-way toggle; sat under the modal
      heading until the heading was removed 2026-08-08, and now shares one row with the close button.
      Stacking the two languages was rejected. The choice is remembered and carries from one video to
      the next. Spanish text is marked as Spanish so screen readers pronounce it correctly.
      Spanish comes from `data/transcripts.es.json`, regenerated from `video/transcripts/esp/`.
      Degrades to English with no switch shown if a node has no Spanish or the file is missing.
      ✔ **The Spanish on the site is the client-approved V3** (installed 2026-08-06), so the old
      "must not go live before review" flag is cleared. The V2 wording queries were closed by V3's
      arrival; the corrections applied to V3 are logged in
      `notes/transcript-queries-for-client.txt`. Nothing here blocks launch.
- [x] **CC control three-way: off / English / Español — BUILT 2026-08-01.** Resolved as a small menu,
      not a cycling button, matching the playback-speed control beside it. The button shows what is
      showing — `CC` when off, `CC EN` / `CC ES` when on — so the language is legible without opening
      the menu. **Nodes with only one caption language keep the plain on/off button, unchanged**, so
      the English-only behaviour verified on 2026-07-27 is untouched. Opening either menu closes the
      other; both close on Escape or a click outside; using them does not pause the video.
- [x] **Per-node caption flags — BUILT 2026-08-01.** `cc:` now lists which languages have landed:
      `cc:['en']` or `cc:['en','es']`. A node never offers a language whose file isn't there. English
      stays at `<key>.vtt`; every other language is `<key>.<lang>.vtt`, so Spanish is `welcome.es.vtt`
      beside `welcome.mp4` — export the Premiere sidecar as `welcome.es.srt` and `scripts/srt2vtt.py`
      needs no change. Legacy `cc:1` still means English-only.
      The reader's choice persists between videos. If it's a language a given node doesn't have, that
      node falls back to its first language rather than showing nothing — and the choice is remembered,
      so it returns on the next node that does have it. Same rule as the Transcript modal.
      Caption line is marked with its language for screen readers.
- [x] ⚠ ~~**One thing to confirm on Aug 4, with real files:** switch language while the video is
      paused~~ — **REPRODUCED AND FIXED 2026-08-02.** It did come up blank. A caption track only just
      switched on has no active cue yet; the browser fills that in on its next cue update, which
      while paused never arrives — so the line stayed empty until playback resumed. Two extra
      repaints after the switch fix it, and cost nothing while the video is playing.
      Verified with a real video element and two caption tracks, paused: before the fix the line was
      empty immediately after the switch; after it, the new language appears. Worth one more look on
      Aug 4 against the real `.vtt` files, but this is no longer an open question.
- [ ] *Deferred, client's call, not a concern now:* signposting Spanish captions to a non-English
      reader inside an English interface; whether the printed PDF carries a transcript and in which
      language (it carries neither today).

**Spanish transcripts — CLIENT-APPROVED V3 INSTALLED 2026-08-06**
The client's translator supplied a NEW translation (one document, 2026-08-06) which **replaced V2
entirely**, exactly as V2 had replaced the drafts. The folder now holds `01_welcome_esp_V3.txt` …
`11_visualart_esp_V3.txt`; the V2 files and the delivered document were deleted, and
`data/transcripts.es.json` was rebuilt. Every file was diffed against the delivered document to
confirm only the intended corrections differ.

Corrections applied to V3, all recorded in `notes/transcript-queries-for-client.txt`:
- **10 mechanical.** The systematic one: "sala" is feminine, but it carried a masculine article five
  times across three videos and was never once right. Plus one agreement error, one plural, a missing
  accent, two double spaces.
- **Two meaning fixes.** (1) The real-world/classroom reversal, raised with the client during the V2
  review and unchanged in V3, so corrected rather than queried again. (2) 🔴 **V3 dropped the CTE
  time requirement** — it said "1000 hours of work experience" where the English, the graphic and the
  Commission all say **per year for at least 3 years**. V2's wording restored. This lands on the three
  extra Spanish cues that exist because the requirement is an English-only graphic, so it was the one
  place a Spanish viewer had no other route to it.
- **⚠ Five errors corrected in V2 came back in V3** — "a lugares educativas", "y asi puede enseñar",
  "las Autorización Suplementarias", "todos estudiantes tienen", "lo mas antes". The new Spanish
  appears to have been written from the original document rather than the corrected V2 files. All
  five fixed again and flagged for the translator. **If a V4 ever arrives, expect the same and check
  for it first.**
- **A dozen further items were raised and deliberately left as the translator wrote them**, including
  "Bienvenidos" (masculine plural in an otherwise feminine text), "entrenamiento" for teacher
  training, and "de todo de California". Listed in the queries file so it is clear they were seen
  rather than missed.

⚠ **The old "V2 is client-approved, do not change it" caution no longer applies to V2** — those files
are gone. V3 is the source of truth for both the transcripts and the subtitles.

Eight mechanical errors in the approved Spanish (agreement, a missing ñ, missing accents, a
duplicated word) were corrected in both the files and the site — listed with before/after in
`notes/transcript-queries-for-client.txt` for the client's records. Everything judged a style or
register call was left untouched and put to the client as a query instead.

The three house-style decisions below came from the *draft*. The approved V2 makes its own choices,
so these now read as a record of what was proposed, not as open questions — except where noted in the
queries file:

- [x] **Form of address: `tú`** (familiar), not `usted`. V3 uses `tú` throughout. Settled.
- [x] **Credentialing terms: English name + Spanish gloss on first use** — Supplementary
      Authorization, CTC, CSET, Single/Multiple Subject Credential, CTE, Prop 28, subject matter
      competency, student teaching, transcript evaluation. V3 does this. Rationale, still worth
      keeping: these are the names on the CTC's own forms and website, which are English-only.
      Translating them outright sends people searching for something that doesn't exist under that
      name. ⚠ **The captions deliberately DROP these glosses** — unreadable at subtitle speed. That
      asymmetry between transcript and caption is intentional; don't "fix" it.
- [x] **Grammatical gender: feminine where neutral phrasing isn't possible** (client instruction,
      2026-07-31). V3 is feminine throughout, with two lapses left as the translator wrote them —
      "Bienvenidos" in the opening line and "arte educador" in CTE Intro — both raised with the client
      and consciously declined (see the queries file). Neutral wording is used where it reads
      naturally. Some organisations prefer `educador/a` throughout; this one does not.
- [x] ~~Client review of the 11 Spanish transcripts~~ — done; V3 installed 2026-08-06
- [x] ~~Second subtitle file per video from the approved Spanish~~ — **BUILT 2026-08-06**, all 11, on
      the English SRT timings as planned; not re-timed. Staged in `video/captions/esp/`; renaming them
      to `<node-key>.es.vtt` in `video/nodes/` is part of the clip drop, not this task.
- [x] ~~Mark the Spanish text so screen readers pronounce it as Spanish~~ — **DONE, both surfaces.**
      The transcript body carries `lang="es"`, and the caption layer's language attribute is set and
      cleared as the reader switches. Confirmed in the code 2026-08-06. The rest of the site is
      English, so nothing else needs it.

**Superseded by the 2026-07-31 scope cut** — kept for the record, in case the client revisits:
- ~~Do not start translating the interface copy until the English copy is final~~ — no interface
  translation is happening.
- ~~Prerequisite: extract the landing-page copy from `index.html`~~ — the questionnaire and results
  half was done 2026-07-31 anyway (for the transcripts); the landing page half is no longer required
  by anything. It stays as optional tidy-up in §1.
- ~~Decide the shape: `/es/` addresses or an on-page toggle~~ — neither; the site stays English.
- ~~Region names translate~~ / ~~per-page `lang`~~ / ~~every copy change made twice, forever~~ — moot.

## 7. Hosting — GitHub organisation + custom domain
**SETTLED 2026-08-01.** New root domain, bought by us on the client's behalf to avoid waiting on them:
**`artsedpathways.org`**, registered at **Porkbun** 15:53 UTC 2026-08-01. Registrar account is ours;
it moves to the client's Porkbun account at handover (account-to-account push, no downtime — verify
the DNS records and HTTPS straight after). Registrar-to-registrar moves are locked for 60 days,
i.e. until roughly 2026-09-30.

Org: **`Laurel-Butler-Consulting`** · repo: `Laurel-Butler-Consulting/PATHWAYS` ·
Pages: `laurel-butler-consulting.github.io/PATHWAYS`

**Phase A — DONE 2026-08-01**
- [x] GitHub **organisation** created (`Laurel-Butler-Consulting`)
- [x] Repository transferred; Pages confirmed live and serving the current build under the new owner
- [x] Local clone repointed at the new remote — verified reachable, matching HEAD
- [ ] **POST-LAUNCH:** two-factor authentication required org-wide. Deferred 2026-08-06 — belongs with
      the handover, not the launch.
- [ ] **POST-LAUNCH:** add the client as a second Owner — needs them to have a GitHub account. Always
      intended for handover rather than launch; confirmed 2026-08-06. Org contact email stays ours for
      now, deliberately: an address nobody reads is a liability while the client is hard to reach.

**Phases B, C and D — ALL DONE 2026-08-01.** Domain verified at organisation level, repository moved,
domain connected, HTTPS enforced. Confirmed 2026-08-06 from the files themselves: `CNAME` in the repo
root reads `artsedpathways.org`, and the remote is `Laurel-Butler-Consulting/PATHWAYS`.

- [x] **Phase B — domain verified first, deliberately before connecting it.** Challenge TXT record
      added at the registrar (`_github-pages-challenge-<ORG>`) and verified.
      **Why the order mattered:** verification means only that organisation's repositories can publish
      to the domain. Skip it, and if the site is ever deleted, disabled or downgraded while DNS still
      points at GitHub, someone else can claim the address and publish on the client's domain.
      ⚠ **Standing rule: no wildcard DNS (`*.artsedpathways.org`).** It reintroduces takeover risk
      even after verification. Applies to anyone touching the DNS later, including the client.
- [x] **Phase C — repository transferred**, Pages confirmed building under the new owner, local clone
      repointed. This duplicated Phase A and should never have been a separate phase.
      Note: `CLAUDE.md` and `.claude/` are untracked and did not transfer. The daily-folder process is
      personal to this build and doesn't need to survive handover.
- [x] **Phase D — domain connected**, `CNAME` written into the repo, DNS propagated, **Enforce HTTPS**
      ticked. For reference if the DNS is ever rebuilt: root domain takes four A records —
      `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`; a subdomain would
      take one CNAME to `<org>.github.io`.
      ⚠ The site is live on the domain but **gated** — the pre-launch password and `noindex` are both
      still in place (§9). Don't share the address until those come off on launch day.

Docs: [custom domain](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site) ·
[verification](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/verifying-your-custom-domain-for-github-pages) ·
[HTTPS](https://docs.github.com/en/pages/getting-started-with-github-pages/securing-your-github-pages-site-with-https)

### Optional, previously discussed — shareable per-pathway links
- [ ] Not built, not committed to. Would give each result its own address so it can be bookmarked,
      shared and found by search — and would make analytics (§5) work without custom events, which is
      the strongest argument for it. Two shapes scoped: routing inside the page (~20 lines, but touches
      the delicate back-button logic) or one standalone page rendering any result (safer, but the
      styling and layout code must be shared out of `index.html` first — same prerequisite as §6).
      **SHELVED UNTIL AFTER LAUNCH (decided 2026-08-01).** Not a launch blocker, and the safer of the
      two shapes needs styling and layout shared out of `index.html` first. Revisit only if the client
      turns out to want individual pathways shareable or findable by search.

## 8. Security + privacy
The site is about as safe as a website gets: no server, no database, no passwords, and — since the
fonts were self-hosted on 2026-08-01 — exactly **one** piece of outside code, the analytics script.
That script and the email form are where nearly all the new risk sits.

**Third-party scripts — the main exposure**
- [x] ⚠ **Ended up with ONE third-party script, not two.** The plan assumed the email form would add a
      second. It doesn't: Constant Contact's widget was dropped over its Google reCAPTCHA (§4) and the
      replacement posts straight to Buttondown from our own code, with no embedded script. So
      **Plausible is the only outside code on the page** — verified 2026-08-06, it is the sole external
      script and one of only four external references in total.
      The risk it carries is unchanged and worth restating: that code can read everything on the page,
      including what someone types into the email field, and can change what is displayed. If Plausible
      is compromised, so is the site.
*Standing rules, not tasks:* keep the script count at **one, and add no more without a reason**;
prefer small single-purpose scripts; use Plausible's option to serve its script from our own domain;
record what each script is for, so an unexplained second one gets noticed.

**No security headers on GitHub Pages**

Normally you would tell the browser "only run code from these places", which contains the damage if a
third party misbehaves. GitHub Pages cannot send those instructions, so the site has no such
protection today. Two ways to answer that, and only one gets chosen:

- **A — put the site behind Cloudflare's free tier**, which can add the headers. Another service in
  the chain, but free and widely used, and it buys back the protection Pages cannot give.
- **B — accept the gap.** Defensible for a brochure site with one third-party script, but it should be
  a decision on the record rather than an oversight.

- [ ] **DECIDE: A or B.** Nothing is blocked on this before launch; it is a standing exposure either
      way, and B is a legitimate answer.

**Domain takeover** — covered in §7 (verify at organisation level, no wildcard DNS)

**Account access**

Whoever controls the organisation controls what the public sees, so this is the highest-value thing to
get right at handover.

- [ ] **POST-LAUNCH: set access rules on the organisation** — two-factor for every member, write
      access limited to those who need it, and branch protection on `main` so nothing reaches the live
      site unreviewed. Deferred 2026-08-06 to the handover. §7 lists the two-factor half separately.

**Collecting email addresses** — new personal data the project doesn't handle today
- [x] Collect only the address, nothing else — the form has one field
- [x] Let the email platform hold the data, not the site — Buttondown holds it; the site stores nothing
- [x] **Privacy policy published and CLIENT-APPROVED 2026-08-06** — `/privacy/`, linked from all four
      footers, and it covers unsubscribing and deletion
- [ ] **POST-LAUNCH:** confirm what Buttondown does about spam. Deferred 2026-08-06. Our own honeypot
      already catches bots before anything leaves the browser, so nothing is exposed in the meantime.

**One risk that already exists**
- [x] ~~The site loads its two typefaces from Google's servers~~ — **SELF-HOSTED 2026-08-01, done
      before the email/analytics scripts as planned.** Files in `fonts/`, both SIL Open Font License.
      **This took the site to zero requests to any outside host** — true on 2026-08-01, and no longer:
      the Plausible script was added 2026-08-05 and is now the only one. The fonts themselves still
      make no outside request, which is the point of this entry.
      Open Sans is ONE variable file covering 300–700 — the five per-weight downloads from Google are
      byte-identical, so the `font-weight:300 700` range in the `@font-face` rule is deliberate; do
      not split it back into five files. Only the Latin pair is preloaded (English + Spanish both sit
      inside it); Latin-Extended loads on demand via unicode-range.
      86 KB on disk, ~50 KB for a typical visitor, down from ~210 KB the old way. Type verified
      identical, all five weights resolving.

- [x] ~~**Re-run the full code review**~~ — **DONE 2026-08-06.** Held until the last third-party
      script was in; Plausible went in 2026-08-05 and no more are planned. Covered `index.html`, the
      three standalone pages, all three data files and both scripts.
      **Clean:** no dead CSS, no unused functions, every data file aligned (11 nodes and 7 profiles
      across three files, no orphaned keys), all 29 internal links resolve, no duplicate IDs, both
      scripts compile, 180 programme entries all with a name and an http URL, one external script.
      **Four defects found and fixed:**
      1. **Transcript text was injected unescaped.** Both languages are plain text today, so nothing
         was broken — but the Spanish arrives pasted out of Word, the same provenance that got the
         "In Short" bullets escaped on 2026-08-02. Now escaped. ⚠ Consequence: transcripts are plain
         text; markup in one would print as code. Neither language uses any.
      2. **The transcript modal stranded screen-reader users.** It set `aria-modal="true"`, which
         tells assistive tech to ignore everything outside the dialog, but never moved focus into it —
         so the reader opened the transcript and was left on content their software now treated as
         hidden. Focus now moves to the card, Tab is trapped inside, and it returns to the button that
         opened it. Verified end to end on the live page. This is the item raised 2026-07-21 and
         bundled with the lorem-ipsum fix; the lorem half shipped and this half did not.
      3. **No `<main>` landmark** on the Program Index, privacy or confirmation pages. Added, inside
         `.wrap` so the centred column and the page footers are untouched.
      4. **Privacy policy clauses were `<b>`, not headings** — no way to move between them with a
         screen reader, on the one document people scan for a single answer. Now real `<h2>`s set to
         `display:inline`, so it looks exactly as before. Verified against a screenshot.
      **One finding withdrawn:** the privacy page having no `noindex` was flagged as an oversight and
      is not — a comment in that file records it as deliberate, a privacy policy being a public
      document. Left alone. See §9 for the pre-launch question it raises.

## 9. Launch / general
- [ ] 🔴 **FIRST ACTION ON LAUNCH DAY — remove the pre-launch gate.** Added 2026-08-01. Password:
      **`thatsawesome`** (case and surrounding spaces ignored). Three pieces to delete, all marked
      "PRE-LAUNCH GATE" in `index.html`: the small script in `<head>`, the `#pwGate` CSS block, and
      the `<div id="pwGate">` + script just inside `<body>`. Leave any one behind and the site is
      still locked. Confirm afterwards in a browser that has never unlocked it — a private window,
      not your own, which remembers the unlock.
      ⚠ **It is not security.** It runs in the visitor's browser and the repository is public, so the
      files are readable on GitHub regardless. It stops someone who stumbles on the address, which is
      the real risk; it would not stop anyone determined. The password is stored as a SHA-256 hash so
      it isn't in the page source as plain text — obscurity, not protection. Do not reuse this password
      anywhere that matters. Genuine access control would mean Cloudflare in front of the site.
- [x] ~~**Should the privacy policy be findable by search?**~~ — **DECIDED 2026-08-06: NO.** It now
      carries `noindex,nofollow` like the other three, and that tag is **permanent** — it does not come
      off on launch day.
      Why: it is reached from the footer of every page, which is where anyone looks for it, so it has
      nothing to gain from search. It was also previously the only page a search engine could index
      while everything else sat behind the pre-launch gate — the gate lives in index.html alone.
      ⚠ A comment in that file used to say the opposite ("deliberately indexable — a privacy policy is
      a public document"). It has been replaced, not merely contradicted.
- [x] ~~**Should the Program Index be findable by search?**~~ — **DECIDED 2026-08-06: NO.** Its
      `noindex` stays and is now documented in the file as **permanent**.
      Why: it is a supporting page reached from every result page, not a front door. Search traffic
      landing straight on the table would skip the questionnaire the site exists to run.
      The argument the other way, recorded in case it is ever revisited: it is a genuinely useful
      public document — 91 programmes in one filterable table, and nothing else on the web lists them
      together. If the client ever wants it found on its own, this is the decision to reopen.

- [ ] 🔴 **AND remove the search-engine block.** `index.html` carries
      `<meta name="robots" content="noindex,nofollow">` near the top, added 2026-08-01 so the
      connected domain stays out of Google while the content isn't final. **Leave it in and the
      launched site is invisible to search with nothing on the page to show it.** Delete the tag and
      its comment, push, then confirm at `view-source:artsedpathways.org` that it's gone.
      ⚠ **This is index.html's tag ONLY. Delete one, leave three.** All four pages now carry
      `noindex`, and index.html's is the only one that is temporary. The other three are permanent by
      decision (2026-08-06) and each says so in a comment beside it:
        • `program-index/` — supporting page, not a front door
        • `privacy/` — reached from every footer, nothing to gain from search
        • `subscribed/` — reached only from a link in an email; nobody should arrive cold
      Clearing them all by reflex would publish the sign-up confirmation page to search.
- [ ] Full QA pass — cross-browser and real devices, not the preview pane
- [ ] **Save one result page as a PDF from the LIVE domain and click the links in it.** Two separate
      things to confirm, both about a minute's work:
      1. **The four resource documents.** They are links to our own site (`resources/…`), written
         relative, so a saved PDF bakes in whatever address the reader was on. From the live domain
         that becomes `https://artsedpathways.org/resources/…` and is correct forever. From a local
         preview it becomes `http://localhost:8765/…` and is dead on anyone else's computer — so a
         PDF saved before the domain is live must not be circulated. The other 32 links are absolute
         and unaffected either way.
      2. **Whether links survive at all, per browser.** Chrome, Edge and Safari keep them clickable.
         Firefox's built-in Save-to-PDF has historically flattened links; if that is still true it is
         worth knowing before someone reports it. Test in Firefox specifically.
      Page-side is already confirmed (2026-08-02): 36 real links inside the printed area, none hidden
      by the print styles, collapsed sections expanded so nothing is omitted.
- [~] Play one real clip through in a normal browser — the preview pane suspends video, so continuous
      playback is the one thing that cannot be confirmed here.
      **`welcome` DONE 2026-08-11**, on phones against the live site: playback, the speaker strip
      changing hands, and the wipe all confirmed. Repeat per clip as the other ten land.
      ⚠ The pane's video decoding is not merely limited, it is INTERMITTENT — it played twice in one
      session and refused either side of that, and it will not seek at all. Treat any playback-based
      check here as unreliable and confirm it in a real browser.
- [ ] Final content review with the client
- [x] ~~Welcome transcript is lorem ipsum~~ — fixed 2026-07-31; real transcript now loads.
- [x] **"Civil Cyber Arts" credit link wired 2026-08-03** — `mailto:civilcyberarts@electrobeam.net`,
      in all four places: the site footer, the result pages, the Program Index and the sign-up
      confirmation page. TEMPORARY by intent: an alias address, chosen so it can be deactivated
      without touching the site if it starts attracting harvested spam. A public mailto in a footer
      is readable by address scrapers — if the alias is ever retired, swap the destination rather
      than leaving a dead link.
- [x] ~~**Cross-index: SSC / TA / CTE have no visible explanation on desktop.**~~ — **CLOSED
      2026-08-06, client's call: not a concern.** The desktop table abbreviates the Pathway column to
      save width. Each chip carries a hover tooltip with the full wording, but it needs about a second
      of stationary hover and the dotted underline that normally signals "this expands" was removed to
      keep the chip clean — so in practice nothing on the page tells a desktop reader what SSC means.
      What made it acceptable: mobile is unaffected (the panels spell the pathway out in full), and the
      dropdown above the table shows the full wording on desktop too.
      If it is ever reopened, the cheapest fix is restoring the dotted underline on the chips — one
      line, a standard cue, and it keeps the width saving.
- [x] ~~Delete unused `images/createca_logo_color.png`~~ — **DONE.** Confirmed gone 2026-08-06; only
      the `_EDIT` version remains and it is the one referenced.
- [x] **`build-scan.py` false readings — ALL THREE FIXED 2026-08-01.** Root cause in every case: the
      scan read `index.html` for text that had moved to `data/content.en.json`. It now reads both.
      1. ~~*"Transcripts written (0/11)"*~~ — reads the content file; correctly reports 11/11, and
         still flags any node that is empty or holding lorem. Round-tripped both ways.
      2. ~~*"Stay in touch opt-in — wired"*~~ — the old check hunted for a placeholder button that
         stopped existing when the band was rebuilt as a form, found nothing, and concluded "wired".
         It now inspects the form's own destination and reports **NOT WIRED — accepts an address and
         silently discards it; must not ship**. Deliberately biased to under-report: if the form is
         ever wired by some route without a destination on the form itself this reads pending when
         it is done, which is the safe direction to be wrong in.
      3. ~~*"No lorem-ipsum placeholders"*~~ — see the result-page summaries entry in §1.
      Verified by round-trip: each line goes green under a simulated finished state and back to
      pending when restored.
      3. ~~*"No lorem-ipsum placeholders"* missed the result-page summaries~~ — **FIXED 2026-08-01.**
         The scan now reads `data/content.en.json` as well, names the file and count, and adds a
         "Result-page summaries (client copy)" line. It goes pending on the summaries' `"placeholder"`
         flag as well as on the text itself — necessary, because only 3 of the 22 placeholder bullets
         literally begin "Lorem ipsum", so a string search alone would have read green.
         Round-tripped: green with real copy in place, pending again once restored.
         **Items 1 and 2 above are still wrong and still unfixed.**

### From the 2026-07-27 code inspection — your call, none started
- [ ] **Base text size overrides browser settings** (`html{font-size:20px}`) — people who enlarge their
      default text get overridden. Fixing means re-checking every size sitewide.
- [x] **Moving content can't be paused — CLOSED 2026-08-01.** Split in two: one half built, the other
      decided against. Nothing outstanding.
      - [x] **"Reduce motion" is respected for the hero photos and the quote carousel.** With the
            setting on, the hero photos stay put (and the other seven aren't even fetched), the quote
            carousel doesn't advance on its own, and both crossfade transitions are off. The arrows
            and dots still work, so the quotes remain reachable — automatic movement is what stops,
            not navigation. Verified in both states, including that manual use doesn't restart the
            drift.
            ⚠ **It does NOT cover video** — corrected 2026-08-08; this entry previously claimed
            "across the whole site", which was written before the player existed. The landing loop
            autoplays for everyone, and each node clip starts playing as its screen opens; neither
            consults the setting. **Reviewed 2026-08-08 and deliberately left as is.**
            If it is ever revisited, the landing loop is the one that matters: ten seconds of motion
            repeating indefinitely with no pause control anywhere on the page. Node clips are far
            less exposed — the visitor chose to start the questionnaire, and each has Skip and
            tap-to-pause. Holding the landing frame on its poster for that setting would also give
            the chosen poster frames a real audience rather than a flash.
      - [x] **A visible pause control — DECIDED 2026-08-01: not building one.** Respecting the OS
            setting is the accessibility requirement and that is done. The quote carousel already
            pauses on hover and has arrows; the hero is decorative. Closed, not deferred.
ℹ **Note, not a task:** local previews must be served over http (`python3 -m http.server 8765 --bind
127.0.0.1`), not opened by double-clicking — the program list can't load from a `file://` page.

---

## 10. Post-launch — deliberately deferred, NOT forgotten
Things that are researched, decided and ready, but should not ship on 2026-08-17.

- [ ] **UCLA Extension: CTE in Teaching Artistry — add once UCLA Extension publishes the page.**
      Moved here 2026-08-05, off the client's ask list. She has been told and agreed to hold it.
      **Why it is not shipping:** the pathway launches **Autumn 2026** and has no public page. The only
      URL on file is a free, non-credit information session ("From Artist to Educator", EDUC 769),
      currently *"Not available this quarter"* — a dormant recruitment event, not a programme.
      **Answered already, so do not re-research:**
      - NOT a duplicate. The existing `UCLA Extension` entry is their *general* CTE credential; this is
        a distinct Teaching Artistry pathway. Both belong once the second exists.
      - Name it `UCLA Extension CTE in Teaching Artistry`, **not** the client's "UCLA VAPAE…" label.
        VAPAE is UCLA's Visual and Performing Arts Education Program in the Graduate School of
        Education — a minor for current undergraduates, a different unit, wrong audience. The client
        has been told the label changed and why.
      - **CTE list only** (client, 2026-08-05). Her original request said Teaching Artist as well; she
        has since confirmed CTE only.
      - Region: Southern California. Delivery: assume Online only to match Extension's other CTE
        offering, but **check at launch** — it is an assumption about an unlaunched programme.
      **To add it:** one entry in `data/programs.json` → `cte`, plus the same name in `SCHOOL_REGION`
      (index.html) and in the Program Index's data block. All three must carry it or the build scan
      will report a mismatch. It was built and reverted on 2026-08-05, so it is a ten-minute job.
      ⚠ `data/programs.json` must be edited IN PLACE. Rewriting it through a JSON library reformats
      the whole file and turns a one-line change into a 1,100-line diff.

---

## Recently completed
**2026-08-02**
- [x] **"Delivery" column and filter renamed "Format"** (2026-08-02). Standard wording in course
      listings and plainer than "delivery", which is institutional. Rejected "In-Person / Online":
      it names two of the four values and omits Hybrid, so it reads as a binary when there are four.
      The four values themselves are unchanged. Note the notes and code comments still call the
      underlying data "delivery method" — that is the concept; "Format" is what the reader sees.
- [x] **Cross-index: online programmes now count as available in every region.** The region filter
      answers "can I do this from where I live?", not "where is the campus?" — so a programme
      delivered **Online only** or **In person or online** matches every region, and its region cell
      reads `Southern (statewide)`: the campus location, then a dimmed marker saying geography does
      not limit it. **Hybrid stays geographic** — it requires attending in person.
      Effect on the filter: Northern 28 → 53, Central 11 → 45, Southern 48 → 66, Statewide 40. Each
      setting now returns half to three-quarters of the list, which is accurate but means the filter
      narrows less; the marker is what lets the eye separate local from statewide. Sorting by region
      puts locals above statewide ones within each region.
- [x] **Region "Online" renamed "Statewide"** — in the cross-index AND on the result pages
      (`data/content.en.json` → `regionLabels`, one word). As a REGION it never meant online
      delivery; it means the organisation has no single campus. Two of the three rows carrying it
      are not online at all — Focus 5 is hybrid, The Entertainment Community Fund is in person only.
      Beside a delivery column that also says "Online only", the old label read as a duplicate of
      something it did not mean.
      ⚠ Stored values are untouched — `SCHOOL_REGION` in index.html still says `"Online"`, and only
      the display maps to Statewide. Don't "tidy" the data to match the labels.
      ⚠ Those three rows are on the PROVISIONAL region list awaiting client review (§2), so the
      client's answer could change this again.
      Note the result pages did NOT get the statewide-matching behaviour, and should not: they
      *group* by region and show every group at once, so nothing is hidden. Only the cross-index
      *filters*, which is where excluding an online programme would have been a false negative.
- [x] **SETTLED 2026-08-02 — what belongs in the cross-index, and why.** Both questions were weighed
      and answered; don't re-open without new information.
      **Teaching Artist and CTE stay in.** Three reasons. (1) The cross-index link sits on all SEVEN
      result pages, including the Teaching Artist and CTE ones — a visitor told their pathway is
      Teaching Artist would otherwise open it and find not one teaching-artist organisation there.
      (2) 27 of the 90 rows are Teaching Artist or CTE *only* and would disappear entirely — Luna
      Dance Institute, LACMA, CoTA, Focus 5, P.S. ARTS, the county offices. They are a different kind
      of provider (community organisations and county offices; the credential lists are all
      universities) and nowhere else lists them together. (3) It would discard the delivery-method
      research already done on them.
      The fair counter-argument, considered and rejected: a CSU credential programme and LACMA's
      teaching-artist training are not like things, and one table invites a false comparison. What
      answers it is the Pathway filter — anyone wanting like-for-like narrows to Single Subject
      Credential and gets exactly the four-discipline index.
      **Supplementary Authorization is deliberately absent, and cannot be added.** It is a pathway in
      the questionnaire (one of the seven result pages) but not a programme anyone enrols in: you
      show the CTC coursework or subject-matter competency you already have and they add the
      authorization. `data/programs.json` says so — `supplementaryAuth` holds a CTC URL and the note
      "Explanatory content profile (not a school list)", where every other pathway holds schools.
      Adding it as a filter option would offer a choice that always returns zero rows.
      ⚠ Open content question if it ever matters: the coursework it requires (20 semester units, or
      10 upper-division) IS taken somewhere, plausibly at institutions already in the index — but
      nobody has recorded which. That is research, not a code change.
- [x] **Cross-index rebuilt as a filterable, sortable table** — replaces the four delivery-mode
      groups. Filter by **pathway** (Single Subject Credential / Teaching Artist / CTE),
      **discipline** (Music / Theatre / Dance / Art), **region**, and **delivery method** — four
      dropdowns, each defaulting to "All …", combining to narrow the list. Sort by Program, Region or
      Delivery. Count of what is showing ("61 programs") plus clear-all; a set filter turns gold so
      the active ones are visible at a glance.
      Design settled 2026-08-02 over several passes, all on request: pill buttons → dropdowns;
      per-value counts removed; oval corners → the same 4px rectangle as the pathway and discipline
      tags in the table; "N of 90" → a plain count, since the unfiltered total is what the line
      already shows with nothing selected; every menu's first option is simply "ALL" (the label above
      it already names the dimension); and regions display as Northern / Central / Southern, without
      "California" — the whole site is Californian, so the word carried nothing.
      ⚠ The stored region values DO keep "California" so they still match `SCHOOL_REGION` in
      index.html — only the display drops it. Don't "tidy" the data to match the labels.
      Consequence of the dropdowns: filters are single-choice — you cannot ask for Music OR Dance in
      one go, which the pills allowed. Revisit only if that combination turns out to be wanted.
      **Data:** names, links and pathway membership are read from `data/programs.json` at load, so
      the page cannot drift from the result pages when a programme is added or a link changes. Only
      region and delivery method are held locally — region is DUPLICATED from `SCHOOL_REGION` in
      index.html and has to be changed in both places; delivery has no counterpart in index.html.
      **Discipline is only recorded for credential programmes.** 27 of the 90 rows are Teaching
      Artist or CTE and show "—"; the discipline filter goes inert when the pathway filter excludes
      Single Subject, rather than silently returning nothing. A note under the table says so.
      If those 27 are ever tagged by discipline (Luna Dance Institute → Dance, LACMA → Art …) the
      filter picks it up with no code change.
      Each pathway/discipline chip links to that programme's own page — 40 of the 90 schools have a
      different address per discipline, so the single "view" link the old page carried could only
      ever be right for some of them. That link was the delivery-mode research source, not the
      programme page; it is no longer shown.
      Verified live: 90 rows, all four axes populated; single filters, two filters combined, the
      inert-discipline rule, clear-all, and all three sort columns including `aria-sort`.
- [x] **Cross-index header + colour scheme settled** — renamed to title "Arts Educator Pathways" over
      subtitle "Program Index" (the result pages' `.res-label`: gold, caps, same size and
      tracking). **Stays on the inverted scheme** — dark ground, light type — after a light-scheme
      version was tried and rejected on 2026-08-02.
      The ground is `--navy`, the exact colour of the result-page header band, and the title now sits
      directly on it with a hairline rule beneath instead of inside a panel: a navy card on a navy
      field had nothing to distinguish it.
      The page's CSS is a COPY of index.html's tokens, not a shared file — a palette change there has
      to be mirrored here by hand. Noted at the top of its stylesheet.
      Known and deliberate: the four category dot colours have no counterpart in index.html, and the
      table's per-row "view ↗" links keep their arrow, which the result pages drop from list links.
- [x] **Cross-index linked as the first item in Additional Resources** — a link, not a collapsible
      section: same typeface, size, colour, hairline and spacing as the section rows, with an arrow
      where they carry a disclosure chevron, so it reads as "goes somewhere" rather than "opens".
      Opens in a new tab like every other resource link, because the result page is drawn in the
      browser and navigating away in the same tab would lose it. Label lives in
      `data/content.en.json` as `ui.crossIndex` ("Program Index") — edit it there, not in
      index.html. Verified on all 7 result pages, print included, accordion unaffected.
      ⚠ **Gated — see §3.** It publishes the online-availability data ahead of the client's sign-off.
- [x] **Additional Resources is now a one-at-a-time accordion** — opening a section closes whichever
      was open. Done with the browser's own exclusive-accordion attribute, no JavaScript behind it;
      a browser too old to know the attribute just lets several open, as before. The programme-region
      bands above are deliberately NOT part of this — they stay independent and open by default.
      ⚠ It carries one non-obvious consequence: the browser will not allow two same-named sections
      open at once, which would have silently dropped all but one resource section from the printed
      page and the saved PDF. The print handler strips the attribute before expanding and puts it
      back afterwards. Verified: exclusive on screen, all five open during print, state and attribute
      restored after, still exclusive on the next click.
- [x] **Full code review of the site** — `index.html` end to end, all three data files, both scripts.
      Nothing to clean up: no dead CSS, no unused functions, all 90 programmes mapped to a region,
      `index.html` and `data/content.en.json` aligned exactly (11 nodes, 21 resource links). Three
      real defects found and fixed (below); everything else was already sound.
- [x] **Missing-clip fallback now clears every clip-only control.** A node switched on with `v:1`
      whose file is absent dropped back to the still and removed mute and CC, but left the playback-
      speed button behind — a live control over a photograph, opening a menu that changed nothing.
      Likely to bite during the video drop if a file is late or misnamed. Speed and the caption layer
      now go with it. Verified by simulating an absent file.
- [x] **Client-written result bullets are now escaped.** The "In Short" copy is the only text in
      `data/content.en.json` written outside the project, and it goes straight into the page. A `<`
      or `&` pasted from Word would have eaten the rest of the line. ⚠ Consequence: those bullets are
      **plain text** — bold or italic inside one will not work. Everything else in that file still
      renders its deliberate markup (`<strong>`, `<em>`, the CTC link, `&copy;`, `&amp;`), which is
      why the escaping is scoped to these bullets and must not be widened. Verified both ways.
- [x] **Resource documents moved onto the site** — `resources/`, four PDFs, replacing every Google
      Drive link in the Additional Resources section. Two of the Prop 28 links pointed at the SAME
      Drive folder, so one title opened the wrong document; those two and a third also carried
      `/u/1/` in the address, which pins the visitor to whichever Google account they signed into
      second — anyone with more than one could have hit a "request access" screen. No Drive links
      remain anywhere on the site. Re-hosting the three third-party reports was approved 2026-08-02;
      the client relationship owner may still want to be told.
      Verified: all four serve as PDFs, each paired with the correct title, all 21 resource links
      unique, no console errors.
- [x] **Local preview server bound to `127.0.0.1`** — `python3 -m http.server 8765` alone publishes
      the whole project folder to the local network (drafts, notes, client research), and the
      pre-launch password gate does NOT cover it: the gate is JavaScript inside `index.html`, so
      fetching any other file walks straight past it. `CLAUDE.md` updated to document the bound form.

**2026-08-01**
- [x] Three-way caption control (off / English / Español) and per-node caption-language flags built
      and verified (§6). Spanish captions are now a file drop on Aug 5, not a build.
      Verified: menu contents and labels, choice persisting and being remembered across nodes,
      fallback on a node without the chosen language, one-language nodes keeping the old on/off
      button, legacy `cc:1`, no CC button where no captions exist, caption track switching, the two
      menus never open at once, Escape and click-away, and no overlaps in the control row at phone
      width or on desktop.
      Known, pre-existing and unrelated: in a very short landscape window (roughly under 700px tall)
      the video frame collapses narrower than the control row, which overflows. The Skip button alone
      already overflowed before this change. Not introduced here; flag it if it matters.

**2026-07-31**
- [x] English transcripts finished and declared final — all 11 nodes, `video/transcripts/eng/`.
      lifeTA and music revised later the same day; current total 2,342 words
- [x] Spanish drafts for lifeTA and music regenerated to match those English edits; both data files
      rebuilt and verified on the site
- [x] Spanish transcripts drafted — all 11, `video/transcripts/esp/`; with the client for review
      (register, terminology and gender decisions recorded in §6)
- [x] **Spanish scope cut, agreed with client: captions + transcripts only, interface stays English.**
      Removed ~1,100 words of client translation work, the `/es/` vs toggle decision, and the
      landing-page extraction dependency (§6)
- [x] Questionnaire + results copy extracted to `data/content.en.json`; `index.html` now holds
      structure only. Verified: all 11 nodes, all 7 result pages, transcript modal, resources,
      Supplementary Authorization page, full click-through and browser Back
- [x] English transcripts loaded into the Transcript modal on all 11 nodes; lorem ipsum removed
- [x] Transcript modal EN/ES switch built and verified — all 11 nodes, choice persists between
      videos, both missing-Spanish fallbacks degrade to English cleanly (§6)
- [x] Playback-speed menu + shortened Skip label built and verified — all 11 nodes, control row
      free of overlaps at phone width, menu stays inside the picture, using the controls does not
      pause the video, choice persists between videos
- [x] Client-preview overlay templates regenerated to match the new control row
- [x] Overlay templates rebuilt for Photoshop — it ignores the SVG vertical-centring instruction,
      so labels sat low. Now positioned on explicit baselines with icons in absolute coordinates.
      Verified centred to within 0.1px. **Do not reintroduce `dominant-baseline` in these files.**
- [x] ~~Transcript modal names its video — "TRANSCRIPT – TEACHING ARTIST VS. CREDENTIALED TEACHER"~~
      — **TITLE REMOVED 2026-08-08. This entry is superseded; kept as the record of why the title
      looked the way it did, in case it ever comes back.**
      Removed as redundant: the transcript can only be opened from the node the reader is already on,
      one tap earlier, so the heading repeated what they had just clicked. Dropping it also settled a
      small oddity — the node name stayed English even while the Spanish text was showing.
      The header was reworked rather than just trimmed, because deleting the heading would have left
      an empty strip: it is now ONE row, language switch left and close button right, 73px with
      Spanish and 69px without. The close button moved into the flow instead of floating over a
      heading that no longer exists.
      ✔ **The node name survives where it is not redundant.** The dialog's spoken name — "Transcript
      – Welcome" — comes from `aria-label` and was always separate from the visible title, so a
      screen-reader user who cannot see which node is behind the sheet is still told. Do not remove
      that too.
      Verified after the change: focus enters the card, Tab stays trapped and wraps across the three
      controls, Escape closes, focus returns to the trigger, and the EN/ES switch still swaps the
      text and marks it as Spanish. The three CSS rules that existed only for the title were deleted.
      <details><summary>Original entry, kept as the record</summary>

      Node titles stay English when the Spanish text is showing, per the §6 scope cut.
      Both parts are set in Bebas Neue, distinguished only by colour (title in `--blue`).
      **Titles read as all caps, and that is intended.** Bebas Neue carries no lowercase glyphs, so
      caps are the only thing it can render. A mixed-case version was built and then reverted by
      request on 2026-07-31 — do not "fix" the capitalisation; changing it means changing typeface.
      Sizes reduced 25% at the client's request (desktop 1.7rem → 1.275rem, narrow 1.25rem → .94rem).
      Header is 11–19% of the card, and the title clears the close button on all 11 nodes at phone
      and desktop width.

      </details>

**2026-07-30**
- [x] Result actions reduced to Print / Save PDF + Restart Questionnaire, side by side
- [x] Email opt-in band added (visual only — see §4)
- [x] Program regions made collapsible: open by default, tinted bands, counts
- [x] Removed link arrows, heading colons, dagger marks + footnote block
- [x] Vertical rhythm across result pages set to 50 / 25 / 15
- [x] 44px tap targets for program + resource links on touch screens
- [x] Resources renamed and reordered (FAQs · Prop 28 · Agencies · Associations · National)
- [x] Resource section titles made real headings (navigable by screen reader)
- [x] Added the missing font preconnect
- [x] Full code review — two dead CSS rules removed; assets, links, data, all 11 questionnaire routes,
      error state and print behaviour all verified clean

**Earlier this build cycle**
- [x] `escapeHTML()` for program-data injection
- [x] Landing landmark (`<main>`) + heading-order fix (h4 → h3)
- [x] Merged duplicated CSS link-arrow rule
- [x] Additional Resources section (collapsible subsections + print-expand)
- [x] Supplementary Authorization page copy update + italic note
- [x] Footer design credit (Civil Cyber Arts) — link wired 2026-08-03, no longer a placeholder
- [x] DPP section / subsection title styling
