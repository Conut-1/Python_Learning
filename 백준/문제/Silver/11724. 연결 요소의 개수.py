import sys
from collections import deque
input = sys.stdin.readline

def bfs(n):
    queue = deque([n])
    visited[n] = 1
    while queue:
        cur = queue.popleft()
        for next in graph[cur]:
            if visited[next]:
                continue
            visited[next] = 1
            queue.append(next)

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

count = 0
for i in range(1, N + 1):
    if visited[i]:
        continue
    bfs(i)
    count += 1

print(count)
