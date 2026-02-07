#!/usr/bin/env python3
import os
import sys
import time
import random
import shutil
from dataclasses import dataclass

# -------------- ANSI helpers --------------
CSI = "\x1b["
def hide_cursor():   sys.stdout.write(f"{CSI}?25l"); sys.stdout.flush()
def show_cursor():   sys.stdout.write(f"{CSI}?25h"); sys.stdout.flush()
def clear_screen():  sys.stdout.write(f"{CSI}2J{CSI}H"); sys.stdout.flush()
def move(y, x):      sys.stdout.write(f"{CSI}{y};{x}H")
def color_rgb(r,g,b):sys.stdout.write(f"{CSI}38;2;{r};{g};{b}m")
def reset_color():   sys.stdout.write(f"{CSI}0m")

# -------------- Config --------------
# Character set (mix of Latin, digits, Katakana-like)
GLYPHS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@#$%&*+-=<>"
KATAKANA = "ｱｲｳｴｵｶｷｸｹｺｻｼｽｾｿﾀﾁﾂﾃﾄﾅﾆﾇﾈﾉﾊﾋﾌﾍﾎﾏﾐﾑﾒﾓﾔﾕﾖﾗﾘﾙﾚﾛﾜｦﾝ"
CHARS = (GLYPHS + KATAKANA)

# Trail look
MIN_LEN, MAX_LEN = 6, 20         # trail length range
HEAD_COLOR = (190, 255, 190)     # bright green head
TAIL_BASE  = (30, 180, 60)       # base tail green
BG_ERASE   = " "                 # what to erase with

FPS = 20                         # target FPS
MOVE_PROB_PER_FRAME = 1.0        # 1.0 => move every frame; lower to slow all drops

# -------------- Drop model --------------
@dataclass
class Drop:
    y: int           # current head y (1..H, can start negative to enter from top)
    length: int      # trail length
    tick: int        # simple modulo ticker to vary per-column speed
    delay: int       # frames between moves (1 = fastest)
    col: int         # 1-based column index

def new_drop(col, H):
    length = random.randint(MIN_LEN, MAX_LEN)
    # start above the screen so trails "fall in"
    start_y = random.randint(-H, 0)
    # per column delay: 1..4 frames
    delay = random.randint(1, 4)
    return Drop(y=start_y, length=length, tick=0, delay=delay, col=col)

def gradient_color(t, length):
    """Return RGB for a trail segment t steps behind the head (t>=1)."""
    # fade factor from 1.0 near head to ~0 at tail end
    fade = max(0.0, 1.0 - (t / (length + 1)))
    r = int(TAIL_BASE[0] * fade)
    g = int(TAIL_BASE[1] * fade + 10)
    b = int(TAIL_BASE[2] * fade)
    return (r, g, b)

def rand_char():
    # Heavier weight to Latin/digits, occasional katakana
    if random.random() < 0.85:
        return random.choice(GLYPHS)
    return random.choice(KATAKANA)

# -------------- Main loop --------------
def matrix_rain():
    random.seed()
    try:
        hide_cursor()
        clear_screen()

        cols, rows = shutil.get_terminal_size((80, 24))
        # Keep a drop per visible column (avoid rightmost to reduce wrapping issues)
        drops = [ new_drop(col+1, rows) for col in range(max(1, cols-1)) ]
        last_size_check = 0

        # For erasing last tail cells efficiently, remember last tail-end y per column
        last_tail_end = {d.col: None for d in drops}

        frame_time = 1.0 / FPS
        t0 = time.time()

        while True:
            # Occasionally re-check terminal size and adjust drops
            if last_size_check >= FPS // 2:  # ~ twice per second
                last_size_check = 0
                ncols, nrows = shutil.get_terminal_size((80, 24))
                if ncols != cols or nrows != rows:
                    # Clear and rebuild state on resize to avoid artifacts
                    cols, rows = ncols, nrows
                    clear_screen()
                    # Rebuild drops to match width (minus one to avoid wrapping)
                    width = max(1, cols-1)
                    new_drops = []
                    for i in range(width):
                        if i < len(drops):
                            d = drops[i]
                            d.col = i+1
                            d.y = min(d.y, rows+MAX_LEN)
                            new_drops.append(d)
                        else:
                            new_drops.append(new_drop(i+1, rows))
                    drops = new_drops
                    last_tail_end = {d.col: None for d in drops}

            # Draw each column
            for d in drops:
                d.tick += 1
                moved = (d.tick % d.delay == 0) and (random.random() < MOVE_PROB_PER_FRAME)
                if moved:
                    d.y += 1

                # HEAD
                if 1 <= d.y <= rows:
                    move(d.y, d.col)
                    color_rgb(*HEAD_COLOR)
                    sys.stdout.write(rand_char())

                # TRAIL behind head
                if d.length > 0:
                    tail_end_y = d.y - d.length
                    # Draw fading trail segments that are on screen
                    t = 1
                    y = d.y - 1
                    while t <= d.length and y >= 1:
                        if y <= rows:
                            move(y, d.col)
                            color_rgb(*gradient_color(t, d.length))
                            # flicker: sometimes refresh with a new glyph
                            ch = rand_char() if random.random() < 0.3 else rand_char()
                            sys.stdout.write(ch)
                        t += 1
                        y -= 1

                    # ERASE the cell just after the tail end (keeps screen clean)
                    erase_y = tail_end_y
                    if erase_y >= 1 and erase_y <= rows:
                        # Only erase if we've moved since last frame and the tail end changed
                        if last_tail_end.get(d.col) != erase_y:
                            move(erase_y, d.col)
                            reset_color()
                            sys.stdout.write(BG_ERASE)
                            last_tail_end[d.col] = erase_y

                # recycle drop after passing through
                if d.y - d.length > rows + 3:
                    # new random drop for this column
                    nd = new_drop(d.col, rows)
                    d.y, d.length, d.tick, d.delay = nd.y, nd.length, 0, nd.delay
                    last_tail_end[d.col] = None

            reset_color()
            sys.stdout.flush()

            # Frame pacing
            last_size_check += 1
            # Sleep to keep FPS; account for work time
            t0 += frame_time
            now = time.time()
            delay = t0 - now
            if delay > 0:
                time.sleep(delay)
            else:
                # If we are behind, reset the clock baseline
                t0 = now

    except KeyboardInterrupt:
        pass
    finally:
        # restore terminal state
        reset_color()
        show_cursor()
        move(shutil.get_terminal_size((80,24)).lines, 1)
        sys.stdout.write("\n")
        sys.stdout.flush()

if __name__ == "__main__":
    # Enable ANSI on very old Windows consoles (best effort; modern Windows Terminal not needed)
    if os.name == "nt":
        try:
            import msvcrt, ctypes
            kernel32 = ctypes.windll.kernel32
            handle = kernel32.GetStdHandle(-11)  # STD_OUTPUT_HANDLE
            mode = ctypes.c_uint32()
            kernel32.GetConsoleMode(handle, ctypes.byref(mode))
            kernel32.SetConsoleMode(handle, mode.value | 0x0004)  # ENABLE_VIRTUAL_TERMINAL_PROCESSING
        except Exception:
            pass
    matrix_rain()
