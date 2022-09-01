import sys
input = sys.stdin.readline


def bellman_ford(start):
    dists[start] = 0

    for i in range(n):
        for j in range(m):
            cur_node = edges[j][0]
            next_node = edges[j][1]
            edge_cost = edges[j][2]
            if dists[cur_node] != float("inf") and dists[next_node] > dists[cur_node] + edge_cost:
                dists[next_node] = dists[cur_node] + edge_cost
                if i == n - 1:
                    return True

    return False


n, m = map(int, input().split())
edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

dists = [float("inf")] * (n + 1)

negative_cycle = bellman_ford(1)

if negative_cycle:
    print(-1)
else:
    for dist in dists[2:]:
        print(-1 if dist == float("inf") else dist)
