__author__ = 'Bartlomiej Ciurus'

line = "test testo \t\ntest\ttest\ntest test test"
splitWords = line.split()
longestWord = ""
for word in splitWords:
    if len(word) > len(longestWord):
        longestWord = word
print("Longest word: " + longestWord + " length: " + str(len(longestWord)))

