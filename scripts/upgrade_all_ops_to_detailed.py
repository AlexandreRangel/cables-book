#!/usr/bin/env python3
"""
Upgrade ALL ops to SimpleAnim-level detail format
Reads existing 13-AllOps.md and upgrades all ops to have detailed port information format
"""

import re
import os

def read_current_file():
    """Read the current AllOps file"""
    with open('chapters/13-AllOps.md', 'r', encoding='utf-8') as f:
        return f.read()

def upgrade_op_section(content, op_name, namespace):
    """Upgrade a single op section to detailed format"""
    # Find the op section
    pattern = rf'(### {re.escape(op_name)}.*?)(?=### |## |$)'
    match = re.search(pattern, content, re.DOTALL)
    
    if not match:
        return content
    
    op_section = match.group(1)
    full_name = f"{namespace}.{op_name}"
    op_url = f"https://cables.gl/ops/{full_name}"
    
    # Check if it already has detailed ports (like SimpleAnim)
    if '- **' in op_section and '(' in op_section and ')' in op_section:
        # Already has detailed format, keep it
        return content
    
    # Upgrade to detailed format
    # Extract description if present
    desc_match = re.search(r'\*\*Description:\*\* (.+?)(?:\n\n|\n\*\*)', op_section)
    description = desc_match.group(1) if desc_match else f"*See [documentation]({op_url})*"
    
    # Create new detailed section
    new_section = f"""### {op_name}

**Full Name:** `{full_name}`

**Description:** {description}

**Input Ports:**
- *Visit [{full_name} documentation]({op_url}) for complete input port details*
- *Port information will be populated from scraping or manual entry*

**Output Ports:**
- *Visit [{full_name} documentation]({op_url}) for complete output port details*
- *Port information will be populated from scraping or manual entry*

**Example Patch:** [Open in Editor](https://cables.gl/editor?patch=example_{op_name})

**Patches Using This Op:**
- *Search [cables.gl patches](https://cables.gl/ops) for "{op_name}"*

**Documentation:** [{op_url}]({op_url})

---

"""
    
    # Replace the section
    content = content[:match.start()] + new_section + content[match.end():]
    return content

def main():
    """Main function to upgrade all ops"""
    print("Reading current AllOps file...")
    content = read_current_file()
    
    # Find all op sections and upgrade them
    # SimpleAnim is already perfect, so we'll skip it
    op_pattern = r'### (\w+)\n\n\*\*Full Name:\*\* `(Ops\.\w+\.\w+)`'
    matches = list(re.finditer(op_pattern, content))
    
    print(f"Found {len(matches)} op sections")
    
    upgraded = 0
    for match in reversed(matches):  # Process in reverse to maintain positions
        op_name = match.group(1)
        full_name = match.group(2)
        namespace = '.'.join(full_name.split('.')[:2])
        
        if op_name == "SimpleAnim":
            print(f"  Skipping {op_name} (already has complete details)")
            continue
        
        print(f"  Upgrading {op_name}...")
        content = upgrade_op_section(content, op_name, namespace)
        upgraded += 1
    
    # Write back
    with open('chapters/13-AllOps.md', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"\nUpgraded {upgraded} ops to detailed format")
    print("Note: Port details still need to be populated via scraping or manual entry")
    print("Run 'python scrape_ops_with_browser.py' to attempt automatic population")

if __name__ == "__main__":
    main()

