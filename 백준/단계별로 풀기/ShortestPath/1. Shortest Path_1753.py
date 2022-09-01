import heapq
import sys
input = sys.stdin.readline


def dijkstra():
    while heap:
        cost, r = heapq.heappop(heap)

        if costs[r] <= cost:
            for w, v in arr_e[r]:
                dis = cost + w
                if costs[v] > dis:
                    costs[v] = dis
                    heapq.heappush(heap, (dis, v))


V, E = map(int, input().split())
k = int(input())
arr_e = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    arr_e[u].append((w, v))

costs = [float("inf")] * (V + 1)
visited = [0] * (V + 1)
heap = [(0, k)]

costs[k] = 0
dijkstra()

for cost in costs[1:]:
    if cost == float("inf"):
        print("INF")
    else:
        print(cost)


# import sys
# input = sys.stdin.readline


# def dijkstra(r):
#     while True:
#         for y, w in arr_e[r]:
#             if visited[y] == 0:
#                 costs[y] = min(costs[y], costs[r] + w)
#         visited[r] = 1
#         min_index = 0
#         for i in range(1, v + 1):
#             if visited[i] == 0 and costs[min_index] > costs[i]:
#                 min_index = i
#         if min_index == 0:
#             break
#         r = min_index


# V, E = map(int, input().split())
# k = int(input())
# arr_e = [[] for _ in range(V + 1)]
# for _ in range(E):
#     u, v, w = map(int, input().split())
#     arr_e[u].append((v, w))

# costs = [float("inf")] * (V + 1)
# visited = [0] * (V + 1)

# costs[k] = 0
# dijkstra(k)

# for cost in costs[1:]:
#     if cost == float("inf"):
#         print("INF")
#     else:
#         print(cost)
