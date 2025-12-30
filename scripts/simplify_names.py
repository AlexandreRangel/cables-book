#!/usr/bin/env python3
"""
Simplify file names: remove letter suffixes
13a-OpsAnim.md -> 13-OpsAnim.md
13ba-OpsArray.md -> 13-OpsArray.md
etc.

Also rename index: 13-AllOps.md -> 13-_AllOps.md (underscore makes it sort first)
"""

import os
import sys
sys.stdout.reconfigure(encoding='utf-8')
import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
CHAPTERS_DIR = PROJECT_ROOT / "chapters"
OLD_INDEX = CHAPTERS_DIR / "13-AllOps.md"
NEW_INDEX = CHAPTERS_DIR / "13-_AllOps.md"

def get_base_name(namespace):
    """Get base filename part from namespace"""
    name = namespace.replace("Ops.", "")
    return name.replace(".", "")

def read_current_mapping():
    """Read current namespace -> filename mapping from index"""
    if not OLD_INDEX.exists():
        print(f"ERROR: Index file not found: {OLD_INDEX}")
        return {}
    
    with open(OLD_INDEX, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Parse: - [Namespace](filename.md)
    pattern = r'- \[([^\]]+)\]\(([^\)]+\.md)\)'
    matches = re.findall(pattern, content)
    
    mapping = {}
    for namespace, old_filename in matches:
        mapping[namespace] = old_filename
    
    return mapping, content

def generate_new_filenames(current_mapping):
    """Generate new simplified filenames"""
    new_mapping = {}
    rename_map = {}  # old_filename -> new_filename
    
    for namespace, old_filename in current_mapping.items():
        base_name = get_base_name(namespace)
        new_filename = f"13-Ops{base_name}.md"
        new_mapping[namespace] = new_filename
        rename_map[old_filename] = new_filename
    
    return new_mapping, rename_map

def update_index_content(content, new_mapping):
    """Update index content with new filenames"""
    # Replace all filename references
    for namespace, old_filename in current_mapping.items():
        if namespace in new_mapping:
            new_filename = new_mapping[namespace]
            # Replace: - [Namespace](old_filename)
            pattern = rf'- \[{re.escape(namespace)}\]\({re.escape(old_filename)}\)'
            replacement = f'- [{namespace}]({new_filename})'
            content = re.sub(pattern, replacement, content)
    
    return content

def rename_files(rename_map):
    """Rename all op files"""
    renamed = []
    errors = []
    
    for old_name, new_name in sorted(rename_map.items()):
        old_path = CHAPTERS_DIR / old_name
        new_path = CHAPTERS_DIR / new_name
        
        if not old_path.exists():
            errors.append(f"Source file not found: {old_name}")
            continue
        
        if new_path.exists() and old_path != new_path:
            errors.append(f"Target file already exists: {new_name}")
            continue
        
        try:
            if old_path != new_path:
                old_path.rename(new_path)
                renamed.append((old_name, new_name))
                print(f"  Renamed: {old_name} -> {new_name}")
            else:
                print(f"  No change: {old_name}")
        except Exception as e:
            errors.append(f"Error renaming {old_name}: {e}")
    
    return renamed, errors

def main():
    print("=" * 80)
    print("SIMPLIFYING FILE NAMES")
    print("=" * 80)
    print()
    print("Plan:")
    print("  - Remove letter suffixes (13a -> 13, 13ba -> 13, etc.)")
    print("  - Rename index: 13-AllOps.md -> 13-_AllOps.md")
    print()
    
    # Read current mapping
    print("Reading current file mapping...")
    global current_mapping
    current_mapping, index_content = read_current_mapping()
    print(f"  Found {len(current_mapping)} namespaces")
    
    # Generate new filenames
    print("\nGenerating new filenames...")
    new_mapping, rename_map = generate_new_filenames(current_mapping)
    
    print(f"  Will rename {len(rename_map)} files")
    
    # Show sample of changes
    print("\nSample of changes (first 10):")
    for i, (old, new) in enumerate(sorted(rename_map.items())[:10]):
        print(f"  {old:45} -> {new}")
    if len(rename_map) > 10:
        print(f"  ... and {len(rename_map) - 10} more")
    
    print()
    print("=" * 80)
    print("PROCEEDING WITH RENAMING")
    print("=" * 80)
    print()
    
    # Rename op files
    print("Renaming op files...")
    renamed, errors = rename_files(rename_map)
    
    if errors:
        print("\n⚠️  ERRORS:")
        for error in errors:
            print(f"  {error}")
    else:
        print(f"\n✓ Successfully renamed {len(renamed)} files")
    
    # Update index content
    print("\nUpdating index file content...")
    updated_content = update_index_content(index_content, new_mapping)
    
    # Write updated index with new name
    with open(NEW_INDEX, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    print(f"  Created: {NEW_INDEX.name}")
    
    # Delete old index
    if OLD_INDEX.exists():
        OLD_INDEX.unlink()
        print(f"  Deleted: {OLD_INDEX.name}")
    
    print()
    print("=" * 80)
    print("DONE!")
    print("=" * 80)
    print(f"\n✓ Renamed {len(renamed)} op files")
    print(f"✓ Updated index file: {NEW_INDEX.name}")

if __name__ == "__main__":
    main()

