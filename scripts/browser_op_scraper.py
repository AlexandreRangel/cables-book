#!/usr/bin/env python3
"""
Browser-based Op Scraper for cables.gl

This script uses Playwright (headless browser) to scrape cables.gl op pages.
Since cables.gl uses JavaScript to render content, a browser-based approach
is required to get accurate port information.

Requirements:
    pip install playwright
    playwright install chromium

Usage:
    python browser_op_scraper.py                    # Scrape all ops
    python browser_op_scraper.py --namespace Ops.Gl # Scrape specific namespace
    python browser_op_scraper.py --resume           # Resume from last position
    python browser_op_scraper.py --test             # Test with 10 ops only
    python browser_op_scraper.py --slow             # Slower but more reliable

Output:
    - browser_ops_data.json   - Complete scraped data
    - chapters/13-AllOps.md   - Generated markdown
    - chapters/images/ops/    - Downloaded SVG images

Note: This is SLOWER than the requests-based scraper but gets more accurate data.
Full scrape takes 4-8 hours for ~1340 ops.
"""

import json
import os
import re
import time
import sys
import argparse
from datetime import datetime
from typing import Dict, List, Optional

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

import requests

# Configuration
BASE_URL = "https://cables.gl"
OUTPUT_DIR = "../chapters/images/ops"
DATA_FILE = "../browser_ops_data.json"
PROGRESS_FILE = "../browser_scrape_progress.json"
MARKDOWN_FILE = "../chapters/13-AllOps.md"

# Timing (seconds)
PAGE_LOAD_WAIT = 5  # Wait for JS to render
REQUEST_DELAY = 1.0  # Between ops
SLOW_MODE_DELAY = 3  # Extra wait in slow mode
PAGE_TIMEOUT = 60000  # Page load timeout (ms)


def log(msg: str, level: str = "INFO"):
    """Log a message with timestamp"""
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}] [{level}] {msg}")


def save_progress(data: Dict, filename: str = PROGRESS_FILE):
    """Save progress to JSON file"""
    os.makedirs(os.path.dirname(filename) or '.', exist_ok=True)
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def load_progress(filename: str = PROGRESS_FILE) -> Optional[Dict]:
    """Load progress from JSON file"""
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    return None


def get_all_ops_list() -> List[Dict]:
    """Get list of all ops from cables.gl (uses requests, not browser)"""
    log("Getting all ops from cables.gl...")
    
    all_ops = []
    visited_namespaces = set()
    
    # First, get all top-level namespaces
    try:
        response = requests.get(f"{BASE_URL}/ops/", timeout=30, 
                               headers={'User-Agent': 'Mozilla/5.0'})
        if response.status_code != 200:
            log(f"Failed to get ops page: {response.status_code}", "ERROR")
            return []
        
        # Find namespace links
        pattern = r'href="/ops/(Ops\.[A-Za-z0-9]+)"'
        namespaces = sorted(set(re.findall(pattern, response.text)))
        log(f"Found {len(namespaces)} top-level namespaces")
        
        # Process each namespace
        for ns in namespaces:
            get_ops_from_namespace(ns, all_ops, visited_namespaces)
            time.sleep(0.3)
        
    except Exception as e:
        log(f"Error: {e}", "ERROR")
    
    # Remove duplicates
    seen = set()
    unique_ops = []
    for op in all_ops:
        if op['full_name'] not in seen:
            seen.add(op['full_name'])
            unique_ops.append(op)
    
    log(f"Total unique ops: {len(unique_ops)}")
    return unique_ops


def get_ops_from_namespace(namespace: str, all_ops: List, visited: set):
    """Recursively get all ops from a namespace"""
    if namespace in visited:
        return
    visited.add(namespace)
    
    try:
        response = requests.get(f"{BASE_URL}/ops/{namespace}", timeout=30,
                               headers={'User-Agent': 'Mozilla/5.0'})
        if response.status_code != 200:
            return
        
        # Find individual op links
        op_pattern = r'href="/op/(Ops\.[A-Za-z0-9_.]+)"'
        op_matches = set(re.findall(op_pattern, response.text))
        
        for full_name in op_matches:
            parts = full_name.split('.')
            if len(parts) >= 3:
                all_ops.append({
                    'full_name': full_name,
                    'short_name': parts[-1],
                    'namespace': '.'.join(parts[:-1]),
                    'url': f"{BASE_URL}/op/{full_name}"
                })
        
        # Find sub-namespaces
        sub_ns_pattern = rf'href="/ops/({re.escape(namespace)}\.[A-Za-z0-9]+)"'
        sub_namespaces = set(re.findall(sub_ns_pattern, response.text))
        
        for sub_ns in sub_namespaces:
            if sub_ns not in visited:
                log(f"  Found sub-namespace: {sub_ns}")
                get_ops_from_namespace(sub_ns, all_ops, visited)
                time.sleep(0.2)
        
    except Exception as e:
        log(f"Error getting {namespace}: {e}", "WARN")


def scrape_op_with_browser(page, full_name: str, url: str, slow_mode: bool = False) -> Dict:
    """
    Scrape an op page using Playwright browser.
    Returns complete op information.
    """
    op_info = {
        'full_name': full_name,
        'short_name': full_name.split('.')[-1],
        'namespace': '.'.join(full_name.split('.')[:-1]),
        'url': url,
        'description': '',
        'input_ports': [],
        'output_ports': [],
        'scraped_at': datetime.now().isoformat(),
        'scrape_status': 'failed'
    }
    
    try:
        # Navigate to the op page with longer timeout
        page.goto(url, wait_until='domcontentloaded', timeout=PAGE_TIMEOUT)
        
        # Wait for the page to fully render - look for specific content
        try:
            # Wait for port sections to appear (indicates JS has loaded)
            page.wait_for_selector('text=INPUT PORTS', timeout=10000)
        except:
            # If no INPUT PORTS text, wait a bit longer
            pass
        
        # Additional wait for content to render
        wait_time = PAGE_LOAD_WAIT + (SLOW_MODE_DELAY if slow_mode else 0)
        time.sleep(wait_time)
        
        # Get the rendered page content
        page_text = page.inner_text('body')
        
        # ===== EXTRACT DESCRIPTION =====
        # Look for Summary section
        summary_match = re.search(r'Summary \(oneliner\)\s*\n\s*([^\n]+)', page_text)
        if summary_match:
            desc = summary_match.group(1).strip()
            if desc and len(desc) > 3 and not desc.lower().startswith('issues'):
                op_info['description'] = desc
        
        # ===== EXTRACT INPUT PORTS =====
        input_section = re.search(
            r'INPUT PORTS\s*(.*?)(?:OUTPUT PORTS|$)',
            page_text, re.DOTALL | re.IGNORECASE
        )
        if input_section:
            input_text = input_section.group(1)
            op_info['input_ports'] = parse_ports_from_text(input_text)
        
        # ===== EXTRACT OUTPUT PORTS =====
        output_section = re.search(
            r'OUTPUT PORTS\s*(.*?)(?:SaveCancel|Changelog|Documentation|Issues|$)',
            page_text, re.DOTALL | re.IGNORECASE
        )
        if output_section:
            output_text = output_section.group(1)
            op_info['output_ports'] = parse_ports_from_text(output_text)
        
        op_info['scrape_status'] = 'success'
        
    except PlaywrightTimeout:
        op_info['scrape_status'] = 'timeout'
    except Exception as e:
        op_info['scrape_status'] = f'error: {str(e)[:50]}'
    
    return op_info


def parse_ports_from_text(port_text: str) -> List[Dict]:
    """Parse port information from rendered text"""
    ports = []
    
    # Split by lines and look for port patterns
    lines = port_text.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Match: "PortName (Type)"
        match = re.match(r'^([A-Za-z][A-Za-z0-9 _-]{0,40}?)\s*\(([^)]+)\)$', line)
        if match:
            port_name = match.group(1).strip()
            port_type = match.group(2).strip()
            
            # Skip garbage matches
            if port_name and len(port_name) < 50 and not port_name.lower() in ['input', 'output', 'ports']:
                # Get description from next line
                desc = ''
                if i + 1 < len(lines):
                    next_line = lines[i + 1].strip()
                    # Check if it's a description (not another port)
                    if next_line and not re.match(r'^[A-Za-z][A-Za-z0-9 _-]*\s*\([^)]+\)$', next_line):
                        desc = next_line
                        i += 1  # Skip the description line
                
                if not desc:
                    desc = '*See documentation*'
                
                # Avoid duplicates
                if not any(p['name'] == port_name for p in ports):
                    ports.append({
                        'name': port_name,
                        'type': port_type,
                        'description': desc
                    })
        
        i += 1
    
    return ports


def download_op_image(full_name: str) -> bool:
    """Download the SVG layout image for an op"""
    safe_name = full_name.replace('.', '_')
    save_path = os.path.join(OUTPUT_DIR, f"{safe_name}.svg")
    
    url = f"{BASE_URL}/api/op/layout/{full_name}"
    
    try:
        response = requests.get(url, timeout=15, headers={'User-Agent': 'Mozilla/5.0'})
        if response.status_code == 200 and b'<svg' in response.content[:200]:
            os.makedirs(OUTPUT_DIR, exist_ok=True)
            with open(save_path, 'wb') as f:
                f.write(response.content)
            return True
    except:
        pass
    
    return False


def format_port_markdown(port: Dict) -> str:
    """Format a port for markdown"""
    name = port.get('name', '')
    port_type = port.get('type', '')
    desc = port.get('description', '*See documentation*')
    return f"- **{name}** ({port_type}): {desc}"


def generate_op_markdown(op: Dict) -> str:
    """Generate markdown for a single op"""
    full_name = op['full_name']
    short_name = op['short_name']
    url = op['url']
    description = op.get('description', '')
    
    # Clean up description - remove junk text
    if description:
        # Remove common junk patterns
        junk_patterns = [
            r'Full Name[^\n]+',
            r'Visibility[^\n]+',
            r'License[^\n]+',
            r'Author[^\n]+',
            r'github[^\n]+',
            r'Maintained by[^\n]+',
            r'Patchlists[^\n]+',
            r'Documentation \(markdown\)',
            r'Issues',
            r'Example patch id',
            r'Youtube ids[^\n]+',
            r'Op Licence',
            r'Caniuse query',
            r'Example Patch[^\n]+',
            r'Open In Editor',
            r'INPUT PORTS',
            r'OUTPUT PORTS',
        ]
        for pattern in junk_patterns:
            description = re.sub(pattern, '', description, flags=re.IGNORECASE)
        description = ' '.join(description.split())  # Normalize whitespace
        description = description.strip()
        if len(description) < 5 or description.lower().startswith('full name'):
            description = ''
    
    if not description:
        description = f"*Visit [documentation]({url}) for details*"
    
    safe_name = full_name.replace('.', '_')
    image_path = f"images/ops/{safe_name}.svg"
    
    md = f"""### {short_name}
![{short_name} op]({image_path})

**Full Name:** `{full_name}`
**Description:** {description}

**> Input Ports:**
"""
    
    if op.get('input_ports'):
        for port in op['input_ports']:
            md += format_port_markdown(port) + "\n"
    else:
        md += f"- *Visit [{full_name} documentation]({url}) for input port details*\n"
    
    md += "\n**< Output Ports:**\n"
    
    if op.get('output_ports'):
        for port in op['output_ports']:
            md += format_port_markdown(port) + "\n"
    else:
        md += f"- *Visit [{full_name} documentation]({url}) for output port details*\n"
    
    md += f"""
**Example Patch:** [Open in Editor]({url}#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "{short_name}"*
**Docs:** [{url}]({url})

---

"""
    return md


def parse_markdown_file(filepath: str) -> Dict:
    """Parse the existing markdown file to extract op sections"""
    if not os.path.exists(filepath):
        return {'header': '', 'sections': {}}
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract header (everything before first namespace section)
    header_match = re.search(r'^(.*?)(?=^## )', content, re.MULTILINE | re.DOTALL)
    header = header_match.group(1) if header_match else ''
    
    sections = {}
    
    # Find all namespace sections
    namespace_pattern = r'^## (Ops\.[^\n]+)\n\n(.*?)(?=^## |\Z)'
    for ns_match in re.finditer(namespace_pattern, content, re.MULTILINE | re.DOTALL):
        namespace = ns_match.group(1)
        ns_content = ns_match.group(2)
        
        # Find all op sections in this namespace (include the ### header in content)
        op_pattern = r'^(### \w+\n.*?)(?=^### |^## |\Z)'
        ops = {}
        for op_match in re.finditer(op_pattern, ns_content, re.MULTILINE | re.DOTALL):
            op_full_content = op_match.group(1)
            # Extract op name from header
            name_match = re.search(r'^### (\w+)', op_full_content, re.MULTILINE)
            if name_match:
                op_name = name_match.group(1)
                ops[op_name] = op_full_content
        
        sections[namespace] = ops
    
    return {'header': header, 'sections': sections}


def should_update_op(existing_content: str, new_op_data: Dict) -> bool:
    """Determine if we should update an op section based on data quality"""
    # If no existing content, definitely update
    if not existing_content:
        return True
    
    # Check if existing has placeholder ports
    has_placeholder = bool(re.search(r'Visit \[.+?\] for (?:input|output) port details', existing_content))
    
    # Check if existing has actual port entries (not just placeholders)
    existing_has_ports = bool(re.search(r'^- \*\*[^\*]+\*\* \([^)]+\):', existing_content))
    
    # Check if new data has actual ports
    has_new_ports = bool(new_op_data.get('input_ports') or new_op_data.get('output_ports'))
    
    # Check if existing has bad description (contains junk)
    has_bad_desc = bool(re.search(r'Full Name[^:]*:|Visibility|License|Author|github|Maintained by|Patchlists', existing_content, re.IGNORECASE))
    
    # Check if new data has a good description
    new_desc = new_op_data.get('description', '').strip()
    has_good_desc = bool(new_desc and len(new_desc) > 10 and not new_desc.lower().startswith('full name'))
    
    # Update if:
    # 1. Has placeholder and we have ports (always update placeholders)
    # 2. Has bad description and we have good one (fix bad descriptions)
    # 3. No existing ports but we have new ports (complete missing data)
    # 4. Existing description is just placeholder and we have a real one
    existing_desc_placeholder = bool(re.search(r'\*\*Description:\*\* \*Visit \[.+?\] for details', existing_content))
    
    return (has_placeholder and has_new_ports) or \
           (has_bad_desc and has_good_desc) or \
           (not existing_has_ports and has_new_ports) or \
           (existing_desc_placeholder and has_good_desc)


def update_markdown_file(filepath: str, op_data: Dict, markdown_cache: Dict):
    """Update the markdown file with a new/updated op section"""
    full_name = op_data['full_name']
    short_name = op_data['short_name']
    namespace = op_data['namespace']
    
    # Generate new op markdown (includes the ### header)
    new_op_md = generate_op_markdown(op_data)
    
    # Check if op already exists
    existing_content = ''
    if namespace in markdown_cache['sections']:
        if short_name in markdown_cache['sections'][namespace]:
            existing_content = markdown_cache['sections'][namespace][short_name]
            
            # Decide if we should update
            if not should_update_op(existing_content, op_data):
                return False  # Skip update, existing is better
    
    # Update cache (op markdown includes ### header)
    if namespace not in markdown_cache['sections']:
        markdown_cache['sections'][namespace] = {}
    markdown_cache['sections'][namespace][short_name] = new_op_md
    
    return True  # Updated


def save_markdown_file(filepath: str, markdown_cache: Dict):
    """Save the markdown file from cache"""
    # Reconstruct markdown
    md = markdown_cache['header']
    
    # Add namespace sections in sorted order
    for namespace in sorted(markdown_cache['sections'].keys()):
        md += f"## {namespace}\n\n"
        
        # Add ops in sorted order (op markdown already includes ### header)
        ops = markdown_cache['sections'][namespace]
        for op_name in sorted(ops.keys(), key=str.lower):
            md += ops[op_name]
    
    # Write to file
    os.makedirs(os.path.dirname(filepath) or '.', exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(md)


def generate_allops_markdown(ops_by_namespace: Dict) -> str:
    """Generate the complete AllOps.md file"""
    
    total_ops = sum(len(ops) for ops in ops_by_namespace.values())
    total_with_ports = sum(
        1 for ops in ops_by_namespace.values()
        for op in ops
        if op.get('input_ports') or op.get('output_ports')
    )
    
    md = f"""# All Operators Reference

This chapter provides a comprehensive reference for all operators (ops) available in cables.gl.

**Statistics:** {total_ops} total ops, {total_with_ports} with port documentation

**Last Updated:** {datetime.now().strftime("%Y-%m-%d %H:%M")}

**Note:** This reference is scraped from [cables.gl/ops](https://cables.gl/ops/).

---

"""
    
    for namespace in sorted(ops_by_namespace.keys()):
        ops = ops_by_namespace[namespace]
        if not ops:
            continue
        
        md += f"## {namespace}\n\n"
        
        for op in sorted(ops, key=lambda x: x['short_name'].lower()):
            md += generate_op_markdown(op)
    
    return md


def main():
    if not PLAYWRIGHT_AVAILABLE:
        log("ERROR: Playwright is required. Install with:", "ERROR")
        log("  pip install playwright", "ERROR")
        log("  playwright install chromium", "ERROR")
        return
    
    parser = argparse.ArgumentParser(description='Browser-based cables.gl op scraper')
    parser.add_argument('--namespace', type=str, help='Scrape only a specific namespace')
    parser.add_argument('--resume', action='store_true', help='Resume from last position')
    parser.add_argument('--test', action='store_true', help='Test mode - only 10 ops')
    parser.add_argument('--slow', action='store_true', help='Slow mode - more reliable')
    parser.add_argument('--skip-images', action='store_true', help='Skip image downloads')
    args = parser.parse_args()
    
    # Change to script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    log("=" * 60)
    log("Browser-based cables.gl Op Scraper")
    log("=" * 60)
    
    # Get all ops list
    all_ops_list = get_all_ops_list()
    
    if not all_ops_list:
        log("No ops found!", "ERROR")
        return
    
    # Filter by namespace if specified
    if args.namespace:
        all_ops_list = [op for op in all_ops_list 
                        if op['namespace'].startswith(args.namespace)]
        log(f"Filtered to {len(all_ops_list)} ops in {args.namespace}")
    
    # Test mode
    if args.test:
        all_ops_list = all_ops_list[:10]
        log("TEST MODE: Only processing 10 ops")
    
    # Load previous progress if resuming
    all_ops_data = {}
    start_index = 0
    
    if args.resume:
        progress = load_progress()
        if progress:
            all_ops_data = progress.get('ops', {})
            start_index = progress.get('last_index', 0)
            log(f"Resuming from index {start_index}")
    
    # Load existing markdown file for incremental updates
    log("\nLoading existing markdown file...")
    markdown_cache = parse_markdown_file(MARKDOWN_FILE)
    existing_ops_count = sum(len(ops) for ops in markdown_cache['sections'].values())
    log(f"Found {existing_ops_count} existing ops in markdown")
    
    # Track stats
    stats = {
        'updated': 0,
        'skipped': 0,
        'added': 0,
        'with_ports': 0,
        'with_desc': 0
    }
    
    # Start browser
    log("\nStarting headless browser...")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        )
        page = context.new_page()
        
        total = len(all_ops_list)
        log(f"\nScraping {total} ops...")
        log("Progress updates every 10 ops, markdown saved every 10 ops")
        log("=" * 60)
        
        start_time = time.time()
        for i, op in enumerate(all_ops_list[start_index:], start_index + 1):
            full_name = op['full_name']
            namespace = op['namespace']
            short_name = op['short_name']
            
            # Progress indicator
            pct = (i / total) * 100
            elapsed = time.time() - start_time
            if i > start_index + 1:
                avg_time = elapsed / (i - start_index - 1)
                remaining = (total - i) * avg_time
                eta_str = f", ETA: {remaining/60:.1f}min"
            else:
                eta_str = ""
            
            # Detailed progress every 10 ops
            if i % 10 == 0 or i == start_index + 1:
                log(f"[{i}/{total}] ({pct:.1f}%) Processing {short_name}{eta_str}")
            
            # Scrape op page
            op_data = scrape_op_with_browser(page, full_name, op['url'], args.slow)
            
            # Download image
            if not args.skip_images:
                img_ok = download_op_image(full_name)
                op_data['image_downloaded'] = img_ok
            
            # Store by namespace
            if namespace not in all_ops_data:
                all_ops_data[namespace] = []
            all_ops_data[namespace].append(op_data)
            
            # Check if op already exists before updating
            existed_before = (namespace in markdown_cache['sections'] and 
                            short_name in markdown_cache['sections'][namespace])
            
            # Update markdown incrementally
            was_update = update_markdown_file(MARKDOWN_FILE, op_data, markdown_cache)
            
            if was_update:
                if existed_before:
                    stats['updated'] += 1
                else:
                    stats['added'] += 1
            else:
                stats['skipped'] += 1
            
            # Count stats
            if op_data.get('input_ports') or op_data.get('output_ports'):
                stats['with_ports'] += 1
            if op_data.get('description') and len(op_data.get('description', '').strip()) > 10:
                stats['with_desc'] += 1
            
            # Save markdown periodically (every 10 ops for better monitoring)
            if i % 10 == 0:
                try:
                    save_markdown_file(MARKDOWN_FILE, markdown_cache)
                    log(f"  -> Markdown saved ({stats['updated']} updated, {stats['added']} added, {stats['skipped']} skipped)")
                except Exception as e:
                    log(f"  -> Error saving markdown: {e}", "WARN")
            
            # Save progress periodically (every 10 ops)
            if i % 10 == 0:
                try:
                    save_progress({
                        'ops': all_ops_data,
                        'last_index': i,
                        'last_updated': datetime.now().isoformat()
                    })
                except Exception as e:
                    log(f"  -> Error saving progress: {e}", "WARN")
            
            time.sleep(REQUEST_DELAY)
        
        browser.close()
    
    print()  # Newline
    
    # Save final markdown
    log("\nSaving final markdown file...")
    save_markdown_file(MARKDOWN_FILE, markdown_cache)
    
    # Save final data
    log("Saving data...")
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(all_ops_data, f, indent=2, ensure_ascii=False)
    log(f"Saved to {DATA_FILE}")
    
    # Summary
    total_ops = sum(len(ops) for ops in all_ops_data.values())
    
    log("\n" + "=" * 60)
    log("SUMMARY")
    log("=" * 60)
    log(f"Total ops scraped: {total_ops}")
    log(f"Ops with ports: {stats['with_ports']} ({100*stats['with_ports']/total_ops:.1f}%)")
    log(f"Ops with descriptions: {stats['with_desc']} ({100*stats['with_desc']/total_ops:.1f}%)")
    log(f"Markdown updates: {stats['updated']} updated, {stats['added']} added, {stats['skipped']} skipped")
    log(f"Markdown file: {MARKDOWN_FILE}")
    log("=" * 60)
    
    # Clean up progress file
    if os.path.exists(PROGRESS_FILE):
        os.remove(PROGRESS_FILE)


if __name__ == "__main__":
    main()

