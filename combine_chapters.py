#!/usr/bin/env python3
"""Combine all chapters into a single markdown file for PDF generation."""

import os
import re

chapters = [
    'chapters/01-introduction.md',
    'chapters/02-getting-started.md',
    'chapters/03-2d-graphics.md',
    'chapters/04-3d-graphics.md',
    'chapters/05-texturing.md',
    'chapters/06-shaders-glsl.md',
    'chapters/07-javascript-ops.md',
    'chapters/08-audio-sound.md',
    'chapters/09-animation-timeline.md',
    'chapters/10-interfaces.md',
    'chapters/11-export-deployment.md',
    'chapters/12-video-tutorials.md',
    'chapters/13-AllOps.md',
]

# Start with title page
content = """# The Cables.gl Book

#### Alexandre Rangel, 2025

---

"""

# Combine chapters
for chapter in chapters:
    if os.path.exists(chapter):
        print(f"  Adding: {chapter}")
        content += "\\pagebreak\n\n"
        with open(chapter, 'r', encoding='utf-8') as f:
            content += f.read()
        content += "\n\n"
    else:
        print(f"  MISSING: {chapter}")

# Convert wiki-link images to full paths
content = re.sub(
    r'!\[\[([^\]]+)\]\]',
    r'![](C:/Dropbox/Rangel-Vault/Media/image/\1)',
    content
)

# Write output with UTF-8 encoding (no BOM)
with open('temp_combined_book.md', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done! Created temp_combined_book.md")

