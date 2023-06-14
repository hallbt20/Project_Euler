from sympy import factorint

def distinct_primes(n):
    orig_factors = factorint(n)
    k = 4

    if len(orig_factors.keys()) != k:
        return False

    for i in range(1, k):
        new_factors = factorint(n + i)
        if len(new_factors.keys()) != k:
            return False
        for p in new_factors.keys():
            if p in orig_factors.keys():
                if orig_factors[p] == new_factors[p]:
                    return False

    return True

if __name__ == '__main__':
    i = 1
    while True:
        temp = distinct_primes(i)
        if temp:
            print(i)
            break
        else:
            i += 1