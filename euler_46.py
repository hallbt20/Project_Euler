from sympy import isprime, primerange

primes = primerange(2, 100)


def goldbach(num):
    i = 1
    while 2 * pow(i, 2) + 2 <= num:
        p = num - 2 * pow(i, 2)
        if isprime(p):
            return (p, i)
        else:
            i += 1
    return False


if __name__ == '__main__':
    for i in range(4, 10000):
        k = 2 * i + 1
        if not isprime(k):
            output = goldbach(k)
            if not output:
                print(k)
                break
