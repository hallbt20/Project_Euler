max_values = [200, 100, 40, 20, 10, 4, 2, 1]


def next_number(x):
    x[1] += 1
    for i in range(len(x) - 1):
        if x[i] == max_values[i] + 1:
            x[i] = 0
            x[i + 1] += 1
    x[0] = 200 - 2 * x[1] - 5 * x[2] - 10 * x[3] - 20 * x[4]
    if x[0] < 0:
        temp = 0
        for i in reversed(x):
            if x[i] != 0:
                x[i] += 1
                temp = i
                break
        for i in range(len(x) - temp):
            x[i] = 0
    return x

def carry_over(money):
    if money[0] < 0:
        temp = 0
        for i in range(len(money) - 1):
            if money[len(money) - (i + 1)] != 0:
                money[i] += 1
                temp = i - 1
                break
        for i in range(temp):
            money[i] = 0
    else:
        money[0] = 0
        money[1] += 1

    for i in range(1, len(money) - 1):
        if money[i] == max_values[i] + 1:
            money[i] = 0
            money[i + 1] += 1
    return money
