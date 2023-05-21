from sympy import isprime

counter = [0, 0, 0]
for a in range(-999, 1000):
    for b in range(-1000, 1001):
        temp = 0
        for n in range(b):
            q = int(pow(n, 2)) + a * n + b
            if not isprime(q):
                break
            else:
                temp += 1
        if temp > counter[2]:
            counter = [a, b, temp]

print(counter)
