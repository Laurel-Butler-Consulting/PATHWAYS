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
- [ ] **Spanish: scope confirmed as text-only** (no re-recorded audio). Still to decide: does Spanish live
      at its own address (`/es/`) or behind an on-page toggle?
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
- [ ] **Spanish translation** of ~1,100 words of interface copy, plus the transcripts once written (§6)
- [ ] Confirmation of the PROVISIONAL region assignments (§2)
- [ ] **A privacy policy**, or a decision about who writes one — required before collecting email
      addresses, and the site has none today (§4, §8)
- [ ] **Approval** of the media below once delivered

**Media — our purview, client approves** *(not a client deliverable; do not put on their ask list)*
- [ ] 11 presenter videos, final (§1)
- [ ] Landing "Find Your Path" preview clip + poster (§1)
- [ ] Final poster stills (§1)
- [ ] Captions — Premiere SRT export → `scripts/srt2vtt.py` (§1)
- [ ] English transcripts for all 11 videos (§1) — assumed ours as a video-derived asset; correct this
      line if the client is writing them
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
- [ ] 11 presenter videos recorded & final → `video/nodes/<node-key>.mp4`
- [ ] Landing "Find Your Path" preview video — final clip + poster (muted loop; no transcript)
- [ ] Poster stills finalized (placeholders currently in `images/video placeholder stills/`)
- [ ] Switch each node on as its clip lands (`v:1`, plus `cc:1` once its `.vtt` is beside it)
- [ ] Captions (`.srt` → `.vtt`) for all narrated videos
- [ ] **Move transcripts + all interface copy out of `index.html` into data files** — prerequisite for
      BOTH the transcripts and the Spanish version (§6). One job, two payoffs. An apostrophe in inline
      text currently blanks the whole page.
- [ ] Transcripts written for all 11 nodes (Option A) — replace `welcome` lorem-ipsum placeholder
- [ ] Result-page video summaries drafted (Option C) — 7 result pages, from the transcripts
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

## 6. Spanish language version
**Scope confirmed 2026-07-30: text elements only, no re-recorded audio. Client is bilingual and will
supply the translation.** That removes the cost and quality risk; what remains is structural work here
plus a real writing job for them.

Word counts (excludes program/organisation names — proper nouns stay in English):

| Area | Words |
|---|---|
| Landing page + footer | 482 |
| Supplementary Authorization page copy | 203 |
| Additional Resources titles + descriptions | 185 |
| Questionnaire answer buttons | 84 |
| Questionnaire questions | 78 |
| Node labels | 31 |
| Result page titles | 30 |
| **Subtotal to translate now** | **~1,100** |
| Transcripts, once written (11 videos, estimate) | 1,700–3,300 |
| Captions | same text as transcripts, re-timed |

**Why this needs structural work first — "every string is inline".** The site is one file containing
three different things mixed together: the design, the behaviour, and the words. Every question, button
label, heading and paragraph is typed directly into the middle of it. There is no single list of "the
words on this site". So there are only two routes:

- *Duplicate the whole file and translate inside it* — fast to start, but then there are two complete
  sites to maintain forever. Every design change, program update and fix has to be made twice, and the
  day someone forgets, the two versions drift apart. **Not recommended.**
- *Separate the words from the machinery first* — one English list, one Spanish list, one site that
  loads whichever is needed. This is the same job already required for the transcripts (§1), so it gets
  done once and serves both. **Recommended.**

- [ ] ⚠ **Do not start translating until the English copy is final** — otherwise they translate twice.
- [ ] ⚠ **Prerequisite: extract strings from `index.html`** (§1)
- [ ] **Decide the shape:** separate addresses (`/es/`) or an on-page toggle. Separate addresses are
      simpler on GitHub Pages, can be shared directly, and can be found by Spanish-language search.
- [ ] Second caption file per video, matching the Spanish transcripts
- [ ] Region names translate (Northern / Central / Southern / Online); school names do not
- [ ] Set `lang` correctly per page so screen readers pronounce Spanish text properly
- [ ] Ongoing cost to name now: every future copy change has to be made twice, forever

## 7. Hosting — transfer to the client's GitHub, with custom domain
⚠ **Open question first:** is the domain a subdomain of the client's existing site
(`pathways.createca.org`) or a brand-new root domain? A subdomain is one DNS record and cannot disturb
their main site. A root domain needs four records and touches the domain's root. Push for the subdomain
unless they have a reason not to.

**Phase A — before touching anything**
- [ ] Client creates a GitHub **organisation** (not a personal account)
- [ ] Two-factor authentication enabled on it
- [ ] We're added as a member with write access

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
- [ ] The site loads its two typefaces from Google's servers, so Google sees every visitor's address.
      Minor and completely standard, but **self-hosting the two font files** removes the site's only
      current outside dependency and improves visitor privacy. Small job — do it before adding scripts,
      not after.

- [ ] Re-run the full code review after the last third-party script is added, not before

## 9. Launch / general
- [ ] Full QA pass — cross-browser and real devices, not the preview pane
- [ ] Play one real clip through in a normal browser — the preview pane suspends video, so continuous
      playback is the one thing never confirmed on a real file
- [ ] Final content review with the client
- [ ] **Welcome transcript is lorem ipsum** — reachable from the first questionnaire screen via the
      Transcript button. Most user-visible of the placeholder items.
- [ ] Wire the "Civil Cyber Arts" credit link — placeholder `href="#"` in two places (footer + result
      pages). Confirmed still unresolved in the 2026-07-30 code review.
- [ ] Delete unused `images/createca_logo_color.png` (48K; only the `_EDIT` version is referenced)?

### From the 2026-07-27 code inspection — your call, none started
- [ ] **Base text size overrides browser settings** (`html{font-size:20px}`) — people who enlarge their
      default text get overridden. Fixing means re-checking every size sitewide.
- [ ] **Moving content can't be paused** — hero photos crossfade continuously with no stop control;
      neither hero nor quote carousel respects the OS "reduce motion" setting (only the scroll arrow
      does). Quote carousel does pause on hover and has arrows, so it's the milder case.
- [ ] Note for local previews: the site must be served over http (`python3 -m http.server 8765`), not
      opened by double-clicking — the program list can't load from a `file://` page.

---

## Recently completed
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
