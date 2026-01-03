# PowerShell script to generate PDF with REAL-TIME page progress
# Uses file monitoring for XeLaTeX log to detect page numbers
param(
    [string]$InputFile,
    [string]$OutputFile,
    [string]$HeaderFile
)

Write-Host ""
Write-Host "[4/5] Generating PDF..."
Write-Host ""

# Ensure we're in the right directory
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptDir

# Get temp directory where XeLaTeX will work
$userTemp = [System.IO.Path]::GetTempPath()

# Check if cover file exists and add it before TOC
$coverFile = "chapters\00-Cover.md"
$coverArg = ""
if (Test-Path $coverFile) {
    # Use --include-before-body to place cover before TOC
    # The cover uses \begin{titlepage} which Pandoc will handle correctly
    $coverArg = "--include-before-body=$coverFile"
    Write-Host "  Cover file found, will be included before TOC"
}

# Build pandoc command
$pandocArgs = @(
    $InputFile,
    "-o", $OutputFile,
    "--pdf-engine=xelatex",
    "--pdf-engine-opt=-interaction=nonstopmode",
    "--resource-path=chapters",
    "-H", $HeaderFile,
    "-V", "geometry:left=0.82in,right=0.82in,top=0.656in,bottom=0.656in",
    "-V", "mainfont=Ubuntu",
    "-V", "sansfont=Ubuntu",
    "-V", "monofont=Ubuntu Mono",
    "-V", "fontsize=11pt",
    "-V", "linestretch=0.96",
    "--toc",
    "--toc-depth=3",
    "--number-sections",
    "-V", "toc-title=Table of Contents",
    "-V", "papersize=letter",
    "--syntax-highlighting=none"
)

# Add cover file before TOC if it exists
if ($coverArg) {
    $pandocArgs += $coverArg
}

# Quote arguments with spaces
$quotedArgs = $pandocArgs | ForEach-Object { 
    if ($_ -match '\s') { "`"$_`"" } else { $_ } 
}
$argString = $quotedArgs -join " "

# Temp files
$tempErr = "temp_pandoc_stderr.txt"
$tempOut = "temp_pandoc_stdout.txt"

# Remove old temp files and PDF
Remove-Item $tempErr -ErrorAction SilentlyContinue
Remove-Item $tempOut -ErrorAction SilentlyContinue
Remove-Item $OutputFile -ErrorAction SilentlyContinue

# Record start time
$startTime = Get-Date

# Create a background job to run pandoc
$cmdLine = "pandoc $argString"
$proc = Start-Process -FilePath "cmd.exe" -ArgumentList "/c", "$cmdLine > $tempOut 2> $tempErr" -NoNewWindow -PassThru

Write-Host "  Generating pages: " -NoNewline

# Monitor for progress
$lastPage = 0
$spinChars = @('|', '/', '-', '\')
$spinIdx = 0

# Try to find the xelatex log file in temp directories
$foundLogFile = $null
$logCheckCount = 0

while (-not $proc.HasExited) {
    $foundPage = $false
    
    # Search for log files created after we started
    if (-not $foundLogFile -or -not (Test-Path $foundLogFile)) {
        try {
            # Look for media-* directories created by pandoc
            $mediaDir = Get-ChildItem -Path $userTemp -Filter "media-*" -Directory -ErrorAction SilentlyContinue |
                        Where-Object { $_.CreationTime -gt $startTime.AddSeconds(-5) } |
                        Sort-Object CreationTime -Descending |
                        Select-Object -First 1
            
            if ($mediaDir) {
                $logFiles = Get-ChildItem -Path $mediaDir.FullName -Filter "*.log" -ErrorAction SilentlyContinue |
                            Where-Object { $_.Length -gt 1000 } |
                            Sort-Object LastWriteTime -Descending
                
                if ($logFiles) {
                    $foundLogFile = $logFiles[0].FullName
                }
            }
        } catch {
            # Ignore errors in file searching
        }
        $logCheckCount++
    }
    
    # Read from the log file if found
    if ($foundLogFile -and (Test-Path $foundLogFile)) {
        try {
            # Read the last portion of the log file efficiently
            $logContent = Get-Content $foundLogFile -Tail 500 -ErrorAction SilentlyContinue | Out-String
            
            if ($logContent) {
                # Look for [page] patterns: [1] [2] [3] etc
                $pageMatches = [regex]::Matches($logContent, '\[(\d{1,4})\]')
                foreach ($match in $pageMatches) {
                    $pageNum = [int]$match.Groups[1].Value
                    if ($pageNum -gt $lastPage -and $pageNum -lt 5000) {
                        $lastPage = $pageNum
                        $foundPage = $true
                    }
                }
            }
        } catch {
            # File might be locked, skip
        }
    }
    
    # Also check stderr for final output
    if (Test-Path $tempErr) {
        try {
            $errContent = Get-Content $tempErr -Tail 100 -ErrorAction SilentlyContinue | Out-String
            if ($errContent) {
                # Look for page patterns
                $pageMatches = [regex]::Matches($errContent, '\[(\d{1,4})\]')
                foreach ($match in $pageMatches) {
                    $pageNum = [int]$match.Groups[1].Value
                    if ($pageNum -gt $lastPage -and $pageNum -lt 5000) {
                        $lastPage = $pageNum
                        $foundPage = $true
                    }
                }
                # Also look for "Output written on ... (N pages)"
                if ($errContent -match '\((\d+)\s+pages?\)') {
                    $pageNum = [int]$matches[1]
                    if ($pageNum -gt $lastPage) {
                        $lastPage = $pageNum
                        $foundPage = $true
                    }
                }
            }
        } catch {
            # Ignore
        }
    }
    
    # Update display
    if ($lastPage -gt 0) {
        Write-Host "`r  Generating pages: $lastPage     " -NoNewline
    } else {
        Write-Host "`r  Generating pages: $($spinChars[$spinIdx]) " -NoNewline
        $spinIdx = ($spinIdx + 1) % 4
    }
    
    Start-Sleep -Milliseconds 300
}

# Final check - read entire stderr for final page count
if (Test-Path $tempErr) {
    try {
        $content = Get-Content $tempErr -Raw -ErrorAction SilentlyContinue
        if ($content) {
            # Check for final page count
            if ($content -match '\((\d+)\s+pages?\)') {
                $pageNum = [int]$matches[1]
                if ($pageNum -gt $lastPage) {
                    $lastPage = $pageNum
                }
            }
        }
    } catch {
        # Ignore
    }
}

# Calculate elapsed time
$endTime = Get-Date
$elapsed = $endTime - $startTime
$minutes = [Math]::Floor($elapsed.TotalMinutes)
$seconds = $elapsed.Seconds

if ($minutes -gt 0) {
    $timeStr = "$minutes min $seconds sec"
} else {
    $timeStr = "$($elapsed.TotalSeconds.ToString('F1')) sec"
}

# Check if PDF was created - this is the most important check
$exitCode = 0
if (Test-Path $OutputFile) {
    # PDF exists - success!
    Write-Host ""
    Write-Host ""
    if ($lastPage -gt 0) {
        Write-Host "  Done! Generated $lastPage pages in $timeStr."
    } else {
        Write-Host "  PDF generation completed in $timeStr."
    }
    Write-Host ""
    $exitCode = 0
} else {
    # PDF doesn't exist - check process exit code
    $exitCode = $proc.ExitCode
    if ($exitCode -eq 0) {
        $exitCode = 1  # Force error if PDF doesn't exist
    }
    Write-Host "  PDF generation encountered issues."
    Write-Host ""
    
    # Show error output
    if (Test-Path $tempErr) {
        $errorContent = Get-Content $tempErr -ErrorAction SilentlyContinue
        if ($errorContent) {
            # Filter for actual errors
            $errors = $errorContent | Where-Object { $_ -match "(Error|Fatal|!)" }
            if ($errors) {
                Write-Host "Errors found:"
                $errors | Select-Object -First 10 | ForEach-Object { Write-Host "  $_" }
                Write-Host ""
            }
            
            Write-Host "Last output lines:"
            $lines = @($errorContent)
            $showCount = [Math]::Min(20, $lines.Count)
            $lines[-$showCount..-1] | ForEach-Object {
                if ($_ -and $_.Trim()) {
                    Write-Host "  $_"
                }
            }
            Write-Host ""
        }
    }
    $exitCode = 1
}

# Clean up temp files on success
if ($exitCode -eq 0) {
    Remove-Item $tempErr -ErrorAction SilentlyContinue
    Remove-Item $tempOut -ErrorAction SilentlyContinue
}

exit $exitCode
