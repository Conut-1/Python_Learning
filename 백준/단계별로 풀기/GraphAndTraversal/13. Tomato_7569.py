from collections import deque
import sys
input = sys.stdin.readline


dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]


def bfs():
    queue = deque()
    for i in range(m * n * h):
        if box[i // (m * n)][i % (m * n) // m][i % (m * n) % m] == 1:
            queue.append((i // (m * n), i % (m * n) // m, i % (m * n) % m))

    while queue:
        cur_x, cur_y, cur_z = queue.popleft()
        for i in range(6):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]
            next_z = cur_z + dz[i]
            if 0 <= next_x < h and 0 <= next_y < n and 0 <= next_z < m and box[next_x][next_y][next_z] == 0:
                box[next_x][next_y][next_z] = box[cur_x][cur_y][cur_z] + 1
                queue.append((next_x, next_y, next_z))

    res = 0
    for floor in box:
        for line in floor:
            if 0 in line:
                return -1
            res = max(res, max(line))
    return res - 1


m, n, h = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

print(bfs())
