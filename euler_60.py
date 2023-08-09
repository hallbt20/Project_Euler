from sympy import isprime, primerange
from itertools import combinations

def intersection(set1, set2):
    return [item for item in set1 if item in set2]

def concat_prime(p1, p2):
    return isprime(int(str(p1) + str(p2))) and isprime(int(str(p2) + str(p1)))

list_of_primes = [3] + list(primerange(7, 30000))

dictionary = {}

for i in range(len(list_of_primes)):
    dictionary[list_of_primes[i]] = []
    for j in range(i, len(list_of_primes)):
        if concat_prime(list_of_primes[i], list_of_primes[j]):
            dictionary[list_of_primes[i]].append(list_of_primes[j])

for num in list_of_primes:
    set1 = dictionary[num]
    if len(set1) == 0:
        break
    else:
        for num1 in set1:
            set2 = intersection(set1, dictionary[num1])
            if len(set2) == 0:
                break
            else:
                for num2 in set2:
                    set3 = intersection(set2, dictionary[num2])
                    if len(set3) == 0:
                        break
                    else:
                        for num3 in set3:
                            set4 = intersection(set3, dictionary[num3])
                            if len(set4) != 0:
                                print(num, num1, num2, num3, set4)
