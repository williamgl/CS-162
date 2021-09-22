# Author: Gan Li
# Date: 9/22/21 11:56 上午
# Description: testing modules
# import test

# print(test.linecount('2021_09_22_module.py'))
# from test import linecount as lc

# print(lc('2021_09_22_module.py'))
from math import sqrt


def distance(x1, y1, x2, y2):
    return int(sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2))


if __name__ == '__main__':
    d = distance(3, 5, -1, 2)
