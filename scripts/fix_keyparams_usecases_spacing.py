#!/usr/bin/env python3
"""
Pandoc requires a blank line between a paragraph and a list in many cases.

In several chapters we have:

  **Key Parameters:**
  - item

and:

  **Use Cases:**
  - item

Without a blank line after the bold label, Pandoc may treat the list markers as
inline hyphens, producing a single run-on paragraph in the PDF.

This script inserts a blank line after those labels when the next line starts a list.
"""

from __future__ import annotations

import glob
import re
from pathlib import Path


LABEL_RE = re.compile(r"^\s*(\*\*(Key Parameters|Use Cases):\*\*)\s*$")
LIST_ITEM_RE = re.compile(r"^\s*-\s+\S")


def fix_text(text: str) -> tuple[str, int]:
    lines = text.splitlines(keepends=True)
    out: list[str] = []
    changes = 0

    i = 0
    while i < len(lines):
        out.append(lines[i])

        m = LABEL_RE.match(lines[i].rstrip("\r\n"))
        if m and (i + 1) < len(lines):
            next_line = lines[i + 1]
            # If the next line starts a list item and there's no blank line between, insert one.
            if LIST_ITEM_RE.match(next_line) and (lines[i].endswith("\n")):
                # Only insert if the very next line isn't already blank
                if next_line.strip() != "" and (len(out) == 0 or out[-1].strip() != ""):
                    out.append("\n")
                    changes += 1
        i += 1

    return ("".join(out), changes)


def main() -> int:
    files = sorted(glob.glob("chapters/*.md"))
    changed_files = 0
    total_changes = 0

    for fp in files:
        p = Path(fp)
        # Skip image markdown docs under chapters/images
        if "chapters\\images\\" in str(p) or "chapters/images/" in str(p):
            continue

        original = p.read_text(encoding="utf-8")
        updated, changes = fix_text(original)
        if changes:
            p.write_text(updated, encoding="utf-8", newline="\n")
            changed_files += 1
            total_changes += changes

    print(f"Updated files: {changed_files}")
    print(f"Blank lines inserted: {total_changes}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


