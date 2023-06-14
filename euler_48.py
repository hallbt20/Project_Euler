from sympy import isprime
from itertools import permutations

def prime_permutations(i):
    perms = list(set([int(''.join(num)) for num in list(permutations(str(i)))]))
    perms = [x for x in perms if isprime(x) and len(str(x)) == 4]
    perms.sort()
    if len(perms) >= 3:
        for num in perms:
            if num + 3330 in perms and num + 2*3330 in perms:
                return [num, num + 3330, num + 3330*2]
    return False

if __name__ == '__main__':
    output = []
    for i in range(1001, 9999):
        p_list = prime_permutations(i)
        if not p_list:
            pass
        else:
            if p_list not in output:
                output.append(prime_permutations(i))
    print(output)
