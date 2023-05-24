max_values = [200, 100, 40, 20, 10, 4, 2, 1]


def carry_over(money):
    if money[0] < 0:
        for i in range(len(money) - 1):
            if money[i + 1] != 0:
                money[i] = 0
            else:
                money[i] += 1
                break
    else:
        money[0] = 0
        money[1] += 1

    for i in range(1, len(money) - 1):
        if money[i] == max_values[i] + 1:
            money[i] = 0
            money[i + 1] += 1
    return money
