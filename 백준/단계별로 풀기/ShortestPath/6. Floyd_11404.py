import sys
input = sys.stdin.readline


n = int(input())
m = int(input())
edges = []
for _ in range(m):
    edges.append(list(map(int, input().split())))

dists = [[float("inf")] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    dists[i][i] = 0
for edge in edges:
    a, b, c = edge
    if dists[a][b] > c:
        dists[a][b] = c

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            if dists[j][k] > dists[j][i] + dists[i][k]:
                dists[j][k] = dists[j][i] + dists[i][k]

for line in dists[1:]:
    for el in line[1:]:
        print(0 if el == float("inf") else el, end = ' ')
    print()
