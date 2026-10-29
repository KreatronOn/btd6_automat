import pyautogui
import time


from myvar import vec2, upgrade
from screenspace import Screen
from cash import get_cash
from data import \
binds, towers,\
tower_price_c, tower_price_e, tower_price_h, tower_price_i, tower_price_n,\
heroes_price_e, heroes_price_h, heroes_price_i, heroes_price_n, heroes_price_c,\
normal, normal_unless_upgrd, adds_button, way_different, change_targeting,\
targets, targets_elite_s, targets_spike, targets_heli, targets_heli_p, targets_ace, targets_ace_c, targets_dartling, targets_dartling_i,\
can_target_camo

screen:Screen = None
tower_prices = None
hero_price = None

#screen_half = 0.4351562 #for this vale and less the upgrades show on right

#ability has no check if its aviable
#ability targeting
#hero 

#usable: __init__, upgrd, ability, retargeting, set_option, should_target_camo, dele

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

    def __init__(self, _position, _type):
        self.position = _position
        self.type = _type

        self.upgrades_open:bool = False
        self.upgrades = upgrade(0, 0, 0)
        self.target_i = 0
        self.option = 0
        self.target_camo: bool = False

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
            self.targeting_chang_on_update()
            
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

        print("upgraded to: "+str(self.upgrades.a)+"-"+str(self.upgrades.b)+"-"+str(self.upgrades.c))

    def ability(self, num:int):
        if num < 0 or num > 3:
            print("wrong ability")
            return
        self.open_upgrd()
        pyautogui.press(binds["t_ab_"+str(num)])
        self.close_upgrd()

    def targeting_chang_on_update(self):
        if self.type in change_targeting:
            if self.type == "heli" and self.upgrades.a == 2:
                self.target_i = change_targeting[self.type]
            elif self.type == "ace" and self.upgrades.c == 2:
                self.target_i = change_targeting[self.type]
            elif self.type == "sniper" and self.upgrades.b == 5:
                print("aaaaaaaaaaa")
                global_upgrades(self)
                self.target_i = change_targeting[self.type]

    def norm_target_change(self, type_of_trageting):
        time.sleep(self.mouse_move_time)
        pyautogui.press(binds["target"])
        if self.type == "sniper" and elite_sniper:
            self.target_i = (self.target_i+1)%len(type_of_trageting)
        else:
            self.target_i = (self.target_i+1)%len(type_of_trageting)
        #print("targeting changed to", targets[target_i])
    
    def target(self, target, targeting_type = targets):
        self.open_upgrd()
        trys = 0
        for i in range (len(targeting_type)+1):
            self.norm_target_change(targeting_type)
            if target == targeting_type[self.target_i]:
                break
            trys += 1
        self.close_upgrd()
        if trys == len(targeting_type)+1:
            print("targeting not found")
            return

    def retargeting(self, target):
        if self.type in normal:
            if self.type == "sniper" and elite_sniper:
                print("aaaaaaaaaaa")
                self.target(target, targets_elite_s)
            else:
                self.target(target)
        elif self.type in normal_unless_upgrd:
            if self.type == "tack" and self.upgrades.a >= 5:
                self.target(target)
            elif self.type == "ice" and self.upgrades.c >= 3:
                self.target(target)
            elif self.type == "village" and self.upgrades.a >= 5:
                self.target(target)
            elif self.type == "sub" and not self.option:
                self.target(target)
            elif self.type == "spike" and self.upgrades.c >= 2:
                self.target(target, targets_spike)
                
            print("retargeting to:", target)
        elif self.type in way_different:
            if self.type == "heli":
                if self.upgrades.a >= 2:
                    print(self.target_i)
                    self.target(target, targets_heli_p)
                else:
                    self.target(target, targets_heli)
            elif self.type == "ace":
                if self.upgrades.c >= 2:
                    self.target(target, targets_ace_c)
                else:
                    self.target(target, targets_ace)
            elif self.type == "dartling":
                if self.upgrades.c >= 4:
                    self.target(target, targets_dartling_i)
                else:
                    self.target(target, targets_dartling)
            elif self.type == "mortar":
                print("yea this is not the place for this")
        else:
            print("this monkey doesnt have targeting")

    def target_click(self, pos, double = None):
        if isinstance(pos, vec2):
            px_pos = screen.to_px(pos)
            print("placing target at:", pos.x, pos.y)
        else:
            px_pos = screen.to_px(pos.position)
        
        if double != None:
            px_pos2 = screen.to_px(double)
            pyautogui.moveTo(px_pos2.x, px_pos2.y, self.mouse_move_time)
            pyautogui.click()
            time.sleep(self.mouse_move_time*2)
        
        pyautogui.moveTo(px_pos.x, px_pos.y, self.mouse_move_time)
        pyautogui.click()
        time.sleep(self.mouse_move_time*2)

    def target_point(self, pos, name, double = None):
        self.open_upgrd()
        pyautogui.press(binds[name])
        
        if pos == None:
            print("location not given")
            return
        self.target_click(pos, double)
        
        self.close_upgrd()

    def set_option(self, opt = None, double = None):
        if self.type in adds_button:
            if self.type == "boomerang":
                self.open_upgrd()
                pyautogui.press(binds["opt1"])
                self.close_upgrd()
                self.option = not self.option
            elif self.type == "sub" and self.upgrades.a >= 3:
                self.open_upgrd()
                pyautogui.press(binds["opt1"])
                self.close_upgrd()
                self.option = not self.option
            elif self.type == "mermonkey" and self.upgrades.c >= 4:
                if not self.option:
                    self.target_point(opt, "opt1")
                else:
                    self.open_upgrd()
                    pyautogui.press(binds["opt1"])
                    self.close_upgrd()

                self.option = not self.option
            elif self.type == "spike" and self.upgrades.c >= 2 and self.target_i == 3:
                self.target_point(opt, "opt1")
            elif self.type == "engineer" and self.upgrades.b >= 3:
                self.target_point(opt, "opt1")
            elif self.type == "wizard" and self.upgrades.c >= 4:
                self.target_point(opt, "opt2")
            elif self.type == "wizard" and self.upgrades.a >=1 and self.upgrades.b >= 2:
                self.target_point(opt, "opt1")
            elif self.type == "skywarden" and self.upgrades.a >= 2:
                self.open_upgrd()
                pyautogui.press(binds["opt1"])
                self.close_upgrd()
                self.option = not self.option
            elif self.type == "handler" and (self.upgrades.a > 0 or self.upgrades.b > 0 or self.upgrades.c > 0):
                if isinstance(opt, vec2):
                    self.target_point(opt, "opt2")
                else:
                    self.target_point(opt, "merge")
        elif self.type in way_different:
            if self.type == "heli" and (self.target_i == 1 or self.target_i == 2):
                if self.target_i == 1:
                    self.target_point(opt, "opt1")
                else:
                    self.target_point(opt, "opt1", double)
            elif self.type == "ace":
                if self.target_i == 4 and opt != None:
                    self.target_point(opt, "centr")
                else:
                    self.open_upgrd()
                    pyautogui.press(binds["opt1"])
                    self.close_upgrd()
                    self.option = not self.option
            elif self.type == "mortar":
                self.target_point(opt, "target")
            elif self.type == "dartling" and self.target_i == 1 :
                self.target_point(opt, "opt1")

    def should_target_camo(self, camo:bool):
        if camo == self.target_camo:
            return
        if not self.type in can_target_camo:
            print("tower cant see camo")
            return
        if can_target_camo[self.type] > self.upgrades:
            print("path cant see camo")
            return

        opt = 1

        if self.type == "skywarden":
            opt = 2

        self.open_upgrd()
        pyautogui.press(binds["opt"+opt])
        self.close_upgrd()
        self.option = not self.option
        
    def dele(self):
        print("deleting", self.type)

        self.open_upgrd()
        
        pyautogui.press(binds["del"])


def global_upgrades(monkey:monkey):
    global elite_sniper

    if monkey.type == "sniper":
        elite_sniper = 1