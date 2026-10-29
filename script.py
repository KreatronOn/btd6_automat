import time
from mokey import monkey, difficulty
from myvar import vec2, upgrade
from menus import game_to_main, difficulty_select, map_select, gold_bln_map, monkey_team_map, play
from menus import click

import pyautogui

sauda_pos = vec2(0.4301, 0.6590)
wizard_pos = vec2(0.3297, 0.4910)
alchemist_pos = vec2(0.3969, 0.3382)
village_pos = vec2(0.3234, 0.3201)
glue_pos = vec2(0.3289, 0.4340)
mermonkey_pos = vec2(0.2715, 0.5319)
engineer_pos = vec2(0.8254, 0.9618)

saudap = vec2(0.3521, 0.3306)
bucp = vec2(0.3760, 0.4917)

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
    #every 100 rounds the additional insta monkey
    map_select("spa_pits")
    difficulty_select("easy_standard")

    play(2)

    time.sleep(.2)
    pyautogui.keyDown('u')
    time.sleep(0.05)
    pyautogui.keyUp('u')
    click(saudap)

    buc = monkey(bucp, "buccaneer")
    buc.upgrd(upgrade(0, 4, 2))
