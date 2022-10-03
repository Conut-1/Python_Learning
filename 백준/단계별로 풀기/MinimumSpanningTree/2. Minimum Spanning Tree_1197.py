import sys
import heapq
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


V, E = map(int, input().split())
heap = []
parent = [-1] * (V + 1)
for _ in range(E):
    a, b, c = map(int, input().split())
    heapq.heappush(heap, (c, a, b))

res = 0
while heap:
    c, a, b = heapq.heappop(heap)
    if find(a) == find(b):
        continue
    union(a, b)
    res += c
print(res)
