# Author: Gan Li
# Date: 9/22/21 12:54 下午
# Description: class example
class Rectangle:
    """
    Represents a geometric rectangle.
    Contains methods for getting its area and perimeter
    """
    def __init__(self, height, width):
        self._height = height
        self._width = width     # the underscore indicates this is a private value

    def area(self):
        return self._height * self._width

    def perimeter(self):
        return (self._height + self._width) * 2


if __name__ == '__main__':
    rec = Rectangle(3, 4)
    print(rec.area())
