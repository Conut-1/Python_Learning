from collections import deque
import sys
input = sys.stdin.readline


def bfs(r):
    visited[r] = 1
    queue.append(r)
    while queue:
        u = queue.popleft()
        for x in e[u]:
            if visited[x] == 0:
                visited[x] = visited[u] * -1
                queue.append(x)
            if visited[x] == visited[u]:
                return "NO"
    return "YES"


k = int(input())
for _ in range(k):
    v, e_num = map(int, input().split())
    e = [[] for __ in range(v + 1)]
    for __ in range(e_num):
        x, y = map(int, input().split())
        e[x].append(y)
        e[y].append(x)

    queue = deque()
    visited = [0] * (v + 1)

    res = "YES"
    for i in range(1, v + 1):
        if visited[i] == 0 and res == "YES":
            res = bfs(i)
    print(res)
