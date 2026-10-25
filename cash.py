import os
import sys
import cv2
import mss
import time
import numpy as np

from screenspace import Screen, monitor_under_cursor

REGION_NORM = (0.191, 0.02, 0.27, 0.04)
REGION = None

def init(screen):
    global REGION
    REGION = screen.to_region(*REGION_NORM)

TEMPLATE_DIR = "digits"
SIZE = (16, 24)

def grab():
    with mss.MSS() as sct:
        img = np.array(sct.grab(REGION))
    return cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)

def segments(gray):
    """Split the region into one binary image per digit (commas are skipped)."""
    mask = (gray > 200).astype(np.uint8) * 255
    cols = mask.any(axis=0)
    parts, start = [], None
    for i, c in enumerate(np.append(cols, False)):
        if c and start is None:
            start = i
        elif not c and start is not None:
            part = mask[:, start:i]
            rows = np.where(part.any(axis=1))[0]
            parts.append(part[rows[0]:rows[-1] + 1])
            start = None
    if not parts:
        return []
    tallest = max(p.shape[0] for p in parts)
    return [cv2.resize(p, SIZE, interpolation=cv2.INTER_AREA)
            for p in parts if p.shape[0] >= 0.7 * tallest]

def load_templates():
    templates = []
    for name in os.listdir(TEMPLATE_DIR):
        img = cv2.imread(os.path.join(TEMPLATE_DIR, name), cv2.IMREAD_GRAYSCALE)
        templates.append((name[0], img.astype(np.float32)))
    return templates

def read_cash(templates=None):
    templates = templates or load_templates()
    digits = ""
    for seg in segments(grab()):
        seg = seg.astype(np.float32)
        best, best_diff = None, 1e9
        for d, t in templates:
            diff = np.abs(seg - t).mean()
            if diff < best_diff:
                best, best_diff = d, diff
        if best_diff > 40:  # nothing matches well, so the read is unreliable
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
    else:
        print(read_cash())