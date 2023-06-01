from math import sqrt

def sub_pent(i, j):
    k = 1 - 12*(3*pow(j, 2) - 6*j*i + j)
    if k >= 0:
        k = sqrt(k)
        if k % 1 == 0 and (k + 1) % 6 == 0:
            return True
    return False

def add_pent(i, j):
    k = sqrt(1 + 12*(3*pow(j, 2) - 6*j*i + j + 6*pow(i, 2) - 2*i))
    if k % 1 == 0 and (k + 1) % 6 == 0:
        return True
    return False

def pent(i, j):
    return sub_pent(i, j) and add_pent(i, j)

for i in range(2, k):
    for j in range(1, i - 1):
        if pent(i, j):
            print(i*(3*i - 1) // 2 - (i - j)*(3*(i - j) - 1) // 2)
            break
    else:
        continue
    break
