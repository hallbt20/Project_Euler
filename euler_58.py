from sympy import isprime

def f():
    num = 3
    den = 5
    i = 1

    while num / den > .1:
        i += 1
        side_length = 2 * i + 1
        num1 = pow(side_length, 2) - (side_length - 1)
        num2 = num1 - (side_length - 1)
        num3 = num2 - (side_length - 1)

        list_diags = [num1, num2, num3]

        num += sum([isprime(num) for num in list_diags])
        den += 4

    return 2*i + 1

print(f())