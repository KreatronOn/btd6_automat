import math
import threading
import time

import cv2
import mss
import numpy as np

from myvar import vec2
import menus as m

TEMPLATE_PATH = "assets/gold.png"
MATCH_THRESHOLD = 0.80
ICON_HEIGHT_FRAC = 0.060
SCALE_SPREAD = np.linspace(0.8, 1.25, 9)
SLOT_HALF_X = 0.105
SLOT_HALF_Y = 0.140
NEXT_PAGE_BTN = vec2(0.858, 0.399)
PREV_PAGE_BTN = vec2(0.141, 0.399)
DOT_Y = 0.7019
DOT_X0 = 0.3453
DOT_DX = 0.01927
DOT_COUNT = 17
PAGE_DELAY = 0.75
DEBUG_IMAGE = ""           #debug image, "" = off



def _load_template(path):
    img = cv2.imread(path, cv2.IMREAD_UNCHANGED)

    if img is None:
        raise FileNotFoundError(f"template not found: {path}")
    if img.ndim == 2:
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

    if img.shape[2] == 4:
        bgr = img[:, :, :3]
        _, mask = cv2.threshold(img[:, :, 3], 127, 255, cv2.THRESH_BINARY)
        ys, xs = np.where(mask > 0)
        if len(xs) == 0:
            raise ValueError("template is fully transparent")
        y0, y1, x0, x1 = ys.min(), ys.max() + 1, xs.min(), xs.max() + 1
        return (np.ascontiguousarray(bgr[y0:y1, x0:x1]),
                np.ascontiguousarray(mask[y0:y1, x0:x1]))

    return np.ascontiguousarray(img[:, :, :3]), None

_cache = {}

def _get_template():
    if "t" not in _cache:
        _cache["t"] = _load_template(TEMPLATE_PATH)
    return _cache["t"]

def _scales():
    tpl, _ = _get_template()
    base = ICON_HEIGHT_FRAC * m.screen.h / tpl.shape[0]
    return base * SCALE_SPREAD

_local = threading.local()

def _grab_monitor():
    scr = m.screen
    sct = getattr(_local, "sct", None)
    if sct is None:                      # one mss object per thread
        sct = _local.sct = mss.mss()
    shot = sct.grab({"left": scr.left, "top": scr.top,
                     "width": scr.w, "height": scr.h})
    return cv2.cvtColor(np.array(shot), cv2.COLOR_BGRA2BGR)

def _best_match(img):
    tpl, mask = _get_template()
    best = (-1.0, (0, 0), 0, 0)
    for s in _scales():
        w, h = int(tpl.shape[1] * s), int(tpl.shape[0] * s)
        if w < 8 or h < 8 or w > img.shape[1] or h > img.shape[0]:
            continue
        t = cv2.resize(tpl, (w, h), interpolation=cv2.INTER_AREA)
        mk = (cv2.resize(mask, (w, h), interpolation=cv2.INTER_NEAREST)
              if mask is not None else None)
        res = cv2.matchTemplate(img, t, cv2.TM_CCOEFF_NORMED, mask=mk)
        # masked CCOEFF can return NaN / huge garbage on flat areas -> drop it
        valid = (res >= -1.01) & (res <= 1.01)
        res = np.where(valid, res, -1.0).astype(np.float32)
        _, score, _, loc = cv2.minMaxLoc(res)
        if score > best[0]:
            best = (float(score), loc, w, h)
    return best

def _scan_frame(frame):
    scr = m.screen
    out = []
    for c in m.SLOT_CENTERS:
        x0 = max(int((c.x - SLOT_HALF_X) * scr.w), 0)
        x1 = min(int((c.x + SLOT_HALF_X) * scr.w), frame.shape[1])
        y0 = max(int((c.y - SLOT_HALF_Y) * scr.h), 0)
        y1 = min(int((c.y + SLOT_HALF_Y) * scr.h), frame.shape[0])
        score, (lx, ly), w, h = _best_match(frame[y0:y1, x0:x1])
        out.append({"score": score,
                    "box": (x0 + lx, y0 + ly, w, h),
                    "rect": (x0, y0, x1 - x0, y1 - y0)})
    return out

def save_debug(frame, results, path=DEBUG_IMAGE):
    if not path:
        return
    img = frame.copy()
    for i, r in enumerate(results):
        x, y, w, h = r["rect"]
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        bx, by, bw, bh = r["box"]
        hit = r["score"] >= MATCH_THRESHOLD
        color = (0, 0, 255) if hit else (160, 160, 160)
        cv2.rectangle(img, (bx, by), (bx + bw, by + bh), color, 3 if hit else 1)
        cv2.putText(img, f"{i}: {r['score']:.2f}", (x + 8, y + 36),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.1, (255, 0, 0), 3)
    cv2.imwrite(path, img)

def find_golden_slot(valid=range(6), tries=3):
    valid = list(valid)
    for _ in range(tries):
        frame = _grab_monitor()
        results = _scan_frame(frame)
        save_debug(frame, results)
        print("   scores:", " ".join(f"{r['score']:.2f}" for r in results))
        best = max(valid, key=lambda i: results[i]["score"])
        if results[best]["score"] >= MATCH_THRESHOLD:
            return best
        time.sleep(0.3)
    return None

def read_page(frame=None):
    if frame is None:
        frame = _grab_monitor()
    scr = m.screen
    y = int(DOT_Y * scr.h)
    bright = []
    for k in range(DOT_COUNT):
        x = int((DOT_X0 + k * DOT_DX) * scr.w)
        patch = frame[y - 2:y + 3, x - 2:x + 3].astype(int)
        bright.append(patch.sum(axis=2).mean())
    best = int(np.argmax(bright))
    return best if bright[best] > 250 else None   # dark dot ~ 30, lit dot ~ 480

def go_to_page(target):
    for _ in range(25):
        page = read_page()
        if page is None:
            raise RuntimeError("cannot read the page dots - is the map select screen open?")
        if page == target:
            return
        m.click(NEXT_PAGE_BTN if page < target else PREV_PAGE_BTN)
        time.sleep(PAGE_DELAY)
    raise RuntimeError(f"could not reach page {target}")

def select_golden_map(click_it=False):
    """Scan the beginner pages and return the golden bloon map's name (or None).
    click_it=True also clicks the map; the default only returns the name, so
    your own code can do map_select(name)."""
    names = m.BEGGINER_MAPS
    last_page = (len(names) - 1) // 6

    if m.points_check(m.main_menu_check):
        m.click(m.play_btn)
        m.wait_for_map_select()

    m.click(m.DIFF_BUTTONS[0])          # Beginner tab = fast way to page 1
    time.sleep(PAGE_DELAY)

    for page in range(last_page + 1):
        go_to_page(page)                # verified with the page dots, never assumed
        print(f"page {page + 1}/{last_page + 1}")
        valid = [s for s in range(6) if page * 6 + s < len(names)]
        slot = find_golden_slot(valid)
        if slot is not None:
            name = names[page * 6 + slot]
            print(f"   golden bloon: page {page}, slot {slot} -> {name}")
            if click_it:
                m.click(m.SLOT_CENTERS[slot])
            return name

    print("golden bloon not found on any beginner page")
    return None

def self_test(scale=None):
    """Works WITHOUT the event. Open the map select screen (page 1), then run.

    Pastes the PNG (with its alpha) into a live screenshot, once per slot, and
    checks that the matcher finds it in the right slot. Compares that to the
    clean screen (no bloon) and suggests a threshold between the two.
    """
    tpl, mask = _get_template()
    if mask is None:
        raise ValueError("self_test needs a template PNG with an alpha channel")

    scr = m.screen
    frame = _grab_monitor()
    clean = _scan_frame(frame)
    clean_max = max(r["score"] for r in clean)
    print("clean screen scores:", " ".join(f"{r['score']:.2f}" for r in clean))

    if scale is None:                    # expected on-screen size of the real icon
        scale = ICON_HEIGHT_FRAC * scr.h / tpl.shape[0]
    t = cv2.resize(tpl, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA)
    a = cv2.resize(mask, (t.shape[1], t.shape[0]),
                   interpolation=cv2.INTER_NEAREST)[..., None] / 255.0
    h, w = t.shape[:2]

    pasted = []
    for i, c in enumerate(m.SLOT_CENTERS):
        x = int(c.x * scr.w) - w // 2
        y = int(c.y * scr.h) - h // 2
        fake = frame.copy()
        roi = fake[y:y + h, x:x + w]
        fake[y:y + h, x:x + w] = (a * t + (1 - a) * roi).astype(np.uint8)
        res = _scan_frame(fake)
        winner = max(range(len(res)), key=lambda k: res[k]["score"])
        pasted.append(res[i]["score"])
        ok = "OK " if winner == i else "BAD"
        print(f"{ok} slot {i}: pasted score {res[i]['score']:.3f} (winner: slot {winner})")
        if i == 0:
            save_debug(fake, res, "debug_selftest.png")

    pasted_min = min(pasted)
    print(f"\nclean max {clean_max:.3f} | pasted min {pasted_min:.3f}")
    if pasted_min > clean_max + 0.05:
        print(f"suggested MATCH_THRESHOLD ~ {(clean_max + pasted_min) / 2:.2f}")
    else:
        print("NO CLEAR GAP: the matcher cannot tell the bloon from the background.\n"
              "Crop the template tighter / use a cleaner PNG.")