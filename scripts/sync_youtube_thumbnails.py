#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Download/cache YouTube thumbnails locally for all ```vid blocks across chapters.

Why: XeLaTeX cannot embed remote images (https://...), so we must materialize
thumbnails as local files referenced by the Pandoc Lua filter.
"""

from __future__ import annotations

import os
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path


if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
CHAPTERS_DIR = PROJECT_ROOT / "chapters"
THUMBS_DIR = CHAPTERS_DIR / "images" / "youtube_thumbs"


VID_BLOCK_RE = re.compile(r"```vid\s*\n([\s\S]*?)\n```", re.MULTILINE)
YOUTUBE_ID_RE = re.compile(
    r"(?:youtu\.be/|youtube\.com/(?:watch\?v=|shorts/|embed/))([A-Za-z0-9_-]{6,})"
)


def extract_youtube_id(url: str) -> str | None:
    m = YOUTUBE_ID_RE.search(url.strip())
    if not m:
        return None
    vid = m.group(1)
    # strip query params if present (youtu.be/ID?...)
    vid = vid.split("?")[0].split("&")[0]
    return vid


def iter_vid_blocks_markdown(md: str):
    for m in VID_BLOCK_RE.finditer(md):
        body = m.group(1)
        lines = [ln.strip() for ln in body.splitlines() if ln.strip()]
        if not lines:
            continue
        url = lines[0]
        yield url


def download(url: str, dest: Path, timeout_s: int = 15) -> bool:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "cables-book/1.0 (+pandoc build)"},
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout_s) as resp:
            data = resp.read()
        dest.write_bytes(data)
        return True
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as e:
        print(f"[thumbs] WARN failed {url} -> {dest.name}: {e}")
        return False


def main() -> int:
    THUMBS_DIR.mkdir(parents=True, exist_ok=True)

    chapter_files = sorted(CHAPTERS_DIR.glob("*.md"))
    if not chapter_files:
        print("[thumbs] No chapter markdown files found.")
        return 1

    ids: set[str] = set()
    for fp in chapter_files:
        md = fp.read_text(encoding="utf-8", errors="replace")
        for url in iter_vid_blocks_markdown(md):
            vid = extract_youtube_id(url)
            if vid:
                ids.add(vid)

    print(f"[thumbs] Found {len(ids)} unique YouTube IDs in ```vid blocks.")

    downloaded = 0
    skipped = 0
    failed = 0

    for vid in sorted(ids):
        dest = THUMBS_DIR / f"{vid}.jpg"
        if dest.exists() and dest.stat().st_size > 0:
            skipped += 1
            continue

        # Try mqdefault (medium quality), fallback to default
        primary = f"https://i.ytimg.com/vi/{vid}/mqdefault.jpg"
        fallback = f"https://i.ytimg.com/vi/{vid}/default.jpg"

        ok = download(primary, dest)
        if not ok:
            ok = download(fallback, dest)

        if ok:
            downloaded += 1
        else:
            failed += 1
            # ensure we don't leave a 0-byte file behind
            if dest.exists() and dest.stat().st_size == 0:
                try:
                    dest.unlink()
                except OSError:
                    pass

        # be polite to YouTube image CDN
        time.sleep(0.05)

    print(
        f"[thumbs] Done. downloaded={downloaded} skipped={skipped} failed={failed} dir={THUMBS_DIR}"
    )
    # Don't hard-fail the build if some thumbs fail; layout still works.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

