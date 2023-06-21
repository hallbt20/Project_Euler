def f(num, den):
    return [num + 2*den, num + den]

counter = 0

start = [3, 2]

for i in range(1001):
    if len(str(start[0])) > len(str(start[1])):
        counter += 1
    start = f(start[0], start[1])

print(counter)
