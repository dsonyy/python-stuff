import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def init():
    fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(12, 8))
    sz = 300

    ax[0].set_title("Accelerometer")
    ax[1].set_title("Gyroscope")

    return fig, ax


def draw(fig, ax, data):
    sz = len(data)
    data_max = [series.max() for series in data.T]
    data_min = [series.min() for series in data.T]
    data_mean = [series.mean().round() for series in data.T]
    data_max, data_min, data_mean

    for s, series_name in enumerate(("Accel", "Gyro")):
        ax[s].clear()

        ax[s].axis([0, sz, min(data_min), max(data_max)])

        ax[s].plot(data[:, s + 0], lw=1, label="X", c="#C00")
        ax[s].plot(data[:, s + 1], lw=1, label="Y", c="#0C0")
        ax[s].plot(data[:, s + 2], lw=1, label="Z", c="#00C")

        ax[s].legend(loc='lower left')

        ax[s].text(sz + 2, data[-1, s + 0], "X: " +
                   str(data[-1, s + 0]), c="#C00")
        ax[s].text(sz + 2, data[-1, s + 1], "Y: " +
                   str(data[-1, s + 1]), c="#0C0")
        ax[s].text(sz + 2, data[-1, s + 2], "Z: " +
                   str(data[-1, s + 2]), c="#00C")

        ax[s].xaxis.set_ticks(np.arange(0, sz + 1, 20))
        ax[s].grid(alpha=0.3)

    ax[0].set_title("Accelerometer")
    ax[1].set_title("Gyroscope")


def animate(data, ax):
    sz = len(data)

    for s, series_name in enumerate(("Accel", "Gyro")):
        ax[s].clear()

        ax[s].axis([0, sz, data.max(), data.min()])
        ax[s].xaxis.set_ticks(np.arange(0, sz + 1, 20))
        ax[s].grid(alpha=0.3)

        ax[s].plot(data[:, s + 0], lw=1, label="X", c="#C00")
        ax[s].plot(data[:, s + 1], lw=1, label="Y", c="#0C0")
        ax[s].plot(data[:, s + 2], lw=1, label="Z", c="#00C")

        ax[s].legend(loc='lower left')

        ax[s].text(sz + 2, data[-1, s + 0], "X: " +
                   str(data[-1, s + 0]), c="#C00")
        ax[s].text(sz + 2, data[-1, s + 1], "Y: " +
                   str(data[-1, s + 1]), c="#0C0")
        ax[s].text(sz + 2, data[-1, s + 2], "Z: " +
                   str(data[-1, s + 2]), c="#00C")


if __name__ == "__main__":
    data = []
    with open("test.txt") as f:
        data = np.array([[int(v) for v in line.split()] for line in f])

    fig, ax = init()
    # draw(fig, ax, data)
    # plt.show()
    ani = animation.FuncAnimation(fig, lambda frame: animate(data, ax))
    plt.show()
