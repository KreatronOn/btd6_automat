from myvar import vec2, upgrade
import screenspace


class monkey:
    mouse_move_time = 0.1

    type = ""
    position = vec2()
    upgrades = upgrade()

    def __init__(self, _position, _type):
        self.position = _position
        self.type = _type

        px_pos = screen.to_px(_position)

        pyautogui.press(towers[_type])
        pyautogui.moveTo(px_pos.x, px_pos.y, self.mouse_move_time)
        pyautogui.click()
