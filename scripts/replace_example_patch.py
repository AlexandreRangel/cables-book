#!/usr/bin/env python3
"""
Replace "Example Patch:" with "Example:" throughout all chapter files.
"""

import os
import re
from pathlib import Path

def replace_example_patch(content):
    """Replace Example Patch: with Example:"""
    # Replace **Example Patch:** with **Example:**
    content = re.sub(r'\*\*Example Patch:\*\*', '**Example:**', content)
    # Also handle cases without bold (though unlikely)
    content = re.sub(r'Example Patch:', 'Example:', content)
    return content

def process_file(file_path):
    """Process a single markdown file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        new_content = replace_example_patch(content)
        
        if new_content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
        return False
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    """Process all chapter markdown files"""
    chapters_dir = Path('chapters')
    if not chapters_dir.exists():
        print("chapters directory not found")
        return
    
    modified_count = 0
    total_files = 0
    
    for md_file in chapters_dir.glob('*.md'):
        total_files += 1
        if process_file(md_file):
            modified_count += 1
            print(f"Modified: {md_file.name}")
    
    print(f"\nProcessed {total_files} files, modified {modified_count} files")

if __name__ == '__main__':
    main()
