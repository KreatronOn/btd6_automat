import time
import pyautogui
from mokey import monkey, difficulty
from myvar import vec2, upgrade
from menus import game_to_main, difficulty_select, map_select, gold_bln_map, monkey_team_map, play, game_done_wait, insta_monkey_wait


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

    alchemis4 = monkey(alchemist4_pos, "alchemist")
    alchemis4.upgrd(upgrade(4, 2, 0))

    perm_spike = monkey(perm_spike_pos, "spike")
    perm_spike.upgrd(upgrade(2, 0, 5))
def sapper_farm():
    for i in range(100):
        start = time.time()
        
        map_select("logs")
        difficulty_select("alternate_bloons_rounds")
        play(2)
        main_game()
        game_done_wait(False)
        free_play()
        game_done_wait()

        print("loop time:", time.time()-start)

gld_strt1_pos = {
    "in_the_loop": [
        vec2(0.6010, 0.6787),
        vec2(0.3318, 0.2898),
        vec2(0.5943, 0.2750),
        vec2(0.4370, 0.2963),
        vec2(0.3641, 0.4407),
        vec2(0.6729, 0.1843),
        vec2(0.4615, 0.2287),
        vec2(0.6229, 0.4639),
        vec2(0.6641, 0.2907),
    ],
    "skull_tweak": [
        vec2(0.2464, 0.5565),
        vec2(0.2490, 0.2463),
        vec2(0.5083, 0.6991),
        vec2(0.3078, 0.1120),
        vec2(0.2260, 0.0528),
        vec2(0.4005, 0.6676),
        vec2(0.3661, 0.2278),
        vec2(0.4062, 0.7500),
        vec2(0.5484, 0.6602),
    ],
    "three_mines_'round": [
        vec2(0.3839, 0.2306),
        vec2(0.5641, 0.3630),
        vec2(0.2198, 0.5352),
        vec2(0.5276, 0.5139),
        vec2(0.6594, 0.2704),
        vec2(0.2776, 0.5500),
        vec2(0.5417, 0.6648),
        vec2(0.5891, 0.5148),
        vec2(0.6203, 0.5231),
    ],
    "spa_pits": [
        vec2(0.3536, 0.3380),
        vec2(0.5266, 0.3352),
        vec2(0.3688, 0.5130),
        vec2(0.5828, 0.2074),
        vec2(0.5542, 0.1380),
        vec2(0.3005, 0.6093),
        vec2(0.5547, 0.2907),
        vec2(0.4313, 0.7593),
        vec2(0.5880, 0.6824),
    ],
    "tinkerton": [
        vec2(0.2188, 0.3722),
        vec2(0.7354, 0.4824),
        vec2(0.4922, 0.6454),
        vec2(0.6531, 0.4361),
        vec2(0.8375, 0.4324),
        vec2(0.4104, 0.6056),
        vec2(0.6526, 0.6037),
        vec2(0.3594, 0.5435),
        vec2(0.4224, 0.3417),
    ],
    "middle_of_the_road": [
        vec2(0.2766, 0.4090),
        vec2(0.4285, 0.8042),
        vec2(0.6945, 0.6056),
        vec2(0.4715, 0.9326),
        vec2(0.3859, 0.9208),
        vec2(0.5961, 0.5597),
        vec2(0.5840, 0.9514),
        vec2(0.6016, 0.4139),
        vec2(0.6430, 0.3563),
    ],
    "one_two_tree": [
        vec2(0.1328, 0.7713),
        vec2(0.7302, 0.3685),
        vec2(0.3766, 0.7269),
        vec2(0.6349, 0.2398),
        vec2(0.7646, 0.4148),
        vec2(0.4844, 0.7944),
        vec2(0.6094, 0.3750),
        vec2(0.2687, 0.7028),
        vec2(0.3792, 0.8556),
    ],
    "the_cabin": [
        vec2(0.3479, 0.1389),
        vec2(0.2844, 0.5472),
        vec2(0.5224, 0.2824),
        vec2(0.1974, 0.5981),
        vec2(0.2323, 0.4028),
        vec2(0.6057, 0.2963),
        vec2(0.2443, 0.6380),
        vec2(0.2880, 0.6852),
        vec2(0.3349, 0.6407),
    ],
    "resort": [
        vec2(0.6859, 0.2019),
        vec2(0.1724, 0.7111),
        vec2(0.5792, 0.2991),
        vec2(0.2687, 0.6898),
        vec2(0.1766, 0.5278),
        vec2(0.4490, 0.2907),
        vec2(0.3635, 0.7120),
        vec2(0.6266, 0.5194),

    ],
    "skates": [
        vec2(0.3885, 0.6806),
        vec2(0.6208, 0.7602),
        vec2(0.4026, 0.6111),
        vec2(0.5505, 0.7083),
        vec2(0.6745, 0.9056),
        vec2(0.3484, 0.5843),
        vec2(0.5714, 0.7870),
        vec2(0.4365, 0.6509),
        vec2(0.5052, 0.6259),
    ],
    "lotus_island": [
        vec2(0.4693, 0.8287),
        vec2(0.6432, 0.1833),
        vec2(0.4453, 0.7361),
        vec2(0.6661, 0.2694),
        vec2(0.7042, 0.3389),
        vec2(0.5130, 0.7009),
        vec2(0.5578, 0.2972),
        vec2(0.4521, 0.5185),
        vec2(0.3443, 0.6194),
    ],
    "candy_falls": [
        vec2(0.7021, 0.6472),
        vec2(0.1901, 0.3685),
        vec2(0.4094, 0.5648),
        vec2(0.2031, 0.5333),
        vec2(0.1922, 0.1824),
        vec2(0.3255, 0.5759),
        vec2(0.3328, 0.4491),
        vec2(0.5432, 0.6509),
        vec2(0.5271, 0.5593),
    ],
    "winter_park": [
        vec2(0.2224, 0.2435),
        vec2(0.6583, 0.2491),
        vec2(0.4411, 0.4833),
        vec2(0.6635, 0.3843),
        vec2(0.6594, 0.0806),
        vec2(0.3708, 0.5944),
        vec2(0.6510, 0.5546),
        vec2(0.4224, 0.6315),
        vec2(0.3411, 0.6796),
    ],
    "carved": [
        vec2(0.6781, 0.5306),
        vec2(0.2755, 0.5861),
        vec2(0.3411, 0.3778),
        vec2(0.3385, 0.5296),
        vec2(0.1958, 0.4796),
        vec2(0.4448, 0.4417),
        vec2(0.4146, 0.6250),
        vec2(0.4323, 0.8611),
        vec2(0.4328, 0.9333),
    ],
    "park_path": [
        vec2(0.5703, 0.7574),
        vec2(0.4307, 0.3204),
        vec2(0.3932, 0.5537),
        vec2(0.5214, 0.3620),
        vec2(0.5531, 0.2833),
        vec2(0.3880, 0.6917),
        vec2(0.3974, 0.3296),
        vec2(0.3276, 0.7676),
        vec2(0.3063, 0.8269),
    ],
    "frozen_over": [
        vec2(0.2932, 0.6167),
        vec2(0.7198, 0.4574),
        vec2(0.4557, 0.5287),
        vec2(0.6854, 0.5787),
        vec2(0.7375, 0.3019),
        vec2(0.3563, 0.5046),
        vec2(0.6323, 0.5731),
        vec2(0.3708, 0.6806),
        vec2(0.4427, 0.6250),
    ],
    "cubism": [
        vec2(0.3258, 0.5542),
        vec2(0.7176, 0.6500),
        vec2(0.4207, 0.3083),
        vec2(0.6098, 0.5993),
        vec2(0.8281, 0.6431),
        vec2(0.4668, 0.4632),
        vec2(0.6051, 0.6882),
        vec2(0.3988, 0.5361),
        vec2(0.5012, 0.3472),
    ],
    "four_circles": [
        vec2(0.4224, 0.5009),
        vec2(0.4036, 0.7093),
        vec2(0.3625, 0.2435),
        vec2(0.4599, 0.6565),
        vec2(0.2927, 0.7037),
        vec2(0.4557, 0.2843),
        vec2(0.5453, 0.6713),
        vec2(0.5354, 0.5407),
        vec2(0.6578, 0.7537),
    ],
    "end_of_the_road": [
        vec2(0.2510, 0.3352),
        vec2(0.7401, 0.5565),
        vec2(0.5661, 0.5194),
        vec2(0.7146, 0.7111),
        vec2(0.8375, 0.6213),
        vec2(0.4813, 0.4167),
        vec2(0.7281, 0.6398),
        vec2(0.5323, 0.4306),
        vec2(0.5458, 0.5824),
    ],
    "logs": [
        vec2(0.2641, 0.4583),
        vec2(0.5723, 0.6611),
        vec2(0.4008, 0.4451),
        vec2(0.6098, 0.5250),
        vec2(0.6199, 0.6875),
        vec2(0.3266, 0.5201),
        vec2(0.4344, 0.6333),
        vec2(0.3348, 0.6347),
        vec2(0.3691, 0.6889),
        vec2(0.3688, 0.6847),
    ]
}
gld_strt2_pos = {
    "monkey_meadow": [
        vec2(0.3281, 0.4979),
        vec2(0.5977, 0.4500),
        vec2(0.3707, 0.4951),
        vec2(0.4441, 0.6229),
        vec2(0.5133, 0.3236),
        vec2(0.7000, 0.3729),
        vec2(0.5074, 0.5132),
    ],
    "tree_stump": [
        vec2(0.2492, 0.3319),
        vec2(0.6551, 0.6785),
        vec2(0.3711, 0.3854),
        vec2(0.4480, 0.2674),
        vec2(0.5477, 0.6326),
        vec2(0.7684, 0.6521),
        vec2(0.4313, 0.7333),
    ],
    "town_center": [
        vec2(0.2816, 0.2826),
        vec2(0.5461, 0.4840),
        vec2(0.3047, 0.4083),
        vec2(0.2051, 0.4799),
        vec2(0.4496, 0.5681),
        vec2(0.5672, 0.3111),
        vec2(0.4320, 0.5000),
    ],
    "scrapyard": [
        vec2(0.6828, 0.2125),
        vec2(0.2418, 0.1660),
        vec2(0.6965, 0.3410),
        vec2(0.7594, 0.3993),
        vec2(0.3555, 0.2146),
        vec2(0.3133, 0.0451),
        vec2(0.2930, 0.3201),
    ],
    "alpine_run": [
        vec2(0.2824, 0.7556),
        vec2(0.6082, 0.6222),
        vec2(0.3508, 0.7257),
        vec2(0.4004, 0.5611),
        vec2(0.5145, 0.7069),
        vec2(0.7086, 0.6021),
        vec2(0.4773, 0.6354),
    ],
    "hedge": [
        vec2(0.1633, 0.5472),
        vec2(0.7059, 0.5354),
        vec2(0.1656, 0.4889),
        vec2(0.1387, 0.3187),
        vec2(0.6469, 0.6924),
        vec2(0.7918, 0.4181),
        vec2(0.6012, 0.7688),
    ],
}
def gold_strt1(map):
    sauda = monkey(gld_strt1_pos[map][0], "sauda")

    buccaneer = monkey(gld_strt1_pos[map][2], "buccaneer")
    buccaneer.upgrd(upgrade(0, 3, 0))

    ice = monkey(gld_strt1_pos[map][1], "ice")
    ice.upgrd(upgrade(0, 2, 2))

    village1 = monkey(gld_strt1_pos[map][3], "village")
    village1.upgrd(upgrade(0, 2, 0))
    village1.upgrd(upgrade(2, 2, 0))

    alchemist = monkey(gld_strt1_pos[map][4], "alchemist")
    alchemist.upgrd(upgrade(2, 0, 0))

    buccaneer.upgrd(upgrade(2, 4, 0))

    village2 = monkey(gld_strt1_pos[map][5], "village")
    village2.upgrd(upgrade(0, 2, 0))
    village2.upgrd(upgrade(2, 2, 0))

    glue = monkey(gld_strt1_pos[map][6], "glue")
    glue.upgrd(upgrade(2, 2, 0))
    glue.upgrd(upgrade(4, 2, 0))

    wizard = monkey(gld_strt1_pos[map][7], "wizard")
    wizard.upgrd(upgrade(0, 2, 4))
    wizard.set_option(gld_strt1_pos[map][8])
    wizard.upgrd(upgrade(0, 2, 5))
def gold_strt2(map):
    sauda = monkey(gld_strt2_pos[map][0], "sauda")

    ice = monkey(gld_strt2_pos[map][1], "ice")
    ice.upgrd(upgrade(0, 2, 2))

    ninja = monkey(gld_strt2_pos[map][2], "ninja")
    ninja.upgrd(upgrade(2, 0, 1))

    alchemist1 = monkey(gld_strt2_pos[map][3], "alchemist") #ninja
    alchemist1.upgrd(upgrade(2, 0, 0))

    village1 = monkey(gld_strt1_pos[map][3], "village") #ice
    village1.upgrd(upgrade(0, 2, 0))
    village1.upgrd(upgrade(2, 2, 0))

    alchemist2 = monkey(gld_strt2_pos[map][4], "alchemist") #ice
    alchemist2.upgrd(upgrade(2, 0, 0))

    ninja.upgrd(upgrade(4, 0, 2))
    alchemist1.upgrd(upgrade(4, 2, 0))

    glue = monkey(gld_strt2_pos[map][5], "glue")
    glue.upgrd(upgrade(2, 2, 0))
    glue.upgrd(upgrade(4, 2, 0))

    ninja.upgrd(upgrade(5, 0, 2))
def gold_getter():
    map = gold_bln_map()

    print("found on map:", map)

    # difficulty_select("hard_standard")

    # play(2)

    # if map in gld_strt1_pos:
    #     gold_strt1(map)
    # else:
    #     gold_strt2(map)
    
    # game_done_wait()

def script():
    difficulty(2)
    #sapper_farm()

    gold_getter()
