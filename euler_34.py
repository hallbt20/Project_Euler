from math import factorial


def digit_factorial(n):
    return sum([factorial(int(digit)) for digit in [*str(n)]]) == n


for i in range(100000):
    if digit_factorial(i):
        print(i)