import time
from mokey import monkey
from myvar import vec2, upgrade
from menus import game_to_main, difficulty_select, map_select

def script():
    map_select("skull_tweak")

    difficulty_select("hard_standard")

    game_to_main()


    # monkey1 = monkey(vec2(0.3, 0.5), "handler")
    # monkey2 = monkey(vec2(0.3, 0.6), "handler")

    # monkey1.upgrd(upgrade(0, 2, 0))
    # monkey2.upgrd(upgrade(0, 1, 0))

    # #monkey1.should_target_camo(True)
    # time.sleep(1)
    # monkey1.set_option(vec2(0.2, 0.5))
    # monkey2.set_option(monkey1)
    # #monkey1.set_option()