import os
import time
import pyautogui
from pynput import keyboard

from myvar import vec2
import screenspace
import monkey
import cash






wait_for_screen = 3

dart1_pos = vec2(0.2883, 0.4813)

print("Hover the mouse over the game monitor...")
time.sleep(wait_for_screen)
screen = screenspace.Screen(screenspace.monitor_under_cursor())

pyautogui.PAUSE = 0.05

def on_press(key):
    if key == keyboard.Key.f11:
        print("\nF11 pressed, aborting.")
        os._exit(0)
keyboard.Listener(on_press=on_press).start()

cash.init(screen)
dart1 = monkey(dart1_pos, "dart")

print("done")