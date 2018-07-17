import csv, sys
import os.path as path

MS_PER_TICK = 1000 / 30

def write_ahk_header(file, demo_name):
	file.write("""WinActivate, Dota 2
Send, \\
Sleep 50
Send, playdemo replays/{demo_name}{{Enter}}
Send, \\
Sleep 15000
""".format(demo_name = demo_name))

def write_ahk_entry(file, player_idx, start_tick, end_tick):
	script_dir = "C:\\Users\\Darren\\Documents\\GitHub\\recorder\\win"
	duration = (end_tick - start_tick) * MS_PER_TICK
	
	file.write("""WinActivate, Dota 2
Send, \\
Sleep, 50
Send, demo_pause{{Enter}}
Send, demo_goto {start_tick}{{Enter}}
Sleep, 2000
Send, dota_spectator_mode 3{{Enter}}
Send, \\
Sleep, 50
Send, {player_idx}
Send, \\
Sleep, 100
Send, demo_resume{{Enter}}
Sleep, 500
Send, demo_pause{{Enter}}
Send, \\
Sleep, 50
RunWait, pipenv run python {script_dir}\\obs-start.py, {script_dir}
WinActivate, Dota 2
Send, {{F9}}
Sleep, {duration}
RunWait, pipenv run python {script_dir}\\obs-stop.py, {script_dir}
WinActivate, Dota 2
Send, {{F9}}
""".format(duration = int(duration),
	           			 start_tick = start_tick,
	           			 script_dir = script_dir,
	           			 player_idx = player_idx))

shots_file = sys.argv[1]
demo_name = path.splitext(path.basename(shots_file))[0]
output_ahk_file = sys.argv[2]
with open(shots_file, 'r') as sf, open(output_ahk_file, 'w') as of:
	write_ahk_header(of, demo_name)
	reader = csv.reader(sf, delimiter='\t')
	for player_idx, start_tick, end_tick in reader:
		write_ahk_entry(of, int(player_idx), int(start_tick), int(end_tick))
