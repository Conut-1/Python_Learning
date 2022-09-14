import heapq
import sys
input = sys.stdin.readline


def dijkstra():
    while heap:
        cost, r = heapq.heappop(heap)

        if costs[r] < cost:
            continue
        for w, v in arr_e[r]:
            dis = cost + w
            if costs[v] > dis:
                costs[v], nearest[v] = dis, r
                heapq.heappush(heap, (dis, v))

n = int(input())
m = int(input())
arr_e = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    arr_e[u].append((w, v))
start, end = map(int, input().split())

costs = [float("inf")] * (n + 1)
nearest = [-1] * (n + 1)
heap = [(0, start)]
costs[start] = 0
dijkstra()

tmp = end
res = []
while tmp != start:
    res.append(tmp)
    tmp = nearest[tmp]
res.append(start)
res.reverse()

print(costs[end])
print(len(res))
print(*res)
