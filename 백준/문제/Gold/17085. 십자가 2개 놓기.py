N, M = map(int, input().split())
map = [input() for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
areas = []


def calc(x, y):
    size = 0
    areas.append((1 + 4 * size, x, y))
    while True:
        for i in range(4):
            next_x = x + dx[i] * (size + 1)
            next_y = y + dy[i] * (size + 1)
            if not (0 <= next_x < N):
                break
            if not (0 <= next_y < M):
                break
            if map[next_x][next_y] == ".":
                break
        else:
            size += 1
            areas.append((1 + 4 * size, x, y))
            continue
        break


for i in range(N):
    for j in range(M):
        if map[i][j] == "#":
            calc(i, j)
areas.sort(reverse=True)

max_value = 0
for start, (area1, x1, y1) in enumerate(areas):
    visited = [[0] * M for _ in range(N)]
    visited[x1][y1] = 1
    for i in range(area1 // 4):
        for j in range(4):
            visited[x1 + (i + 1) * dx[j]][y1 + (i + 1) * dy[j]] = 1
    for area2, x2, y2 in areas[start + 1 :]:
        if area1 * area2 < max_value:
            break
        if visited[x2][y2] == 1:
            continue
        for i in range(area2 // 4):
            for j in range(4):
                if visited[x2 + (i + 1) * dx[j]][y2 + (i + 1) * dy[j]] == 1:
                    break
            else:
                continue
            break
        else:
            max_value = area1 * area2

print(max_value)
