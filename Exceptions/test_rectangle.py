from collections.__main__ import Point
from unittest import TestCase
from Exceptions.rectangle import Rectangle


class TestRectangle(TestCase):
    def testInit(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 1, 3, -5)
        rectangle_example = Rectangle(2, 5, 3, 6)
        self.assertEqual((rectangle_example.pt1.x, rectangle_example.pt1.y, rectangle_example.pt2.x, rectangle_example.pt2.y),
                         (2, 5, 3, 6))

    def testStr(self):
        self.assertEqual(str(Rectangle(1, 21, 51, 463)), "[(1, 21), (51, 463)]")
        self.assertEqual(str(Rectangle(-31, 0, 3, 15)), "[(-31, 0), (3, 15)]")

    def testRepr(self):
        self.assertEqual(repr(Rectangle(1, 21, 51, 463)), "Rectangle(1, 21, 51, 463)")
        self.assertEqual(repr(Rectangle(-31, 0, 3, 15)), "Rectangle(-31, 0, 3, 15)")
        self.assertEqual(repr(Rectangle(-31.5, 0, 3, 15)), "Rectangle(-31.5, 0, 3, 15)")

    def testEq(self):
        self.assertFalse(Rectangle(-31, 0, 3, 15) == Rectangle(-31, 0, 3, 14))
        self.assertFalse(Rectangle(-31, 0, 3, 15) == Rectangle(-31, 4, 3, 15))
        self.assertTrue(Rectangle(-31, 0, 3, 15) == Rectangle(-31, 0, 3, 15))

    def testNe(self):
        self.assertFalse(Rectangle(-31, 0, 3, 15) != Rectangle(-31, 0, 3, 15))
        self.assertTrue(Rectangle(-31, 0, 3, 15) != Rectangle(-31, 0, 3, 14))

    def testCenter(self):
        self.assertEqual(Rectangle(-31, 0, 3, 15).center(), Point(-14.0, 7.5))
        self.assertEqual(Rectangle(-31.5, 0, 3, 15).center(), Point(-14.25, 7.5))

    def testArea(self):
        self.assertEqual(Rectangle(-31, 0, 3, 15).area(), 510.0)
        self.assertEqual(Rectangle(1, 21, 51, 463).area(), 22100.0)

    def testMove(self):
        self.assertEqual(Rectangle(-31, 0, 3, 15).move(-2, 2), Rectangle(-33, 2, 1, 17))
        self.assertEqual(Rectangle(1, 21, 51, 463).move(5, 4), Rectangle(6, 25, 56, 467))

    def testMake4(self):
        self.assertEqual(Rectangle(-31, 0, 3, 15).make4(),
                         [Rectangle(-31, 0, -14.0, 7.5), Rectangle(-14.0, 0, 3, 7.5), Rectangle(-31, 7.5, -14.0, 15),
                          Rectangle(-14.0, 7.5, 3, 15)])
        self.assertEqual(Rectangle(-4, -8, -1, -3).make4(),
                         [Rectangle(-4, -8, -2.5, -5.5), Rectangle(-2.5, -8, -1, -5.5), Rectangle(-4, -5.5, -2.5, -3),
                          Rectangle(-2.5, -5.5, -1, -3)])

    def testIntersection(self):
        with self.assertRaises(ValueError):
            Rectangle(-5, 3, 6, 4).intercection(Rectangle(7, -12, 53, 67))
        self.assertEqual(Rectangle(-1, 0, 1, 2).intercection(Rectangle(0, -2, 2, 1)), Rectangle(0, 0, 1, 1))

    def testCover(self):
        self.assertEqual(Rectangle(1, 1, 2, 2).cover(Rectangle(1, 1, 3, 3)), Rectangle(1, 1, 3, 3))
        self.assertEqual(Rectangle(-12, -4, 12, 4).cover(Rectangle(-12, 4, 12, 8)), Rectangle(-12, -4, 12, 8))
