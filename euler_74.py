from math import factorial 

def f(n):
    return sum([factorial(int(d)) for d in str(n)])

def g(n):
    queue = [n]
    temp = f(n)
    
    whlie temp not in queue:
        queue.append(temp)
        temp = f(temp)
    
    return len(queue)

counter = 0

for i in range(1000000):
    if g(i) == 60:
        counter += 1

print(counter)
