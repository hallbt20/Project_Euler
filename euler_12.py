from sympy.ntheory import *

def tri_num(input):
    return input*(input + 1) // 2

def num_of_factors(input):
    prod = 1
    for value in factorint(input).values():
        prod *= value + 1
    return prod

i = 1

while(num_of_factors(tri_num(i)) <= 500):
    i += 1

print(tri_num(i))
