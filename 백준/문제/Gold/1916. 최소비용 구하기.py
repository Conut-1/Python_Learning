import heapq
import sys
input = sys.stdin.readline


def dijkstra():
    while heap:
        cost, r = heapq.heappop(heap)

        if costs[r] < cost:
            continue
        for w, v in edges[r]:
            cost_next = cost + w
            if costs[v] > cost_next:
                costs[v] = cost_next
                heapq.heappush(heap, (cost_next, v))


N = int(input())
M = int(input())
edges = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    edges[u].append((w, v))
START, END = map(int, input().split())

costs = [float("inf")] * (N + 1)
heap = [(0, START)]

costs[START] = 0
dijkstra()

print(costs[END])
