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


N = int(input())
heap = []
parent = [-1] * N
stars = []
for _ in range(N):
    x, y = map(float, input().split())
    stars.append((x, y))

for i, j in list(combinations(range(N), 2)):
    x_i, y_i = stars[i]
    x_j, y_j = stars[j]
    d = round((abs(x_i - x_j) ** 2 + abs(y_i - y_j) ** 2) ** 0.5, 2)
    heapq.heappush(heap, (d, i, j))

res = 0
while heap:
    c, a, b = heapq.heappop(heap)
    if find(a) == find(b):
        continue
    union(a, b)
    res += c
print(res)
