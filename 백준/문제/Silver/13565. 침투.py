import sys

input = sys.stdin.readline


def dfs(i):
    visited[0][i] = 1
    stack = [(0, i)]
    while stack:
        cur_x, cur_y = stack.pop()
        for i in range(4):
            next_x, next_y = cur_x + dx[i], cur_y + dy[i]
            if not (0 <= next_x < M and 0 <= next_y < N):
                continue
            if visited[next_x][next_y] == 1 or grid[next_x][next_y] == "1":
                continue
            if next_x == M - 1:
                return "YES"
            visited[next_x][next_y] = 1
            stack.append((next_x, next_y))
    return "NO"


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

M, N = map(int, input().split())
grid = [input().rstrip() for _ in range(M)]

visited = [[0] * N for _ in range(M)]
res = ""
for i in range(N):
    if visited[0][i] == 1:
        continue
    res = dfs(i)
    if res == "YES":
        break

print(res)
