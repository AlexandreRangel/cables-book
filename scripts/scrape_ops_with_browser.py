#!/usr/bin/env python3
"""
Comprehensive scraper for cables.gl ops using headless browser
Extracts port information and downloads images for all ops
"""

import json
import os
import re
import time
from urllib.parse import urljoin, urlparse
import requests
from bs4 import BeautifulSoup

try:
    from playwright.sync_api import sync_playwright
    PLAYWRIGHT_AVAILABLE = True
except ImportError:
    PLAYWRIGHT_AVAILABLE = False
    print("Playwright not available, will try requests-based approach")

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

def extract_ports_from_html(html_content, op_name):
    """Extract input and output ports from HTML content"""
    soup = BeautifulSoup(html_content, 'html.parser')
    
    input_ports = []
    output_ports = []
    
    # Look for port sections - cables.gl typically has structured port information
    # Try multiple selectors to find port information
    
    # Method 1: Look for sections with "Input" or "Output" in headings
    for heading in soup.find_all(['h2', 'h3', 'h4', 'h5', 'div'], string=re.compile(r'(input|output).*port', re.I)):
        section = heading.find_next_sibling()
        if not section:
            section = heading.parent
        
        # Look for port items
        port_items = section.find_all(['li', 'div', 'span', 'p'], class_=re.compile(r'port', re.I))
        for item in port_items:
            port_text = item.get_text().strip()
            if port_text and len(port_text) > 3:
                # Extract port name and type
                # Format is usually: "PortName (Type): Description"
                if 'input' in heading.get_text().lower():
                    input_ports.append(port_text)
                elif 'output' in heading.get_text().lower():
                    output_ports.append(port_text)
    
    # Method 2: Look for structured data in script tags (JSON-LD or similar)
    for script in soup.find_all('script', type='application/json'):
        try:
            data = json.loads(script.string)
            # Try to extract port information from structured data
            if isinstance(data, dict):
                if 'inputPorts' in data:
                    input_ports.extend([str(p) for p in data['inputPorts']])
                if 'outputPorts' in data:
                    output_ports.extend([str(p) for p in data['outputPorts']])
        except:
            pass
    
    # Method 3: Look for port information in text content
    page_text = soup.get_text()
    
    # Try to find port patterns like "PortName (Type): Description"
    port_pattern = r'(\w+)\s*\(([^)]+)\)\s*:?\s*([^\n]*)'
    matches = re.findall(port_pattern, page_text)
    
    # This is a fallback - we'll need to be more sophisticated
    # For now, return what we found
    
    return input_ports, output_ports

def scrape_op_with_playwright(op_url, op_name):
    """Scrape op page using Playwright (handles JavaScript)"""
    if not PLAYWRIGHT_AVAILABLE:
        return None
    
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            
            print(f"  Loading {op_url}...")
            page.goto(op_url, wait_until='networkidle', timeout=60000)
            
            # Handle cookie consent if present
            try:
                cookie_button = page.locator('button:has-text("Accept"), button:has-text("OK"), [data-testid*="cookie"]').first
                if cookie_button.is_visible(timeout=2000):
                    cookie_button.click()
                    time.sleep(1)
            except:
                pass
            
            # Wait for actual content to load (not just cookie banner)
            # Look for op-specific content
            try:
                page.wait_for_selector('h1, h2, [class*="op"], main', timeout=10000)
            except:
                pass
            
            # Additional wait for JavaScript to render
            time.sleep(5)
            
            # Try to extract data from JavaScript context
            # cables.gl might store op data in window or global variables
            try:
                # Try to get op data from page context
                op_data_js = page.evaluate("""
                    () => {
                        // Try to find op data in various places
                        if (window.opData) return window.opData;
                        if (window.__OP_DATA__) return window.__OP_DATA__;
                        if (window.cables && window.cables.opData) return window.cables.opData;
                        return null;
                    }
                """)
                if op_data_js:
                    print(f"    Found op data in JavaScript context")
            except:
                pass
            
            # Try to extract op data from page's JavaScript/JSON
            try:
                # Look for JSON data in script tags
                script_data = page.evaluate("""
                    () => {
                        const scripts = Array.from(document.querySelectorAll('script[type="application/json"], script:not([src])'));
                        for (let script of scripts) {
                            try {
                                const data = JSON.parse(script.textContent);
                                if (data && (data.ports || data.inputPorts || data.outputPorts || data.op)) {
                                    return data;
                                }
                            } catch(e) {}
                        }
                        return null;
                    }
                """)
                if script_data:
                    print(f"    Found structured data in script tags")
                    if script_data.get('ports'):
                        op_data['input_ports'] = script_data['ports'].get('input', [])
                        op_data['output_ports'] = script_data['ports'].get('output', [])
                    elif script_data.get('inputPorts'):
                        op_data['input_ports'] = script_data['inputPorts']
                    elif script_data.get('outputPorts'):
                        op_data['output_ports'] = script_data['outputPorts']
            except Exception as e:
                print(f"    Could not extract from script tags: {e}")
            
            # Get the rendered HTML
            html_content = page.content()
            
            # Try to find port information using more specific selectors
            # Look for port lists or tables
            try:
                # Try to find port elements by looking for common patterns
                port_elements = page.locator('[class*="port"], [data-port], li:has-text("(")').all()
                for elem in port_elements[:50]:  # Limit to avoid too many
                    try:
                        text = elem.inner_text()
                        if text and '(' in text and ')' in text and len(text) > 5:
                            # Check if it's input or output
                            parent_text = elem.locator('xpath=ancestor::*[contains(@class, "input") or contains(@class, "output")]').first
                            if parent_text.count() > 0:
                                parent_class = parent_text.get_attribute('class') or ''
                                if 'input' in parent_class.lower():
                                    if text not in op_data['input_ports']:
                                        op_data['input_ports'].append(text)
                                elif 'output' in parent_class.lower():
                                    if text not in op_data['output_ports']:
                                        op_data['output_ports'].append(text)
                    except:
                        pass
            except:
                pass
            
            # Extract information
            soup = BeautifulSoup(html_content, 'html.parser')
            
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
            
            # Extract description
            desc_selectors = [
                'p.description',
                '.description',
                'p:first-of-type',
                '[data-testid="description"]',
                'main p',
            ]
            
            for selector in desc_selectors:
                desc_elem = soup.select_one(selector)
                if desc_elem:
                    desc_text = desc_elem.get_text().strip()
                    if desc_text and len(desc_text) > 10 and 'javascript' not in desc_text.lower():
                        op_data['description'] = desc_text
                        break
            
            # Try to extract ports using Playwright's better DOM access
            # Look for port sections in the rendered page
            try:
                # Try to find input/output port sections
                input_section = page.locator('[class*="input"], [class*="Input"], section:has-text("Input")').first
                if input_section.is_visible(timeout=2000):
                    input_text = input_section.inner_text()
                    # Parse port information from text
                    lines = input_text.split('\n')
                    for line in lines:
                        line = line.strip()
                        if line and '(' in line and ')' in line and len(line) > 5:
                            if line not in op_data['input_ports']:
                                op_data['input_ports'].append(line)
            except:
                pass
            
            try:
                output_section = page.locator('[class*="output"], [class*="Output"], section:has-text("Output")').first
                if output_section.is_visible(timeout=2000):
                    output_text = output_section.inner_text()
                    lines = output_text.split('\n')
                    for line in lines:
                        line = line.strip()
                        if line and '(' in line and ')' in line and len(line) > 5:
                            if line not in op_data['output_ports']:
                                op_data['output_ports'].append(line)
            except:
                pass
            
            # Fallback: Extract ports from HTML
            input_ports, output_ports = extract_ports_from_html(html_content, op_name)
            op_data['input_ports'].extend([p for p in input_ports if p not in op_data['input_ports']])
            op_data['output_ports'].extend([p for p in output_ports if p not in op_data['output_ports']])
            
            # Try to find port information in the DOM (HTML fallback)
            port_sections = soup.find_all(['section', 'div'], class_=re.compile(r'port', re.I))
            for section in port_sections:
                section_text = section.get_text().lower()
                port_items = section.find_all(['li', 'div', 'span'])
                for item in port_items:
                    item_text = item.get_text().strip()
                    if item_text and len(item_text) > 5:
                        # Check if it looks like a port definition
                        if '(' in item_text and ')' in item_text:
                            if 'input' in section_text or 'in' in section_text:
                                if item_text not in op_data['input_ports']:
                                    op_data['input_ports'].append(item_text)
                            elif 'output' in section_text or 'out' in section_text:
                                if item_text not in op_data['output_ports']:
                                    op_data['output_ports'].append(item_text)
            
            # Find op image
            img_selectors = [
                'img[src*="op"]',
                'img[class*="op"]',
                'img[class*="screenshot"]',
                'img[alt*="op"]',
                'main img:first-of-type',
                'article img:first-of-type',
            ]
            
            for selector in img_selectors:
                img_elem = soup.select_one(selector)
                if img_elem and img_elem.get('src'):
                    img_url = img_elem.get('src')
                    if not img_url.startswith('http'):
                        img_url = urljoin(BASE_URL, img_url)
                    # Skip icons and logos
                    if 'icon' not in img_url.lower() and 'logo' not in img_url.lower():
                        op_data['image_url'] = img_url
                        break
            
            # Download image
            if op_data['image_url']:
                op_name_safe = op_name.replace('.', '_').replace('/', '_').replace(':', '_')
                img_ext = os.path.splitext(urlparse(op_data['image_url']).path)[1] or '.png'
                img_path = f"chapters/images/ops/{op_name_safe}{img_ext}"
                if download_image(op_data['image_url'], img_path):
                    op_data['image_path'] = img_path
                    print(f"    Downloaded image: {img_path}")
            
            # Find example patches
            for link in soup.find_all('a', href=re.compile(r'(editor|patch)', re.I)):
                patch_url = link.get('href')
                if patch_url:
                    if not patch_url.startswith('http'):
                        patch_url = urljoin(BASE_URL, patch_url)
                    if patch_url not in op_data['example_patches']:
                        op_data['example_patches'].append(patch_url)
            
            browser.close()
            return op_data
            
    except Exception as e:
        error_msg = str(e).encode('ascii', 'ignore').decode('ascii')
        print(f"  Error scraping with Playwright: {error_msg}")
        return None

def get_all_op_urls_from_list():
    """Get all individual op URLs from the ops list page"""
    # This will use the comprehensive list from the web search results
    # For now, we'll generate URLs based on known namespace patterns
    
    op_urls = []
    
    # Known namespaces and their ops (from web search results)
    # We'll need to expand this with the full list
    
    base_ops = {
        "Ops.Anim": ["AnimNumber", "Bang", "BoolAnim", "Crossfade", "FrameRangeAnim", 
                     "FrameRangeAnimSwitcher", "InOutInAnim", "LFO", "RandomAnim", 
                     "SimpleAnim", "SineAnim", "Smooth", "Snap", "Spring", 
                     "StringTypeAnimation", "TimeDelta", "Timer"],
        "Ops.Array": ["AnglesBetweenPoints", "AnimArray", "Array", "Array1toX", "Array2To3",
                     "Array3", "Array3GetAverage", "Array3GetNumbers", "Array3InterpolateDistributed",
                     "Array3Iterator", "Array3Multiply", "Array3PushNumbers", "Array3RandomSelection",
                     "Array3SetNumber", "Array3Sum", "Array3To2", "Array3To4", "Array3VectorLength",
                     "Array4", "Array4GetNumbers", "Array4SetNumber", "Array4toArray3", "ArrayAbs",
                     "ArrayAppendArray", "ArrayBuffer", "ArrayBuffer3", "ArrayCeil", "ArrayChunk",
                     "ArrayChunkDuplicate", "ArrayClamp", "ArrayContains", "ArrayDivide", "ArrayFindStrings",
                     "ArrayFloor", "ArrayFract", "ArrayFromNumbers", "ArrayGetArray", "ArrayGetNumber",
                     "ArrayGetObject", "ArrayGetString", "ArrayGetTexture", "ArrayGetValuesByIndexArray",
                     "ArrayIndexBetween", "ArrayIndexMinMax", "ArrayIteratorArray", "ArrayIteratorNumbers",
                     "ArrayIteratorObjects", "ArrayIteratorStrings", "ArrayIteratorTextures", "ArrayLength",
                     "ArrayLogic", "ArrayLogicArray", "ArrayLogicBetween", "ArrayLookup", "ArrayMath",
                     "ArrayMathArray", "ArrayMathExpression", "ArrayMathExpressionTrigger", "ArrayMax",
                     "ArrayMerge", "ArrayMergeTrigger", "ArrayMin", "ArrayModulo", "ArrayMultiply",
                     "ArrayNumberRamp", "ArrayOfArrays", "ArrayOfObjectsFilterByKeyValue",
                     "ArrayOfObjectsFilterKeys", "ArrayOfObjectsToString", "ArrayPack", "ArrayPack2",
                     "ArrayPack2Simple", "ArrayPack3", "ArrayPack3Simple", "ArrayPack4", "ArrayPack4Simple",
                     "ArrayPow", "ArrayPushString", "ArrayQuantizer", "ArrayRandomSelection", "ArrayRemoveFalsy",
                     "ArrayReverse", "ArrayRound", "ArraySetNumber", "ArraySetString", "ArraySin",
                     "ArraySmoothStep", "ArraySort", "ArraySplit", "ArraySubtract", "ArraySum",
                     "ArrayToObject", "ArrayToString", "ArrayUnique", "ArrayUnpack", "ArrayUnpack2",
                     "ArrayUnpack3", "ArrayUnpack4", "ArrayZip"],
    }
    
    for namespace, ops in base_ops.items():
        for op in ops:
            full_name = f"{namespace}.{op}"
            op_url = f"{BASE_URL}/ops/{full_name}"
            op_urls.append((full_name, op_url))
    
    return op_urls

def format_port(port_text):
    """Format a port text into structured format"""
    # Try to parse "PortName (Type): Description" format
    match = re.match(r'^(\w+)\s*\(([^)]+)\)\s*:?\s*(.*)$', port_text)
    if match:
        name, port_type, desc = match.groups()
        return f"- **{name} ({port_type})**: {desc.strip() if desc.strip() else '*See documentation*'}"
    else:
        # If it doesn't match the pattern, just format it nicely
        return f"- **{port_text}**"

def generate_op_markdown_detailed(op_data):
    """Generate detailed markdown for a single op (like SimpleAnim example)"""
    name = op_data.get('name', 'Unknown')
    op_short_name = name.split('.')[-1] if '.' in name else name
    description = op_data.get('description', '*See documentation*')
    if not description or description == '*See documentation*' or 'javascript' in description.lower():
        description = f"*See [documentation]({op_data.get('url', '')})*"
    url = op_data.get('url', '')
    
    # Format input ports
    input_ports = op_data.get('input_ports', [])
    if not input_ports:
        input_ports_text = f"- *Visit [{name} documentation]({url}) for complete input port details*"
    else:
        input_ports_text = "\n".join([format_port(port) for port in input_ports[:30]])
        if len(input_ports) > 30:
            input_ports_text += f"\n- *... and {len(input_ports) - 30} more (see [documentation]({url}))*"
    
    # Format output ports
    output_ports = op_data.get('output_ports', [])
    if not output_ports:
        output_ports_text = f"- *Visit [{name} documentation]({url}) for complete output port details*"
    else:
        output_ports_text = "\n".join([format_port(port) for port in output_ports[:30]])
        if len(output_ports) > 30:
            output_ports_text += f"\n- *... and {len(output_ports) - 30} more (see [documentation]({url}))*"
    
    # Image
    image_markdown = ""
    if op_data.get('image_path'):
        rel_path = op_data['image_path'].replace('chapters/', '')
        image_markdown = f"\n![{op_short_name} op]({rel_path})\n\n"
    
    # Example patches
    example_patches = op_data.get('example_patches', [])
    if example_patches:
        example_text = "\n".join([f"- [Example Patch]({patch})" for patch in example_patches[:3]])
    else:
        example_text = f"[Open in Editor](https://cables.gl/editor?patch=example_{op_short_name})"
    
    markdown = f"""### {op_short_name}

**Full Name:** `{name}`

**Description:** {description}

{image_markdown}**Input Ports:**
{input_ports_text}

**Output Ports:**
{output_ports_text}

**Example Patch:** {example_text}

**Patches Using This Op:**
- *Search [cables.gl patches](https://cables.gl/ops) for "{op_short_name}"*

**Documentation:** [{url}]({url})

---

"""
    return markdown

def main():
    """Main function to scrape all ops with detailed information"""
    print("Starting comprehensive op scraping with browser...")
    
    # Create images directory
    os.makedirs("chapters/images/ops", exist_ok=True)
    
    if not PLAYWRIGHT_AVAILABLE:
        print("Installing Playwright browsers...")
        os.system("playwright install chromium")
    
    # Get all op URLs
    op_urls = get_all_op_urls_from_list()
    print(f"Found {len(op_urls)} ops to scrape")
    
    # Organize by namespace
    ops_by_namespace = {}
    scraped_data = []
    
    print(f"\nScraping {len(op_urls)} op pages with detailed information...")
    for i, (op_name, op_url) in enumerate(op_urls, 1):
        print(f"[{i}/{len(op_urls)}] Processing {op_name}...")
        
        if PLAYWRIGHT_AVAILABLE:
            op_data = scrape_op_with_playwright(op_url, op_name)
        else:
            print("  Playwright not available, skipping...")
            continue
        
        if op_data:
            scraped_data.append(op_data)
            # Extract namespace
            name_parts = op_name.split('.')
            if len(name_parts) >= 2:
                namespace = '.'.join(name_parts[:2])
                if namespace not in ops_by_namespace:
                    ops_by_namespace[namespace] = {'ops': []}
                ops_by_namespace[namespace]['ops'].append(op_data)
        
        # Rate limiting
        if i % 5 == 0:
            print(f"  Progress: {i}/{len(op_urls)} ops processed, pausing...")
            time.sleep(3)
        else:
            time.sleep(1)
    
    # Save scraped data
    with open('scraped_ops_detailed.json', 'w', encoding='utf-8') as f:
        json.dump(scraped_data, f, indent=2, ensure_ascii=False)
    print(f"\nSaved scraped data to scraped_ops_detailed.json")
    
    # Generate markdown
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

---

"""
    
    # Generate sections
    for namespace in sorted(ops_by_namespace.keys()):
        namespace_data = ops_by_namespace[namespace]
        markdown += f"## {namespace}\n\n"
        
        ops = sorted(namespace_data['ops'], key=lambda x: x.get('name', ''))
        for op in ops:
            markdown += generate_op_markdown_detailed(op)
        
        markdown += "\n"
    
    # Write to file
    with open('chapters/13-AllOps.md', 'w', encoding='utf-8') as f:
        f.write(markdown)
    
    print(f"\nGenerated chapters/13-AllOps.md with {len(scraped_data)} ops")
    print(f"Organized into {len(ops_by_namespace)} namespaces")
    print(f"Downloaded images to chapters/images/ops/")

if __name__ == "__main__":
    main()

