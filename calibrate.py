import time
import mss
import pyautogui
from pynput import keyboard

from myvar import vec2, upgrade
import screenspace

running = True

def on_press(key):
    global running
    if key == keyboard.Key.f11:
        running = False
        return False  # stops the listener

keyboard.Listener(on_press=on_press).start()

print("Hover the mouse over the game monitor...")
time.sleep(3)

screen = screenspace.Screen(screenspace.monitor_under_cursor())
print(f"Monitor: left={screen.left} top={screen.top} {screen.w}x{screen.h}")

print("Move the mouse over things in the game. Press F11 to quit.\n")

with mss.mss() as sct:
    while running:
        pos = vec2(*pyautogui.position())
        nx, ny = screen.to_norm(pos.x, pos.y)
        r, g, b = sct.grab({"left": pos.x, "top": pos.y, "width": 1, "height": 1}).pixel(0, 0)

        print(
            f"\rpx:   ({pos.x}, {pos.y})  RGB=({r}, {g}, {b})\033[K\n"
            f"norm: ({nx:.4f}, {ny:.4f})\033[K\033[A",
            end="", flush=True,
        )
        time.sleep(0.05)

print("\n\nStopped.")