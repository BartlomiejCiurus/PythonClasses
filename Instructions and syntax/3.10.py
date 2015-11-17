from pip._vendor.distlib.compat import raw_input

__author__ = 'Bartek'

romanValues = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

romanNumber = raw_input("Podaj liczbe rzymska do przekonwertowania: ")
result = 0
previousNumber = 0

for number in romanNumber:
    if number not in romanValues:
        raise SyntaxError
    if romanValues[number] > previousNumber:
        result -= previousNumber
    else:
        result += previousNumber
    previousNumber = romanValues[number]
result += previousNumber
print(result)





