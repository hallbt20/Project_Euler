import numpy as np

def f(row1, row2):
    temp = [[] for i in range(len(row2))]

    if len(row1) == 1:
        row1 = [row1]

    for i in range(len(row1)):
        for num in row1[i]:
            temp[i].append(num + row2[i])
            temp[i + 1].append(num + row2[i + 1])

    return temp

with open('num.txt') as file:
    rows = [row.rstrip().split(' ') for row in file]

for row in rows:
    for i in range(len(row)):
        row[i] = int(row[i])

row1 = rows[0]

for i in range(len(rows) - 1):
    row2 = rows[i + 1]
    row1 = f(row1, row2)

row1 = list(np.concatenate(row1).flat)
