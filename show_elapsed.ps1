# Show elapsed time from timer_start.xml
$startTime = Import-Clixml -Path 'timer_start.xml'
$elapsed = (Get-Date) - $startTime
$h = [math]::Floor($elapsed.TotalHours)
$m = $elapsed.Minutes
$s = $elapsed.Seconds
Write-Host "[Elapsed: $($h.ToString('00')):$($m.ToString('00')):$($s.ToString('00'))]" -NoNewline

