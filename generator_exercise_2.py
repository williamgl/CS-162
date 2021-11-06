# Author: Gan Li
# Date: 11/4/21 11:04 上午
# Description:
import math


def all_primes():
    num = 2
    while True:
        if is_prime(num):
            yield num
        # num = next_prime(num)
        num += 1


def is_prime(num):
    root = math.sqrt(num)
    test = 2
    while test <= root:
        if num % test == 0:
            return False
        test += 1
    return True


def next_prime(num):
    num += 1
    while not is_prime(num):
        num += 1
    return num
