import random
import time

while True:
    v = [random.randrange(-20000, 20000) for i in range(10)]
    print("{}\t{}\t{}\t{}\t{}\t{}".format(*v), flush=True)
    time.sleep(0.1)
