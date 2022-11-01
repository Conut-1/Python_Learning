import sys
input = sys.stdin.readline

def set_tree():
    stack = [(0, 1, 0)]
    while stack:
        pnode, node, dist = stack.pop()
        depth[node] = depth[pnode] + 1
        dist_min[0][node] = dist
        dist_max[0][node] = dist
        for child, child_dist in graph[node]:
            if child != pnode:
                parent[0][child] = node
                stack.append((node, child, child_dist))

def set_table():
    for k in range(1, MAX_LOG_N + 1):
        for i in range(1, N + 1):
            parent[k][i] = parent[k - 1][parent[k - 1][i]]
            dist_min[k][i] = min(dist_min[k - 1][i], dist_min[k - 1][parent[k - 1][i]])
            dist_max[k][i] = max(dist_max[k - 1][i], dist_max[k - 1][parent[k - 1][i]])

def get_dist(a, b):
    min_res = float("inf")
    max_res = float("-inf")

    if depth[a] < depth[b]:
        a, b = b, a
    diff = depth[a] - depth[b]
    for i in reversed(range(MAX_LOG_N + 1)):
        if diff & (1 << i):
            min_res = min(min_res, dist_min[i][a])
            max_res = max(max_res, dist_max[i][a])
            a = parent[i][a]

    if a == b:
        return (min_res, max_res)

    for i in reversed(range(MAX_LOG_N + 1)):
        if parent[i][a] != parent[i][b]:
            min_res = min(min_res, dist_min[i][a], dist_min[i][b])
            max_res = max(max_res, dist_max[i][a], dist_max[i][b])
            a = parent[i][a]
            b = parent[i][b]

    min_res = min(min_res, dist_min[0][a], dist_min[0][b])
    max_res = max(max_res, dist_max[0][a], dist_max[0][b])

    return (min_res, max_res)

MAX_LOG_N = 17

N = int(input())

depth = [0] * (N + 1)
parent = [[0] * (N + 1) for _ in range(MAX_LOG_N + 1)]
dist_min = [[0] * (N + 1) for _ in range(MAX_LOG_N + 1)]
dist_max = [[0] * (N + 1) for _ in range(MAX_LOG_N + 1)]
graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

set_tree()
set_table()

K = int(input())
for _ in range(K):
    a, b = map(int, input().split())
    print(*get_dist(a, b))
