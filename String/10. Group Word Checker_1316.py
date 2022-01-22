test_case = int(input())
cnt = 0
for i in range(test_case):
    input_value = input()
    array = []
    array.append(input_value[0])
    is_groub_word = 1
    for j in range(1, len(input_value)):
        if input_value[j - 1] != input_value[j]:
            if input_value[j] in array:
                is_groub_word = -1
                break
            else:
                array.append(input_value[j])
    if is_groub_word == 1:
        cnt += 1
print(cnt)