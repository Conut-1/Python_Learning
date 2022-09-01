import heapq
import sys
input = sys.stdin.readline


def dijkstra(start, dists):
    heap = [(0, start)]
    dists[start] = 0

    while heap:
        cur_dis, a = heapq.heappop(heap)
        if dists[a] < cur_dis:
            continue
        for d, b in roads[a]:
            next_dis = cur_dis + d
            if dists[b] > next_dis:
                dists[b] = next_dis
                heapq.heappush(heap, (next_dis, b))


T = int(input())
for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    roads = [[] for __ in range(n + 1)]
    dests = []
    for __ in range(m):
        a, b, d = map(int, input().split())
        roads[a].append((d, b))
        roads[b].append((d, a))
    for __ in range(t):
        x = int(input())
        dests.append(x)

    dists_start = [float("inf")] * (n + 1)
    dists_g = [float("inf")] * (n + 1)
    dists_h = [float("inf")] * (n + 1)

    dijkstra(s, dists_start)
    dijkstra(g, dists_g)
    dijkstra(h, dists_h)

    res = []
    for dest in dests:
        if dists_start[dest] != float("inf") and dists_start[dest] == min(dists_start[g] + dists_g[h] + dists_h[dest], dists_start[h] + dists_h[g] + dists_g[dest]):
            res.append(dest)

    res.sort()
    print(*res)
