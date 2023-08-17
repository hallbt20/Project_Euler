from math import isqrt

block = []

def is_square(i: int) -> bool:
    return i == isqrt(i) ** 2

def f(a, c):
    denom = (radicand - pow(c, 2)) // a
    remainder = ((c + base) % denom) - base
    quotient = (c + base) // denom
    dictionary = {quotient: [denom, -1 * remainder]}
    block.append(dictionary)
    return denom, -1 * remainder

counter = 0

for radicand in range(2, 10001):
    if is_square(radicand):
        continue

    block = []

    base = int(pow(radicand, .5))
    output = f(1, base)

    while True:
        output = f(output[0], output[1])
        if block[-1] in block[:-1]:
            break

    if len(block[:-1]) % 2 == 1:
        counter += 1
print(counter)
