@echo off
REM ============================================
REM Cables.gl Book PDF Generator
REM ============================================

echo.
echo ============================================
echo Cables.gl Book - PDF Generator
echo ============================================
echo.

REM Initialize start time in a file
powershell -Command "$startTime = Get-Date; $startTime | Export-Clixml -Path 'timer_start.xml'"

REM Announce PDF generation started
powershell -Command "Add-Type -AssemblyName System.Speech; $synth = New-Object System.Speech.Synthesis.SpeechSynthesizer; $synth.Volume = 50; $synth.Speak('Beep! Beep! Cursor says: PDF generation started.')"

REM Refresh PATH to include Pandoc
call refreshenv >nul 2>&1
set PATH=%PATH%;C:\Program Files\Pandoc;%LOCALAPPDATA%\Pandoc

REM Check if Pandoc is installed
where pandoc >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Pandoc is not installed or not in PATH.
    echo Please install from: https://pandoc.org/installing.html
    if exist timer_start.xml del timer_start.xml
    exit /b 1
)

powershell -ExecutionPolicy Bypass -File "show_elapsed.ps1"
echo [1/5] Pandoc found.

REM Convert SVG files to PDF (XeLaTeX doesn't support SVG natively)
powershell -ExecutionPolicy Bypass -File "show_elapsed.ps1"
echo [2/5] Converting SVG images to PDF format...
python convert_svg_to_pdf.py
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: SVG to PDF conversion failed.
    echo Make sure svglib and reportlab are installed: pip install svglib reportlab
    if exist timer_start.xml del timer_start.xml
    exit /b 1
)

powershell -ExecutionPolicy Bypass -File "show_elapsed.ps1"
echo [2.5/5] Syncing YouTube thumbnails...
if exist scripts\sync_youtube_thumbnails.py (
    python scripts/sync_youtube_thumbnails.py
    if %ERRORLEVEL% NEQ 0 (
        echo WARNING: Thumbnail sync failed, continuing anyway...
    )
) else (
    echo NOTE: sync_youtube_thumbnails.py not found, skipping thumbnail sync...
)

REM Set file paths
set TEMP_MD=temp_combined_book.md
set OUTPUT_PDF=cables-gl-book.pdf
set HEADER_FILE=latex-header.tex

REM Check header file exists
if not exist %HEADER_FILE% (
    echo ERROR: Header file %HEADER_FILE% not found.
    if exist timer_start.xml del timer_start.xml
    exit /b 1
)

REM Delete old PDF to verify new one is created
if exist %OUTPUT_PDF% del %OUTPUT_PDF%

powershell -ExecutionPolicy Bypass -File "show_elapsed.ps1"
echo [3/5] Combining chapters with proper UTF-8 encoding...

REM Use PowerShell to combine files with proper UTF-8 encoding
REM Cover will be added separately before TOC, then chapters 1-12, then all section 13 files dynamically
powershell -ExecutionPolicy Bypass -Command "& { $startTime = Import-Clixml -Path 'timer_start.xml'; $files = @('chapters\01-introduction.md', 'chapters\02-getting-started.md', 'chapters\03-2d-graphics.md', 'chapters\04-3d-graphics.md', 'chapters\05-texturing.md', 'chapters\06-shaders-glsl.md', 'chapters\07-javascript-ops.md', 'chapters\08-audio-sound.md', 'chapters\09-animation-timeline.md', 'chapters\10-interfaces.md', 'chapters\11-export-deployment.md', 'chapters\12-video-tutorials.md'); $section13Files = Get-ChildItem -Path 'chapters' -Filter '13-*.md' | Where-Object { $_.Name -ne '13-_AllOps.md' } | Sort-Object Name | ForEach-Object { $_.FullName }; $content = ''; foreach ($f in $files) { if (Test-Path $f) { $elapsed = (Get-Date) - $startTime; $h = [math]::Floor($elapsed.TotalHours); $m = $elapsed.Minutes; $s = $elapsed.Seconds; Write-Host ('[Elapsed: ' + $h.ToString('00') + ':' + $m.ToString('00') + ':' + $s.ToString('00') + ']') -NoNewline; Write-Host ('  Adding: ' + $f); $content += '\pagebreak' + [char]10 + [char]10; $content += (Get-Content $f -Raw -Encoding UTF8); $content += [char]10 + [char]10; } }; Write-Host ('  Adding ' + $section13Files.Count + ' section 13 files...'); foreach ($f in $section13Files) { $elapsed = (Get-Date) - $startTime; $h = [math]::Floor($elapsed.TotalHours); $m = $elapsed.Minutes; $s = $elapsed.Seconds; Write-Host ('[Elapsed: ' + $h.ToString('00') + ':' + $m.ToString('00') + ':' + $s.ToString('00') + ']') -NoNewline; Write-Host ('  Adding: ' + $f); $content += '\pagebreak' + [char]10 + [char]10; $content += (Get-Content $f -Raw -Encoding UTF8); $content += [char]10 + [char]10; }; $content = $content -replace '!\[\[([^\]]+)\]\]', '![](C:/Dropbox/Rangel-Vault/Media/image/$1)'; $content = $content -replace '\.svg\)', '.pdf)'; [System.IO.File]::WriteAllText('temp_combined_book.md', $content, [System.Text.Encoding]::UTF8) }"

if not exist %TEMP_MD% (
    echo ERROR: Failed to combine chapters.
    if exist timer_start.xml del timer_start.xml
    exit /b 1
)

powershell -ExecutionPolicy Bypass -File "show_elapsed.ps1"
echo [4/5] Generating PDF...

REM Use PowerShell script to show page-by-page progress
powershell -ExecutionPolicy Bypass -File "generate_pdf_with_progress.ps1" -InputFile "%TEMP_MD%" -OutputFile "%OUTPUT_PDF%" -HeaderFile "%HEADER_FILE%"
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: PDF generation failed.
    if exist timer_start.xml del timer_start.xml
    exit /b 1
)

powershell -ExecutionPolicy Bypass -File "show_elapsed.ps1"
echo [5/5] Cleaning up...
if exist %TEMP_MD% del %TEMP_MD%
if exist temp_debug.tex del temp_debug.tex

REM Check if PDF was created
if exist %OUTPUT_PDF% (
    REM Optional: compress PDF (requires Ghostscript). Replaces output only if smaller.
    REM You can change the profile: /screen (smallest), /ebook (balanced), /printer (higher quality)
    set PDF_COMPRESS_PROFILE=/ebook
    where gswin64c >nul 2>&1
    if %ERRORLEVEL% EQU 0 (
        echo.
        echo ============================================
        echo Compressing PDF with Ghostscript (%PDF_COMPRESS_PROFILE%)...
        echo ============================================
        set COMPRESSED_PDF=%OUTPUT_PDF%.compressed.pdf
        gswin64c -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=%PDF_COMPRESS_PROFILE% -dNOPAUSE -dQUIET -dBATCH -sOutputFile="%COMPRESSED_PDF%" "%OUTPUT_PDF%"
        if %ERRORLEVEL% EQU 0 (
            powershell -NoProfile -Command "$orig=(Get-Item '%OUTPUT_PDF%').Length; $cmp=(Get-Item '%COMPRESSED_PDF%').Length; if ($cmp -lt $orig) { Move-Item -Force '%COMPRESSED_PDF%' '%OUTPUT_PDF%'; Write-Host ('  Compressed: ' + [math]::Round(($orig/1MB),2) + 'MB -> ' + [math]::Round(($cmp/1MB),2) + 'MB') } else { Remove-Item -Force '%COMPRESSED_PDF%'; Write-Host ('  Skipped: compressed not smaller (' + [math]::Round(($orig/1MB),2) + 'MB <= ' + [math]::Round(($cmp/1MB),2) + 'MB)') }"
        ) else (
            echo WARNING: Ghostscript compression failed, keeping original PDF.
            if exist "%COMPRESSED_PDF%" del "%COMPRESSED_PDF%"
        )
    ) else (
        echo.
        echo NOTE: Ghostscript not found (gswin64c). Skipping PDF compression.
    )

    powershell -Command "$startTime = Import-Clixml -Path 'timer_start.xml'; $elapsed = (Get-Date) - $startTime; $h = [math]::Floor($elapsed.TotalHours); $m = $elapsed.Minutes; $s = $elapsed.Seconds; Write-Host ('[Total Time: ' + $h.ToString('00') + ':' + $m.ToString('00') + ':' + $s.ToString('00') + ']')"
    echo.
    echo ============================================
    echo SUCCESS! PDF created: %OUTPUT_PDF%
    echo ============================================
    echo.
    REM Play sound notification using PowerShell text-to-speech at 50% volume
    powershell -Command "Add-Type -AssemblyName System.Speech; $synth = New-Object System.Speech.Synthesis.SpeechSynthesizer; $synth.Volume = 50; $synth.Speak('Beep Beeep Cursor said: the pdf generation is complete.')"
    if exist timer_start.xml del timer_start.xml
    exit /b 0
) else (
    echo.
    echo ERROR: PDF generation failed.
    echo.
    echo Make sure you have:
    echo   - XeLaTeX installed (MiKTeX or TeX Live)
    echo   - Ubuntu fonts installed
    echo.
    if exist timer_start.xml del timer_start.xml
    exit /b 1
)
