#!/usr/bin/env python3
"""
Add blank lines between consecutive list items in markdown files.
This ensures proper line breaks in PDF output.
"""
import os
import re
from pathlib import Path

def add_line_breaks_to_lists(file_path):
    """Add blank lines between consecutive list items."""
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    modified = False
    new_lines = []
    
    for i, line in enumerate(lines):
        # Check if current line is a list item (starts with - or * or number)
        is_list_item = re.match(r'^(\s*)([-*]|\d+\.)\s+', line)
        
        # Check if previous line was a list item
        if i > 0:
            prev_line = lines[i - 1]
            prev_is_list_item = re.match(r'^(\s*)([-*]|\d+\.)\s+', prev_line)
            
            # If both current and previous are list items
            if is_list_item and prev_is_list_item:
                # Check if there's already a blank line between them
                # Since prev_line is a list item (not blank), we need to check
                # if we've already added a blank line after it
                # The last line we added should be prev_line (since we process sequentially)
                # If the last line in new_lines is not blank, we need to add a blank line
                if len(new_lines) > 0 and new_lines[-1].strip() != '':
                    # Previous line we added wasn't blank, so add blank line before current
                    new_lines.append('\n')
                    modified = True
        
        new_lines.append(line)
    
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
        if add_line_breaks_to_lists(md_file):
            modified_count += 1
            print(f"Modified: {md_file}")
    
    print(f"\nDone! Modified {modified_count} out of {total_files} files.")

if __name__ == '__main__':
    main()
