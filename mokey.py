import pyautogui
import time


from myvar import vec2, upgrade
from screenspace import Screen
from cash import get_cash
from data import towers, tower_price_c, tower_price_e, tower_price_h, tower_price_i, tower_price_n, heroes_price_e, heroes_price_h, heroes_price_i, heroes_price_n, binds, targets, normal, targets_elite_s, normal_unless_upgrd, targets_spike, adds_button

screen:Screen = None
tower_prices = None
hero_price = None

#screen_half = 0.4351562 #for this vale and less the upgrades show on right

#ability has no check if its aviable
#ability targeting
#hero 

#usable: __init__, upgrd, ability, retargeting*, del

elite_sniper:bool = 0

def init(hero, _screen, diff = 0):
    global screen, tower_prices, hero_price

    screen = _screen
    match diff:
        case 0:
            tower_prices = tower_price_e
            hero_price = heroes_price_e[hero]
        case 1:
            tower_prices = tower_price_n
            hero_price = heroes_price_n[hero]
        case 2:
            tower_prices = tower_price_h
            hero_price = heroes_price_h[hero]
        case 3:
            tower_prices = tower_price_i
            hero_price = heroes_price_i[hero]
        case 4:
            tower_prices = tower_price_c
            hero_price = heroes_price_c[hero]

def cash_wait(money):
    mon = get_cash()
    while mon < money:
        time.sleep(1/10)
        print("waiting for cash:", mon, "/", money)
        mon = get_cash()
    print("waiting for cash:", mon, "/", money)


class monkey:
    mouse_move_time = 0.1
    upgrades_open:bool = False

    type = ""
    position = vec2()
    upgrades = upgrade(0, 0, 0)
    target_i = 0
    option:bool = 0

    def __init__(self, _position, _type):
        self.position = _position
        self.type = _type

        cash_wait(tower_prices[_type])
        
        pyautogui.press(towers[_type])
        self.click(True)

    def click(self, initial:bool = False):
        px_pos = screen.to_px(self.position)
        pyautogui.moveTo(px_pos.x, px_pos.y, self.mouse_move_time)
        pyautogui.click()
        if not initial:
            self.upgrades_open = not self.upgrades_open
        time.sleep(self.mouse_move_time*2)

    def open_upgrd(self):
        if not self.upgrades_open:
            self.click()
            self.upgrades_open = True

    def close_upgrd(self):
        if self.upgrades_open:
            self.click()
            self.upgrades_open = False

    def path_upgrd(self, path, level):
        if level:
            print("upgrading path:", path, ",to level:", level)

        upgrad:int = 0
        path_name:str = ""
        match path:
            case 0:
                upgrad = self.upgrades.a
                path_name = "top"
            case 1:
                upgrad = self.upgrades.b
                path_name = "mid"
            case 2:
                upgrad = self.upgrades.c
                path_name = "bot"

        if level < upgrad:
            print("wrong upgrade path")
            return

        for i in range(upgrad, level):
            cash_wait(tower_prices[self.type+"_u"][path][upgrad])
        
            self.open_upgrd()
            pyautogui.press(binds[path_name])
            self.close_upgrd()

            match path:
                case 0:
                    self.upgrades.a += 1
                case 1:
                    self.upgrades.b += 1
                case 2:
                    self.upgrades.c += 1
            upgrad += 1
            
    def upgrd(self, paths:upgrade):
        if not paths.is_valid():
            print("wrong upgrade path")
            return

        if self.type == "hero":
            print("yea i didnt add that")
            return

        self.path_upgrd(0, paths.a)
        self.path_upgrd(1, paths.b)
        self.path_upgrd(2, paths.c)
        
        global_upgrades(self, self.type, paths)

        print("upgraded to: "+str(self.upgrades.a)+"-"+str(self.upgrades.b)+"-"+str(self.upgrades.c))

    def ability(self, num:int):
        if num < 0 or num > 3:
            print("wrong ability")
            return
        self.open_upgrd()
        pyautogui.press(binds["t_ab_"+str(num)])
        self.close_upgrd()

    def norm_target_change(self):
        time.sleep(self.mouse_move_time)
        pyautogui.press(binds["target"])
        if self.type == "sniper" and elite_sniper:
            self.target_i = (self.target_i+1)%len(targets_elite_s)
        else:
            self.target_i = (self.target_i+1)%len(targets)
        #print("targeting changed to", targets[target_i])
    
    def norm_target(self, target):
        self.open_upgrd()
        trys = 0
        for i in range (len(targets)+1):
            self.norm_target_change()
            if target == targets[self.target_i]:
                break
            trys += 1
        self.close_upgrd()
        if trys == len(targets)+1:
            print("targeting not found")
            return

    def elite_target(self, target):
            self.open_upgrd()
            trys = 0
            for i in range (len(targets_elite_s)+1):
                self.norm_target_change()
                if target == targets_elite_s[self.target_i]:
                    break
                trys += 1
            self.close_upgrd()
            if trys == len(targets_elite_s)+1:
                print("targeting not found")
                return

    def spike_target(self, target):
                self.open_upgrd()
                trys = 0
                for i in range (len(targets_spike)+1):
                    self.norm_target_change()
                    if target == targets_spike[self.target_i]:
                        break
                    trys += 1
                self.close_upgrd()
                if trys == len(targets_spike)+1:
                    print("targeting not found")
                    return

    def retargeting(self, target):
        if self.type in normal:
            if self.type == "sniper" and elite_sniper:
                pass
            else:
                self.norm_target(target)
        elif self.type in normal_unless_upgrd:
            if self.type == "tack" and self.upgrades.a >= 5:
                self.norm_target(target)
            elif self.type == "ice" and self.upgrades.c >= 3:
                self.norm_target(target)
            elif self.type == "village" and self.upgrades.a >= 5:
                self.norm_target(target)
        else:
            print("this monkey doesnt have targeting")

    def set_option(self):
        if self.type in adds_button:
            if self.type == "boomerang":
                self.open_upgrd()
                pyautogui.press(binds["opt1"])
                self.close_upgrd()

    def dele(self):
        print("deleting", self.type)

        self.open_upgrd()
        
        pyautogui.press(binds["del"])


def global_upgrades(monkey:monkey, monkey_name, upgrad:upgrade):
    global elite_sniper

    if monkey_name == "snipier" and upgrad.b >= 5:
        elite_sniper = 1
        monkey.target_i = 4