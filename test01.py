# Author: Gan Li
# Date: 9/22/21 11:57 上午
# Description:
from a2021_09_22_module import distance


def linecount(filename):
    count = 0
    for line in open(filename):
        count += 1
    return count


if __name__ == '__main__':
    linecount('test01.py')
    d = distance(3, 5, -1, 2)
    print(d)
