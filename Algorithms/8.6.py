dictionary = {}


def p_function(i, j):
    if (i, j) in dictionary:
        return dictionary[(i, j)]
    if i == 0 and j == 0:
        dictionary[(0, 0)] = 0.5
        return 0.5
    elif j == 0:
        dictionary[(i, 0)] = 0
        return 0
    elif i == 0:
        dictionary[(0, j)] = 1
        return 1
    else:
        dictionary[(i, j)] = (p_function(i - 1, j) + p_function(i, j - 1)) / 2
        return dictionary[(i, j)]
