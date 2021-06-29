import ahrs


def preprocess(ax, ay, az, gx, gy, gz):
    """
        Preprocess raw accelerometer and gyroscope data.
    """

    # TODO: calibration support

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

    return ax, ay, az, gx, gy, gz
