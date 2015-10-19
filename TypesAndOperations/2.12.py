__author__ = 'Bartlomiej Ciurus'

line = "test test \t\ntest\ttest\ntest test test"
splitWords = line.split()
result = ""
for word in splitWords:
    result += word[0]
print(result)
