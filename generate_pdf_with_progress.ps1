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
    "-V", "geometry:left=0.82in,right=0.82in,top=0.82in,bottom=0.82in",
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

# Temp file for stderr (where page numbers appear)
$tempErr = "temp_pandoc_stderr.txt"

# Remove old temp file
Remove-Item $tempErr -ErrorAction SilentlyContinue

# Record start time
$startTime = Get-Date

# Start pandoc in background
$cmdArgs = "/c pandoc $argString 2> $tempErr"
$proc = Start-Process -FilePath "cmd.exe" -ArgumentList $cmdArgs -NoNewWindow -PassThru

Write-Host "  Generating pages: " -NoNewline

# Monitor the stderr file for page numbers while pandoc runs
$lastPage = 0
$lastSize = 0
$spinChars = @('|', '/', '-', '\')
$spinIdx = 0

while (-not $proc.HasExited) {
    # Check if stderr file exists and has new content
    if (Test-Path $tempErr) {
        $currentSize = (Get-Item $tempErr).Length
        if ($currentSize -gt $lastSize) {
            $lastSize = $currentSize
            
            # Read the file and look for page numbers
            $content = Get-Content $tempErr -Raw -ErrorAction SilentlyContinue
            if ($content) {
                $pageMatches = [regex]::Matches($content, '\[(\d+)\]')
                foreach ($match in $pageMatches) {
                    $pageNum = [int]$match.Groups[1].Value
                    if ($pageNum -gt $lastPage) {
                        $lastPage = $pageNum
                        # Clear line and show new page number
                        Write-Host "`r  Generating pages: $lastPage   " -NoNewline
                    }
                }
            }
        }
    }
    
    # Show spinner if no page updates
    if ($lastPage -eq 0) {
        Write-Host "`r  Generating pages: $($spinChars[$spinIdx]) " -NoNewline
        $spinIdx = ($spinIdx + 1) % 4
    }
    
    Start-Sleep -Milliseconds 500
}

# Final check for page count
if (Test-Path $tempErr) {
    $content = Get-Content $tempErr -Raw -ErrorAction SilentlyContinue
    if ($content) {
        $pageMatches = [regex]::Matches($content, '\[(\d+)\]')
        foreach ($match in $pageMatches) {
            $pageNum = [int]$match.Groups[1].Value
            if ($pageNum -gt $lastPage) {
                $lastPage = $pageNum
            }
        }
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
