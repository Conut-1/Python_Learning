str1 = input()
str2 = input()

str1_len = len(str1)
str2_len = len(str2)
arr = [[(0, "") for _ in range(str1_len + 1)] for __ in range(str2_len + 1)]
for i in range(1, str2_len + 1):
    for j in range(1, str1_len + 1):
        if str1[j - 1][0] == str2[i - 1][0]:
            arr[i][j] = (arr[i - 1][j - 1][0] + 1, arr[i - 1][j - 1][1] + str1[j - 1][0])
        else:
            if arr[i - 1][j][0] > arr[i][j - 1][0]:
                arr[i][j] = arr[i - 1][j]
            else:
                arr[i][j] = arr[i][j - 1]

res_len, res_str = arr[str2_len][str1_len]
print(res_len)
print(res_str)
