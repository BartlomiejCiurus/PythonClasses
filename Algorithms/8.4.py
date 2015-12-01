import math


def heron(a, b, c):
    if (a + b <= c) or (a + c <= b) or (b + c <= a) or (a == 0 or b == 0 or c == 0):
        raise ValueError("Podane liczby nie spelniaja warunkow trojkata!")
    semi_parameter = (a + b + c) / 2
    print(math.sqrt(semi_parameter * (semi_parameter - a) * (semi_parameter - b) * (semi_parameter - c)))
