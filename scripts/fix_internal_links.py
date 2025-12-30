#!/usr/bin/env python3
"""Update internal links in op files to reference new index filename"""

import sys
sys.stdout.reconfigure(encoding='utf-8')
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
CHAPTERS_DIR = PROJECT_ROOT / "chapters"

def fix_links():
    op_files = list(CHAPTERS_DIR.glob("13-Ops*.md"))
    
    print("=" * 80)
    print("FIXING INTERNAL LINKS IN OP FILES")
    print("=" * 80)
    print()
    
    updated = 0
    for op_file in op_files:
        with open(op_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Replace old index filename with new one
        content = content.replace('13-AllOps.md', '13-_AllOps.md')
        
        if content != original_content:
            with open(op_file, 'w', encoding='utf-8') as f:
                f.write(content)
            updated += 1
    
    print(f"✓ Updated {updated} files")
    print(f"✓ {len(op_files) - updated} files already correct")
    print()
    print("=" * 80)

if __name__ == "__main__":
    fix_links()

