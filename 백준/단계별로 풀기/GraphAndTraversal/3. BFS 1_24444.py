import sys
from collections import deque
input = sys.stdin.readline


def bfs(r):
    count = 1

    visited[r] = count
    count += 1
    queue.append(r)
    while queue:
        u = queue.popleft()
        for x in e[u]:
            if visited[x] == 0:
                visited[x] = count
                count += 1
                queue.append(x)


n, m, r = map(int, input().split())
e = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    e[u].append(v)
    e[v].append(u)

for arr in e:
    arr.sort()

queue = deque()
visited = [0] * (n + 1)
bfs(r)

for i in visited[1:]:
    print(i)
