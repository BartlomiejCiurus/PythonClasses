__author__ = 'Bartek'

L = L.sort()  # unresolved reference
x, y = 1, 2, 3  # too many valuse to unpack
X = 1, 2, 3; X[1] = 4  # Tuple don't support item assignment
X = [1, 2, 3]; X[3] = 4  # index out of list
X = "abc"; X.append("d")  # unresolved atribute reference
map(pow, range(8))  #