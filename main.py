import os
import time
from pynput import keyboard, mouse

from myvar import vec2, upgrade
import mokey
from mokey import monkey
import screenspace
import cash

#key binds of script
def on_press(key):
    if key == keyboard.Key.f11:
        print("\nF11 pressed, aborting.")
        os._exit(0)
keyboard.Listener(on_press=on_press).start()

#initializing
screen = screenspace.Screen(screenspace.monitor_under_cursor())
cash.init(screen)
mokey.init("sauda", screen, 0)

def main():
    dart1 = monkey(vec2(0.5, 0.5), "boomerang")

    dart1.upgrd(upgrade(0, 2, 5))

    dart1.retargeting("strong")

    dart1.set_option()

    #del dart1

#mouse clicks
print("Waiting for a mouse click to trigger main()... (Press F11 to abort)")
def on_click(x, y, button, pressed):
    if pressed:
        time.sleep(1/10)
        main()
        return False #listens only for the firs click
with mouse.Listener(on_click=on_click) as listener:
    listener.join()

print("done")