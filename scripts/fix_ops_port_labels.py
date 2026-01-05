#!/usr/bin/env python3
"""
Normalize ops port section headings in chapter 13 markdown files.

Goal (book PDF rendering):
  > Inputs
  < Output

We remove the trailing ":" and the word "Ports" from the headings.
"""

from __future__ import annotations

import glob
from pathlib import Path


REPLACEMENTS: list[tuple[str, str]] = [
    ("**`\\inputsymbol`{=latex} Input Ports:**", "**`\\inputsymbol`{=latex} Inputs**"),
    ("**`\\outputsymbol`{=latex} Output Ports:**", "**`\\outputsymbol`{=latex} Output**"),
    ("**> Input Ports:**", "**> Inputs**"),
    ("**< Output Ports:**", "**< Output**"),
    ("**Input Ports:**", "**Inputs**"),
    ("**Output Ports:**", "**Output**"),
]


def main() -> int:
    files = sorted(glob.glob("chapters/13-*.md"))
    if not files:
        print("No files matched chapters/13-*.md")
        return 0

    changed_files = 0
    total_replacements = 0

    for fp in files:
        p = Path(fp)
        original = p.read_text(encoding="utf-8")
        updated = original

        for a, b in REPLACEMENTS:
            if a in updated:
                total_replacements += updated.count(a)
                updated = updated.replace(a, b)

        if updated != original:
            # enforce LF for pandoc stability across machines
            p.write_text(updated, encoding="utf-8", newline="\n")
            changed_files += 1

    print(f"Updated {changed_files}/{len(files)} files")
    print(f"Replacements applied: {total_replacements}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


