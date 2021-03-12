import platform
import os
import time
from math import sqrt, floor
import numpy as np

WIDTH = 100
HEIGHT = 100
SZ = (WIDTH, HEIGHT)

COLORSCALES = (
    "0123456789",
    "0123456789ABCDEF",
    ".:;+=x$X#",
    "░▒▓█",
)


def clear():
    """Clear the console buffer."""
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def render(surf, colorscale_idx=-1):
    colorscale = COLORSCALES[colorscale_idx]
    min = np.nanmin(surf)
    max = np.nanmax(surf)

    buffer = ""
    for row in surf:
        for val in row:
            if np.isnan(val):
                buffer += " "
            elif val == max:
                buffer += colorscale[-1]
            else:
                idx = floor((val - min) / (max - min) * len(colorscale))
                buffer += colorscale[idx]
        buffer += "\n"
    print(buffer, end="")


def create_surface(w, h):
    return np.full((h, w), np.nan, dtype=np.single)


def torusdep(w, h, surf, r, R):
    for i in range(w):
        for j in range(h):
            x = i - w / 2
            y = j - h / 2

            z_sq = r**2 - (sqrt(x**2 + y**2) - R)**2
            # No real solutions
            if z_sq < 0:
                continue
            # One real solution
            elif z_sq == 0:
                surf[j][i] = "0"
            # Two real solutions (but we consider only the greatest one)
            else:
                surf[j][i] = "#"  # sqrt(z_sq)


def torus(x, y, r, R):
    z_sq = r**2 - (sqrt(x**2 + y**2) - R)**2
    # No real solutions
    if z_sq < 0:
        return None
    # One real solution
    elif z_sq == 0:
        return 0
    # Two real solutions (but we consider only the greatest one)
    else:
        return sqrt(z_sq)


def sphere(x, y, r, x0=0, y0=0):
    """
    Formula:
        (x - x0)**2 + (y - y0)**2 + (z - z0)**2 = r**2
    """
    z_sq = r**2 - (x - x0)**2 - (y - y0)**2
    if z_sq < 0:
        return None
    elif z_sq == 0:
        return 0
    else:
        return sqrt(z_sq)


def draw(w, h, surf, fn, args=()):
    for i in range(w):
        for j in range(h):
            x = i - w / 2
            y = j - h / 2
            z = fn(x, y, *args)
            if not z is None:
                surf[j, i] = z


def main():
    """Program entry point."""
    while True:
        surf = create_surface(WIDTH, HEIGHT)
        fn = torus
        args = (10, 30)
        draw(WIDTH, HEIGHT, surf, fn, args)
        render(surf)
        break
        time.sleep(0.2)
        clear()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
