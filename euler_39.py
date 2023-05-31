def num_right_triangles(p):
    if p % 2:
        return 0
    output = 0
    for a in range(1, p):
        for b in range(a, p):
            if pow(p, 2) == 2*(p*a + p*b - a*b) and a + b < p:
                output += 1
    return output

max_perimeter = [0, 0]
for i in range(1, 1001):
    print(i)
    temp = num_right_triangles(i)
    if temp > max_perimeter[1]:
        max_perimeter[0] = i
        max_perimeter[1] = temp
print(max_perimeter)
