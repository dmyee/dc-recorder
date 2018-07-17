WinActivate, Dota 2
Send, \
Sleep 500
Send, playdemo replays/3987626377{Enter}

; TBD how long does it take for the game to load?
; Better to have some sort of event wait here than a sleep
Sleep 15000
Send, demo_pause{Enter}
Send, demo_goto 10700{Enter}
Sleep, 2000 ; TBD how long does it take for the game to load scene? event-wait is better
Send, \ ; Hide console
; TBD verify console is gone, game clock is correct

; TBD how long does this take to execute? game play is being lost...
Send, {F9}
RunWait, pipenv run python C:\Users\Darren\Documents\GitHub\recorder\win\obs-start.py, C:\Users\Darren\Documents\GitHub\recorder\win
Sleep, 5000
RunWait, pipenv run python C:\Users\Darren\Documents\GitHub\recorder\win\obs-stop.py, C:\Users\Darren\Documents\GitHub\recorder\win

WinActivate, Dota 2
Send, {F9}
; TBD verify game clock is correct

Send, \demo_pause{Enter}
Send, demo_goto 15000{Enter}
Sleep, 2000
Send, demo_resume{Enter}\

; TBD how long does this take to execute? game play is being lost...
RunWait, pipenv run python C:\Users\Darren\Documents\GitHub\recorder\win\obs-start.py, C:\Users\Darren\Documents\GitHub\recorder\win
Sleep, 5000
RunWait, pipenv run python C:\Users\Darren\Documents\GitHub\recorder\win\obs-stop.py, C:\Users\Darren\Documents\GitHub\recorder\win
