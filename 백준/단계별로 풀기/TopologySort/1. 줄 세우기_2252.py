import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
in_degree = [0] * (N + 1)
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    in_degree[B] += 1

queue = deque()
for i in range(1, N + 1):
    if in_degree[i] == 0:
        queue.append(i)

res = []
for _  in range(N):
    x = queue.popleft()
    res.append(x)
    for y in graph[x]:
        in_degree[y] -= 1
        if in_degree[y] == 0:
            queue.append(y)

print(*res)
