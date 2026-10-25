import mss
import pyautogui

from myvar import vec2

def monitor_under_cursor():
    x, y = pyautogui.position()

    with mss.mss() as sct:
        for m in sct.monitors[1:]:
            if (m["left"] <= x < m["left"] + m["width"] and
                    m["top"] <= y < m["top"] + m["height"]):
                return m
    raise RuntimeError("Cursor is not on any monitor")

class Screen:
    def __init__(self, mon):
        self.left, self.top = mon["left"], mon["top"]
        self.w, self.h = mon["width"], mon["height"]

    def to_px(self, nx:float, ny:float):
        return vec2(self.left + nx * self.w, self.top + ny * self.h)
    def to_px(self, xy:vec2):
            return vec2(self.left + xy.x * self.w, self.top + xy.y * self.h)

    def to_norm(self, x, y):
        return (x - self.left) / self.w, (y - self.top) / self.h

    def to_region(self, nx, ny, nw, nh):
        """Normalized box -> mss region dict."""
        return {
            "left": round(self.left + nx * self.w),
            "top": round(self.top + ny * self.h),
            "width": round(nw * self.w),
            "height": round(nh * self.h),
        }