import time
import platform
import os

W = 180
H = 100
x_min = -2.5
x_max = 1.0
y_min = -1.0
y_max = 1.0


def clear():
    """Clear the console buffer."""
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def mandelbrot(max_iteration):
    canvas = ""
    for i in range(H + 1):
        for j in range(W + 1):
            x0 = j / W * (x_max - x_min) + x_min
            y0 = i / H * (y_max - y_min) + y_min

            x = 0
            y = 0

            iteration = 0

            while x*x + y*y <= 4 and iteration < max_iteration:
                x, y = x*x - y*y + x0, 2*x*y + y0
                iteration += 1

            canvas += "#" if iteration == max_iteration else " "
        canvas += "\n"
    return canvas


if __name__ == "__main__":
    try:
        for i in range(1, 10000):
            canv = mandelbrot(i)
            time.sleep(0.1)
            canv = "Iterations: " + str(i) + "\n" + canv
            clear()
            print(canv)
    except KeyboardInterrupt:
        pass
