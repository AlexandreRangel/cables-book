#!/usr/bin/env python3
"""
Remove trailing colons from port descriptions
Change:
  - **Port Name** (Type):
To:
  - **Port Name** (Type)
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')
from pathlib import Path
import re

PROJECT_ROOT = Path(__file__).parent.parent
CHAPTERS_DIR = PROJECT_ROOT / "chapters"

def remove_trailing_colons():
    """Remove trailing colons from port description lines"""
    
    op_files = list(CHAPTERS_DIR.glob("13-Ops*.md"))
    
    print("=" * 80)
    print("REMOVING TRAILING COLONS FROM PORT DESCRIPTIONS")
    print("=" * 80)
    print()
    print(f"Processing {len(op_files)} op files...")
    print()
    
    total_replacements = 0
    files_updated = 0
    
    for op_file in sorted(op_files):
        with open(op_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        new_lines = []
        file_replacements = 0
        
        for line in lines:
            # Match lines like: - **Port Name** (Type):
            # and remove the trailing colon (but keep empty lines after)
            if re.match(r'^- \*\*[^*]+\*\* \([^)]+\):\s*$', line):
                # Remove the colon and any trailing whitespace, keep newline
                new_line = re.sub(r'\([^)]+\):\s*$', lambda m: m.group(0).rstrip(':'), line.rstrip()) + '\n'
                new_lines.append(new_line)
                if new_line != line:
                    file_replacements += 1
            else:
                new_lines.append(line)
        
        if file_replacements > 0:
            with open(op_file, 'w', encoding='utf-8') as f:
                f.writelines(new_lines)
            
            total_replacements += file_replacements
            files_updated += 1
            print(f"  Updated {op_file.name}: {file_replacements} replacements")
    
    print()
    print("=" * 80)
    print(f"✓ Updated {files_updated} files")
    print(f"✓ Made {total_replacements} total replacements")
    print("=" * 80)

if __name__ == "__main__":
    remove_trailing_colons()


