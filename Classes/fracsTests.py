import unittest


from Classes.fracs import Fraction

__author__ = 'Bartek'


class TestFractions(unittest.TestCase):
    def test_add(self):
        self.assertEqual("10/8", str(Fraction(1, 2) + Fraction(3, 4)))
        self.assertEqual("-12/8", str(Fraction(-4, 2) + Fraction(2, 4)))

    def test_sub(self):
        self.assertEqual("-2/8", str(Fraction(1, 2) - Fraction(3, 4)))
        self.assertEqual("-20/8", str(Fraction(-4, 2) - Fraction(2, 4)))

    def test_mul(self):
        self.assertEqual("3/8", str(Fraction(1, 2) * Fraction(3, 4)))
        self.assertEqual("-8/8", str(Fraction(-4, 2) * Fraction(2, 4)))

    def test_div(self):
        self.assertEqual("4/6", str(Fraction(1, 2) / Fraction(3, 4)))
        self.assertEqual("-16/4", str(Fraction(-4, 2) / Fraction(2, 4)))

    def test_pos(self):
        self.assertEqual("1/2", str(+Fraction(1, 2)))
        self.assertEqual("4/2", str(+Fraction(-4, 2)))

    def test_neg(self):
        self.assertEqual("-1/2", str(-Fraction(1, 2)))
        self.assertEqual("-4/2", str(-Fraction(-4, 2)))

    def test_invert(self):
        self.assertEqual("2/1", str(~Fraction(1, 2)))
        self.assertEqual("2/-4", str(~Fraction(-4, 2)))

    def test_repr(self):
        self.assertEqual("Fraction(1, 2)", repr(Fraction(1, 2)))
        self.assertEqual("Fraction(-4, 2)", repr(Fraction(-4, 2)))
