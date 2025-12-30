#!/usr/bin/env python3
"""
Regenerate AllOps chapter with correct op names and information from cables.gl
"""

import requests
from bs4 import BeautifulSoup
import json
import os
import re
import time

BASE_URL = "https://cables.gl"
OUTPUT_DIR = "chapters/images/ops"

def get_op_details(full_name):
    """Get op details from the op page"""
    url = f"{BASE_URL}/op/{full_name}"
    
    try:
        response = requests.get(url, timeout=15, headers={'User-Agent': 'Mozilla/5.0'})
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
        
        # Extract description - look for Summary section
        summary_match = re.search(r'Summary \(oneliner\)\s*\n\s*([^\n]+)', page_text)
        if summary_match:
            desc = summary_match.group(1).strip()
            if desc and len(desc) > 3:
                op_info['description'] = desc
        
        # If no summary, try Documentation section
        if not op_info['description']:
            doc_match = re.search(r'Documentation \(markdown\)\s*\n\s*([^\n]+)', page_text)
            if doc_match:
                desc = doc_match.group(1).strip()
                if desc and len(desc) > 3 and not desc.startswith('Issues'):
                    op_info['description'] = desc
        
        # Extract INPUT PORTS section
        input_section = re.search(r'INPUT PORTS\s*(.*?)(?:OUTPUT PORTS|$)', page_text, re.DOTALL | re.IGNORECASE)
        if input_section:
            input_text = input_section.group(1)
            # Parse port entries: "PortName (Type)\nDescription"
            port_pattern = r'([A-Za-z][A-Za-z0-9 _-]*?)\s*\(([^)]+)\)\s*\n\s*([^\n]*)'
            for match in re.finditer(port_pattern, input_text):
                name, port_type, desc = match.groups()
                name = name.strip()
                if name and not name.startswith('###') and len(name) < 50:
                    op_info['input_ports'].append({
                        'name': name,
                        'type': port_type.strip(),
                        'description': desc.strip() if desc.strip() else '*Check documentation*'
                    })
        
        # Extract OUTPUT PORTS section
        output_section = re.search(r'OUTPUT PORTS\s*(.*?)(?:SaveCancel|Changelog|Documentation \(markdown\)|$)', page_text, re.DOTALL | re.IGNORECASE)
        if output_section:
            output_text = output_section.group(1)
            port_pattern = r'([A-Za-z][A-Za-z0-9 _-]*?)\s*\(([^)]+)\)\s*\n\s*([^\n]*)'
            for match in re.finditer(port_pattern, output_text):
                name, port_type, desc = match.groups()
                name = name.strip()
                if name and not name.startswith('###') and len(name) < 50:
                    op_info['output_ports'].append({
                        'name': name,
                        'type': port_type.strip(),
                        'description': desc.strip() if desc.strip() else '*Check documentation*'
                    })
        
        return op_info
        
    except Exception as e:
        return None

def download_op_image(full_name):
    """Download op image with correct name"""
    safe_name = full_name.replace('.', '_')
    save_path = f"{OUTPUT_DIR}/{safe_name}.svg"
    
    # Always download to ensure we have the correct image
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
    
    # Image
    safe_name = full_name.replace('.', '_')
    image_path = f"images/ops/{safe_name}.svg"
    
    # Build markdown
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
    print("Regenerating AllOps chapter with correct data from cables.gl...")
    print()
    
    # Load the correct op list
    with open('all_correct_ops.json', 'r', encoding='utf-8') as f:
        all_ops = json.load(f)
    
    # Count total ops
    total_ops = sum(len(ops) for ops in all_ops.values())
    print(f"Total ops to process: {total_ops}")
    
    # Process each namespace
    all_op_data = {}
    processed = 0
    
    for namespace in sorted(all_ops.keys()):
        ops = all_ops[namespace]
        if not ops:
            continue
        
        print(f"\n{namespace} ({len(ops)} ops):")
        all_op_data[namespace] = []
        
        for op in ops:
            full_name = op['full_name']
            short_name = op['short_name']
            
            # Download image
            img_ok = download_op_image(full_name)
            
            # Get details
            details = get_op_details(full_name)
            
            if details:
                all_op_data[namespace].append(details)
                status = "[OK]" if img_ok else "[!]"
            else:
                # Use basic info
                all_op_data[namespace].append({
                    'full_name': full_name,
                    'short_name': short_name,
                    'namespace': namespace,
                    'url': f"{BASE_URL}/op/{full_name}",
                    'description': '',
                    'input_ports': [],
                    'output_ports': []
                })
                status = "[--]"
            
            processed += 1
            print(f"  {status} {short_name}")
            
            # Rate limiting
            time.sleep(0.3)
        
        # Save progress after each namespace
        with open('complete_ops_data.json', 'w', encoding='utf-8') as f:
            json.dump(all_op_data, f, indent=2, ensure_ascii=False)
    
    print(f"\n\nProcessed {processed} ops")
    print("Saved to complete_ops_data.json")
    
    # Generate markdown
    print("\nGenerating markdown...")
    
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
    
    # Namespace descriptions
    ns_descriptions = {
        "Ops.Anim": "Animation and Motion",
        "Ops.Array": "Array Operations",
        "Ops.Audio": "Audio Processing",
        "Ops.Boolean": "Boolean Logic",
        "Ops.Cables": "Cables Platform",
        "Ops.Color": "Color Manipulation",
        "Ops.Data": "Data Handling",
        "Ops.Date": "Date and Time",
        "Ops.Debug": "Debugging Tools",
        "Ops.Devices": "Input Devices",
        "Ops.Gl": "WebGL Rendering",
        "Ops.Graphics": "Graphics Utilities",
        "Ops.Html": "HTML DOM",
        "Ops.Json": "JSON and HTTP",
        "Ops.Math": "Mathematical Operations",
        "Ops.Net": "Networking",
        "Ops.Number": "Number Operations",
        "Ops.Sidebar": "Sidebar UI",
        "Ops.String": "String Operations",
        "Ops.Templates": "Templates",
        "Ops.TimeLine": "Timeline and Sequencing",
        "Ops.Trigger": "Trigger Flow Control",
        "Ops.Ui": "User Interface",
        "Ops.Vars": "Global Variables",
        "Ops.WebAudio": "Web Audio API",
        "Ops.Website": "Website Integration",
    }
    
    for namespace in sorted(all_op_data.keys()):
        ops = all_op_data[namespace]
        if not ops:
            continue
        
        desc = ns_descriptions.get(namespace, "")
        md_content += f"## {namespace}\n\n"
        if desc:
            md_content += f"*{desc}*\n\n"
        
        for op in sorted(ops, key=lambda x: x['short_name']):
            md_content += generate_op_markdown(op)
    
    # Write markdown
    with open('chapters/13-AllOps.md', 'w', encoding='utf-8') as f:
        f.write(md_content)
    
    print("Generated chapters/13-AllOps.md")
    print(f"Total namespaces: {len(all_op_data)}")
    print(f"Total ops: {sum(len(ops) for ops in all_op_data.values())}")

if __name__ == "__main__":
    main()

