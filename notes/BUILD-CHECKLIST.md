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
- [ ] **The domain.** Which address? A subdomain of their existing site (`pathways.createca.org`) is one
      DNS record and can't disturb their main site; a new root domain needs four and touches its root.
      Decide before any link is shared publicly — changing it later means re-sharing everything.
- [ ] **Analytics: what do they want to know?** Completion rate, drop-off points, which pathways come up
      most, mobile vs desktop? The answer determines the tool and whether extra build work is needed.
      Also: are they willing to pay ~$9–15/month? Free tools can't answer questionnaire questions.
- [x] **Spanish scope settled 2026-07-31: captions and transcripts only.** No interface translation,
      no `/es/` address, no language toggle. The site's own text stays English. (§6)
- [ ] **Repository public or private**, and who keeps write access after handover.
- [ ] **Dagger caveat** — does the "this link may open a general credential page" warning need to reach
      users some other way, now the footnote is gone? (§2)
- [ ] **Online-availability marker threshold** (§3)
- [ ] **UCLA Extension CTE** — region, and whether it duplicates the existing UCLA entry (§2)
- [ ] **Captions on by default?** (§1)

**Accounts + access**
- [ ] Create a GitHub **organisation** (not a personal account — it survives staff changes and supports
      multiple maintainers). Enable two-factor authentication. Add us as a member with write access.
- [ ] Access to the domain registrar, or a named person who can add DNS records on request.
- [ ] **Constant Contact account access** (or confirmation of a different platform).
- [ ] Decide who owns the analytics account and who reads the numbers.

**Content the client must supply**
- [ ] **Review the Spanish transcripts** (drafted 2026-07-31, 11 files) — three house-style calls need
      their confirmation, listed in §6. This is a review, not a writing job, and it is now the ONLY
      Spanish item on their list. It gates the Spanish captions.
- [ ] Confirmation of the PROVISIONAL region assignments (§2)
- [ ] **A privacy policy**, or a decision about who writes one — required before collecting email
      addresses, and the site has none today (§4, §8)
- [ ] **Approval** of the media below once delivered

**Media — our purview, client approves** *(not a client deliverable; do not put on their ask list)*
- [ ] 11 presenter videos, final (§1)
- [ ] Landing "Find Your Path" preview clip + poster (§1)
- [ ] Final poster stills (§1)
- [ ] Captions — Premiere SRT export → `scripts/srt2vtt.py` (§1)
- [x] English transcripts for all 11 videos — written and final 2026-07-31 (§1)
- [~] Spanish transcripts — drafted 2026-07-31, **awaiting client review / edits** (§6)
- [ ] "Civil Cyber Arts" credit link destination (§9) — ours alone, no client input needed

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
- [ ] **Landing page copy is still inline HTML** (~480 words: hero, About, Who Is This For, quotes,
      footer). No apostrophe risk there, and since the 2026-07-31 scope cut it is no longer a
      prerequisite for anything (§6). Optional tidy-up only — it would put all site copy in one place
      for editing. Low priority; do not do it on spec.
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
- [ ] Decide: captions on by default? (`PW_CC` currently off; playback starts muted)

## 2. Pending client review
- [ ] **REVIEW: dagger footnotes removed (2026-07-30)** — the `†` marks and the "State-approved program.
      This link opens the school's general credential page rather than a discipline-specific one — confirm
      program specifics with the school" note were removed from all result pages to reduce visual noise.
      **22 programs still carry the `f` flag in `data/programs.json`**, so this is display-only and fully
      reversible. Decide before launch whether that caveat needs to reach users some other way.
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

## 3. Online-availability marking
- [ ] Client sign-off on marker threshold, then wire in (research done for all 92 programs)
      [`notes/online-availability-README.md`](online-availability-README.md) · `notes/online-availability-review.json`

## 4. Email capture — Constant Contact
- [ ] **BUILT but NOT WIRED (2026-07-30). MUST NOT SHIP AS-IS.** The navy band at the foot of every
      result page accepts an address and silently discards it — no confirmation, no error, and it looks
      like it worked.
- [ ] Client to confirm the platform and provide account access.
- [ ] **Verify in their account before design is final:** the form's post-submission setting must show a
      success message on our page rather than redirecting to theirs. Their public docs don't state this
      either way. If it forces a redirect, people get thrown out of their results and the band needs
      rethinking.
- [ ] Route chosen: **their embedded form, restyled** (their markup + our CSS). Rejected the API route —
      it needs server-side code a static site can't hold, plus ongoing credential renewal and an owner.
      Consequence: their form loads a third-party script (§8) and their updates can break our styling.
- [ ] Design + build the states: success, failure (keep the typed address), already-subscribed.
- [ ] Confirmation must be **announced** for screen-reader users, not only displayed.
- [ ] **Privacy policy page** — collecting addresses normally requires one, and there is none today.
      Confirm who is the data controller and what the client's own policy says.

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
1. Client reviews / edits the 11 Spanish transcripts (drafted, below).
2. Build the Spanish captions from the approved transcripts — Premiere SRT → `scripts/srt2vtt.py`,
   same workflow as English, re-timed to each clip.
3. Wire both into the site. **Two design decisions must be made first — see "Open questions" below.**

⚠ **Blocked on the videos either way.** Captions can't be timed against clips that don't exist (§1),
so step 2 cannot start until the final videos land, no matter how fast the transcript review goes.

**Design decided 2026-07-31:**
- [x] **Transcript modal EN/ES switch — BUILT 2026-07-31.** Two-way toggle under the modal heading;
      stacking the two languages was rejected. The choice is remembered and carries from one video to
      the next. Spanish text is marked as Spanish so screen readers pronounce it correctly.
      Spanish comes from `data/transcripts.es.json`, regenerated from `video/transcripts/esp/`.
      Degrades to English with no switch shown if a node has no Spanish or the file is missing.
      ⚠ **The Spanish on the site is the DRAFT translation** — it must not go live before the client's
      review. Nothing is live yet (no videos), but this is the item to re-check before launch.
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
- [ ] ⚠ **One thing to confirm on Aug 4, with real files:** switch language **while the video is
      paused** and check the caption line repaints straight away. Browsers are supposed to recompute
      on the switch, and it can't be tested in the preview pane (which suspends video). If it comes up
      blank until playback resumes, it's a small fix — but find out before launch, not after.
- [ ] *Deferred, client's call, not a concern now:* signposting Spanish captions to a non-English
      reader inside an English interface; whether the printed PDF carries a transcript and in which
      language (it carries neither today).

**Spanish transcripts — DRAFTED 2026-07-31, awaiting client review / edits**
All 11 translated into `video/transcripts/esp/`, mirroring the English naming
(`01_welcome_esp.txt` … `11_visualart_esp.txt`). Standalone documents; nothing in `index.html` was
touched. Three house-style decisions were made in the drafting — the client's bilingual reviewer
should confirm or overrule all three, and each one is a full re-pass if changed later:

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
- [ ] Client review of the 11 Spanish transcripts
- [ ] Second caption file per video (`.vtt`), matching the approved Spanish transcripts — re-timed
      to the clips. Blocked on the videos as well as on the review.
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
      **Ask the client whether they expect to send individual pathways to people, and whether they want
      these found by search. Two "no"s and this stays shelved.**

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
- [ ] Play one real clip through in a normal browser — the preview pane suspends video, so continuous
      playback is the one thing never confirmed on a real file
- [ ] Final content review with the client
- [x] ~~Welcome transcript is lorem ipsum~~ — fixed 2026-07-31; real transcript now loads.
- [ ] Wire the "Civil Cyber Arts" credit link — placeholder `href="#"` in two places (footer + result
      pages). Confirmed still unresolved in the 2026-07-30 code review.
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
      - [ ] **A visible pause control** for people who don't have that setting on — still open, still
            your call. It's a design question (where the button goes, what it looks like), not an
            accessibility gap now.
- [ ] Note for local previews: the site must be served over http (`python3 -m http.server 8765`), not
      opened by double-clicking — the program list can't load from a `file://` page.

---

## Recently completed
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
- [x] Footer design credit (Civil Cyber Arts; placeholder link)
- [x] DPP section / subsection title styling
