def palindromic(n):
    return str(n) == str(n)[::-1]

output = []
for i in range(1, 1000000):
    if palindromic(i) and palindromic(bin(i)[2:]):
        output.append(i)

print(sum(output))