#!/usr/bin/env python3
"""Verify that grouping is correct - each namespace family has unique first letter"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

# Read current mapping from index file
index_file = "../chapters/13-AllOps.md"
with open(index_file, 'r', encoding='utf-8') as f:
    content = f.read()

import re
pattern = r'- \[([^\]]+)\]\(([^\)]+)\)'
matches = re.findall(pattern, content)

# Extract first letter from filename
grouping = {}
for namespace, filename in matches:
    # Extract prefix like "13ba" -> "b", "13l" -> "l"
    prefix_match = re.match(r'13([a-z]+)', filename)
    if prefix_match:
        prefix = prefix_match.group(1)
        first_letter = prefix[0]
        
        if first_letter not in grouping:
            grouping[first_letter] = []
        grouping[first_letter].append((namespace, filename, prefix))

# Check for conflicts
print("Current grouping by first letter:")
print("=" * 80)

conflicts = []
for letter in sorted(grouping.keys()):
    namespaces = grouping[letter]
    print(f"\nLetter '{letter}' ({len(namespaces)} files):")
    
    # Group by top-level namespace
    top_level = {}
    for ns, fn, pre in namespaces:
        top = ns.split('.')[1] if '.' in ns else ns.replace('Ops.', '')
        if top not in top_level:
            top_level[top] = []
        top_level[top].append((ns, fn))
    
    if len(top_level) > 1:
        conflicts.append((letter, top_level))
        print(f"  ⚠️  CONFLICT: Multiple top-level namespaces share letter '{letter}':")
        for top, items in sorted(top_level.items()):
            print(f"    - {top}: {len(items)} files")
    else:
        top_name = list(top_level.keys())[0]
        print(f"  ✓ {top_name} family ({len(namespaces)} files)")
        for ns, fn in sorted(items, key=lambda x: x[1])[:3]:
            print(f"      {fn} - {ns}")
        if len(namespaces) > 3:
            print(f"      ... and {len(namespaces) - 3} more")

print()
print("=" * 80)
if conflicts:
    print(f"⚠️  Found {len(conflicts)} conflicts!")
else:
    print("✓ No conflicts - each namespace family has a unique first letter")






