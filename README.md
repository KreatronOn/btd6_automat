# btd6_automat

# ==🟡project wip==

### About:
btd6_automat is a macro-like python script that allows for basic automation of tower placing and modifying
it is configured for full monkey knowledge setup and is meant to automate boring part of the game (like getting sapper achievement)
I assume that the user has some programming knowledge, knows python syntax and how to run a python script

---
### ==🔴WARNING!!!==
this script will most likely result in a ban if used in most of online competitive modes (especially races) and in serious accusations of being a jerk and/or a noob

---
### Usage:
1. Download script
2. Open main.py
3. Modify the main() function
4. Make sure that btd6 window is on entire screen and nothing will be covering it
5. Run main()
6. Click on btd6 window

---
### Documentation:
vec2 - class used for screen positions
	attributes:
		 x: float - the x position
		 y: float - the y position
	constructor:
		(x:float, y:float) - if left blank gives 0, 0
	supported operations:
		add
		sub
		mul

upgrade - holds 3 ints for each upgrade path
	attributes:
		a: int - top path
		b: int - mid path
		c: int - bot path
	constructor:
		(a:int, b:int, c:int) - if left blank gives 0, 0, 0
	methods:
		is_valid() - returns a bool if the upgrades are valid (for example 111 gives false, 034 gives false )

monkey - class for a tower

---
to be continued

bullet points to be added to readme:
- think of this as a library for writing your own macros
- link to ninja kiwi terms of service
- documentation is in line, fix

? - yea i dont know if ill do that
functionality to be added:
- finish tower settings (the ones changed with pageup, pagedown)
- finish targeting on towers with alternate targeting
- add proper controls for each ability?
- round_wait(round) that could read the current round and wait till given one
- add support for different aspect ratios (mainly the cost and round grab)
- add functions to start a given map on given difficulty
- map with golden balloon map detection?
- hero selection function