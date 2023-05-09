from sympy import divisors

def d(n):
    if sum(divisors(n)[:-1]) > n:
        return True

    else:
        return False

abundant_numbers = [x for x in range(1,28124) if d(x)]

abundant_sums = []

for num1 in abundant_numbers:
    for num2 in abundant_numbers:
        temp = num1 + num2
        if temp > 28123:
            break
        abundant_sums.append(temp)

abundant_sums = set(abundant_sums)

print(sum([x for x in range(1, 28124) if x not in abundant_sums]))
