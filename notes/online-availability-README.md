# Online-availability marking — SUPERSEDED SNAPSHOT, do not work from this file

> ## ⚠ READ THIS FIRST (added 2026-08-05)
>
> **Everything below is the ORIGINAL two-category research and is out of date.** It was written
> before the Program Index existed. Working from it wastes time — it did so on 2026-08-05, when its
> "18 undetermined" and two-category scheme were mistaken for the current position and a problem was
> reconstructed that had already been solved.
>
> **The live data is in `program-index/index.html`** (the `d:` field on each school, ~line 329).
> 91 schools, **four** categories, none unresolved:
>
> | category | count |
> |---|---|
> | In-person only | 35 |
> | Online only | 30 |
> | Hybrid | 18 |
> | In person or online | 8 |
>
> **Hybrid is its own category**, NOT a flavour of "in person or online". Hybrid mixes both by
> design; "in person or online" means the student picks one. The two-category scheme below
> deliberately folded them together — that is the single biggest way this file misleads.
>
> The client supplied determinations for the 18 that this file lists as likely/undetermined, and the
> Index already reflects every one of them. "The Teaching Artist Institute" was dropped as inactive
> and is correctly absent. `University of Phoenix` appears below but is not on the site.
>
> **Still outstanding:** the markers exist on the Program Index but NOT on the result pages, where
> visitors would see them. **Deliberately left off for now (2026-08-05)** — the client is being asked
> whether she wants them on the result pages at all, given the Program Index already carries them and
> the most common category, in-person, is the least informative to label. Do not wire them in until
> she answers. The data is ready, so it is a short job whenever she does.
>
> Keep this file only as the record of how the research was done and the caveats at the bottom,
> which are still worth reading.

**Status (historical):** All 92 programs researched, then re-verified for delivery *mode*. Client
chose a **two-marker** scheme at the time. Nothing was on the live site at that point.

**Client's actual request:** in addition to programs already shown as "online only," also
indicate which programs can be taken **in person OR online**.

## The two markers (SUPERSEDED — four categories now, see the box above)
- **In person or online** — student can choose either format (includes blended / hybrid programs)
- **Online only** — coursework delivered online with no in-person alternative

Programs with neither get no marker (in-person only). "Likely" and "Undetermined" stay unmarked
until confirmed.

## Findings tally (92)
| category | count |
|---|---|
| In person or online | 23 |
| Online only | 26 |
| In-person only | 25 |
| Likely online (unconfirmed) | 4 |
| Undetermined | 14 |

Data: [`online-availability-review.json`](online-availability-review.json) — each row now has
a `category` field (`both` = in person or online, `online_only`, `inperson`, `likely`,
`undetermined`) plus `evidence`, `source`, `confidence`, `pages`.

Review page ("Pathways Programs Cross-Index"):
- Claude artifact (needs Claude account): https://claude.ai/code/artifact/3e71a90d-019b-4fef-a674-e884f00a12c6
- Repo copy for GitHub Pages: `program-index/index.html` → https://zz72z7z7.github.io/PATHWAYS/program-index/ (only live after it's pushed; has noindex). Generator: `scratchpad/gen_review.py` + `build_v2.py`. (Folder renamed from `cross-index/` on 2026-08-03, along with the page's own name.)

## Implementation plan (once approved) — do NOT run until then
School-level markers, so marking a school once shows on every page it appears (the cross-index).
Mirror the existing `†` footnote pattern in `index.html` `listHTML()` (~line 697): render two
distinct markers (e.g. `*` = in person or online, `**` = online only) after the school name, with
a two-line legend. Absence of a marker = "not confirmed online," never "unavailable."

## Caveats to surface
- **CSU East Bay** is **online only** (arts credential = all classes online, no in-person option) —
  not "in person or online," despite the client's expectation.
- A few land in "online only" though the school has a physical campus, because *that specific
  credential* is online-only (e.g. LMU, Alliant, Dominican, most county CTE programs).
- **William Jessup** is "in person or online" but its Single Subject credential is English/Math,
  not arts — questionable whether it belongs on the art/music pages at all.
- Nearly every credential still requires in-person student teaching locally regardless of marker.
