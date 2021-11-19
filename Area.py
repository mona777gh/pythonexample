from math import pi
def area(radius):
    if radius < 0:
        raise ValueError("the radius can not be negative")
    return pi * (radius**2)
def square(n):
    return n*n





