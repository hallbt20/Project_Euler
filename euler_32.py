d = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


def pandigital_product(i, j):
    digits = str(i) + str(j) + str(i*j)
    if sorted(digits) == d:
        return True
    else:
        return False

temp = []

for i in range(1, 100):
    for j in range(pow(10, 4 - len(str(i))), 9999//i):
        if pandigital_product(i, j) and i*j not in temp:
            temp.append(i*j)

print(sum(temp))