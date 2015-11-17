__author__ = 'Bartlomiej Ciurus'


def is_denominator_valid(fraction):
    return fraction[1] != 0


def is_denominator_same(fraction1, fraction2):
    return fraction1[1] == fraction2[1]


def add_fraction(fraction1, fraction2):
    if not is_denominator_valid(fraction1) and not is_denominator_valid(fraction2):
        raise ZeroDivisionError
    if is_denominator_same(fraction1, fraction2):
        return [fraction1[0] + fraction2[0], fraction1[1]]
    else:
        return [fraction1[0] * fraction2[1] + fraction2[0] * fraction1[1], fraction1[1] * fraction2[1]]


def sub_fraction(fraction1, fraction2):
    if not is_denominator_valid(fraction1) and not is_denominator_valid(fraction2):
        raise ZeroDivisionError
    if is_denominator_same(fraction1, fraction2):
        return [fraction1[0] - fraction2[0], fraction1[1]]
    else:
        return [fraction1[0] * fraction2[1] - fraction2[0] * fraction1[1], fraction1[1] * fraction2[1]]


def mul_fraction(fraction1, fraction2):
    if not is_denominator_valid(fraction1) and not is_denominator_valid(fraction2):
        raise ZeroDivisionError
    return [fraction1[0] * fraction2[0], fraction1[1] * fraction2[1]]


def div_fraction(fraction1, fraction2):
    if not is_denominator_valid(fraction1) and not is_denominator_valid(fraction2):
        raise ZeroDivisionError
    return [fraction1[0] * fraction2[1], fraction1[1] * fraction2[0]]


def is_positive(fraction):
    if not is_denominator_valid(fraction):
        raise ZeroDivisionError
    is_fraction_positive = (fraction[0] * fraction[1]) >= 0
    return is_fraction_positive


def is_zero(fraction):
    if not is_denominator_valid(fraction):
        raise ZeroDivisionError
    return fraction[0] == 0


def cmp_fractions(fraction1, fraction2):
    if not is_denominator_valid(fraction1) and not is_denominator_valid(fraction2):
        raise ZeroDivisionError
    if (fraction1[0] / fraction1[1]) == (fraction2[0] / fraction2[1]):
        return 0
    if (fraction1[0] / fraction1[1]) > (fraction2[0] / fraction2[1]):
        return 1
    else:
        return -1


def fraction2float(fraction):
    return float(fraction[0]) / float(fraction[1])
