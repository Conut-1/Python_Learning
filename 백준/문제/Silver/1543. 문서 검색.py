document = input()
word = input()

count = 0
i = 0
while i < len(document) - len(word) + 1:
    if document[i:i + len(word)] == word:
        count += 1
        i = i + len(word)
    else:
        i += 1

print(count)
