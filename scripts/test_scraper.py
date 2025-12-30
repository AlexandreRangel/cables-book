#!/usr/bin/env python3
"""Test scraper on SimpleAnim to verify it works"""

from scrape_ops_with_browser import scrape_op_with_playwright, generate_op_markdown_detailed
import os

os.makedirs("chapters/images/ops", exist_ok=True)

# Test with SimpleAnim
op_url = "https://cables.gl/ops/Ops.Anim.SimpleAnim"
op_name = "Ops.Anim.SimpleAnim"

print(f"Testing scraper on {op_name}...")
op_data = scrape_op_with_playwright(op_url, op_name)

if op_data:
    print("\nScraped data:")
    print(f"Description: {op_data.get('description', 'N/A')[:100]}")
    print(f"Input ports: {len(op_data.get('input_ports', []))}")
    print(f"Output ports: {len(op_data.get('output_ports', []))}")
    print(f"Image: {op_data.get('image_path', 'N/A')}")
    
    # Generate markdown
    markdown = generate_op_markdown_detailed(op_data)
    print("\nGenerated markdown preview:")
    print(markdown[:500])
else:
    print("Failed to scrape op data")

