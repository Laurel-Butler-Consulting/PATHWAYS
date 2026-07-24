# Online-availability marking — WORK IN PROGRESS (awaiting client sign-off)

**Status (2026-07-24):** Research complete for all 92 programs. **Nothing wired into the
live site yet.** On hold while the client reviews and picks the marking threshold.

**Goal (client request):** cross-index the programs across all Pathways pages and mark
which ones can be taken online (e.g. an asterisk).

## What's decided vs. open
- Data source: researched each program from its own published page (+ targeted search). Done.
- OPEN — client must choose the marker threshold:
  - **Online + hybrid (49 programs)** — recommended ("available fully or partially online")
  - Online only (32)
  - Online + hybrid + likely (53) — risks over-claiming; would need visual distinction

## Findings tally (of 92)
| verdict | count |
|---|---|
| online | 32 |
| hybrid | 17 |
| likely | 4 |
| unclear | 14 |
| in-person | 25 |

Data: [`online-availability-review.json`](online-availability-review.json) — each row:
`{name, verdict, confidence(1-5), evidence, source, pages[]}`.
Review page: titled "Pathways Programs Cross-Index" (subject-neutral).
- Claude artifact (needs Claude account): https://claude.ai/code/artifact/3e71a90d-019b-4fef-a674-e884f00a12c6
- Repo copy for GitHub Pages: `cross-index/index.html` → https://zz72z7z7.github.io/PATHWAYS/cross-index/ (no account needed once pushed; has noindex; source generator: scratchpad gen_review.py).

## Implementation plan (once threshold approved) — do NOT run until then
The marker is **school-level**, so marking a school once makes the `*` appear on every
page it's listed on (the cross-index). Mirror the existing `†` footnote pattern.

1. In `data/programs.json`, add an `"online": true` field to entries whose school is in the
   approved set (or add a top-level `onlineSchools` list). Keep it school-consistent.
2. In `index.html` `listHTML()` (~line 697): append `<sup>*</sup>` after the school name
   when online; add a legend line to the `.prog-note` area:
   *"* Offered fully or partially online — coursework only; student teaching/fieldwork is
   completed locally. Confirm current format with the school."*
3. Absence of `*` means **"not confirmed online," NOT "unavailable online."** Word the
   legend so it can't be misread as a definitive negative.

## Caveats to preserve
- Nearly every credential requires in-person student teaching locally even when coursework
  is online — "online" = the coursework, not a 100%-remote credential.
- Delivery formats change term to term — treat the marker as "confirm with the school."
