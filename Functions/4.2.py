__author__ = 'Bartek'


def print_ruler(number):
    ruler = ""
    limiter = "    "
    counter = 0
    border_value = 10

    for i in range(1, number):
        ruler += "|...."
    ruler += "|\n"
    for character in ruler:
        if character == '|':
            ruler += str(counter)
            counter += 1
            if counter >= border_value:
                border_value *= 10
                limiter = limiter[:(len(limiter) - 1)]
            ruler += limiter
    return ruler


def print_rectangle(width, height):
    horizontal_line = "+---" * width + "+\n"
    vertical_line = "|   " * width + "|\n"

    result = ""

    for counter in range(0, height * 2):
        if counter % 2 == 0:
            result += horizontal_line
        else:
            result += vertical_line
    result += horizontal_line
    return result
