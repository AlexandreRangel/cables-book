#!/usr/bin/env python3
"""Verify that all files are correctly renamed"""

import sys
sys.stdout.reconfigure(encoding='utf-8')
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
CHAPTERS_DIR = PROJECT_ROOT / "chapters"
INDEX_FILE = CHAPTERS_DIR / "13-_AllOps.md"

def verify():
    # Get all 13-Ops*.md files
    op_files = sorted([f.name for f in CHAPTERS_DIR.glob("13-Ops*.md")])
    
    # Get all 13*.md files
    all_13_files = sorted([f.name for f in CHAPTERS_DIR.glob("13*.md")])
    
    print("=" * 80)
    print("VERIFICATION OF SIMPLIFIED NAMES")
    print("=" * 80)
    print()
    
    print(f"Total 13*.md files: {len(all_13_files)}")
    print(f"  - Op files (13-Ops*.md): {len(op_files)}")
    print(f"  - Index file: {'13-_AllOps.md' if '13-_AllOps.md' in all_13_files else 'NOT FOUND'}")
    print()
    
    # Check index is first alphabetically
    if all_13_files and all_13_files[0] == '13-_AllOps.md':
        print("✓ Index file (13-_AllOps.md) sorts first alphabetically")
    else:
        print(f"⚠️  Index file does not sort first. First file: {all_13_files[0] if all_13_files else 'N/A'}")
    
    # Check for old naming patterns
    old_patterns = [f for f in all_13_files if any(c.isalpha() and f.startswith(f'13{c}-') for c in 'abcdefghijklmnopqrstuvwxyz')]
    if old_patterns:
        print(f"\n⚠️  Found {len(old_patterns)} files with old naming pattern:")
        for f in old_patterns[:10]:
            print(f"    {f}")
    else:
        print("\n✓ No files with old letter-suffix naming found")
    
    # Check all files follow pattern
    invalid = [f for f in op_files if not f.startswith('13-Ops')]
    if invalid:
        print(f"\n⚠️  Found {len(invalid)} op files with invalid pattern:")
        for f in invalid:
            print(f"    {f}")
    else:
        print("✓ All op files follow the 13-Ops*.md pattern")
    
    print()
    print("=" * 80)
    print("✓ Verification complete!")

if __name__ == "__main__":
    verify()


