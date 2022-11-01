import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def find_root(node):
    while parent[node] != 0:
        node = parent[node]

    return node

def set_tree(pnode, node):
    depth[node] = depth[pnode] + 1
    for child in graph[node]:
        set_tree(node, child)

def get_lca(a, b):
    if depth[a] < depth[b]:
        a, b = b, a
    while depth[a] != depth[b]:
        a = parent[a]

    while a != b:
        a = parent[a]
        b = parent[b]

    return a

T = int(input())
for _ in range(T):
    n = int(input())
    depth = [0] * (n + 1)
    parent = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]

    for __ in range(n - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        parent[b] = a

    set_tree(0, find_root(1))

    a, b = map(int, input().split())
    print(get_lca(a, b))
