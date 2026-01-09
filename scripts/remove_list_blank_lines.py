#!/usr/bin/env python3
"""
Remove blank lines between consecutive list items in markdown files.
List items should be on separate lines but without blank lines between them.
"""
import os
import re
from pathlib import Path

def remove_blank_lines_between_lists(file_path):
    """Remove blank lines between consecutive list items."""
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    modified = False
    new_lines = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        is_list_item = re.match(r'^(\s*)([-*]|\d+\.)\s+', line)
        
        if is_list_item:
            # Add the list item
            new_lines.append(line)
            i += 1
            
            # Skip blank lines that follow list items if the next line is also a list item
            while i < len(lines):
                next_line = lines[i]
                next_is_blank = next_line.strip() == ''
                next_is_list_item = re.match(r'^(\s*)([-*]|\d+\.)\s+', next_line)
                
                if next_is_blank and i + 1 < len(lines):
                    # Check if the line after the blank is also a list item
                    line_after_blank = lines[i + 1]
                    after_blank_is_list_item = re.match(r'^(\s*)([-*]|\d+\.)\s+', line_after_blank)
                    
                    if after_blank_is_list_item:
                        # Skip this blank line (don't add it)
                        modified = True
                        i += 1
                        continue
                
                # Not a blank line between list items, or end of list
                break
        else:
            # Not a list item, add it normally
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
        if remove_blank_lines_between_lists(md_file):
            modified_count += 1
            print(f"Modified: {md_file}")
    
    print(f"\nDone! Modified {modified_count} out of {total_files} files.")

if __name__ == '__main__':
    main()
