import math

def circle_status(radius):
     area = math.pi * radius ** 2
     circumference = 2 * math.pi * radius
     return area, circumference


a, c = circle_status(3)

print("area :" ,math.floor(a), "curcumference :", math.floor(c))