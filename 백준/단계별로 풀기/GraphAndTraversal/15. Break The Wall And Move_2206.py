from collections import deque
import sys
input = sys.stdin.readline


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs():
    visited_0[0][0] = 1
    while queue:
        x, y, count = queue.popleft()
        if x == n - 1 and y == m - 1:
            return
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if 0 <= next_x < n and 0 <= next_y < m:
                if count == 0:
                    if maze[next_x][next_y] == "1" and visited_1[next_x][next_y] == -1:
                        visited_1[next_x][next_y] = visited_0[x][y] + 1
                        queue.append((next_x, next_y, 1))
                    elif maze[next_x][next_y] == "0" and visited_0[next_x][next_y] == -1:
                        visited_0[next_x][next_y] = visited_0[x][y] + 1
                        queue.append((next_x, next_y, count))
                else:
                    if maze[next_x][next_y] == "0" and visited_1[next_x][next_y] == -1:
                        visited_1[next_x][next_y] = visited_1[x][y] + 1
                        queue.append((next_x, next_y, count))


n, m = map(int, input().split())
maze = [input().rstrip() for _ in range(n)]

queue = deque([(0, 0, 0)])
visited_0 = [[-1] * m for _ in range(n)]
visited_1 = [[-1] * m for _ in range(n)]

bfs()

minimum = min(visited_0[n - 1][m - 1], visited_1[n - 1][m - 1])
maximum = max(visited_0[n - 1][m - 1], visited_1[n - 1][m - 1])
if minimum == -1:
    print(maximum)
else:
    print(minimum)
