#!/usr/bin/env python3
"""Test description extraction from a cables.gl op page"""

import sys
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except:
        pass

from playwright.sync_api import sync_playwright
import re
import time

TEST_OPS = [
    "https://cables.gl/op/Ops.Math.Abs",
    "https://cables.gl/op/Ops.Anim.SimpleAnim", 
    "https://cables.gl/op/Ops.Gl.MainLoop",
    "https://cables.gl/op/Ops.String.Concat",
]


def extract_description_new(page):
    """NEW extraction method - from textarea/input elements"""
    description = ''
    
    try:
        # Get all textareas and text inputs
        inputs = page.query_selector_all('textarea, input[type="text"]')
        
        for inp in inputs:
            try:
                # Get value from the element
                value = inp.get_attribute('value') or ''
                if not value:
                    value = inp.inner_text() or ''
                value = value.strip()
                
                # Check if this looks like a description
                if value and len(value) > 15 and len(value) < 500:
                    # Skip if it looks like code or metadata
                    if not any(x in value.lower() for x in ['function', 'const ', 'var ', 'let ', '<script', '<div', 'http://', 'https://']):
                        # Skip if it's clearly junk
                        if not any(x in value for x in ['INPUT PORTS', 'OUTPUT PORTS', 'SaveCancel']):
                            # Clean up HTML entities
                            value = value.replace('&gt;', '>').replace('&lt;', '<').replace('&amp;', '&')
                            # Normalize whitespace
                            value = re.sub(r'\s+', ' ', value).strip()
                            description = value
                            break
            except:
                continue
    except:
        pass
    
    return description


def test_extraction():
    print("=" * 60)
    print("Testing Description Extraction")
    print("=" * 60)
    print()
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        for url in TEST_OPS:
            op_name = url.split('/')[-1]
            print(f"Testing: {op_name}")
            print(f"  URL: {url}")
            
            page.goto(url, wait_until='domcontentloaded', timeout=30000)
            time.sleep(5)  # Wait for JS to render
            
            # Test NEW extraction method
            desc = extract_description_new(page)
            
            if desc:
                print(f"  [SUCCESS] Description: {desc}")
            else:
                print(f"  [FAILED] No description extracted")
            
            print()
            print("-" * 60)
            print()
        
        browser.close()

if __name__ == "__main__":
    test_extraction()

