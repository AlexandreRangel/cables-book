#!/usr/bin/env python3
"""
Full scraper for ALL cables.gl ops
Gets all ops, downloads images, scrapes port info
"""

import requests
from bs4 import BeautifulSoup
import json
import os
import re
import time
import sys

BASE_URL = 'https://cables.gl'
OUTPUT_DIR = 'chapters/images/ops'

def get_all_ops():
    """Get all ops from the main ops page"""
    print("Getting all ops from cables.gl/ops/...")
    
    response = requests.get(f'{BASE_URL}/ops/', timeout=60, headers={'User-Agent': 'Mozilla/5.0'})
    if response.status_code != 200:
        print(f"Failed: {response.status_code}")
        return {}, []
    
    # Find namespace links
    namespace_pattern = r'href="/ops/(Ops\.[A-Za-z0-9.]+)"'
    namespaces = sorted(set(re.findall(namespace_pattern, response.text)))
    
    # Find all op links
    op_pattern = r'href="/op/(Ops\.[A-Za-z0-9_.]+)"'
    all_ops = sorted(set(re.findall(op_pattern, response.text)))
    
    print(f"Found {len(namespaces)} namespaces")
    print(f"Found {len(all_ops)} ops")
    
    # Organize by namespace
    ops_by_ns = {}
    for op in all_ops:
        parts = op.split('.')
        ns = '.'.join(parts[:-1])
        if ns not in ops_by_ns:
            ops_by_ns[ns] = []
        ops_by_ns[ns].append({
            'full_name': op,
            'short_name': parts[-1],
            'namespace': ns,
            'url': f'{BASE_URL}/op/{op}'
        })
    
    return ops_by_ns, namespaces

def get_op_details(op):
    """Get detailed info from op page"""
    url = op['url']
    
    try:
        response = requests.get(url, timeout=20, headers={'User-Agent': 'Mozilla/5.0'})
        if response.status_code != 200:
            return op
        
        page_text = BeautifulSoup(response.text, 'html.parser').get_text()
        
        # Get description
        short_name = op['short_name']
        lines = [l.strip() for l in page_text.split('\n') if l.strip()]
        
        # Look for description after op name
        for i, line in enumerate(lines):
            if line == short_name and i + 1 < len(lines):
                next_line = lines[i + 1]
                if next_line and len(next_line) > 5 and not next_line.startswith('Summary'):
                    op['description'] = next_line
                    break
        
        # Try Summary section
        summary_match = re.search(r'Summary \(oneliner\)\s*([^\n]+)', page_text)
        if summary_match:
            desc = summary_match.group(1).strip()
            if desc and len(desc) > 3:
                op['description'] = desc
        
        # INPUT PORTS
        op['input_ports'] = []
        input_match = re.search(r'INPUT PORTS\s*(.*?)(?:OUTPUT PORTS|SaveCancel|Changelog|$)', page_text, re.DOTALL | re.IGNORECASE)
        if input_match:
            input_text = input_match.group(1)
            port_pattern = r'([A-Za-z][A-Za-z0-9 _-]{0,35}?)\s*\(([^)]+)\)\s*\n\s*([^\n]*)'
            for match in re.finditer(port_pattern, input_text):
                name, ptype, desc = match.groups()
                name = name.strip()
                if name and len(name) < 35:
                    op['input_ports'].append({
                        'name': name,
                        'type': ptype.strip(),
                        'description': desc.strip() or '*Check documentation*'
                    })
        
        # OUTPUT PORTS
        op['output_ports'] = []
        output_match = re.search(r'OUTPUT PORTS\s*(.*?)(?:SaveCancel|Changelog|Documentation|Issues|$)', page_text, re.DOTALL | re.IGNORECASE)
        if output_match:
            output_text = output_match.group(1)
            for match in re.finditer(port_pattern, output_text):
                name, ptype, desc = match.groups()
                name = name.strip()
                if name and len(name) < 35:
                    op['output_ports'].append({
                        'name': name,
                        'type': ptype.strip(),
                        'description': desc.strip() or '*Check documentation*'
                    })
        
        return op
        
    except Exception as e:
        return op

def download_image(full_name):
    """Download op image"""
    safe_name = full_name.replace('.', '_')
    save_path = f'{OUTPUT_DIR}/{safe_name}.svg'
    
    if os.path.exists(save_path):
        return True
    
    url = f'{BASE_URL}/api/op/layout/{full_name}'
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
    name = port.get('name', '')
    ptype = port.get('type', '')
    desc = port.get('description', '*Check documentation*')
    return f"- **{name} ({ptype})**: {desc}"

def generate_markdown(ops_by_ns):
    """Generate the AllOps markdown file"""
    md = """# All Operators Reference

This chapter provides a comprehensive reference for all operators (ops) available in cables.gl.

**Note:** This reference is based on the [cables.gl ops documentation](https://cables.gl/ops/). For the most up-to-date information, visit the official documentation.

## How to Use This Reference

- **Op Name**: The full namespace and name of the operator
- **Description**: What the op does
- **> Input Ports**: Input ports with their types and descriptions
- **< Output Ports**: Output ports with their types and descriptions
- **Docs**: Link to the official op documentation page

---

"""
    
    for ns in sorted(ops_by_ns.keys()):
        ops = ops_by_ns[ns]
        if not ops:
            continue
        
        md += f"## {ns}\n\n"
        
        for op in sorted(ops, key=lambda x: x['short_name']):
            full_name = op['full_name']
            short_name = op['short_name']
            url = op['url']
            desc = op.get('description', f"*Visit [documentation]({url}) for details*")
            if not desc:
                desc = f"*Visit [documentation]({url}) for details*"
            
            safe_name = full_name.replace('.', '_')
            
            md += f"""### {short_name}
![{short_name} op](images/ops/{safe_name}.svg)

**Full Name:** `{full_name}`
**Description:** {desc}

**> Input Ports:**
"""
            
            if op.get('input_ports'):
                for port in op['input_ports']:
                    md += format_port(port) + "\n"
            else:
                md += f"- *Visit [{full_name} documentation]({url}) for input port details*\n"
            
            md += "**< Output Ports:**\n"
            
            if op.get('output_ports'):
                for port in op['output_ports']:
                    md += format_port(port) + "\n"
            else:
                md += f"- *Visit [{full_name} documentation]({url}) for output port details*\n"
            
            md += f"""
**Example Patch:** [Open in Editor]({url}#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "{short_name}"*
**Docs:** [{url}]({url})

---

"""
    
    return md

def main():
    print("=" * 60)
    print("cables.gl Comprehensive Op Scraper")
    print("=" * 60)
    print()
    
    # Step 1: Get all ops
    ops_by_ns, namespaces = get_all_ops()
    total = sum(len(ops) for ops in ops_by_ns.values())
    
    if total == 0:
        print("No ops found!")
        return
    
    print(f"\nTotal: {total} ops in {len(ops_by_ns)} namespaces")
    
    # Save op list
    with open('all_ops_complete.json', 'w', encoding='utf-8') as f:
        json.dump(ops_by_ns, f, indent=2, ensure_ascii=False)
    print("Saved op list to all_ops_complete.json")
    
    # Step 2: Get details and download images
    print("\nGetting details and downloading images...")
    print("This will take a while for", total, "ops...\n")
    
    processed = 0
    for ns in sorted(ops_by_ns.keys()):
        ops = ops_by_ns[ns]
        print(f"{ns} ({len(ops)} ops):")
        
        for i, op in enumerate(ops):
            sys.stdout.write(f"\r  [{i+1}/{len(ops)}] {op['short_name']}...                    ")
            sys.stdout.flush()
            
            # Get details
            updated_op = get_op_details(op)
            ops[i] = updated_op
            
            # Download image
            download_image(op['full_name'])
            
            processed += 1
            time.sleep(0.15)  # Rate limiting
        
        print(f"\r  Done: {len(ops)} ops                              ")
        
        # Save progress
        with open('ops_with_details.json', 'w', encoding='utf-8') as f:
            json.dump(ops_by_ns, f, indent=2, ensure_ascii=False)
    
    print(f"\nProcessed {processed} ops")
    
    # Step 3: Generate markdown
    print("\nGenerating markdown...")
    md = generate_markdown(ops_by_ns)
    
    with open('chapters/13-AllOps.md', 'w', encoding='utf-8') as f:
        f.write(md)
    
    # Count images
    img_count = len([f for f in os.listdir(OUTPUT_DIR) if f.endswith('.svg')]) if os.path.exists(OUTPUT_DIR) else 0
    
    print("\n" + "=" * 60)
    print("DONE!")
    print("=" * 60)
    print(f"Namespaces: {len(ops_by_ns)}")
    print(f"Total ops: {processed}")
    print(f"Images: {img_count}")
    print(f"Output: chapters/13-AllOps.md")

if __name__ == "__main__":
    main()

