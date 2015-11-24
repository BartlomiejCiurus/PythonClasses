import math


class Rectangle:
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        if x1 > x2 or y1 > y2:
            raise ValueError("Błędne dane!")
        else:
            self.x1 = x1
            self.x2 = x2
            self.y1 = y1
            self.y2 = y2

    def __str__(self):
        return "[(" + str(self.x1) + ", " + str(self.y1) + "), (" + str(self.x2) + ", " + str(self.y2) + ")]"

    def __repr__(self):
        return "Rectangle(" + str(self.x1) + ", " + str(self.y1) + ", " + str(self.x2) + ", " + str(self.y2) + ")"

    def __eq__(self, other):
        return self.x1 == other.x1 and self.y1 == other.y1 and self.x2 == other.x2 and self.y2 == other.y2

    def __ne__(self, other):
        return not self == other

    def center(self):
        return (self.x1 + self.x2) / 2, (self.y1 + self.y2) / 2

    def area(self):
        a = math.fabs(self.x2 - self.x1)
        b = math.fabs(self.y2 - self.y1)
        return a * b

    def move(self, x, y):
        self.x1 = self.x1 + x
        self.y1 = self.y1 + y
        self.x2 = self.x2 + x
        self.y2 = self.y2 + y
        return self

    def make4(self):
        list_of_smaller_rectangles = []
        center_x = (self.x1 + self.x2) / 2
        center_y = (self.y1 + self.y2) / 2

        list_of_smaller_rectangles.append(Rectangle(self.x1, self.y1, center_x, center_y))
        list_of_smaller_rectangles.append(Rectangle(center_x, self.y1, self.x2, center_y))
        list_of_smaller_rectangles.append(Rectangle(self.x1, center_y, center_x, self.y2))
        list_of_smaller_rectangles.append(Rectangle(center_x, center_y, self.x2, self.y2))

        return list_of_smaller_rectangles

    def intercection(self, other):
        if other.x1 > self.x2 or other.x2 < self.x1 or other.y1 > self.y2 or other.y2 < self.y1:
            raise ValueError("Brak czesci wspolnej!")
        else:
            x0 = max(self.x1, other.x1)
            y0 = max(self.y1, other.y1)
            x1 = min(self.x2, other.x2)
            y1 = min(self.y2, other.y2)

        return Rectangle(x0, y0, x1, y1)

    def cover(self, other):
        x0 = min(self.x1, other.x1)
        y0 = min(self.y1, other.y1)
        x1 = max(self.x2, other.x2)
        y1 = max(self.y2, other.y2)

        return Rectangle(x0, y0, x1, y1)
