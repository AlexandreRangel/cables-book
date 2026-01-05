#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Update all op markdown files with actual patch links.
This script:
1. Scrapes patch links from each op page using Playwright
2. Updates the markdown files to use actual links or omit the line if no patches
"""

import os
import sys
import json
import re
from pathlib import Path
from typing import Dict, List

# Ensure UTF-8 output
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
CHAPTERS_DIR = PROJECT_ROOT / "chapters"
DATA_FILE = PROJECT_ROOT / "thorough_ops_data.json"

# Try to import Playwright
try:
    from playwright.sync_api import sync_playwright
    PLAYWRIGHT_AVAILABLE = True
except ImportError:
    PLAYWRIGHT_AVAILABLE = False
    print("WARNING: Playwright not available. Install with: pip install playwright && playwright install chromium")

BASE_URL = "https://cables.gl"


def extract_patch_links(op_url: str) -> List[Dict[str, str]]:
    """Extract patch links from an op page using Playwright"""
    if not PLAYWRIGHT_AVAILABLE:
        return []
    
    patch_links = []
    
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            
            # Use 'domcontentloaded' instead of 'networkidle' for faster loading
            page.goto(op_url, wait_until='domcontentloaded', timeout=30000)
            # Wait for patches section to potentially load
            try:
                page.wait_for_selector('a[href*="/patch/"]', timeout=5000)
            except:
                pass  # Patches might not exist, that's okay
            time.sleep(2)  # Additional wait for any dynamic content
            
            # Look for links with /patch/ in href
            patch_elements = page.query_selector_all('a[href*="/patch/"]')
            
            for elem in patch_elements:
                try:
                    href = elem.get_attribute('href')
                    text = elem.inner_text().strip()
                    
                    if href and '/patch/' in href:
                        # Only accept actual cables.gl patch links
                        # Must be: cables.gl/patch/... or /patch/...
                        # Exclude: YouTube, external docs, GitHub, etc.
                        if any(excluded in href.lower() for excluded in ['youtube.com', 'youtu.be', 'github.com', 'developer.mozilla.org', 'w3.org', '/op/', '/github']):
                            continue
                        
                        # Must be from cables.gl domain or relative path to /patch/
                        if href.startswith('/patch/'):
                            href = f"{BASE_URL}{href}"
                        elif href.startswith('http') and 'cables.gl/patch/' not in href:
                            continue
                        elif not href.startswith('http'):
                            continue
                        
                        # Verify it's actually a patch URL
                        if 'cables.gl/patch/' not in href:
                            continue
                        
                        if text and len(text) > 0:
                            patch_links.append({
                                'name': text[:100],
                                'url': href
                            })
                except:
                    continue
            
            # Also look in "Patches using" sections
            all_sections = page.query_selector_all('section, h2, div')
            for section in all_sections:
                try:
                    text = section.inner_text()
                    if 'Patches using' in text or 'patches using' in text.lower():
                        section_links = section.query_selector_all('a[href]')
                        for link in section_links:
                            try:
                                href = link.get_attribute('href')
                                link_text = link.inner_text().strip()
                                
                                if href and '/patch/' in href:
                                    # Only accept actual cables.gl patch links
                                    if any(excluded in href.lower() for excluded in ['youtube.com', 'youtu.be', 'github.com', 'developer.mozilla.org', 'w3.org', '/op/', '/github']):
                                        continue
                                    
                                    if href.startswith('/patch/'):
                                        href = f"{BASE_URL}{href}"
                                    elif href.startswith('http') and 'cables.gl/patch/' not in href:
                                        continue
                                    elif not href.startswith('http'):
                                        continue
                                    
                                    # Verify it's actually a patch URL
                                    if 'cables.gl/patch/' not in href:
                                        continue
                                    
                                    if not any(p['url'] == href for p in patch_links):
                                        patch_links.append({
                                            'name': link_text[:100] if link_text else 'Patch',
                                            'url': href
                                        })
                            except:
                                continue
                        break
                except:
                    continue
            
            browser.close()
            
    except Exception as e:
        print(f"  Error extracting patches: {e}")
    
    return patch_links


def update_op_file_markdown(filepath: Path, patch_links: List[Dict[str, str]]) -> bool:
    """Update an op markdown file with patch links"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        
        # Find and replace the "Patches Using This Op:" line
        # Pattern 1: **Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "..."
        pattern1 = r'\*\*Patches Using This Op:\*\*\s*\*Search.*?\*\s*\n'
        
        if patch_links and len(patch_links) > 0:
            # Replace with actual patch links
            patch_links_text = ", ".join([f"[{p['name']}]({p['url']})" for p in patch_links])
            replacement = f"**Patches Using This Op:** {patch_links_text}\n\n"
            content = re.sub(pattern1, replacement, content)
        else:
            # Remove the line entirely
            content = re.sub(pattern1, '', content)
        
        # Also handle pattern without the search text (just in case)
        pattern2 = r'\*\*Patches Using This Op:\*\*.*?\n'
        if patch_links and len(patch_links) > 0:
            patch_links_text = ", ".join([f"[{p['name']}]({p['url']})" for p in patch_links])
            replacement = f"**Patches Using This Op:** {patch_links_text}\n\n"
            content = re.sub(pattern2, replacement, content)
        else:
            content = re.sub(pattern2, '', content)
        
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        
        return False
    except Exception as e:
        print(f"  ERROR processing {filepath.name}: {e}")
        return False


def get_op_url_from_file(filepath: Path) -> str:
    """Extract the op URL from a markdown file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Look for Docs: line with URL
        match = re.search(r'\*\*Docs:\*\*\s*\[(https://[^\]]+)\]', content)
        if match:
            return match.group(1)
        
        # Look for Full Name and construct URL
        match = re.search(r'\*\*Full Name:\*\*\s*`([^`]+)`', content)
        if match:
            full_name = match.group(1)
            return f"{BASE_URL}/op/{full_name}"
    except:
        pass
    
    return None


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Update op files with patch links')
    parser.add_argument('--test', action='store_true', help='Test mode: only process first 3 files')
    parser.add_argument('--file', type=str, help='Process only a specific file (e.g., 13-OpsArray.md)')
    args = parser.parse_args()
    
    if not PLAYWRIGHT_AVAILABLE:
        print("ERROR: Playwright is required for this script.")
        print("Install with: pip install playwright")
        print("Then run: playwright install chromium")
        return
    
    print("=" * 80)
    print("UPDATING OP FILES WITH PATCH LINKS")
    print("=" * 80)
    print()
    print("This will:")
    print("  1. Scrape patch links from each op page using Playwright")
    print("  2. Update markdown files with actual patch links")
    print("  3. Omit 'Patches Using This Op:' line if no patches found")
    print()
    
    # Find all op files
    op_files = list(CHAPTERS_DIR.glob("13-Ops*.md"))
    
    if args.file:
        op_files = [f for f in op_files if f.name == args.file]
        if not op_files:
            print(f"File {args.file} not found!")
            return
    elif args.test:
        op_files = sorted(op_files)[:3]
        print("TEST MODE: Processing only first 3 files")
        print()
    
    if not op_files:
        print("No op files found!")
        return
    
    print(f"Found {len(op_files)} op files")
    print("This will take a while as we need to load each page with a browser...")
    print()
    
    updated_count = 0
    patches_found_count = 0
    no_patches_count = 0
    
    for i, op_file in enumerate(sorted(op_files), 1):
        print(f"[{i}/{len(op_files)}] Processing {op_file.name}...")
        
        # Get op URL
        op_url = get_op_url_from_file(op_file)
        if not op_url:
            print(f"  Could not find op URL, skipping")
            continue
        
        # Extract patch links
        patch_links = extract_patch_links(op_url)
        
        if patch_links:
            print(f"  Found {len(patch_links)} patch(es)")
            patches_found_count += 1
        else:
            print(f"  No patches found")
            no_patches_count += 1
        
        # Update the file
        if update_op_file_markdown(op_file, patch_links):
            print(f"  ✓ Updated")
            updated_count += 1
        else:
            print(f"  - No changes needed")
        
        # Rate limiting
        import time
        time.sleep(1)
    
    print()
    print("=" * 80)
    print(f"Processed {len(op_files)} files")
    print(f"Updated {updated_count} files")
    print(f"Found patches for {patches_found_count} ops")
    print(f"No patches for {no_patches_count} ops")
    print("=" * 80)


if __name__ == "__main__":
    import time
    main()

