#!/usr/bin/env python3
"""
Remove Input/Output section headers and placeholder text when there are no actual ports.
Removes sections like:
**`\inputsymbol`{=latex} Inputs**
- *Visit ... for input port details*

or

**`\outputsymbol`{=latex} Output**
- *Visit ... for output port details*
"""

import os
import re
from pathlib import Path

def remove_empty_port_sections(content):
    """Remove empty Input/Output sections (only placeholder text)"""
    lines = content.split('\n')
    result = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Check if this is an Input/Output header
        if re.match(r'\*\*`\\inputsymbol`\{=latex\} Inputs?\*\*', line) or \
           re.match(r'\*\*`\\outputsymbol`\{=latex\} Outputs?\*\*', line):
            # Check if the next non-empty line is a placeholder
            j = i + 1
            while j < len(lines) and lines[j].strip() == '':
                j += 1
            
            if j < len(lines):
                next_line = lines[j]
                # Check if it's a placeholder (Visit ... for ... port details)
                if re.search(r'Visit.*for (?:complete )?(?:input|output) port details', next_line, re.IGNORECASE):
                    # Skip the header and the placeholder line
                    i = j + 1
                    # Also skip any blank lines after the placeholder
                    while i < len(lines) and lines[i].strip() == '':
                        i += 1
                    continue
        
        result.append(line)
        i += 1
    
    return '\n'.join(result)

def process_file(file_path):
    """Process a single markdown file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        new_content = remove_empty_port_sections(content)
        
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
