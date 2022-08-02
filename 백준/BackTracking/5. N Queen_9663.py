def check_pos(i, j):
    if check1[j] == 1:
        return (0)
    if check2[i + j] == 1:
        return (0)
    if check3[i - j + n - 1] == 1:
        return (0)
    return (1)

def dfs(i):
    if n == i:
        global count
        count += 1
        return
    for j in range(0, n):
        queen[i] = j
        if check_pos(i, j):
            check1[j] = 1
            check2[i + j] = 1
            check3[i - j + n - 1] = 1
            dfs(i + 1)
            check1[j] = 0
            check2[i + j] = 0
            check3[i - j + n - 1] = 0

n = int(input())

queen = [0] * n
check1 = [0] * n
check2 = [0] * (2 * n - 1)
check3 = [0] * (2 * n - 1)
count = 0

dfs(0)
print(count)
