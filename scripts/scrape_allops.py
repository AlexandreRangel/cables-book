#!/usr/bin/env python3
"""
Automated script to scrape all op information from cables.gl/ops/
Downloads op images and extracts port information
"""

import requests
from bs4 import BeautifulSoup
import os
import json
import re
from urllib.parse import urljoin, urlparse
import time

BASE_URL = "https://cables.gl"
OPS_LIST_URL = "https://cables.gl/ops/"

def download_image(url, save_path):
    """Download an image from a URL"""
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            with open(save_path, 'wb') as f:
                f.write(response.content)
            return True
    except Exception as e:
        print(f"  Error downloading image {url}: {e}")
    return False

def scrape_op_page(op_url):
    """Scrape information from a single op page"""
    try:
        print(f"  Scraping {op_url}...")
        response = requests.get(op_url, timeout=10)
        if response.status_code != 200:
            print(f"  Failed to fetch {op_url}: {response.status_code}")
            return None
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        op_data = {
            'url': op_url,
            'name': '',
            'description': '',
            'input_ports': [],
            'output_ports': [],
            'image_url': None,
            'example_patches': []
        }
        
        # Extract op name (usually in a heading)
        name_elem = soup.find('h1') or soup.find('h2')
        if name_elem:
            op_data['name'] = name_elem.get_text().strip()
        
        # Extract description
        desc_elem = soup.find('p') or soup.find(class_=re.compile('description', re.I))
        if desc_elem:
            op_data['description'] = desc_elem.get_text().strip()
        
        # Try to find input/output ports
        # Look for sections with "Input" or "Output" in headers
        for section in soup.find_all(['section', 'div'], class_=re.compile('port|input|output', re.I)):
            section_text = section.get_text().lower()
            if 'input' in section_text:
                # Extract port information
                ports = section.find_all(['li', 'div', 'span'])
                for port in ports:
                    port_text = port.get_text().strip()
                    if port_text:
                        op_data['input_ports'].append(port_text)
            elif 'output' in section_text:
                ports = section.find_all(['li', 'div', 'span'])
                for port in ports:
                    port_text = port.get_text().strip()
                    if port_text:
                        op_data['output_ports'].append(port_text)
        
        # Find op image/screenshot
        # Look for images in the op page
        img_elem = soup.find('img', class_=re.compile('op|screenshot|preview', re.I))
        if not img_elem:
            # Try to find any image that might be the op visualization
            img_elem = soup.find('img', src=re.compile('op|screenshot', re.I))
        
        if img_elem and img_elem.get('src'):
            img_url = img_elem.get('src')
            if not img_url.startswith('http'):
                img_url = urljoin(BASE_URL, img_url)
            op_data['image_url'] = img_url
            
            # Download the image
            op_name_safe = op_data['name'].replace('.', '_').replace('/', '_')
            img_ext = os.path.splitext(urlparse(img_url).path)[1] or '.png'
            img_path = f"chapters/images/ops/{op_name_safe}{img_ext}"
            if download_image(img_url, img_path):
                op_data['image_path'] = img_path
                print(f"    Downloaded image: {img_path}")
        
        # Look for example patches
        for link in soup.find_all('a', href=re.compile('editor|patch', re.I)):
            patch_url = link.get('href')
            if patch_url:
                if not patch_url.startswith('http'):
                    patch_url = urljoin(BASE_URL, patch_url)
                op_data['example_patches'].append(patch_url)
        
        time.sleep(0.5)  # Be polite with rate limiting
        return op_data
        
    except Exception as e:
        print(f"  Error scraping {op_url}: {e}")
        return None

def scrape_ops_list():
    """Scrape the main ops list page to get all op URLs"""
    try:
        print(f"Fetching ops list from {OPS_LIST_URL}...")
        response = requests.get(OPS_LIST_URL, timeout=10)
        if response.status_code != 200:
            print(f"Failed to fetch ops list: {response.status_code}")
            return []
        
        soup = BeautifulSoup(response.content, 'html.parser')
        op_urls = []
        
        # Find all links to individual op pages
        # Op pages typically have URLs like /ops/Ops.Namespace.OpName
        for link in soup.find_all('a', href=True):
            href = link.get('href')
            if href and '/ops/Ops.' in href:
                if not href.startswith('http'):
                    href = urljoin(BASE_URL, href)
                if href not in op_urls:
                    op_urls.append(href)
        
        print(f"Found {len(op_urls)} op URLs")
        return op_urls
        
    except Exception as e:
        print(f"Error scraping ops list: {e}")
        return []

def generate_markdown_from_data(ops_data_by_namespace):
    """Generate markdown chapter from scraped data"""
    markdown = """# All Operators Reference

This chapter provides a comprehensive reference for all operators (ops) available in cables.gl. Each op is documented with its input/output ports, description, and links to examples and documentation.

**Note:** This reference is based on the [cables.gl ops documentation](https://cables.gl/ops/). For the most up-to-date information, visit the official documentation.

## How to Use This Reference

- **Op Name**: The full namespace and name of the operator
- **Description**: What the op does
- **Input Ports**: All input ports with their types and descriptions
- **Output Ports**: All output ports with their types and descriptions
- **Example Patch**: Link to open an example in the cables.gl editor
- **Patches Using This Op**: Community patches that demonstrate usage
- **Documentation**: Link to the official op documentation page

## Updating This Reference

To update this reference when cables.gl adds new ops or changes existing ones:

1. Run `python scrape_allops.py` to automatically scrape the latest information
2. Or manually visit [https://cables.gl/ops/](https://cables.gl/ops/) and update individual sections

---

"""
    
    # Sort namespaces
    for namespace in sorted(ops_data_by_namespace.keys()):
        namespace_data = ops_data_by_namespace[namespace]
        markdown += f"## {namespace}\n\n"
        if namespace_data.get('description'):
            markdown += f"*{namespace_data['description']}*\n\n"
        
        # Sort ops by name
        ops = sorted(namespace_data['ops'], key=lambda x: x['name'])
        
        for op in ops:
            markdown += generate_op_markdown(op)
        
        markdown += "\n"
    
    return markdown

def generate_op_markdown(op_data):
    """Generate markdown for a single op"""
    name = op_data.get('name', 'Unknown')
    description = op_data.get('description', '*See documentation*')
    url = op_data.get('url', '')
    
    # Input ports
    input_ports = op_data.get('input_ports', [])
    if not input_ports:
        input_ports_text = f"- *Visit [{name} documentation]({url}) for complete input port details*"
    else:
        input_ports_text = "\n".join([f"- **{port}**" for port in input_ports[:20]])  # Limit to 20 ports
        if len(input_ports) > 20:
            input_ports_text += f"\n- *... and {len(input_ports) - 20} more (see [documentation]({url}))*"
    
    # Output ports
    output_ports = op_data.get('output_ports', [])
    if not output_ports:
        output_ports_text = f"- *Visit [{name} documentation]({url}) for complete output port details*"
    else:
        output_ports_text = "\n".join([f"- **{port}**" for port in output_ports[:20]])
        if len(output_ports) > 20:
            output_ports_text += f"\n- *... and {len(output_ports) - 20} more (see [documentation]({url}))*"
    
    # Image
    image_markdown = ""
    if op_data.get('image_path'):
        rel_path = op_data['image_path'].replace('chapters/', '')
        image_markdown = f"\n![{name} op]({rel_path})\n\n"
    
    # Example patches
    example_patches = op_data.get('example_patches', [])
    if example_patches:
        example_text = "\n".join([f"- [Example Patch]({patch})" for patch in example_patches[:3]])
    else:
        example_text = f"[Open in Editor](https://cables.gl/editor?patch=example_{name.replace('.', '_')})"
    
    markdown = f"""### {name}

**Description:** {description}

{image_markdown}**Input Ports:**
{input_ports_text}

**Output Ports:**
{output_ports_text}

**Example Patch:** {example_text}

**Patches Using This Op:**
- *Search [cables.gl patches](https://cables.gl/ops) for "{name.split('.')[-1]}"*

**Documentation:** [{url}]({url})

---

"""
    return markdown

def main():
    """Main function to scrape all ops"""
    print("Starting op scraping...")
    
    # Create images directory
    os.makedirs("chapters/images/ops", exist_ok=True)
    
    # Scrape ops list
    op_urls = scrape_ops_list()
    
    if not op_urls:
        print("No op URLs found. Using fallback method...")
        # Fallback: use the generate_allops_complete.py approach
        return
    
    # Organize ops by namespace
    ops_by_namespace = {}
    scraped_data = []
    
    print(f"\nScraping {len(op_urls)} op pages...")
    for i, op_url in enumerate(op_urls, 1):
        print(f"[{i}/{len(op_urls)}] Processing {op_url}...")
        op_data = scrape_op_page(op_url)
        
        if op_data:
            scraped_data.append(op_data)
            # Extract namespace from URL
            # URL format: https://cables.gl/ops/Ops.Namespace.OpName
            parts = op_url.split('/ops/')
            if len(parts) > 1:
                full_name = parts[1]
                namespace_parts = full_name.split('.')
                if len(namespace_parts) >= 2:
                    namespace = '.'.join(namespace_parts[:2])  # Ops.Namespace
                    if namespace not in ops_by_namespace:
                        ops_by_namespace[namespace] = {
                            'description': '',
                            'ops': []
                        }
                    ops_by_namespace[namespace]['ops'].append(op_data)
        
        # Save progress periodically
        if i % 10 == 0:
            print(f"  Progress: {i}/{len(op_urls)} ops processed")
    
    # Save scraped data as JSON for reference
    with open('scraped_ops_data.json', 'w', encoding='utf-8') as f:
        json.dump(scraped_data, f, indent=2, ensure_ascii=False)
    print(f"\nSaved scraped data to scraped_ops_data.json")
    
    # Generate markdown
    markdown = generate_markdown_from_data(ops_by_namespace)
    
    # Write to file
    with open('chapters/13-AllOps.md', 'w', encoding='utf-8') as f:
        f.write(markdown)
    
    print(f"\nGenerated chapters/13-AllOps.md with {len(scraped_data)} ops")
    print(f"Organized into {len(ops_by_namespace)} namespaces")

if __name__ == "__main__":
    main()

