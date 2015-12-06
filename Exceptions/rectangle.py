from collections.__main__ import Point
import math


class Rectangle:
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        if x1 > x2 or y1 > y2:
            raise ValueError("Błędne dane!")
        else:
            self.pt1 = Point(x1, y1)
            self.pt2 = Point(x2, y2)

    def __str__(self):
        return "[(" + str(self.pt1.x) + ", " + str(self.pt1.y) + "), (" + str(self.pt2.x) + ", " + str(self.pt2.y) + ")]"

    def __repr__(self):
        return "Rectangle(" + str(self.pt1.x) + ", " + str(self.pt1.y) + ", " + str(self.pt2.x) + ", " + str(self.pt2.y) + ")"

    def __eq__(self, other):
        return self.pt1.x == other.x1 and self.pt1.y == other.y1 and self.pt2.x == other.x2 and self.pt2.y == other.y2

    def __ne__(self, other):
        return not self == other

    def center(self):
        return Point((self.pt1.x + self.pt2.x) / 2, (self.pt1.y + self.pt2.y) / 2)

    def area(self):
        a = math.fabs(self.pt2.x - self.pt1.x)
        b = math.fabs(self.pt2.y - self.pt1.y)
        return a * b

    def move(self, x, y):
        self.pt1.x = self.pt1.x + x
        self.pt1.y = self.pt1.y + y
        self.pt2.x = self.pt2.x + x
        self.pt2.y = self.pt2.y + y
        return self

    def make4(self):
        list_of_smaller_rectangles = []
        center_x = (self.pt1.x + self.pt2.x) / 2
        center_y = (self.pt1.y + self.pt2.y) / 2

        list_of_smaller_rectangles.append(Rectangle(self.pt1.x, self.pt1.y, center_x, center_y))
        list_of_smaller_rectangles.append(Rectangle(center_x, self.pt1.y, self.pt2.x, center_y))
        list_of_smaller_rectangles.append(Rectangle(self.pt1.x, center_y, center_x, self.pt2.y))
        list_of_smaller_rectangles.append(Rectangle(center_x, center_y, self.pt2.x, self.pt2.y))

        return list_of_smaller_rectangles

    def intercection(self, other):
        if other.x1 > self.pt2.x or other.x2 < self.pt1.x or other.y1 > self.pt2.y or other.y2 < self.pt1.y:
            raise ValueError("Brak czesci wspolnej!")
        else:
            x0 = max(self.pt1.x, other.x1)
            y0 = max(self.pt1.y, other.y1)
            x1 = min(self.pt2.x, other.x2)
            y1 = min(self.pt2.y, other.y2)

        return Rectangle(x0, y0, x1, y1)

    def cover(self, other):
        x0 = min(self.pt1.x, other.x1)
        y0 = min(self.pt1.y, other.y1)
        x1 = max(self.pt2.x, other.x2)
        y1 = max(self.pt2.y, other.y2)

        return Rectangle(x0, y0, x1, y1)
