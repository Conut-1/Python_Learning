import sys

input = sys.stdin.readline


def find_root(x):
    if parents[x] == x:
        return x
    parents[x] = find_root(parents[x])
    return parents[x]


def union_root(x, y):
    x = find_root(x)
    y = find_root(y)
    if x != y:
        parents[y] = x


N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]

parents = [i for i in range(N)]
edges = []
for i in range(N):
    for j in range(i + 1, N):
        edges.append((costs[i][j], i, j))
edges.sort()

res = 0
count = 0
for cost, a, b in edges:
    if find_root(a) == find_root(b):
        continue
    count += 1
    res += cost
    union_root(a, b)
    if count == N - 1:
        break

print(res)
