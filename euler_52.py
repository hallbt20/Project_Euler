def f(n):
    standard = [digit for digit in str(2*n)]
    for i in range(3, 7):
        test = [digit for digit in str(i*n)]
        if len(standard) != len(test):
            return False
        for digit in test:
            if digit not in standard:
                return False
    return True

i = 1
while not f(i):
    i += 1
print(i)