with open('0067_triangle.txt') as file:
    rows = [row.rstrip().split(' ') for row in file]

for row in rows:
    for i in range(len(row)):
        row[i] = int(row[i])

for i in reversed(range(len(rows) - 1)):
    for j in range(len(rows[i])):
        rows[i][j] += max(rows[i + 1][j], rows[i + 1][j + 1])

print(rows)