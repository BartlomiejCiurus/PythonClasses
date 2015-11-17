import unittest
import fractions

__author__ = 'Bartlomiej Ciurus'


class TestFractions(unittest.TestCase):
    def test_add_fractions(self):
        self.assertEqual(fractions.add_fraction([1, 2], [1, 2]), [2, 2])
        self.assertEqual(fractions.add_fraction([1, 3], [3, 4]), [13, 12])

    def test_sub_fractions(self):
        self.assertEqual(fractions.sub_fraction([1, 2], [1, 2]), [0, 2])
        self.assertEqual(fractions.sub_fraction([1, 3], [3, 4]), [-5, 12])

    def test_mul_fractions(self):
        self.assertEqual(fractions.mul_fraction([1, 2], [1, 2]), [1, 4])
        self.assertEqual(fractions.mul_fraction([1, 3], [3, 4]), [3, 12])

    def test_div_fractions(self):
        self.assertEqual(fractions.div_fraction([1, 2], [1, 2]), [2, 2])
        self.assertEqual(fractions.div_fraction([1, 3], [3, 4]), [4, 9])

    def test_is_positive(self):
        self.assertTrue(fractions.is_positive([1, 2]))
        self.assertFalse(fractions.is_positive([-4, 3]))
        self.assertTrue(fractions.is_positive([-4, -2]))

    def test_is_zero(self):
        self.assertTrue(fractions.is_zero([0, 5]))
        self.assertFalse(fractions.is_zero([2, 3]))

    def test_cmp_fractions(self):
        self.assertEqual(fractions.cmp_fractions([1, 2], [1, 2]), 0)
        self.assertEqual(fractions.cmp_fractions([1, 2], [1, 4]), 1)
        self.assertEqual(fractions.cmp_fractions([1, 2], [5, 4]), 2)
        self.assertEqual(fractions.cmp_fractions([1, -3], [1, 2]), 2)

    def test_fraction2float(self):
        self.assertEqual(fractions.fraction2float([1, 2]), 0.5)
        self.assertEqual(fractions.fraction2float([4, 3]), 1.3333333333333333)


if __name__ == '__main__':
    unittest.main()
