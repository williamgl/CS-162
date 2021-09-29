# Author: Gan Li
# Date: 9/28/21 7:24 下午
# Description:
class HourlyWorker:
    """
    Represents a worker with hourly wage.
    Contains the worker's name, ID number, and hourly wage
    """
    def __init__(self, name, ID, wage):
        self._name = name
        self._ID = ID
        self._wage = wage


class Box:
    """
    Represents a box with its length, width, and height.
    Contains methods to calculate its volume and surface area.
    """
    def __init__(self, length, width, height):
        self._length = length
        self._width = width
        self._height = height

    def volume(self):
        return self._height * self._width * self._length

    def surface_area(self):
        return 2 * (self._height * self._width + self._width * self._length
                    + self._length * self._height)


class OutOfRangeError(Exception):
    pass


def name_the_number():
    number = int(input('type in an integer:'))
    if number == 1:
        print('one')
    elif number == 2:
        print('two')
    elif number == 3:
        print('three')
    else:
        raise OutOfRangeError


if __name__ == '__main__':
    try:
        name_the_number()
    except OutOfRangeError:
        print("That's not one of the allowed values!")


def multiply_3_numbers(a, b, c):
    return a * b * c
