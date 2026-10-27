import os
import time
from pynput import keyboard, mouse

from myvar import vec2, upgrade
import mokey
from mokey import monkey
import screenspace
import cash
from script import script
import menus

#key binds of script
def on_press(key):
    if key == keyboard.Key.f9:
        print("\nF9 pressed, aborting.")
        os._exit(0)
keyboard.Listener(on_press=on_press).start()


def main():
    #initializing
    screen = screenspace.Screen(screenspace.monitor_under_cursor())
    cash.init(screen)
    mokey.init("sauda", screen, 0)
    menus.init(screen)

    script()

#mouse clicks
print("Waiting for a mouse click to trigger main()... (Press F9 to abort)")
def on_click(x, y, button, pressed):
    if pressed:
        time.sleep(1/10)
        main()
        return False #listens only for the firs click
with mouse.Listener(on_click=on_click) as listener:
    listener.join()

print("done")