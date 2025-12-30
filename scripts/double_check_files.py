#!/usr/bin/env python3
"""
Double-check: Verify all files are correctly named and no duplicates exist
"""

import os
import sys
sys.stdout.reconfigure(encoding='utf-8')
import re
from pathlib import Path
from collections import defaultdict

PROJECT_ROOT = Path(__file__).parent.parent
CHAPTERS_DIR = PROJECT_ROOT / "chapters"
INDEX_FILE = CHAPTERS_DIR / "13-AllOps.md"

def analyze_files():
    """Comprehensive analysis of all files"""
    
    # Get all 13*.md files
    all_files = list(CHAPTERS_DIR.glob("13*.md"))
    
    # Get files referenced in index
    with open(INDEX_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    pattern = r'- \[([^\]]+)\]\(([^\)]+\.md)\)'
    index_entries = dict(re.findall(pattern, content))
    
    print("=" * 80)
    print("COMPREHENSIVE FILE ANALYSIS")
    print("=" * 80)
    print()
    
    # Categorize files
    index_files = [f for f in all_files if f.name == "13-AllOps.md"]
    backup_files = [f for f in all_files if "backup" in f.name.lower() or "restored" in f.name.lower()]
    op_files = [f for f in all_files if f.name.startswith("13") and "Ops" in f.name and f.name != "13-AllOps.md"]
    other_13_files = [f for f in all_files if f.name.startswith("13") and f.name not in [p.name for p in op_files + index_files + backup_files]]
    
    print(f"Total 13*.md files: {len(all_files)}")
    print(f"  - Op files (13*-Ops*.md): {len(op_files)}")
    print(f"  - Index file (13-AllOps.md): {len(index_files)}")
    print(f"  - Backup/restored files: {len(backup_files)}")
    if other_13_files:
        print(f"  - Other 13*.md files: {len(other_13_files)}")
    print()
    
    # Check for duplicates in index
    print("Checking for duplicate entries in index...")
    index_filenames = list(index_entries.values())
    filename_counts = defaultdict(int)
    for filename in index_filenames:
        filename_counts[filename] += 1
    
    duplicates = {f: c for f, c in filename_counts.items() if c > 1}
    if duplicates:
        print(f"  ⚠️  Found {len(duplicates)} duplicate filenames in index:")
        for filename, count in duplicates.items():
            print(f"    {filename}: appears {count} times")
    else:
        print("  ✓ No duplicate filenames in index")
    
    # Check namespace to filename mapping
    print("\nChecking namespace to filename mapping...")
    op_files_set = {f.name for f in op_files}
    index_filenames_set = set(index_filenames)
    
    missing_from_files = index_filenames_set - op_files_set
    extra_files = op_files_set - index_filenames_set
    
    if missing_from_files:
        print(f"  ⚠️  {len(missing_from_files)} files in index but don't exist:")
        for f in sorted(missing_from_files):
            print(f"    {f}")
    else:
        print("  ✓ All files in index exist")
    
    if extra_files:
        print(f"  ⚠️  {len(extra_files)} files exist but not in index (OLD/LEFTOVER):")
        for f in sorted(extra_files):
            file_path = CHAPTERS_DIR / f
            size = file_path.stat().st_size
            print(f"    {f} ({size:,} bytes)")
    else:
        print("  ✓ All existing op files are in index")
    
    # Check backup files
    if backup_files:
        print(f"\nBackup/restored files found ({len(backup_files)}):")
        for f in backup_files:
            size = f.stat().st_size
            print(f"  {f.name} ({size:,} bytes)")
        print("  (These can be safely deleted if no longer needed)")
    
    print()
    print("=" * 80)
    
    return extra_files, backup_files

if __name__ == "__main__":
    extra_files, backup_files = analyze_files()
    
    if extra_files or backup_files:
        print("\nSUMMARY:")
        if extra_files:
            print(f"  - {len(extra_files)} old/leftover op files to delete")
        if backup_files:
            print(f"  - {len(backup_files)} backup files to optionally delete")
    else:
        print("\n✓ No cleanup needed - all files are correctly organized!")

