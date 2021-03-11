import platform
import os
import time
from math import sqrt

WIDTH = 40
HEIGHT = 40
SZ = (WIDTH, HEIGHT)


def clear():
    """Clear the console buffer."""
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def render(surf):
    buffer = ""
    for row in surf:
        for ch in row:
            buffer += ch
        buffer += "\n"
    print(buffer, end="")


def create_surface(w, h, ch="."):
    return [[ch] * w] * h


def torus(w, h, surf, r, R):
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


def main():
    """Program entry point."""
    while True:
        surf = create_surface(WIDTH, HEIGHT)
        torus(WIDTH, HEIGHT, surf, 0.0001, 0.00001)
        render(surf)
        time.sleep(0.2)
        clear()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
