import sys
from collections import deque
input = sys.stdin.readline


def dfs(prev, node):
    visited[node] = True
    for n in graph[node]:
        if n == prev:
            continue
        if visited[n]:
            return False
        if not dfs(node, n):
            return False
    return True


case = 1
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        node_1, node_2 = map(int, input().split())
        graph[node_1].append(node_2)
        graph[node_2].append(node_1)

    count = 0
    visited = [0] * (n + 1)
    for i in range(1, n + 1):
        if visited[i] == 1:
            continue
        if dfs(0, i):
            count += 1

    if count == 0:
        print(f"Case {case}: No trees.")
    if count == 1:
        print(f"Case {case}: There is one tree.")
    if count > 1:
        print(f"Case {case}: A forest of {count} trees.")
    case += 1
