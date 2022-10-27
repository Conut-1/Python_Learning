import sys
from collections import deque
input = sys.stdin.readline

def solve():
    n = int(input())

    teams = list(map(int, input().split()))
    graph = [[] for _ in range(n + 1)]
    in_degree = [0] * (n + 1)

    for i in range(len(teams)):
        for j in range(i + 1, len(teams)):
            graph[teams[i]].append(teams[j])
            in_degree[teams[j]] += 1

    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        if b in graph[a]:
            a, b = b, a
        graph[a].append(b)
        graph[b].remove(a)
        in_degree[b] += 1
        in_degree[a] -= 1

    queue = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)

    res = []
    for _  in range(n):
        if not queue:
            print("IMPOSSIBLE")
            return
        if len(queue) > 1:
            print("?")
            return
        x = queue.popleft()
        res.append(x)
        for y in graph[x]:
            in_degree[y] -= 1
            if in_degree[y] == 0:
                queue.append(y)

    print(*res)


T = int(input())
for _ in range(T):
    solve()
