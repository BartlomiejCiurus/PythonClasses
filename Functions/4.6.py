__author__ = 'Bartek'

seq = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]


def sum_seq(sequence):
    result = 0
    for i in range(0, len(sequence)):
        if isinstance(sequence[i], (list, tuple)):
            result += sum_seq(sequence[i])
        else:
            result += sequence[i]
    return result

print(sum_seq(seq))
# 45
