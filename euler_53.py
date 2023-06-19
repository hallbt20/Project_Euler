from scipy.special import binom

def f(n):
    output = 0
    for r in range(4, n - 3):
        if binom(n, r) > 1000000:
            output += 1
    return output

output = 0

for i in range(23, 101):
    output += f(i)

print(output)
