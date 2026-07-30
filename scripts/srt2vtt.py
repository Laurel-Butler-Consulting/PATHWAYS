#!/usr/bin/env python3
"""
SRT -> WebVTT converter for the questionnaire caption files.

Premiere Pro exports caption sidecars as .srt only; the site's <track> elements need .vtt.
The two formats are the same apart from a `WEBVTT` header and dots instead of commas in the
timestamps, so this is a small, lossless rewrite.

    python3 scripts/srt2vtt.py video/nodes/*.srt      # convert every SRT in the folder
    python3 scripts/srt2vtt.py video/nodes/welcome.srt

Each `<name>.srt` is written out as `<name>.vtt` beside it, so `welcome.srt` lands as
`welcome.vtt` next to `welcome.mp4`. Re-run it after any caption revision.

What it deliberately does NOT do
--------------------------------
* No cue positioning. Captions are drawn by the site's own caption layer (.qv-caps), which
  already sits clear of the Skip/CC/mute row — position hints in the file would be ignored.
* No stripping of Premiere's styling tags. If any are found the file is still written, but
  a warning is printed: the real fix is turning OFF "include SRT styling" at export, not
  patching it up here.

Safety
------
Premiere is the source of truth for caption text — don't hand-edit a .vtt, because the next
run overwrites it. If a .vtt is newer than its .srt (the sign of a hand-edit) the file is
skipped with a warning; pass --force to overwrite anyway.
"""
import argparse
import os
import re
import sys

# 00:00:03,120 --> 00:00:06,480   (also accepts dots, and any trailing cue settings)
TIMING = re.compile(
    r"^(\d{1,3}:\d{2}:\d{2})[,.](\d{1,3})\s*-->\s*(\d{1,3}:\d{2}:\d{2})[,.](\d{1,3})(.*)$"
)
STYLE_TAG = re.compile(r"<(?!/?[biuv][ >/])[^>]+>")   # <font …> etc; VTT allows <b> <i> <u> <v>


def read_text(path):
    """Read the SRT as text, stripping any byte-order mark and coping with legacy encodings.

    A BOM left in front of the WEBVTT header makes browsers reject the whole caption file
    silently, so utf-8-sig (which consumes it) is tried first. Returns (text, note) where
    note is '' for an ordinary UTF-8 file and a short description when something was fixed.
    """
    raw = open(path, "rb").read()
    had_bom = raw.startswith(b"\xef\xbb\xbf")
    for enc in ("utf-8-sig", "utf-8", "cp1252", "latin-1"):
        try:
            text = raw.decode(enc)
        except UnicodeDecodeError:
            continue
        if enc in ("utf-8-sig", "utf-8"):
            return text, ("byte-order mark removed" if had_bom else "")
        return text, "re-encoded from %s" % enc
    return raw.decode("utf-8", "replace"), "unreadable characters replaced"


def convert(text):
    """Return (vtt_text, cue_count, styled_line_count).

    Only timestamp lines are rewritten. Dialogue is passed through untouched — a blanket
    comma->dot replace would turn "Hi, I'm Laurel." into "Hi. I'm Laurel."
    """
    lines = text.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    out, cues, styled = [], 0, 0
    for line in lines:
        m = TIMING.match(line.strip())
        if m:
            start_hms, start_ms, end_hms, end_ms, rest = m.groups()
            out.append("%s.%s --> %s.%s%s" % (start_hms, start_ms.ljust(3, "0"),
                                              end_hms, end_ms.ljust(3, "0"), rest.rstrip()))
            cues += 1
        else:
            if STYLE_TAG.search(line):
                styled += 1
            out.append(line.rstrip())
    body = "\n".join(out).strip("\n")
    return "WEBVTT\n\n" + body + "\n", cues, styled


def main():
    ap = argparse.ArgumentParser(description="Convert Premiere .srt caption sidecars to .vtt")
    ap.add_argument("files", nargs="+", help="one or more .srt files (globs work)")
    ap.add_argument("--force", action="store_true",
                    help="overwrite a .vtt even if it looks hand-edited (newer than its .srt)")
    args = ap.parse_args()

    written = skipped = failed = 0
    for src in args.files:
        name = os.path.basename(src)
        if not src.lower().endswith(".srt"):
            print("  skip  %s — not an .srt" % name)
            skipped += 1
            continue
        if not os.path.isfile(src):
            print("  FAIL  %s — no such file" % name)
            failed += 1
            continue

        dst = src[:-4] + ".vtt"
        text, note = read_text(src)
        vtt, cues, styled = convert(text)
        if not cues:
            print("  FAIL  %s — no timestamps found; is this really an SRT?" % name)
            failed += 1
            continue

        # Only refuse when the existing .vtt is something this script did NOT produce and is
        # newer than the .srt — i.e. genuinely hand-edited. A plain re-run rewrites the same
        # bytes, so it must not trip the guard (or --force becomes a reflex and protects nothing).
        if os.path.exists(dst) and not args.force:
            try:
                existing = open(dst, encoding="utf-8").read()
            except (OSError, UnicodeDecodeError):
                existing = None
            if (existing is not None and existing != vtt
                    and os.path.getmtime(dst) > os.path.getmtime(src)):
                print("  skip  %s — %s was edited by hand and is newer than the .srt.\n"
                      "        Fix the captions in Premiere and re-export, or --force to discard those edits."
                      % (name, os.path.basename(dst)))
                skipped += 1
                continue

        with open(dst, "w", encoding="utf-8", newline="\n") as f:
            f.write(vtt)
        written += 1

        print("  ok    %s -> %s  (%d cue%s)%s"
              % (name, os.path.basename(dst), cues, "" if cues == 1 else "s",
                 "  [%s]" % note if note else ""))
        if styled:
            print("        ⚠ %d line(s) carry styling tags — these render as literal text on the "
                  "page. Re-export with \"include SRT styling\" turned OFF." % styled)

    print("\n%d written · %d skipped · %d failed" % (written, skipped, failed))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
