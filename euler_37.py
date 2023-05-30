from sympy import isprime


def truncated_values(n):
    output = [n]

    n = str(n)
    while len(n) != 1:
        n = n[1:]
        output.append(int(n))

    n = str(output[0])
    while len(n) != 1:
        n = n[:-1]
        if n not in output:
            output.append(int(n))

    return output


def truncated_prime(n):
    for digit in str(n)[1:]:
        if not int(digit) % 2:
            return False

    for num in truncated_values(n):
        if not isprime(num):
            return False

    return True


output = []
for i in range(11, 1000000):
    if truncated_prime(i):
        output.append(i)
print(sum(output))
