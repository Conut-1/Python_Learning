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


N = int(input())
parent = [-1] * (N + 1)
for _ in range(N - 2):
    a, b = map(int, input().split())
    union(a, b)

res = []
for i in range(1, N + 1):
    if parent[i] < 0:
        res.append(i)

print(*res)
