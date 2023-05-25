max_values = [200, 100, 40, 20, 10, 4, 2, 1]


def set_pence(x):
    return 200 - 2 * x[1] - 5 * x[2] - 10 * x[3] - 20 * x[4] - 50 * x[5] - 100 * x[6] - 200 * x[7]


def rounding(x):
    for i in range(len(x) - 1):
        if x[i] == max_values[i] + 1:
            x[i] = 0
            x[i + 1] += 1
    return x


def next_number(x):
    x[1] += 1
    x = rounding(x)
    x[0] = set_pence(x)
    while x[0] < 0:
        x[1] = 101
        rounding(x)
        x[0] = set_pence(x)
    return x


def counter():
    x = [200, 0, 0, 0, 0, 0, 0, 0]
    count = 1
    while x[7] != 1:
        x = next_number(x)
        count += 1
    return count
