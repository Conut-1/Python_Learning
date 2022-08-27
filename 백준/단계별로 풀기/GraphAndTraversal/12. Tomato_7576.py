from collections import deque
import sys
input = sys.stdin.readline


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs():
    queue = deque()
    for i in range(m * n):
        if box[i // m][i % m] == 1:
            queue.append((i // m, i % m))

    while queue:
        cur_x, cur_y = queue.popleft()
        for i in range(4):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]
            if 0 <= next_x < n and 0 <= next_y < m and box[next_x][next_y] == 0:
                box[next_x][next_y] = box[cur_x][cur_y] + 1
                queue.append((next_x, next_y))
        

m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]

bfs()

res = 0
for line in box:
    if 0 in line:
        res = 0
        break
    res = max(res, max(line))
print(res - 1)
