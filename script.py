import time
from mokey import monkey
from myvar import vec2, upgrade
from menus import game_to_main, difficulty_select, map_select, click

import pyautogui

sauda_pos = vec2(0.4301, 0.6590)
wizard_pos = vec2(0.3297, 0.4910)
alchemist_pos = vec2(0.3969, 0.3382)
village_pos = vec2(0.3234, 0.3201)
glue_pos = vec2(0.3289, 0.4340)
mermonkey_pos = vec2(0.2715, 0.5319)
engineer_pos = vec2(0.8254, 0.9618)

def main_game():
    #sauda = monkey(sauda_pos, "hero")
    time.sleep(.2)
    pyautogui.keyDown('u')
    time.sleep(0.05)
    pyautogui.keyUp('u')
    click(sauda_pos)

    wizard = monkey(wizard_pos, "wizard")
    wizard.upgrd(upgrade(0, 2, 4))
    wizard.set_option(vec2(0.3664, 0.6951))

    alchemist = monkey(alchemist_pos, "alchemist")
    alchemist.upgrd(upgrade(3, 2, 0))

    wizard.upgrd(upgrade(0, 2, 5))

    alchemist.upgrd(upgrade(4, 2, 0))

    village = monkey(village_pos, "village")
    village.upgrd(upgrade(2, 3, 0))

    glue = monkey(glue_pos, "glue")
    glue.upgrd(upgrade(0, 2, 5))

    mermonkey = monkey(mermonkey_pos, "mermonkey")
    mermonkey.upgrd(upgrade(5, 2, 0))

    #engineer = monkey(engineer_pos, "engineer")
    #engineer.upgrd(upgrade(0, 5, 0))

def script():
    main_game()

    # map_select("skull_tweak")

    # difficulty_select("hard_standard")

    # game_to_main()


    # monkey1 = monkey(vec2(0.3, 0.5), "handler")
    # monkey2 = monkey(vec2(0.3, 0.6), "handler")

    # monkey1.upgrd(upgrade(0, 2, 0))
    # monkey2.upgrd(upgrade(0, 1, 0))

    # #monkey1.should_target_camo(True)
    # time.sleep(1)
    # monkey1.set_option(vec2(0.2, 0.5))
    # monkey2.set_option(monkey1)
    # #monkey1.set_option()