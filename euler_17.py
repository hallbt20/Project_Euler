def f(x):
    if x == 0:
        return 0
    elif x == 1 or x == 2 or x == 6 or x == 10:
        return 3
    elif x == 4 or x == 5 or x == 9:
        return 4
    elif x == 3 or x == 7 or x == 8:
        return 5
    elif x == 11 or x == 12:
        return 6
    elif x == 15 or x == 16:
        return 7
    elif x == 13 or x == 14 or x == 18 or x == 19:
        return 8
    elif x == 17:
        return 9
    elif x == 1000:
        return 11
    elif (x >= 40 and x < 70):
        return 5 + f(x % 10)
    elif (x >= 20 and x < 40) or (x >= 80 and x < 100):
        return 6 + f(x % 10)
    elif (x >= 70 and x < 80):
        return 7 + f(x % 10)
    elif (x % 100 != 0):
        return f(x // 100) + 10 + f(x % 100)
    else:
        return f(x // 100) + 7 + f(x % 100)
