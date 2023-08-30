from math import ceil, floor, gcd

output = 0

for d in range(4, 12001):
    lower = ceil((1 / 3) * d)
    upper = floor((1 / 2) * d)
    for n in range(lower, upper + 1):
        if gcd(n, d) == 1:
            output += 1

print(output)
