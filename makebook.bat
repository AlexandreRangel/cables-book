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
    pause
    exit /b 1
)

echo [1/4] Pandoc found.

REM Set file paths
set TEMP_MD=temp_combined_book.md
set OUTPUT_PDF=cables-gl-book.pdf
set HEADER_FILE=latex-header.tex

REM Check header file exists
if not exist %HEADER_FILE% (
    echo ERROR: Header file %HEADER_FILE% not found.
    pause
    exit /b 1
)

REM Remove old temp file
if exist %TEMP_MD% del %TEMP_MD%

echo [2/4] Combining chapters...

REM Add title page
(
    echo # The Cables.gl Book
    echo.
    echo #### Alexandre Rangel, 2025
    echo.
    echo ---
    echo.
) > %TEMP_MD%

REM Combine all chapter files
for %%f in (chapters\01-introduction.md chapters\02-getting-started.md chapters\03-2d-graphics.md chapters\04-3d-graphics.md chapters\05-texturing.md chapters\06-shaders-glsl.md chapters\07-javascript-ops.md chapters\08-audio-sound.md chapters\09-animation-timeline.md chapters\10-export-deployment.md chapters\11-video-tutorials.md) do (
    if exist %%f (
        echo   Adding: %%f
        echo. >> %TEMP_MD%
        echo \pagebreak >> %TEMP_MD%
        echo. >> %TEMP_MD%
        type %%f >> %TEMP_MD%
        echo. >> %TEMP_MD%
    )
)

REM Convert wiki-link images ![[filename]] to full path
REM Images are stored in C:\Dropbox\Rangel-Vault\Media\image\
echo [2.5/4] Processing image links...
powershell -Command "$content = Get-Content 'temp_combined_book.md' -Raw; $content = $content -replace '!\[\[([^\]]+)\]\]', '![](C:/Dropbox/Rangel-Vault/Media/image/$1)'; $content | Out-File 'temp_combined_book2.md' -Encoding UTF8 -NoNewline"
if exist temp_combined_book2.md (
    del temp_combined_book.md
    ren temp_combined_book2.md temp_combined_book.md
)

echo [3/4] Generating PDF...

pandoc %TEMP_MD% ^
    -o %OUTPUT_PDF% ^
    --pdf-engine=xelatex ^
    --resource-path=chapters ^
    -H %HEADER_FILE% ^
    -V geometry:margin=1in ^
    -V mainfont="Ubuntu" ^
    -V sansfont="Ubuntu" ^
    -V monofont="Ubuntu Mono" ^
    -V fontsize=11pt ^
    -V linestretch=1.3 ^
    --toc ^
    --toc-depth=3 ^
    --number-sections ^
    -V papersize=letter ^
    --syntax-highlighting=none ^
    --quiet

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ERROR: PDF generation failed.
    echo.
    echo Make sure you have:
    echo   - XeLaTeX installed (MiKTeX or TeX Live)
    echo   - Ubuntu fonts installed
    echo   - Segoe UI Symbol and Segoe UI Emoji fonts (Windows default)
    echo.
    if exist %TEMP_MD% del %TEMP_MD%
    pause
    exit /b 1
)

echo [4/4] Cleaning up...
if exist %TEMP_MD% del %TEMP_MD%
if exist temp_debug.tex del temp_debug.tex

echo.
echo ============================================
echo SUCCESS! PDF created: %OUTPUT_PDF%
echo ============================================
echo.
pause
