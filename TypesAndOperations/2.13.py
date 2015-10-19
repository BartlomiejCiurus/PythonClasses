__author__ = 'Bartlomiej Ciurus'

line = "test test \t\ntest\ttest\ntest test test"
splitWords = line.split()
numberOfLetters = 0
for word in splitWords:
    numberOfLetters += len(word)
print(numberOfLetters)
