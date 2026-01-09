#!/usr/bin/env python3
"""
Find and fix list items that are on the same line (e.g., "Label: - item1 - item2")
and split them into separate lines with proper formatting.
"""
import os
import re
from pathlib import Path

def fix_inline_list_items(file_path):
    """Fix list items that are on the same line."""
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    modified = False
    new_lines = []
    
    for i, line in enumerate(lines):
        # Pattern: text followed by " - " and then more items with " - "
        # We want to find patterns like:
        # "Label: - item1 - item2 - item3"
        # But avoid code blocks, math expressions, etc.
        
        # Skip code blocks
        if line.strip().startswith('```'):
            new_lines.append(line)
            continue
        
        # Pattern to match: text ending with colon or text, then " - " followed by items
        # Match: "Label:" or "Label" followed by " - item1 - item2"
        pattern = r'^(.+?)(\s+-\s+[^-]+(?:\s+-\s+[^-]+)+)$'
        match = re.match(pattern, line.rstrip())
        
        if match:
            prefix = match.group(1)
            items_part = match.group(2)
            
            # Extract all items (split by " - ")
            items = [item.strip() for item in items_part.split(' - ') if item.strip()]
            
            if len(items) > 1:
                # Check if prefix ends with colon (like "Requirements:")
                if prefix.rstrip().endswith(':'):
                    # Add the prefix with colon
                    new_lines.append(prefix.rstrip() + '\n')
                    new_lines.append('\n')  # Blank line before first item
                    # Add each item on its own line
                    for item in items:
                        new_lines.append(f'- {item}\n')
                    modified = True
                    continue
                else:
                    # Prefix doesn't end with colon, might be a different pattern
                    # Check if first "item" is actually part of the prefix
                    # For now, let's be conservative and only fix clear cases
                    pass
        
        # Also check for patterns like "text - item1 - item2" where text might be a label
        # Pattern: starts with text, has " - " followed by items
        pattern2 = r'^([^:]+?)(\s+-\s+[^-]+(?:\s+-\s+[^-]+)+)$'
        match2 = re.match(pattern2, line.rstrip())
        
        if match2:
            prefix2 = match2.group(1).strip()
            items_part2 = match2.group(2)
            
            # Extract items
            items2 = [item.strip() for item in items_part2.split(' - ') if item.strip()]
            
            # Only fix if we have multiple items and prefix looks like a label
            # (not code, not math, not a URL, etc.)
            if len(items2) > 1 and not prefix2.startswith('`') and not prefix2.startswith('http'):
                # Check if this looks like a label (ends with common label words or is short)
                looks_like_label = (
                    len(prefix2) < 50 and  # Not too long
                    not re.search(r'[=+\-*/]', prefix2) and  # Not math
                    not prefix2.startswith('//') and  # Not comment
                    not prefix2.startswith('*')  # Not markdown emphasis
                )
                
                if looks_like_label:
                    new_lines.append(f'{prefix2}\n')
                    new_lines.append('\n')  # Blank line before first item
                    for item in items2:
                        new_lines.append(f'- {item}\n')
                    modified = True
                    continue
        
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
        if fix_inline_list_items(md_file):
            modified_count += 1
            print(f"Modified: {md_file}")
    
    print(f"\nDone! Modified {modified_count} out of {total_files} files.")

if __name__ == '__main__':
    main()
