import sys
input = sys.stdin.readline


V, E = map(int, input().split())

dists = [[float("inf")] * (V + 1) for _ in range(V + 1)]
for i in range(1, V + 1):
    dists[i][i] = 0

for _ in range(E):
    a, b, c = map(int, input().split())
    if dists[a][b] > c:
        dists[a][b] = c

for i in range(1, V + 1):
    for j in range(1, V + 1):
        for k in range(1, V + 1):
            if dists[j][k] > dists[j][i] + dists[i][k]:
                dists[j][k] = dists[j][i] + dists[i][k]

res = float("inf")

for i in range(1, V):
    for j in range(i + 1, V + 1):
        res = min(res, dists[i][j] + dists[j][i])

print(-1 if res == float("inf") else res)
