#!/usr/bin/env python3
"""
Improved automated script to scrape all op information from cables.gl/ops/
Downloads op images and extracts port information from individual op pages
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
        response = requests.get(url, timeout=10, headers={'User-Agent': 'Mozilla/5.0'})
        if response.status_code == 200:
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            with open(save_path, 'wb') as f:
                f.write(response.content)
            return True
    except Exception as e:
        print(f"  Error downloading image {url}: {e}")
    return False

def get_all_individual_ops():
    """Get all individual op URLs by scraping namespace pages"""
    all_op_urls = []
    
    # First, get the main ops page
    try:
        print("Fetching main ops page...")
        response = requests.get(OPS_LIST_URL, timeout=10, headers={'User-Agent': 'Mozilla/5.0'})
        if response.status_code != 200:
            print(f"Failed to fetch ops list: {response.status_code}")
            return []
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all links to individual ops (format: /ops/Ops.Namespace.OpName)
        # Look for links that have 3+ parts when split by '.'
        for link in soup.find_all('a', href=True):
            href = link.get('href', '')
            if '/ops/Ops.' in href:
                # Check if it's an individual op (has 3+ parts) or namespace (2 parts)
                parts = href.split('/ops/')
                if len(parts) > 1:
                    op_path = parts[1]
                    dot_count = op_path.count('.')
                    # Individual ops have at least 2 dots (Ops.Namespace.OpName)
                    if dot_count >= 2 and op_path not in ['Ops.Anim', 'Ops.Array', 'Ops.Audio']:
                        full_url = urljoin(BASE_URL, href)
                        if full_url not in all_op_urls:
                            all_op_urls.append(full_url)
        
        # Also try to find ops by looking at the page content
        # Many ops are listed with their full names
        for elem in soup.find_all(['a', 'div', 'span'], string=re.compile(r'Ops\.\w+\.\w+')):
            text = elem.get_text()
            # Extract op names like "Ops.Anim.SimpleAnim"
            matches = re.findall(r'Ops\.\w+\.\w+(?:\.\w+)*', text)
            for match in matches:
                op_url = f"{BASE_URL}/ops/{match}"
                if op_url not in all_op_urls:
                    all_op_urls.append(op_url)
        
        print(f"Found {len(all_op_urls)} individual op URLs from main page")
        
        # Also scrape namespace pages to find more ops
        namespace_urls = []
        for link in soup.find_all('a', href=re.compile(r'/ops/Ops\.\w+$')):
            href = link.get('href')
            if href:
                namespace_urls.append(urljoin(BASE_URL, href))
        
        print(f"Found {len(namespace_urls)} namespace pages, scraping for individual ops...")
        
        for ns_url in namespace_urls[:5]:  # Limit to first 5 for testing
            try:
                print(f"  Scraping namespace: {ns_url}")
                ns_response = requests.get(ns_url, timeout=10, headers={'User-Agent': 'Mozilla/5.0'})
                if ns_response.status_code == 200:
                    ns_soup = BeautifulSoup(ns_response.content, 'html.parser')
                    # Find all op links in this namespace
                    for link in ns_soup.find_all('a', href=re.compile(r'/ops/Ops\.')):
                        href = link.get('href', '')
                        if '/ops/Ops.' in href:
                            op_path = href.split('/ops/')[1] if '/ops/' in href else href
                            if op_path.count('.') >= 2:  # Individual op
                                full_url = urljoin(BASE_URL, href)
                                if full_url not in all_op_urls:
                                    all_op_urls.append(full_url)
                time.sleep(0.5)
            except Exception as e:
                print(f"  Error scraping namespace {ns_url}: {e}")
        
        print(f"Total individual op URLs found: {len(all_op_urls)}")
        return all_op_urls
        
    except Exception as e:
        print(f"Error getting ops list: {e}")
        return []

def scrape_op_page(op_url):
    """Scrape information from a single op page"""
    try:
        response = requests.get(op_url, timeout=10, headers={'User-Agent': 'Mozilla/5.0'})
        if response.status_code != 200:
            return None
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract op name from URL
        op_path = op_url.split('/ops/')[-1] if '/ops/' in op_url else op_url
        op_name = op_path.replace('/', '.')
        
        op_data = {
            'url': op_url,
            'name': op_name,
            'description': '',
            'input_ports': [],
            'output_ports': [],
            'image_url': None,
            'image_path': None,
            'example_patches': []
        }
        
        # Extract description - look for common description patterns
        desc_selectors = [
            'p.description',
            '.description',
            'p:first-of-type',
            'div.description',
            '[class*="description"]'
        ]
        
        for selector in desc_selectors:
            desc_elem = soup.select_one(selector)
            if desc_elem:
                desc_text = desc_elem.get_text().strip()
                if desc_text and len(desc_text) > 10:
                    op_data['description'] = desc_text
                    break
        
        # If no description found, try to get from meta or first paragraph
        if not op_data['description']:
            meta_desc = soup.find('meta', attrs={'name': 'description'})
            if meta_desc and meta_desc.get('content'):
                op_data['description'] = meta_desc.get('content').strip()
            else:
                first_p = soup.find('p')
                if first_p:
                    op_data['description'] = first_p.get_text().strip()[:200]
        
        # Try to find input/output ports
        # Look for sections with port information
        page_text = soup.get_text().lower()
        
        # Look for "Input Ports" or "Output Ports" sections
        for heading in soup.find_all(['h2', 'h3', 'h4'], string=re.compile(r'(input|output).*port', re.I)):
            section = heading.find_next_sibling()
            if section:
                ports = section.find_all(['li', 'div', 'span', 'p'])
                for port in ports:
                    port_text = port.get_text().strip()
                    if port_text and len(port_text) > 3:
                        if 'input' in heading.get_text().lower():
                            op_data['input_ports'].append(port_text)
                        elif 'output' in heading.get_text().lower():
                            op_data['output_ports'].append(port_text)
        
        # Find op image - look for images in the page
        # Try multiple selectors
        img_selectors = [
            'img[src*="op"]',
            'img[class*="op"]',
            'img[class*="screenshot"]',
            'img[class*="preview"]',
            '.op-image img',
            '.screenshot img',
            'main img',
            'article img'
        ]
        
        for selector in img_selectors:
            img_elem = soup.select_one(selector)
            if img_elem and img_elem.get('src'):
                img_url = img_elem.get('src')
                if not img_url.startswith('http'):
                    img_url = urljoin(BASE_URL, img_url)
                # Skip very small images (likely icons)
                if 'icon' not in img_url.lower() and 'logo' not in img_url.lower():
                    op_data['image_url'] = img_url
                    break
        
        # Download the image if found
        if op_data['image_url']:
            op_name_safe = op_name.replace('.', '_').replace('/', '_').replace(':', '_')
            img_ext = os.path.splitext(urlparse(op_data['image_url']).path)[1] or '.png'
            img_path = f"chapters/images/ops/{op_name_safe}{img_ext}"
            if download_image(op_data['image_url'], img_path):
                op_data['image_path'] = img_path
                print(f"    Downloaded image: {img_path}")
        
        # Look for example patches
        for link in soup.find_all('a', href=re.compile(r'(editor|patch)', re.I)):
            patch_url = link.get('href')
            if patch_url:
                if not patch_url.startswith('http'):
                    patch_url = urljoin(BASE_URL, patch_url)
                if patch_url not in op_data['example_patches']:
                    op_data['example_patches'].append(patch_url)
        
        return op_data
        
    except Exception as e:
        print(f"  Error scraping {op_url}: {e}")
        return None

def generate_markdown_from_data(ops_data_by_namespace):
    """Generate markdown chapter from scraped data"""
    markdown = """# All Operators Reference

This chapter provides a comprehensive reference for all operators (ops) available in cables.gl. Each op is documented with its input/output ports, description, and links to examples and documentation.

**Note:** This reference is automatically generated from the [cables.gl ops documentation](https://cables.gl/ops/). For the most up-to-date information, visit the official documentation.

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

1. Run `python scrape_allops_improved.py` to automatically scrape the latest information
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
        ops = sorted(namespace_data['ops'], key=lambda x: x.get('name', ''))
        
        for op in ops:
            markdown += generate_op_markdown(op)
        
        markdown += "\n"
    
    return markdown

def generate_op_markdown(op_data):
    """Generate markdown for a single op"""
    name = op_data.get('name', 'Unknown')
    description = op_data.get('description', '*See documentation*')
    if not description or description == '*See documentation*':
        description = f"*See [documentation]({op_data.get('url', '')})*"
    url = op_data.get('url', '')
    
    # Input ports
    input_ports = op_data.get('input_ports', [])
    if not input_ports:
        input_ports_text = f"- *Visit [{name} documentation]({url}) for complete input port details*"
    else:
        input_ports_text = "\n".join([f"- **{port}**" for port in input_ports[:20]])
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
        op_short_name = name.split('.')[-1] if '.' in name else name
        example_text = f"[Open in Editor](https://cables.gl/editor?patch=example_{op_short_name})"
    
    markdown = f"""### {name.split('.')[-1] if '.' in name else name}

**Full Name:** `{name}`

**Description:** {description}

{image_markdown}**Input Ports:**
{input_ports_text}

**Output Ports:**
{output_ports_text}

**Example Patch:** {example_text}

**Patches Using This Op:**
- *Search [cables.gl patches](https://cables.gl/ops) for "{name.split('.')[-1] if '.' in name else name}"*

**Documentation:** [{url}]({url})

---

"""
    return markdown

def main():
    """Main function to scrape all ops"""
    print("Starting improved op scraping...")
    
    # Create images directory
    os.makedirs("chapters/images/ops", exist_ok=True)
    
    # Get all individual op URLs
    op_urls = get_all_individual_ops()
    
    if not op_urls:
        print("No individual op URLs found. The website structure may have changed.")
        return
    
    # Organize ops by namespace
    ops_by_namespace = {}
    scraped_data = []
    
    print(f"\nScraping {len(op_urls)} individual op pages...")
    for i, op_url in enumerate(op_urls, 1):
        print(f"[{i}/{len(op_urls)}] Processing {op_url}...")
        op_data = scrape_op_page(op_url)
        
        if op_data:
            scraped_data.append(op_data)
            # Extract namespace from op name
            # Format: Ops.Namespace.OpName or Ops.Namespace.SubNamespace.OpName
            name_parts = op_data['name'].split('.')
            if len(name_parts) >= 2:
                namespace = '.'.join(name_parts[:2])  # Ops.Namespace
                if namespace not in ops_by_namespace:
                    ops_by_namespace[namespace] = {
                        'description': '',
                        'ops': []
                    }
                ops_by_namespace[namespace]['ops'].append(op_data)
        
        # Be polite with rate limiting
        if i % 10 == 0:
            print(f"  Progress: {i}/{len(op_urls)} ops processed, pausing...")
            time.sleep(2)
        else:
            time.sleep(0.5)
    
    # Save scraped data as JSON for reference
    with open('scraped_ops_data_improved.json', 'w', encoding='utf-8') as f:
        json.dump(scraped_data, f, indent=2, ensure_ascii=False)
    print(f"\nSaved scraped data to scraped_ops_data_improved.json")
    
    # Generate markdown
    markdown = generate_markdown_from_data(ops_by_namespace)
    
    # Write to file
    with open('chapters/13-AllOps.md', 'w', encoding='utf-8') as f:
        f.write(markdown)
    
    print(f"\nGenerated chapters/13-AllOps.md with {len(scraped_data)} ops")
    print(f"Organized into {len(ops_by_namespace)} namespaces")
    print(f"Downloaded images to chapters/images/ops/")

if __name__ == "__main__":
    main()

