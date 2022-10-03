import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def number_island(x, y, island_number):
    queue = deque()
    queue.append((x, y))
    islands_map[x][y] = island_number
    while queue:
        cur_x, cur_y = queue.popleft()
        for x_diff, y_diff in zip(dx, dy):
            next_x = cur_x + x_diff
            next_y = cur_y + y_diff
            if not (0 <= next_x < N and 0 <= next_y < M):
                continue
            if map[next_x][next_y] == 0:
                continue
            if islands_map[next_x][next_y] != 0:
                continue
            queue.append((next_x, next_y))
            islands_map[next_x][next_y] = island_number

def make_bridge(x, y):
    a = islands_map[x][y]
    for x_diff, y_diff in zip(dx, dy):
        cur_x, cur_y = x, y
        bridge_len = -1
        while True:
            cur_x += x_diff
            cur_y += y_diff
            bridge_len += 1
            if not (0 <= cur_x < N and 0 <= cur_y < M):
                break
            if islands_map[cur_x][cur_y] != 0:
                if bridge_len < 2:
                    break
                b = islands_map[cur_x][cur_y]
                if a == b:
                    break
                bridge.append((bridge_len, a, b))
                break

def find(x):
    if islands[x] < 0:
        return x
    else:
        y = find(islands[x])
        islands[x] = y
        return y

def union(x, y):
    x = find(x)
    y = find(y)
    if (x == y):
        return
    if islands[x] < islands[y]:
        islands[x] += islands[y]
        islands[y] = x
    else:
        islands[y] += islands[x]
        islands[x] = y

N, M = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]
islands_map = [[0] * M for _ in range(N)]

island_number = 0
for i in range(N):
    for j in range(M):
        if map[i][j] == 1 and islands_map[i][j] == 0:
            island_number += 1
            number_island(i, j, island_number)

islands = [-1] * (island_number + 1)
bridge = []
for i in range(N):
    for j in range(M):
        if islands_map[i][j] != 0:
            make_bridge(i, j)
bridge.sort()

res = 0
for i in range(len(bridge)):
    d, a, b = bridge[i]
    if find(a) == find(b):
        continue
    union(a, b)
    res += d

idx = find(1)
for i in range(2, island_number + 1):
    if idx != find(i):
        idx = -1
        break

if idx == -1:
    print(-1)
else:
    print(res)
