#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Add line breaks before numbered list items after "Setup:" headings.
Fixes patterns like:
  **Setup:**
  1. First item
  2. Second item

To:
  **Setup:**

  1. First item
  2. Second item
"""

import re
from pathlib import Path

CHAPTERS_DIR = Path(__file__).parent.parent / "chapters"


def fix_setup_numbered_lists(content: str) -> str:
    """Remove blank line between Setup: and first numbered item."""
    
    # Pattern: Setup: (with optional **) followed by blank line(s) and then number 1
    # We want: Setup:\n1. (no blank line before 1)
    
    # Match: **Setup:** or Setup: followed by newline(s), then 1.
    # Remove blank lines between Setup: and 1.
    pattern = r'(\*\*Setup:\*\*|Setup:)\n\n+(\d+\.)'
    content = re.sub(pattern, r'\1\n\2', content)
    
    return content


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
            
            # Fix the pattern
            content = fix_setup_numbered_lists(content)
            
            if content != original:
                fp.write_text(content, encoding='utf-8')
                print(f"Fixed: {fp.name}")
                fixed_count += 1
        except Exception as e:
            print(f"Error processing {fp.name}: {e}")
    
    print(f"\nDone. Fixed {fixed_count} file(s).")


if __name__ == "__main__":
    main()

