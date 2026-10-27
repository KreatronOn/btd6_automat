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


def main():
    #initializing
    screen = screenspace.Screen(screenspace.monitor_under_cursor())
    cash.init(screen)
    mokey.init("sauda", screen, 0)

    monkey1 = monkey(vec2(0.3, 0.5), "handler")
    monkey2 = monkey(vec2(0.3, 0.6), "handler")

    monkey1.upgrd(upgrade(0, 2, 0))
    monkey2.upgrd(upgrade(0, 1, 0))

    #monkey1.should_target_camo(True)
    time.sleep(1)
    monkey1.set_option(vec2(0.2, 0.5))
    monkey2.set_option(monkey1)
    #monkey1.set_option()

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