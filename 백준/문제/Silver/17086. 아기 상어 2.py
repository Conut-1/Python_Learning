import sys
from collections import deque

input = sys.stdin.readline

dx = [1, 1, 0, -1, -1, -1, 0, 1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

N, M = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(N)]

queue = deque()
for i in range(N):
    for j in range(M):
        if area[i][j] == 1:
            queue.append((i, j))

while queue:
    cur_x, cur_y = queue.popleft()

    for i in range(8):
        next_x = cur_x + dx[i]
        next_y = cur_y + dy[i]

        if not (0 <= next_x < N and 0 <= next_y < M):
            continue
        if area[next_x][next_y] == 0:
            queue.append((next_x, next_y))
            area[next_x][next_y] = area[cur_x][cur_y] + 1

res = 0
for i in range(N):
    for j in range(M):
        res = max(res, area[i][j] - 1)
print(res)
