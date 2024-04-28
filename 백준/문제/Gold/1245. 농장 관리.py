import sys

input = sys.stdin.readline

n, m = map(int, input().split())
farm = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]
res = 0
dx = [1, 1, 0, -1, -1, -1, 0, 1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]


def dfs(x, y):
    visited[x][y] = True
    stack = [(x, y, farm[x][y])]
    height = farm[x][y]
    is_peak = True
    while stack:
        x, y, h = stack.pop()
        for i in range(8):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if not (0 <= next_x < n and 0 <= next_y < m):
                continue
            if visited[next_x][next_y]:
                continue
            if farm[next_x][next_y] > h and h == height:
                is_peak = False
            if farm[next_x][next_y] > h:
                continue
            visited[next_x][next_y] = True
            stack.append((next_x, next_y, farm[next_x][next_y]))
    return 0 if is_peak == False else 1


for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            res += dfs(i, j)

print(res)
