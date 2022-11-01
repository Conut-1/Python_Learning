import sys
input = sys.stdin.readline

def set_tree():
    stack = [(0, 1, 0)]
    while stack:
        pnode, node, node_cost = stack.pop()
        depth[node] = depth[pnode] + 1
        cost[0][node] = node_cost
        for child, child_cost in graph[node]:
            if child != pnode:
                parent[0][child] = node
                stack.append((node, child, child_cost))

def set_table():
    for k in range(1, MAX_LOG_N + 1):
        for i in range(1, N + 1):
            parent[k][i] = parent[k - 1][parent[k - 1][i]]
            cost[k][i] = cost[k - 1][i] + cost[k - 1][parent[k - 1][i]]

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

def get_cost_1(target):
    a, b = target
    cost_res = 0
    lca = get_lca(a, b)

    diff = depth[a] - depth[lca]
    for i in reversed(range(MAX_LOG_N + 1)):
        if diff & (1 << i):
            cost_res += cost[i][a]
            a = parent[i][a]
    
    diff = depth[b] - depth[lca]
    for i in reversed(range(MAX_LOG_N + 1)):
        if diff & (1 << i):
            cost_res += cost[i][b]
            b = parent[i][b]

    return cost_res

def get_cost_2(target):
    a, b, c = target
    lca = get_lca(a, b)

    diff_a = depth[a] - depth[lca]
    if c <= diff_a + 1:
        target = c - 1
        for i in reversed(range(MAX_LOG_N + 1)):
            if target & (1 << i):
                a = parent[i][a]
        return a
    
    diff_b = depth[b] - depth[lca]
    target = diff_a + diff_b + 1 - c
    for i in reversed(range(MAX_LOG_N + 1)):
        if target & (1 << i):
            b = parent[i][b]
    return b

MAX_LOG_N = 17

N = int(input())

depth = [0] * (N + 1)
parent = [[0] * (N + 1) for _ in range(MAX_LOG_N + 1)]
cost = [[0] * (N + 1) for _ in range(MAX_LOG_N + 1)]
graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

set_tree()
set_table()

M = int(input())
for _ in range(M):
    mode, *target = map(int, input().split())
    if mode == 1:
        print(get_cost_1(target))
    else:
        print(get_cost_2(target))
