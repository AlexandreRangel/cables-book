#!/usr/bin/env python3
"""
Find old/leftover files by comparing what exists vs what's in the index
"""

import os
import sys
sys.stdout.reconfigure(encoding='utf-8')
import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
CHAPTERS_DIR = PROJECT_ROOT / "chapters"
INDEX_FILE = CHAPTERS_DIR / "13-AllOps.md"

def get_files_from_index():
    """Extract all filenames referenced in the index"""
    if not INDEX_FILE.exists():
        print(f"ERROR: Index file not found: {INDEX_FILE}")
        return set()
    
    with open(INDEX_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all markdown links: - [Namespace](filename.md)
    pattern = r'- \[[^\]]+\]\(([^\)]+\.md)\)'
    files_in_index = set(re.findall(pattern, content))
    
    return files_in_index

def get_existing_files():
    """Get all 13*-Ops*.md files that actually exist"""
    existing = set()
    for file_path in CHAPTERS_DIR.glob("13*-Ops*.md"):
        existing.add(file_path.name)
    return existing

def main():
    print("=" * 80)
    print("FINDING OLD/LEFTOVER FILES")
    print("=" * 80)
    print()
    
    # Get files from index
    print("Reading index file...")
    files_in_index = get_files_from_index()
    print(f"  Found {len(files_in_index)} files referenced in index")
    
    # Get existing files
    print("\nScanning chapters directory...")
    existing_files = get_existing_files()
    print(f"  Found {len(existing_files)} existing 13*-Ops*.md files")
    
    # Find files that exist but are NOT in index (these are old/leftover)
    old_files = existing_files - files_in_index
    
    # Find files that are in index but don't exist (missing files - should not happen)
    missing_files = files_in_index - existing_files
    
    print()
    print("=" * 80)
    print("ANALYSIS RESULTS")
    print("=" * 80)
    
    if old_files:
        print(f"\n⚠️  Found {len(old_files)} OLD/LEFTOVER files (exist but not in index):")
        print("-" * 80)
        for old_file in sorted(old_files):
            file_path = CHAPTERS_DIR / old_file
            size = file_path.stat().st_size
            print(f"  {old_file:50} ({size:,} bytes)")
        
        print(f"\n⚠️  These files appear to be old naming and should be deleted.")
    else:
        print("\n✓ No old/leftover files found!")
    
    if missing_files:
        print(f"\n⚠️  Found {len(missing_files)} MISSING files (in index but don't exist):")
        print("-" * 80)
        for missing_file in sorted(missing_files):
            print(f"  {missing_file}")
        print("\n⚠️  These files are referenced in index but don't exist!")
    else:
        print("\n✓ All files referenced in index exist!")
    
    # Show summary of correct files
    correct_files = existing_files & files_in_index
    print(f"\n✓ {len(correct_files)} files are correctly named and in index")
    
    print()
    print("=" * 80)
    
    if old_files:
        print("\nOLD FILES TO DELETE:")
        print("-" * 80)
        total_size = sum((CHAPTERS_DIR / f).stat().st_size for f in old_files)
        for old_file in sorted(old_files):
            print(f"  chapters/{old_file}")
        print(f"\nTotal: {len(old_files)} files, {total_size:,} bytes")
        print("\n⚠️  Review the list above carefully before proceeding with deletion!")

if __name__ == "__main__":
    main()


