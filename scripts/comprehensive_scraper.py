#!/usr/bin/env python3
"""
Comprehensive scraper for ALL cables.gl ops
Visits each individual op page to get accurate port information
Handles sub-namespaces like Ops.Extension.Ai, Ops.Gl.Matrix, etc.
"""

import requests
from bs4 import BeautifulSoup
import json
import os
import re
import time
import sys

BASE_URL = "https://cables.gl"
OUTPUT_DIR = "chapters/images/ops"

# Track progress
processed_count = 0
total_count = 0

def get_all_ops_from_main_page():
    """Get all ops by scraping the main ops page and following namespace links"""
    print("Getting all ops from cables.gl/ops...")
    
    all_ops = {}
    
    # First get main ops page to find all namespace links
    try:
        response = requests.get(f"{BASE_URL}/ops/", timeout=30, headers={'User-Agent': 'Mozilla/5.0'})
        if response.status_code != 200:
            print(f"Failed to get main ops page: {response.status_code}")
            return {}
        
        # Find all namespace links
        namespace_pattern = r'href="/ops/(Ops\.[A-Za-z0-9.]+)"'
        namespaces = list(set(re.findall(namespace_pattern, response.text)))
        print(f"Found {len(namespaces)} top-level namespaces")
        
        # Process each namespace
        for ns in sorted(namespaces):
            print(f"\nProcessing namespace: {ns}")
            ns_ops = get_ops_from_namespace(ns)
            
            for op in ns_ops:
                # Use the full namespace path
                ns_key = op['namespace']
                if ns_key not in all_ops:
                    all_ops[ns_key] = []
                all_ops[ns_key].append(op)
            
            time.sleep(0.3)
        
    except Exception as e:
        print(f"Error: {e}")
    
    return all_ops

def get_ops_from_namespace(namespace):
    """Get all ops from a namespace page, including sub-namespaces"""
    url = f"{BASE_URL}/ops/{namespace}"
    ops = []
    
    try:
        response = requests.get(url, timeout=30, headers={'User-Agent': 'Mozilla/5.0'})
        if response.status_code != 200:
            return []
        
        # Find all op links - both /op/... and /ops/...
        # Pattern for individual ops: /op/Ops.Namespace.OpName
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
        
        # Also look for sub-namespace links to scrape
        sub_ns_pattern = rf'href="/ops/({re.escape(namespace)}\.[A-Za-z0-9]+)"'
        sub_namespaces = set(re.findall(sub_ns_pattern, response.text))
        
        for sub_ns in sub_namespaces:
            if sub_ns != namespace:
                print(f"  Found sub-namespace: {sub_ns}")
                sub_ops = get_ops_from_namespace(sub_ns)
                ops.extend(sub_ops)
                time.sleep(0.2)
        
        print(f"  Found {len(ops)} ops in {namespace}")
        
    except Exception as e:
        print(f"  Error getting {namespace}: {str(e)[:50]}")
    
    return ops

def get_op_details(full_name, url):
    """Get detailed information from an individual op page"""
    global processed_count, total_count
    
    try:
        response = requests.get(url, timeout=20, headers={'User-Agent': 'Mozilla/5.0'})
        if response.status_code != 200:
            return None
        
        soup = BeautifulSoup(response.text, 'html.parser')
        page_text = soup.get_text()
        
        op_info = {
            'full_name': full_name,
            'short_name': full_name.split('.')[-1],
            'namespace': '.'.join(full_name.split('.')[:-1]),
            'url': url,
            'description': '',
            'input_ports': [],
            'output_ports': []
        }
        
        # Extract description from the page
        # Look for text after the op name heading
        lines = page_text.split('\n')
        for i, line in enumerate(lines):
            line = line.strip()
            # Look for op description - usually after the op name
            if line == op_info['short_name'] and i + 1 < len(lines):
                next_line = lines[i + 1].strip()
                if next_line and len(next_line) > 5 and not next_line.startswith('Summary'):
                    op_info['description'] = next_line
                    break
        
        # Also try Summary section
        summary_match = re.search(r'Summary \(oneliner\)\s*\n\s*([^\n]+)', page_text)
        if summary_match:
            desc = summary_match.group(1).strip()
            if desc and len(desc) > 3:
                op_info['description'] = desc
        
        # Extract INPUT PORTS
        input_section = re.search(r'INPUT PORTS\s*(.*?)(?:OUTPUT PORTS|SaveCancel|Changelog|$)', page_text, re.DOTALL | re.IGNORECASE)
        if input_section:
            input_text = input_section.group(1)
            # Parse: "PortName (Type)\nDescription"
            port_matches = re.findall(r'([A-Za-z][A-Za-z0-9 _-]{0,40}?)\s*\(([^)]+)\)\s*\n\s*([^\n]*)', input_text)
            for name, port_type, desc in port_matches:
                name = name.strip()
                if name and len(name) < 40 and not name.startswith('###'):
                    op_info['input_ports'].append({
                        'name': name,
                        'type': port_type.strip(),
                        'description': desc.strip() if desc.strip() else '*Check documentation*'
                    })
        
        # Extract OUTPUT PORTS
        output_section = re.search(r'OUTPUT PORTS\s*(.*?)(?:SaveCancel|Changelog|Documentation|Issues|$)', page_text, re.DOTALL | re.IGNORECASE)
        if output_section:
            output_text = output_section.group(1)
            port_matches = re.findall(r'([A-Za-z][A-Za-z0-9 _-]{0,40}?)\s*\(([^)]+)\)\s*\n\s*([^\n]*)', output_text)
            for name, port_type, desc in port_matches:
                name = name.strip()
                if name and len(name) < 40 and not name.startswith('###'):
                    op_info['output_ports'].append({
                        'name': name,
                        'type': port_type.strip(),
                        'description': desc.strip() if desc.strip() else '*Check documentation*'
                    })
        
        processed_count += 1
        return op_info
        
    except Exception as e:
        return None

def download_op_image(full_name):
    """Download op image"""
    safe_name = full_name.replace('.', '_')
    save_path = f"{OUTPUT_DIR}/{safe_name}.svg"
    
    url = f"{BASE_URL}/api/op/layout/{full_name}"
    try:
        response = requests.get(url, timeout=10, headers={'User-Agent': 'Mozilla/5.0'})
        if response.status_code == 200 and b'<svg' in response.content[:100]:
            os.makedirs(OUTPUT_DIR, exist_ok=True)
            with open(save_path, 'wb') as f:
                f.write(response.content)
            return True
    except:
        pass
    return False

def format_port(port):
    """Format a port for markdown"""
    name = port.get('name', '')
    port_type = port.get('type', '')
    desc = port.get('description', '*Check documentation*')
    return f"- **{name} ({port_type})**: {desc}"

def generate_op_markdown(op):
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
            md += format_port(port) + "\n"
    else:
        md += f"- *Visit [{full_name} documentation]({url}) for complete input port details*\n"
    
    md += "**< Output Ports:**\n"
    
    if op.get('output_ports'):
        for port in op['output_ports']:
            md += format_port(port) + "\n"
    else:
        md += f"- *Visit [{full_name} documentation]({url}) for complete output port details*\n"
    
    md += f"""
**Example Patch:** [Open in Editor]({url}#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "{short_name}"*
**Docs:** [{url}]({url})

---

"""
    return md

def main():
    global total_count, processed_count
    
    print("=" * 60)
    print("Comprehensive cables.gl Op Scraper")
    print("=" * 60)
    print()
    
    # Step 1: Get all ops from all namespaces
    print("STEP 1: Getting all ops from cables.gl...")
    all_ops = get_all_ops_from_main_page()
    
    # Count total
    total_count = sum(len(ops) for ops in all_ops.values())
    print(f"\nTotal ops found: {total_count}")
    print(f"Total namespaces: {len(all_ops)}")
    
    # Save the op list
    with open('all_ops_list.json', 'w', encoding='utf-8') as f:
        json.dump(all_ops, f, indent=2, ensure_ascii=False)
    print("Saved op list to all_ops_list.json")
    
    # Step 2: Get details for each op and download images
    print("\nSTEP 2: Getting details and downloading images...")
    
    detailed_ops = {}
    
    for namespace in sorted(all_ops.keys()):
        ops = all_ops[namespace]
        if not ops:
            continue
        
        print(f"\n{namespace} ({len(ops)} ops):")
        detailed_ops[namespace] = []
        
        for op in ops:
            full_name = op['full_name']
            short_name = op['short_name']
            url = op['url']
            
            # Get details
            sys.stdout.write(f"  {short_name}... ")
            sys.stdout.flush()
            
            details = get_op_details(full_name, url)
            
            # Download image
            img_ok = download_op_image(full_name)
            
            if details:
                detailed_ops[namespace].append(details)
                in_ports = len(details.get('input_ports', []))
                out_ports = len(details.get('output_ports', []))
                status = f"[{in_ports}in/{out_ports}out]"
            else:
                # Use basic info
                detailed_ops[namespace].append({
                    'full_name': full_name,
                    'short_name': short_name,
                    'namespace': namespace,
                    'url': url,
                    'description': '',
                    'input_ports': [],
                    'output_ports': []
                })
                status = "[--]"
            
            img_status = "img:OK" if img_ok else "img:--"
            print(f"{status} {img_status}")
            
            time.sleep(0.2)
        
        # Save progress
        with open('detailed_ops_data.json', 'w', encoding='utf-8') as f:
            json.dump(detailed_ops, f, indent=2, ensure_ascii=False)
    
    print(f"\nProcessed {processed_count} ops")
    
    # Step 3: Generate markdown
    print("\nSTEP 3: Generating markdown...")
    
    md_content = """# All Operators Reference

This chapter provides a comprehensive reference for all operators (ops) available in cables.gl. Each op is documented with its input/output ports, description, and links to examples and documentation.

**Note:** This reference is based on the [cables.gl ops documentation](https://cables.gl/ops/). For the most up-to-date information, visit the official documentation.

## How to Use This Reference

- **Op Name**: The full namespace and name of the operator
- **Description**: What the op does
- **Input Ports**: All input ports with their types and descriptions
- **Output Ports**: All output ports with their types and descriptions
- **Example Patch**: Link to open an example in the cables.gl editor
- **Patches Using This Op**: Community patches that demonstrate usage
- **Docs**: Link to the official op documentation page

---

"""
    
    for namespace in sorted(detailed_ops.keys()):
        ops = detailed_ops[namespace]
        if not ops:
            continue
        
        md_content += f"## {namespace}\n\n"
        
        for op in sorted(ops, key=lambda x: x['short_name']):
            md_content += generate_op_markdown(op)
    
    with open('chapters/13-AllOps.md', 'w', encoding='utf-8') as f:
        f.write(md_content)
    
    print("Generated chapters/13-AllOps.md")
    
    # Summary
    total_final = sum(len(ops) for ops in detailed_ops.values())
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Total namespaces: {len(detailed_ops)}")
    print(f"Total ops: {total_final}")
    print(f"Output file: chapters/13-AllOps.md")
    print(f"Images directory: {OUTPUT_DIR}")

if __name__ == "__main__":
    main()

