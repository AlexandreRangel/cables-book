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
python scripts/sync_youtube_thumbnails.py
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Thumbnail sync failed.
    if exist timer_start.xml del timer_start.xml
    exit /b 1
)

REM Set file paths
set TEMP_MD=temp_combined_book.md
set OUTPUT_PDF_FINAL=cables-gl-book.pdf
set OUTPUT_PDF_TMP=cables-gl-book.build.pdf
set OUTPUT_PDF=%OUTPUT_PDF_FINAL%
set HEADER_FILE=latex-header.tex

REM Check header file exists
if not exist %HEADER_FILE% (
    echo ERROR: Header file %HEADER_FILE% not found.
    if exist timer_start.xml del timer_start.xml
    exit /b 1
)

REM Do NOT delete the final PDF up-front (it may be open/locked by a viewer).
REM Instead, render to a temp PDF and then attempt to replace the final atomically.
if exist %OUTPUT_PDF_TMP% del %OUTPUT_PDF_TMP%

powershell -ExecutionPolicy Bypass -File "show_elapsed.ps1"
echo [3/5] Combining chapters with proper UTF-8 encoding...

REM Use PowerShell to combine files with proper UTF-8 encoding
REM Cover will be added separately before TOC, then chapters 1-12, then all section 13 files dynamically
powershell -ExecutionPolicy Bypass -Command "& { $startTime = Import-Clixml -Path 'timer_start.xml'; $files = @('chapters\01-introduction.md', 'chapters\02-getting-started.md', 'chapters\03-2d-graphics.md', 'chapters\04-3d-graphics.md', 'chapters\05-texturing.md', 'chapters\06-shaders-glsl.md', 'chapters\07-javascript-ops.md', 'chapters\08-audio-sound.md', 'chapters\09-animation-timeline.md', 'chapters\10-interfaces.md', 'chapters\11-export-deployment.md', 'chapters\12-video-tutorials.md'); $section13Files = Get-ChildItem -Path 'chapters' -Filter '13-*.md' | Where-Object { $_.Name -ne '13-_AllOps.md' } | Sort-Object Name | ForEach-Object { $_.FullName }; $content = ''; foreach ($f in $files) { if (Test-Path $f) { $elapsed = (Get-Date) - $startTime; $h = [math]::Floor($elapsed.TotalHours); $m = $elapsed.Minutes; $s = $elapsed.Seconds; Write-Host ('[Elapsed: ' + $h.ToString('00') + ':' + $m.ToString('00') + ':' + $s.ToString('00') + ']') -NoNewline; Write-Host ('  Adding: ' + $f); $chapterText = (Get-Content $f -Raw -Encoding UTF8); $chapterText = $chapterText.TrimEnd(); $chapterText = $chapterText -replace '(\r?\n)\s*---\s*$', '$1'; $content += $chapterText; $content += [char]10 + [char]10 + '\pagebreak' + [char]10 + [char]10; } }; Write-Host ('  Adding ' + $section13Files.Count + ' section 13 files...'); foreach ($f in $section13Files) { $elapsed = (Get-Date) - $startTime; $h = [math]::Floor($elapsed.TotalHours); $m = $elapsed.Minutes; $s = $elapsed.Seconds; Write-Host ('[Elapsed: ' + $h.ToString('00') + ':' + $m.ToString('00') + ':' + $s.ToString('00') + ']') -NoNewline; Write-Host ('  Adding: ' + $f); $chapterText = (Get-Content $f -Raw -Encoding UTF8); $chapterText = $chapterText.TrimEnd(); $chapterText = $chapterText -replace '(\r?\n)\s*---\s*$', '$1'; $content += $chapterText; $content += [char]10 + [char]10 + '\pagebreak' + [char]10 + [char]10; }; $content = $content -replace '!\[\[([^\]]+)\]\]', '![](C:/Dropbox/Rangel-Vault/Media/image/$1)'; $content = $content -replace '\.svg\)', '.pdf)'; [System.IO.File]::WriteAllText('temp_combined_book.md', $content, [System.Text.Encoding]::UTF8) }"

if not exist %TEMP_MD% (
    echo ERROR: Failed to combine chapters.
    if exist timer_start.xml del timer_start.xml
    exit /b 1
)

powershell -ExecutionPolicy Bypass -File "show_elapsed.ps1"
echo [4/5] Generating PDF...

REM Use PowerShell script to show page-by-page progress
powershell -ExecutionPolicy Bypass -File "generate_pdf_with_progress.ps1" -InputFile "%TEMP_MD%" -OutputFile "%OUTPUT_PDF_TMP%" -HeaderFile "%HEADER_FILE%"
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: PDF generation failed.
    if exist timer_start.xml del timer_start.xml
    exit /b 1
)

REM Try to replace the final PDF; if it is locked, keep the temp PDF and continue.
move /y "%OUTPUT_PDF_TMP%" "%OUTPUT_PDF_FINAL%" >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    set OUTPUT_PDF=%OUTPUT_PDF_FINAL%
) else (
    echo NOTE: Could not overwrite "%OUTPUT_PDF_FINAL%" - it may be open. Keeping "%OUTPUT_PDF_TMP%".
    set OUTPUT_PDF=%OUTPUT_PDF_TMP%
)

powershell -ExecutionPolicy Bypass -File "show_elapsed.ps1"
echo [5/5] Cleaning up...
if exist %TEMP_MD% del %TEMP_MD%
if exist temp_debug.tex del temp_debug.tex

REM Check if PDF was created (avoid parentheses blocks; cmd.exe is picky with () in PowerShell strings)
if not exist %OUTPUT_PDF% goto pdf_fail

call :compress_pdf

powershell -NoProfile -Command "$startTime = Import-Clixml -Path 'timer_start.xml'; $elapsed = (Get-Date) - $startTime; $h = [math]::Floor($elapsed.TotalHours); $m = $elapsed.Minutes; $s = $elapsed.Seconds; Write-Host ('[Total Time: ' + $h.ToString('00') + ':' + $m.ToString('00') + ':' + $s.ToString('00') + ']')"
echo.
echo ============================================
echo SUCCESS! PDF created: %OUTPUT_PDF%
echo ============================================
echo.
REM Play sound notification using PowerShell text-to-speech at 50% volume
powershell -NoProfile -Command "Add-Type -AssemblyName System.Speech; $synth = New-Object System.Speech.Synthesis.SpeechSynthesizer; $synth.Volume = 50; $synth.Speak('Beep Beeep Cursor said: the pdf generation is complete.')"
if exist timer_start.xml del timer_start.xml
exit /b 0

:pdf_fail
echo.
echo ERROR: PDF generation failed.
echo.
echo Make sure you have:
echo   - XeLaTeX installed (MiKTeX or TeX Live)
echo   - Ubuntu fonts installed
echo.
if exist timer_start.xml del timer_start.xml
exit /b 1

:compress_pdf
REM Optional: compress PDF (requires Ghostscript). Replaces output only if smaller.
REM You can change the profile: /screen (smallest), /ebook (balanced), /printer (higher quality)
set PDF_COMPRESS_PROFILE=/printer
set "GSCMD="
for /f "usebackq delims=" %%G in (`where gswin64c 2^>nul`) do (
    set "GSCMD=%%G"
    goto gs_found
)
for /f "usebackq delims=" %%G in (`where gswin32c 2^>nul`) do (
    set "GSCMD=%%G"
    goto gs_found
)

REM Fallback: common install path (Ghostscript installer may not add to PATH)
for /d %%D in ("C:\Program Files\gs\gs*") do (
    if exist "%%D\bin\gswin64c.exe" (
        set "GSCMD=%%D\bin\gswin64c.exe"
        goto gs_found
    )
)
for /d %%D in ("C:\Program Files (x86)\gs\gs*") do (
    if exist "%%D\bin\gswin32c.exe" (
        set "GSCMD=%%D\bin\gswin32c.exe"
        goto gs_found
    )
)
:gs_found
if not defined GSCMD goto :eof
echo.
echo ============================================
echo Compressing PDF with Ghostscript (%PDF_COMPRESS_PROFILE%)...
echo ============================================
powershell -NoProfile -ExecutionPolicy Bypass -File "scripts\compress_pdf.ps1" -InputFile "%OUTPUT_PDF%" -Profile "%PDF_COMPRESS_PROFILE%" -GhostscriptPath "%GSCMD%"
goto :eof
