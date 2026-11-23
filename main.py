#!/usr/bin/env python3
"""Funniest AI Agent Mishap: GTA 6 Launch Week.

Writes one sentence to $MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output):
the funniest true-to-life thing an AI coding agent did while its human
was busy playing GTA 6 on launch week. Pure Python 3 standard library.
"""

import os
import sys

JOKE = (
    "I left my coding agent alone for one GTA 6 mission and came back to "
    "find it had refactored my entire app into a single file called "
    "final_final_FINAL.py \u2014 then deleted the originals to avoid confusion."
)

MAX_CHARS = 240


def validate(text):
    if not text or not text.strip():
        raise ValueError("entry must not be empty or whitespace-only")
    if len(text) > MAX_CHARS:
        raise ValueError("entry exceeds %d characters: %d" % (MAX_CHARS, len(text)))
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return text


def main():
    validate(JOKE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    tmp = target + ".tmp"
    with open(tmp, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE + "\n")
    os.replace(tmp, target)
    return 0


if __name__ == "__main__":
    sys.exit(main())
