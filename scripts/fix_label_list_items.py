#!/usr/bin/env python3
"""
Find and fix cases where labels are followed by list items on the same line.
Pattern: "Label: - item1 - item2" or "Label - item1 - item2"
"""
import os
import re
from pathlib import Path

def fix_label_list_items(file_path):
    """Fix labels followed by list items on the same line."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    modified = False
    
    # Pattern 1: "Label:" or "**Label:**" followed by " - item1 - item2"
    # Match bold or regular labels ending with colon
    pattern1 = r'(\*\*[^*]+\*\*:|[A-Za-z][^:\n]*:)\s+-\s+([^-]+(?:\s+-\s+[^-]+)+)'
    
    def replace_func1(match):
        nonlocal modified
        label = match.group(1)
        items_part = match.group(2)
        
        # Split items by " - "
        items = [item.strip() for item in items_part.split(' - ') if item.strip()]
        
        if len(items) > 1:
            modified = True
            # Format: label on one line, blank line, then items
            result = f'{label}\n\n'
            for item in items:
                result += f'- {item}\n'
            return result.rstrip() + '\n'
        return match.group(0)
    
    content = re.sub(pattern1, replace_func1, content, flags=re.MULTILINE)
    
    # Pattern 2: Bold labels without colon: "**Label** - item1 - item2"
    pattern2 = r'(\*\*[^*]+\*\*)\s+-\s+([^-]+(?:\s+-\s+[^-]+)+)'
    
    def replace_func2(match):
        nonlocal modified
        label = match.group(1)
        items_part = match.group(2)
        
        # Split items
        items = [item.strip() for item in items_part.split(' - ') if item.strip()]
        
        # Only fix if it looks like a label (short, not code, not math)
        if len(items) > 1 and len(label) < 50:
            # Check if items don't look like code/math
            first_item = items[0]
            if not (first_item.startswith('`') or 
                   re.search(r'[=+\-*/]', first_item) or
                   first_item.startswith('http')):
                modified = True
                result = f'{label}\n\n'
                for item in items:
                    result += f'- {item}\n'
                return result.rstrip() + '\n'
        return match.group(0)
    
    content = re.sub(pattern2, replace_func2, content, flags=re.MULTILINE)
    
    # Pattern 3: Regular text labels (not bold) followed by items
    # More conservative - only if it ends with colon or common label words
    pattern3 = r'^([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\s*(?:Options|Settings|Features|Types|Methods|Properties|Values|Examples|Notes|Tips|Warning|Important|Note):?)\s+-\s+([^-]+(?:\s+-\s+[^-]+)+)$'
    
    def replace_func3(match):
        nonlocal modified
        label = match.group(1)
        items_part = match.group(2)
        
        items = [item.strip() for item in items_part.split(' - ') if item.strip()]
        
        if len(items) > 1:
            modified = True
            # Ensure label ends with colon
            if not label.endswith(':'):
                label += ':'
            result = f'{label}\n\n'
            for item in items:
                result += f'- {item}\n'
            return result.rstrip() + '\n'
        return match.group(0)
    
    content = re.sub(pattern3, replace_func3, content, flags=re.MULTILINE)
    
    if modified and content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
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
        if fix_label_list_items(md_file):
            modified_count += 1
            print(f"Modified: {md_file}")
    
    print(f"\nDone! Modified {modified_count} out of {total_files} files.")

if __name__ == '__main__':
    main()
