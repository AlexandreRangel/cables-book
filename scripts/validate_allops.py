#!/usr/bin/env python3
"""
Validate and Audit AllOps.md

This script analyzes the 13-AllOps.md file and the scraped JSON data to identify:
- Ops with missing descriptions
- Ops with missing/incomplete port information  
- Ops with placeholder text instead of real data
- Missing images
- Broken URLs

Usage:
    python validate_allops.py                # Full validation report
    python validate_allops.py --summary      # Summary only
    python validate_allops.py --export       # Export issues to CSV
    python validate_allops.py --check-urls   # Also verify URLs are valid

Output:
    Prints detailed validation report to console
    Optional: validation_issues.csv
"""

import json
import os
import re
import sys
import argparse
from collections import defaultdict
from datetime import datetime
from typing import Dict, List, Tuple

# Paths (relative to scripts folder)
DATA_FILE = "../thorough_ops_data.json"
LEGACY_DATA_FILE = "../detailed_ops_data.json"
MARKDOWN_FILE = "../chapters/13-AllOps.md"
IMAGES_DIR = "../chapters/images/ops"


def load_ops_data() -> Dict:
    """Load the ops data from JSON"""
    for data_file in [DATA_FILE, LEGACY_DATA_FILE]:
        if os.path.exists(data_file):
            with open(data_file, 'r', encoding='utf-8') as f:
                return json.load(f)
    return {}


def analyze_ops_data(ops_data: Dict) -> Dict:
    """Analyze ops data for completeness issues"""
    issues = {
        'no_description': [],
        'no_input_ports': [],
        'no_output_ports': [],
        'placeholder_description': [],
        'placeholder_ports': [],
        'missing_image': [],
        'scrape_failed': [],
    }
    
    stats = {
        'total_ops': 0,
        'total_namespaces': len(ops_data),
        'with_description': 0,
        'with_input_ports': 0,
        'with_output_ports': 0,
        'with_image': 0,
        'complete': 0,  # Has description AND at least one port type
    }
    
    for namespace, ops in ops_data.items():
        for op in ops:
            stats['total_ops'] += 1
            full_name = op.get('full_name', 'Unknown')
            short_name = op.get('short_name', full_name.split('.')[-1])
            
            # Check description
            desc = op.get('description', '')
            if not desc:
                issues['no_description'].append(full_name)
            elif 'Visit' in desc and 'documentation' in desc.lower():
                issues['placeholder_description'].append(full_name)
            else:
                stats['with_description'] += 1
            
            # Check input ports
            input_ports = op.get('input_ports', [])
            if not input_ports:
                issues['no_input_ports'].append(full_name)
            else:
                # Check for placeholder port descriptions
                for port in input_ports:
                    port_desc = port.get('description', '')
                    if 'documentation' in port_desc.lower() or port_desc == '*Check documentation*':
                        if full_name not in issues['placeholder_ports']:
                            issues['placeholder_ports'].append(full_name)
                        break
                stats['with_input_ports'] += 1
            
            # Check output ports
            output_ports = op.get('output_ports', [])
            if not output_ports:
                issues['no_output_ports'].append(full_name)
            else:
                stats['with_output_ports'] += 1
            
            # Check image
            safe_name = full_name.replace('.', '_')
            image_path = os.path.join(IMAGES_DIR, f"{safe_name}.svg")
            if os.path.exists(image_path):
                stats['with_image'] += 1
            else:
                issues['missing_image'].append(full_name)
            
            # Check scrape status
            if op.get('scrape_status') and op['scrape_status'] != 'success':
                issues['scrape_failed'].append(f"{full_name}: {op['scrape_status']}")
            
            # Check if complete (has description and at least some ports)
            has_desc = desc and 'Visit' not in desc
            has_ports = bool(input_ports) or bool(output_ports)
            if has_desc and has_ports:
                stats['complete'] += 1
    
    return {
        'issues': issues,
        'stats': stats
    }


def analyze_markdown_file() -> Dict:
    """Analyze the markdown file directly for issues"""
    if not os.path.exists(MARKDOWN_FILE):
        return {'error': 'Markdown file not found'}
    
    with open(MARKDOWN_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    issues = {
        'placeholder_in_markdown': [],
        'missing_image_refs': [],
    }
    
    # Find all op sections
    op_pattern = r'### (\w+)\n'
    op_names = re.findall(op_pattern, content)
    
    # Find placeholder text
    placeholder_patterns = [
        r'Visit \[[^\]]+\] \(documentation\) for (?:details|complete (?:input|output) port details)',
        r'\*Visit \[.+?\] for (?:details|complete (?:input|output) port details)\*',
    ]
    
    for pattern in placeholder_patterns:
        matches = re.findall(pattern, content)
        if matches:
            issues['placeholder_in_markdown'].extend(matches[:10])  # First 10
    
    # Count placeholders
    placeholder_count = len(re.findall(r'Visit \[.+?\] for', content))
    
    return {
        'total_ops_in_markdown': len(op_names),
        'placeholder_text_count': placeholder_count,
        'issues': issues
    }


def check_urls(ops_data: Dict, sample_size: int = 10) -> List[str]:
    """Check if op URLs are valid (sample only)"""
    import requests
    
    broken_urls = []
    all_ops = [op for ops in ops_data.values() for op in ops]
    
    # Sample random ops
    import random
    sample = random.sample(all_ops, min(sample_size, len(all_ops)))
    
    for op in sample:
        url = op.get('url', '')
        if url:
            try:
                response = requests.head(url, timeout=5, allow_redirects=True)
                if response.status_code >= 400:
                    broken_urls.append(f"{op['full_name']}: {url} (HTTP {response.status_code})")
            except Exception as e:
                broken_urls.append(f"{op['full_name']}: {url} (Error: {str(e)[:30]})")
    
    return broken_urls


def print_report(analysis: Dict, markdown_analysis: Dict, args):
    """Print the validation report"""
    issues = analysis['issues']
    stats = analysis['stats']
    
    print("=" * 70)
    print("CABLES.GL ALLOPS VALIDATION REPORT")
    print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)
    
    # Summary statistics
    print("\n[STATS] SUMMARY STATISTICS")
    print("-" * 40)
    print(f"Total namespaces:     {stats['total_namespaces']}")
    print(f"Total ops:            {stats['total_ops']}")
    print(f"With description:     {stats['with_description']} ({100*stats['with_description']/stats['total_ops']:.1f}%)")
    print(f"With input ports:     {stats['with_input_ports']} ({100*stats['with_input_ports']/stats['total_ops']:.1f}%)")
    print(f"With output ports:    {stats['with_output_ports']} ({100*stats['with_output_ports']/stats['total_ops']:.1f}%)")
    print(f"With image:           {stats['with_image']} ({100*stats['with_image']/stats['total_ops']:.1f}%)")
    print(f"Fully complete:       {stats['complete']} ({100*stats['complete']/stats['total_ops']:.1f}%)")
    
    if args.summary:
        return
    
    # Issue breakdown
    print("\n[!] ISSUES FOUND")
    print("-" * 40)
    
    def print_issue_section(title: str, items: List, show_limit: int = 10):
        count = len(items)
        if count == 0:
            print(f"[OK] {title}: None")
        else:
            print(f"[X] {title}: {count} ops")
            for item in items[:show_limit]:
                print(f"   - {item}")
            if count > show_limit:
                print(f"   ... and {count - show_limit} more")
    
    print_issue_section("Missing description", issues['no_description'])
    print_issue_section("Placeholder description", issues['placeholder_description'])
    print_issue_section("No input ports", issues['no_input_ports'])
    print_issue_section("No output ports", issues['no_output_ports'])
    print_issue_section("Placeholder port descriptions", issues['placeholder_ports'])
    print_issue_section("Missing image", issues['missing_image'])
    print_issue_section("Scrape failed", issues['scrape_failed'])
    
    # Markdown analysis
    if markdown_analysis and 'error' not in markdown_analysis:
        print("\n[MD] MARKDOWN FILE ANALYSIS")
        print("-" * 40)
        print(f"Ops in markdown:      {markdown_analysis['total_ops_in_markdown']}")
        print(f"Placeholder texts:    {markdown_analysis['placeholder_text_count']}")
    
    # Recommendations
    print("\n[*] RECOMMENDATIONS")
    print("-" * 40)
    
    incomplete_pct = 100 - (100 * stats['complete'] / stats['total_ops'])
    if incomplete_pct > 50:
        print("[HIGH] Over 50% of ops are incomplete. Re-run thorough_op_scraper.py")
    elif incomplete_pct > 20:
        print("[MEDIUM] About 20-50% of ops are incomplete. Consider targeted re-scraping.")
    else:
        print("[GOOD] Less than 20% of ops are incomplete.")
    
    if issues['missing_image']:
        print(f"[!] {len(issues['missing_image'])} ops are missing images. Run scraper with --images-only")
    
    if issues['scrape_failed']:
        print(f"[!] {len(issues['scrape_failed'])} ops had scraping errors. May need browser-based scraping.")


def export_to_csv(analysis: Dict, filename: str = "validation_issues.csv"):
    """Export issues to CSV for easy review"""
    import csv
    
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Issue Type', 'Op Full Name', 'Details'])
        
        for issue_type, items in analysis['issues'].items():
            for item in items:
                if ':' in item:
                    op_name, details = item.split(':', 1)
                else:
                    op_name, details = item, ''
                writer.writerow([issue_type, op_name, details.strip()])
    
    print(f"\nExported issues to {filename}")


def main():
    parser = argparse.ArgumentParser(description='Validate AllOps.md completeness')
    parser.add_argument('--summary', action='store_true', help='Show summary only')
    parser.add_argument('--export', action='store_true', help='Export issues to CSV')
    parser.add_argument('--check-urls', action='store_true', help='Check if URLs are valid')
    args = parser.parse_args()
    
    # Change to script directory for relative paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    # Load and analyze data
    ops_data = load_ops_data()
    
    if not ops_data:
        print("ERROR: No ops data found. Run thorough_op_scraper.py first.")
        print(f"Looking for: {DATA_FILE} or {LEGACY_DATA_FILE}")
        sys.exit(1)
    
    # Analyze
    analysis = analyze_ops_data(ops_data)
    markdown_analysis = analyze_markdown_file()
    
    # Print report
    print_report(analysis, markdown_analysis, args)
    
    # Check URLs if requested
    if args.check_urls:
        print("\n[URL] URL VALIDATION (sample of 10)")
        print("-" * 40)
        try:
            broken = check_urls(ops_data, sample_size=10)
            if broken:
                print(f"[X] {len(broken)} broken URLs found:")
                for url in broken:
                    print(f"   - {url}")
            else:
                print("[OK] All sampled URLs are valid")
        except ImportError:
            print("[!] requests module not available for URL checking")
    
    # Export if requested
    if args.export:
        export_to_csv(analysis)


if __name__ == "__main__":
    main()

