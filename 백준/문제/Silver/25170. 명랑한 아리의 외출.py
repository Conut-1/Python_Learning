import sys
from collections import deque
input = sys.stdin.readline

dx = [1, 0, 1]
dy = [0, 1, 1]

def bfs(dp, work, time):
    queue = deque()
    queue.append((0, 0, 0, 0))
    while queue:
        cur_x, cur_y, cur_t, cur_w = queue.popleft()
        for x_plus, y_plus in zip(dx, dy):
            next_x = cur_x + x_plus
            next_y = cur_y + y_plus
            next_t = cur_t + 1
            if next_x >= N or next_y >= M or next_t > T - max(N - 1 - next_x, M - 1 - next_y):
                continue
            if dp[next_x][next_y][next_t] < cur_w:
                dp[next_x][next_y][next_t] = cur_w
                queue.append((next_x, next_y, next_t, cur_w))
            if work[cur_x][cur_y] != 0:
                next_t = cur_t + 1 + time[cur_x][cur_y]
                if next_t > T - max(N - 1 - next_x, M - 1 - next_y):
                    continue
                next_w = cur_w + work[cur_x][cur_y]
                if dp[next_x][next_y][next_t] < next_w:
                    dp[next_x][next_y][next_t] = next_w
                    queue.append((next_x, next_y, next_t, next_w))

N, M, T = map(int, input().split())
work = [list(map(int, input().split())) for _ in range(N)]
time = [list(map(int, input().split())) for _ in range(N)]

dp = [[[-1] * (T + 1) for _ in range(M)] for _ in range(N)]
bfs(dp, work, time)
            
print(max(dp[-1][-1]))
