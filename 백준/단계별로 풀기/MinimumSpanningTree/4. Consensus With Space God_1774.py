import sys
import heapq
from itertools import combinations
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


N, M = map(int, input().split())
heap = []
parent = [-1] * (N + 1)
pos = [(0, 0)]
for _ in range(N):
    x, y = map(int, input().split())
    pos.append((x, y))

for _ in range(M):
    i, j = map(int, input().split())
    union(i, j)

for i, j in list(combinations(range(1, N + 1), 2)):
    if find(i) == find(j):
        continue
    x_i, y_i = pos[i]
    x_j, y_j = pos[j]
    d = (abs(x_i - x_j) ** 2 + abs(y_i - y_j) ** 2) ** 0.5
    heapq.heappush(heap, (d, i, j))

res = 0
while heap:
    d, a, b = heapq.heappop(heap)
    if find(a) == find(b):
        continue
    union(a, b)
    res += d
print(f'{res:.2f}')
