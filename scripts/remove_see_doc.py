#!/usr/bin/env python3
"""Remove ': *See documentation*' from all port descriptions"""

import os
import re
import sys

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except:
        pass

CHAPTERS_DIR = "../chapters"

def main():
    print("=" * 60)
    print("Removing ': *See documentation*' from port descriptions")
    print("=" * 60)
    print()
    
    total_replacements = 0
    files_updated = 0
    
    # Find all 13-Ops*.md files
    for filename in sorted(os.listdir(CHAPTERS_DIR)):
        if filename.startswith('13-Ops') and filename.endswith('.md'):
            filepath = os.path.join(CHAPTERS_DIR, filename)
            
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Count occurrences
            pattern = r': \*See documentation\*'
            count = len(re.findall(pattern, content))
            
            if count > 0:
                # Replace
                new_content = re.sub(pattern, '', content)
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                
                total_replacements += count
                files_updated += 1
                print(f"  {filename}: {count} replacements")
    
    print()
    print("=" * 60)
    print(f"DONE: {total_replacements} replacements in {files_updated} files")
    print("=" * 60)

if __name__ == "__main__":
    main()

