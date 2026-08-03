# Online-availability marking — WORK IN PROGRESS (awaiting client sign-off)

**Status:** All 92 programs researched, then re-verified for delivery *mode*. Client chose a
**two-marker** scheme. **Nothing on the live site yet** — this is the review stage.

**Client's actual request:** in addition to programs already shown as "online only," also
indicate which programs can be taken **in person OR online**. So the live site needs two markers.

## The two markers (live-site plan)
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
