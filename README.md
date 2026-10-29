# btd6_automat

# ==🟡project wip==

### About:
btd6_automat is a macro-like, library-like python script that allows for most* automation of tower placing and modifying, and some menu navigation, which also means there is little to no protection from when you type in something that will break the rest of the run
it is configured for full monkey knowledge setup and is meant to automate boring part of the game (like getting sapper achievement)
I assume that the user has some programming knowledge, knows python syntax and how to run a python script

`most* - right now I'm planning to have everything except for powers, and I'm still thinking of proper ability handling`

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

---
### Documentation:
- vec2 - class used for screen positions
	- attributes:
		 - x: float - the x position
		 - y: float - the y position
	- constructor:
		- (x:float, y:float) - if left blank gives 0, 0
	- supported operations:
		- add
		- sub
		- mul

- upgrade - holds 3 ints for each upgrade path
	- attributes:
		- a: int - top path
		- b: int - mid path
		- c: int - bot path
	- constructor:
		- (a:int, b:int, c:int) - if left blank gives 0, 0, 0
	- methods:
		- is_valid() - returns a bool if the upgrades are valid (for example 111 gives false, 034 gives false )

monkey - class for a tower

---
to be continued

bullet points to be added to readme:
- im using linux mint and testing on windows is required
- only works on 16:9
- needed packages
- if you already have a save on the map the script will pause for you to select if you want to overwrite it

? - yea i dont know if ill do that
functionality to be added:
- round_wait(round) that could read the current round and wait till given one
- hero selection function
- checking for correct data?
- checking for if something changed? like when placing the pixel color changes
- farm collecting while waiting
- heroes_price_c correct
- some functions like place_next_to? that would account for monkey hitbox and place it right next to one another?