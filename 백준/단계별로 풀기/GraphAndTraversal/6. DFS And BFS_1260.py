import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def dfs(r):
    visited[r] = 1
    seq.append(r)
    for x in e[r]:
        if visited[x] == 0:
            dfs(x)


def bfs(r):
    visited[r] = 1
    seq.append(r)
    queue.append(r)
    while queue:
        u = queue.popleft()
        for x in e[u]:
            if visited[x] == 0:
                visited[x] = 1
                seq.append(x)
                queue.append(x)


n, m, r = map(int, input().split())
e = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    e[u].append(v)
    e[v].append(u)

for arr in e:
    arr.sort()

visited = [0] * (n + 1)
seq = []
dfs(r)

print(*seq)

queue = deque()
visited = [0] * (n + 1)
seq = []
bfs(r)

print(*seq)
