#!/usr/bin/env python3
"""
Update the ops per-file LaTeX block to remove the artificial subsection (.1)
so op entries become:
  13.12  (section.subsubsection)
instead of:
  13.1.12 (section.subsection.subsubsection)

Replaces:
  \\stepcounter{subsection}\\setcounter{subsubsection}{0}
with:
  \\OpsSubsubNoSubsectionNumbering\\setcounter{subsubsection}{0}
"""

from __future__ import annotations

import glob
from pathlib import Path


OLD = "\\stepcounter{subsection}\\setcounter{subsubsection}{0}"
NEW = "\\OpsSubsubNoSubsectionNumbering\\setcounter{subsubsection}{0}"


def main() -> int:
    files = sorted(glob.glob("chapters/13-*.md"))
    changed = 0
    for fp in files:
        p = Path(fp)
        s = p.read_text(encoding="utf-8")
        if OLD not in s:
            continue
        p.write_text(s.replace(OLD, NEW), encoding="utf-8", newline="\n")
        changed += 1
    print(f"Updated {changed}/{len(files)} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


