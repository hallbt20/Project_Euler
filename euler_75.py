from math import isqrt
from math import gcd

dictionary = {}

test = []

for n in [num for num in range(1, 1000) if num % 2 == 1]:
    bound = (-n + isqrt(pow(n, 2) + 6000000)) // 2
    for m in [num for num in range(n + 2, bound + 1) if num % 2 == 1 and gcd(num, n) == 1]:
        L = pow(m, 2) + m * n
        if L in test:
            continue
        test.append(L)
        k = 1
        factor = L * k
        while factor <= 1500000:
            if factor in dictionary:
                dictionary[factor] += 1
            else:
                dictionary[factor] = 1
            k += 1
            factor = L * k

counter = 0

for key in dictionary:
    if dictionary[key] == 1:
        counter += 1

print(counter)
