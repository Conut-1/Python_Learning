import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

def dfs(x, y, dfs_from, dfs_to):
    if dp[x][y] != -1:
        return dp[x][y]

    count = 0
    if 0 < x and map_h[x][y] < map_h[x - 1][y] and dfs_from != UP:
        count += dfs(x - 1, y, DOWN, UP)
    if 0 < y and map_h[x][y] < map_h[x][y - 1] and dfs_from != LEFT:
        count += dfs(x, y - 1, RIGHT, LEFT)
    if x < m - 1 and map_h[x][y] < map_h[x + 1][y] and dfs_from != DOWN:
        count += dfs(x + 1, y, UP, DOWN)
    if y < n - 1 and map_h[x][y] < map_h[x][y + 1] and dfs_from != RIGHT:
        count += dfs(x, y + 1, LEFT, RIGHT)
    dp[x][y] = count
    return dp[x][y]


m, n = map(int, input().split())
map_h = [list(map(int, input().split())) for _ in range(m)]

dp = [[-1] * n for _ in range(m)]
dp[0][0] = 1
res = dfs(m - 1, n - 1, 0, 0)

print(res)
