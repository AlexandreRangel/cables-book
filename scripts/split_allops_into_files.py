#!/usr/bin/env python3
"""
Split 13-AllOps.md into smaller files by namespace

Creates files like:
- 13a-OpsAnim.md
- 13b-OpsArray.md
- 13c-OpsAudio.md
- etc.

Preserves all content and maintains the original order.
"""

import re
import os
from typing import Dict, List, Tuple

# Get script directory and calculate chapters path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
CHapters_DIR = os.path.join(PROJECT_ROOT, "chapters")
INPUT_FILE = os.path.join(CHapters_DIR, "13-AllOps.md")
BACKUP_FILE = os.path.join(CHapters_DIR, "13-AllOps.md.backup")

def create_namespace_filename(namespace: str, index: int) -> str:
    """Create a filename from namespace like Ops.Anim -> 13a-OpsAnim.md"""
    # Remove "Ops." prefix
    name = namespace.replace("Ops.", "")
    
    # Handle nested namespaces - use main part for filename
    # Ops.Array.PointArray -> OpsArrayPointArray
    # Ops.Gl.ImageCompose -> OpsGlImageCompose
    name = name.replace(".", "")
    
    # Generate suffix (a-z, then aa-zz, etc.)
    if index < 26:
        suffix = chr(ord('a') + index)
    elif index < 52:
        # aa, ab, ..., az
        suffix = 'a' + chr(ord('a') + (index - 26))
    elif index < 78:
        # ba, bb, ..., bz
        suffix = 'b' + chr(ord('a') + (index - 52))
    elif index < 104:
        # ca, cb, ..., cz
        suffix = 'c' + chr(ord('a') + (index - 78))
    else:
        # For even more, use numbers
        suffix = str(index + 1)
    
    return f"13{suffix}-Ops{name}.md"

def parse_markdown_file(filepath: str) -> Tuple[str, Dict[str, str]]:
    """Parse the markdown file and return header and namespace sections"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract header (everything before first namespace section)
    header_match = re.search(r'^(.*?)(?=^## )', content, re.MULTILINE | re.DOTALL)
    header = header_match.group(1) if header_match else ''
    
    # Find all namespace sections
    namespace_sections = {}
    namespace_pattern = r'^## (Ops\.[^\n]+)\n\n(.*?)(?=^## |\Z)'
    
    for ns_match in re.finditer(namespace_pattern, content, re.MULTILINE | re.DOTALL):
        namespace = ns_match.group(1)
        ns_content = ns_match.group(2)
        namespace_sections[namespace] = ns_content
    
    return header, namespace_sections

def create_index_file(header: str, namespace_files: List[Tuple[str, str]]) -> str:
    """Create an index file that links to all namespace files"""
    md = header
    md += "\n**Note:** This reference has been split into multiple files for easier navigation:\n\n"
    
    for namespace, filename in namespace_files:
        # Clean namespace name for display
        display_name = namespace.replace("Ops.", "")
        md += f"- [{namespace}]({filename})\n"
    
    md += "\n---\n\n"
    
    return md

def main():
    print("=" * 60)
    print("Splitting 13-AllOps.md into smaller files")
    print("=" * 60)
    
    # Check if input file exists
    if not os.path.exists(INPUT_FILE):
        print(f"ERROR: Input file not found: {INPUT_FILE}")
        return
    
    # Create backup
    print(f"\nCreating backup: {BACKUP_FILE}")
    import shutil
    shutil.copy2(INPUT_FILE, BACKUP_FILE)
    print("Backup created!")
    
    # Parse the file
    print(f"\nParsing {INPUT_FILE}...")
    header, namespace_sections = parse_markdown_file(INPUT_FILE)
    
    print(f"Found {len(namespace_sections)} namespace sections")
    
    # Sort namespaces (same order as in original file)
    sorted_namespaces = sorted(namespace_sections.keys())
    
    # Create files for each namespace
    namespace_files = []
    
    print(f"\nCreating individual files...")
    for index, namespace in enumerate(sorted_namespaces):
        filename = create_namespace_filename(namespace, index)
        filepath = os.path.join(CHapters_DIR, filename)
        
        # Create content for this namespace file
        content = f"# {namespace}\n\n"
        content += f"*Part of the [All Operators Reference](13-AllOps.md)*\n\n"
        content += "---\n\n"
        content += f"## {namespace}\n\n"
        content += namespace_sections[namespace]
        
        # Write file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        namespace_files.append((namespace, filename))
        print(f"  Created: {filename} ({len(namespace_sections[namespace])} chars)")
    
    # Create updated index file (13-AllOps.md)
    print(f"\nCreating index file: 13-AllOps.md")
    index_content = create_index_file(header, namespace_files)
    
    with open(INPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(index_content)
    
    print("\n" + "=" * 60)
    print("SUCCESS!")
    print("=" * 60)
    print(f"Split into {len(namespace_files)} files")
    print(f"Backup saved to: {BACKUP_FILE}")
    print(f"Original file converted to index: {INPUT_FILE}")
    print("\nFiles created:")
    for namespace, filename in namespace_files:
        print(f"  - {filename}")

if __name__ == "__main__":
    main()

