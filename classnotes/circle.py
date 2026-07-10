import math

class Circle:
    "A circle with a 2-D center point and a radius."

    def __init__(self, x, y, radius):
        self.x = x 
        self.y = y
        self.radius = radius
    
    def area(self):
        "Return the area of the circle"
        return math.pi * (self.radius ** 2)
    
    def perimeter(self):
        "Returns the circumference of the circle"
        return math.pi * self.radius * 2

    def expand(self, factor):
        "Increases the radius by the given factor"
        self.radius *= factor
        return self

    def move(self, dx, dy):
        "Moves the center point by <dx, dy>"
        self.x += dx
        self.y += dy
        return self

    def __repr__(self):
        return f'Circle at ({self.x},{self.y}) with r={self.radius}'