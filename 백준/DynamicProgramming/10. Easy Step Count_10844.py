n = int(input())

dict = {1: [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]}
for i in range(2, n + 1):
    dict[i] = [0] * 10
    for j in range(10):
        if j == 0:
            dict[i][j] = dict[i - 1][j + 1]
        elif j == 9:
            dict[i][j] = dict[i - 1][j - 1]
        else:
            dict[i][j] = dict[i - 1][j - 1] + dict[i - 1][j + 1]

print(sum(dict[n]) % 1000000000)
