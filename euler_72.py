from sympy.ntheory.factor_ import totient

output = 0

for n in range(2, 1000001):
    output += totient(n)

print(output)