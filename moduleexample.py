import math
from math import pi
from math import e

a,b,c = 1,2,3

print(e ** a)
print(e ** b)
print(e ** c)

pi = 3.14159

def square(x):
    return x**2

def cube(x):
    return x**3

def sphere(r):
    return pi*(r**2)

def cylinder(r,h):
    return 2*pi*r*h + 2*sphere(r)

def cone(r,h):
    return pi*r**2 + sphere(r) + cylinder(r,h)

def sphere_volume(r):
    return pi*(r**3)/3

def cylinder_volume(r,h):
    return pi*(r**2)*h

def cone_volume(r,h):
    return pi*(r**2)*h/3 + sphere_volume(r)

def sphere_surface_area(r):
    return 4*pi*r

def cylinder_surface_area(r,h):
    return 2*pi*r*h + 2*sphere_surface_area(r)

def circumference(r):
    return 2*pi*r

def area(r):
    return pi*r**2
