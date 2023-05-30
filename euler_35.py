from sympy import isprime


def rotations(n):
    output = []
    n = str(n)
    temp = n

    while len(output) == 0 or int(temp) != output[0]:
        output.append(int(temp))
        n = str(temp)
        temp = ''
        for i in range(len(n)):
            temp += n[(i + 1) % len(n)]

    return output


def circular_prime(n):
    if n == 2:
        return True

    for digit in str(n):
        if not int(digit) % 2:
            return False

    for num in rotations(n):
        if not isprime(num):
            return False

    return True


output = []
for i in range(1000000):
    if i in output:
        continue
    else:
        if circular_prime(i):
            for num in rotations(i):
                output.append(num)

print(len(output))
