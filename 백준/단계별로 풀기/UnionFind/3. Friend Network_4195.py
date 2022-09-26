import sys
input = sys.stdin.readline


def find(x):
    if parent[x] < 0:
        return x
    else:
        y = find(parent[x])
        parent[x] = y
        return y


def union(x, y):
    x = find(x)
    y = find(y)
    if (x == y):
        return
    if parent[x] < parent[y]:
        parent[x] += parent[y]
        parent[y] = x
    else:
        parent[y] += parent[x]
        parent[x] = y


T = int(input())
for _ in range(T):
    f = int(input())
    parent = [-1]
    name = {}
    for __ in range(f):
        a, b = input().split()
        if not a in name:
            name[a] = len(name) + 1
            parent.append(-1)
        if not b in name:
            name[b] = len(name) + 1
            parent.append(-1)
        union(name[a], name[b])
        print(parent[find(name[a])] * (-1))
