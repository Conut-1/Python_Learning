import sys
from collections import deque

input = sys.stdin.readline


def find_cities(k, x):
    visited[x] = 1
    queue = deque([(x, 0)])
    cities = []
    while queue:
        cur, cur_dist = queue.popleft()
        for next in edges[cur]:
            if visited[next] == 1:
                continue
            visited[next] = 1
            if cur_dist + 1 == k:
                cities.append(next)
            else:
                queue.append((next, cur_dist + 1))
    return cities


N, M, K, X = map(int, input().split())
visited = [0] * (N + 1)
edges = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    edges[a].append(b)

cities = find_cities(K, X)
cities.sort()

if len(cities):
    print(*cities, sep="\n")
else:
    print(-1)
