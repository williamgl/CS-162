# Author: Gan Li
# Date: 8/25/21 9:59 上午
# Description:
import turtle
import math

bob = turtle.Turtle()


def square(t, n):  # t is turtle module, n is the length. exercise 1 & 2
    t.fd(n)
    t.lt(90)
    t.fd(n)
    t.lt(90)
    t.fd(n)
    t.lt(90)
    t.fd(n)


def polygon(t, n, length, per=1.0):
    """
    t is turtle module

    n means this is a n-sided regular polygon
    The exterior angles of an n-sided regular polygon are 360/n degrees

    per is the percentage of angle/360 that we wanna display in this diagram
    This is for the arc function in circle function
    """
    angle = 360 / n
    for i in range(int(per * n)):
        t.fd(length)
        t.lt(angle)


def circle(t, r, angle=360):
    cir = int(2 * math.pi * r)
    length = 1  # This is the length of unit for the circle
    n = int(cir / length)
    per = angle / 360
    polygon(t, n, length, per)


"""
length_p = int(input('Please give a length:'))
# square(bob, length)

number = int(input('How many sides does this polygon have?'))
polygon(bob, number, length_p)
"""
radius = int(input('Please give a radius:'))
angle_c = int(input('Please give an angle:'))
# circle(bob, radius)
circle(bob, radius, angle_c)

"""
t = bob
t.fd(100)
t.lt(90)
t.bk(100)
t.rt(90)
t.pu()  # t.pd() 抬起来笔，放下笔
t.fd(100)
t.lt(90)
t.bk(100)
t.rt(90)
t.pd()
t.fd(100)
t.lt(90)
t.bk(100)
t.rt(90)
"""
turtle.mainloop()  # mainloop tells the window to wait for the user to do something
