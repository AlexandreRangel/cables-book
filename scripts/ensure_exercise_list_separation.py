#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ensure proper separation between exercise subsections and their numbered lists.
Adds blank line between subsection heading and list to ensure Pandoc treats them as separate lists.
"""

import re
from pathlib import Path

CHAPTERS_DIR = Path(__file__).parent.parent / "chapters"


def ensure_list_separation(content: str) -> str:
    """Ensure blank line between subsection headings and numbered lists in exercises."""
    
    lines = content.split('\n')
    result = []
    i = 0
    in_exercises = False
    
    while i < len(lines):
        line = lines[i]
        
        # Check if we're entering an Exercises section
        if re.match(r'^##\s+Exercises', line, re.IGNORECASE):
            in_exercises = True
            result.append(line)
            i += 1
            continue
        
        # Check if we're leaving the Exercises section
        if in_exercises and re.match(r'^##\s+', line) and not re.match(r'^##\s+Exercises', line, re.IGNORECASE):
            in_exercises = False
            result.append(line)
            i += 1
            continue
        
        # If we're in exercises section
        if in_exercises:
            # Check if this is a subsection heading (###)
            if re.match(r'^###\s+', line):
                result.append(line)
                i += 1
                # Check next line - if it's a numbered list item, add blank line
                if i < len(lines):
                    next_line = lines[i]
                    if re.match(r'^\s*\d+\.', next_line):
                        # Add blank line between heading and list
                        result.append('')
                continue
        
        result.append(line)
        i += 1
    
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
            
            # Ensure proper separation
            content = ensure_list_separation(content)
            
            if content != original:
                fp.write_text(content, encoding='utf-8')
                print(f"Fixed: {fp.name}")
                fixed_count += 1
        except Exception as e:
            print(f"Error processing {fp.name}: {e}")
    
    print(f"\nDone. Fixed {fixed_count} file(s).")


if __name__ == "__main__":
    main()


