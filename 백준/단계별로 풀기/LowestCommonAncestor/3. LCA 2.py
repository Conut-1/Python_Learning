import sys
input = sys.stdin.readline

def set_tree():
    stack = [(0, 1)]
    while stack:
        pnode, node = stack.pop()
        depth[node] = depth[pnode] + 1
        for child in graph[node]:
            if child != pnode:
                parent[0][child] = node
                stack.append((node, child))

def set_parent():
    for k in range(1, MAX_LOG_N + 1):
        for i in range(1, N + 1):
            parent[k][i] = parent[k - 1][parent[k - 1][i]]

def get_lca(a, b):
    if depth[a] < depth[b]:
        a, b = b, a
    diff = depth[a] - depth[b]
    for i in reversed(range(MAX_LOG_N + 1)):
        if diff & (1 << i):
            a = parent[i][a]

    for i in reversed(range(MAX_LOG_N + 1)):
        if parent[i][a] != parent[i][b]:
            a = parent[i][a]
            b = parent[i][b]

    if a != b:
        a = parent[0][a]

    return a

MAX_LOG_N = 17

N = int(input())

depth = [0] * (N + 1)
parent = [[0] * (N + 1) for _ in range(MAX_LOG_N + 1)]
graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

set_tree()
set_parent()

M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    print(get_lca(a, b))
