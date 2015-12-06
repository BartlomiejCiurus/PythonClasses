__author__ = 'Bartek'

# recursive
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# iterative
def iter_factorial(n):
    result = 1
    for i in range(n):
        result *= i + 1
    return result
