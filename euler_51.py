from itertools import combinations
from sympy import isprime

def f(a):
    output = 0
    a = [int(d) for d in str(a)]
    for k in range(1, len(a)):
        for combin in list(combinations(range(len(a) - 1), k)):
            counter = 10
            for j in range(10):
                temp = list(a)
                for i in range(0, k):
                    temp[combin[i]] = j
                num = int(''.join(map(str,temp)))
                if not isprime(num) or len(str(num)) < len(a):
                    counter -= 1
                else: 
                    pass
                if counter < 8:
                    break
            if counter == 8:
                return True
    return False

def g(a):
    a = [int(d) for d in str(a)]
    for k in range(1, len(a)):
        for combin in list(combinations(range(len(a) - 1), k)):
            counter = 10
            output = []
            for j in range(10):
                temp = list(a)
                for i in range(0, k):
                    temp[combin[i]] = j
                num = int(''.join(map(str,temp)))
                if not isprime(num) or len(str(num)) < len(a):
                    counter -= 1
                else: 
                    output.append(num)
                if counter < 8:
                    break
            if counter == 8:
                return output
    return False

output = 0
for i in range(56003, 1000000):
    if isprime(i) and f(i):
        output = i
        break
print(g(output)[0])
