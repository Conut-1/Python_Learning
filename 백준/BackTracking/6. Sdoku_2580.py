def is_promising(i, j):
    if j in arr[i // 9]:
        return (0)
    for k in range(9):
        if arr[k][i % 9] == j:
            return (0)
    for k in range(9):
        if arr[(((i // 9) // 3) * 3) + (k // 3)][(((i % 9) // 3) * 3) + (k % 3)] == j:
            return (0)
    return (1)

def sdoku(i):
    if i == 81:
        for line in arr:
            print(" ".join(map(str, line)))
        quit()
    if arr[i // 9][i % 9] != 0:
        sdoku(i + 1)
    else:
        for j in range(1, 9 + 1):
            if is_promising(i, j):
                arr[i // 9][i % 9] = j
                sdoku(i + 1)
                arr[i // 9][i % 9] = 0

arr = []
for _ in range(9):
    arr.append(list(map(int, input().split())))
sdoku(0)
