import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, color, grid, visited):
    visited[x][y] = 1
    for x_dif, y_dif in zip(dx, dy):
        next_x = x + x_dif
        next_y = y + y_dif
        if next_x < 0 or next_x >= N:
            continue
        if next_y < 0 or next_y >= N:
            continue
        if visited[next_x][next_y]:
            continue
        if grid[next_x][next_y] == color:
            dfs(next_x, next_y, color, grid, visited)


N = int(input())
grid = [input().rstrip() for _ in range(N)]
grid_weakness = [line.replace("G", "R") for line in grid]

visited = [[0] * N for _ in range(N)]
visited_weakness = [[0] * N for _ in range(N)]

count = 0
count_weakness = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs(i, j, grid[i][j], grid, visited)
            count += 1

for i in range(N):
    for j in range(N):
        if not visited_weakness[i][j]:
            dfs(i, j, grid_weakness[i][j], grid_weakness, visited_weakness)
            count_weakness += 1

print(count, count_weakness)
