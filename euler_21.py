from sympy import divisors

def d(n):
    return sum(divisors(n)[:-1])

sum = 0

for i in range(2, 10000):
    if d(d(i)) == i and i != d(i):
        sum += i
