#for i in range(9, 10000):
pandigital = '123456789'

def pandigital_multiple(num):
    temp = str(num)
    for n in range(2, 7):
        temp += str(num*n)
        if len(temp) > 9:
            return False
        elif len(temp) < 9:
            continue
        elif len(temp) == 9 and ''.join(sorted(temp)) == pandigital:
            return int(temp)
    return temp

max_pan = 0
for i in range(9, 10000):
    temp = pandigital_multiple(i)
    if temp > max_pan:
        max_pan = temp

print(max_pan)
