# Cannot use URL format to open Dota since it doesn't support args
$progname = "dota2"
$prog = "D:\SteamLibrary\steamapps\common\dota 2 beta\game\bin\win64\dota2.exe"

$running = Get-Process $progname -ErrorAction SilentlyContinue
if ($running -ne $null)
{
    Stop-Process -Name $progname
}

Start-Process -FilePath $prog "-console -map dota"
Start-Sleep -Seconds 10
Start-Process -FilePath ".\sendkeys.ahk"