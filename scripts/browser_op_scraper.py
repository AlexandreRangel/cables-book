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


def log(msg: str, level: str = "INFO", flush: bool = False):
    """Log a message with timestamp"""
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}] [{level}] {msg}", flush=flush)


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
        'editor_url': '',  # "Open in Editor" link
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
        
        # ===== EXTRACT "OPEN IN EDITOR" LINK =====
        # Look for links containing "/edit/" in their href
        try:
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
                    op_info['editor_url'] = editor_url
                    break
        except Exception as e:
            # If we can't find the link, that's ok - we'll use the fallback
            pass
        
        # ===== EXTRACT DESCRIPTION =====
        # cables.gl stores descriptions in textarea/input elements!
        # Method 1: Extract from textarea/input elements (MOST RELIABLE)
        try:
            # Get all textareas and text inputs
            inputs = page.query_selector_all('textarea, input[type="text"]')
            
            for inp in inputs:
                try:
                    # Get value from the element
                    value = inp.get_attribute('value') or ''
                    if not value:
                        value = inp.inner_text() or ''
                    value = value.strip()
                    
                    # Check if this looks like a description (not too short, not too long, no HTML tags)
                    if value and len(value) > 15 and len(value) < 500:
                        # Skip if it looks like code or metadata
                        if not any(x in value.lower() for x in ['function', 'const ', 'var ', 'let ', '<script', '<div', 'http://', 'https://']):
                            # Skip if it's clearly junk
                            if not any(x in value for x in ['INPUT PORTS', 'OUTPUT PORTS', 'SaveCancel']):
                                # Clean up HTML entities
                                value = value.replace('&gt;', '>').replace('&lt;', '<').replace('&amp;', '&')
                                # Normalize whitespace
                                value = re.sub(r'\s+', ' ', value).strip()
                                op_info['description'] = value
                                break
                except:
                    continue
        except Exception as e:
            pass
        
        # Method 2: Look for parent of "Summary (oneliner)" element
        if not op_info['description']:
            try:
                summary_el = page.query_selector('text=/Summary.*oneliner/i')
                if summary_el:
                    # Get the parent container and look for nearby input/textarea
                    parent = summary_el.evaluate('el => el.parentElement')
                    if parent:
                        # Look for sibling input/textarea
                        sibling_inputs = page.evaluate('''el => {
                            const parent = el.parentElement;
                            if (!parent) return [];
                            const inputs = parent.querySelectorAll("textarea, input[type='text']");
                            return Array.from(inputs).map(i => i.value || i.innerText || "").filter(v => v.length > 10);
                        }''', summary_el)
                        
                        if sibling_inputs and len(sibling_inputs) > 0:
                            desc = sibling_inputs[0].strip()
                            if desc and len(desc) > 15 and len(desc) < 500:
                                desc = desc.replace('&gt;', '>').replace('&lt;', '<').replace('&amp;', '&')
                                desc = re.sub(r'\s+', ' ', desc).strip()
                                op_info['description'] = desc
            except:
                pass
        
        # Method 3: Fallback - look in page text for Summary section
        if not op_info['description']:
            desc_patterns = [
                r'Summary\s*\(oneliner\)\s*\n\s*([^\n\r]{15,300})',
                r'Summary\s*\(oneliner\)\s*:?\s*([^\n\r]{15,300})',
            ]
            
            for pattern in desc_patterns:
                match = re.search(pattern, page_text, re.IGNORECASE | re.DOTALL)
                if match:
                    desc = match.group(1).strip()
                    desc = desc.split('\n')[0].strip()
                    desc = re.sub(r'\s+', ' ', desc)
                    
                    if (desc and len(desc) > 10 and 
                        not desc.lower().startswith(('full name', 'visibility', 'license', 'input', 'output')) and
                        not any(x in desc.upper() for x in ['INPUT PORTS', 'OUTPUT PORTS', 'SAVECANCEL'])):
                        op_info['description'] = desc
                        break
        
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
    
    # Use editor_url if available, otherwise fallback to url#example
    example_patch_url = op.get('editor_url', '') or f"{url}#example"
    
    md += f"""
**Example Patch:** [Open in Editor]({example_patch_url})
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "{short_name}"*
**Docs:** [{url}]({url})

---

"""
    return md


def parse_markdown_file(filepath: str) -> Dict:
    """Parse the existing markdown file to extract op sections.
    
    Handles both unified file format and split file format.
    """
    chapters_dir = os.path.dirname(filepath) or '../chapters'
    
    # Check if we have split files (13-Ops*.md files)
    split_files = []
    if os.path.exists(chapters_dir):
        for f in os.listdir(chapters_dir):
            if f.startswith('13-Ops') and f.endswith('.md') and f != '13-AllOps.md' and f != '13-_AllOps.md':
                split_files.append(os.path.join(chapters_dir, f))
    
    sections = {}
    header = ''
    
    if split_files:
        # Parse split files
        for split_file in sorted(split_files):
            with open(split_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract namespace from split file (look for ## Ops.XXX)
            ns_match = re.search(r'^## (Ops\.[^\n]+)', content, re.MULTILINE)
            if ns_match:
                namespace = ns_match.group(1)
                
                # Extract op sections from this namespace file
                op_pattern = r'^(### \w+\n.*?)(?=^### |^## |\Z)'
                ops = {}
                for op_match in re.finditer(op_pattern, content, re.MULTILINE | re.DOTALL):
                    op_full_content = op_match.group(1)
                    # Extract op name from header
                    name_match = re.search(r'^### (\w+)', op_full_content, re.MULTILINE)
                    if name_match:
                        op_name = name_match.group(1)
                        ops[op_name] = op_full_content
                
                if ops:
                    sections[namespace] = ops
    elif os.path.exists(filepath):
        # Parse unified file
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract header (everything before first namespace section)
        header_match = re.search(r'^(.*?)(?=^## )', content, re.MULTILINE | re.DOTALL)
        header = header_match.group(1) if header_match else ''
        
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
    """Determine if we should update an op section based on data quality.
    
    IMPORTANT: Never overwrite good existing data with worse data!
    """
    # If no existing content, definitely update
    if not existing_content:
        return True
    
    # Check if existing has placeholder ports
    has_placeholder_ports = bool(re.search(r'Visit \[.+?\] for (?:input|output) port details', existing_content))
    
    # Check if existing has actual port entries (not just placeholders)
    existing_has_ports = bool(re.search(r'^- \*\*[^\*]+\*\* \([^)]+\):', existing_content))
    
    # Check if new data has actual ports
    has_new_ports = bool(new_op_data.get('input_ports') or new_op_data.get('output_ports'))
    
    # Check existing description quality
    existing_desc_match = re.search(r'\*\*Description:\*\* (.+)', existing_content, re.DOTALL)
    existing_desc = ''
    existing_desc_placeholder = False
    existing_desc_is_good = False
    
    if existing_desc_match:
        existing_desc = existing_desc_match.group(1).strip()
        # Check if it's a placeholder
        existing_desc_placeholder = bool(re.search(r'^\*Visit \[.+?\] for details\*$', existing_desc))
        # Check if it's a real description (not placeholder, not junk, has reasonable length)
        if not existing_desc_placeholder:
            existing_desc_clean = re.sub(r'^\*|\*$', '', existing_desc).strip()
            # Good description: not placeholder, has length, doesn't start with common junk
            if (len(existing_desc_clean) > 15 and 
                not existing_desc_clean.lower().startswith(('full name', 'visibility', 'license', 'visit')) and
                not re.search(r'Full Name|Visibility|License|Author|github', existing_desc_clean, re.IGNORECASE)):
                existing_desc_is_good = True
    
    # Check if new data has a good description
    new_desc = new_op_data.get('description', '').strip()
    has_good_new_desc = bool(new_desc and len(new_desc) > 10 and 
                             not new_desc.lower().startswith(('full name', 'visibility', 'license', 'visit')) and
                             not re.search(r'Full Name|Visibility|License|INPUT PORTS|OUTPUT PORTS', new_desc, re.IGNORECASE))
    
    # Check if existing has bad description (contains junk metadata)
    has_bad_desc = bool(re.search(r'Full Name[^:]*:|Visibility|License|Author|github|Maintained by|Patchlists', existing_content, re.IGNORECASE))
    
    # Check if existing has editor URL
    existing_has_editor = bool(re.search(r'\*\*Example Patch:\*\*\s*\[Open in Editor\]\([^)]*\/edit\/[^)]+\)', existing_content))
    new_has_editor = bool(new_op_data.get('editor_url'))
    
    # Update logic (conservative - preserve good data):
    # 1. Update if has placeholder ports AND we have new ports
    # 2. Update if has bad description (junk) AND we have good new description
    # 3. Update if no existing ports AND we have new ports
    # 4. Update if existing description is placeholder AND we have real description
    # 5. Update if no editor URL but we have one
    # 6. NEVER update if existing has good description UNLESS new one is clearly better
    
    should_update = False
    
    if has_placeholder_ports and has_new_ports:
        should_update = True  # Always fix placeholder ports
    elif has_bad_desc and has_good_new_desc:
        should_update = True  # Fix bad descriptions
    elif not existing_has_ports and has_new_ports:
        should_update = True  # Add missing ports
    elif existing_desc_placeholder and has_good_new_desc:
        should_update = True  # Replace placeholder with real description
    elif not existing_has_editor and new_has_editor:
        should_update = True  # Add editor URL if missing
    # CRITICAL: If existing has good description, only update if new is clearly better
    elif existing_desc_is_good:
        # Don't overwrite good description unless new one is significantly better
        # (e.g., new is much longer/more detailed)
        if has_good_new_desc and len(new_desc) > len(existing_desc) * 1.5:
            should_update = True
        # But still update ports/editor links even if description is good
        elif (has_new_ports and has_placeholder_ports) or (not existing_has_editor and new_has_editor):
            should_update = True
    
    return should_update


def update_markdown_file(filepath: str, op_data: Dict, markdown_cache: Dict):
    """Update the markdown file with a new/updated op section.
    
    Preserves existing good descriptions and merges new data intelligently.
    """
    full_name = op_data['full_name']
    short_name = op_data['short_name']
    namespace = op_data['namespace']
    
    # Check if op already exists
    existing_content = ''
    if namespace in markdown_cache['sections']:
        if short_name in markdown_cache['sections'][namespace]:
            existing_content = markdown_cache['sections'][namespace][short_name]
            
            # Extract existing description if it's good
            existing_desc_match = re.search(r'\*\*Description:\*\* (.+?)(?:\n\n|\n\*\*>)', existing_content, re.DOTALL)
            if existing_desc_match:
                existing_desc = existing_desc_match.group(1).strip()
                # Check if existing description is good (not a placeholder)
                if not re.search(r'^\*Visit \[.+?\] for details\*$', existing_desc):
                    existing_desc_clean = re.sub(r'^\*|\*$', '', existing_desc).strip()
                    # If it's a real description, preserve it unless new one is clearly better
                    if (len(existing_desc_clean) > 15 and 
                        not existing_desc_clean.lower().startswith(('full name', 'visibility', 'license', 'visit'))):
                        # Only use new description if it's significantly better
                        new_desc = op_data.get('description', '').strip()
                        if not (new_desc and len(new_desc) > len(existing_desc_clean) * 1.3):
                            # Keep existing description
                            op_data['description'] = existing_desc_clean
            
            # Extract existing editor URL if present
            existing_editor_match = re.search(r'\*\*Example Patch:\*\*\s*\[Open in Editor\]\(([^)]+)\)', existing_content)
            if existing_editor_match:
                existing_editor_url = existing_editor_match.group(1)
                # If existing has a real editor link and new one doesn't, keep existing
                if '/edit/' in existing_editor_url and not op_data.get('editor_url'):
                    op_data['editor_url'] = existing_editor_url
                # If both exist but existing is a real editor link, prefer it unless new is different
                elif '/edit/' in existing_editor_url and op_data.get('editor_url'):
                    # Keep existing if it's valid, new one will override if it's also valid
                    pass
            
            # Decide if we should update
            if not should_update_op(existing_content, op_data):
                return False  # Skip update, existing is better
    
    # Generate new op markdown (includes the ### header)
    new_op_md = generate_op_markdown(op_data)
    
    # Update cache (op markdown includes ### header)
    if namespace not in markdown_cache['sections']:
        markdown_cache['sections'][namespace] = {}
    markdown_cache['sections'][namespace][short_name] = new_op_md
    
    return True  # Updated


def save_markdown_file(filepath: str, markdown_cache: Dict):
    """Save the markdown file from cache. Handles both unified and split file formats."""
    chapters_dir = os.path.dirname(filepath) or '../chapters'
    
    # Check if we should use split files (if 13-Ops*.md files exist)
    split_files_exist = False
    if os.path.exists(chapters_dir):
        for f in os.listdir(chapters_dir):
            if f.startswith('13-Ops') and f.endswith('.md') and f != '13-AllOps.md' and f != '13-_AllOps.md':
                split_files_exist = True
                break
    
    if split_files_exist:
        # Save to split files
        for namespace in sorted(markdown_cache['sections'].keys()):
            # Find existing split file for this namespace
            namespace_file = None
            for f in os.listdir(chapters_dir):
                if f.startswith('13-Ops') and f.endswith('.md'):
                    file_path = os.path.join(chapters_dir, f)
                    with open(file_path, 'r', encoding='utf-8') as fobj:
                        content = fobj.read()
                        if f'## {namespace}\n' in content:
                            namespace_file = file_path
                            break
            
            # Create content for this namespace
            ns_content = f"# {namespace}\n\n"
            ns_content += f"*Part of the [All Operators Reference](13-_AllOps.md)*\n\n"
            ns_content += "---\n\n"
            ns_content += f"## {namespace}\n\n"
            
            # Add ops in sorted order
            ops = markdown_cache['sections'][namespace]
            for op_name in sorted(ops.keys(), key=str.lower):
                ns_content += ops[op_name]
            
            # Write to file (create new if doesn't exist)
            if not namespace_file:
                # Create filename from namespace
                name_part = namespace.replace('Ops.', '').replace('.', '')
                namespace_file = os.path.join(chapters_dir, f"13-Ops{name_part}.md")
            
            with open(namespace_file, 'w', encoding='utf-8') as f:
                f.write(ns_content)
    else:
        # Save to unified file
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
    
    # Get all ops list (with progress indication)
    log("Fetching ops list from cables.gl (this may take 30-60 seconds)...")
    all_ops_list = get_all_ops_list()
    
    if not all_ops_list:
        log("No ops found!", "ERROR")
        return
    
    log(f"✓ Found {len(all_ops_list)} ops to process")
    
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
    log("\nLoading existing markdown files...")
    log("  Scanning for split namespace files (13-Ops*.md)...")
    markdown_cache = parse_markdown_file(MARKDOWN_FILE)
    existing_ops_count = sum(len(ops) for ops in markdown_cache['sections'].values())
    namespace_count = len(markdown_cache['sections'])
    log(f"  ✓ Found {existing_ops_count} existing ops in {namespace_count} namespaces")
    
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
        log("Progress saved every 2 ops for faster updates")
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
            
            # Progress indicator - show EVERY op for visibility
            if i % 1 == 0:  # Show every op
                log(f"[{i}/{total}] ({pct:.1f}%) {short_name} ({namespace}){eta_str}", flush=True)
            
            # Scrape op page
            op_data = scrape_op_with_browser(page, full_name, op['url'], args.slow)
            
            # Log what we got - show for every op
            desc_str = f" ✓ desc: {op_data.get('description', '')[:60]}..." if op_data.get('description') else " ✗ no desc"
            editor_str = f" ✓ editor: {op_data.get('editor_url', '')}" if op_data.get('editor_url') else " ✗ no editor"
            log(f"  ->{desc_str}{editor_str}", flush=True)
            
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
            
            # Save markdown periodically (every 2 ops for faster updates)
            if i % 2 == 0:
                try:
                    save_markdown_file(MARKDOWN_FILE, markdown_cache)
                    desc_count = sum(1 for ns in markdown_cache['sections'].values() 
                                   for op_content in ns.values() 
                                   if not re.search(r'\*\*Description:\*\* \*Visit \[.+?\] for details\*', op_content))
                    log(f"  -> Markdown saved ({stats['updated']} updated, {stats['added']} added, {stats['skipped']} skipped, {desc_count} with descriptions)")
                except Exception as e:
                    log(f"  -> Error saving markdown: {e}", "WARN")
            
            # Save progress periodically (every 2 ops for faster updates)
            if i % 2 == 0:
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

