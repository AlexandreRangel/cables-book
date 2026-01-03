# PowerShell script to generate PDF with REAL-TIME page progress
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
    "-V", "papersize=letter",
    "--syntax-highlighting=none"
)

# Quote arguments with spaces
$quotedArgs = $pandocArgs | ForEach-Object { 
    if ($_ -match '\s') { "`"$_`"" } else { $_ } 
}
$argString = $quotedArgs -join " "

# Temp files
$tempErr = "temp_pandoc_stderr.txt"
$tempOut = "temp_pandoc_stdout.txt"

# Remove old temp files
Remove-Item $tempErr -ErrorAction SilentlyContinue
Remove-Item $tempOut -ErrorAction SilentlyContinue

# Record start time
$startTime = Get-Date

# Start pandoc with output redirection
$cmdArgs = "/c pandoc $argString > $tempOut 2> $tempErr"
$proc = Start-Process -FilePath "cmd.exe" -ArgumentList $cmdArgs -NoNewWindow -PassThru

Write-Host "  Generating pages: " -NoNewline

# Monitor output files and log files for page numbers
$lastPage = 0
$lastErrSize = 0
$lastOutSize = 0
$lastLogCheck = $startTime
$spinChars = @('|', '/', '-', '\')
$spinIdx = 0

while (-not $proc.HasExited) {
    $foundPage = $false
    
    # Check stderr file
    if (Test-Path $tempErr) {
        $currentSize = (Get-Item $tempErr).Length
        if ($currentSize -gt $lastErrSize) {
            $lastErrSize = $currentSize
            $content = Get-Content $tempErr -Raw -ErrorAction SilentlyContinue
            if ($content) {
                # Look for [1], [2], etc. pattern
                $pageMatches = [regex]::Matches($content, '\[(\d+)\]')
                foreach ($match in $pageMatches) {
                    $pageNum = [int]$match.Groups[1].Value
                    if ($pageNum -gt $lastPage) {
                        $lastPage = $pageNum
                        $foundPage = $true
                    }
                }
            }
        }
    }
    
    # Check stdout file
    if (Test-Path $tempOut) {
        $currentSize = (Get-Item $tempOut).Length
        if ($currentSize -gt $lastOutSize) {
            $lastOutSize = $currentSize
            $content = Get-Content $tempOut -Raw -ErrorAction SilentlyContinue
            if ($content) {
                $pageMatches = [regex]::Matches($content, '\[(\d+)\]')
                foreach ($match in $pageMatches) {
                    $pageNum = [int]$match.Groups[1].Value
                    if ($pageNum -gt $lastPage) {
                        $lastPage = $pageNum
                        $foundPage = $true
                    }
                }
            }
        }
    }
    
    # Check for XeLaTeX log files in current directory and subdirectories
    $now = Get-Date
    if (($now - $lastLogCheck).TotalSeconds -gt 1) {
        $lastLogCheck = $now
        $logFiles = Get-ChildItem -Path "." -Filter "*.log" -Recurse -ErrorAction SilentlyContinue | 
                    Where-Object { $_.LastWriteTime -gt $startTime -and $_.Length -gt 0 }
        foreach ($log in $logFiles) {
            try {
                $logContent = Get-Content $log.FullName -Raw -ErrorAction SilentlyContinue
                if ($logContent) {
                    # Look for page numbers - XeLaTeX outputs them as [1], [2], etc.
                    $pageMatches = [regex]::Matches($logContent, '\[(\d+)\]')
                    foreach ($match in $pageMatches) {
                        $pageNum = [int]$match.Groups[1].Value
                        if ($pageNum -gt $lastPage) {
                            $lastPage = $pageNum
                            $foundPage = $true
                        }
                    }
                }
            } catch {
                # Skip files that are locked or can't be read
            }
        }
    }
    
    # Update display if we found a new page
    if ($foundPage) {
        Write-Host "`r  Generating page $lastPage...    " -NoNewline
    } elseif ($lastPage -eq 0) {
        # Show spinner only if we haven't found any pages yet
        Write-Host "`r  Generating pages: $($spinChars[$spinIdx]) " -NoNewline
        $spinIdx = ($spinIdx + 1) % 4
    }
    
    Start-Sleep -Milliseconds 200
}

# Final comprehensive check for page count
$allLogFiles = Get-ChildItem -Path "." -Filter "*.log" -Recurse -ErrorAction SilentlyContinue
foreach ($log in $allLogFiles) {
    try {
        $logContent = Get-Content $log.FullName -Raw -ErrorAction SilentlyContinue
        if ($logContent) {
            $pageMatches = [regex]::Matches($logContent, '\[(\d+)\]')
            foreach ($match in $pageMatches) {
                $pageNum = [int]$match.Groups[1].Value
                if ($pageNum -gt $lastPage) {
                    $lastPage = $pageNum
                }
            }
        }
    } catch {
        # Skip locked files
    }
}

$exitCode = $proc.ExitCode

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

# Show result
Write-Host ""
Write-Host ""
if ($exitCode -eq 0) {
    if ($lastPage -gt 0) {
        Write-Host "  Done! Generated $lastPage pages in $timeStr."
    } else {
        Write-Host "  PDF generation completed in $timeStr."
        Write-Host "  (Page count could not be determined from log files)"
    }
    Write-Host ""
} else {
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
}

# Clean up temp file on success
if ($exitCode -eq 0) {
    Remove-Item $tempErr -ErrorAction SilentlyContinue
}

exit $exitCode
