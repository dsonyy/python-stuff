from types import FrameType
import matplotlib.pyplot as plt
import matplotlib.animation as ani
import numpy as np
import random


def init_chaos(pts, samples):
    # defining the triangle vertices
    a = 0.95
    pts[0] = np.array((-a, -a))
    pts[1] = np.array((a, -a))
    pts[2] = np.array((0, a))

    # starting point
    p_idx, q_idx = random.sample(range(3), 2)
    pts[3] = np.array((
        (pts[p_idx, 0] + pts[q_idx, 0]) / 2,
        (pts[p_idx, 1] + pts[q_idx, 1]) / 2
    ))

    # calculating chaos points
    for idx in range(4, samples):
        p_idx = idx - 1
        q_idx = random.randint(0, 2)
        pts[idx] = np.array((
            (pts[p_idx, 0] + pts[q_idx, 0]) / 2,
            (pts[p_idx, 1] + pts[q_idx, 1]) / 2
        ))


def init_chaos2(pts, samples):
    # defining the vertices
    vertices = 3
    a = 0.95
    pts[0] = np.array((random.uniform(-a, -a/2), random.uniform(-a, -a/2)))
    pts[1] = np.array((random.uniform(-a, a), random.uniform(a/2, a)))
    pts[2] = np.array((random.uniform(a/2, a), random.uniform(-a, -a/2)))

    # starting point
    p_idx, q_idx = random.sample(range(vertices), 2)
    pts[vertices] = np.array((
        (pts[p_idx, 0] + pts[q_idx, 0]) / 2,
        (pts[p_idx, 1] + pts[q_idx, 1]) / 2
    ))

    # calculating chaos points
    for idx in range(vertices + 1, samples):
        p_idx = idx - 1
        q_idx = random.randint(0, vertices)
        pts[idx] = np.array((
            (pts[p_idx, 0] + pts[q_idx, 0]) / 2,
            (pts[p_idx, 1] + pts[q_idx, 1]) / 2
        ))


def animate(frames, plot):
    plot.set_data(frames[:, 0], frames[:, 1])


def get_frames():
    # allocating data buffer
    samples = 7000
    pts = np.empty((samples, 2), np.float)

    while True:
        # generating chaos data
        init_chaos2(pts, samples)

        # yielding animation frames
        i = 3
        while i < len(pts):
            yield pts[:i]
            i += 20


def main():
    # creating a figure
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.axes.set_aspect('equal')
    ax.set_axis_off()
    fig.tight_layout()

    # creating a plot with all points
    # ax.plot(pts[:, 0], pts[:, 1], ".", c="k")

    # creating an empty plot to be filled over time
    plot, = ax.plot([], [], ".", c="b")

    # creating an animation
    _ = ani.FuncAnimation(fig, lambda f: animate(f, plot),
                          frames=get_frames(), interval=10)

    # run the plot
    plt.show()


if __name__ == "__main__":
    main()
