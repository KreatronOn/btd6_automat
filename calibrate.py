import time
import mss
import pyautogui
from pynput import keyboard

from myvar import vec2, upgrade
import screenspace

running = True
saved_locations = []

def on_press(key):
    global running, saved_locations
    if key == keyboard.Key.f9:
        running = False
        return False
        
    elif key == keyboard.Key.f4:
        # F4: Save coordinates only
        px, py = pyautogui.position()
        screen = screenspace.Screen(screenspace.monitor_under_cursor())
        pos = vec2(px, py)
        nx, ny = screen.to_norm(pos.x, pos.y)
        
        saved_locations.append({
            "has_color": False,
            "nx": nx,
            "ny": ny,
        })
        
        print(f"\n[Saved Pos #{len(saved_locations)}] norm: ({nx:.4f}, {ny:.4f})")
        
    elif key == keyboard.Key.f3:
        # F3: Save coordinates + pixel color
        px, py = pyautogui.position()
        screen = screenspace.Screen(screenspace.monitor_under_cursor())
        pos = vec2(px, py)
        nx, ny = screen.to_norm(pos.x, pos.y)
        
        try:
            r, g, b = pyautogui.pixel(px, py)
        except Exception:
            r, g, b = (0, 0, 0)
        
        saved_locations.append({
            "has_color": True,
            "nx": nx,
            "ny": ny,
            "r": r,
            "g": g,
            "b": b
        })
        
        print(f"\n[Saved Pos + Color #{len(saved_locations)}] norm: ({nx:.4f}, {ny:.4f}) | RGB=({r}, {g}, {b})")

keyboard.Listener(on_press=on_press).start()

print("Press F4 to save coordinates only.")
print("Press F3 to save coordinates and pixel color.")
print("Press F9 to quit.\n")

with mss.mss() as sct:
    while running:
        screen = screenspace.Screen(screenspace.monitor_under_cursor())

        px, py = pyautogui.position()

        pos = vec2(px, py)
        nx, ny = screen.to_norm(pos.x, pos.y)
        
        try:
            r, g, b = sct.grab({"left": pos.x, "top": pos.y, "width": 1, "height": 1}).pixel(0, 0)
        except Exception:
            r, g, b = (0, 0, 0)

        print(
            f"\rpx: ({pos.x:5d}, {pos.y:4d}) | RGB=({r}, {g}, {b})     \n"
            f"norm: ({nx:.4f}, {ny:.4f})\033[K\033[A",
            end="", flush=True,
        )
        time.sleep(0.05)

print("\n\nStopped.")
print(f"Total saved locations ({len(saved_locations)}):")
for i, loc in enumerate(saved_locations, 1):
    if loc.get("has_color"):
        print(f"vec2({loc['nx']:.4f}, {loc['ny']:.4f}): ({loc['r']}, {loc['g']}, {loc['b']}),")
    else:
        print(f"vec2({loc['nx']:.4f}, {loc['ny']:.4f}),")