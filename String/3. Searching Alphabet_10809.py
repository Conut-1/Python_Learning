input_value = input()
alphabet = [-1] * 26
for i in range(len(input_value)):
    cha_index = ord(input_value[i]) - ord("a")
    if alphabet[cha_index] == - 1:
        alphabet[cha_index] = i
print(" ".join(map(str, alphabet)))