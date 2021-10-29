# Author: Gan Li
# Date: 10/28/21 4:40 下午
# Description: Module 6 recursions
def rec_binary_search(a_list, target, first, last):
    """
    Searches a_list for an occurrence of target
    If found, returns the index of its position in the list
    If not found, returns -1, indicating the target value isn't in the list
    """
    if first > last:
        return -1
    middle = (first + last) // 2
    if a_list[middle] == target:
        return middle
    if a_list[middle] > target:
        return rec_binary_search(a_list, target, first, middle-1)
    else:
        return rec_binary_search(a_list, target, middle+1, last)


def binary_search(a_list, target):
    return rec_binary_search(a_list, target, 0, len(a_list)-1)


my_list = [5, 10, 32, 98, 67, 112, 113]
print(binary_search(my_list, 112))
