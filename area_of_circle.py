print('Hello and welcome to this area calculator for a circle')
radius = float(input('Please enter the radius of the circle -> ' ))
import math

def area_of_circle(radius):
 area = 2 * math.pi * radius
 print('The area of the cirle is ' + str(area))

area_of_circle(radius)
