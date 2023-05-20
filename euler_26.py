def length_of_repeating_decimal(n):
    stack = []
    temp = []
    r = 10
    
    while r < n:
            r *= 10
            stack.append(0)
            temp.append(0)
    
    temp.append(r // n)
    r = r % n
    
    while r not in stack:
            if r == 0:
                    return 0
    
            else:
                    stack.append(r)
                    r *= 10
                    while r < n:
                            r *= 10
                            stack.append(0)
                            temp.append(0)
                    temp.append(r // n)
                    r = r % n
    
    return len(stack) - stack.index(r)

max = [0, 0]
for i in range(2, 1000):
    if length_of_repeating_decimal(i) > max[1]:
        max[0] = i
        max[1] = length_of_repeating_decimal(i)

print(max[0])
