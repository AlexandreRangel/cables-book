#!/usr/bin/env python3
"""
Thorough Op Scraper for cables.gl

This script thoroughly scrapes EACH op's individual page from cables.gl to get:
- Accurate description
- All input ports with types and descriptions
- All output ports with types and descriptions  
- Fresh SVG images

Features:
- Visits every individual op page (https://cables.gl/op/Ops.Namespace.OpName)
- Handles sub-namespaces (Ops.Gl.Matrix, Ops.Extension.Ai, etc.)
- Saves progress incrementally (can resume if interrupted)
- Rate limiting to be nice to cables.gl servers
- Detailed logging

Usage:
    python thorough_op_scraper.py                    # Scrape all ops
    python thorough_op_scraper.py --namespace Ops.Gl # Scrape specific namespace
    python thorough_op_scraper.py --resume           # Resume interrupted scrape
    python thorough_op_scraper.py --test             # Test with 5 ops only

Output:
    - thorough_ops_data.json  - Complete scraped data
    - chapters/13-AllOps.md   - Generated markdown
    - chapters/images/ops/    - Downloaded SVG images
"""

import requests
from bs4 import BeautifulSoup
import json
import os
import re
import time
import sys
import argparse
from datetime import datetime
from typing import Dict, List, Optional, Any

# Try to import Playwright for JavaScript-rendered content
try:
    from playwright.sync_api import sync_playwright
    PLAYWRIGHT_AVAILABLE = True
except ImportError:
    PLAYWRIGHT_AVAILABLE = False

# Configuration
BASE_URL = "https://cables.gl"
OUTPUT_DIR = "../chapters/images/ops"
DATA_FILE = "../thorough_ops_data.json"
PROGRESS_FILE = "../scrape_progress.json"
MARKDOWN_FILE = "../chapters/13-AllOps.md"

# Rate limiting (seconds between requests)
REQUEST_DELAY = 0.5
NAMESPACE_DELAY = 1.0

# Request headers
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
}

# Session for connection reuse
session = requests.Session()
session.headers.update(HEADERS)


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


def get_all_namespaces() -> List[str]:
    """Get all namespace URLs from the main ops page"""
    log("Getting all namespaces from cables.gl/ops/...")
    
    try:
        response = session.get(f"{BASE_URL}/ops/", timeout=30)
        if response.status_code != 200:
            log(f"Failed to get ops page: HTTP {response.status_code}", "ERROR")
            return []
        
        # Find all namespace links: /ops/Ops.Something
        pattern = r'href="/ops/(Ops\.[A-Za-z0-9]+)"'
        namespaces = sorted(set(re.findall(pattern, response.text)))
        
        log(f"Found {len(namespaces)} top-level namespaces")
        return namespaces
        
    except Exception as e:
        log(f"Error getting namespaces: {e}", "ERROR")
        return []


def get_ops_from_namespace(namespace: str, visited: set = None) -> List[Dict]:
    """
    Get all ops from a namespace page, recursively handling sub-namespaces.
    Returns list of op info dicts with full_name, short_name, namespace, url.
    """
    if visited is None:
        visited = set()
    
    if namespace in visited:
        return []
    visited.add(namespace)
    
    url = f"{BASE_URL}/ops/{namespace}"
    ops = []
    
    try:
        response = session.get(url, timeout=30)
        if response.status_code != 200:
            return []
        
        # Find individual op links: /op/Ops.Namespace.OpName
        op_pattern = r'href="/op/(Ops\.[A-Za-z0-9_.]+)"'
        op_matches = set(re.findall(op_pattern, response.text))
        
        for full_name in op_matches:
            parts = full_name.split('.')
            if len(parts) >= 3:
                op_namespace = '.'.join(parts[:-1])
                short_name = parts[-1]
                ops.append({
                    'full_name': full_name,
                    'short_name': short_name,
                    'namespace': op_namespace,
                    'url': f"{BASE_URL}/op/{full_name}"
                })
        
        # Find sub-namespace links and recursively get their ops
        sub_ns_pattern = rf'href="/ops/({re.escape(namespace)}\.[A-Za-z0-9]+)"'
        sub_namespaces = set(re.findall(sub_ns_pattern, response.text))
        
        for sub_ns in sub_namespaces:
            if sub_ns not in visited:
                log(f"  Found sub-namespace: {sub_ns}")
                time.sleep(REQUEST_DELAY)
                sub_ops = get_ops_from_namespace(sub_ns, visited)
                ops.extend(sub_ops)
        
    except Exception as e:
        log(f"Error getting {namespace}: {str(e)[:50]}", "ERROR")
    
    return ops


def scrape_op_page(full_name: str, url: str) -> Dict:
    """
    Scrape an individual op page for complete information.
    Returns dict with description, input_ports, output_ports.
    """
    op_info = {
        'full_name': full_name,
        'short_name': full_name.split('.')[-1],
        'namespace': '.'.join(full_name.split('.')[:-1]),
        'url': url,
        'description': '',
        'input_ports': [],
        'output_ports': [],
        'patch_links': [],  # List of dicts: [{'name': 'Patch Name', 'url': 'https://...'}]
        'scraped_at': datetime.now().isoformat(),
        'scrape_status': 'failed'
    }
    
    try:
        response = session.get(url, timeout=20)
        if response.status_code != 200:
            op_info['scrape_status'] = f'http_{response.status_code}'
            return op_info
        
        soup = BeautifulSoup(response.text, 'html.parser')
        page_text = soup.get_text()
        
        # ===== EXTRACT DESCRIPTION =====
        # Method 1: Look for "Summary (oneliner)" section
        summary_match = re.search(r'Summary \(oneliner\)\s*\n\s*([^\n]+)', page_text)
        if summary_match:
            desc = summary_match.group(1).strip()
            if desc and len(desc) > 3 and not desc.startswith('Issues'):
                op_info['description'] = desc
        
        # Method 2: Look after op name in the page
        if not op_info['description']:
            lines = page_text.split('\n')
            short_name = op_info['short_name']
            for i, line in enumerate(lines):
                if line.strip() == short_name and i + 1 < len(lines):
                    next_line = lines[i + 1].strip()
                    # Validate it's a description, not navigation text
                    if (next_line and len(next_line) > 10 and 
                        not next_line.startswith(('Summary', 'INPUT', 'OUTPUT', 'Full Name', 'Ops.'))):
                        op_info['description'] = next_line
                        break
        
        # ===== EXTRACT INPUT PORTS =====
        # Find INPUT PORTS section
        input_section = re.search(
            r'INPUT PORTS\s*(.*?)(?:OUTPUT PORTS|SaveCancel|Changelog|Documentation \(markdown\)|$)', 
            page_text, re.DOTALL | re.IGNORECASE
        )
        if input_section:
            input_text = input_section.group(1)
            op_info['input_ports'] = parse_ports(input_text)
        
        # ===== EXTRACT OUTPUT PORTS =====
        # Find OUTPUT PORTS section  
        output_section = re.search(
            r'OUTPUT PORTS\s*(.*?)(?:SaveCancel|Changelog|Documentation \(markdown\)|Issues|$)', 
            page_text, re.DOTALL | re.IGNORECASE
        )
        if output_section:
            output_text = output_section.group(1)
            op_info['output_ports'] = parse_ports(output_text)
        
        # ===== EXTRACT PATCH LINKS (requires JavaScript rendering) =====
        if PLAYWRIGHT_AVAILABLE:
            try:
                patch_links = extract_patch_links_with_browser(url)
                op_info['patch_links'] = patch_links
            except Exception as e:
                log(f"Failed to extract patch links for {full_name}: {e}", "WARN")
                op_info['patch_links'] = []
        else:
            # Without Playwright, we can't get patch links (they're JS-loaded)
            op_info['patch_links'] = []
        
        op_info['scrape_status'] = 'success'
        return op_info
        
    except Exception as e:
        op_info['scrape_status'] = f'error: {str(e)[:50]}'
        return op_info


def parse_ports(port_text: str) -> List[Dict]:
    """
    Parse port information from text.
    Format expected: "PortName (Type)\nDescription"
    """
    ports = []
    
    # Pattern: Name (Type) followed by description on next line
    # More flexible pattern to catch various formats
    patterns = [
        # Standard: "PortName (Type)\nDescription"
        r'([A-Za-z][A-Za-z0-9 _-]{0,50}?)\s*\(([^)]+)\)\s*\n\s*([^\n]*)',
        # Alternative: "PortName (Type): Description" on same line
        r'([A-Za-z][A-Za-z0-9 _-]{0,50}?)\s*\(([^)]+)\)\s*:\s*([^\n]*)',
    ]
    
    for pattern in patterns:
        matches = re.findall(pattern, port_text)
        for name, port_type, desc in matches:
            name = name.strip()
            # Validate this is a real port name, not garbage
            if (name and 
                len(name) < 50 and 
                not name.startswith('###') and
                not name.startswith('INPUT') and
                not name.startswith('OUTPUT') and
                not name.lower() in ['savecacnel', 'changelog', 'issues']):
                
                # Clean up description
                desc = desc.strip()
                if not desc or len(desc) < 2:
                    desc = '*See documentation*'
                
                # Avoid duplicates
                if not any(p['name'] == name for p in ports):
                    ports.append({
                        'name': name,
                        'type': port_type.strip(),
                        'description': desc
                    })
    
    return ports


def extract_patch_links_with_browser(url: str) -> List[Dict[str, str]]:
    """
    Extract patch links from an op page using Playwright (handles JavaScript).
    Returns list of dicts with 'name' and 'url' keys.
    """
    if not PLAYWRIGHT_AVAILABLE:
        return []
    
    patch_links = []
    
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            
            # Load the page - use domcontentloaded for faster loading
            page.goto(url, wait_until='domcontentloaded', timeout=30000)
            
            # Wait for patches to potentially load
            try:
                page.wait_for_selector('a[href*="/patch/"]', timeout=5000)
            except:
                pass  # Patches might not exist, that's okay
            
            time.sleep(2)  # Additional wait for dynamic content
            
            # Look for patch links - they might be in various formats
            # Method 1: Look for links with /patch/ in href
            patch_elements = page.query_selector_all('a[href*="/patch/"]')
            
            for elem in patch_elements:
                try:
                    href = elem.get_attribute('href')
                    text = elem.inner_text().strip()
                    
                    if href and '/patch/' in href:
                        # Only accept actual cables.gl patch links
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
                        
                        # Clean up the text
                        if text and len(text) > 0:
                            patch_links.append({
                                'name': text[:100],  # Limit name length
                                'url': href
                            })
                except Exception as e:
                    continue
            
            # Method 2: Look for patch links in "Patches using" section
            # Find sections containing "Patches using" text
            try:
                all_sections = page.query_selector_all('section, h2, div')
                for section in all_sections:
                    try:
                        text = section.inner_text()
                        if 'Patches using' in text or 'patches using' in text.lower():
                            # Get all links in this section
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
                                    
                                    # Avoid duplicates
                                    if not any(p['url'] == href for p in patch_links):
                                        patch_links.append({
                                            'name': link_text[:100] if link_text else 'Patch',
                                            'url': href
                                        })
                                except:
                                    continue
                            break  # Found the section, no need to continue
                    except:
                        continue
            except:
                pass
            
            browser.close()
            
    except Exception as e:
        log(f"Error extracting patch links with browser: {e}", "WARN")
    
    return patch_links


def download_op_image(full_name: str) -> bool:
    """Download the SVG layout image for an op"""
    safe_name = full_name.replace('.', '_')
    save_path = os.path.join(OUTPUT_DIR, f"{safe_name}.svg")
    
    url = f"{BASE_URL}/api/op/layout/{full_name}"
    
    try:
        response = session.get(url, timeout=15)
        if response.status_code == 200 and b'<svg' in response.content[:200]:
            os.makedirs(OUTPUT_DIR, exist_ok=True)
            with open(save_path, 'wb') as f:
                f.write(response.content)
            return True
    except Exception as e:
        log(f"Failed to download image for {full_name}: {e}", "WARN")
    
    return False


def format_port_markdown(port: Dict) -> str:
    """Format a port for markdown output"""
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
    
    md += "\n**< Output Ports:**\n\n"
    
    if op.get('output_ports'):
        for port in op['output_ports']:
            md += format_port_markdown(port) + "\n"
    else:
        md += f"- *Visit [{full_name} documentation]({url}) for output port details*\n"
    
    md += f"""
**Example Patch:** [Open in Editor]({url}#example)
"""
    
    # Add patch links if available, otherwise omit the line entirely
    if op.get('patch_links') and len(op['patch_links']) > 0:
        patch_links_text = ", ".join([f"[{p['name']}]({p['url']})" for p in op['patch_links']])
        md += f"""
**Patches Using This Op:** {patch_links_text}
"""
    # If no patches, omit the line entirely
    
    md += f"""
**Docs:** [{url}]({url})

---

"""
    return md


def generate_allops_markdown(ops_by_namespace: Dict) -> str:
    """Generate the complete AllOps.md file"""
    
    # Namespace descriptions for better documentation
    ns_descriptions = {
        "Ops.Anim": "Animation and Motion - Timing, easing, and animation utilities",
        "Ops.Array": "Array Operations - Array manipulation and iteration",
        "Ops.Audio": "Audio Processing - Audio analysis and effects",
        "Ops.Boolean": "Boolean Logic - Logical operations and comparisons",
        "Ops.Cables": "Cables Platform - Platform-specific functionality",
        "Ops.Color": "Color Manipulation - Color conversion and effects",
        "Ops.Data": "Data Handling - Data storage and retrieval",
        "Ops.Date": "Date and Time - Date/time utilities",
        "Ops.Debug": "Debugging Tools - Development and debugging",
        "Ops.Devices": "Input Devices - Mouse, keyboard, touch, gamepad",
        "Ops.Extension": "Extensions - Third-party extensions",
        "Ops.Gl": "WebGL Rendering - 3D graphics, shaders, meshes",
        "Ops.Graphics": "Graphics Utilities - 2D graphics and effects",
        "Ops.Html": "HTML DOM - HTML element manipulation",
        "Ops.Json": "JSON and HTTP - API calls and JSON handling",
        "Ops.Math": "Mathematical Operations - Math functions and utilities",
        "Ops.Net": "Networking - WebSockets and networking",
        "Ops.Number": "Number Operations - Number manipulation",
        "Ops.Sidebar": "Sidebar UI - Parameter sidebar controls",
        "Ops.String": "String Operations - Text manipulation",
        "Ops.Templates": "Templates - Op templates",
        "Ops.TimeLine": "Timeline and Sequencing - Timeline control",
        "Ops.Trigger": "Trigger Flow Control - Execution flow",
        "Ops.Ui": "User Interface - UI components",
        "Ops.Vars": "Global Variables - Variable storage",
        "Ops.WebAudio": "Web Audio API - Sound synthesis",
        "Ops.Website": "Website Integration - Website utilities",
        "Ops.User": "User Ops - Community-created operators",
        "Ops.Team": "Team Ops - Team-specific operators",
    }
    
    # Count stats
    total_ops = sum(len(ops) for ops in ops_by_namespace.values())
    total_with_ports = sum(
        1 for ops in ops_by_namespace.values() 
        for op in ops 
        if op.get('input_ports') or op.get('output_ports')
    )
    
    md = f"""# All Operators Reference

This chapter provides a comprehensive reference for all operators (ops) available in cables.gl. Each op is documented with its input/output ports, description, and links to examples and documentation.

**Statistics:** {total_ops} total ops, {total_with_ports} with port documentation

**Note:** This reference is automatically scraped from the [cables.gl ops documentation](https://cables.gl/ops/). For the most up-to-date information, visit the official documentation.

**Last Updated:** {datetime.now().strftime("%Y-%m-%d %H:%M")}

## How to Use This Reference

- **Op Name**: The full namespace and name of the operator
- **Description**: What the op does
- **> Input Ports**: Input ports with their types and descriptions
- **< Output Ports**: Output ports with their types and descriptions
- **Example Patch**: Link to open an example in the cables.gl editor
- **Patches Using This Op**: Community patches that demonstrate usage
- **Docs**: Link to the official op documentation page

---

"""
    
    # Generate sections for each namespace
    for namespace in sorted(ops_by_namespace.keys()):
        ops = ops_by_namespace[namespace]
        if not ops:
            continue
        
        # Get namespace description
        base_ns = '.'.join(namespace.split('.')[:2])
        ns_desc = ns_descriptions.get(base_ns, "")
        
        md += f"## {namespace}\n\n"
        if ns_desc:
            md += f"*{ns_desc}*\n\n"
        
        # Sort ops by short name
        for op in sorted(ops, key=lambda x: x['short_name'].lower()):
            md += generate_op_markdown(op)
    
    return md


def main():
    """Main scraping function"""
    parser = argparse.ArgumentParser(description='Thorough cables.gl op scraper')
    parser.add_argument('--namespace', type=str, help='Scrape only a specific namespace')
    parser.add_argument('--resume', action='store_true', help='Resume from last progress')
    parser.add_argument('--test', action='store_true', help='Test mode - only scrape 5 ops')
    parser.add_argument('--skip-images', action='store_true', help='Skip image downloads')
    parser.add_argument('--generate-only', action='store_true', help='Only generate markdown from existing data')
    args = parser.parse_args()
    
    # Change to script directory for relative paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    log("=" * 60)
    log("Thorough cables.gl Op Scraper")
    log("=" * 60)
    
    # If generate-only, just regenerate markdown from existing data
    if args.generate_only:
        if os.path.exists(DATA_FILE):
            log("Loading existing data and regenerating markdown...")
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                all_ops = json.load(f)
            md = generate_allops_markdown(all_ops)
            with open(MARKDOWN_FILE, 'w', encoding='utf-8') as f:
                f.write(md)
            log(f"Generated {MARKDOWN_FILE}")
            return
        else:
            log(f"No data file found at {DATA_FILE}", "ERROR")
            return
    
    # Load previous progress if resuming
    all_ops = {}
    processed_namespaces = set()
    
    if args.resume:
        progress = load_progress()
        if progress:
            all_ops = progress.get('ops', {})
            processed_namespaces = set(progress.get('processed_namespaces', []))
            log(f"Resuming from {len(processed_namespaces)} processed namespaces")
    
    # Step 1: Get all namespaces
    log("\nSTEP 1: Getting all namespaces...")
    if args.namespace:
        namespaces = [args.namespace]
    else:
        namespaces = get_all_namespaces()
    
    if not namespaces:
        log("No namespaces found!", "ERROR")
        return
    
    log(f"Will process {len(namespaces)} namespaces")
    
    # Step 2: Get all ops from each namespace
    log("\nSTEP 2: Getting ops from each namespace...")
    all_ops_list = []
    
    for ns in namespaces:
        if ns in processed_namespaces and args.resume:
            log(f"Skipping {ns} (already processed)")
            continue
        
        log(f"\nNamespace: {ns}")
        ops = get_ops_from_namespace(ns)
        log(f"  Found {len(ops)} ops")
        
        all_ops_list.extend(ops)
        time.sleep(NAMESPACE_DELAY)
    
    # Remove duplicates
    seen = set()
    unique_ops = []
    for op in all_ops_list:
        if op['full_name'] not in seen:
            seen.add(op['full_name'])
            unique_ops.append(op)
    
    log(f"\nTotal unique ops to scrape: {len(unique_ops)}")
    
    if args.test:
        unique_ops = unique_ops[:5]
        log("TEST MODE: Only scraping 5 ops")
    
    # Step 3: Scrape each op page
    log("\nSTEP 3: Scraping individual op pages...")
    
    total = len(unique_ops)
    for i, op in enumerate(unique_ops, 1):
        full_name = op['full_name']
        namespace = op['namespace']
        
        # Skip if already scraped (resume mode)
        if namespace in all_ops and any(o['full_name'] == full_name for o in all_ops[namespace]):
            continue
        
        # Progress indicator
        pct = (i / total) * 100
        sys.stdout.write(f"\r  [{i}/{total}] ({pct:.1f}%) {op['short_name'][:30]:30s}")
        sys.stdout.flush()
        
        # Scrape op page
        op_data = scrape_op_page(full_name, op['url'])
        
        # Download image
        if not args.skip_images:
            img_ok = download_op_image(full_name)
            op_data['image_downloaded'] = img_ok
        
        # Store in namespace group
        if namespace not in all_ops:
            all_ops[namespace] = []
        all_ops[namespace].append(op_data)
        
        # Status logging for detailed info
        in_ports = len(op_data.get('input_ports', []))
        out_ports = len(op_data.get('output_ports', []))
        
        # Save progress periodically
        if i % 50 == 0:
            save_progress({
                'ops': all_ops,
                'processed_namespaces': list(processed_namespaces),
                'last_updated': datetime.now().isoformat()
            })
        
        time.sleep(REQUEST_DELAY)
    
    print()  # Newline after progress
    
    # Save final data
    log("\nSTEP 4: Saving data...")
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(all_ops, f, indent=2, ensure_ascii=False)
    log(f"Saved to {DATA_FILE}")
    
    # Step 5: Generate markdown
    log("\nSTEP 5: Generating markdown...")
    md = generate_allops_markdown(all_ops)
    with open(MARKDOWN_FILE, 'w', encoding='utf-8') as f:
        f.write(md)
    log(f"Generated {MARKDOWN_FILE}")
    
    # Summary
    total_ops = sum(len(ops) for ops in all_ops.values())
    total_with_desc = sum(1 for ops in all_ops.values() for op in ops if op.get('description'))
    total_with_ports = sum(1 for ops in all_ops.values() for op in ops 
                          if op.get('input_ports') or op.get('output_ports'))
    
    log("\n" + "=" * 60)
    log("SUMMARY")
    log("=" * 60)
    log(f"Total namespaces: {len(all_ops)}")
    log(f"Total ops: {total_ops}")
    log(f"Ops with description: {total_with_desc} ({100*total_with_desc/total_ops:.1f}%)")
    log(f"Ops with ports: {total_with_ports} ({100*total_with_ports/total_ops:.1f}%)")
    log(f"Output: {MARKDOWN_FILE}")
    log(f"Images: {OUTPUT_DIR}")
    
    # Clean up progress file
    if os.path.exists(PROGRESS_FILE):
        os.remove(PROGRESS_FILE)


if __name__ == "__main__":
    main()


