import sys

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def cal_cross_size(i, j):
    size = 0
    while True:
        for k in range(4):
            next_x = i + dx[k] * (size + 1)
            next_y = j + dy[k] * (size + 1)
            if not (0 <= next_x < n and 0 <= next_y < m):
                return size
            if draw[next_x][next_y] != "*":
                return size
        size += 1


n, m = map(int, input().split())
draw = [list(input().rstrip()) for _ in range(n)]

res = []
for i in range(1, n - 1):
    for j in range(1, m - 1):
        if draw[i][j] == ".":
            continue
        size = cal_cross_size(i, j)
        if size == 0:
            continue
        res.append([i + 1, j + 1, size])

for cross in res:
    draw[cross[0] - 1][cross[1] - 1] = "."
    for i in range(cross[2]):
        for j in range(4):
            draw[cross[0] - 1 + (i + 1) * dx[j]][cross[1] - 1 + (i + 1) * dy[j]] = "."

for i in range(n):
    for j in range(m):
        if draw[i][j] == "*":
            res.clear()

if len(res) == 0:
    print(-1)
else:
    print(len(res))
    print("\n".join([" ".join(map(str, cross)) for cross in res]))
