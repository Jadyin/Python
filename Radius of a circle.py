#Accepts the radius of a circle and then prints the area of the circle
#By Jakob Delaney

import math

print("Hello Welcome to Area solver for a circle")
radius = input("Please input a float value larger than 0. \n")
radius = float(radius)
Area = math.pi*pow(radius, 2)

if radius > 0:
    print("Area =", Area, "\n")
elif radius <= 0:
    print("Sorry please print a number greater than 0")
else:
    print("Sorry invalid input")

