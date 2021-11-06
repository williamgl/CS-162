# Author: Gan Li
# Date: 11/4/21 10:44 上午
# Description: module 8 generators and decorators
def even_numbers(limit):
    num = 0
    while num < limit:
        yield num
        num += 2


