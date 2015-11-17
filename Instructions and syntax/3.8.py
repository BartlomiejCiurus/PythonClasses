from pip._vendor.distlib.compat import raw_input

__author__ = 'Bartek'

firstList = raw_input("Podaj sekwencje elementow oddzielajac je przecinkami: ")
secondList = raw_input("Podaj druga sekwencje elementow oddzielajac je przecinkami: ")

firstListArray = firstList.split(",")
secondListArray = secondList.split(",")
resultArray = []

for element in firstListArray:
    element.replace(",", "")
for element in secondListArray:
    element.replace(",", "")

print("Wspolne elementy: ")
for element in firstListArray:
    if element.strip() not in resultArray:
        resultArray.append(element.strip())
    if element in secondListArray:
        print(element, end=", ")
print("")
for element in secondListArray:
    if element.strip() not in resultArray:
        resultArray.append(element.strip())
print("Wszystkie elementy: ")
print(resultArray)

