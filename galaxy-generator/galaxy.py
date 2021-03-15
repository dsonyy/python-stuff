import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
plt.style.use('dark_background')

def arc(s, e, a, b):
    s += np.random.normal() * 0.5
    e += np.random.normal() * 0.5
    c = np.random.normal(scale=1) * 1
    theta = np.arange(s, e, 0.04)

    x = a*np.cos(c + theta)*np.exp(b*theta) + np.random.normal()
    y = a*np.sin(c + theta)*np.exp(b*theta) + np.random.normal()

    return x, y, -x, -y

def galaxy(X, Y):
    N = 5
    ptsx = []
    ptsy = []
    r = 0.5
    for i, (x, y) in enumerate(zip(X, Y)):
        for j in range(N):
            ptsx.append(x + np.random.normal(scale=r))
            ptsy.append(y + np.random.normal(scale=r))
            
            ptsx[i * N + j] = x + np.random.normal(scale=r*3)
            ptsy[i * N + j] = y + np.random.normal(scale=r*3)
        r = r + 0.005
    return ptsx, ptsy

for asdf in range(1000):
    plt.subplots(figsize=(20, 20))
    for i in range(np.random.randint(1, 5)):
        s = 4.5 * np.pi
        e = 8 * np.pi
        a = 2
        b = 0.15

        x0, y0, x1, y1 = arc(s, e, a, b)
        x0, y0 = galaxy(x0, y0)
        x1, y1 = galaxy(x1, y1)

        x, y = [], []
        for i in range(np.random.randint(500, 3000)):
            x.append(np.random.normal(scale=35))
            y.append(np.random.normal(scale=35))

        for i in range(np.random.randint(500, 3000)):
            x.append(np.random.normal(scale=15))
            y.append(np.random.normal(scale=15))

        plt.scatter(x, y, marker=".", alpha=0.3, c="w")
        plt.scatter(x0, y0, marker=".", alpha=0.3, c="w")
        plt.scatter(x1, y1, marker=".", alpha=0.3, c="w")

    plt.xlim(-130, 130)
    plt.ylim(-130, 130)
    # plt.show()
    plt.axis('off')
    plt.savefig(str(asdf) + ".png", bbox_inches="tight")
    plt.savefig(str(asdf) + ".svg", bbox_inches="tight")
    print(asdf, datetime.now())