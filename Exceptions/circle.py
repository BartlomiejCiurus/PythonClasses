from collections.__main__ import Point
from math import pi
from math import sqrt


class Circle:
    def __init__(self, x=0, y=0, radius=1):
        if radius < 0:
            raise ValueError("promień ujemny")
        self.pt = Point(x, y)
        self.radius = radius

    def __repr__(self):
        return "Circle(" + str(self.pt.x) + ", " + str(self.pt.y) + ", " + str(self.radius) + ")"

    def __eq__(self, other):
        return self.pt.x == other.pt.x and self.pt.y == other.pt.y and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def area(self):
        return pi * pow(self.radius, 2)

    def move(self, x, y):
        self.pt.x = self.pt.x + x
        self.pt.y = self.pt.y + y

    def cover(self, other):
        length_beetwen_points = sqrt(pow(self.pt.x - other.pt.x, 2) + pow(self.pt.y - other.pt.y, 2))
        radius = length_beetwen_points + (self.radius / 2) + (other.radius / 2)
        return Circle((self.pt.x + other.pt.x) / 2, (self.pt.y + other.pt.y) / 2, radius)
