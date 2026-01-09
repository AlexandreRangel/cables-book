#!/usr/bin/env python3
"""
Add blank line before first list item after "Requirements:" header.
"""
import os
import re
from pathlib import Path

def add_blank_line_before_first_list_item(file_path):
    """Add blank line between Requirements: and first list item."""
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    modified = False
    new_lines = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Check if this line contains "Requirements:" (with or without bold)
        if re.search(r'\*\*Requirements:\*\*|Requirements:', line, re.IGNORECASE):
            new_lines.append(line)
            i += 1
            
            # Look for the next non-blank line
            while i < len(lines):
                next_line = lines[i]
                
                # If it's a blank line, keep it and continue
                if next_line.strip() == '':
                    new_lines.append(next_line)
                    i += 1
                    continue
                
                # If it's a list item, ensure there's a blank line before it
                is_list_item = re.match(r'^(\s*)([-*]|\d+\.)\s+', next_line)
                if is_list_item:
                    # Check if the last line we added was blank
                    if len(new_lines) > 0 and new_lines[-1].strip() != '':
                        # Add blank line before first list item
                        new_lines.append('\n')
                        modified = True
                    new_lines.append(next_line)
                    i += 1
                    break
                
                # Not a list item, just add it
                new_lines.append(next_line)
                i += 1
                break
        else:
            new_lines.append(line)
            i += 1
    
    if modified:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        return True
    return False

def main():
    """Process all markdown files in chapters directory."""
    chapters_dir = Path('chapters')
    if not chapters_dir.exists():
        print(f"Error: {chapters_dir} directory not found")
        return
    
    md_files = list(chapters_dir.rglob('*.md'))
    total_files = len(md_files)
    modified_count = 0
    
    print(f"Processing {total_files} markdown files...")
    
    for md_file in md_files:
        if add_blank_line_before_first_list_item(md_file):
            modified_count += 1
            print(f"Modified: {md_file}")
    
    print(f"\nDone! Modified {modified_count} out of {total_files} files.")

if __name__ == '__main__':
    main()
