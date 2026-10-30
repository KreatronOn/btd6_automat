import pyautogui
import time
import mss
import math

from myvar import vec2
from data import binds
from mokey import difficulty, farming

screen = None
animation_time = 0.1
_sct = mss.mss()
play_state = 0

game_pause_home = vec2(0.4516, 0.7676)

difficulties = {
    "easy": vec2(0.3307, 0.4102),
    "easy_standard": vec2(0.3349, 0.5472),
    "easy_sandbox": vec2(0.4906, 0.6722),
    "primary_only": vec2(0.5073, 0.4213),
    "deflation": vec2(0.6823, 0.4398),
    "medium": vec2(0.4974, 0.3963),
    "medium_standard": vec2(0.3359, 0.5546),
    "medium_sandbox": vec2(0.6693, 0.6778),
    "reverse": vec2(0.5135, 0.6880),
    "military_only": vec2(0.4911, 0.4537),
    "apopalypse": vec2(0.6687, 0.4324),
    "hard": vec2(0.6786, 0.3722),
    "hard_standard": vec2(0.3505, 0.5241),
    "hard_sandbox": vec2(0.1469, 0.5528),
    "alternate_bloons_rounds": vec2(0.4964, 0.7065),
    "impoppable": vec2(0.6698, 0.7019),
    "chimps": vec2(0.8380, 0.6870),
    "magic_only": vec2(0.4880, 0.4259),
    "double_hp_moabs": vec2(0.6698, 0.4333),
    "half_cash": vec2(0.8250, 0.4056),
} #easy: -4, medium: 5-10, hard 11+
difficulty_select_check = {
    vec2(0.3328, 0.3491): (173, 91, 36),
    vec2(0.3089, 0.3167): (110, 221, 229),
    vec2(0.3333, 0.4093): (255, 105, 239),
    vec2(0.5036, 0.3278): (139, 201, 37),
    vec2(0.5010, 0.3120): (254, 230, 0),
    vec2(0.4911, 0.3815): (255, 255, 255),
    vec2(0.5099, 0.4009): (232, 150, 53),
    vec2(0.4672, 0.3861): (89, 167, 11),
    vec2(0.6849, 0.3389): (68, 73, 90),
    vec2(0.6469, 0.3083): (255, 0, 0),
    vec2(0.6734, 0.3741): (255, 0, 0),
    vec2(0.6693, 0.4370): (53, 58, 75),
    vec2(0.6849, 0.3861): (193, 203, 211),
    vec2(0.3615, 0.3870): (109, 220, 229),
    vec2(0.3432, 0.4111): (208, 244, 249),
    vec2(0.0292, 0.0713): (0, 198, 255),
    vec2(0.0349, 0.0481): (255, 255, 255),
    vec2(0.0484, 0.0278): (0, 221, 255),
}
easy_select_check = {
    vec2(0.3260, 0.5398): (255, 255, 255),
    vec2(0.3500, 0.5157): (0, 222, 234),
    vec2(0.3589, 0.4852): (205, 171, 121),
    vec2(0.3651, 0.5907): (203, 145, 32),
    vec2(0.2958, 0.5481): (0, 158, 191),
    vec2(0.0292, 0.0713): (0, 198, 255),
    vec2(0.0339, 0.0407): (255, 255, 255),
    vec2(0.0474, 0.0315): (0, 221, 255),
    vec2(0.3349, 0.0204): (187, 142, 87),
    vec2(0.3536, 0.0204): (128, 74, 36),
    vec2(0.4719, 0.0389): (255, 255, 255),
    vec2(0.6099, 0.0324): (128, 74, 36),
}
medium_select_check = {
    vec2(0.3250, 0.5417): (255, 255, 255),
    vec2(0.3510, 0.5213): (0, 224, 236),
    vec2(0.3594, 0.5065): (0, 145, 182),
    vec2(0.3667, 0.5000): (204, 169, 117),
    vec2(0.3661, 0.5880): (200, 143, 36),
    vec2(0.0292, 0.0676): (0, 201, 255),
    vec2(0.0344, 0.0481): (255, 255, 255),
    vec2(0.0474, 0.0278): (0, 221, 255),
    vec2(0.3323, 0.0213): (187, 143, 87),
    vec2(0.3464, 0.0222): (128, 74, 36),
    vec2(0.6302, 0.0389): (128, 74, 36),
    vec2(0.6656, 0.0185): (187, 143, 88),
    vec2(0.4896, 0.0444): (255, 255, 255),
}
hard_select_check = {
    vec2(0.3318, 0.5472): (255, 255, 255),
    vec2(0.3531, 0.5167): (0, 217, 231),
    vec2(0.3370, 0.4833): (0, 138, 178),
    vec2(0.3531, 0.4806): (205, 172, 124),
    vec2(0.3630, 0.5963): (209, 151, 28),
    vec2(0.0271, 0.0741): (0, 196, 255),
    vec2(0.0344, 0.0491): (255, 255, 255),
    vec2(0.0495, 0.0278): (0, 221, 255),
    vec2(0.3339, 0.0185): (187, 143, 88),
    vec2(0.3474, 0.0213): (128, 74, 36),
    vec2(0.4677, 0.0398): (255, 255, 255),
    vec2(0.5526, 0.0398): (128, 74, 36),
    vec2(0.6656, 0.0259): (185, 140, 85),
}

map_load_popup_check = {
    vec2(0.2958, 0.7315): (78, 132, 209),
    vec2(0.3448, 0.6787): (85, 138, 212),
    vec2(0.3698, 0.7333): (78, 132, 208),
    vec2(0.4073, 0.6694): (86, 139, 212),
    vec2(0.5693, 0.7231): (80, 133, 209),
    vec2(0.6104, 0.6352): (87, 141, 212),
    vec2(0.6385, 0.7093): (82, 135, 210),
    vec2(0.6958, 0.6509): (87, 140, 211),
    vec2(0.7198, 0.7315): (78, 132, 209),
    vec2(0.7214, 0.3528): (103, 156, 218),
    vec2(0.6839, 0.3917): (101, 153, 217),
    vec2(0.6745, 0.3583): (102, 155, 217),
    vec2(0.2604, 0.4056): (100, 153, 217),
    vec2(0.2984, 0.3500): (104, 156, 218),
    vec2(0.3281, 0.4120): (100, 152, 217),
    vec2(0.3703, 0.3250): (246, 114, 37),
    vec2(0.4870, 0.3880): (240, 60, 11),
    vec2(0.6208, 0.3565): (242, 77, 18),
    vec2(0.6490, 0.3065): (220, 35, 0),
    vec2(0.3521, 0.3093): (220, 35, 0),
}
map_popup_ok = vec2(0.4969, 0.6981)

maps = [
    # beginner
    "monkey_meadow", "in_the_loop", "skull_tweak", "three_mines_'round", "spa_pits",
    "tinkerton", "tree_stump", "town_center", "middle_of_the_road", "one_two_tree",
    "scrapyard", "the_cabin", "resort", "skates", "lotus_island", "candy_falls",
    "winter_park", "carved", "park_path", "alpine_run", "frozen_over", "cubism",
    "four_circles", "hedge", "end_of_the_road", "logs",

    # intermediate
    "lost_crevasse", "luminous_cove", "ancient_portal", "sulfur_springs", "water_park",
    "polyphemus", "covered_garden", "quarry", "quiet_street", "bloonarius_prime",
    "balance", "encrypted", "bazaar", "adora's_temple", "spring_spring", "kartsndarts",
    "moon_landing", "haunted", "downstream", "firing_range", "cracked", "streambed",
    "chutes", "rake", "spice_islands",

    # advanced
    "ship_capture", "ascent", "mushroom_grotto", "party_parade", "sunset_gulch",
    "enchanted_glade", "last_resort", "castle_revenge", "dark_path", "erosion",
    "midnight_mansion", "sunken_columns", "x_factor", "mesa", "geared", "spillway",
    "cargo", "pat's_pond", "peninsula", "high_finance", "another_brick",
    "off_the_coast", "cornfield", "underground",

    # expert
    "tricky_tracks", "glacial_trail", "dark_dungeons", "sanctuary", "ravine",
    "flooded_valley", "infernal", "bloody_puddles", "workshop", "quad",
    "dark_castle", "muddy_puddles", "ouch",
]
search_btn = vec2(0.0417, 0.1528)
search_area = vec2(0.5000, 0.0481)
map_pos = vec2(0.2786, 0.3019)
map_select_check = {
    vec2(0.0521, 0.1463): (0, 210, 255),
    vec2(0.0453, 0.1454): (254, 255, 255),
    vec2(0.0365, 0.1722): (0, 198, 255),
    vec2(0.0510, 0.0306): (0, 221, 255),
    vec2(0.0370, 0.0454): (255, 255, 255),
    vec2(0.0312, 0.0676): (0, 201, 255),
    vec2(0.9615, 0.0269): (0, 221, 255),
    vec2(0.9625, 0.0491): (255, 255, 255),
    vec2(0.9505, 0.0713): (0, 198, 255),
    vec2(0.6870, 0.8685): (255, 184, 0),
    vec2(0.5615, 0.9148): (255, 197, 0),
    vec2(0.4333, 0.8833): (255, 200, 0),
    vec2(0.2984, 0.8981): (255, 200, 0),
    vec2(0.3214, 0.8833): (0, 216, 230),
    vec2(0.4229, 0.9343): (0, 217, 230),
    vec2(0.5521, 0.8704): (0, 224, 235),
    vec2(0.7094, 0.8843): (255, 52, 0),
}
map_1 = vec2(0.2729, 0.2500)
map_2 = vec2(0.4969, 0.2500)
map_3 = vec2(0.7214, 0.2500)
map_4 = vec2(0.2719, 0.5389)
map_5 = vec2(0.4953, 0.5417)
map_6 = vec2(0.7047, 0.5361)

loading_screen_check = [
    vec2(0.0042, 0.0481),
    vec2(0.0068, 0.3463),
    vec2(0.0042, 0.8370),
    vec2(0.0031, 0.5352),
    vec2(0.0526, 0.0315),
    vec2(0.9031, 0.0259),
    vec2(0.9927, 0.1593),
    vec2(0.9901, 0.9333),
    vec2(0.9922, 0.5537),
    vec2(0.8354, 0.0463),
    vec2(0.1635, 0.0306),
]

main_menu_check = {
    vec2(0.4797, 0.8315): (16, 207, 0),
    vec2(0.5177, 0.8398): (63, 227, 0),
    vec2(0.4948, 0.8769): (255, 255, 255),
    vec2(0.4807, 0.8991): (90, 229, 0),
    vec2(0.3990, 0.8407): (97, 112, 132),
    vec2(0.3635, 0.8287): (71, 69, 78),
    vec2(0.3677, 0.9130): (0, 236, 254),
    vec2(0.4026, 0.9019): (0, 234, 253),
    vec2(0.8219, 0.8880): (255, 184, 1),
    vec2(0.8292, 0.8361): (144, 90, 210),
    vec2(0.8427, 0.9037): (164, 106, 214),
    vec2(0.9667, 0.0657): (255, 198, 0),
    vec2(0.9740, 0.0463): (255, 255, 255),
    vec2(0.9786, 0.0407): (254, 220, 0),
    vec2(0.5042, 0.9167): (87, 230, 0),
}
play_btn = vec2(0.5000, 0.8713)

victory_check = {
    vec2(0.4198, 0.3907): (255, 231, 0),
    vec2(0.5854, 0.3815): (255, 231, 0),
    vec2(0.5870, 0.4120): (224, 40, 0),
    vec2(0.4130, 0.4120): (224, 40, 0),
    vec2(0.3823, 0.1417): (255, 238, 0),
    vec2(0.3937, 0.1833): (255, 228, 0),
    vec2(0.4219, 0.1407): (255, 235, 0),
    vec2(0.4240, 0.1759): (255, 224, 0),
    vec2(0.4516, 0.1278): (255, 216, 0),
    vec2(0.4526, 0.1861): (255, 231, 0),
    vec2(0.4813, 0.1259): (255, 214, 0),
    vec2(0.4854, 0.1769): (255, 225, 0),
    vec2(0.5250, 0.1343): (255, 228, 0),
    vec2(0.5260, 0.1824): (255, 231, 0),
    vec2(0.5682, 0.1269): (255, 218, 0),
    vec2(0.5557, 0.1769): (255, 227, 0),
    vec2(0.6010, 0.1463): (255, 243, 0),
    vec2(0.6021, 0.1778): (255, 227, 0),
    vec2(0.5464, 0.8333): (107, 230, 0),
    vec2(0.5214, 0.8333): (255, 255, 255),
    vec2(0.4464, 0.8556): (28, 145, 0),
    vec2(0.5776, 0.7685): (44, 204, 0),
    vec2(0.5870, 0.7361): (53, 210, 0),
    vec2(0.5885, 0.7000): (82, 134, 210),
    vec2(0.4151, 0.6139): (85, 139, 211),
}
game_done_check = {
    vec2(0.3828, 0.3963): (255, 239, 0),
    vec2(0.3885, 0.4343): (255, 227, 0),
    vec2(0.4240, 0.4083): (255, 251, 0),
    vec2(0.4245, 0.4315): (255, 227, 0),
    vec2(0.4453, 0.3944): (255, 235, 0),
    vec2(0.4495, 0.4370): (255, 228, 0),
    vec2(0.4839, 0.3944): (255, 235, 0),
    vec2(0.4844, 0.4370): (255, 228, 0),
    vec2(0.5266, 0.3880): (255, 228, 0),
    vec2(0.5271, 0.4435): (255, 235, 0),
    vec2(0.5599, 0.3954): (255, 239, 0),
    vec2(0.5583, 0.4259): (255, 223, 0),
    vec2(0.5969, 0.3954): (255, 235, 0),
    vec2(0.6062, 0.4407): (255, 231, 0),
    vec2(0.7042, 0.4361): (100, 151, 216),
    vec2(0.7068, 0.7972): (79, 133, 210),
    vec2(0.2901, 0.8028): (77, 131, 209),
    vec2(0.2958, 0.4259): (102, 153, 217),
    vec2(0.3932, 0.7491): (0, 221, 255),
    vec2(0.3734, 0.7731): (255, 255, 255),
    vec2(0.3563, 0.8157): (0, 197, 255),
    vec2(0.4807, 0.8194): (0, 196, 255),
    vec2(0.5078, 0.7972): (255, 255, 255),
    vec2(0.5141, 0.7500): (0, 221, 255),
    vec2(0.6130, 0.8194): (58, 214, 0),
    vec2(0.6167, 0.7833): (255, 255, 255),
    vec2(0.6448, 0.7500): (113, 232, 0),
}
game_over_check = {
    vec2(0.3458, 0.7176): (0, 221, 255),
    vec2(0.3281, 0.7398): (255, 255, 255),
    vec2(0.3073, 0.7778): (0, 197, 255),
    vec2(0.4589, 0.7148): (255, 221, 0),
    vec2(0.4297, 0.7389): (255, 255, 255),
    vec2(0.4229, 0.7602): (255, 207, 0),
    vec2(0.5427, 0.7796): (0, 196, 255),
    vec2(0.5536, 0.7426): (0, 216, 255),
    vec2(0.5714, 0.7148): (0, 221, 255),
    vec2(0.3156, 0.3343): (99, 151, 216),
    vec2(0.6906, 0.3250): (100, 152, 217),
    vec2(0.7036, 0.6759): (82, 135, 210),
    vec2(0.2974, 0.6685): (83, 136, 211),
    vec2(0.3932, 0.2880): (255, 84, 0),
    vec2(0.4458, 0.2861): (255, 85, 0),
    vec2(0.4807, 0.2824): (255, 89, 0),
    vec2(0.5208, 0.2806): (255, 90, 0),
    vec2(0.5589, 0.2926): (255, 79, 0),
    vec2(0.5974, 0.2833): (255, 89, 0),
    vec2(0.5979, 0.3352): (255, 39, 0),
    vec2(0.5490, 0.3343): (255, 39, 0),
    vec2(0.5146, 0.3407): (255, 35, 0),
    vec2(0.4771, 0.3398): (255, 34, 0),
    vec2(0.4437, 0.3361): (255, 39, 0),
    vec2(0.3891, 0.3389): (255, 36, 0),
}
game_over_chimp_check = {
    vec2(0.3031, 0.7250): (79, 133, 209),
    vec2(0.2969, 0.3139): (102, 154, 217),
    vec2(0.7026, 0.3176): (102, 153, 217),
    vec2(0.7005, 0.7204): (80, 133, 210),
    vec2(0.6318, 0.7083): (0, 221, 255),
    vec2(0.6224, 0.7546): (255, 255, 255),
    vec2(0.6089, 0.7407): (0, 217, 255),
    vec2(0.6026, 0.7787): (0, 197, 255),
    vec2(0.5219, 0.7815): (255, 196, 0),
    vec2(0.5099, 0.7713): (255, 255, 255),
    vec2(0.4865, 0.7343): (255, 255, 255),
    vec2(0.3995, 0.7157): (0, 221, 255),
    vec2(0.3870, 0.7407): (255, 255, 255),
    vec2(0.3641, 0.7815): (0, 196, 255),
    vec2(0.4016, 0.2861): (255, 86, 0),
    vec2(0.4474, 0.2796): (255, 91, 0),
    vec2(0.4760, 0.2833): (255, 88, 0),
    vec2(0.5151, 0.2843): (255, 87, 0),
    vec2(0.5536, 0.2861): (255, 85, 0),
    vec2(0.5938, 0.2833): (255, 89, 0),
    vec2(0.7026, 0.5102): (91, 143, 214),
    vec2(0.5042, 0.5139): (91, 143, 213),
    vec2(0.2922, 0.5139): (91, 143, 213),
}
gm_over_check = {
    vec2(0.3495, 0.1935): (255, 47, 0),
    vec2(0.4156, 0.1880): (255, 51, 0),
    vec2(0.4703, 0.1861): (255, 55, 0),
    vec2(0.5255, 0.1935): (255, 48, 0),
    vec2(0.5734, 0.1796): (255, 60, 0),
    vec2(0.6115, 0.1778): (255, 62, 0),
    vec2(0.6516, 0.1778): (255, 61, 0),
    vec2(0.5844, 0.7806): (43, 202, 0),
    vec2(0.5865, 0.7481): (52, 210, 0),
    vec2(0.5891, 0.4630): (217, 31, 0),
    vec2(0.5906, 0.4167): (224, 41, 0),
    vec2(0.4130, 0.4176): (224, 41, 0),
    vec2(0.4141, 0.4509): (218, 33, 0),
    vec2(0.5375, 0.8472): (94, 225, 0),
    vec2(0.5193, 0.8407): (255, 255, 255),
    vec2(0.4635, 0.8389): (107, 230, 0),
    vec2(0.4755, 0.8380): (255, 255, 255),
    vec2(0.4953, 0.8102): (34, 158, 0),
}
insta_monkey_check = {
    vec2(0.1203, 0.6407): (20, 15, 40),
    vec2(0.3781, 0.8843): (19, 14, 38),
    vec2(0.8969, 0.3472): (17, 13, 34),
    vec2(0.2448, 0.3370): (42, 31, 83),
    vec2(0.8161, 0.4361): (31, 23, 61),
    vec2(0.4505, 0.2380): (144, 123, 0),
    vec2(0.4193, 0.2463): (255, 217, 0),
    vec2(0.4182, 0.2454): (255, 217, 0),
    vec2(0.4510, 0.2370): (255, 217, 0),
    vec2(0.4708, 0.2407): (255, 217, 0),
    vec2(0.4917, 0.2417): (193, 164, 0),
    vec2(0.5172, 0.2417): (255, 217, 0),
    vec2(0.5229, 0.2417): (255, 217, 0),
    vec2(0.5229, 0.2417): (255, 217, 0),
    vec2(0.7927, 0.8519): (17, 13, 34),
    vec2(0.5266, 0.9991): (0, 0, 0),
    vec2(0.5260, 0.9991): (0, 0, 0),
}
collection_event_check = {
    vec2(0.1000, 0.3444): (97, 72, 111),
    vec2(0.3099, 0.2157): (104, 73, 122),
    vec2(0.9328, 0.8000): (75, 53, 88),
    vec2(0.6995, 0.7093): (112, 78, 132),
    vec2(0.4833, 0.4157): (175, 69, 14),
    vec2(0.4672, 0.6444): (12, 74, 0),
    vec2(0.4531, 0.6343): (88, 223, 0),
    vec2(0.4865, 0.6333): (255, 255, 255),
    vec2(0.5453, 0.6352): (86, 222, 0),
    vec2(0.2526, 0.4389): (235, 173, 99),
    vec2(0.2505, 0.5333): (237, 180, 93),
    vec2(0.3740, 0.0574): (145, 46, 202),
    vec2(0.6229, 0.0676): (142, 43, 199),
    vec2(0.6458, 0.0602): (255, 211, 22),
    vec2(0.6583, 0.0278): (159, 49, 210),
    vec2(0.3422, 0.0861): (246, 86, 0),
    vec2(0.3490, 0.0315): (0, 120, 161),
    vec2(0.5833, 0.5944): (137, 96, 162),
    vec2(0.5849, 0.5963): (137, 96, 161),
}
next_btn = vec2(0.4984, 0.8370)
button1_4 = vec2(0.3260, 0.7519)
button2_4 = vec2(0.4396, 0.7509)
button3_4 = vec2(0.5552, 0.7472)
button4_4 = vec2(0.6750, 0.7500)
button1_3 = vec2(0.3844, 0.7537)
button2_3 = vec2(0.5000, 0.7537)
button3_3 = vec2(0.6141, 0.7537)


def init(scrn):
    global screen
    screen = scrn

def click(pos, time_mult = 1):
    px_pos = screen.to_px(pos)
    pyautogui.moveTo(px_pos.x, px_pos.y, animation_time * time_mult)
    pyautogui.click()
    time.sleep(animation_time)

def get_pixel(p):
    shot = _sct.grab({"left": int(p.x), "top": int(p.y), "width": 1, "height": 1})
    return shot.pixel(0, 0)

def color_distance(c1, c2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(c1[:3], c2[:3])))
def points_check(points, threshold = 10, tolerance = 0.3):
    correct = True
    wrong = 0
    for pos, col in points.items():
        if color_distance(get_pixel(screen.to_px(pos)), col) >= threshold:
            wrong += 1
    return wrong < tolerance * len(points)
    
def is_black(rgb, threshold = 15):
    return max(rgb[:3]) <= threshold
def points_state(points):
    return  [is_black(get_pixel(screen.to_px(p))) for p in points]
def wait_for_map_load(timeout=240, poll=0.2, stable_polls=5):
    start = time.time()

    print("awaiting black screen")
    while time.time() - start < timeout:
        if all(points_state(loading_screen_check)):
            break
        time.sleep(poll)
    print("black screen")

    print("awaiting map")
    stable = 0
    while time.time() - start < timeout:
        if not any(points_state(loading_screen_check)):
            stable += 1
            if stable >= stable_polls:
                return True
        else:
            stable = max(stable-1, 0)
        time.sleep(poll)

    return False

def wait_for_map_select(timeout=240, poll=0.2):
    start = time.time()

    while time.time() - start < timeout:
        if points_check(map_select_check):
            break
        time.sleep(poll)

def wait_for_difficulty_select(timeout=240, poll=0.2):
    start = time.time()

    while time.time() - start < timeout:
        if points_check(difficulty_select_check):
            break
        time.sleep(poll)
def wait_for_difficulty(diff, timeout=240, poll=0.2):
    check = None
    match diff:
        case "easy":
            check = easy_select_check
        case "medium":
            check = medium_select_check
        case "hard":
            check = hard_select_check
    
    start = time.time()

    while time.time() - start < timeout:
        if points_check(check):
            break
        time.sleep(poll)

def popup():
    time.sleep(0.2)
    if points_check(map_load_popup_check):
        click(map_popup_ok)
        time.sleep(0.2)
        click(map_popup_ok)
        time.sleep(0.2)
        click(map_popup_ok)
    time.sleep(0.2)

def freeplay():
    global play_state
    play_state_before = play_state
    play_state = 1
    time.sleep(1)
    click(button3_3)
    time.sleep(1)
    popup()
    time.sleep(2)
    play(play_state_before)
    time.sleep(1)




def game_to_main():
    print("going to main menu")
    pyautogui.press(binds["pause"])
    click(game_pause_home, 3)

def difficulty_select(diff):
    if diff in difficulties:
        print("setting difficulty:", diff)
    else:
        raise ValueError("difficulty", diff, "doesnt exist")
        
    wait_for_difficulty_select()

    keys_list = list(difficulties.keys())
    index = keys_list.index(diff)

    main_diff = None
    if index <= 4:
        main_diff = "easy"
        difficulty(0)
    elif index >= 5 and index <= 10:
        main_diff = "medium"
        difficulty(1)
    elif index >= 11:
        main_diff = "hard"

    if index == 15:
        difficulty(3)
    elif index == 16:
        difficulty(4)
    elif index >= 11:
        difficulty(2)


    click(difficulties[main_diff])

    wait_for_difficulty(main_diff)

    click(difficulties[diff])

    if not wait_for_map_load():
        raise TimeoutError("map did not load")

    popup()
    popup()

def map_select(name):
    if name not in maps:
        raise ValueError("map name:", name, ",not found")
    else:
        print("selecting map:", name)

    if points_check(main_menu_check):
        click(play_btn)
        wait_for_map_select()

    click(search_btn)
    click(search_area)

    name = name.replace("_", " ")
    pyautogui.write(name, interval=0.05)

    click(map_pos)

def gold_bln_map(diff = 0):
    print("selcting map with golden bloon on difficulty:", diff)

    map_pos = None
    match diff:
        case 0:
            map_pos = map_1
        case 1:
            map_pos = map_2
        case 3:
            map_pos = map_3
        case 4:
            map_pos = map_4

    if points_check(main_menu_check):
        click(play_btn)
        wait_for_map_select()

    click(search_btn)
    click(search_area)

    pyautogui.write("/GoldenBloons", interval=0.05)

    click(map_pos)

def monkey_team_map(diff = 0):
    print("selcting map with monkey teams on difficulty:", diff)

    map_pos = None
    match diff:
        case 0:
            map_pos = map_1
        case 1:
            map_pos = map_2
        case 3:
            map_pos = map_3
        case 4:
            map_pos = map_4

    if points_check(main_menu_check):
        click(play_btn)
        wait_for_map_select()

    click(search_btn)
    click(search_area)

    pyautogui.write("/MonkeyTeams", interval=0.05)

    click(map_pos)

def play(opt = -1):
    if opt >= -1 and opt <= 2:
        print("setting play speed to:", opt, "| ", end="")
    else:
        print("speed", opt, "doesnt exist")
        return

    global play_state

    if opt == -1:
        pyautogui.press(binds["play"])
        play_state = (play_state%2)+1
        print(play_state, ",", end="")
        return

    if play_state == opt or opt == 0:
        return
    for i in range(2):
        pyautogui.press(binds["play"])
        play_state = (play_state%2)+1
        print(play_state, ",", end="")
        time.sleep(0.1)
        if play_state == opt:
            break
    print()

def game_done_wait(home = True, timeout=99999, poll=1):
    print("waiting for end, going to home:", home)

    start = time.time()

    summary_screen = False
    win = True

    while time.time() - start < timeout:
        if points_check(victory_check):
            summary_screen = True
            click(next_btn)
            break
        elif points_check(gm_over_check):
            summary_screen = True
            win = False
            click(next_btn)
            break
        elif points_check(game_over_chimp_check) or points_check(game_over_check):
            win = False
            break
        farming()
        time.sleep(poll)


    while time.time() - start < timeout and summary_screen:
        if points_check(game_done_check) or points_check(game_over_chimp_check) or points_check(game_over_check):
            break
        time.sleep(poll)

    if home:
        if win:
            click(button1_3)
        else:
            click(button1_4)
    else:
        freeplay()

def insta_monkey_wait(timeout=99999, poll=1):
    print("waiting for insta monkey")

    start = time.time()

    while time.time() - start < timeout:
        if points_check(insta_monkey_check):
            break
        farming()
        time.sleep(poll)

    click(vec2(0.5, 0.5))
    time.sleep(1)