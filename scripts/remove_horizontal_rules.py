#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Remove all horizontal rule lines (---) from markdown files.
Removes lines that are just "---" (with optional whitespace).
"""

import re
from pathlib import Path

CHAPTERS_DIR = Path(__file__).parent.parent / "chapters"


def remove_horizontal_rules(content: str) -> str:
    """Remove all lines that are just horizontal rules (---)."""
    
    lines = content.split('\n')
    result = []
    
    for line in lines:
        # Check if line is just a horizontal rule (--- with optional whitespace)
        if re.match(r'^\s*-{3,}\s*$', line):
            # Skip this line (don't add it to result)
            continue
        result.append(line)
    
    return '\n'.join(result)


def main():
    """Process all chapter markdown files."""
    chapter_files = sorted(CHAPTERS_DIR.glob("*.md"))
    
    if not chapter_files:
        print("No chapter files found.")
        return
    
    fixed_count = 0
    for fp in chapter_files:
        try:
            content = fp.read_text(encoding='utf-8')
            original = content
            
            # Remove horizontal rules
            content = remove_horizontal_rules(content)
            
            if content != original:
                fp.write_text(content, encoding='utf-8')
                print(f"Fixed: {fp.name}")
                fixed_count += 1
        except Exception as e:
            print(f"Error processing {fp.name}: {e}")
    
    print(f"\nDone. Fixed {fixed_count} file(s).")


if __name__ == "__main__":
    main()

