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
landing_is_demo = "demo/demo_questionnaire_preview.mp4" in html
# presenter video wiring: code renders .qv-still images, no <video class="qv-video"> is created
video_wiring_built = "qv-video" in html and re.search(r"<video[^>]*qv-video", html) is not None

# ---- Section 1: video & transcript content ----
S1 = "1. Video & transcript content"
add(S1, DONE if not landing_is_demo else PEND,
    "Landing preview video finalized",
    "still the demo clip (video/demo/demo_questionnaire_preview.mp4)" if landing_is_demo else "replaced")
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
prov = "PROVISIONAL region assignments" in html
add(S2, PEND if prov else DONE, "Region assignments verified",
    "PROVISIONAL flag still present in index.html" if prov else "flag removed")
# "Stay in touch" opt-in. The old check looked for a placeholder BUTTON that no longer exists (the
# band was rebuilt as a form on 2026-07-30, and its copy moved to content.en.json), so it found
# nothing and reported "wired" — green on the one item that must not ship. It now inspects the form
# itself: wired means the address goes somewhere, i.e. a real action= on the form.
# Deliberately biased to under-report. If it is ever wired by some other means this reads PENDING
# when it is actually done; the reverse — green on a form that discards addresses — is the failure
# that mattered.
optin_present = "qv-optin" in html
m_optin = re.search(r"<form[^>]*\boi-form\b[^>]*>", html)
optin_tag = m_optin.group(0) if m_optin else ""
m_action = re.search(r'\baction="([^"]+)"', optin_tag)
m_onsub = re.search(r'\bonsubmit="([^"]*)"', optin_tag)
dead_handler = bool(m_onsub) and m_onsub.group(1).replace(" ", "").rstrip(";") == "returnfalse"
optin_wired = bool(m_action) and not dead_handler
if not optin_present:
    add(S2, INFO, '"Stay in touch" opt-in', "band not on the page")
elif optin_wired:
    add(S2, DONE, '"Stay in touch" opt-in wired', "form posts to " + m_action.group(1))
else:
    add(S2, PEND, '"Stay in touch" opt-in wired',
        "NOT WIRED — accepts an address and silently discards it; must not ship (§4)")
ucla = programs_raw.count("UCLA Extension CTE in Teaching Artistry")
add(S2, DONE if ucla >= 2 else PEND, "UCLA Extension entry resolved",
    "not in program lists (reverted, awaiting client)" if ucla == 0
    else "present in %d list(s)" % ucla)

# ---- Section 3: online-availability ----
S3 = "3. Online-availability marking"
oa_research = os.path.exists(rp("notes", "online-availability-review.json"))
oa_wired = "online-availability" in html or "onlineAvail" in html
add(S3, DONE if oa_wired else PEND, "Marking wired into site",
    ("research ready; " if oa_research else "") + ("wired" if oa_wired else "not wired — awaiting threshold sign-off"))

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
