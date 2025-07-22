#!/usr/bin/python3
Rectangle = __import__('5-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
area = my_rectangle.area()
perimeter = my_rectangle.perimeter()
print("Area: {} - Perimeter: {}".format(area, perimeter))

del my_rectangle

try:
    print(my_rectangle)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
