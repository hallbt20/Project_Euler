from math import isqrt
from itertools import chain

block = []

def f(a, c):
    denom = (D - pow(c, 2)) // a
    remainder = ((c + base) % denom) - base
    quotient = (c + base) // denom
    dictionary = {quotient: [denom, -1 * remainder]}
    block.append(dictionary)
    return denom, -1 * remainder

max_value = [0, 0]

for D in range(2, 1001):
    if D == isqrt(D) ** 2:
        continue

    block = []

    base = int(pow(D, .5))
    output = f(1, base)

    while True:
        output = f(output[0], output[1])
        if block[-1] in block[:-1]:
            break

    block = list(chain.from_iterable(list(x.keys()) for x in block[:-1]))

    h = [base, base * block[0] + 1]
    k = [1, block[0]]

    if pow(h[1], 2) - D * pow(k[1], 2) == 1:
        if h[1] > max_value[1]:
            max_value[0] = D
            max_value[1] = h[1]
        continue

    i = 2
    while True:
        h.append(block[(i - 1) % len(block)] * h[i - 1] + h[i - 2])
        k.append(block[(i - 1) % len(block)] * k[i - 1] + k[i - 2])
        if pow(h[i], 2) - D * pow(k[i], 2) == 1:
            break
        else:
            i += 1

    if h[-1] > max_value[1]:
        max_value[0] = D
        max_value[1] = h[-1]
print(max_value)
