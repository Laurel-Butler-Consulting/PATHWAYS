# Questionnaire video — export spec

Export/transcode spec for the 11 node videos. Player is `.qv-window`:
`aspect-ratio:9/16; object-fit:cover; object-position:50% 0` (top-anchored crop).
Static host, no streaming, no build step — what you export is what ships.

## Spec

| | |
|---|---|
| Aspect / resolution | **9:16 exactly, 1080 × 1920** — never letterbox |
| Container / codec | **MP4**, H.264 High L4.0, yuv420p, **faststart** |
| Quality | **VBR 2-pass, 4 Mbps target / 6 max**, keyframe 60 (ffmpeg equivalent: CRF 21) |
| Frame rate | match source (24/30), **constant not variable** |
| Color | **Rec.709 SDR**, limited range, tagged bt709 |
| Audio | **AAC-LC**, 48 kHz, 128 kbps, **−16 LUFS**, ≤ −1.5 dBTP, consistent across all 11 |
| Captions | Export **SRT** (Premiere's only sidecar option) → convert to **WebVTT `.vtt`**, UTF-8, same basename |
| Poster | JPEG 1080 × 1920, q≈80 |

## Check the source first

```bash
ffprobe -v error -select_streams v:0 -show_entries stream=width,height,r_frame_rate,avg_frame_rate,pix_fmt,color_primaries,color_transfer,color_space -of default=nw=1 SOURCE.mov
```

- **Not 9:16?** Crop at export, **from the top** (`y=0`) to match the player. Never pad with bars —
  `object-fit:cover` zooms them.
- **HLG / Dolby Vision / Log?** Tone-map, don't retag. Retagging relabels without converting;
  it shows up washed-out in Safari.
- **Burned-in lower-thirds?** Player chrome covers the bottom ~54 px (Skip/CC/mute) and centre
  (play icon when paused). Reposition in the timeline — the chrome can't move.
- **Variable frame rate?** Premiere conforms VFR on import, but confirm `r_frame_rate` and
  `avg_frame_rate` match on the export. VFR drifts out of A/V sync in Safari specifically.

## Export — Premiere Pro 2026

### First, in the sequence (not at export)

Export mode has no crop tool, so reframing happens on the timeline:

- **Sequence Settings → 1080 × 1920**, square pixels.
- Reframe each clip with **Motion → Position / Scale**. Anchor framing toward the **top** of the
  frame, matching the player's `object-position:50% 0`.
- Keep the bottom ~12% clear of lower-thirds — player chrome sits there.

### Export tab → Media File → Format: **H.264**

Pick **H.264**, not `MPEG4`. Both are MPEG-4 family — H.264 is Part 10 (AVC); the `MPEG4` entry is
legacy Part 2 (DivX/Xvid era), about half as efficient and unreliable in Safari/iOS HTML5 video.
HEVC, AV1 and VP9 all compress better but none is safe as a *sole* source across browsers, and
dual-encoding means 22 files and `<source>` changes to save bandwidth that isn't a problem yet.
(QuickTime/ProRes is for the intermediate master only — never a delivery format.)

Set the values below once, then **save a custom preset** (the icon beside the Preset dropdown) so
all 11 clips are identical. Send to **Media Encoder** to queue them rather than exporting singly.

**Video**

| Control | Value |
|---|---|
| Frame Size | 1080 × 1920 |
| Frame Rate | match source (don't conform 24→30) |
| Field Order | Progressive |
| Aspect | Square Pixels (1.0) |
| Profile | **High** |
| Level | **4.0** |
| Bitrate Encoding | **VBR, 2 pass** |
| Target Bitrate | **3 Mbps** |
| Maximum Bitrate | **5 Mbps** |
| Key Frame Distance | **60** (tick the box to enable the field) |
| Performance | **Software Encoding** — hardware/VideoToolbox is faster but worse per bit |
| Use Maximum Render Quality | on, if scaling from a larger source |

Premiere has no CRF mode; the 3/5 Mbps VBR pair is the equivalent target for this content.

**Lowered from 4/6 on 2026-08-08**, to hold the repository nearer 265 MB than 345 MB (see Repo size
below). The content is the easy case for it — a seated presenter against a plain background barely
changes between frames, and the player never shows a clip above about 375 px wide, so detail lost at
3 Mbps is detail no visitor sees. **The ceiling went to 5, not 4.5, deliberately:** the maximum is
the encoder's allowance for its hardest seconds, and lowering the average makes that headroom matter
more. The places to check a test export are the CTE Intro text graphic (sharp edges show artefacts
first), rapid hand gestures, and smooth gradients on a plainly lit wall.
⚠ Compare a test at the size the SITE uses, not full screen — full screen exaggerates a difference
no visitor will meet.
⚠ `welcome` was exported at 4 Mbps before this change and was left alone. Re-export it only if it is
being re-cut anyway; the saving on its own is about 7 MB.

**Color Management** — set the output/export color space to **Rec. 709**. This is the setting that
handles HLG/Log source correctly. (Exact label placement shifts between releases — verify the tag
afterward, see below.) If source is HDR and color management alone isn't conforming it, Effects →
**SDR Conform** is the fallback.

**Audio**

| Control | Value |
|---|---|
| Audio Format / Codec | AAC / AAC |
| Sample Rate | 48000 Hz |
| Channels | Stereo |
| Bitrate | 128 kbps |
| Audio Quality | High |

**Multiplexer** — Multiplexer: **MP4**, Stream Compatibility: **Standard**.

**Effects** — enable **Loudness Normalization**:
ITU-R BS.1770-3 · Target **−16 LUFS** · Max True Peak **−1.5 dBTP** · leave Tolerance at default.
Leave every other Effects toggle off (Lumetri Look/LUT, overlays, Video Limiter, Time Tuner).

**Captions** — if captions exist on the timeline: Export Options → **Create Sidecar File**.
Premiere only offers **SubRip (.srt)** here — it has no WebVTT sidecar option — so export SRT and
convert. Turn **"include SRT styling" OFF**: it embeds formatting tags that render as literal text
on the page. Don't burn in.

The site's `<track>` elements need `.vtt`. The two formats differ only by a `WEBVTT` header and
dots instead of commas in the timestamps, so conversion is lossless:

```bash
python3 scripts/srt2vtt.py video/captions/eng/*.srt
```

Writes each `.vtt` beside its `.srt` — so the output keeps the dated export name and then gets
**renamed to the node key**, which is what the site loads (see Naming below). Re-run after any
caption revision. It leaves dialogue commas
alone (a blanket comma→dot replace would mangle the text), strips the byte-order mark Premiere
sometimes writes — which silently invalidates the whole caption file — and warns if styling tags
came through. Keep Premiere as the source of truth: don't hand-edit a `.vtt`, since the next run
overwrites it.

**Don't add cue positioning.** The site draws captions in its own layer, already clear of the
Skip/CC/mute row, so position hints in the file are ignored. Plain cues are what's wanted.

### The one thing Premiere can't do: faststart

Premiere exposes no moov-atom / web-optimize control, and without it the browser downloads the
whole file before painting frame one. Check, and remux if needed — `-c copy` is lossless and takes
seconds:

```bash
ffmpeg -i IN.mp4 -c copy -movflags +faststart OUT.mp4
```

`brew install ffmpeg` — not installed on this machine.

## Verify (once on clip 1, then spot-check)

```bash
head -c 2048 OUTPUT.mp4 | strings | grep -m1 -E 'moov|mdat'
```
`moov` → faststart correct. `mdat` → whole file downloads before first frame.

```bash
ffprobe -v error -select_streams v:0 -show_entries stream=profile,pix_fmt,r_frame_rate,avg_frame_rate,color_primaries,color_transfer,color_space -of default=nw=1 OUTPUT.mp4
```
Frame rates should match (CFR); all three color fields `bt709`, not `unknown`/`bt2020nc`/`arib-std-b67`.
Then play it in **Safari** — that's where color and VFR problems surface.

## Also

- **Playback starts muted** (browsers block autoplay with sound), so opening seconds are silent for
  most viewers and captions are the main comprehension path — plus WCAG 1.2.2. The CC button is
  wired and appears only on nodes that have a `.vtt`. It currently defaults to **off**
  (`PW_CC`, index.html) — worth revisiting given playback starts silent.
- **Repo size** — git keeps every version of every file forever, and video cannot be stored as
  differences: each re-export is kept whole, alongside the old ones. Deleting a clip later frees
  nothing. The 11 transcripts run ~2,250 words ≈ **11–12 minutes of finished video**; at 3 Mbps
  (~22 MB/min) that is roughly **265 MB** committed permanently, against ~345 MB at the old 4 Mbps.
  **Commit only the cut you intend to keep** — three passes at a 28 MB clip costs 84 MB forever,
  and that is the largest avoidable waste here. GitHub refuses any single file >100 MB (no clip is
  close) and warns on repositories over 1 GB. Undoing it later means rewriting history, which breaks
  every existing clone — including every dated build folder — so the decision is effectively
  one-way once pushed.
- **CDN later?** Cross-origin `.vtt` needs CORS headers *and* `crossorigin` on `<video>`, or
  captions break silently. Video itself is fine cross-origin.

## Where the files go — reorganised 2026-08-08

Four folders under `video/`, one kind of file in each. Nothing sits "beside the clip" any more.

```
video/clips/welcome.mp4            the film
video/stills/welcome.jpg           its poster
video/captions/eng/welcome.vtt     English captions   (+ the dated .srt they came from)
video/captions/esp/welcome.vtt     Spanish subtitles
video/transcripts/eng|esp/         transcript text, read into data/transcripts.*.json
```

The landing loop is not a node and has no node key; it is named `questprev` and lives in the same
two folders — `video/clips/questprev.mp4`, `video/stills/questprev.jpg`.

## Naming

Name each file after its **node**, not its presenter — there are 11 videos but only 8 presenters
(Laurel and Ricky each carry three separate clips), so persona basenames would collide. No spaces
(the placeholder-stills folder needs `%20` — standing papercut).

**Premiere export names are not site filenames.** Exports carry a number and a date —
`01_welcome_260806.mp4` — and that is right for the source files: it keeps a visible link between a
clip and the caption file cut from the same version. But the site addresses everything by node key,
so **the copy that goes into the folders above is renamed**: `welcome.mp4`, `welcome.jpg`,
`welcome.vtt`. The dated `.srt` stays as it is, in `video/captions/eng/`, as the record of which
export the captions came from.

Settled 2026-08-08. The alternative — teaching the site the dated names — needs a lookup table of
11 clips and 22 caption files, re-edited on every re-export, and a stale entry fails **silently**:
the node drops back to its placeholder still and nothing reports a problem.

| Basename | Video | Presenter |
|---|---|---|
| `welcome` | Welcome | Laurel & Ricky |
| `taVsCred` | Teaching Artist vs. Credentialed Teacher | Laurel |
| `discipline` | Choosing a Discipline | Laurel / Ricky |
| `lifeTA` | Life of a Teaching Artist | Laurel |
| `cteIntro` | The CTE Certificate | Ricky |
| `cteVideo` | The CTE Pathway | Tiffany |
| `suppAuth` | Supplementary Authorization | Chris |
| `mMusic` | Teaching Music | Matthew |
| `mTheater` | Teaching Theater | Eric |
| `mDance` | Teaching Dance | Lindsay |
| `mArt` | Teaching Visual Art | Kristin |

Dropping the file in doesn't switch it on by itself — each node is enabled in `index.html` with
`v:1` on its `NODES` entry, plus `cc:['en']` (or `cc:['en','es']`) once the caption files are in
`video/captions/`. Until then the node keeps rendering its placeholder still, and a `v:1` with no
file falls back to the still rather than showing a broken player.

## Landing loop (`.fyp-loop`) — differs

Muted forever and autoplaying: **uncheck Export Audio** entirely, encode harder (target
**1.5–2 Mbps**), trim so first and last frame match. Keep its poster current.

Named `questprev`, not by node key — it isn't a node. ⚠ **It has no fallback.** The stand-in demo
clip that used to cover this frame was removed on 2026-08-08, so if `video/clips/questprev.mp4` or
`video/stills/questprev.jpg` is missing or misnamed, the landing page shows an empty frame. This is
the first thing anyone sees; `build-scan.py` checks both files exist.

## Why 1080 × 1920

Peak render is ~1320 × 2347 device px (DPR-3 phone, full-bleed); tablet 1000 × 1778, desktop
900 × 1600. 1080 upscales ~1.22× on top-tier phones — imperceptible on a talking head.
1440 × 2560 kills that upscale at ~1.7× the file size; not worth it against the repo-size limit.
