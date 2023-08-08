from sympy import isprime, primerange
from itertools import combinations

def concat_prime(p1, p2):
    return isprime(int(str(p1) + str(p2))) and isprime(int(str(p2) + str(p1)))

list_of_primes = list(primerange(7, 1000))

dictionary = {3 : []}

for prime in list_of_primes:
    if concat_prime(3, prime):
        dictionary[3].append(prime)

for i in range(len(list_of_primes)):
    dictionary[list_of_primes[i]] = []
    for j in range(i, len(list_of_primes)):
        if concat_prime(list_of_primes[i], list_of_primes[j]):
            dictionary[list_of_primes[i]].append(list_of_primes[j])

print(dictionary.keys())