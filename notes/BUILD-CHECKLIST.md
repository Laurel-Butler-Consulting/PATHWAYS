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
- [ ] **Analytics: what do they want to know?** Completion rate, drop-off points, which pathways come up
      most, mobile vs desktop? The answer determines the tool and whether extra build work is needed.
      Also: are they willing to pay ~$9–15/month? Free tools can't answer questionnaire questions.
- [x] **Spanish scope settled 2026-07-31: captions and transcripts only.** No interface translation,
      no `/es/` address, no language toggle. The site's own text stays English. (§6)
- [x] **Repository stays PUBLIC** (decided 2026-08-01). Who keeps write access after handover is
      still open — see §7 Phase A.
- [x] **Dagger caveat — CLOSED 2026-08-01: not needed.** The removal stands; the warning does not
      have to reach users another way. (§2)
- [ ] **Online-availability marker threshold** (§3)
- [~] **UCLA Extension CTE — mostly resolved by research 2026-08-03 (§2).** Not a duplicate; the URL
      on file is only an info session; the real pathway launches Fall 2026 and needs its URL from
      UCLA Extension. Nothing needed from the client except the pathway URL when it exists. A separate
      decision IS needed from us on the UCLA name collision (§2).
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
      goal fired and was seen in Plausible: the 6 custom events, the 8 pathway pageview goals
      including the `/result/*` overall rate, plus Plausible's own File Download and Outbound Link.
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
- [x] ~~**Review the Spanish transcripts**~~ — **DONE. Client supplied approved V2 2026-08-03**, all 11
      installed 2026-08-04. Superseded the drafts entirely.
- [ ] **Answer the 12 transcript queries** — `notes/transcript-queries-for-client.txt`. Wording calls
      only, no rewriting: two Spanish meaning items (the "real world / classroom" sentence in CTE
      Intro, and how CTE itself is translated), seven register/consistency calls for their translator.
      Nothing is blocked on these — the site carries the approved text as-is meanwhile.
- [ ] **CTE experience: paid vs unpaid — decision needed 2026-08-05.** The Commission counts three
      years of work experience "full-time or part-time, paid or unpaid", at 1,000 clock hours a year,
      verified by employers (CL-888). The word *paid* therefore turns away people who qualify. The
      CTE Intro question card has been changed to "3 years of work experience in your art form, with
      at least 1000 hours per year". Two things still say *paid* and need the client's call:
      the CTE Intro **video narration**, which would need a re-record, and that node's **transcript
      text** in `data/content.en.json`, which we can change without touching the video but which
      would then differ from what is spoken. The next video in the branch (CTE Path) already says
      "work experience", so the footage is already inconsistent with itself.
- [ ] Confirmation of the PROVISIONAL region assignments (§2)
- [ ] **A privacy policy**, or a decision about who writes one — required before collecting email
      addresses, and the site has none today (§4, §8)
- [ ] **Approval** of the media below once delivered

**Media — our purview, client approves** *(not a client deliverable; do not put on their ask list)*
- [ ] 11 presenter videos, final (§1)
- [ ] Landing "Find Your Path" preview clip + poster (§1)
- [ ] Final poster stills (§1)
- [ ] Captions — Premiere SRT export → `scripts/srt2vtt.py` (§1)
- [ ] **FOR THE EDITOR: spell it "theatre", not "theater", in the caption source.** The site was made
      uniform on 2026-08-05 — every word a visitor reads now says *theatre*. Captions are the one
      place that can drift back, because Premiere is the source of truth and the next export
      overwrites anything corrected by hand here. Fix it in Premiere and re-export.
      Done: `09_theatre_260805.srt` (was `09_theater_…`, 6 instances, Eric's video).
      ⚠ Still outstanding, one instance each:
        • `video/captions/eng/03_discipline_260801.srt` — "Dance, Theater, Music, and Visual Arts"
        • `video/captions/eng/07_suppauth_260804.srt` — "degree in dance, music, theater, or visual arts"
      Spanish captions are unaffected (they say *teatro*), and the corrected file kept its timings
      exactly, so the Spanish sidecars still line up cue for cue and need no rework.
      NOT to be changed: the internal name `mTheater` in index.html and data/content.en.json (a code
      label, never shown, and the two files must keep matching), and the San Diego State link in
      data/programs.json, whose web address contains "theater".
- [x] English transcripts for all 11 videos — written and final 2026-07-31 (§1)
- [x] Spanish transcripts — **client-approved V2 installed 2026-08-04**, 11 files (§6)
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
- [ ] 11 presenter videos recorded & final → `video/nodes/<node-key>.mp4`
- [ ] Landing "Find Your Path" preview video — final clip + poster (muted loop; no transcript)
- [ ] Poster stills finalized (placeholders currently in `images/video placeholder stills/`)
- [ ] Switch each node on as its clip lands (`v:1`, plus `cc:1` once its `.vtt` is beside it)
- [ ] Captions (`.srt` → `.vtt`) for all narrated videos
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
- [ ] **Result-page video summaries (Option C) — CLIENT IS WRITING THESE, 2026-08-01.** Not ours to
      draft. 7 result pages, 2–4 bullets each, recapping what the videos on that route covered, so the
      printed/saved page carries the substance and not just links. Chased, not yet received.
      ⚠ Needs a date from the client. It is public copy, so it has to be in before the Aug 5 freeze or
      it becomes a post-launch addition. Not structural — the result pages work without it.
      Add it to the client ask-list in §0; the 2026-08-01 decision email does not currently request it.
- [x] **Container for those summaries BUILT 2026-08-01**, so the copy is a paste, not a build. Sits
      between the pathway title and the programme list, inside `#resultDoc` so it carries into the
      printed page and the saved PDF. White card, gold left rule, heading "In Short" (editable).
      Copy lives in `data/content.en.json` under `summaries`.
      **Currently LOREM IPSUM.** ⚠ The on-page red warning band was **removed on request
      2026-08-01** — nothing on the page or in the printed version now marks this copy as unfinished.
      The only remaining safeguard is the `"placeholder": true` line in `data/content.en.json`, which
      `build-scan.py` reports on. **Run the scan before launch; the page will not warn you.**
      Two edits when the client's copy lands: paste the bullets, delete the `"placeholder"` line.
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
- [ ] PROVISIONAL region assignments (`SCHOOL_REGION`) — verify before launch
- [~] **UCLA CTE entries — client answered 2026-07-30: keep BOTH, not a duplicate.** Link text to read
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
      - **Region is answerable but blocked on a data-model problem — see §2 "UCLA name collision".**

- [ ] 🔴 **UCLA name collision — one name, two programmes, and both region and delivery are wrong for
      one of them.** `University of California, Los Angeles` covers TWO different offerings:
      **CTE** (UCLA Extension — courses "delivered online via Canvas", some with a live Zoom session)
      and **Music** (CenterX — a full-time, in-person credential inside a four-year UCLA undergraduate
      degree). Region and delivery are keyed by SCHOOL NAME, so both programmes share one value:
      - `SCHOOL_REGION` (index.html) and `r:` (program-index) say **Southern California** — correct for
        Music, wrong for the online CTE programme.
      - `d:` (program-index) says **Online only** — correct for CTE, wrong for the in-person Music
        programme.
      So each field is already wrong for one of the two, and changing either fixes one while breaking
      the other. **The fix is to split the name**, listing the CTE entry as `UCLA Extension`
      (r: Online, d: Online only) and leaving `University of California, Los Angeles` for Music
      (r: Southern California, d: In-person). That also gives the Teaching Artistry pathway a correct
      home when it launches, since it is also UCLA Extension and also online.
      Consequences of the split: the Program Index gains a row (90 ➜ 91) and the CTE result pages show
      "UCLA Extension" rather than "University of California, Los Angeles". **Needs a decision before
      building — it changes a published link label.**

## 3. Online-availability marking
- [ ] Client sign-off on marker threshold, then wire in (research done for all 92 programs)
      [`notes/online-availability-README.md`](online-availability-README.md) · `notes/online-availability-review.json`
- [ ] 🔴 **The cross-index is now LINKED from every result page (2026-08-02) — this publishes the
      online-availability data ahead of the sign-off above.** `program-index/index.html` groups all 92
      programmes by delivery mode (In-Person Only / In Person or Online / Hybrid / Online Only),
      which is the same research this section is gating. Linking it means a visitor reaches that
      grouping even though the markers themselves are not on the programme lists yet.
      Nothing is public while the pre-launch gate and `noindex` are in place, so there is no exposure
      today. **Before launch, either get the client's sign-off (which covers both) or remove the row**
      — it is one line in `resourcesHTML()` in index.html, marked with a ⚠ comment.
      Second-order: the cross-index carries its own `noindex`; if it stays, decide whether that is
      still wanted once the main site is meant to be found by search.

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
- [ ] ⚠ **Buttondown settings still to confirm:** double opt-in ON (the success copy tells people to
      check their inbox), and "Embed fingerprinting" left OFF (it penalises exactly this kind of plain
      form, and it is fingerprinting).
- [ ] ⚠ **Deletion requests need an owner.** The privacy policy promises we delete an address on
      request. Unsubscribing does NOT delete it — Buttondown keeps the record so a later import cannot
      re-add the person. Whoever watches `info@createca.org` needs to know these arrive and needs
      Buttondown access, or a reliable route to someone who has it.

## 5. Analytics — anonymous, third-party
- [ ] ⚠ **The deciding factor is custom events, not privacy.** All the credible options are equally
      private. But the whole site is one page with one address — every questionnaire screen and every
      result renders without the address changing. A tool that only counts page visits will report one
      visit per person and nothing else. To learn completion rate, drop-off, or which pathway anyone
      reached, the site must send its own signals, which the tool has to support.
- [ ] Confirm with the client **what they want to know** before choosing.

| Tool | Cost | Custom events | Notes |
|---|---|---|---|
| **Plausible** *(recommended)* | from ~$9/mo | Yes | Open source, EU-hosted, cookie-free, small script; script can be served from our own domain, which reduces exposure (§8) |
| Fathom | from ~$15/mo | Yes | Cookie-free, EU data isolation, long retention |
| GoatCounter | Free | Limited | Open source, admirably minimal; thin event support and effectively a one-person project — sustainability risk for a client site |
| Cloudflare Web Analytics | Free | Very limited | Fine for basic traffic counts; not enough for questionnaire data |

- [ ] **Recommendation: Plausible** — cheapest tool that can answer the client's likely questions.
      No cookies means **no consent banner**, so nobody meets a popup before they meet the site.
- [ ] Confirm current pricing directly; these change.
- [ ] If the client won't fund a paid tool, the honest outcome is basic visit counts only and the
      questionnaire stays a black box. Say so rather than pretending otherwise.
- [ ] Adds a second third-party script — see §8.

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
1. ~~Client reviews / edits the 11 Spanish transcripts~~ — **DONE, V2 installed 2026-08-04.**
2. Build the Spanish subtitle files from the approved transcripts — **method decided 2026-08-04, see
   below.**
3. Wire both into the site — already built; only the files are missing.

**Spanish subtitles — METHOD DECIDED 2026-08-04, not started**

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

⚠ **The one complication: Spanish runs ~20–25% longer than English.** With timings locked to the
English, some cues get too dense to read. Handle it by letting cues run two lines, and by moving the
split point between neighbouring cues — which shifts words without touching a timecode. Merge two
short adjacent cues only as a fallback. Do **not** trim the Spanish: it's approved copy, and
shortening it means going back to the client. Any cue still above a comfortable reading rate gets
flagged rather than silently squeezed.

Manual alternatives if this ever needs doing without Claude: Subtitle Edit (free) or Aegisub load the
English timings and let you type the translation cue by cue. Same job, by hand.

⚠ **Blocked on the videos.** The English SRTs don't exist yet — `video/nodes/` is empty (§1). Nothing
here can start until the final clips and their English caption exports land. Suggested first pass:
**theater**, the densest script — if it reads comfortably at these timings, the other ten will.

**Design decided 2026-07-31:**
- [x] **Transcript modal EN/ES switch — BUILT 2026-07-31.** Two-way toggle under the modal heading;
      stacking the two languages was rejected. The choice is remembered and carries from one video to
      the next. Spanish text is marked as Spanish so screen readers pronounce it correctly.
      Spanish comes from `data/transcripts.es.json`, regenerated from `video/transcripts/esp/`.
      Degrades to English with no switch shown if a node has no Spanish or the file is missing.
      ✔ **The Spanish on the site is now the client-approved V2** (installed 2026-08-04), so the old
      "must not go live before review" flag is cleared. Twelve wording queries remain open — see
      `notes/transcript-queries-for-client.txt` — but none of them blocks launch.
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

**Spanish transcripts — CLIENT-APPROVED V2 INSTALLED 2026-08-04**
The client supplied their own approved translation (one document, 2026-08-03), which **replaced the
drafts entirely** — the 11 draft files were deleted and the folder now holds
`01_welcome_esp_V2.txt` … `11_visualart_esp_V2.txt`. `data/transcripts.es.json` was rebuilt from
them; all 11 verified word-for-word against the site.

Eight mechanical errors in the approved Spanish (agreement, a missing ñ, missing accents, a
duplicated word) were corrected in both the files and the site — listed with before/after in
`notes/transcript-queries-for-client.txt` for the client's records. Everything judged a style or
register call was left untouched and put to the client as a query instead.

The three house-style decisions below came from the *draft*. The approved V2 makes its own choices,
so these now read as a record of what was proposed, not as open questions — except where noted in the
queries file:

- [~] **Form of address: `tú`** (familiar), not `usted`. Matches the warmth of the English.
- [~] **Credentialing terms: English name + Spanish gloss on first use** — Supplementary
      Authorization, CTC, CSET, Single/Multiple Subject Credential, CTE, Prop 28, subject matter
      competency, student teaching, transcript evaluation. Rationale: these are the names on the CTC's
      own forms and website, which are English-only. Translating them outright sends people searching
      for something that doesn't exist under that name.
- [~] **Grammatical gender: feminine where neutral phrasing isn't possible** (client instruction,
      2026-07-31). Neutral wording is used where it reads naturally — e.g. *"te damos la bienvenida"*
      rather than *"bienvenida/o"*. Flag for the reviewer: some organisations prefer `educador/a`
      throughout instead.
- [x] ~~Client review of the 11 Spanish transcripts~~ — done, V2 installed 2026-08-04
- [ ] Second subtitle file per video (`<key>.es.vtt`) from the approved Spanish — **not** re-timed;
      built on the English SRT timings by the method above. Blocked on the videos.
- [ ] Mark the Spanish text so screen readers pronounce it as Spanish, not as English with an accent —
      applies to the transcript modal and the caption layer only, since the rest of the site is English.

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
- [ ] Two-factor authentication required org-wide
- [ ] Client added as a second Owner — needs them to have a GitHub account; settle before handover,
      not before launch. Org contact email is ours for now, deliberately: an address nobody reads is
      a liability while the client is hard to reach.

**Phase B — verify the domain FIRST** *(deliberately before connecting it)*
- [ ] In the organisation's settings → Pages, add the domain; GitHub issues a challenge code
- [ ] At the registrar, add a **TXT record** containing that code
      (`_github-pages-challenge-<ORG>`)
- [ ] Wait (up to 24h), then click Verify
- [ ] **Why first:** verification means only that organisation's repositories can publish to the domain.
      Skip it and if the site is ever deleted, disabled, or downgraded while DNS still points at GitHub,
      someone else can claim the address and publish their own content on the client's domain.
- [ ] Avoid wildcard DNS (`*.example.org`) — reintroduces takeover risk even after verification

**Phase C — transfer the repository**
- [ ] Transfer `ZZ72Z7Z7/PATHWAYS` to the organisation (history and settings come with it)
- [ ] Confirm Pages is enabled and building under the new owner
- [ ] Repoint the local clone's remote (`git remote set-url`) — otherwise the daily folder keeps pushing
      to the old address
- [ ] Note: `CLAUDE.md` and `.claude/` are untracked and do not transfer. The daily-folder process is
      personal to this build and doesn't need to survive handover.

**Phase D — connect the domain**
- [ ] Repository Settings → Pages → enter the custom domain (this writes a `CNAME` file into the repo —
      expect to see it appear in the working tree)
- [ ] At the registrar:
      - **Subdomain:** one CNAME → `<org>.github.io`
      - **Root domain:** four A records → `185.199.108.153`, `185.199.109.153`, `185.199.110.153`,
        `185.199.111.153`
- [ ] Wait for DNS propagation (up to 24h)
- [ ] Tick **Enforce HTTPS**; the certificate can take up to an hour and the box stays greyed out until
      it's ready
- [ ] Don't share any link until the domain is live

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
Today the site is about as safe as a website gets: no server, no database, no passwords, no outside code
except the fonts. **Nearly all new risk arrives with the additions above.**

**Third-party scripts — the main exposure**
- [ ] The email form and the analytics tool each place another company's code on the page. That code can
      read everything on the page — including what someone types into the email field — and can change
      what's displayed. If either company is compromised, so is the site.
- [ ] *Mitigations:* keep the count at **two, and no more**; prefer small single-purpose scripts; use
      Plausible's option to serve its script from our own domain; record what each script is for so an
      unexplained third one gets noticed.

**No security headers on GitHub Pages**
- [ ] Normally you'd tell the browser "only run code from these places", which contains the damage if a
      third party misbehaves. GitHub Pages can't send those instructions.
- [ ] *Mitigation A:* put the site behind **Cloudflare's free tier**, which can add them. Another
      service in the chain, but free and widely used, and it buys back the protection Pages can't give.
- [ ] *Mitigation B:* accept the gap — defensible for a brochure site with two scripts, but make it a
      decision, not an oversight.

**Domain takeover** — covered in §7 (verify at organisation level, no wildcard DNS)

**Account access**
- [ ] Whoever controls the organisation controls what the public sees
- [ ] Two-factor authentication for every member; write access limited to those who need it; branch
      protection on `main` so nothing reaches the live site unreviewed

**Collecting email addresses** — new personal data the project doesn't handle today
- [ ] Collect only the address, nothing else
- [ ] Let the email platform hold the data, not the site
- [ ] Publish a privacy policy; make unsubscribing obvious
- [ ] Spam is handled by the email platform — confirm what it does

**One risk that already exists**
- [x] ~~The site loads its two typefaces from Google's servers~~ — **SELF-HOSTED 2026-08-01, done
      before the email/analytics scripts as planned.** Files in `fonts/`, both SIL Open Font License.
      **The site now makes zero requests to any outside host** (verified: no external resource loads
      on the landing page or a result page).
      Open Sans is ONE variable file covering 300–700 — the five per-weight downloads from Google are
      byte-identical, so the `font-weight:300 700` range in the `@font-face` rule is deliberate; do
      not split it back into five files. Only the Latin pair is preloaded (English + Spanish both sit
      inside it); Latin-Extended loads on demand via unicode-range.
      86 KB on disk, ~50 KB for a typical visitor, down from ~210 KB the old way. Type verified
      identical, all five weights resolving.

- [ ] Re-run the full code review after the last third-party script is added, not before

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
- [ ] 🔴 **AND remove the search-engine block.** `index.html` carries
      `<meta name="robots" content="noindex,nofollow">` near the top, added 2026-08-01 so the
      connected domain stays out of Google while the content isn't final. **Leave it in and the
      launched site is invisible to search with nothing on the page to show it.** Delete the tag and
      its comment, push, then confirm at `view-source:artsedpathways.org` that it's gone.
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
- [ ] Play one real clip through in a normal browser — the preview pane suspends video, so continuous
      playback is the one thing never confirmed on a real file
- [ ] Final content review with the client
- [x] ~~Welcome transcript is lorem ipsum~~ — fixed 2026-07-31; real transcript now loads.
- [x] **"Civil Cyber Arts" credit link wired 2026-08-03** — `mailto:civilcyberarts@electrobeam.net`,
      in all four places: the site footer, the result pages, the Program Index and the sign-up
      confirmation page. TEMPORARY by intent: an alias address, chosen so it can be deactivated
      without touching the site if it starts attracting harvested spam. A public mailto in a footer
      is readable by address scrapers — if the alias is ever retired, swap the destination rather
      than leaving a dead link.
- [ ] **Cross-index: SSC / TA / CTE have no visible explanation on desktop.** Raised and DEFERRED
      2026-08-02 — left as is for now, review before launch. The desktop table abbreviates the
      Pathway column to save width; each chip carries a hover tooltip with the full wording, but the
      tooltip is close to invisible in practice: it needs about a second of stationary hover, and the
      dotted underline that normally signals "this abbreviation expands" was removed to keep the chip
      clean. So nothing on the page tells a desktop reader what SSC means. Mobile is unaffected — the
      panels spell the pathway out in full — and the dropdown above the table shows full wording, which
      is the argument for leaving it. Three fixes, cheapest first: restore the dotted underline on the
      chips (one line, standard cue, keeps the width saving); a one-line key under the filters
      (`SSC Single Subject Credential · TA Teaching Artist`, always visible, costs ~20px — the only
      option that doesn't rely on the reader discovering something); or widen the column and drop the
      abbreviation on desktop too (costs ~74px, which the 1080px container can now absorb).
- [ ] Delete unused `images/createca_logo_color.png` (48K; only the `_EDIT` version is referenced)?
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
- [~] **Moving content can't be paused.** Split in two 2026-08-01; the accessibility half is done.
      - [x] **"Reduce motion" is now respected** across the whole site. With the setting on, the hero
            photos stay put (and the other seven aren't even fetched), the quote carousel doesn't
            advance on its own, and both crossfade transitions are off. The arrows and dots still
            work, so the quotes remain reachable — automatic movement is what stops, not navigation.
            Verified in both states, including that manual use doesn't restart the drift.
      - [x] **A visible pause control — DECIDED 2026-08-01: not building one.** Respecting the OS
            setting is the accessibility requirement and that is done. The quote carousel already
            pauses on hover and has arrows; the hero is decorative. Closed, not deferred.
- [ ] Note for local previews: the site must be served over http (`python3 -m http.server 8765`), not
      opened by double-clicking — the program list can't load from a `file://` page.

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
- [x] Transcript modal names its video — "TRANSCRIPT – TEACHING ARTIST VS. CREDENTIALED TEACHER".
      Node titles stay English when the Spanish text is showing, per the §6 scope cut.
      Both parts are set in Bebas Neue, distinguished only by colour (title in `--blue`).
      **Titles read as all caps, and that is intended.** Bebas Neue carries no lowercase glyphs, so
      caps are the only thing it can render. A mixed-case version was built and then reverted by
      request on 2026-07-31 — do not "fix" the capitalisation; changing it means changing typeface.
      Sizes reduced 25% at the client's request (desktop 1.7rem → 1.275rem, narrow 1.25rem → .94rem).
      Header is 11–19% of the card, and the title clears the close button on all 11 nodes at phone
      and desktop width.

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
