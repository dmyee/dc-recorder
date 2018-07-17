About the files
----

### .dem file

This is the replay file itself

### .shots file

Indicates what shots to record. Each line indicates one shot.

Each line is in the following tab-separated format:
```
player_idx	start_tick	end_tick
```

`player_idx` is a digit 0-9 which indicates the player's index within the game, where 1-5 are the radiant heroes and 6-9 & 0 are the dire heroes.