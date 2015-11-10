from importlib import reload

__author__ = 'Bartlomiej Ciurus'

import functions

print("First: " + str(functions.factorial(8)))
print("Second: " + str(functions.fibonacci(8)))

reload(functions)

print("Third: " + str(functions.factorial(8)))
print("Fourth: " + str(functions.fibonacci(8)))

del functions

import functions as func

print("Fifth: " + str(func.factorial(6)))
print("Sixth: " + str(func.fibonacci(5)))

reload(func)

print("Seventh: " + str(func.factorial(6)))
print("Eight: " + str(func.fibonacci(5)))

del func

from functions import *

print("Ninth: " + str(fibonacci(8)))
print("Tenth: " + str(factorial(8)))
