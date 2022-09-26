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


n, m = map(int, input().split())
parent = [-1] * (n + 1)
for _ in range(m):
    mode, a, b = map(int, input().split())
    if mode == 0:
        union(a, b)
    if mode == 1:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
