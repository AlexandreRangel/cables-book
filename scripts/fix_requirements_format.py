#!/usr/bin/env python3
"""
Fix Requirements sections: ensure first list item is on its own line after "Requirements:"
"""
import os
import re
from pathlib import Path

def fix_requirements_format(file_path):
    """Fix Requirements sections to have line break before first list item."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Pattern: "Requirements:" followed by space and dash on same line
    # Match: **Requirements:** - item or Requirements: - item
    pattern = r'(\*\*Requirements:\*\*|\*\*Requirements:\*\*)\s+-\s+([^\n]+)'
    
    def replace_func(match):
        requirements_label = match.group(1)
        first_item = match.group(2)
        # Return with line break before first item
        return f'{requirements_label}\n- {first_item}'
    
    content = re.sub(pattern, replace_func, content)
    
    # Also handle without bold
    pattern2 = r'(Requirements:)\s+-\s+([^\n]+)'
    def replace_func2(match):
        requirements_label = match.group(1)
        first_item = match.group(2)
        return f'{requirements_label}\n- {first_item}'
    
    content = re.sub(pattern2, replace_func2, content)
    
    if content != original_content:
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
        if fix_requirements_format(md_file):
            modified_count += 1
            print(f"Modified: {md_file}")
    
    print(f"\nDone! Modified {modified_count} out of {total_files} files.")

if __name__ == '__main__':
    main()
