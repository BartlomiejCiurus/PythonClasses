__author__ = 'Bartek'


class Fraction:
    counter = 0
    denominator = 0

    def __init__(self, counter, denominator):
        self.counter = counter
        self.denominator = denominator

    def is_denominator_valid(self):
        return self.denominator != 0

    def is_denominator_same(self, fraction):
        return self.denominator == fraction.denominator

    def __add__(self, fraction):
        if not self.is_denominator_valid() and not fraction.is_denominator_valid():
            raise ZeroDivisionError
        if self.is_denominator_same(fraction):
            return Fraction(self.counter + fraction.counter, self.denominator)
        else:
            return Fraction(self.counter * fraction.denominator + fraction.counter * self.denominator,
                            self.denominator * fraction.denominator)

    def __sub__(self, fraction):
        if not self.is_denominator_valid() and not fraction.is_denominator_valid():
            raise ZeroDivisionError
        if self.is_denominator_same(fraction):
            return Fraction(self.counter - fraction.counter, self.denominator)
        else:
            return Fraction(self.counter * fraction.denominator - fraction.counter * self.denominator,
                            self.denominator * fraction.denominator)

    def __mul__(self, fraction):
        if not self.is_denominator_valid() and not fraction.is_denominator_valid():
            raise ZeroDivisionError
        return Fraction(self.counter * fraction.counter, self.denominator * fraction.denominator)

    def __truediv__(self, fraction):
        if not self.is_denominator_valid() and not fraction.is_denominator_valid():
            raise ZeroDivisionError
        return Fraction(self.counter * fraction.denominator, self.denominator * fraction.counter)

    def __pos__(self):
        if self.is_positive():
            return self
        return Fraction(self.counter * -1, self.denominator)

    def __neg__(self):
        if not self.is_positive():
            return self
        return Fraction(self.counter * -1, self.denominator)

    def __invert__(self):
        return Fraction(self.denominator, self.counter)

    def is_positive(self):
        if not self.is_denominator_valid():
            raise ZeroDivisionError
        is_fraction_positive = self.counter * self.denominator >= 0
        return is_fraction_positive

    def is_zero(self):
        if not self.is_denominator_valid():
            raise ZeroDivisionError
        return self.counter == 0

    # no longer available in Python 3.0
    def __cmp__(self, fraction):
        if not self.is_denominator_valid() and not fraction.is_denominator_valid():
            raise ZeroDivisionError
        float_inner_fraction = float(self)
        float_outer_fraction = float(fraction)
        if float_inner_fraction == float_outer_fraction:
            return 0
        if float_inner_fraction > float_outer_fraction:
            return 1
        else:
            return -1

    # in python 3.0 result of dividing two integers is float
    def __float__(self):
        return self.counter / self.denominator

    def __str__(self):
        return str(self.counter) + "/" + str(self.denominator)

    def __repr__(self):
        return "Fraction(" + str(self.counter) + ", " + str(self.denominator) + ")"
