import numpy as np
import csv

def spec_prod(input):
    prod = 1
    for num in input:
        prod *= int(num)
    return prod

def larg_prod(input):
    prod = 0
    for i in range(0, len(input) - 3):
        if spec_prod(input[i:i+4]) > prod:
            prod = spec_prod(input[i:i+4])
    return prod

mat = np.array(list(csv.reader(open('grid.csv'))))

# Find largest rightmost product
l_right = 0
for row in range(len(mat[:,0])):
    if larg_prod(mat[row]) > l_right:
        l_right = larg_prod(mat[row])

# Find largest downwards product
l_down = 0
for col in range(len(mat[0])):
    if larg_prod(mat[:,col]) > l_down:
        l_down = larg_prod(mat[:,col])

# Find largest principal diagonal product
l_prin_diag = 0
for i in range(-16, 17):
    temp = mat.diagonal(i)
    if larg_prod(mat.diagonal(i)) > l_prin_diag:
        l_prin_diag = larg_prod(mat.diagonal(i))

# Find largest counter diagonal product
l_counter_diag = 0
mat = np.fliplr(mat)
for i in range(-16, 17):
    temp = mat.diagonal(i)
    if larg_prod(mat.diagonal(i)) > l_counter_diag:
        l_counter_diag = larg_prod(mat.diagonal(i))
print(max(l_right, l_down, l_prin_diag, l_counter_diag))
