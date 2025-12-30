@echo off
REM ============================================
REM Cables.gl Book PDF Generator
REM ============================================

echo.
echo ============================================
echo Cables.gl Book - PDF Generator
echo ============================================
echo.

REM Refresh PATH to include Pandoc
call refreshenv >nul 2>&1
set PATH=%PATH%;C:\Program Files\Pandoc;%LOCALAPPDATA%\Pandoc

REM Check if Pandoc is installed
where pandoc >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Pandoc is not installed or not in PATH.
    echo Please install from: https://pandoc.org/installing.html
    exit /b 1
)

echo [1/5] Pandoc found.

REM Convert SVG files to PDF (XeLaTeX doesn't support SVG natively)
echo [2/5] Converting SVG images to PDF format...
python convert_svg_to_pdf.py
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: SVG to PDF conversion failed.
    echo Make sure svglib and reportlab are installed: pip install svglib reportlab
    exit /b 1
)

REM Set file paths
set TEMP_MD=temp_combined_book.md
set OUTPUT_PDF=cables-gl-book.pdf
set HEADER_FILE=latex-header.tex

REM Check header file exists
if not exist %HEADER_FILE% (
    echo ERROR: Header file %HEADER_FILE% not found.
    exit /b 1
)

REM Delete old PDF to verify new one is created
if exist %OUTPUT_PDF% del %OUTPUT_PDF%

echo [3/5] Combining chapters with proper UTF-8 encoding...

REM Use PowerShell to combine files with proper UTF-8 encoding
REM Cover page first, then chapters 1-12, then all section 13 files dynamically
powershell -ExecutionPolicy Bypass -Command "& { $files = @('chapters\01-introduction.md', 'chapters\02-getting-started.md', 'chapters\03-2d-graphics.md', 'chapters\04-3d-graphics.md', 'chapters\05-texturing.md', 'chapters\06-shaders-glsl.md', 'chapters\07-javascript-ops.md', 'chapters\08-audio-sound.md', 'chapters\09-animation-timeline.md', 'chapters\10-interfaces.md', 'chapters\11-export-deployment.md', 'chapters\12-video-tutorials.md'); $section13Files = Get-ChildItem -Path 'chapters' -Filter '13-*.md' | Sort-Object Name | ForEach-Object { $_.FullName }; $content = ''; if (Test-Path 'chapters\0-Cover.md') { Write-Host '  Adding: chapters\0-Cover.md'; $content += (Get-Content 'chapters\0-Cover.md' -Raw -Encoding UTF8); $content += [char]10 + [char]10; }; foreach ($f in $files) { if (Test-Path $f) { Write-Host ('  Adding: ' + $f); $content += '\pagebreak' + [char]10 + [char]10; $content += (Get-Content $f -Raw -Encoding UTF8); $content += [char]10 + [char]10; } }; Write-Host ('  Adding ' + $section13Files.Count + ' section 13 files...'); foreach ($f in $section13Files) { Write-Host ('  Adding: ' + $f); $content += '\pagebreak' + [char]10 + [char]10; $content += (Get-Content $f -Raw -Encoding UTF8); $content += [char]10 + [char]10; }; $content = $content -replace '!\[\[([^\]]+)\]\]', '![](C:/Dropbox/Rangel-Vault/Media/image/$1)'; $content = $content -replace '\.svg\)', '.pdf)'; [System.IO.File]::WriteAllText('temp_combined_book.md', $content, [System.Text.Encoding]::UTF8) }"

if not exist %TEMP_MD% (
    echo ERROR: Failed to combine chapters.
    exit /b 1
)

echo [4/5] Generating PDF...

pandoc %TEMP_MD% -o %OUTPUT_PDF% --pdf-engine=xelatex --pdf-engine-opt=-interaction=nonstopmode --resource-path=chapters -H %HEADER_FILE% -V geometry:"left=0.82in,right=0.82in,top=0.82in,bottom=0.82in" -V mainfont="Ubuntu" -V sansfont="Ubuntu" -V monofont="Ubuntu Mono" -V fontsize=11pt -V linestretch=1.3 --toc --toc-depth=3 --number-sections -V papersize=letter --syntax-highlighting=none 2>&1 | findstr /V /C:"major issue: So far, you have not checked for MiKTeX updates" | findstr /V /C:"miktex-dvipdfmx: major issue"

echo [5/5] Cleaning up...
if exist %TEMP_MD% del %TEMP_MD%
if exist temp_debug.tex del temp_debug.tex

REM Check if PDF was created
if exist %OUTPUT_PDF% (
    echo.
    echo ============================================
    echo SUCCESS! PDF created: %OUTPUT_PDF%
    echo ============================================
    echo.
    exit /b 0
) else (
    echo.
    echo ERROR: PDF generation failed.
    echo.
    echo Make sure you have:
    echo   - XeLaTeX installed (MiKTeX or TeX Live)
    echo   - Ubuntu fonts installed
    echo.
    exit /b 1
)
