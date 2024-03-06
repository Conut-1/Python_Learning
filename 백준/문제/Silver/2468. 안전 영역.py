import sys

input = sys.stdin.readline

n = int(input())
area = [list(map(int, input().split())) for _ in range(n)]

max_safe_count = 1
height = 1
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def check_safe_area():
    stack = [(i, j)]
    visited[i][j] = 1
    while stack:
        x, y = stack.pop()
        for k in range(4):
            next_x = x + dx[k]
            next_y = y + dy[k]
            if not (0 <= next_x < n and 0 <= next_y < n):
                continue
            if area[next_x][next_y] <= height:
                continue
            if visited[next_x][next_y] == 1:
                continue
            visited[next_x][next_y] = 1
            stack.append((next_x, next_y))


while True:
    count = 0
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if area[i][j] > height and visited[i][j] == 0:
                check_safe_area()
                count += 1
    max_safe_count = max(max_safe_count, count)
    if count == 0:
        break
    height += 1

print(max_safe_count)
