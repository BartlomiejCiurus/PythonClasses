from Tools.Scripts.treesync import raw_input

__author__ = 'Bartek'

while True:
    value = raw_input("Podaj wartosc: ")
    if value == "stop\n":
        break
    intValue = int(value)
    print("x: " + value + "x^3: " + str(pow(intValue, 3)))
