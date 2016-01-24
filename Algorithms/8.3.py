import math
import random


def calc_pi(n=100):
    internal_counter = 0
    external_counter = 0
    for count in range(0, n):
        d = math.hypot(random.random(), random.random())
        if d < 1:
            internal_counter += 1
        external_counter = count
    print(4.0 * internal_counter / external_counter)
