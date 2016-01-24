def binary_search(list, element, min, max):
    if max < min:
        raise ValueError("Right must be greater than left!")
    if min == max:
        if list[min] == element:
            return min
        else:
            return None

    middle = int((min + max) / 2)
    value = list[middle]

    if value == element:
        return middle
    elif value > element:
        return binary_search(list, min, middle - 1, element)
    else:
        return binary_search(list, middle + 1, max, element)
