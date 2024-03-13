import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
knight_x, knight_y = map(int, input().split())

step = [[-1] * (n + 1) for _ in range(n + 1)]
dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

queue = deque()
step[knight_x][knight_y] = 0
queue.append((knight_x, knight_y))
while queue:
    x, y = queue.popleft()
    for i in range(8):
        next_x = x + dx[i]
        next_y = y + dy[i]
        if not (0 < next_x <= n and 0 < next_y <= n):
            continue
        if step[next_x][next_y] != -1:
            continue
        step[next_x][next_y] = step[x][y] + 1
        queue.append((next_x, next_y))

res = []
for _ in range(m):
    target_x, target_y = map(int, input().split())
    res.append(step[target_x][target_y])

print(*res)
