def exponent(a, b):
    return sum([int(num) for num in list(str(pow(a, b)))])

maximum = 0

for a in range(1, 100):
    for b in range(1, 100):
        if maximum < exponent(a, b):
            maximum = exponent(a, b)

print(maximum)