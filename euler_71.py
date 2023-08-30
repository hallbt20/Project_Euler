from math import floor, gcd

min_diff = [0, 0, 1]

top_denom = 1000001

for d in range(8, top_denom):
    n = floor(d * (3 / 7))

    while True:
        if gcd(n, d) == 1:
            break
        n -= 1

    diff = 3 / 7 - n / d
    if diff < min_diff[2]:
        min_diff[0] = n
        min_diff[1] = d
        min_diff[2] = diff

print(min_diff)
