import sys
from collections import deque
input = sys.stdin.readline

x_diff = [1, 0, -1, 0]
y_diff = [0, 1, 0, -1]

def bfs():
    global time_gram

    queue = deque()
    queue.append((0, 0))
    time[0][0] = 0
    while queue:
        x_cur, y_cur = queue.popleft()
        if x_cur == N - 1 and y_cur == M - 1:
            return
        for dx, dy in zip(x_diff, y_diff):
            x_next = x_cur + dx
            y_next = y_cur + dy
            if x_next < 0 or x_next >= N:
                continue
            if y_next < 0 or y_next >= M:
                continue
            if castle[x_next][y_next] == 1:
                continue
            if time[x_next][y_next] <= time[x_cur][y_cur] + 1:
                continue
            if time[x_cur][y_cur] + 1 > T:
                continue
            time[x_next][y_next] = time[x_cur][y_cur] + 1
            if castle[x_next][y_next] == 2:
                time_gram = time[x_next][y_next] + (N - 1 - x_next) + (M - 1 - y_next)
            queue.append((x_next, y_next))

N, M, T = map(int, input().split())
castle = [list(map(int, input().split())) for _ in range(N)]

time = [[T + 1] * M for _ in range(N)]
time_gram = T + 1
bfs()

res = min(time[-1][-1], time_gram)
if res > T:
    print("Fail")
else:
    print(res)
