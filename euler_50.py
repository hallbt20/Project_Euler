from sympy import isprime, primerange

primes = list(primerange(2, 4000))

maximum = 0

def g(num):
    max_interval = 0
    counter = 0

    while num > counter:
        counter += primes[max_interval]
        max_interval += 1

    if num != counter:
        max_interval -= 1

    return max_interval

def f(num):
    max_interval = g(num)

    for i in reversed(list(range(1, max_interval + 1))):
        global maximum
        if i < maximum:
            break
        for j in range(0, len(primes) - (max_interval - 1)):
            if sum(primes[j:j + i]) > num:
                break
            elif sum(primes[j:j + i]) == num:
                if maximum < i:
                    maximum = i
                return i
            else:
                pass
    return 0

if __name__ == "__main__":
    output = [0, 0]
    for i in range(2, 1000000):
        if isprime(i) and f(i) > output[1]:
            output[0] = i
            output[1] = f(i)
    print(output)
