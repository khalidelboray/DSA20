# here i use a function for every action just for get used to use functions :"D

import math


def triangle(n1, n2):
    print("The area of triangle: ", 0.5 * n1 * n2)


def rectangle(n1, n2):
    print("The area of rectangle: ", n1 * n2)


def square(n1):
    print("The area of square: ", n1 * n1)


def circle(n1):
    print("The area of circle: ", math.pi * (n1 / 2 * n1))


def area_shapes():
    letter = input('Letter: ')
    n1 = int(input('N1: '))
    n2 = input('N2: ')

    if letter == 't':
        triangle(n1, int(n2))
    elif letter == 'r' and not n2:
        square(n1)
    elif letter == 'r':
        rectangle(n1, int(n2))
    elif letter == 'c' and not n2:
        circle(n1)
    else:
        print('Invalid char!')


area_shapes()
