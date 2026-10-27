import time
import mss
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

print("Running... Move the mouse freely across monitors. Press F11 to quit.\n")

with mss.mss() as sct:
    while running:
        # Automatically detect which monitor the mouse is on right now
        screen = screenspace.Screen(screenspace.monitor_under_cursor())

        # Grab position using screenspace's pointer lookup
        # (We query pointer via a quick tkinter call matching screenspace)
        import tkinter as tk
        root = tk.Tk()
        root.withdraw()
        px, py = root.winfo_pointerx(), root.winfo_pointery()
        root.destroy()

        pos = vec2(px, py)
        nx, ny = screen.to_norm(pos.x, pos.y)
        
        try:
            r, g, b = sct.grab({"left": pos.x, "top": pos.y, "width": 1, "height": 1}).pixel(0, 0)
        except Exception:
            r, g, b = (0, 0, 0)

        print(
            f"\rMonitor left: {screen.left:5d} | px: ({pos.x:5d}, {pos.y:4d}) | RGB=({r}, {g}, {b})     \n"
            f"norm: ({nx:.4f}, {ny:.4f})\033[K\033[A",
            end="", flush=True,
        )
        time.sleep(0.05)

print("\n\nStopped.")