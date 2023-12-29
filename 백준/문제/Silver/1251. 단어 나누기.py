word = input()
dict_min = ""

for i in range(1, len(word) - 2 + 1):
    for j in range(1, len(word) - i - 1 + 1):
        k = len(word) - i - j
        new_word = (
            "".join(reversed(word[:i]))
            + "".join(reversed(word[i : i + j]))
            + "".join(reversed(word[i + j : i + j + k]))
        )
        if not dict_min or new_word < dict_min:
            dict_min = new_word

print(dict_min)
