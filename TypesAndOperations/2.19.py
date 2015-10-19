__author__ = 'Bartlomiej Ciurus'

L = [12, 4, 534, 31, 6, 421, 521]
result = ""
for number in L:
    if len(repr(number)) == 1:
        result += "00" + repr(number)
    elif len(repr(number)) == 2:
        result += "0" + repr(number)
    else:
        result += repr(number)
print(result)



