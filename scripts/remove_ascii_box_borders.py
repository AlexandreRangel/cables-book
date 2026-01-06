#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Remove ASCII box drawing borders from code blocks, keeping only the content.
Removes lines that are just borders (starting with + and -, or | with only spaces).
"""

import re
from pathlib import Path

CHAPTERS_DIR = Path(__file__).parent.parent / "chapters"


def is_border_line(line: str) -> bool:
    """Check if a line is just a border (no actual content)."""
    stripped = line.strip()
    
    # Lines that are just + and - or = (horizontal borders)
    # Can have multiple + characters: +----+----+ or +----------------------+
    # Can also end with |: +----+                                       |
    # Match: starts with +, has one or more sequences of -/= followed by +, optional | at end
    if re.match(r'^\+([-=]+\+)+[-=\s]*(\+|[\s]*\|)?$', stripped) or re.match(r'^\+[-=]+[\s]*(\+|[\s]*\|)?$', stripped):
        return True
    
    # Lines that are just | with spaces or nothing (vertical borders)
    # Match: | followed by optional spaces, optional | at end
    if re.match(r'^\|[\s]*\|?$', stripped):
        return True
    
    # Lines that start with | and end with | but are just empty borders
    if stripped.startswith('|') and stripped.endswith('|'):
        content = stripped[1:-1].strip()
        # If it's all spaces or empty, it's a border
        if not content or content.isspace():
            return True
    
    return False


def remove_box_borders(content: str) -> str:
    """Remove ASCII box borders from code blocks."""
    
    lines = content.split('\n')
    result = []
    i = 0
    in_code_block = False
    
    while i < len(lines):
        line = lines[i]
        
        # Track code block state
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            result.append(line)
            i += 1
            continue
        
        # Inside code block
        if in_code_block:
            # Skip pure border lines (no content)
            if is_border_line(line):
                i += 1
                continue
            
            # Remove all | characters from content lines (they're just border markers)
            # But preserve the content structure
            cleaned = line
            # Remove | characters, but preserve spacing
            cleaned = re.sub(r'\s*\|\s*', ' ', cleaned)  # Replace | with space
            cleaned = re.sub(r'\s+', ' ', cleaned)  # Normalize multiple spaces to single space
            # Remove leading/trailing spaces but preserve indentation
            if line.startswith(' '):
                # Preserve original indentation
                indent = len(line) - len(line.lstrip())
                cleaned = ' ' * indent + cleaned.lstrip()
            else:
                cleaned = cleaned.strip()
            
            # Keep content lines (even if empty after cleaning, to preserve spacing)
            result.append(cleaned)
            i += 1
            continue
        
        # Outside code block, keep as is
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
            
            # Remove box borders
            content = remove_box_borders(content)
            
            if content != original:
                fp.write_text(content, encoding='utf-8')
                print(f"Fixed: {fp.name}")
                fixed_count += 1
        except Exception as e:
            print(f"Error processing {fp.name}: {e}")
    
    print(f"\nDone. Fixed {fixed_count} file(s).")


if __name__ == "__main__":
    main()

