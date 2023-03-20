class Circle:
def __init__(self, radius):
self.radius = radius
def area(self):
"""
Computes the area of the circle.
"""
return 3.14 * (self.radius ** 2)
def perimeter(self):
"""
Computes the perimeter (circumference) of the circle.
"""
return 2 * 3.14 * self.radius