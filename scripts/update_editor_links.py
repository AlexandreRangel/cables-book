#!/usr/bin/env python3
"""
Update Editor Links in Markdown

This script updates the "Example Patch" links in the AllOps.md file
to use the actual "Open in Editor" links from cables.gl instead of
the placeholder links.

It extracts editor URLs (like https://cables.gl/edit/vtPZ7i) from
each op page and updates the markdown accordingly.
"""

import json
import os
import re
import sys
import time
from pathlib import Path

# Fix encoding for Windows
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except:
        pass

try:
    from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout
    PLAYWRIGHT_AVAILABLE = True
except ImportError:
    PLAYWRIGHT_AVAILABLE = False
    print("WARNING: Playwright not installed. Run: pip install playwright && playwright install chromium")

# Configuration
BASE_URL = "https://cables.gl"
CHAPTERS_DIR = "../chapters"
PAGE_LOAD_WAIT = 3
REQUEST_DELAY = 1.0
PAGE_TIMEOUT = 30000


def extract_editor_url_from_page(page, op_url: str) -> str:
    """Extract the editor URL from an op page"""
    try:
        page.goto(op_url, wait_until='domcontentloaded', timeout=PAGE_TIMEOUT)
        time.sleep(PAGE_LOAD_WAIT)
        
        # Find all links on the page
        links = page.query_selector_all('a[href]')
        for link in links:
            href = link.get_attribute('href') or ''
            # Check if it's an editor link (pattern: /edit/[alphanumeric])
            if '/edit/' in href:
                # Make it absolute if relative
                if href.startswith('/'):
                    editor_url = f"{BASE_URL}{href}"
                elif not href.startswith('http'):
                    editor_url = f"{BASE_URL}/{href}"
                else:
                    editor_url = href
                return editor_url
    except Exception as e:
        print(f"    Error extracting editor URL: {e}")
    
    return ''


def find_all_op_files() -> list:
    """Find all namespace op files (13-Ops*.md)"""
    op_files = []
    chapters_path = Path(CHAPTERS_DIR)
    if chapters_path.exists():
        for filepath in chapters_path.glob("13-Ops*.md"):
            op_files.append(filepath)
    return sorted(op_files)


def parse_op_file(filepath: str) -> tuple:
    """Parse an op file and extract op sections with their URLs"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all op sections
    # Pattern: ### OpName ... **Docs:** [url](url)
    op_sections = {}
    op_urls = []
    
    # Find all op sections (### OpName ... until next ### or ##)
    op_pattern = r'^### (\w+)\n(.*?)(?=^### |^## |\Z)'
    
    for match in re.finditer(op_pattern, content, re.MULTILINE | re.DOTALL):
        op_name = match.group(1)
        op_content = match.group(2)
        
        # Extract URL from "**Docs:** [url](url)"
        url_match = re.search(r'\*\*Docs:\*\*\s*\[([^\]]+)\]\(([^)]+)\)', op_content)
        if url_match:
            url = url_match.group(2)
            op_urls.append((op_name, url, match.start(), match.end()))
            op_sections[op_name] = {
                'content': op_content,
                'start': match.start(),
                'end': match.end(),
                'url': url
            }
    
    return content, op_sections, op_urls


def update_op_section_in_content(content: str, op_name: str, editor_url: str) -> str:
    """Update the Example Patch link in an op section"""
    # Find the Example Patch line for this specific op and update it
    # Current: **Example Patch:** [Open in Editor](old_url)
    # New: **Example Patch:** [Open in Editor](editor_url)
    
    # Match the op section first to ensure we update the right one
    op_section_pattern = rf'(^### {re.escape(op_name)}\n)(.*?)(?=^### |^## |\Z)'
    
    def replace_op_section(match):
        op_header = match.group(1)
        op_content = match.group(2)
        
        # Update the Example Patch line within this op's content
        pattern = r'(\*\*Example Patch:\*\*\s*\[Open in Editor\]\()([^)]+)(\))'
        new_op_content = re.sub(pattern, lambda m: f"{m.group(1)}{editor_url}{m.group(3)}", op_content)
        
        return f"{op_header}{new_op_content}"
    
    return re.sub(op_section_pattern, replace_op_section, content, flags=re.MULTILINE | re.DOTALL)


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Update editor links in op markdown files')
    parser.add_argument('--test', action='store_true', help='Test mode - only process first 10 ops')
    parser.add_argument('--limit', type=int, help='Limit number of ops to process')
    args = parser.parse_args()
    
    if not PLAYWRIGHT_AVAILABLE:
        print("ERROR: Playwright is required. Install with:")
        print("  pip install playwright")
        print("  playwright install chromium")
        return
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    print("=" * 60)
    print("Update Editor Links in Markdown")
    print("=" * 60)
    print()
    
    # Find all op files
    print("Finding op files...")
    op_files = find_all_op_files()
    print(f"Found {len(op_files)} namespace files")
    print()
    
    if not op_files:
        print("No op files found!")
        return
    
    # Collect all ops from all files
    all_ops = []
    for filepath in op_files:
        content, op_sections, op_urls = parse_op_file(str(filepath))
        for op_name, op_url, start_pos, end_pos in op_urls:
            all_ops.append({
                'filepath': str(filepath),
                'op_name': op_name,
                'op_url': op_url,
                'op_content': op_sections[op_name]['content'],
                'file_content': content
            })
    
    print(f"Total ops found: {len(all_ops)}")
    
    # Apply limits
    if args.test:
        all_ops = all_ops[:10]
        print(f"TEST MODE: Processing only {len(all_ops)} ops")
    elif args.limit:
        all_ops = all_ops[:args.limit]
        print(f"LIMITED MODE: Processing only {len(all_ops)} ops")
    
    print()
    
    if not all_ops:
        print("No ops found in files!")
        return
    
    updated_count = 0
    skipped_count = 0
    error_count = 0
    files_to_save = {}  # Track which files need to be saved
    
    # Start browser
    print("Starting browser...")
    print()
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        )
        page = context.new_page()
        
        print(f"Processing {len(all_ops)} ops...")
        print("Progress updates every 50 ops")
        print("=" * 60)
        print()
        
        for i, op_data in enumerate(all_ops, 1):
            op_name = op_data['op_name']
            op_url = op_data['op_url']
            filepath = op_data['filepath']
            
            # Progress indicator
            if i % 50 == 0 or i == 1:
                print(f"[{i}/{len(all_ops)}] Processing {op_name}...")
            
            # Check if we already have an editor link (not just url#example)
            op_content = op_data['op_content']
            current_example_match = re.search(r'\*\*Example Patch:\*\*\s*\[Open in Editor\]\(([^)]+)\)', op_content)
            
            if current_example_match:
                current_url = current_example_match.group(1)
                # Skip if already using an editor URL (contains /edit/)
                if '/edit/' in current_url:
                    skipped_count += 1
                    if i % 50 == 0:
                        print(f"    Already has editor link, skipping")
                    time.sleep(0.1)  # Small delay anyway
                    continue
            
            # Extract editor URL
            try:
                editor_url = extract_editor_url_from_page(page, op_url)
                
                if editor_url:
                    # Get or create file content for this file
                    if filepath not in files_to_save:
                        files_to_save[filepath] = op_data['file_content']
                    
                    # Update content
                    files_to_save[filepath] = update_op_section_in_content(
                        files_to_save[filepath], op_name, editor_url
                    )
                    updated_count += 1
                    if i % 50 == 0:
                        print(f"    ✓ Found editor URL: {editor_url}")
                else:
                    skipped_count += 1
                    if i % 50 == 0:
                        print(f"    - No editor link found")
                
            except Exception as e:
                error_count += 1
                if i % 50 == 0:
                    print(f"    ✗ Error: {str(e)[:50]}")
            
            time.sleep(REQUEST_DELAY)
        
        browser.close()
    
    # Save updated files
    if files_to_save:
        print()
        print(f"Saving {len(files_to_save)} updated files...")
        for filepath, content in files_to_save.items():
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  ✓ Saved {Path(filepath).name}")
    else:
        print()
        print("No updates needed - all editor links are already correct!")
    
    # Summary
    print()
    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Total ops processed: {len(all_ops)}")
    print(f"Updated with editor links: {updated_count}")
    print(f"Skipped (already correct): {skipped_count}")
    print(f"Errors: {error_count}")
    print(f"Files updated: {len(files_to_save)}")
    print("=" * 60)


if __name__ == "__main__":
    main()

