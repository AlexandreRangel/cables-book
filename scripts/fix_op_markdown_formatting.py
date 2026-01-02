#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix markdown formatting in op chapter files:
1. Convert image markdown to HTML with 80% width and left alignment
2. Ensure proper line breaks after Input/Output Ports headers
"""

import os
import re
import sys
from pathlib import Path

# Ensure UTF-8 output
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Get script directory and calculate chapters path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
CHAPTERS_DIR = os.path.join(PROJECT_ROOT, "chapters")


def fix_image_markdown(content: str) -> str:
    """Convert HTML img tags back to markdown images (Pandoc handles sizing via LaTeX)"""
    # Pattern: <img src="..." alt="..." style="..." align="..." />
    html_pattern = r'<img\s+src="([^"]+)"\s+alt="([^"]+)"[^>]*/>'
    
    def replace_image(match):
        image_path = match.group(1)
        alt_text = match.group(2)
        # Extract just the op name from alt text (remove " op" suffix)
        op_name = alt_text.replace(" op", "").strip()
        return f'![{op_name} op]({image_path})'
    
    return re.sub(html_pattern, replace_image, content)


def fix_port_headers(content: str) -> str:
    """Ensure proper line breaks after Input/Output Ports headers"""
    # Fix "**> Input Ports:**" followed immediately by content (no newline)
    # Should be: "**> Input Ports:**\n\n" or "**> Input Ports:**\n-"
    content = re.sub(
        r'\*\*> Input Ports:\*\*\s*([^\n-])',
        r'**> Input Ports:**\n\n\1',
        content
    )
    
    # Fix "**< Output Ports:**" followed immediately by content
    content = re.sub(
        r'\*\*< Output Ports:\*\*\s*([^\n-])',
        r'**< Output Ports:**\n\n\1',
        content
    )
    
    # Ensure there's at least one blank line after Input Ports header
    content = re.sub(
        r'\*\*> Input Ports:\*\*\n([^\n])',
        r'**> Input Ports:**\n\n\1',
        content
    )
    
    # Ensure there's at least one blank line after Output Ports header
    content = re.sub(
        r'\*\*< Output Ports:\*\*\n([^\n])',
        r'**< Output Ports:**\n\n\1',
        content
    )
    
    return content


def fix_op_file(filepath: Path) -> bool:
    """Fix formatting in a single op file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            original_content = f.read()
        
        content = original_content
        
        # Fix images
        content = fix_image_markdown(content)
        
        # Fix port headers
        content = fix_port_headers(content)
        
        # Only write if changed
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        
        return False
    except Exception as e:
        print(f"  ERROR processing {filepath.name}: {e}")
        return False


def main():
    print("=" * 80)
    print("FIXING OP MARKDOWN FORMATTING")
    print("=" * 80)
    print()
    print("Fixes:")
    print("  1. Convert HTML img tags to markdown images (LaTeX handles sizing)")
    print("  2. Ensure proper line breaks after Input/Output Ports headers")
    print()
    
    # Find all section 13 op files
    op_files = list(Path(CHAPTERS_DIR).glob("13-Ops*.md"))
    
    if not op_files:
        print("No op files found!")
        return
    
    print(f"Processing {len(op_files)} op files...")
    print()
    
    fixed_count = 0
    
    for op_file in sorted(op_files):
        if fix_op_file(op_file):
            print(f"  Fixed: {op_file.name}")
            fixed_count += 1
    
    print()
    print("=" * 80)
    print(f"Processed {len(op_files)} files")
    print(f"Fixed {fixed_count} files")
    print("=" * 80)


if __name__ == "__main__":
    main()

