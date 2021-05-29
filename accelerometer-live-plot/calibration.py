import sys
import numpy as np

N = 100

data = np.empty((0, 6))
for i in range(N):
    line = [int(i) for i in input().split()]
    data = np.append(data, (line,), 0)
    print("Read {}/{} lines.".format(i + 1, N), file=sys.stderr, flush=True)

print("Mean: ", *np.mean(data, 0))
print("Median: ", *np.median(data, 0))
print("Standard Deviation: ", *np.std(data, 0))

