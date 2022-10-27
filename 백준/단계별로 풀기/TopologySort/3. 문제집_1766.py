import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
in_degree = [0] * (N + 1)
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    in_degree[B] += 1

heap = []
for i in range(1, N + 1):
    if in_degree[i] == 0:
        heapq.heappush(heap, i)

res = []
for _  in range(N):
    x = heapq.heappop(heap)
    res.append(x)
    for y in graph[x]:
        in_degree[y] -= 1
        if in_degree[y] == 0:
            heapq.heappush(heap, y)

print(*res)
