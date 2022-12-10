import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[float("inf")] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for i in range(1, N + 1):
    for j in range(1, N + 1):
        for k in range(1, N + 1):
            if graph[j][k] > graph[j][i] + graph[i][k]:
                graph[j][k] = graph[j][i] + graph[i][k]

minimum = float("inf")
result = 0
for i in range(1, N + 1):
    if minimum > sum(graph[i][1:]):
        result = i
        minimum = sum(graph[i][1:])

print(result)
