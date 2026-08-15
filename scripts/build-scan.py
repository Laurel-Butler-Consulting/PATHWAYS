#!/usr/bin/env python3
"""
PATHWAYS build-status scan (Option 2).

Derives the CURRENT done/pending state of the mechanical build items straight from the real
repo files (index.html, data/programs.json, assets, notes/) — so it can't drift from reality.
Run from anywhere:

    python3 scripts/build-scan.py

Covers only what leaves a detectable trace in the files. Soft items (client sign-offs, design
decisions) live in notes/BUILD-CHECKLIST.md and are not scanned.
"""
import json
import os
import re
import glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def rp(*a):
    return os.path.join(ROOT, *a)


def read(path):
    try:
        with open(rp(path), encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return ""


html = read("index.html")
programs_raw = read("data/programs.json")
# Site copy moved out of index.html on 2026-07-31, so anything looking for TEXT has to read this too.
content_raw = read("data/content.en.json")
try:
    content = json.loads(content_raw) if content_raw else {}
except ValueError:
    content = {}

# Result-page video summaries — client-supplied copy. "placeholder": true means lorem ipsum is live
# on the result pages, which the lorem string-count alone will not reliably catch (only some of the
# placeholder bullets literally begin "Lorem ipsum"). This flag is the authoritative signal.
summaries = content.get("summaries") or {}
summary_items = summaries.get("items") or {}
summary_filled = [k for k, v in summary_items.items() if v]
summary_placeholder = bool(summaries.get("placeholder"))

DONE, PEND, PART, INFO = "DONE", "PENDING", "PARTIAL", "INFO"
MARK = {DONE: "[x]", PEND: "[ ]", PART: "[~]", INFO: " i "}

rows = []  # (section, status, label, detail)


def add(section, status, label, detail=""):
    rows.append((section, status, label, detail))


# ---- Parse questionnaire video nodes (objects that start with `{p:` = presenter) ----
node_starts = [(m.group(1), m.start()) for m in re.finditer(r"\n  (\w+):\{p:", html)]
prof_pos = html.find("PROFILES=")
bodies = {}
for i, (name, s) in enumerate(node_starts):
    e = node_starts[i + 1][1] if i + 1 < len(node_starts) else (prof_pos if prof_pos > s else len(html))
    bodies[name] = html[s:e]

video_nodes = list(bodies.keys())
# index.html holds the node STRUCTURE; the transcript text moved to data/content.en.json on
# 2026-07-31. Reading index.html for it reported 0/11 while all eleven were written and live.
node_text = {k: (v.get("text") or []) for k, v in (content.get("nodes") or {}).items()}
have_text = [n for n in video_nodes if node_text.get(n)]
lorem_nodes = [n for n in video_nodes
               if any("lorem ipsum" in str(t).lower() for t in node_text.get(n) or [])]
real_transcripts = [n for n in have_text if n not in lorem_nodes]
missing_transcripts = [n for n in video_nodes if n not in have_text]

# ---- Video / caption assets ----
vtt_files = glob.glob(rp("**", "*.vtt"), recursive=True)
stills = glob.glob(rp("images", "video placeholder stills", "vp_*.jpg"))
# The landing loop used to be detected by spotting the stand-in demo clip in index.html. That clip
# was removed in the 2026-08-08 folder reorganisation, which would have made this line read GREEN on
# an empty frame. Check the actual files instead: the clip AND its poster have to be on disk.
landing_clip = os.path.exists(rp("video", "clips", "questprev.mp4"))
landing_poster = os.path.exists(rp("video", "stills", "questprev.jpg"))
# presenter video wiring: code renders .qv-still images, no <video class="qv-video"> is created
video_wiring_built = "qv-video" in html and re.search(r"<video[^>]*qv-video", html) is not None

# ---- Section 1: video & transcript content ----
S1 = "1. Video & transcript content"
add(S1, DONE if (landing_clip and landing_poster) else PEND,
    "Landing preview video finalized",
    "video/clips/questprev.mp4 + video/stills/questprev.jpg present"
    if (landing_clip and landing_poster) else
    "missing: " + ", ".join(
        ([] if landing_clip else ["video/clips/questprev.mp4"])
        + ([] if landing_poster else ["video/stills/questprev.jpg"])))
add(S1, DONE if video_wiring_built else PEND,
    "Video-playback wiring built",
    "not built — personas render as stills only" if not video_wiring_built else "present")
n = len(video_nodes)
add(S1, DONE if len(real_transcripts) == n and n else (PART if real_transcripts else PEND),
    "Transcripts written (%d/%d nodes)" % (len(real_transcripts), n),
    ("placeholder(lorem): " + ", ".join(lorem_nodes) + "; " if lorem_nodes else "")
    + ("missing: " + ", ".join(missing_transcripts) if missing_transcripts else "").strip("; "))
add(S1, DONE if vtt_files else PEND,
    "Captions (.vtt) present",
    "%d .vtt file(s)" % len(vtt_files) if vtt_files else "none found")
add(S1, INFO, "Placeholder stills on disk", "%d of 8 personas" % len(stills))
add(S1,
    PEND if (summary_placeholder or not summary_filled) else DONE,
    "Result-page summaries (client copy)",
    ("PLACEHOLDER live on %d of 7 pages — client copy not received" % len(summary_filled))
    if summary_placeholder else
    ("%d of 7 pages have copy" % len(summary_filled) if summary_filled else "none supplied"))

# ---- Section 2: pending client review ----
S2 = "2. Pending client review"
# Region assignments. CLEARED 2026-08-05: every flagged row was resolved — six against evidence
# (headquarters or campus location), two by the client's call that Santa Barbara is Southern.
# ⚠ What this check does NOT mean: the other 84 have still never been checked one by one. They were
# assigned the same way, are mostly self-evident, and nothing is known to be wrong — but "verified"
# is doing more work than the evidence supports. Kept green deliberately, not by oversight.
prov = "PROVISIONAL region assignments" in html
add(S2, PEND if prov else DONE, "Region assignments resolved",
    "PROVISIONAL flag still present in index.html" if prov
    else "flagged rows all resolved 2026-08-05; the remaining 84 were never individually checked")
# "Stay in touch" opt-in.
# History of this check, because it has been wrong in both directions:
#   1. It first looked for a placeholder BUTTON that no longer existed, found nothing, and reported
#      "wired" — green on the one item that must not ship.
#   2. It was then rewritten to require action= on the form. On 2026-08-03 the form was wired to
#      Buttondown via fetch() in a submit handler, which has no action= — so it went red on work
#      that was finished. A status tool that cries wolf gets ignored, which is its own failure.
# It now accepts EITHER route: a real action=, or a submit handler that posts somewhere.
# Still deliberately biased to under-report: a false PENDING costs a second look, a false DONE ships
# a form that silently discards addresses.
optin_present = "qv-optin" in html
m_optin = re.search(r"<form[^>]*\boi-form\b[^>]*>", html)
optin_tag = m_optin.group(0) if m_optin else ""
m_action = re.search(r'\baction="([^"]+)"', optin_tag)
m_onsub = re.search(r'\bonsubmit="([^"]*)"', optin_tag)
dead_handler = bool(m_onsub) and m_onsub.group(1).replace(" ", "").rstrip(";") == "returnfalse"
# Submit handler route: the form calls a function, and that function posts to somewhere off-site.
handler_name = ""
if m_onsub and not dead_handler:
    m_fn = re.match(r"\s*([A-Za-z_$][\w$]*)\s*\(", m_onsub.group(1))
    handler_name = m_fn.group(1) if m_fn else ""
posts_to = ""
if handler_name:
    m_body = re.search(r"function\s+" + re.escape(handler_name) + r"\s*\([\s\S]*?\n\}", html)
    if m_body:
        m_url = re.search(r"fetch\(\s*['\"](https?://[^'\"]+)", m_body.group(0))
        if m_url:
            posts_to = m_url.group(1)
optin_wired = (bool(m_action) and not dead_handler) or bool(posts_to)
if not optin_present:
    add(S2, INFO, '"Stay in touch" opt-in', "band not on the page")
elif optin_wired:
    add(S2, DONE, '"Stay in touch" opt-in wired',
        "form posts to " + (m_action.group(1) if m_action else posts_to))
else:
    add(S2, PEND, '"Stay in touch" opt-in wired',
        "NOT WIRED — accepts an address and silently discards it; must not ship (§4)")
ucla = programs_raw.count("UCLA Extension CTE in Teaching Artistry")
add(S2, DONE if ucla >= 2 else PEND, "UCLA Extension entry resolved",
    "not in program lists (reverted, awaiting client)" if ucla == 0
    else "present in %d list(s)" % ucla)

# ---- Section 3: online-availability ----
S3 = "3. Online-availability marking"
# The delivery data lives on the Program Index (the `d:` field per school), NOT in the research
# JSON, which is a superseded two-category snapshot — see notes/online-availability-README.md.
# ⚠ This check used to look for the STRING "online-availability" anywhere in index.html, which
# matched a CODE COMMENT saying the work was still outstanding. It therefore reported the item as
# done because of a note explaining that it wasn't (found 2026-08-05). Test for the marker actually
# rendering in the program lists instead.
xindex = read(rp("program-index", "index.html"))
oa_categories = sorted(set(re.findall(r'\bd:"([^"]+)"', xindex)))
oa_research = len(oa_categories) >= 4
# Wired = the RESULT pages carry it. A marker on the Program Index alone is not the deliverable.
oa_wired = "PW_DELIVERY" in html or "deliveryMarker" in html
add(S3, DONE if oa_wired else PEND, "Marking on the result pages",
    ("index has %d categories (%s); " % (len(oa_categories), ", ".join(oa_categories)) if oa_research else "")
    + ("wired" if oa_wired else "deliberately NOT on the result pages (2026-08-05) — data is ready; asking the client whether she wants them there at all"))

# ---- Section 4: code-quality signals (mostly done; flags drift here if reintroduced) ----
S4 = "4. Code-quality signals"
add(S4, DONE if "function escapeHTML" in html else PEND, "escapeHTML present")
main_ct = len(re.findall(r"<main\b", html))
add(S4, DONE if main_ct == 1 else PART, "Single <main> landmark", "%d <main> element(s)" % main_ct)
h4_home = len(re.findall(r"<h4", html[:prof_pos] if prof_pos > 0 else html))
add(S4, DONE if h4_home == 0 else PART, "No skipped headings in landing", "%d stray <h4>" % h4_home)
lorem_by_file = {
    "index.html": html.lower().count("lorem ipsum"),
    "data/programs.json": programs_raw.lower().count("lorem ipsum"),
    "data/content.en.json": content_raw.lower().count("lorem ipsum"),
}
lorem_total = sum(lorem_by_file.values())
where = ", ".join("%s:%d" % (f, c) for f, c in lorem_by_file.items() if c)
# Goes PENDING on the summaries placeholder flag as well as on the string count — placeholder copy
# that doesn't happen to start "Lorem ipsum" would otherwise let this line read green while it is live.
add(S4, DONE if (lorem_total == 0 and not summary_placeholder) else PEND,
    "No placeholder copy",
    "; ".join(filter(None, [
        ("lorem ipsum ×%d (%s)" % (lorem_total, where)) if lorem_total else "",
        "result-page summaries flagged placeholder" if summary_placeholder else "",
    ])) or "none found")

# ---- Duplicated data: the two checks below exist because nothing else enforces these ----
# The site has three standalone pages that each carry their OWN copy of the palette, and region is
# held twice (index.html and program-index). Both were verified by hand on 2026-08-03 and were in
# sync — but "someone remembers the comment" is not a mechanism. These turn a silent mismatch into a
# line in this scan. Neither can be fixed by sharing a file without giving every page a second
# network request, which is why the duplication stands.
STANDALONE = ["program-index/index.html", "subscribed/index.html", "privacy/index.html"]
TOKENS = ["--white", "--ice", "--gold", "--blue", "--navy", "--r", "--font-body", "--font-display"]


def tokens_of(src):
    """Read the :root token values a file actually declares."""
    m = re.search(r":root\s*\{(.*?)\}", src, re.S)
    if not m:
        return {}
    body = m.group(1)
    out = {}
    for t in TOKENS:
        mv = re.search(re.escape(t) + r"\s*:\s*([^;]+);", body)
        if mv:
            out[t] = mv.group(1).strip()
    return out


base_tokens = tokens_of(html)
drift = []
for page in STANDALONE:
    src = read(page)
    if not src:
        drift.append("%s: missing" % page)
        continue
    theirs = tokens_of(src)
    for t, v in base_tokens.items():
        if t in theirs and theirs[t] != v:
            drift.append("%s %s=%s (index.html: %s)" % (page, t, theirs[t], v))
add(S4, PEND if drift else DONE, "Palette copies in step",
    "; ".join(drift) if drift else
    "%d tokens match across index.html + %d standalone pages" % (len(base_tokens), len(STANDALONE)))

# Region is declared twice: SCHOOL_REGION in index.html, and r: in program-index's meta table.
# Also checks every program name HAS a region — one without falls into "Unsorted" on the live page.
REGIONS = "Northern California|Southern California|Central California|Online"
region_index = dict(re.findall(r'"([^"]+)":"(%s)"' % REGIONS, html))
region_xidx = dict(re.findall(r'"([^"]+)":\{r:"([^"]+)"', read("program-index/index.html")))
try:
    prog = json.loads(programs_raw) if programs_raw else {}
except ValueError:
    prog = {}
prog_names = {e["name"] for v in prog.values() if isinstance(v, list) for e in v if "name" in e}
no_region = sorted(n for n in prog_names if n not in region_index)
stale = sorted(k for k in region_index if k not in prog_names)
mismatch = sorted("%s (%s vs %s)" % (k, region_index[k], region_xidx[k])
                  for k in set(region_index) & set(region_xidx) if region_index[k] != region_xidx[k])
only_one = sorted(set(region_index) ^ set(region_xidx))
region_problems = (
    (["no region — shows as Unsorted: " + ", ".join(no_region)] if no_region else []) +
    (["region for a name that no longer exists: " + ", ".join(stale)] if stale else []) +
    (["DISAGREE between files: " + ", ".join(mismatch)] if mismatch else []) +
    (["listed in only one file: " + ", ".join(only_one)] if only_one else [])
)
add(S4, PEND if region_problems else DONE, "Region data in step",
    "; ".join(region_problems) if region_problems else
    "%d programs, all mapped, index.html and program-index agree" % len(prog_names))

# ---- Report ----
W = 78
print("=" * W)
print("PATHWAYS build-status scan  (derived from files — soft items are in notes/BUILD-CHECKLIST.md)")
print("=" * W)
counts = {DONE: 0, PEND: 0, PART: 0, INFO: 0}
current = None
for section, status, label, detail in rows:
    if section != current:
        current = section
        print("\n" + section)
    counts[status] += 1
    line = "  %s %s" % (MARK[status], label)
    if detail:
        line += "  — " + detail
    print(line)
print("\n" + "-" * W)
print("Summary: %d done · %d pending · %d partial   (%d nodes: %d transcripts, %d lorem, %d missing)"
      % (counts[DONE], counts[PEND], counts[PART], len(video_nodes),
         len(real_transcripts), len(lorem_nodes), len(missing_transcripts)))
print("=" * W)
