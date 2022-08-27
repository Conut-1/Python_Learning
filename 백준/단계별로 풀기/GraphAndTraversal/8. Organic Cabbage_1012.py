import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)


def dfs(r):
    field_map[r // n][r % n] = 0
    if r // n > 0 and field_map[r // n - 1][r % n] == 1:
        dfs(r - n)
    if r // n < m - 1 and field_map[r // n + 1][r % n] == 1:
        dfs(r + n)
    if r % n > 0 and field_map[r // n][r % n - 1] == 1:
        dfs(r - 1)
    if r % n < n - 1 and field_map[r // n][r % n + 1] == 1:
        dfs(r + 1)


t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    field_map = [[0] * n for _ in range(m)]
    for __ in range(k):
        x, y = map(int, input().split())
        field_map[x][y] = 1

    count = 0
    for i in range(m * n):
        if field_map[i // n][i % n] == 1:
            dfs(i)
            count += 1

    print(count)
