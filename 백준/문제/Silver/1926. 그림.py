import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

x_diff = [1, -1, 0, 0]
y_diff = [0, 0, 1, -1]

def dfs(x, y):
    global count

    visited[x][y] = 1
    if draw[x][y] == 0:
        return
    count += 1
    for dx, dy in zip(x_diff, y_diff):
        x_next, y_next = x + dx, y + dy
        if 0 <= x_next < n and 0 <= y_next < m:
            if visited[x_next][y_next] == 1:
                continue
            dfs(x_next, y_next)

n, m = map(int, input().split())
draw = [list(map(int, input().split())) for _ in range(n)]

visited = [[0] * m for _ in range(n)]
area = []

for i in range(n):
    for j in range(m):
        if visited[i][j] == 1:
            continue
        count = 0
        dfs(i, j)
        if count:
            area.append(count)

if area:
    print(len(area))
    print(max(area))
else:
    print(0)
    print(0)
