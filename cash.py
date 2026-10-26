import os
import sys
import cv2
import mss
import time
import numpy as np

from screenspace import Screen, monitor_under_cursor


REGION_NORM = (0.191, 0.022, 0.2, 0.035)
REGION = None

def init(screen):
    global REGION
    REGION = screen.to_region(*REGION_NORM)

DEBUG_SAVE = False       # set to False for normal runs
DEBUG_DIR = "debug"
TEMPLATE_DIR = "digits"
SIZE = (16, 24)

def save_debug(gray, name):
    os.makedirs(DEBUG_DIR, exist_ok=True)
    cv2.imwrite(os.path.join(DEBUG_DIR, name), gray)
    debug_read()
def debug_read():
    gray = grab()
    cv2.imwrite(os.path.join(DEBUG_DIR, "raw.png"), gray)
    mask = make_mask(gray)
    os.makedirs(DEBUG_DIR, exist_ok=True)
    cv2.imwrite(os.path.join(DEBUG_DIR, "mask.png"), mask)
    templates = load_templates()
    segs = segments(gray)
    print("segments:", len(segs))
    for i, seg in enumerate(segs):
        s = seg.astype(np.float32)
        d, name = min((np.abs(s - t).mean(), n) for n, t in templates)
        print(i, "best:", name, "diff:", round(float(d), 1))
        cv2.imwrite(os.path.join(DEBUG_DIR, f"seg_{i}.png"), seg)

def grab():
    with mss.MSS() as sct:
        img = np.array(sct.grab(REGION))
    return cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)

KERNEL = np.ones((3, 3), np.uint8)
def make_mask(gray):
    mask = (gray > 240).astype(np.uint8) * 255
    return cv2.morphologyEx(mask, cv2.MORPH_OPEN, KERNEL)

def segments(gray):
    """One binary image per digit, left to right (commas and specks are dropped)."""
    mask = make_mask(gray)
    n, _, stats, _ = cv2.connectedComponentsWithStats(mask)
    comps = [tuple(int(v) for v in stats[i]) for i in range(1, n)]  # x, y, w, h, area
    if not comps:
        return []
    max_h = max(c[3] for c in comps)
    if max_h < 0.4 * gray.shape[0]:        # nothing digit-sized in the box
        return []
    max_area = max(c[4] for c in comps)
    keep = [c for c in comps if c[3] >= 0.7 * max_h and c[4] >= 0.15 * max_area]
    keep.sort(key=lambda c: c[0])
    return [cv2.resize(mask[y:y + h, x:x + w], SIZE, interpolation=cv2.INTER_AREA)
            for x, y, w, h, _ in keep]

def load_templates():
    templates = []
    for name in os.listdir(TEMPLATE_DIR):
        img = cv2.imread(os.path.join(TEMPLATE_DIR, name), cv2.IMREAD_GRAYSCALE)
        templates.append((name[0], img.astype(np.float32)))
    return templates

def read_cash(templates=None):
    templates = templates or load_templates()
    gray = grab()
    if DEBUG_SAVE:
        save_debug(gray, "last.png")

    digits = ""
    for seg in segments(gray):
        seg = seg.astype(np.float32)
        best, best_diff = None, 1e9
        for d, t in templates:
            diff = np.abs(seg - t).mean()
            if diff < best_diff:
                best, best_diff = d, diff
        if best_diff > 40:
            if DEBUG_SAVE:
                save_debug(gray, f"fail_{int(time.time())}.png")
            return None
        digits += best
    return int(digits) if digits else None

def learn(text):
    cv2.imwrite("debug_region.png", grab())
    """Save the digits currently on screen as templates. text = the cash you see."""
    os.makedirs(TEMPLATE_DIR, exist_ok=True)
    segs = segments(grab())
    if len(segs) != len(text):
        print(f"Found {len(segs)} segments but you typed {len(text)} digits. "
              "Adjust REGION or the threshold.")
        return
    n = len(os.listdir(TEMPLATE_DIR))
    for i, (d, seg) in enumerate(zip(text, segs)):
        cv2.imwrite(os.path.join(TEMPLATE_DIR, f"{d}_{n + i}.png"), seg)
    print("Saved", text)

if __name__ == "__main__":
    print("Move the cursor onto the game monitor...")
    time.sleep(3)
    init(Screen(monitor_under_cursor()))
    if sys.argv[1] == "learn":
        learn(sys.argv[2])
    elif sys.argv[1] == "debug":
        debug_read()
    else:
        print(read_cash())

def get_cash(samples = 5, retries=20):
    counts = {}
    attempts = 0
    good = 0
    while good < samples and attempts < retries:
        attempts += 1
        value = read_cash()
        if value is None:
            time.sleep(1 / 60)
            continue
        counts[value] = counts.get(value, 0) + 1
        good += 1
    if not counts:
        return None
    return max(counts, key=counts.get)