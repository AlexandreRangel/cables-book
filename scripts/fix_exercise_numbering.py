#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix exercise numbering: each subsection should restart from 1.
Fixes patterns where numbering continues across subsections.
"""

import re
from pathlib import Path

CHAPTERS_DIR = Path(__file__).parent.parent / "chapters"


def fix_exercise_numbering(content: str) -> str:
    """Fix numbering in exercise sections so each subsection starts from 1."""
    
    lines = content.split('\n')
    result = []
    i = 0
    in_exercises = False
    current_number = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Check if we're entering an Exercises section
        if re.match(r'^##\s+Exercises', line, re.IGNORECASE):
            in_exercises = True
            current_number = 0
            result.append(line)
            i += 1
            continue
        
        # Check if we're leaving the Exercises section (next ## heading)
        if in_exercises and re.match(r'^##\s+', line) and not re.match(r'^##\s+Exercises', line, re.IGNORECASE):
            in_exercises = False
            current_number = 0
            result.append(line)
            i += 1
            continue
        
        # If we're in exercises section
        if in_exercises:
            # Check if this is a subsection heading (###)
            if re.match(r'^###\s+', line):
                # Reset numbering for new subsection
                current_number = 0
                result.append(line)
                i += 1
                # Ensure blank line after subsection heading before list starts
                if i < len(lines):
                    next_line = lines[i] if i < len(lines) else ""
                    # If next line is not blank and not a numbered item, add blank line
                    if next_line.strip() != "" and not re.match(r'^\s*\d+\.', next_line):
                        result.append('')
                continue
            
            # Check if this line starts with a number followed by a period
            # Pattern: start of line, optional whitespace, number, period, space
            match = re.match(r'^(\s*)(\d+)\.(\s+)(.*)$', line)
            if match:
                indent = match.group(1)
                old_number = int(match.group(2))
                space_after = match.group(3)
                rest = match.group(4)
                
                # Increment and use new number
                current_number += 1
                new_line = f"{indent}{current_number}.{space_after}{rest}"
                result.append(new_line)
                i += 1
                continue
        
        # Regular line, just append
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
            
            # Fix the numbering
            content = fix_exercise_numbering(content)
            
            if content != original:
                fp.write_text(content, encoding='utf-8')
                print(f"Fixed: {fp.name}")
                fixed_count += 1
        except Exception as e:
            print(f"Error processing {fp.name}: {e}")
    
    print(f"\nDone. Fixed {fixed_count} file(s).")


if __name__ == "__main__":
    main()

