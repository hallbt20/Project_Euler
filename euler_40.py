pow_of_ten = [pow(10, n) for n in range(7)]

def champernowne():
    output = []
    counter = 0
    i = 1
    while counter < 1000000:
        for digit in str(i):
            counter += 1
            if counter in pow_of_ten:
                output.append(int(digit))
        i += 1
    return output

temp = 1
for num in champernowne():
    temp *= num
print(temp)