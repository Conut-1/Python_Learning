from collections import deque
import sys
input = sys.stdin.readline


def bfs(x_2, y_2):
    while queue:
        x, y = queue.popleft()
        if x == x_2 and y == y_2:
            return chess[x][y]
        for i in range(8):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if 0 <= next_x < l and 0 <= next_y < l:
                if chess[next_x][next_y] == 0:
                    chess[next_x][next_y] = chess[x][y] + 1
                    queue.append((next_x, next_y))


dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

t = int(input())
for _ in range(t):
    l = int(input())
    chess = [[0] * l for _ in range(l)]
    x_1, y_1 = list(map(int, input().split()))
    x_2, y_2 = list(map(int, input().split()))

    queue = deque([(x_1, y_1)])
    print(bfs(x_2, y_2))
