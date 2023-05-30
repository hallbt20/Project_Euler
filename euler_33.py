def digit_cancelling(n, d):
    p = n / d

    n = [*str(n)]
    d = [*str(d)]

    if set(n).isdisjoint(d) or n[-1] == '0' or d[-1] == '0':
        return False

    for digit in n:
        if digit in d:
            n.remove(digit)
            d.remove(digit)
            break

    if int(n[0]) / int(d[0]) == p:
        return True
    else:
        return False


num = 1
den = 1

for i in range(11, 100):
    for j in range(i + 1, 100):
        if digit_cancelling(i, j):
            num *= i
            den *= j

print(num, den, num / den)
