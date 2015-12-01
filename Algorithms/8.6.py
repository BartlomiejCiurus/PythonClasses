dictionary = {}

def P(i, j):
    if i == 0 and j == 0:
        dictionary['P(0, 0)'] = 0.5
        return 0.5
    elif i == 0 and j > 0:
        dictionary['P(0, %d)' % j] = 1
        return 1
    elif i > 0 and j == 0:
        dictionary['P(%d, 0)' % i] = 0
        return 0
    elif j > 0 and i > 0:
        dictionary['P(%d, %d)' % (i, j)] = (P(i - 1, j) + P(i, j - 1)) / 2
        return (P(i - 1, j) + P(i, j - 1)) / 2
