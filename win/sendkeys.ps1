$wshell = New-Object -ComObject wscript.shell;
$wshell.AppActivate('Dota 2')
Sleep 1
$wshell.SendKeys('\/hello world')