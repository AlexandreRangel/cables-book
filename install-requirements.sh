#!/bin/bash
# ============================================
# Cables.gl Book - Requirements Installer (macOS)
# Run this to install all Python dependencies
# Last updated: December 29, 2025
# ============================================

echo ""
echo "============================================"
echo "Cables.gl Book - Dependency Installer"
echo "============================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed or not in PATH."
    echo "Please install Python from: https://www.python.org/downloads/"
    echo "Or run: brew install python3"
    exit 1
fi
echo "[OK] Python found."

# Check if pip is available
if ! python3 -m pip --version &> /dev/null; then
    echo "ERROR: pip is not available."
    echo "Please ensure pip is installed with Python."
    exit 1
fi
echo "[OK] pip found."

# Setup virtual environment (to avoid externally-managed-environment error on macOS)
VENV_DIR="venv"
if [ ! -d "$VENV_DIR" ]; then
    echo ""
    echo "Creating virtual environment..."
    python3 -m venv "$VENV_DIR"
    if [ $? -ne 0 ]; then
        echo "ERROR: Failed to create virtual environment."
        exit 1
    fi
    echo "[OK] Virtual environment created."
fi

# Activate virtual environment
echo "Activating virtual environment..."
source "$VENV_DIR/bin/activate"

# Install Python packages
echo ""
echo "[1/3] Installing Python packages..."
echo ""
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

if [ $? -ne 0 ]; then
    echo ""
    echo "ERROR: Failed to install Python packages."
    deactivate 2>/dev/null
    exit 1
fi
echo ""
echo "[OK] Python packages installed."

# Install Playwright browser
echo ""
echo "[2/3] Installing Playwright Chromium browser..."
echo ""
python -m playwright install chromium

if [ $? -ne 0 ]; then
    echo ""
    echo "WARNING: Playwright browser installation may have failed."
    echo "You can try manually: playwright install chromium"
fi
echo ""
echo "[OK] Playwright browser installed."

# Check for system dependencies
echo ""
echo "[3/3] Checking system dependencies..."
echo ""

MISSING_DEPS=0

# Check Pandoc
if ! command -v pandoc &> /dev/null; then
    echo "[MISSING] Pandoc not found."
    echo "          Install from: https://pandoc.org/installing.html"
    echo "          Or run: brew install pandoc"
    MISSING_DEPS=1
else
    echo "[OK] Pandoc found."
fi

# Check XeLaTeX (part of MacTeX or BasicTeX)
# Check in PATH first, then check common macOS locations
XELATEX_FOUND=0
if command -v xelatex &> /dev/null; then
    XELATEX_FOUND=1
elif [ -f "/Library/TeX/texbin/xelatex" ]; then
    XELATEX_FOUND=1
    echo "[INFO] XeLaTeX found but not in PATH."
    echo "       Add to PATH: export PATH=\"/Library/TeX/texbin:\$PATH\""
    echo "       Or add to ~/.zshrc: echo 'export PATH=\"/Library/TeX/texbin:\$PATH\"' >> ~/.zshrc"
fi

if [ $XELATEX_FOUND -eq 0 ]; then
    echo "[MISSING] XeLaTeX not found."
    echo "          Option 1 - Install MacTeX (full, ~4GB):"
    echo "            Download from: https://www.tug.org/mactex/"
    echo ""
    echo "          Option 2 - Install BasicTeX (minimal, ~100MB):"
    echo "            brew install --cask basictex"
    echo "            Then add to PATH and install required packages:"
    echo "            export PATH=\"/Library/TeX/texbin:\$PATH\""
    echo "            sudo tlmgr update --self"
    echo "            sudo tlmgr install xetex adjustbox float caption tocloft fontspec titlesec fancyvrb mdframed pgf zref needspace"
    MISSING_DEPS=1
else
    echo "[OK] XeLaTeX found."
    
    # Check if required LaTeX packages are installed
    # Try to find tlmgr to check packages
    TLMGR_CMD=""
    if command -v tlmgr &> /dev/null; then
        TLMGR_CMD="tlmgr"
    elif [ -f "/Library/TeX/texbin/tlmgr" ]; then
        TLMGR_CMD="/Library/TeX/texbin/tlmgr"
    fi
    
    if [ -n "$TLMGR_CMD" ]; then
        echo ""
        echo "Checking required LaTeX packages..."
        REQUIRED_PACKAGES="adjustbox float caption tocloft fontspec titlesec fancyvrb mdframed pgf zref needspace"
        MISSING_PACKAGES=""
        
        for pkg in $REQUIRED_PACKAGES; do
            # Check if the package is installed (not just known to the repo)
            if ! $TLMGR_CMD info --only-installed "$pkg" 2>/dev/null | grep -qi '^installed:.*yes'; then
                MISSING_PACKAGES="$MISSING_PACKAGES $pkg"
            fi
        done
        
        if [ -n "$MISSING_PACKAGES" ]; then
            echo "[MISSING] Some LaTeX packages are missing:$MISSING_PACKAGES"
            echo "          Install with:"
            echo "            sudo $TLMGR_CMD install$MISSING_PACKAGES"
            MISSING_DEPS=1
        else
            echo "[OK] All required LaTeX packages found."
        fi
    fi
fi

echo ""
echo "============================================"

if [ $MISSING_DEPS -eq 1 ]; then
    echo ""
    echo "WARNING: Some system dependencies are missing."
    echo "Please install them manually:"
    echo ""
    echo "  1. Install Pandoc:"
    echo "     brew install pandoc"
    echo ""
    echo "  2. Install BasicTeX (or MacTeX for full installation):"
    echo "     brew install --cask basictex"
    echo ""
    echo "  3. Add TeX Live to your PATH (add to ~/.zshrc):"
    echo "     echo 'export PATH=\"/Library/TeX/texbin:\$PATH\"' >> ~/.zshrc"
    echo "     source ~/.zshrc"
    echo ""
    echo "  4. Update TeX Live and install required packages:"
    echo "     sudo tlmgr update --self"
    echo "     sudo tlmgr install xetex adjustbox float caption tocloft fontspec titlesec fancyvrb mdframed pgf zref needspace"
    echo ""
    echo "  Also make sure to install Ubuntu fonts:"
    echo "    https://fonts.google.com/specimen/Ubuntu"
    echo ""
else
    echo ""
    echo "SUCCESS! All dependencies are installed."
    echo ""
    echo "Don't forget to install Ubuntu fonts if not already:"
    echo "  https://fonts.google.com/specimen/Ubuntu"
    echo ""
    echo "You can now generate the book with:"
    echo "  ./makebook.sh"
    echo ""
fi

# Deactivate virtual environment
deactivate 2>/dev/null

echo "============================================"
