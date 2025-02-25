import math

class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * (self.radius **2)

Rectangle=Rectangle(10,20)
circle=Circle(10)

print(f"Area of rectangle: {Rectangle.area()}")
print(f"Area of circle: {circle.area()}")


