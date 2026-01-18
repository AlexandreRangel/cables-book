#!/bin/bash
# ============================================
# Cables.gl Book PDF Generator (macOS)
# ============================================

echo ""
echo "============================================"
echo "Cables.gl Book - PDF Generator"
echo "============================================"
echo ""

# Check if Pandoc is installed
if ! command -v pandoc &> /dev/null; then
    echo "ERROR: Pandoc is not installed or not in PATH."
    echo "Please install from: https://pandoc.org/installing.html"
    echo "Or run: brew install pandoc"
    exit 1
fi

echo "[1/5] Pandoc found."

# Use virtual environment Python if it exists, otherwise use system python3
VENV_DIR="venv"
VENV_ACTIVATED=0
if [ -d "$VENV_DIR" ] && [ -f "$VENV_DIR/bin/activate" ]; then
    source "$VENV_DIR/bin/activate"
    PYTHON_CMD="python"
    VENV_ACTIVATED=1
else
    PYTHON_CMD="python3"
fi

# Convert SVG files to PDF (XeLaTeX doesn't support SVG natively)
echo "[2/5] Converting SVG images to PDF format..."
$PYTHON_CMD scripts/convert_svg_to_pdf.py
if [ $? -ne 0 ]; then
    echo "ERROR: SVG to PDF conversion failed."
    echo "Make sure svglib and reportlab are installed."
    echo "Run ./install.sh or ./install-requirements.sh to install dependencies."
    if [ $VENV_ACTIVATED -eq 1 ]; then deactivate 2>/dev/null; fi
    exit 1
fi

# Set file paths
TEMP_MD="temp_combined_book.md"
OUTPUT_PDF="cables-gl-book.pdf"
HEADER_FILE="latex-header.tex"

# Check header file exists
if [ ! -f "$HEADER_FILE" ]; then
    echo "ERROR: Header file $HEADER_FILE not found."
    exit 1
fi

# Delete old PDF to verify new one is created
if [ -f "$OUTPUT_PDF" ]; then
    rm "$OUTPUT_PDF"
fi

echo "[3/5] Combining chapters with proper UTF-8 encoding..."

# Use the existing Python combiner so macOS output mirrors the Windows PowerShell logic
$PYTHON_CMD scripts/combine_chapters.py
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to combine chapters."
    if [ $VENV_ACTIVATED -eq 1 ]; then deactivate 2>/dev/null; fi
    exit 1
fi

if [ ! -f "$TEMP_MD" ]; then
    echo "ERROR: Failed to combine chapters."
    if [ $VENV_ACTIVATED -eq 1 ]; then deactivate 2>/dev/null; fi
    exit 1
fi

# Deactivate venv if it was activated
if [ $VENV_ACTIVATED -eq 1 ]; then deactivate 2>/dev/null; fi

echo "[4/5] Generating PDF..."

# Generate PDF with Pandoc
pandoc "$TEMP_MD" -o "$OUTPUT_PDF" \
    --pdf-engine=xelatex \
    --pdf-engine-opt=-interaction=nonstopmode \
    --resource-path=chapters \
    -H "$HEADER_FILE" \
    -V geometry:"left=0.82in,right=0.82in,top=0.82in,bottom=0.82in" \
    -V mainfont="Ubuntu" \
    -V sansfont="Ubuntu" \
    -V monofont="Ubuntu Mono" \
    -V fontsize=11pt \
    -V linestretch=1.3 \
    --toc \
    --toc-depth=3 \
    --number-sections \
    -V papersize=letter \
    --syntax-highlighting=none 2>&1 | grep -v "major issue: So far, you have not checked for" | grep -v "miktex-dvipdfmx: major issue"

echo "[5/5] Cleaning up..."
if [ -f "$TEMP_MD" ]; then
    rm "$TEMP_MD"
fi
if [ -f "temp_debug.tex" ]; then
    rm "temp_debug.tex"
fi

# Check if PDF was created
if [ -f "$OUTPUT_PDF" ]; then
    echo ""
    echo "============================================"
    echo "SUCCESS! PDF created: $OUTPUT_PDF"
    echo "============================================"
    echo ""
    exit 0
else
    echo ""
    echo "ERROR: PDF generation failed."
    echo ""
    echo "Make sure you have:"
    echo "  - XeLaTeX installed (MacTeX or BasicTeX)"
    echo "    If BasicTeX is installed but xelatex not found, add to PATH:"
    echo "    export PATH=\"/Library/TeX/texbin:\$PATH\""
    echo "  - Ubuntu fonts installed"
    echo ""
    echo "Run ./install.sh for installation instructions."
    echo ""
    exit 1
fi
