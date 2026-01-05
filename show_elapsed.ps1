# Show elapsed time from timer_start.xml
# Be tolerant: if the timer file is missing/corrupt, don't break the batch output.

$timerPath = 'timer_start.xml'
if (-not (Test-Path $timerPath)) {
  Write-Host "[Elapsed: 00:00:00]" -NoNewline
  exit 0
}

try {
  $startTime = Import-Clixml -Path $timerPath
  $elapsed = (Get-Date) - $startTime
  $h = [math]::Floor($elapsed.TotalHours)
  $m = $elapsed.Minutes
  $s = $elapsed.Seconds
  Write-Host "[Elapsed: $($h.ToString('00')):$($m.ToString('00')):$($s.ToString('00'))]" -NoNewline
} catch {
  Write-Host "[Elapsed: 00:00:00]" -NoNewline
  exit 0
}

