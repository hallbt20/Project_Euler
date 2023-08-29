from math import gcd
from sympy import factorint

def totient(n):
    output = 1

    factorization = factorint(n)

    for p in factorization.keys():
        output *= (p - 1) * pow(p, factorization[p] - 1)

    return output

max = [0, 0]

for n in range(2, 1000001):
    t = n / totient(n)
    if t > max[1]:
        max[0] = n
        max[1] = t

print(max)