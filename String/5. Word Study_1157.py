#최초 풀이
"""
input_value = input()
alphabet = [0] * 26
for cha in input_value:
    if ord("A") <= ord(cha) <= ord("Z"):
        alphabet[ord(cha) - ord("A")] += 1
    elif ord("a") <= ord(cha) <= ord("z"):
        alphabet[ord(cha) - ord("a")] += 1

max_number = 0
max_count = 0
result = 0
for i in range(len(alphabet)):
    if alphabet[i] > max_number:
        max_number = alphabet[i]
        result = i
        max_count = 1
    elif alphabet[i] == max_number:
        max_count += 1
if max_count == 1:
    print(chr(result + ord("A")))
else:
    print("?")
"""

input_value = input().upper()
input_value_set = list(set(input_value))
cnt = []
for cha in input_value_set:
    cnt.append(input_value.count(cha))

max_value = max(cnt)
max_number = cnt.count(max_value)
if max_number == 1:
    print(input_value_set[cnt.index(max_value)])
else:
    print("?")