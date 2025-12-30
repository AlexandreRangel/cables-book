#!/usr/bin/env python3
"""
Scrape correct op information from cables.gl
Gets accurate op names, descriptions, ports, and images
"""

import requests
from bs4 import BeautifulSoup
import json
import os
import re
import time

BASE_URL = "https://cables.gl"

def get_op_info(op_url):
    """Scrape individual op page for accurate information"""
    try:
        response = requests.get(op_url, timeout=15, headers={'User-Agent': 'Mozilla/5.0'})
        if response.status_code != 200:
            return None
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        op_info = {
            'url': op_url,
            'full_name': None,
            'short_name': None,
            'description': None,
            'input_ports': [],
            'output_ports': []
        }
        
        # Get the full name - usually in a specific element
        # Look for "Full Name" text
        page_text = soup.get_text()
        
        # Find Full Name pattern
        full_name_match = re.search(r'Full Name\s*\n?\s*Ops\.[A-Za-z0-9_.]+', page_text)
        if full_name_match:
            full_name = re.search(r'Ops\.[A-Za-z0-9_.]+', full_name_match.group(0))
            if full_name:
                op_info['full_name'] = full_name.group(0)
                op_info['short_name'] = op_info['full_name'].split('.')[-1]
        
        # Look for Summary or Description
        summary_match = re.search(r'Summary \(oneliner\)\s*\n\s*([^\n]+)', page_text)
        if summary_match:
            op_info['description'] = summary_match.group(1).strip()
        
        # Look for INPUT PORTS section
        input_section = re.search(r'INPUT PORTS\s*(.*?)(?:OUTPUT PORTS|$)', page_text, re.DOTALL)
        if input_section:
            input_text = input_section.group(1)
            # Parse port entries - format: "PortName (Type)\nDescription"
            port_matches = re.findall(r'([A-Za-z][A-Za-z0-9 ]*)\s*\(([^)]+)\)\s*\n\s*([^\n]+)', input_text)
            for name, port_type, desc in port_matches:
                op_info['input_ports'].append({
                    'name': name.strip(),
                    'type': port_type.strip(),
                    'description': desc.strip()
                })
        
        # Look for OUTPUT PORTS section
        output_section = re.search(r'OUTPUT PORTS\s*(.*?)(?:SaveCancel|Changelog|$)', page_text, re.DOTALL)
        if output_section:
            output_text = output_section.group(1)
            port_matches = re.findall(r'([A-Za-z][A-Za-z0-9 ]*)\s*\(([^)]+)\)\s*\n\s*([^\n]+)', output_text)
            for name, port_type, desc in port_matches:
                op_info['output_ports'].append({
                    'name': name.strip(),
                    'type': port_type.strip(),
                    'description': desc.strip()
                })
        
        return op_info
        
    except Exception as e:
        print(f"  Error scraping {op_url}: {str(e)[:50]}")
        return None

def get_namespace_ops(namespace_url, namespace_name):
    """Get all ops from a namespace page"""
    try:
        response = requests.get(namespace_url, timeout=15, headers={'User-Agent': 'Mozilla/5.0'})
        if response.status_code != 200:
            return []
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        ops = []
        # Look for links to individual ops
        for link in soup.find_all('a', href=True):
            href = link.get('href', '')
            # Match pattern /op/Ops.Namespace.OpName or /ops/Ops.Namespace.OpName
            if '/op/' in href or '/ops/' in href:
                # Extract full op name
                match = re.search(r'(Ops\.[A-Za-z0-9_.]+)', href)
                if match:
                    full_name = match.group(1)
                    # Only include ops from this namespace (or sub-namespaces)
                    if full_name.startswith(namespace_name + '.'):
                        # Count dots to determine if it's an op or sub-namespace
                        parts = full_name.split('.')
                        if len(parts) >= 3:  # At least Ops.Namespace.OpName
                            if full_name not in [o['full_name'] for o in ops]:
                                ops.append({
                                    'full_name': full_name,
                                    'short_name': parts[-1],
                                    'url': f"{BASE_URL}/op/{full_name}"
                                })
        
        return ops
        
    except Exception as e:
        print(f"  Error getting namespace {namespace_url}: {str(e)[:50]}")
        return []

def get_all_namespaces():
    """Get all namespaces from the main ops page"""
    try:
        response = requests.get(f"{BASE_URL}/ops/", timeout=15, headers={'User-Agent': 'Mozilla/5.0'})
        if response.status_code != 200:
            print(f"Failed to get ops page: {response.status_code}")
            return []
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        namespaces = []
        # Look for namespace links
        for link in soup.find_all('a', href=True):
            href = link.get('href', '')
            # Match /ops/Ops.NamespaceName
            match = re.search(r'/ops/(Ops\.[A-Za-z]+)/?$', href)
            if match:
                ns_name = match.group(1)
                if ns_name not in namespaces:
                    namespaces.append(ns_name)
        
        return sorted(namespaces)
        
    except Exception as e:
        print(f"Error getting namespaces: {e}")
        return []

def download_op_image(full_name, output_dir):
    """Download op image from cables.gl API"""
    safe_name = full_name.replace('.', '_')
    save_path = f"{output_dir}/{safe_name}.svg"
    
    if os.path.exists(save_path):
        return True
    
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
    print("Scraping correct op information from cables.gl...")
    
    # Get all namespaces
    print("\nStep 1: Getting namespaces...")
    namespaces = get_all_namespaces()
    print(f"Found {len(namespaces)} namespaces: {namespaces}")
    
    if not namespaces:
        print("No namespaces found, using default list...")
        namespaces = ["Ops.Anim", "Ops.Array", "Ops.Boolean", "Ops.Color", "Ops.Dev", 
                      "Ops.Devices", "Ops.Gl", "Ops.Html", "Ops.Json", "Ops.Math",
                      "Ops.Number", "Ops.Object", "Ops.Sequence", "Ops.Sidebar",
                      "Ops.String", "Ops.Trigger", "Ops.Ui", "Ops.Vars", "Ops.WebAudio"]
    
    all_ops = []
    
    # Get ops from each namespace
    print("\nStep 2: Getting ops from each namespace...")
    for ns in namespaces[:5]:  # Start with first 5 for testing
        print(f"\n{ns}:")
        ns_url = f"{BASE_URL}/ops/{ns}"
        ops = get_namespace_ops(ns_url, ns)
        print(f"  Found {len(ops)} ops")
        
        # Get detailed info for first few ops
        for i, op in enumerate(ops[:3]):  # First 3 ops for testing
            print(f"    Scraping {op['short_name']}...")
            detailed = get_op_info(op['url'])
            if detailed:
                op.update(detailed)
            time.sleep(0.5)
        
        all_ops.extend(ops)
        time.sleep(1)
    
    print(f"\n\nTotal ops found: {len(all_ops)}")
    
    # Save to JSON
    with open('correct_ops_data.json', 'w', encoding='utf-8') as f:
        json.dump(all_ops, f, indent=2, ensure_ascii=False)
    
    print("\nSaved to correct_ops_data.json")
    
    # Show sample
    print("\nSample ops:")
    for op in all_ops[:5]:
        print(f"  {op.get('full_name', 'Unknown')}: {op.get('description', 'No description')}")

if __name__ == "__main__":
    main()

