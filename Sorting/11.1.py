import random


def list_with_random_values(range_var):
    if range_var < 1:
        raise ValueError("Za maly zakres!")

    my_randoms = [random.randrange(0, range_var - 1, 1) for _ in range(10)]
    return my_randoms


def almost_sorted_list(range_var):
    if range_var < 1:
        raise ValueError("Za maly zakres!")

    sorted_randoms = [random.randrange(0, range_var - 1, 1) for _ in range(10)]
    sorted_randoms.sort()

    my_randoms = [random.randrange(0, range_var - 1, 1) for _ in range(4)]
    sorted_randoms.extend(my_randoms)

    return sorted_randoms


def almost_sorted_list_with_reverse(range_var):
    almost_sorted_list_var = almost_sorted_list(range_var)
    almost_sorted_list_var.reverse()

    return almost_sorted_list_var


def list_with_random_values_gauss(quantity):
    if quantity < 0:
        raise ValueError("Dlugosc listy nie moze byc ujemna!")

    list_with_random_values_gauss_var = [random.gauss(0, 1) for _ in range(quantity)]
    return list_with_random_values_gauss_var


def random_list_with_repeat(quantity, range_var):
    if quantity < 0 or range_var < 1:
        raise ValueError("Ujemna dlugosc listy lub za maly zakres!")
    if quantity <= range_var:
        raise ValueError("Dlugosc listy mniejsza lub rowna wartsci zakersu!")

    random_list_with_repeat_var = [random.randint(0, range_var - 1) for _ in range(quantity)]
    return random_list_with_repeat_var
