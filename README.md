# btd6_automat

# ==🟡project wip==

### About:
> btd6_automat is a macro-like, library-like python script that allows for most* automation of tower placing and modifying, and some menu navigation, which also means there is little to no protection from when you type in something that will break the rest of the run
> it is configured for full monkey knowledge setup and is meant to automate boring part of the game (like getting sapper achievement)
> I assume that the user has some programming knowledge, knows python syntax and how to run a python script

`most* - right now I'm planning to have everything except for powers, and I'm still thinking of proper ability handling`
### Reqirements:
- 16:9 monitor
- python
- python packages: pyautogui mss opencv-python numpy pynput
- linux? untested

---
### ==🔴WARNING!!!==
this script will most likely result in a ban if used in most of online competitive modes (especially races (its not even optimized for that very well)) and in serious accusations of being a jerk and/or a noob

---
### Usage:
1. Download script
2. Check binds in data.py
3. Open script.py
4. Modify the script() function
5. Make sure that btd6 window is on entire screen and nothing will be covering it
6. Run main.py
7. Click on btd6 window

##### Notes:
- to get positions of monkeys i recommend using the provided calibrate.py script by just running it normally, take the monkey where you want to place it and click f4, after you get every position press f9 to close the script and it will give you vec2 coordinates in the same order you took them
- positions are normalized (from 0 to 1 on width and height)
- if you dont select map in script, make sure to set difficulty with difficulty(diff:int = 0), 0 - easy, 1 - normal, 2 - hard, 3 - impoppable, 4 - chimps (its mainly for pricing so this is enough)
- if you dont want to go through entire game before you can open sandbox, get the positions, and hope for the best
- you have to know where the game end screen and instamonkeys will appear in between the upgrades as right now their detection is manual
- if there was a save where you wanted to play the script will pause on the window with question if you want to overwrite the save for you to click what you want (if not i recommend turning the script off first)
- you can find more minimalistic documentation in script.py
- if anything will cover the cash by accident the program will most likely crash

---
### Documentation:
- vec2 - class used for screen positions, example: pos = vec2(0.5, 0.5)
	- attributes:
		 - x: float - the x position
		 - y: float - the y position
	- constructor:
		- (x:float, y:float) - if left blank gives 0, 0
	- supported operations:
		- +
		- -
		- *

- upgrade - holds 3 ints for each upgrade path
	- attributes:
		- a: int - top path
		- b: int - mid path
		- c: int - bot path
	- constructor:
		- (a:int, b:int, c:int) - if left blank gives 0, 0, 0
	- methods:
		- is_valid() - returns a bool if the upgrades are valid (for example 111 gives false, 034 gives false )
	- supported operations: (they check if each path meets the requirements, expect for when its 0 )
		- <
		- <=
		- >
		- >=
		- ==

monkey - class for a tower, example: dartmonkey = monkey(vec2(0.5, 0.5), type), full list of types at the bottom
	attributes:
		position - the vec2 position
		type - type of monkey 
	constructor:
		(pos:vec2, type:str) - full list of types at the bottom
	methods:
		upgrd(paths:upgrade) - upgrades the monkey in order from top to bottom paths
		ability(num:int) - simple function to use ability of monkey, num - ability number
		retargeting(target:str) - changes targeting to the specified one, list at the bottom
		set_option(opt:vec2 = None, double:vec2 = None) - for changing the option, if left bland it will just push the button, like the throwing hand for boomerang, or submerge for monkey sub, when one option it can be like the mermonkey totem thing, or the engineer foam, but also targeting for mortar, and double for heli patrol points
		should_target_camo(camo:bool) - should the monkey target camo first, for example on ninja
		dele() - deletes the monkey

other functions:
	map_select(name:str) - will choose the map you type in, either from main menu or map select screen
	difficulty_select(diff:str) - will choose difficulty, list below
	gold_bln_map(diff:int = 0) - plays the map with golden balloon, 0 for beginner maps, 1 - intermediate, 2 - advanced, 3 - expert
	monkey_team_map - you get it
	play(opt:int = -1) - changes play speed, -1 clicks space one, 1 sets the slower one, 2 faster one
	game_done_wait(home = True) - waits for the end screen and by default leaves to home, if False, turns on freeplay
	insta_monkey_wait() - will wait out until the instamonkey screen on 100 round and skip it
	time.sleep(x) - stops program for x seconds
	click(vec2) - makes a mouse click on specified coordinate

---
? - yea i dont know if ill do that
functionality to be added:
- checking for if something changed? like when placing the pixel color changes
- can you like delete just the last line from console, useful for cash_wait to not take up so mach space in output
- collection event interruption
- checking for correct data?
- round_wait(round) that could read the current round and wait till given one?
- some functions like place_next_to? that would account for monkey hitbox and place it right next to one another?
- the play struggles because you cant get to 0 normally