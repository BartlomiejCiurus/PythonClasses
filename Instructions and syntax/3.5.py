from pip._vendor.distlib.compat import raw_input

__author__ = 'Bartek'

number = int(raw_input("Podaj dlugosc linijki: "))
ruler = ""
limiter = "    "
counter = 0
borderValue = 10

for i in range(1, number):
    ruler += "|...."
ruler += "|\n"
for character in ruler:
    if character == '|':
        ruler += str(counter)
        counter += 1
        if counter >= borderValue:
            borderValue *= 10
            limiter = limiter[:(len(limiter)-1)]
        ruler += limiter


print(ruler)

