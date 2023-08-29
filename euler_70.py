from sympy.ntheory.factor_ import totient

def perm(m, n):
    return sorted(str(m)) == sorted(str(n))

minimum = [0, 10000000]

for n in range(2, 10000001):
    if perm(n, totient(n)) and n / totient(n) < minimum[1]:
        t = n / totient(n)
        minimum = [n, t]

print(minimum)
