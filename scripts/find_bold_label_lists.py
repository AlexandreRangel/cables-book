#!/usr/bin/env python3
"""
Find cases where bold labels are followed by descriptions on the same line,
with multiple labels on one line. Shows you where they are so you can fix them manually.
"""
import os
import re
from pathlib import Path

def find_bold_label_lists(file_path):
    """Find bold labels on the same line."""
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    found_cases = []
    
    in_code_block = False
    
    for i, line in enumerate(lines, 1):
        # Track code blocks
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            continue
        
        # Skip code blocks
        if in_code_block:
            continue
        
        # Pattern: **Label:** text **Label2:** text (multiple bold labels on same line)
        # Look for at least 2 bold labels with colons on the same line
        bold_labels = re.findall(r'\*\*[^*]+\*\*:', line)
        
        if len(bold_labels) >= 2:
            # Found multiple bold labels on one line
            found_cases.append({
                'line_num': i,
                'content': line.rstrip()[:150],  # First 150 chars
                'full_line': line.rstrip()
            })
    
    return found_cases

def main():
    """Find all cases in markdown files."""
    chapters_dir = Path('chapters')
    if not chapters_dir.exists():
        print(f"Error: {chapters_dir} directory not found")
        return
    
    md_files = list(chapters_dir.rglob('*.md'))
    total_cases = 0
    
    print("Searching for inline bold labels (multiple **Label:** on same line)...\n")
    
    for md_file in sorted(md_files):
        cases = find_bold_label_lists(md_file)
        if cases:
            print(f"\n{md_file}:")
            for case in cases:
                total_cases += 1
                print(f"  Line {case['line_num']}:")
                print(f"    {case['content']}")
                if len(case['full_line']) > 150:
                    print(f"    ... (truncated, {len(case['full_line'])} chars total)")
    
    if total_cases == 0:
        print("No cases found! All bold labels appear to be properly formatted.")
    else:
        print(f"\n\nFound {total_cases} case(s) that need manual fixing.")
        print("\nTo fix manually:")
        print("1. Put each **Label:** on its own line")
        print("2. Add a blank line after the label")
        print("3. Convert descriptions to list items with '- ' prefix")
        print("4. Add blank line before next label")

if __name__ == '__main__':
    main()
