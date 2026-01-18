#!/usr/bin/env python3
"""
Combine chapters into a single markdown file for PDF generation.

This is intended to mirror the behavior in `makebook.bat`:
- Optional cover page first (`chapters/0-Cover.md`)
- Chapters 01-12 in a fixed order
- All `chapters/13-*.md` files appended in name order
- Insert `\\pagebreak` before each appended chapter/section file (but not before the cover)
- Replace Obsidian-style image links `![[...]]` with absolute paths
- Replace `.svg)` with `.pdf)` to match SVG-to-PDF conversion
"""

from __future__ import annotations

import os
import re
from pathlib import Path


def _default_image_base_dir() -> Path:
    # User-specific default for macOS; can be overridden via env var.
    # Using a file:// URI later ensures spaces are handled correctly.
    return Path.home() / "Dropbox (Personal)" / "Rangel-Vault" / "Media" / "image"


def _replace_obsidian_images(markdown: str, image_base_dir: Path) -> str:
    """
    Replace `![[filename.png]]` with `![](file:///.../filename.png)`.
    """

    def repl(match: re.Match[str]) -> str:
        filename = match.group(1)
        uri = (image_base_dir / filename).expanduser().resolve().as_uri()
        return f"![]({uri})"

    return re.sub(r"!\[\[([^\]]+)\]\]", repl, markdown)


def main() -> None:
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    chapters_dir = project_root / "chapters"

    # Fixed ordered list (matches makebook.bat PowerShell array)
    ordered = [
        chapters_dir / "01-introduction.md",
        chapters_dir / "02-getting-started.md",
        chapters_dir / "03-2d-graphics.md",
        chapters_dir / "04-3d-graphics.md",
        chapters_dir / "05-texturing.md",
        chapters_dir / "06-shaders-glsl.md",
        chapters_dir / "07-javascript-ops.md",
        chapters_dir / "08-audio-sound.md",
        chapters_dir / "09-animation-timeline.md",
        chapters_dir / "10-interfaces.md",
        chapters_dir / "11-export-deployment.md",
        chapters_dir / "12-video-tutorials.md",
    ]

    cover = chapters_dir / "0-Cover.md"
    section13_files = sorted(chapters_dir.glob("13-*.md"), key=lambda p: p.name)

    parts: list[str] = []

    if cover.exists():
        print("  Adding: chapters/0-Cover.md")
        parts.append(cover.read_text(encoding="utf-8"))
        parts.append("\n\n")

    for f in ordered:
        if f.exists():
            print(f"  Adding: {f.as_posix()}")
            parts.append("\\pagebreak\n\n")
            parts.append(f.read_text(encoding="utf-8"))
            parts.append("\n\n")

    print(f"  Adding {len(section13_files)} section 13 files...")
    for f in section13_files:
        print(f"  Adding: {f.as_posix()}")
        parts.append("\\pagebreak\n\n")
        parts.append(f.read_text(encoding="utf-8"))
        parts.append("\n\n")

    content = "".join(parts)

    # Replace Obsidian wiki-style image links.
    # Can be disabled by setting CABLES_BOOK_SKIP_IMAGE_REWRITE=1
    if os.environ.get("CABLES_BOOK_SKIP_IMAGE_REWRITE") != "1":
        image_base = Path(os.environ.get("CABLES_BOOK_IMAGE_BASE", str(_default_image_base_dir())))
        content = _replace_obsidian_images(content, image_base)

    # Replace .svg) with .pdf) to match conversion step
    content = re.sub(r"\.svg\)", ".pdf)", content)

    out_path = project_root / "temp_combined_book.md"
    out_path.write_text(content, encoding="utf-8")
    print("Done! Created temp_combined_book.md")


if __name__ == "__main__":
    main()

