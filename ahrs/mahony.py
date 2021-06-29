import numpy as np
import ahrs

mahony = ahrs.filters.Mahony()

Q = np.array([1., 0., 0., 0.])
while True:
    ax, ay, az, gx, gy, gz = (float(v) for v in input().split())

    # Raw values from MPU-6050 have to be divided by a constant value
    # depending on the chosen sensitivity. More details in MPU documentation.
    ax /= 16384.0
    ay /= 16384.0
    az /= 16384.0
    gx /= 131.0
    gy /= 131.0
    gz /= 131.0

    # MPU-6050 accel values have to be multiplied by g to get m/s^2
    ax = ax * ahrs.MEAN_NORMAL_GRAVITY
    ay = ay * ahrs.MEAN_NORMAL_GRAVITY
    az = az * ahrs.MEAN_NORMAL_GRAVITY
    # MPU-6050 gyro values have to be converted from deg/s to rad/s
    gx = gx * ahrs.DEG2RAD
    gy = gy * ahrs.DEG2RAD
    gz = gz * ahrs.DEG2RAD

    a = np.array((ax, ay, az))
    g = np.array((gx, gy, gz))
    mahony.updateIMU(q=Q, acc=a, gyr=g)

    print(Q[0] * 180, Q[1], Q[2], Q[3], sep="\t", flush=True)
