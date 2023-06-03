from time import time
start_time = time()

from math import sqrt

n = 286

while True:
    if not (1 + sqrt(1 + 12*pow(n, 2) + 12*n)) % 6:
        print(n*(n + 1) // 2)
        break
    else:
        n += 1

print("--- %s seconds ---" % (time() - start_time))
