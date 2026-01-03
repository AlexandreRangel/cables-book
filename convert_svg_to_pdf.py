#!/usr/bin/env python3
"""
Convert all SVG files to PDF for LaTeX/XeLaTeX compatibility.

This script converts SVG files to PDF format which is required for 
PDF generation with XeLaTeX (XeLaTeX doesn't support SVG natively).

Usage:
    python convert_svg_to_pdf.py

Requirements:
    pip install svglib reportlab
"""

import os
import sys
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

try:
    from svglib.svglib import svg2rlg
    from reportlab.graphics import renderPDF
except ImportError:
    print("ERROR: Required packages not installed.")
    print("Please run: pip install svglib reportlab")
    sys.exit(1)


def convert_svg_to_pdf(svg_path: Path) -> tuple[bool, str]:
    """
    Convert a single SVG file to PDF.
    
    Returns:
        tuple: (success: bool, message: str)
    """
    pdf_path = svg_path.with_suffix('.pdf')
    
    # Skip if PDF exists and is newer than SVG
    if pdf_path.exists():
        svg_mtime = svg_path.stat().st_mtime
        pdf_mtime = pdf_path.stat().st_mtime
        if pdf_mtime >= svg_mtime:
            return True, f"Skipped (up-to-date): {svg_path.name}"
    
    try:
        drawing = svg2rlg(str(svg_path))
        if drawing is None:
            return False, f"Failed to parse: {svg_path.name}"
        
        renderPDF.drawToFile(drawing, str(pdf_path), fmt='PDF')
        return True, f"Converted: {svg_path.name}"
    except Exception as e:
        return False, f"Error converting {svg_path.name}: {str(e)}"


def main():
    # Directory containing SVG files
    ops_dir = Path(__file__).parent / "chapters" / "images" / "ops"
    
    if not ops_dir.exists():
        print(f"ERROR: Directory not found: {ops_dir}")
        sys.exit(1)
    
    # Find all SVG files
    svg_files = list(ops_dir.glob("*.svg"))
    
    if not svg_files:
        print("No SVG files found.")
        return
    
    print(f"Found {len(svg_files)} SVG files to process...")
    print()
    
    converted = 0
    skipped = 0
    failed = 0
    
    # Use thread pool for parallel conversion
    with ThreadPoolExecutor(max_workers=8) as executor:
        futures = {executor.submit(convert_svg_to_pdf, svg): svg for svg in svg_files}
        
        for future in as_completed(futures):
            success, message = future.result()
            if success:
                if "Skipped" in message:
                    skipped += 1
                else:
                    converted += 1
                    print(f"  {message}")
            else:
                failed += 1
                print(f"  ERROR: {message}")
    
    print()
    print("=" * 50)
    print(f"Conversion complete!")
    print(f"  Converted: {converted}")
    print(f"  Skipped (up-to-date): {skipped}")
    print(f"  Failed: {failed}")
    print(f"  Total: {len(svg_files)}")
    print("=" * 50)
    
    if failed > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()



