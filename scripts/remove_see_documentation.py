#!/usr/bin/env python3
"""
Remove "*See documentation*" from port descriptions
Change:
  - **X** (Number): *See documentation*
To:
  - **X** (Number):
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')
from pathlib import Path
import re

PROJECT_ROOT = Path(__file__).parent.parent
CHAPTERS_DIR = PROJECT_ROOT / "chapters"

def remove_see_documentation():
    """Remove '*See documentation*' from all op files"""
    
    op_files = list(CHAPTERS_DIR.glob("13-Ops*.md"))
    
    print("=" * 80)
    print("REMOVING '*See documentation*' FROM PORT DESCRIPTIONS")
    print("=" * 80)
    print()
    print(f"Processing {len(op_files)} op files...")
    print()
    
    total_replacements = 0
    files_updated = 0
    
    for op_file in sorted(op_files):
        with open(op_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Replace pattern: "*See documentation*" (with optional whitespace before)
        # This matches:
        # - **X** (Number): *See documentation*
        # and removes the "*See documentation*" part
        pattern = r'(\*\*[^*]+\*\* \([^)]+\):)\s*\*See documentation\*'
        replacement = r'\1'
        
        new_content = re.sub(pattern, replacement, content)
        
        if new_content != original_content:
            count = len(re.findall(pattern, original_content))
            total_replacements += count
            
            with open(op_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            files_updated += 1
            print(f"  Updated {op_file.name}: {count} replacements")
    
    print()
    print("=" * 80)
    print(f"✓ Updated {files_updated} files")
    print(f"✓ Made {total_replacements} total replacements")
    print("=" * 80)

if __name__ == "__main__":
    remove_see_documentation()


