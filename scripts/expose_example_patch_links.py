#!/usr/bin/env python3
"""
Replace '**Example Patch:** [Open in Editor](URL)' with '**Example Patch:** URL'
to expose the actual links instead of hiding them behind link text.
"""

import re
import os
from pathlib import Path

def replace_example_patch_links(content):
    """Replace markdown link format with exposed URL."""
    # Pattern: **Example Patch:** [Open in Editor](URL)
    # Replace with: **Example Patch:** URL
    pattern = r'\*\*Example Patch:\*\* \[Open in Editor\]\(([^)]+)\)'
    replacement = r'**Example Patch:** \1'
    return re.sub(pattern, replacement, content)

def process_file(file_path):
    """Process a single markdown file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = replace_example_patch_links(content)
        
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
        return False
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    """Process all markdown files in chapters directory."""
    chapters_dir = Path('chapters')
    if not chapters_dir.exists():
        print(f"Error: {chapters_dir} directory not found")
        return
    
    md_files = list(chapters_dir.glob('*.md'))
    print(f"Found {len(md_files)} markdown files")
    
    modified_count = 0
    for md_file in sorted(md_files):
        if process_file(md_file):
            print(f"Modified: {md_file}")
            modified_count += 1
    
    print(f"\nDone! Modified {modified_count} files.")

if __name__ == '__main__':
    main()
