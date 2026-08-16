# Arts Educator Pathways

An interactive questionnaire that helps people find a route into arts education in California.
Visitors answer a short series of video-led questions and arrive at a result page listing the
training and certification programs that fit them, grouped by region.

**Live site: [artsedpathways.org](https://artsedpathways.org)** — an initiative of
[CREATE CA](https://createca.org/).

---

## How this site is built

There is **no build step, no framework and no package manager**. The site is plain HTML, CSS and
JavaScript, served exactly as it appears in this repository.

Almost all of it is one file, `index.html`, which holds the markup, the stylesheet and the script
inline. That is deliberate: it keeps the whole site in one place for a small team, and it means a
change is live the moment it is pushed. The trade-off is that `index.html` is large, so read the
comments — decisions are documented next to the code that implements them, including several that
look wrong until you read why.

The three standalone pages (`privacy/`, `program-index/`, `subscribed/`) are separate files that
each repeat the small part of the palette they need. **They do not share a stylesheet with
`index.html`** — if a colour changes there, it has to be mirrored by hand.

## Running it locally

Any static file server will do. From the repository root:

```bash
python3 -m http.server 8765 --bind 127.0.0.1
```

Then open <http://localhost:8765>.

Keep `--bind 127.0.0.1`. Without it the server publishes the whole folder to your local network.

Opening `index.html` directly from the filesystem will **not** work — the page fetches its content
from `data/`, and browsers block those requests on `file://`.

## Repository layout

```
index.html            The entire questionnaire: markup, styles and script
privacy/              Privacy policy
program-index/        Filterable table of every program on the site
subscribed/           Where the email confirmation link lands
data/                 Content and program data (see below)
video/                Clips, poster stills, captions and transcripts
images/               Hero photographs and testimonial portraits
fonts/                Self-hosted Open Sans and Bebas Neue
resources/            Four research PDFs linked from the result pages
scripts/              Maintenance tools, not part of the site
CNAME                 Custom domain for GitHub Pages
```

## Where the content lives

Text is kept out of `index.html` wherever a non-developer might need to change it.

| File | Holds |
|---|---|
| `data/content.en.json` | Every piece of interface and questionnaire copy — button labels, questions, answers, result-page summaries, speaker names and titles |
| `data/programs.json` | The program listings: 92 institutions across six discipline lists, each with a name, link and a confidence rating |
| `data/transcripts.es.json` | Spanish transcripts for all 11 videos |

If a wording change is needed, look in `data/content.en.json` first. It is very unlikely to be in
`index.html`.

## Generated files — do not edit these by hand

Two sets of files are produced from sources elsewhere. Editing them directly works until the next
regeneration silently overwrites your change.

- **Caption files (`video/captions/eng/*.vtt`, `esp/*.vtt`)** are converted from the `.srt` exports
  sitting beside them. Premiere Pro is the source of truth and exports SRT only. To change a
  caption, change it in Premiere, re-export, then run:

  ```bash
  python3 scripts/srt2vtt.py video/captions/eng/*.srt
  ```

- **`data/transcripts.es.json`** is kept in step with the text files in `video/transcripts/esp/`.
  There is no script for this one; it is maintained by hand, so change the text file and the JSON
  together.

## The node key rule

The eleven questionnaire videos are identified by a **node key** — `welcome`, `suppAuth`,
`taVsCred`, `cteIntro`, `cteVideo`, `discipline`, `lifeTA`, `mMusic`, `mTheater`, `mDance`, `mArt`.

**One key names four files**, and the site builds those paths at runtime:

```
video/clips/<key>.mp4
video/stills/<key>.jpg
video/captions/eng/<key>.vtt
video/captions/esp/<key>.vtt
```

Two things follow from that, and both have caused real breakage:

- **Filenames are case-sensitive in production.** macOS disks are not, so `cteintro.mp4` resolves
  fine on your machine and 404s on the live site. Match the key exactly.
- **`mTheater` uses the American spelling on purpose.** It is an internal key no visitor ever sees,
  and `index.html` and `data/content.en.json` must agree on it. Everything a visitor reads says
  *theatre*.

Video files are named per node, not per presenter — several presenters appear in more than one.

## Result pages

Seven result pages are rendered from the `PROFILES` map in `index.html`. Each has its own shareable
address, so a result can be sent to someone or bookmarked:

`?pathway=` `supplementary-authorization` · `teaching-artist` · `cte` · `music` · `theatre` ·
`dance` · `visual-art`

Those slugs are public and have been shared. Changing one breaks every link already sent.

## Scripts

Neither script is part of the site. Both are safe to run at any time.

```bash
python3 scripts/srt2vtt.py <files>   # Premiere SRT exports -> WebVTT caption files
python3 scripts/build-scan.py        # reports build status derived from the actual files
```

## Deployment

The site is served by **GitHub Pages** from the default branch. Pushing to `main` publishes it;
there is nothing to build and no deploy step.

`CNAME` holds the custom domain. Everything committed here is published, including files the site
itself never loads — treat the repository as public in the literal sense.

## Third-party code and privacy

The site loads **one** external script: [Plausible](https://plausible.io) for visitor statistics.
It sets no cookies, stores no IP addresses and processes data in the EU. It is named in the privacy
policy, which must be updated in step if it is ever changed or removed.

Nothing else comes from another company. Fonts are self-hosted rather than loaded from Google, and
the email sign-up posts directly to the mailing-list provider rather than embedding their widget —
both so that no outside party sees a visitor who has not chosen to send something. Adding an embed,
a font host, a map or a tag manager would undo that.
