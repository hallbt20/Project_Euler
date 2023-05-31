from sympy import isprime

pandigital_sorted = '123456789'

def pandigital(n):
    n = str(n)
    length = len(n)
    for digit in pandigital_sorted[:length]:
        if digit not in n:
            return False
    return True

max_pandigital = 0
for x in (x for x in range(1234567, 7654322) if x % 2 and x % 5):
    if pandigital(x) and isprime(x):
        max_pandigital = x
print(max_pandigital)
