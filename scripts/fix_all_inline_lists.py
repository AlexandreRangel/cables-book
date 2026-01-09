#!/usr/bin/env python3
"""
Comprehensive fix for inline list items - finds cases where labels/text are 
followed by list items on the same line and splits them properly.
"""
import os
import re
from pathlib import Path

def fix_inline_lists(file_path):
    """Fix all inline list patterns."""
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    modified = False
    new_lines = []
    in_code_block = False
    code_block_type = None
    
    for i, line in enumerate(lines):
        # Track code blocks
        if line.strip().startswith('```'):
            if not in_code_block:
                in_code_block = True
                code_block_type = line.strip()[3:].strip()
            else:
                in_code_block = False
                code_block_type = None
            new_lines.append(line)
            continue
        
        # Skip code blocks
        if in_code_block:
            new_lines.append(line)
            continue
        
        # Skip lines that are clearly code/math
        stripped = line.strip()
        if (stripped.startswith('`') or 
            stripped.startswith('//') or
            stripped.startswith('*') and not stripped.startswith('**') or
            'return' in stripped and ' - ' in stripped or
            '=' in stripped and ' - ' in stripped and not ':' in stripped[:30]):
            new_lines.append(line)
            continue
        
        # Pattern: text ending with colon followed by " - item1 - item2"
        # Match: "Label:" or "**Label:**" followed by items
        pattern1 = r'^(.+?)(:\s+-\s+[^-]+(?:\s+-\s+[^-]+)+)$'
        match1 = re.match(pattern1, line.rstrip())
        
        if match1:
            prefix = match1.group(1)
            items_part = match1.group(2)[2:]  # Remove ": " from start
            
            # Split items
            items = [item.strip() for item in items_part.split(' - ') if item.strip()]
            
            if len(items) > 1:
                # Check if prefix looks like a label (not too long, not code)
                if (len(prefix) < 80 and 
                    not prefix.startswith('`') and
                    not re.search(r'[=+\-*/]', prefix[-20:]) and  # No math in last 20 chars
                    not prefix.strip().endswith('://')):  # Not URL
                    
                    new_lines.append(f'{prefix}:\n')
                    new_lines.append('\n')  # Blank line before list
                    for item in items:
                        new_lines.append(f'- {item}\n')
                    modified = True
                    continue
        
        # Pattern: text (no colon) followed by " - item1 - item2"
        # Only if it looks like a label (short, starts with capital, common label words)
        pattern2 = r'^([A-Z][^:]*?)(\s+-\s+[^-]+(?:\s+-\s+[^-]+)+)$'
        match2 = re.match(pattern2, line.rstrip())
        
        if match2:
            prefix2 = match2.group(1).strip()
            items_part2 = match2.group(2)
            
            # Split items
            items2 = [item.strip() for item in items_part2.split(' - ') if item.strip()]
            
            # Only fix if:
            # - Multiple items
            # - Prefix is short and looks like a label
            # - Items don't look like code/math
            if (len(items2) > 1 and 
                len(prefix2) < 60 and
                not prefix2.startswith('`') and
                not re.search(r'[=+\-*/]', prefix2) and
                not any(item.startswith('`') or re.search(r'[=+\-*/]', item) for item in items2[:2])):
                
                # Check if prefix ends with common label words
                label_indicators = ['Options', 'Settings', 'Types', 'Methods', 'Properties', 
                                  'Values', 'Features', 'Examples', 'Notes', 'Tips']
                looks_like_label = any(prefix2.endswith(word) for word in label_indicators)
                
                if looks_like_label or len(prefix2.split()) <= 5:
                    new_lines.append(f'{prefix2}:\n')
                    new_lines.append('\n')
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
        if fix_inline_lists(md_file):
            modified_count += 1
            print(f"Modified: {md_file}")
    
    print(f"\nDone! Modified {modified_count} out of {total_files} files.")

if __name__ == '__main__':
    main()
