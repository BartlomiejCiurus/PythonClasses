__author__ = 'Bartlomiej Ciurus'


def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
