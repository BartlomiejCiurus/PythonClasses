from math import pi
from math import sqrt


class Circle:
    def __init__(self, x=0, y=0, radius=1):
        if radius < 0:
            raise ValueError("promień ujemny")
        self.x = x
        self.y = y
        self.radius = radius

    def __repr__(self):
        return "Circle(" + str(self.x) + ", " + str(self.y) + ", " + str(self.radius) + ")"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def area(self):
        return pi * pow(self.radius, 2)

    def move(self, x, y):
        self.x = self.x + x
        self.y = self.y + y

    def cover(self, other):
        length_beetwen_points = sqrt(pow(self.x - other.x, 2) + pow(self.y - other.y, 2))
        radius = length_beetwen_points + (self.radius / 2) + (other.radius / 2)
        return Circle((self.x + other.x) / 2, (self.y + other.y) / 2, radius)
