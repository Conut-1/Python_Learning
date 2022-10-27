arr = [list(map(int, input().split())) for _ in range(9)]

maximum = 0
max_i = 1
max_j = 1
for i in range(9):
    for j in range(9):
        if arr[i][j] > maximum:
            maximum = arr[i][j]
            max_i = i + 1
            max_j = j + 1

print(maximum)
print(max_i, max_j)
