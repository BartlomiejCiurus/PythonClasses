__author__ = 'Bartek'

seq = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]


def flatten(sequence):
    result_list = []
    for i in range(0, len(sequence)):
        if isinstance(sequence[i], (list, tuple)):
            result_list.extend(flatten(sequence[i]))
        else:
            result_list.append(sequence[i])
    return result_list

print(flatten(seq))
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
