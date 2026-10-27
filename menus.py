import pyautogui
import time
import mss

from myvar import vec2
from data import binds

screen = None
animation_time = 0.1
_sct = mss.mss()

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

map_load_points = [
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

def is_black(rgb, threshold = 15):
    return max(rgb[:3]) <= threshold
def points_state(points):
    return  [is_black(get_pixel(screen.to_px(p))) for p in points]
def wait_for_map_load(timeout=240, poll=0.2, stable_polls=5, wait_for_black=False):
    start = time.time()

    while time.time() - start < timeout:
        if all(points_state(map_load_points)):
            break
        time.sleep(poll)

    stable = 0
    while time.time() - start < timeout:
        if not any(points_state(map_load_points)):
            stable += 1
            if stable >= stable_polls:
                return True
        else:
            stable = max(stable-1, 0)
        time.sleep(poll)

    return False




def game_to_main():
    pyautogui.press(binds["pause"])
    click(game_pause_home, 3)

def difficulty_select(diff):
    keys_list = list(difficulties.keys())
    index = keys_list.index(diff)

    main_diff = None
    if index <= 4:
        main_diff = "easy"
    elif index >= 5 and index <= 10:
        main_diff = "medium"
    elif index >= 11:
        main_diff = "hard"

    click(difficulties[main_diff])
    click(difficulties[diff])

    if not wait_for_map_load():
        raise TimeoutError("map did not load")

def map_select(name):
    if name not in maps:
        raise ValueError("map name nod found")

    #at the begining check if there is the play button bellow, if yes, press it

    click(search_btn)
    click(search_area)

    name = name.replace("_", " ")
    pyautogui.write(name, interval=0.05)

    click(map_pos)


