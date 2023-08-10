def is_perm(n1, n2):
    return sorted(str(n1)) == sorted(str(n2))

list_of_cubes = [pow(n, 3) for n in range(345, 10000)]

for i in range(len(list_of_cubes)):
    counter = 0
    for j in range(i + 1, len(list_of_cubes)):
        if is_perm(list_of_cubes[i], list_of_cubes[j]):
            counter += 1
        if counter == 4:
            print(list_of_cubes[i])
            break


