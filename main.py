# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from new import *

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    x = [0, 0, 0, 0, 0]
    counter = 0
    while x[4] != 1:
        x[0] = 200 - 2*x[1] - 5*x[2] - 10*x[3]
        if x[0] >= 0:
            print(x)
            counter += 1
        carry_over(x)
        print(x)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
