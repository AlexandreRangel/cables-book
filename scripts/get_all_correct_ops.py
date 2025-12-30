#!/usr/bin/env python3
"""
Get all correct op names from cables.gl by scraping namespace pages
"""

import requests
from bs4 import BeautifulSoup
import json
import os
import re
import time

BASE_URL = "https://cables.gl"

# All namespaces to scrape
NAMESPACES = [
    "Ops.Anim", "Ops.Array", "Ops.Audio", "Ops.Boolean", "Ops.Cables", 
    "Ops.Color", "Ops.Data", "Ops.Date", "Ops.Debug", "Ops.Devices",
    "Ops.Extension", "Ops.Gl", "Ops.Graphics", "Ops.Html", "Ops.Json",
    "Ops.Math", "Ops.Net", "Ops.Number", "Ops.Sidebar", "Ops.String",
    "Ops.Templates", "Ops.TimeLine", "Ops.Trigger", "Ops.Ui", "Ops.Vars",
    "Ops.WebAudio", "Ops.Website"
]

def get_ops_from_namespace_page(namespace):
    """Get all op names from a namespace page"""
    url = f"{BASE_URL}/ops/{namespace}"
    
    try:
        response = requests.get(url, timeout=15, headers={'User-Agent': 'Mozilla/5.0'})
        if response.status_code != 200:
            print(f"  Failed to get {namespace}: HTTP {response.status_code}")
            return []
        
        # Find all op links using regex
        pattern = rf'href="/op/({re.escape(namespace)}\.[A-Za-z0-9_]+)"'
        matches = re.findall(pattern, response.text)
        
        # Get unique op names
        ops = list(set(matches))
        return sorted(ops)
        
    except Exception as e:
        print(f"  Error getting {namespace}: {str(e)[:50]}")
        return []

def get_op_details(full_name):
    """Get op details from the op page"""
    url = f"{BASE_URL}/op/{full_name}"
    
    try:
        response = requests.get(url, timeout=15, headers={'User-Agent': 'Mozilla/5.0'})
        if response.status_code != 200:
            return None
        
        text = response.text
        
        op_info = {
            'full_name': full_name,
            'short_name': full_name.split('.')[-1],
            'namespace': '.'.join(full_name.split('.')[:-1]),
            'url': url,
            'description': '',
            'input_ports': [],
            'output_ports': []
        }
        
        # Extract description from summary
        # Pattern: "Summary (oneliner)" followed by description
        soup = BeautifulSoup(text, 'html.parser')
        page_text = soup.get_text()
        
        # Look for description in various patterns
        desc_patterns = [
            r'Summary \(oneliner\)\s*\n\s*([^\n]+)',
            r'Documentation \(markdown\)\s*\n\s*([^\n]+)',
        ]
        
        for pattern in desc_patterns:
            match = re.search(pattern, page_text)
            if match:
                desc = match.group(1).strip()
                if desc and len(desc) > 3 and not desc.startswith('Issues'):
                    op_info['description'] = desc
                    break
        
        # Extract input ports
        # Pattern: "INPUT PORTS" section
        input_match = re.search(r'INPUT PORTS\s*(.*?)(?:OUTPUT PORTS|SaveCancel|$)', page_text, re.DOTALL | re.IGNORECASE)
        if input_match:
            input_text = input_match.group(1)
            # Parse port entries
            port_pattern = r'([A-Za-z][A-Za-z0-9 _-]*?)\s*\(([^)]+)\)\s*\n\s*([^\n]*)'
            for match in re.finditer(port_pattern, input_text):
                name, port_type, desc = match.groups()
                if name.strip() and not name.strip().startswith('###'):
                    op_info['input_ports'].append({
                        'name': name.strip(),
                        'type': port_type.strip(),
                        'description': desc.strip() if desc.strip() else '*Check documentation*'
                    })
        
        # Extract output ports
        output_match = re.search(r'OUTPUT PORTS\s*(.*?)(?:SaveCancel|Changelog|Documentation|$)', page_text, re.DOTALL | re.IGNORECASE)
        if output_match:
            output_text = output_match.group(1)
            port_pattern = r'([A-Za-z][A-Za-z0-9 _-]*?)\s*\(([^)]+)\)\s*\n\s*([^\n]*)'
            for match in re.finditer(port_pattern, output_text):
                name, port_type, desc = match.groups()
                if name.strip() and not name.strip().startswith('###'):
                    op_info['output_ports'].append({
                        'name': name.strip(),
                        'type': port_type.strip(),
                        'description': desc.strip() if desc.strip() else '*Check documentation*'
                    })
        
        return op_info
        
    except Exception as e:
        print(f"    Error getting details for {full_name}: {str(e)[:50]}")
        return None

def download_op_image(full_name, output_dir):
    """Download op image"""
    safe_name = full_name.replace('.', '_')
    save_path = f"{output_dir}/{safe_name}.svg"
    
    url = f"{BASE_URL}/api/op/layout/{full_name}"
    try:
        response = requests.get(url, timeout=10, headers={'User-Agent': 'Mozilla/5.0'})
        if response.status_code == 200 and b'<svg' in response.content[:100]:
            with open(save_path, 'wb') as f:
                f.write(response.content)
            return True
    except:
        pass
    return False

def main():
    print("Getting all correct op names from cables.gl...")
    print()
    
    all_ops = {}  # namespace -> list of op info
    total_ops = 0
    
    for namespace in NAMESPACES:
        print(f"{namespace}:")
        ops = get_ops_from_namespace_page(namespace)
        print(f"  Found {len(ops)} ops")
        
        if ops:
            all_ops[namespace] = []
            for op_name in ops:
                all_ops[namespace].append({
                    'full_name': op_name,
                    'short_name': op_name.split('.')[-1],
                    'url': f"{BASE_URL}/op/{op_name}"
                })
            total_ops += len(ops)
        
        time.sleep(0.5)
    
    print(f"\nTotal ops found: {total_ops}")
    
    # Save to JSON
    with open('all_correct_ops.json', 'w', encoding='utf-8') as f:
        json.dump(all_ops, f, indent=2, ensure_ascii=False)
    
    print("Saved op list to all_correct_ops.json")
    
    # Now get details for a sample of ops to verify
    print("\nGetting details for sample ops...")
    sample_ops = []
    for namespace in ['Ops.Math', 'Ops.Boolean']:
        if namespace in all_ops:
            for op in all_ops[namespace][:3]:
                print(f"  {op['full_name']}...")
                details = get_op_details(op['full_name'])
                if details:
                    sample_ops.append(details)
                time.sleep(0.3)
    
    print("\nSample op details:")
    for op in sample_ops:
        print(f"  {op['full_name']}")
        print(f"    Description: {op['description'][:60]}..." if op['description'] else "    Description: None")
        print(f"    Input ports: {len(op['input_ports'])}")
        print(f"    Output ports: {len(op['output_ports'])}")
    
    # Save sample details
    with open('sample_op_details.json', 'w', encoding='utf-8') as f:
        json.dump(sample_ops, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    main()

