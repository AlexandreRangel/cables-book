#!/usr/bin/env python3
"""
Enhanced scraper for cables.gl ops
Uses correct API endpoints:
- Op images: https://cables.gl/api/op/layout/Ops.Namespace.OpName
- Op docs: https://cables.gl/op/Ops.Namespace.OpName
"""

import json
import os
import re
import time
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://cables.gl"

# Complete list of all ops from cables.gl/ops/
ALL_OPS_DATA = {
    "Ops.Anim": {
        "description": "Animations",
        "ops": [
            ("AnimNumber", "Always animates to the current value"),
            ("Bang", "Trigger a simple bang animation going from 1 to 0"),
            ("BoolAnim", "Animate between two numbers based on a boolean value"),
            ("Crossfade", "Crossfade between 2 values"),
            ("FrameRangeAnim", "Parses string containing ranges of frames and play as coherent animation"),
            ("FrameRangeAnimSwitcher", "Switch between multiple anim ranges of a keyframed 3d scene"),
            ("InOutInAnim", "Animates after a trigger from 1 to 0 to 1"),
            ("LFO", "Low-frequency oscillation for animations"),
            ("RandomAnim", "Animates between random values defined by a min and max value"),
            ("SimpleAnim", "Simple animation between two values"),
            ("SineAnim", "Animation in the form of a sine/cosine curve (sinus/cos)"),
            ("Smooth", "Smooths out jumps in values (AverageInterpolation)"),
            ("Snap", "Snap at certain points (e.g. while scrolling)"),
            ("Spring", "Spring simulation based on input target value."),
            ("StringTypeAnimation", "Animates a text/string, like it is being typed out by a person"),
            ("TimeDelta", "Measure the time difference between two triggers"),
            ("Timer", "A timer that can be started, paused and reset by triggering"),
        ]
    },
    "Ops.Array": {
        "description": "Process and manipulate collections (arrays) of data",
        "ops": [
            ("AnglesBetweenPoints", "Outputs the angle between points in 3D space (degree)"),
            ("AnimArray", "Animate values in an array to another array"),
            ("Array", "Can generate 3 kinds of arrays: Number - 1,2,3,4 - Normalized"),
            ("Array1toX", "Convert an array1 to array2,3,4 by choosing content for new axis"),
            ("Array2To3", "Inserts zeroes every third item"),
            ("Array3", "Create an array of num triplets set to default values xyz"),
            ("Array3GetAverage", "Average x,y,z values of an array3x"),
            ("Array3GetNumbers", "Get 3 values XYZ from an array"),
            ("Array3InterpolateDistributed", "Interpolate between two arrays"),
            ("Array3Iterator", "Iterate over an array in steps of three and outputs three values"),
            ("Array3Multiply", "Multiply every XYZ member of array3x"),
            ("Array3PushNumbers", "Push three numbers to the end of an array"),
            ("Array3RandomSelection", "Extract definable amount of random xyz points from an array"),
            ("Array3SetNumber", "Set three numbers at index in an array"),
            ("Array3Sum", "Add number to every XYZ member of array3x"),
            ("Array3To2", "Remove every 3rd item of an array"),
            ("Array3To4", "Convert an array3 to an array4 by filling it up with 1"),
            ("Array3VectorLength", "Return the length of a vector from an array 3"),
            ("Array4", "Create an array of num quadruples set to default values xyz"),
            ("Array4GetNumbers", "Get 4 values from an array"),
            ("Array4SetNumber", "Set four numbers at index in an array"),
            ("Array4toArray3", "Convert an array4 to array3 by dropping every 4th number"),
            ("ArrayAbs", "Converts array contents to absolute values"),
            ("ArrayAppendArray", "Append an array to an existing array"),
            ("ArrayBuffer", "Store values in an array / fifo array buffer"),
            ("ArrayBuffer3", "Circular buffer for xyz values"),
            ("ArrayCeil", "Round numbers up"),
            ("ArrayChunk", "Extracts x elements from an array"),
            ("ArrayChunkDuplicate", "Repeat chunks of an array multiple times"),
            ("ArrayClamp", "Clamp the values of an array to a min and max value"),
            ("ArrayContains", "Check if an array contains a number"),
            ("ArrayDivide", "Divide all values in an array by one number"),
            ("ArrayFindStrings", "Return all the indexes of a string in an array"),
            ("ArrayFloor", "Round numbers down"),
            ("ArrayFract", "Return the fractional remainder of all values in an array"),
            ("ArrayFromNumbers", "Simple way to create small arrays of numbers"),
            ("ArrayGetArray", "Get an array from an array of arrays"),
            ("ArrayGetNumber", "Return a value from an array"),
            ("ArrayGetObject", "Get an object from an array"),
            ("ArrayGetString", "Get a string from an array at [index]"),
            ("ArrayGetTexture", "Get texture from array at index"),
            ("ArrayGetValuesByIndexArray", "Pick values from input array at given indices and stride"),
            ("ArrayIndexBetween", "Output index where value is greater than number and smaller then next number"),
            ("ArrayIndexMinMax", "Find lowest/highest numbers in an array"),
            ("ArrayIteratorArray", "Iterate over an array of arrays"),
            ("ArrayIteratorNumbers", "Loop over every element of an array"),
            ("ArrayIteratorObjects", "Iterate over an array of objects"),
            ("ArrayIteratorStrings", "Loop over every element of an array"),
            ("ArrayIteratorTextures", "Iterate over an array of objects"),
            ("ArrayLength", "Number of items in an array"),
            ("ArrayLogic", "Performs logical comparison operations on a single array of numbers"),
            ("ArrayLogicArray", "Performs logical comparison operations on two arrays"),
            ("ArrayLogicBetween", "If value of array is between min and max then the value is 1 else 0"),
            ("ArrayLookup", "Create an array that is filled with values looked up by index from another array"),
            ("ArrayMath", "Pick from multiple mathematical modes which can all be applied to a single array"),
            ("ArrayMathArray", "Perform a math operations on two arrays"),
            ("ArrayMathExpression", "Calculate a user-defined mathematical expression"),
            ("ArrayMathExpressionTrigger", "Calculate a user-defined mathematical expression"),
            ("ArrayMax", "Apply a max operation to all values in an array"),
            ("ArrayMerge", "Merge multiple arrays - in consecutive order"),
            ("ArrayMergeTrigger", "Merge / concatenate arrays by trigger"),
            ("ArrayMin", "Apply a min operation to all values in an array"),
            ("ArrayModulo", "Apply a modulo operation to all values in an array"),
            ("ArrayMultiply", "Multiply every number in an array"),
            ("ArrayNumberRamp", "Create an array that contains X numbers between start and end values"),
            ("ArrayOfArrays", "Create an array filled with other arrays"),
            ("ArrayOfObjectsFilterByKeyValue", "Filter key-value pairs in objects in an array of objects"),
            ("ArrayOfObjectsFilterKeys", "Remove key-value pairs from objects in an array of objects"),
            ("ArrayOfObjectsToString", "Convert an array of objects into readable string format"),
            ("ArrayPack", "Pack multiple arrays into a new array"),
            ("ArrayPack2", "Pack two individual arrays into a new array"),
            ("ArrayPack2Simple", "Pack 2 individual arrays into an array2"),
            ("ArrayPack3", "Pack 3 individual arrays into a xyz array"),
            ("ArrayPack3Simple", "Pack 3 individual arrays into an array3"),
            ("ArrayPack4", "Pack 4 arrays into one array"),
            ("ArrayPack4Simple", "Pack 3 individual arrays into an array3"),
            ("ArrayPow", "Apply a Pow function to an array"),
            ("ArrayPushString", "Push/Append a string to the end of an array"),
            ("ArrayQuantizer", "Quantize input to nearest number in array"),
            ("ArrayRandomSelection", "Extract a definable amount of values from an array"),
            ("ArrayRemoveFalsy", "Remove falsy items from an array"),
            ("ArrayReverse", "Reverse an array"),
            ("ArrayRound", "Round numbers up"),
            ("ArraySetNumber", "Set a number at index in an array"),
            ("ArraySetString", "Set a string at index in an array"),
            ("ArraySin", "Perform a sin or cos operation on the contents of an array"),
            ("ArraySmoothStep", "Apply a smoothstep function to the contents of an array"),
            ("ArraySort", "Sort an array"),
            ("ArraySplit", "Split an array into multiple arrays"),
            ("ArraySubtract", "Subtract a number from all values in an array"),
            ("ArraySum", "Sum all values in an array"),
            ("ArrayToObject", "Convert an array to an object"),
            ("ArrayToString", "Convert an array to a string"),
            ("ArrayUnique", "Remove duplicate values from an array"),
            ("ArrayUnpack", "Unpack an array into multiple arrays"),
            ("ArrayUnpack2", "Unpack an array2 into two individual arrays"),
            ("ArrayUnpack3", "Unpack an array3 into three individual arrays"),
            ("ArrayUnpack4", "Unpack an array4 into four individual arrays"),
            ("ArrayZip", "Zip two arrays together"),
        ]
    },
}

def download_op_image(full_name, save_dir="chapters/images/ops"):
    """
    Download op SVG image from cables.gl API
    URL format: https://cables.gl/api/op/layout/Ops.Namespace.OpName
    """
    os.makedirs(save_dir, exist_ok=True)
    
    image_url = f"{BASE_URL}/api/op/layout/{full_name}"
    safe_name = full_name.replace(".", "_")
    save_path = os.path.join(save_dir, f"{safe_name}.svg")
    
    try:
        print(f"    Downloading image: {image_url}")
        response = requests.get(image_url, timeout=10, headers={'User-Agent': 'Mozilla/5.0'})
        if response.status_code == 200:
            with open(save_path, 'wb') as f:
                f.write(response.content)
            print(f"    Saved: {save_path}")
            return save_path.replace("chapters/", "")
        else:
            print(f"    Failed to download image: {response.status_code}")
    except Exception as e:
        print(f"    Error downloading image: {e}")
    
    return None

def scrape_op_page(full_name):
    """
    Scrape op documentation page
    URL format: https://cables.gl/op/Ops.Namespace.OpName (note: /op/ not /ops/)
    """
    op_url = f"{BASE_URL}/op/{full_name}"
    
    try:
        print(f"  Scraping: {op_url}")
        response = requests.get(op_url, timeout=15, headers={'User-Agent': 'Mozilla/5.0'})
        
        if response.status_code != 200:
            print(f"    Failed: {response.status_code}")
            return None
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract description from page content
        description = ""
        # Look for the description section
        desc_elem = soup.find('h3', string=re.compile(r'Simple|Description', re.I))
        if desc_elem:
            next_text = desc_elem.find_next_sibling()
            if next_text:
                description = next_text.get_text().strip()
        
        # Also try to find the one-liner description
        page_text = soup.get_text()
        
        # Parse INPUT PORTS
        input_ports = []
        output_ports = []
        
        # Method 1: Look for INPUT PORTS and OUTPUT PORTS sections
        input_section = re.search(r'INPUT PORTS(.*?)(?:OUTPUT PORTS|$)', page_text, re.DOTALL | re.IGNORECASE)
        output_section = re.search(r'OUTPUT PORTS(.*?)(?:Changelog|Patches using|SaveCancel|$)', page_text, re.DOTALL | re.IGNORECASE)
        
        if input_section:
            input_text = input_section.group(1)
            # Parse ports: portName (Type) Description
            port_matches = re.findall(r'(\w+(?:\s+\w+)*)\s*\(([^)]+)\)\s*([^\n]*)', input_text)
            for name, port_type, desc in port_matches:
                name = name.strip()
                port_type = port_type.strip()
                desc = desc.strip()
                if name and port_type and len(name) < 50:
                    input_ports.append({
                        "name": name,
                        "type": port_type,
                        "description": desc
                    })
        
        if output_section:
            output_text = output_section.group(1)
            port_matches = re.findall(r'(\w+(?:\s+\w+)*)\s*\(([^)]+)\)\s*([^\n]*)', output_text)
            for name, port_type, desc in port_matches:
                name = name.strip()
                port_type = port_type.strip()
                desc = desc.strip()
                if name and port_type and len(name) < 50:
                    output_ports.append({
                        "name": name,
                        "type": port_type,
                        "description": desc
                    })
        
        # Method 2: Parse HTML structure more carefully
        # Look for elements with port-like content
        for elem in soup.find_all(['div', 'p', 'li']):
            text = elem.get_text().strip()
            # Match pattern: name (Type) description
            match = re.match(r'^(\w+(?:\s+\w+)?)\s*\(([^)]+)\)\s*(.*)$', text)
            if match:
                name, port_type, desc = match.groups()
                name = name.strip()
                port_type = port_type.strip()
                desc = desc.strip()
                
                if name and port_type and len(name) < 30:
                    # Determine if input or output based on context
                    parent_text = ""
                    parent = elem.parent
                    for _ in range(5):
                        if parent:
                            parent_text += parent.get_text().lower()
                            parent = parent.parent
                    
                    port_data = {"name": name, "type": port_type, "description": desc}
                    
                    if 'input' in parent_text[:200].lower():
                        if port_data not in input_ports:
                            input_ports.append(port_data)
                    elif 'output' in parent_text[:200].lower():
                        if port_data not in output_ports:
                            output_ports.append(port_data)
        
        return {
            "url": op_url,
            "description": description,
            "input_ports": input_ports,
            "output_ports": output_ports
        }
        
    except Exception as e:
        print(f"    Error: {e}")
        return None

def format_port(port):
    """Format a port in SimpleAnim style"""
    name = port.get("name", "")
    port_type = port.get("type", "")
    description = port.get("description", "")
    
    if description:
        return f"- **{name} ({port_type})**: {description}"
    else:
        return f"- **{name} ({port_type})**: *Check documentation*"

def generate_op_markdown(namespace, op_name, op_data, image_path=None):
    """Generate markdown for a single op in SimpleAnim format"""
    full_name = f"{namespace}.{op_name}"
    op_url = f"https://cables.gl/op/{full_name}"  # Correct URL: /op/ not /ops/
    
    description = op_data.get("description", "See documentation")
    if not description or description == "See documentation":
        # Use the description from our data
        for ns, ns_data in ALL_OPS_DATA.items():
            if ns == namespace:
                for op, desc in ns_data.get("ops", []):
                    if op == op_name:
                        description = desc
                        break
    
    # Image markdown
    image_markdown = ""
    if image_path:
        image_markdown = f"\n![{op_name} op]({image_path})\n\n"
    
    # Input ports
    input_ports = op_data.get("input_ports", [])
    if input_ports:
        input_ports_text = "\n".join([format_port(p) for p in input_ports])
    else:
        input_ports_text = f"- *Visit [{full_name} documentation]({op_url}) for complete input port details*"
    
    # Output ports
    output_ports = op_data.get("output_ports", [])
    if output_ports:
        output_ports_text = "\n".join([format_port(p) for p in output_ports])
    else:
        output_ports_text = f"- *Visit [{full_name} documentation]({op_url}) for complete output port details*"
    
    markdown = f"""### {op_name}

**Full Name:** `{full_name}`

**Description:** {description}

{image_markdown}**Input Ports:**
{input_ports_text}

**Output Ports:**
{output_ports_text}

**Example Patch:** [Open in Editor](https://cables.gl/op/{full_name}#example)

**Patches Using This Op:**
- *Search [cables.gl patches](https://cables.gl/patches) for "{op_name}"*

**Documentation:** [{op_url}]({op_url})

---

"""
    return markdown

def generate_allops_chapter():
    """Generate complete AllOps chapter by scraping all ops"""
    
    header = """# All Operators Reference

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

---

"""
    
    content = header
    all_scraped_data = []
    
    # Process each namespace
    for namespace in sorted(ALL_OPS_DATA.keys()):
        namespace_data = ALL_OPS_DATA[namespace]
        
        content += f"## {namespace}\n\n"
        content += f"*{namespace_data['description']}*\n\n"
        
        # Process each op in this namespace
        for op_name, default_description in namespace_data.get("ops", []):
            full_name = f"{namespace}.{op_name}"
            print(f"\n[{namespace}] Processing {op_name}...")
            
            # Download op image (SVG)
            image_path = download_op_image(full_name)
            
            # Scrape op page for port information
            op_data = scrape_op_page(full_name)
            
            if not op_data:
                op_data = {
                    "url": f"https://cables.gl/op/{full_name}",
                    "description": default_description,
                    "input_ports": [],
                    "output_ports": []
                }
            elif not op_data.get("description"):
                op_data["description"] = default_description
            
            # Store for JSON export
            all_scraped_data.append({
                "full_name": full_name,
                "namespace": namespace,
                "op_name": op_name,
                "image_path": image_path,
                **op_data
            })
            
            # Generate markdown
            content += generate_op_markdown(namespace, op_name, op_data, image_path)
            
            # Rate limiting
            time.sleep(0.5)
        
        content += "\n"
    
    # Add footer
    footer = """
## Quick Reference: All Op Namespaces

- **Ops.Anim** - Animations
- **Ops.Array** - Process and manipulate collections (arrays) of data
- **Ops.Audio** - Audio operations
- **Ops.Boolean** - Boolean logic operations
- **Ops.Cables** - Cables-specific operations
- **Ops.Color** - Color manipulation
- **Ops.Data** - Data operations
- **Ops.Date** - Date and time operations
- **Ops.Debug** - Debugging tools
- **Ops.Devices** - Device input/output
- **Ops.Extension** - Extension operations
- **Ops.Gl** - WebGL operations
- **Ops.Graphics** - Graphics operations
- **Ops.Html** - HTML operations
- **Ops.Json** - JSON operations
- **Ops.Math** - Mathematical operations
- **Ops.Net** - Network operations
- **Ops.Number** - Number operations
- **Ops.Sidebar** - Sidebar interface operations
- **Ops.String** - String operations
- **Ops.Templates** - Template operations
- **Ops.TimeLine** - Timeline operations
- **Ops.Trigger** - Trigger operations
- **Ops.Ui** - User interface operations
- **Ops.Vars** - Variable operations
- **Ops.WebAudio** - Web Audio API operations
- **Ops.Website** - Website operations

For the complete, up-to-date list of all ops, visit: [https://cables.gl/ops/](https://cables.gl/ops/)

---

"""
    
    content += footer
    
    # Save scraped data as JSON
    with open('scraped_ops_data.json', 'w', encoding='utf-8') as f:
        json.dump(all_scraped_data, f, indent=2, ensure_ascii=False)
    print(f"\nSaved scraped data to scraped_ops_data.json")
    
    # Write chapter
    with open('chapters/13-AllOps.md', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"\nGenerated chapters/13-AllOps.md")
    print(f"Total ops processed: {len(all_scraped_data)}")
    
    # Count ops with port info
    ops_with_ports = sum(1 for op in all_scraped_data if op.get('input_ports') or op.get('output_ports'))
    ops_with_images = sum(1 for op in all_scraped_data if op.get('image_path'))
    print(f"Ops with port info: {ops_with_ports}")
    print(f"Ops with images: {ops_with_images}")

if __name__ == "__main__":
    os.makedirs("chapters/images/ops", exist_ok=True)
    generate_allops_chapter()

