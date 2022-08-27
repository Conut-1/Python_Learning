import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    maze[0][0] = 0
    queue.append((0, 0, 1))
    while queue:
        x, y, count = queue.popleft()
        if x == n - 1 and y == m - 1:
            return count
        if x > 0 and maze[x - 1][y] == 1:
            maze[x - 1][y] = 0
            queue.append((x - 1, y, count + 1))
        if x < n - 1 and maze[x + 1][y] == 1:
            maze[x + 1][y] = 0
            queue.append((x + 1, y, count + 1))
        if y > 0 and maze[x][y - 1] == 1:
            maze[x][y - 1] = 0
            queue.append((x, y - 1, count + 1))
        if y < m - 1 and maze[x][y + 1] == 1:
            maze[x][y + 1] = 0
            queue.append((x, y + 1, count + 1))


n, m = map(int, input().split())
maze = [list(map(int, input().rstrip())) for _ in range(n)]

queue = deque()
res = bfs()

print(res)
