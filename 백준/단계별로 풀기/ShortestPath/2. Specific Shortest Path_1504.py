import heapq
import sys
input = sys.stdin.readline


def dijkstra(start, costs):
    heap = [(0, start)]
    costs[start] = 0

    while heap:
        cost, r = heapq.heappop(heap)

        if costs[r] < cost:
            continue
        for w, v in arr_e[r]:
            dis = cost + w
            if costs[v] > dis:
                costs[v] = dis
                heapq.heappush(heap, (dis, v))


N, E = map(int, input().split())
arr_e = [[] for _ in range(N + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    arr_e[a].append((c, b))
    arr_e[b].append((c, a))
v_1, v_2 = map(int, input().split())

costs_1 = [float("inf")] * (N + 1)
costs_v_1 = [float("inf")] * (N + 1)
costs_v_2 = [float("inf")] * (N + 1)

dijkstra(1, costs_1)
dijkstra(v_1, costs_v_1)
dijkstra(v_2, costs_v_2)

res = min(costs_1[v_1] + costs_v_1[v_2] + costs_v_2[N], costs_1[v_2] + costs_v_2[v_1] + costs_v_1[N])
if res == float("inf"):
    print(-1)
else:
    print(res)
