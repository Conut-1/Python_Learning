from collections import deque


def pour(x, y):
    if not visited[x][y]:
        visited[x][y] = 1
        queue.append((x, y))


def bfs():
    while queue:
        x, y = queue.popleft()
        z = c - x - y

        if x == 0:
            result.append(z)

        water = min(x, b - y)
        pour(x - water, y + water)

        water = min(x, c - z)
        pour(x - water, y)

        water = min(y, a - x)
        pour(x + water, y - water)

        water = min(y, c - z)
        pour(x, y - water)

        water = min(z, a - x)
        pour(x + water, y)

        water = min(z, b - y)
        pour(x, y + water)


a, b, c = map(int, input().split())
visited = [[0] * (b + 1) for _ in range(a + 1)]
result = []

queue = deque()
queue.append((0, 0))
visited[0][0] = 1

bfs()

result.sort()
print(*result)
