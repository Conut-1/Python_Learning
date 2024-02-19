import sys

input = sys.stdin.readline

dx = [1, 1, 0, -1, -1, -1, 0, 1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    grid = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]

    count = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 1 and visited[i][j] == 0:
                stack = []
                stack.append((i, j))
                visited[i][j] = 1
                while stack:
                    x, y = stack.pop()
                    for k in range(8):
                        next_x = x + dx[k]
                        next_y = y + dy[k]
                        if not (0 <= next_x < h and 0 <= next_y < w):
                            continue
                        if grid[next_x][next_y] == 0 or visited[next_x][next_y] == 1:
                            continue
                        stack.append((next_x, next_y))
                        visited[next_x][next_y] = 1

                count += 1

    print(count)
