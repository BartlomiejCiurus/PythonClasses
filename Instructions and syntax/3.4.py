from Tools.Scripts.treesync import raw_input

__author__ = 'Bartek'

while True:
    value = raw_input("Podaj wartosc: ")
    if value == "stop\n":
        break
    try:
        intValue = int(value)
    except ValueError:
        print("Wyglada na to, ze podana wartosc nie jest wartoscia typu integer!")
        continue
    print("x: " + value + "x^3: " + str(pow(intValue, 3)))
