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
parent = [-1] * n
lines = [list(map(int, input().split())) for _ in range(m)]

res = 0
for i in range(len(lines)):
    a, b = lines[i]
    if find(a) == find(b):
        res = i + 1
        break
    union(a, b)
print(res)
