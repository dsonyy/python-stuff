import numpy as np
import ahrs

mahony = ahrs.filters.Mahony()

Q = np.array([1., 0., 0., 0.])
while True:
    ax, ay, az, gx, gy, gz = (float(v) for v in input().split())
    a = np.array((ax, ay, az))
    g = np.array((gx, gy, gz))

    mahony.updateIMU(q=Q, acc=a, gyr=g)
    print(Q[0] * 180, Q[1], Q[2], Q[3], sep="\t", flush=True)
