from math import factorial

num = ''
numbers = [x for x in range(10)]
placement = 1

while len(numbers) != 1:
    for i in range(len(numbers)):
        if placement + factorial(len(numbers) - 1) > 1000000:
            num += str(numbers[i])
            numbers.remove(numbers[i])
            break
        else:
            placement += factorial(len(numbers) - 1)

print(num)
