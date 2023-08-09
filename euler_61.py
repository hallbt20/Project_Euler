from math import isqrt
from itertools import chain

def is_square(i: int) -> bool:
    return i == isqrt(i) ** 2


def is_tri(n):
    return is_square(1 + 8 * n) and (-1 + isqrt(1 + 8 * n)) % 2 == 0


def is_pent(n):
    return is_square(1 + 24 * n) and (1 + isqrt(1 + 24 * n)) % 6 == 0


def is_hex(n):
    return is_tri(n) and (1 + isqrt(1 + 8 * n)) % 4 == 0


def is_hep(n):
    return is_square(9 + 40 * n) and (3 + isqrt(9 + 40 * n)) % 10 == 0


def is_oct(n):
    return is_square(4 + 12 * n) and (2 + isqrt(4 + 12 * n)) % 6 == 0

dictionary = {
    'tri': [],
    'square': [],
    'pent': [],
    'hex': [],
    'hep': [],
    'oct': []
}

for n in range(1000, 10000):
    if is_tri(n) and n % 100 // 10 != 0:
        dictionary['tri'].append(n)
    if is_square(n) and n % 100 // 10 != 0:
        dictionary['square'].append(n)
    if is_pent(n) and n % 100 // 10 != 0:
        dictionary['pent'].append(n)
    if is_hex(n) and n % 100 // 10 != 0:
        dictionary['hex'].append(n)
    if is_hep(n) and n % 100 // 10 != 0:
        dictionary['hep'].append(n)
    if is_oct(n) and n % 100 // 10 != 0:
        dictionary['oct'].append(n)

def cyclic(num, output = None):
    l = []
    if output is None:
        output = {'oct': num}
    for key in dictionary.keys():
        if key in output.keys():
            continue
        else:
            for num1 in dictionary[key]:
                if num % 100 == num1 // 100:
                    output1 = output.copy()
                    output1[key] = num1
                    l.append(output1)
    return l

def cyclic_test(list_values):
    m = []
    for l in list_values:
        m.append(cyclic(list(l.values())[-1], l))
    m = list(chain.from_iterable(m))
    try:
        if len(m[0].keys()) == 6:
            return m
    except:
        return m
    return cyclic_test(m)


final = []

for temp in dictionary['oct']:
    final.append(cyclic_test(cyclic(temp)))

final = list(chain.from_iterable(final))

counter = 0

for val in final:
    if list(val.values())[-1] % 100 == list(val.values())[0] // 100:
        print(sum(val.values()))


