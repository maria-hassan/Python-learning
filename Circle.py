import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

    def diameter(self):
        return 2 * self.radius


radius = float(input("Enter the value for radius"))

c = Circle(radius)
area = c.area()
circumference = c.circumference()
diameter=c.diameter()
print(area)
print(circumference)
print(diameter)
