__author__ = 'Bartlomiej Ciurus'

line = "dest gest aest GvR testGvRtest tes"
print(sorted(line.split(), key=str.lower))
print(sorted(line.split(), key=len))

