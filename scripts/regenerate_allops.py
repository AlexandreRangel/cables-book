#!/usr/bin/env python3
"""
Regenerate AllOps.md from scraped JSON data

This script regenerates the 13-AllOps.md file from the scraped JSON data.
Use this when you want to:
- Update the markdown format without re-scraping
- Fix formatting issues
- Regenerate after manual JSON edits

Usage:
    python regenerate_allops.py                    # Use default data file
    python regenerate_allops.py --input data.json  # Use specific JSON file
    python regenerate_allops.py --dry-run          # Preview without writing

Output:
    chapters/13-AllOps.md
"""

import json
import os
import argparse
from datetime import datetime
from typing import Dict, List


# Paths (relative to scripts folder)
DATA_FILE = "../thorough_ops_data.json"
LEGACY_DATA_FILES = [
    "../detailed_ops_data.json",
    "../complete_ops_data.json",
    "../all_ops_complete.json",
]
MARKDOWN_FILE = "../chapters/13-AllOps.md"


# Namespace descriptions for better documentation
NAMESPACE_DESCRIPTIONS = {
    "Ops.Anim": "Animation and Motion - Timing, easing, and animation utilities for smooth transitions and movement",
    "Ops.Array": "Array Operations - Tools for creating, manipulating, and iterating over arrays of data",
    "Ops.Audio": "Audio Processing - Audio analysis, visualization, and effects processing",
    "Ops.Boolean": "Boolean Logic - Logical operations, comparisons, and boolean value manipulation",
    "Ops.Cables": "Cables Platform - Platform-specific functionality and utilities",
    "Ops.Color": "Color Manipulation - Color conversion, mixing, and color space transformations",
    "Ops.Data": "Data Handling - Data storage, retrieval, and persistence",
    "Ops.Date": "Date and Time - Date/time utilities and formatting",
    "Ops.Debug": "Debugging Tools - Development helpers, logging, and debugging utilities",
    "Ops.Devices": "Input Devices - Mouse, keyboard, touch, gamepad, and other input device handling",
    "Ops.Extension": "Extensions - Third-party extensions and additional functionality",
    "Ops.Gl": "WebGL Rendering - 3D graphics, shaders, meshes, materials, and rendering pipeline",
    "Ops.Graphics": "Graphics Utilities - 2D graphics, image processing, and visual effects",
    "Ops.Html": "HTML DOM - HTML element creation, manipulation, and DOM interactions",
    "Ops.Json": "JSON and HTTP - API calls, JSON parsing, and HTTP request handling",
    "Ops.Math": "Mathematical Operations - Math functions, vectors, matrices, and numerical utilities",
    "Ops.Net": "Networking - WebSockets, WebRTC, and real-time networking",
    "Ops.Number": "Number Operations - Number manipulation, conversion, and formatting",
    "Ops.Sidebar": "Sidebar UI - Parameter sidebar controls for interactive patches",
    "Ops.String": "String Operations - Text manipulation, parsing, and formatting",
    "Ops.Templates": "Templates - Op templates and starting points",
    "Ops.TimeLine": "Timeline and Sequencing - Timeline control, keyframes, and sequencing",
    "Ops.Trigger": "Trigger Flow Control - Execution flow, triggers, and event handling",
    "Ops.Ui": "User Interface - UI components and interactive elements",
    "Ops.Vars": "Global Variables - Global variable storage and sharing between ops",
    "Ops.WebAudio": "Web Audio API - Sound synthesis, audio nodes, and audio graph management",
    "Ops.Website": "Website Integration - Website utilities and integrations",
    "Ops.User": "User Ops - Community-created operators",
    "Ops.Team": "Team Ops - Team-specific operators",
}


def load_ops_data(input_file: str = None) -> Dict:
    """Load ops data from JSON file"""
    files_to_try = [input_file] if input_file else [DATA_FILE] + LEGACY_DATA_FILES
    
    for data_file in files_to_try:
        if data_file and os.path.exists(data_file):
            print(f"Loading data from: {data_file}")
            with open(data_file, 'r', encoding='utf-8') as f:
                return json.load(f)
    
    return {}


def format_port_markdown(port: Dict) -> str:
    """Format a port for markdown output"""
    name = port.get('name', 'Unknown')
    port_type = port.get('type', 'Unknown')
    desc = port.get('description', '*See documentation*')
    
    # Clean up description
    if not desc or desc in ['*Check documentation*', '*See documentation*', '']:
        desc = '*See documentation*'
    
    return f"- **{name}** ({port_type}): {desc}"


def generate_op_markdown(op: Dict) -> str:
    """Generate markdown for a single op"""
    full_name = op.get('full_name', 'Unknown')
    short_name = op.get('short_name', full_name.split('.')[-1])
    url = op.get('url', f"https://cables.gl/op/{full_name}")
    description = op.get('description', '')
    
    # Handle empty or placeholder descriptions
    if not description or description.strip() == '':
        description = f"*Visit [documentation]({url}) for details*"
    
    # Image path
    safe_name = full_name.replace('.', '_')
    image_path = f"images/ops/{safe_name}.svg"
    
    # Build markdown
    md = f"""### {short_name}
![{short_name} op]({image_path})

**Full Name:** `{full_name}`

**Description:** {description}

**> Input Ports:**
"""
    
    # Input ports
    input_ports = op.get('input_ports', [])
    if input_ports:
        for port in input_ports:
            md += format_port_markdown(port) + "\n"
    else:
        md += f"- *Visit [{full_name} documentation]({url}) for complete input port details*\n"
    
    md += "\n**< Output Ports:**\n"
    
    # Output ports
    output_ports = op.get('output_ports', [])
    if output_ports:
        for port in output_ports:
            md += format_port_markdown(port) + "\n"
    else:
        md += f"- *Visit [{full_name} documentation]({url}) for complete output port details*\n"
    
    md += f"""
**Example Patch:** [Open in Editor]({url}#example)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "{short_name}"*

**Docs:** [{url}]({url})

---

"""
    return md


def generate_allops_markdown(ops_data: Dict) -> str:
    """Generate the complete AllOps.md file content"""
    
    # Calculate statistics
    total_ops = sum(len(ops) for ops in ops_data.values())
    total_with_desc = sum(
        1 for ops in ops_data.values() 
        for op in ops 
        if op.get('description') and 'Visit' not in op.get('description', '')
    )
    total_with_ports = sum(
        1 for ops in ops_data.values() 
        for op in ops 
        if op.get('input_ports') or op.get('output_ports')
    )
    
    # Header
    md = f"""# All Operators Reference

This chapter provides a comprehensive reference for all operators (ops) available in cables.gl. Each op is documented with its input/output ports, description, and links to examples and documentation.

**Statistics:**
- Total operators: {total_ops}
- With descriptions: {total_with_desc} ({100*total_with_desc/total_ops:.1f}%)
- With port information: {total_with_ports} ({100*total_with_ports/total_ops:.1f}%)

**Note:** This reference is automatically generated from the [cables.gl ops documentation](https://cables.gl/ops/). For the most up-to-date information, visit the official documentation.

**Last Updated:** {datetime.now().strftime("%Y-%m-%d %H:%M")}

## How to Use This Reference

- **Op Name**: The full namespace and name of the operator
- **Description**: What the op does
- **> Input Ports**: Input ports with their types and descriptions
- **< Output Ports**: Output ports with their types and descriptions
- **Example Patch**: Link to open an example in the cables.gl editor
- **Patches Using This Op**: Community patches that demonstrate usage
- **Docs**: Link to the official op documentation page

---

"""
    
    # Generate namespace sections
    for namespace in sorted(ops_data.keys()):
        ops = ops_data[namespace]
        if not ops:
            continue
        
        # Get namespace description
        base_ns = '.'.join(namespace.split('.')[:2])
        ns_desc = NAMESPACE_DESCRIPTIONS.get(base_ns, "")
        if not ns_desc:
            # Try exact match for sub-namespaces
            ns_desc = NAMESPACE_DESCRIPTIONS.get(namespace, "")
        
        md += f"## {namespace}\n\n"
        if ns_desc:
            md += f"*{ns_desc}*\n\n"
        
        # Sort ops alphabetically by short name
        sorted_ops = sorted(ops, key=lambda x: x.get('short_name', '').lower())
        
        for op in sorted_ops:
            md += generate_op_markdown(op)
    
    return md


def main():
    parser = argparse.ArgumentParser(description='Regenerate AllOps.md from JSON data')
    parser.add_argument('--input', type=str, help='Input JSON file path')
    parser.add_argument('--output', type=str, help='Output markdown file path')
    parser.add_argument('--dry-run', action='store_true', help='Preview without writing')
    parser.add_argument('--stats-only', action='store_true', help='Show statistics only')
    args = parser.parse_args()
    
    # Change to script directory for relative paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    output_file = args.output or MARKDOWN_FILE
    
    print("=" * 60)
    print("AllOps.md Regeneration")
    print("=" * 60)
    
    # Load data
    ops_data = load_ops_data(args.input)
    
    if not ops_data:
        print("ERROR: No ops data found!")
        print("Run thorough_op_scraper.py first to generate the data.")
        return
    
    # Statistics
    total_ops = sum(len(ops) for ops in ops_data.values())
    total_namespaces = len(ops_data)
    
    print(f"\nLoaded data:")
    print(f"  Namespaces: {total_namespaces}")
    print(f"  Total ops: {total_ops}")
    
    if args.stats_only:
        # Show per-namespace stats
        print("\nPer-namespace breakdown:")
        for ns in sorted(ops_data.keys()):
            ops = ops_data[ns]
            with_desc = sum(1 for op in ops if op.get('description'))
            with_ports = sum(1 for op in ops if op.get('input_ports') or op.get('output_ports'))
            print(f"  {ns}: {len(ops)} ops ({with_desc} with desc, {with_ports} with ports)")
        return
    
    # Generate markdown
    print("\nGenerating markdown...")
    md_content = generate_allops_markdown(ops_data)
    
    # Output
    if args.dry_run:
        print("\nDRY RUN - Preview of first 2000 characters:")
        print("-" * 40)
        print(md_content[:2000])
        print("-" * 40)
        print(f"\nTotal content length: {len(md_content)} characters")
    else:
        # Ensure output directory exists
        output_dir = os.path.dirname(output_file)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(md_content)
        
        print(f"\n✅ Generated: {output_file}")
        print(f"   Size: {len(md_content):,} characters")
        print(f"   Lines: {md_content.count(chr(10)):,}")


if __name__ == "__main__":
    main()

