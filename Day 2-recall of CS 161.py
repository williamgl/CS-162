# Author: Gan Li
# Date: 9/11/21 9:43 下午
# Description:
# Chapter 7 exercises
import math
from prettytable import PrettyTable as t


def my_sqrt(n):
    epsilon = 1e-16
    x = 1.0
    while True:
        # print(x)
        y = (x + n / x) / 2
        if abs(x - y) < epsilon:
            break
        x = y
    return x


def test_sqrt():
    table = t(['a', 'mysqrt(a)', 'math.sqrt(a)', 'diff'])
    for i in range(1, 10):
        i = float(i)
        table.add_row([i, my_sqrt(i), math.sqrt(i), abs(my_sqrt(i) - math.sqrt(i))])
    print(table)


if __name__ == "__main__":
    test_sqrt()
