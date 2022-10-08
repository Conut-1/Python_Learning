import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def make_tree(cur_node, parent_node):
    for node in tree[cur_node]:
        if node != parent_node:
            connect[cur_node].append(node)
            parent[node] = cur_node
            make_tree(node, cur_node)

def count_subtree_node(cur_node):
    size[cur_node] = 1
    for node in connect[cur_node]:
        count_subtree_node(node)
        size[cur_node] += size[node]

N, R, Q = map(int, input().split())
tree = [[] for _ in range(N + 1)]
connect = [[] for _ in range(N + 1)]
parent = [-1] * (N + 1)
size = [0] * (N + 1)

for _ in range(N - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

make_tree(R, 0)
count_subtree_node(R)

for _ in range(Q):
    query = int(input())
    print(size[query])
