import time
from mokey import monkey, difficulty
from myvar import vec2, upgrade
from menus import game_to_main, difficulty_select, map_select, gold_bln_map, monkey_team_map, play, game_done_wait, insta_monkey_wait

import pyautogui

sauda_pos = vec2(0.4318, 0.6630)
wizard_pos = vec2(0.3297, 0.4910)
alchemist_pos = vec2(0.3969, 0.3382)
village_pos = vec2(0.3234, 0.3201)
glue_pos = vec2(0.3289, 0.4340)
mermonkey_pos = vec2(0.2715, 0.5319)
ace_pos = vec2(0.2672, 0.4407)
alchemis2_pos = vec2(0.1854, 0.3343)
tack_pos = vec2(0.3302, 0.6324)
village2_pos = vec2(0.2896, 0.6741)
alchemist3_pos = vec2(0.3911, 0.6333)
alchemist4_pos = vec2(0.3958, 0.6907)
perm_spike_pos = vec2(0.0573, 0.6704)

engineer_pos = vec2(0.8254, 0.9618)

def main_game():
    sauda = monkey(sauda_pos, "sauda")

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

    #engineer = monkey(engineer_pos, "engineer")
    #engineer.upgrd(upgrade(0, 5, 0))

def free_play():
    mermonkey = monkey(mermonkey_pos, "mermonkey")
    mermonkey.upgrd(upgrade(5, 2, 0))

    ace = monkey(ace_pos, "ace")
    ace.upgrd(upgrade(2, 0, 4))

    alchemis2 = monkey(alchemis2_pos, "alchemist")
    alchemis2.upgrd(upgrade(4, 2, 0))

    insta_monkey_wait()

    ace.upgrd(upgrade(2, 0, 5))

    tack = monkey(tack_pos, "tack")
    tack.upgrd(upgrade(5, 0, 2))

    village2 = monkey(village2_pos, "village")
    village2.upgrd(upgrade(4, 2, 0))

    alchemis3 = monkey(alchemist3_pos, "alchemist")
    alchemis3.upgrd(upgrade(4, 2, 0))

    alchemis4 = monkey(alchemist3_pos, "alchemist")
    alchemis4.upgrd(upgrade(4, 2, 0))

    perm_spike_pos = monkey(alchemist3_pos, "alchemist")
    perm_spike_pos.upgrd(upgrade(2, 0, 5))



def script():
    difficulty(2)

    for i in range(1):
        start = time.time()
        
        map_select("logs")
        difficulty_select("hard_standard")
        play(2)
        main_game()
        game_done_wait(False)
        free_play()
        game_done_wait()

        print("loop time:", time.time()-start)




