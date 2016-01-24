from Tools.demo.sortvisu import quicksort


def sort_with_median(list, min, max):
    if max < min:
        raise ValueError
    quicksort(list)
    quantity = max - min + 1
    middle = int((min + max) / 2)
    if quantity % 2 == 0:
        return (list[middle] + list[middle + 1]) / 2
    else:
        return list[middle]
