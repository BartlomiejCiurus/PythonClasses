from pip._vendor.distlib.compat import raw_input

__author__ = 'Bartek'

width = int(raw_input("Podaj szerokosc prostokatu: "))
height = int(raw_input("Podaj wysokosc prostokatu: "))

horizontalLine = "+---" * width + "+\n"
verticalLine = "|   " * width + "|\n"

result = ""

for counter in range(0, height*2):
    if counter % 2 == 0:
        result += horizontalLine
    else:
        result += verticalLine
result += horizontalLine
print(result)
