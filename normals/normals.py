import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)

TERRAIN_FNS = [
    lambda x, y: x,
    lambda x, y: np.sin(x) + np.sin(y),
    lambda x, y: 0,
    lambda x, y: x * 100
]


def gen_terrain(n, fn):
    """Generates a height map of size n x n."""
    pts = []
    for x in range(n):
        row = []
        for y in range(n):
            row.append(fn(x, y))
        pts.append(row)
    return pts


def terrain_to_pts(terrain):
    """Converts a terrain to 3 lists of points (x, y, z)."""
    px, py, pz = [], [], []
    for x in range(len(terrain)):
        for y in range(len(terrain[x])):
            px.append(x)
            py.append(y)
            pz.append(terrain[x][y])

    return px, py, pz


def cross(x0, y0, z0, x1, y1, z1, x2, y2, z2):
    """Calculates the cross product of two vectors."""
    x = y0 * (z1 - z2) + y1 * (z2 - z0) + y2 * (z0 - z1)
    y = z0 * (x1 - x2) + z1 * (x2 - x0) + z2 * (x0 - x1)
    z = x0 * (y1 - y2) + x1 * (y2 - y0) + x2 * (y0 - y1)
    return x, y, z


def norm(x, y, z):
    """Normalizes a vector."""
    l = np.sqrt(x**2 + y**2 + z**2)
    return x/l, y/l, z/l


def calculate_normal(x0, y0, z0, x1, y1, z1, x2, y2, z2):
    """Calculates the normal of a triangle."""
    x, y, z = cross(x0, y0, z0, x1, y1, z1, x2, y2, z2)
    return norm(x, y, z)


def calculate_angle_between_normals(x0, y0, z0, x1, y1, z1):
    """Calculates the angle between two vectors."""
    dot = x0 * x1 + y0 * y1 + z0 * z1
    return np.arccos(dot)


def normals(terrain_fn):
    """Calculates the normals of a terrain."""
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.set_zlim3d(-3, 3)

    n = 10
    terrain = gen_terrain(n, terrain_fn)
    px, py, pz = terrain_to_pts(terrain)
    for x in range(len(terrain) - 1):
        for y in range(len(terrain[x]) - 1):
            n = calculate_normal(
                x, y, terrain[x][y], x + 1, y, terrain[x + 1][y], x, y + 1, terrain[x][y + 1])
            theta = calculate_angle_between_normals(n[0], n[1], n[2], 0, 0, 1)
            color = theta / (np.pi / 2)
            print(color)
            ax.quiver(x + 0.5, y + 0.5, terrain[x][y], n[0], n[1], n[2],
                      length=0.5, normalize=True, color=(color, 0, 0))
    ax.scatter(px, py, pz, c="k")
    plt.show()


if __name__ == "__main__":
    for fn in TERRAIN_FNS:
        normals(fn)
