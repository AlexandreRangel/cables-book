#!/usr/bin/env python3
"""
Remove redundant group heading in ops markdown files that causes duplicate TOC entries:

  # Ops.Foo.Bar        -> section (e.g. 34 Ops.Foo.Bar)
  ## Ops.Foo.Bar       -> subsection (e.g. 34.1 Ops.Foo.Bar)  [redundant]

We delete the duplicated '## ...' heading and (optionally) insert a tiny LaTeX
counter step so subsequent '### OpName' headings keep their familiar numbering.
"""

from __future__ import annotations

import glob
from pathlib import Path


LATEX_COUNTER_STEP = "```{=latex}\n\\stepcounter{subsection}\\setcounter{subsubsection}{0}\n```\n"


def fix_file(path: Path) -> int:
    s = path.read_text(encoding="utf-8")
    lines = s.splitlines(keepends=True)

    if not lines:
        return 0

    # Find first H1 as title
    if not lines[0].startswith("# "):
        return 0

    title = lines[0][2:].strip()
    # Find the first H2 that exactly repeats the title
    h2_idx = None
    for i, line in enumerate(lines[1:], start=1):
        if line.startswith("## ") and line[3:].strip() == title:
            h2_idx = i
            break
        # Stop early if we reached the first op heading already
        if line.startswith("### "):
            break

    if h2_idx is None:
        return 0

    # Remove that duplicated H2 line plus at most one immediate blank line after it
    new_lines = lines[:h2_idx] + lines[h2_idx + 1 :]
    if h2_idx < len(new_lines) and new_lines[h2_idx].strip() == "":
        new_lines.pop(h2_idx)

    # Insert LaTeX counter step where the H2 was removed (keeps numbering stable).
    # Only insert if not already present nearby.
    window = "".join(new_lines[max(0, h2_idx - 2) : min(len(new_lines), h2_idx + 5)])
    if "\\stepcounter{subsection}" not in window:
        new_lines.insert(h2_idx, LATEX_COUNTER_STEP)

    out = "".join(new_lines)
    if out != s:
        path.write_text(out, encoding="utf-8", newline="\n")
        return 1
    return 0


def main() -> int:
    files = sorted(glob.glob("chapters/13-*.md"))
    changed = 0
    for fp in files:
        changed += fix_file(Path(fp))
    print(f"Updated {changed}/{len(files)} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


