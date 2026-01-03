#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Read first and last N pages of a PDF to help debug issues
"""

import sys
from pathlib import Path

try:
    import PyPDF2
except ImportError:
    print("Installing PyPDF2...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "PyPDF2"])
    import PyPDF2

SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
PDF_FILE = PROJECT_ROOT / "cables-gl-book.pdf"


def read_pdf_pages(pdf_path, first_n=10, last_n=10):
    """Read first N and last N pages of PDF"""
    if not pdf_path.exists():
        print(f"PDF file not found: {pdf_path}")
        return
    
    print(f"Reading PDF: {pdf_path}")
    print("=" * 80)
    
    with open(pdf_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        total_pages = len(reader.pages)
        print(f"Total pages: {total_pages}")
        print("=" * 80)
        
        # First N pages
        print(f"\nFIRST {first_n} PAGES:")
        print("=" * 80)
        for i in range(min(first_n, total_pages)):
            page = reader.pages[i]
            text = page.extract_text()
            print(f"\n--- PAGE {i+1} ---")
            print(text[:1000])  # First 1000 chars
            if len(text) > 1000:
                print("... (truncated)")
        
        # Last N pages
        if total_pages > first_n:
            print(f"\n\nLAST {last_n} PAGES:")
            print("=" * 80)
            start = max(first_n, total_pages - last_n)
            for i in range(start, total_pages):
                page = reader.pages[i]
                text = page.extract_text()
                print(f"\n--- PAGE {i+1} ---")
                print(text[:1000])  # First 1000 chars
                if len(text) > 1000:
                    print("... (truncated)")


if __name__ == "__main__":
    read_pdf_pages(PDF_FILE)

