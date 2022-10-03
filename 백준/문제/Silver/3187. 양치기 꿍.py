import sys
from collections import deque
input = sys.stdin.readline


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    global wolf
    global sheep

    v_count = 0
    k_count = 0
    queue.append((x, y))
    visited[x][y] = 1
    while queue:
        cur_x, cur_y = queue.popleft()
        if field[cur_x][cur_y] == "v":
            v_count += 1
        if field[cur_x][cur_y] == "k":
            k_count += 1
        for x_diff, y_diff in zip(dx, dy):
            next_x = cur_x + x_diff
            next_y = cur_y + y_diff
            if not (0 <= next_x < R and 0 <= next_y < C):
                continue
            if visited[next_x][next_y] == 1:
                continue
            queue.append((next_x, next_y))
            visited[next_x][next_y] = 1
    if v_count < k_count:
        sheep += k_count
    else:
        wolf += v_count


R, C = map(int, input().split())
field = []
visited = [[0] * C for _ in range(R)]
for i in range(R):
    line = input().strip()
    field.append(line)
    for j in range(C):
        if line[j] == "#":
            visited[i][j] = 1

wolf = 0
sheep = 0
queue = deque()
for x in range(R):
    for y in range(C):
        if visited[x][y] == 0:
            bfs(x, y)

print(sheep, wolf)
