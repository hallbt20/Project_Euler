def f(n):
    reversed_n = int(str(n)[::-1])
    return n + reversed_n

def palindromic(n):
    return n == int(str(n)[::-1])

def is_lychrel(n):
    for i in range(50):
        n = f(n)
        if palindromic(n):
            return True
    return False

counter = 0

for num in range(10000):
    if not is_lychrel(num):
        counter += 1

print(counter)