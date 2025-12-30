#!/usr/bin/env python3
"""
Upgrade all ops to SimpleAnim-level detail
Creates comprehensive AllOps chapter with all ops in detailed format
"""

import os
import json

# SimpleAnim template - this is the format we want for ALL ops
SIMPLEANIM_TEMPLATE = """### {op_short_name}

**Full Name:** `{full_name}`

**Description:** {description}

{image_markdown}**Input Ports:**
{input_ports}

**Output Ports:**
{output_ports}

**Example Patch:** {example_patch}

**Patches Using This Op:**
- *Search [cables.gl patches](https://cables.gl/ops) for "{op_short_name}"*

**Documentation:** [{op_url}]({op_url})

---

"""

def format_port_detailed(port_name, port_type, description=""):
    """Format a port in the detailed style like SimpleAnim"""
    if description:
        return f"- **{port_name} ({port_type})**: {description}"
    else:
        return f"- **{port_name} ({port_type})**: *Check [documentation]({{op_url}})*"

def generate_op_entry_detailed(namespace, op_name, description, input_ports_data=None, output_ports_data=None, image_path=None):
    """Generate detailed op entry matching SimpleAnim format"""
    full_name = f"{namespace}.{op_name}"
    op_url = f"https://cables.gl/ops/{full_name}"
    op_short_name = op_name
    
    # Image markdown
    image_markdown = ""
    if image_path and os.path.exists(f"chapters/{image_path}"):
        image_markdown = f"\n![{op_short_name} op]({image_path})\n\n"
    
    # Input ports
    if input_ports_data:
        input_ports = "\n".join([
            format_port_detailed(port.get('name', ''), port.get('type', ''), port.get('description', ''))
            for port in input_ports_data
        ])
    else:
        input_ports = f"- *Visit [{full_name} documentation]({op_url}) for complete input port details*"
    
    # Output ports
    if output_ports_data:
        output_ports = "\n".join([
            format_port_detailed(port.get('name', ''), port.get('type', ''), port.get('description', ''))
            for port in output_ports_data
        ])
    else:
        output_ports = f"- *Visit [{full_name} documentation]({op_url}) for complete output port details*"
    
    # Example patch
    example_patch = f"[Open in Editor](https://cables.gl/editor?patch=example_{op_short_name})"
    
    entry = SIMPLEANIM_TEMPLATE.format(
        op_short_name=op_short_name,
        full_name=full_name,
        description=description,
        image_markdown=image_markdown,
        input_ports=input_ports,
        output_ports=output_ports,
        example_patch=example_patch,
        op_url=op_url
    )
    
    return entry

# SimpleAnim ports (from your screenshot) - use as reference
SIMPLEANIM_INPUT_PORTS = [
    {"name": "Exe", "type": "Trigger", "description": "Trigger the op"},
    {"name": "Reset", "type": "Trigger", "description": "Trigger the animation"},
    {"name": "Rewind", "type": "Trigger", "description": "Rewinds animation to start but only after it's finished"},
    {"name": "Start", "type": "Number", "description": "Starting animation value"},
    {"name": "End", "type": "Number", "description": "Ending animation value"},
    {"name": "Duration", "type": "Number", "description": "Duration to get from start to end value"},
    {"name": "Loop", "type": "Number: Boolean", "description": "Enable to loop animation back and forth"},
    {"name": "Wait For Reset", "type": "Number: Boolean", "description": ""},
    {"name": "Easing Index", "type": "Number: Integer", "description": ""},
]

SIMPLEANIM_OUTPUT_PORTS = [
    {"name": "Next", "type": "Trigger", "description": "Trigger out"},
    {"name": "Result", "type": "Number", "description": "The animated value out"},
    {"name": "Finished", "type": "Number", "description": "Outputs true when animation is finished"},
    {"name": "Finished Trigger", "type": "Trigger", "description": "Outputs a trigger when animation is finished"},
]

# All ops data - this will be populated from scraping or manual entry
# For now, we'll use the structure and SimpleAnim as the example
OPS_DATA = {
    "Ops.Anim": {
        "description": "Animations",
        "ops": [
            ("SimpleAnim", "Simple animation between two values", 
             SIMPLEANIM_INPUT_PORTS, SIMPLEANIM_OUTPUT_PORTS, "images/ops/Ops_Anim_SimpleAnim.png"),
            # Add other Anim ops here - they'll need port data from scraping
        ]
    },
}

def generate_complete_chapter():
    """Generate complete AllOps chapter with detailed format"""
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

## Updating This Reference

To update this reference when cables.gl adds new ops or changes existing ones:

1. Run `python scrape_ops_with_browser.py` to automatically scrape port information
2. Or manually visit each op page at [https://cables.gl/ops/](https://cables.gl/ops/) and update port details
3. Download op images and save to `chapters/images/ops/`

---

"""
    
    content = header
    
    # Generate sections for each namespace
    for namespace in sorted(OPS_DATA.keys()):
        namespace_data = OPS_DATA[namespace]
        content += f"## {namespace}\n\n"
        content += f"*{namespace_data['description']}*\n\n"
        
        for op_info in namespace_data['ops']:
            if len(op_info) >= 2:
                op_name = op_info[0]
                description = op_info[1]
                input_ports = op_info[2] if len(op_info) > 2 else None
                output_ports = op_info[3] if len(op_info) > 3 else None
                image_path = op_info[4] if len(op_info) > 4 else None
                
                content += generate_op_entry_detailed(
                    namespace, op_name, description, 
                    input_ports, output_ports, image_path
                )
        
        content += "\n"
    
    return content

if __name__ == "__main__":
    os.makedirs("chapters/images/ops", exist_ok=True)
    
    output = generate_complete_chapter()
    with open("chapters/13-AllOps.md", "w", encoding="utf-8") as f:
        f.write(output)
    print("Generated chapters/13-AllOps.md with detailed format")
    print("Note: Currently includes SimpleAnim with full details")
    print("Run scrape_ops_with_browser.py to populate all other ops")

