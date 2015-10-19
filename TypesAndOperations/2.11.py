__author__ = 'Bartlomiej Ciurus'

word = "word"
result = ""
for i in range(len(word)):
    if i == 0:
        result += word[i]
        continue
    result += "_" + word[i]
print(result)
