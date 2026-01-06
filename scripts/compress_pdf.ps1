param(
  [Parameter(Mandatory=$true)][string]$InputFile,
  [Parameter(Mandatory=$false)][string]$Profile = "/ebook",
  [Parameter(Mandatory=$false)][string]$GhostscriptPath
)

$ErrorActionPreference = "Stop"

if (-not (Test-Path $InputFile)) {
  Write-Host "compress_pdf: Input file not found: $InputFile"
  exit 1
}

function Resolve-Ghostscript {
  # Prefer 64-bit, fall back to 32-bit. Try PowerShell resolution first, then where.exe.
  $candidates = @("gswin64c.exe", "gswin32c.exe", "gs.exe")
  foreach ($c in $candidates) {
    $cmd = Get-Command $c -ErrorAction SilentlyContinue
    if ($cmd) { return $cmd.Source }
  }
  foreach ($c in $candidates) {
    $found = (& where.exe $c 2>$null | Select-Object -First 1)
    if ($found) { return $found }
  }

  # Common Windows install locations (Ghostscript installer does not always add to PATH)
  $roots = @(
    ${env:ProgramFiles},
    ${env:ProgramFiles(x86)}
  ) | Where-Object { $_ -and (Test-Path $_) }

  foreach ($root in $roots) {
    $gsRoot = Join-Path $root "gs"
    if (-not (Test-Path $gsRoot)) { continue }
    $bins = Get-ChildItem -Path $gsRoot -Directory -Filter "gs*" -ErrorAction SilentlyContinue |
      ForEach-Object { Join-Path $_.FullName "bin" }
    foreach ($bin in $bins) {
      foreach ($exe in @("gswin64c.exe","gswin32c.exe")) {
        $p = Join-Path $bin $exe
        if (Test-Path $p) { return $p }
      }
    }
  }

  return $null
}

$gsPath = $GhostscriptPath
if (-not $gsPath) {
  $gsPath = Resolve-Ghostscript
}
if (-not $gsPath) {
  Write-Host "compress_pdf: Ghostscript not found (gswin64c/gswin32c). Skipping."
  exit 0
}

$tmp = "$InputFile.compressed.pdf"

$gsArgs = @(
  "-sDEVICE=pdfwrite"
  "-dCompatibilityLevel=1.4"
  "-dPDFSETTINGS=$Profile"
  "-dAutoRotatePages=/None"
  "-dNOPAUSE"
  "-dQUIET"
  "-dBATCH"
  "-sOutputFile=$tmp"
  $InputFile
)

& $gsPath @gsArgs

if (-not (Test-Path $tmp)) {
  Write-Host "compress_pdf: Compression failed to produce output."
  exit 0
}

$orig = (Get-Item $InputFile).Length
$cmp  = (Get-Item $tmp).Length

if ($cmp -lt $orig) {
  Move-Item -Force $tmp $InputFile
  Write-Host ("compress_pdf: Compressed {0:N2}MB -> {1:N2}MB" -f ($orig/1MB), ($cmp/1MB))
} else {
  Remove-Item -Force $tmp
  Write-Host ("compress_pdf: Skipped (not smaller) {0:N2}MB <= {1:N2}MB" -f ($orig/1MB), ($cmp/1MB))
}

exit 0

