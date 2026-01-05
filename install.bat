@echo off
REM ============================================
REM Cables.gl Book - Dependency Installer
REM ============================================

echo.
echo ============================================
echo Cables.gl Book - Dependency Installer
echo ============================================
echo.

REM Check if Python is installed
where python >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Python is not installed or not in PATH.
    echo Please install Python from: https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation.
    pause
    exit /b 1
)
echo [OK] Python found.

REM Check if pip is available
python -m pip --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: pip is not available.
    echo Please ensure pip is installed with Python.
    pause
    exit /b 1
)
echo [OK] pip found.

REM Install Python packages
echo.
echo [1/3] Installing Python packages...
echo.
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ERROR: Failed to install Python packages.
    pause
    exit /b 1
)
echo.
echo [OK] Python packages installed.

REM Install Playwright browser
echo.
echo [2/3] Installing Playwright Chromium browser...
echo.
python -m playwright install chromium

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo WARNING: Playwright browser installation may have failed.
    echo You can try manually: playwright install chromium
)
echo.
echo [OK] Playwright browser installed.

REM Check for system dependencies
echo.
echo [3/3] Checking system dependencies...
echo.

REM Check Pandoc
where pandoc >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo [MISSING] Pandoc not found.
    echo          Install from: https://pandoc.org/installing.html
    echo          Or run: choco install pandoc
    set MISSING_DEPS=1
) else (
    echo [OK] Pandoc found.
)

REM Check XeLaTeX (part of MiKTeX or TeX Live)
where xelatex >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo [MISSING] XeLaTeX not found.
    echo          Install MiKTeX from: https://miktex.org/download
    echo          Or run: choco install miktex
    set MISSING_DEPS=1
) else (
    echo [OK] XeLaTeX found.
)

echo.
echo ============================================

if defined MISSING_DEPS (
    echo.
    echo WARNING: Some system dependencies are missing.
    echo Please install them manually or use Chocolatey:
    echo.
    echo   choco install pandoc miktex -y
    echo.
    echo Also make sure to install Ubuntu fonts:
    echo   https://fonts.google.com/specimen/Ubuntu
    echo.
) else (
    echo.
    echo SUCCESS! All dependencies are installed.
    echo.
    echo Don't forget to install Ubuntu fonts if not already:
    echo   https://fonts.google.com/specimen/Ubuntu
    echo.
    echo You can now generate the book with:
    echo   ./makebook.bat
    echo.
)

echo ============================================
pause




