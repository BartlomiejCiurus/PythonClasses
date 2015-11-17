__author__ = 'Bartek'

sequence = [[], [4], (1, 2), [3, 4], (5, 6, 7)]
summarizedList = []

for subSequence in sequence:
    summarizedList.append(sum(subSequence))
print(summarizedList)
