from unittest import TestCase

from Exceptions.circle import Circle
from math import pi


class TestCircle(TestCase):
    def testArea(self):
        self.assertEqual(Circle(1, 2, 1).area(), pi)
        self.assertEqual(Circle(2, 3, 5).area(), pi * 25)

    def testMove(self):
        self.assertEqual(Circle(1, 2, 1).move(10, 10), Circle(11, 12, 3))
        self.assertEqual(Circle(2, 3, 5).move(-2, -3), Circle(0, 0, 1))

    def testCover(self):
        self.assertEqual(Circle(1, 1, 3).cover(Circle(1, 2, 3)), Circle(1, 1.5, 4.0))
        self.assertEqual(Circle(1, 10, 15).cover(Circle(1, 20, 10)), Circle(1.0, 15.0, 22.5))

    def testInit(self):
        with self.assertRaises(ValueError):
            Circle(1, 1, -1)
        circle_example = Circle(1, 1, 1)
        self.assertEqual((circle_example.x, circle_example.y, circle_example.radius), (1, 1, 1))

    def testRepr(self):
        self.assertEqual(repr(Circle(1, -1, 1)), "Circle(1, -1, 1)")
        self.assertEqual(repr(Circle(-2, -3, 1)), "Circle(-2, -3, 1)")

    def testEq(self):
        self.assertTrue(Circle(-15, 31, 512) == Circle(-15, 31, 512))
        self.assertFalse(Circle(-15, 31, 512) == Circle(-15, 31, 412))
        self.assertFalse(Circle(-15, 421, 512) == Circle(-15, 31, 512))

    def testNeEq(self):
        self.assertFalse(Circle(-15, 31, 512) != Circle(-15, 31, 512))
        self.assertTrue(Circle(-15, 31, 512) != Circle(-15, 31, 412))
        self.assertTrue(Circle(-15, 421, 512) != Circle(-15, 31, 512))
