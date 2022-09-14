import sys
input = sys.stdin.readline


def find_path(i, j):
    if nearest[i][j] == 0:
        return []
    
    k = nearest[i][j]
    return find_path(i, k) + [k] + find_path(k, j)


n = int(input())
m = int(input())
edges = []
for _ in range(m):
    edges.append(list(map(int, input().split())))

dists = [[float("inf")] * (n + 1) for _ in range(n + 1)]
nearest = [[0] * (n + 1) for _ in range(n + 1)]
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
                nearest[j][k] = i

for line in dists[1:]:
    for el in line[1:]:
        print(0 if el == float("inf") else el, end = ' ')
    print()

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if dists[i][j] in [0, float("inf")]:
            print(0)
            continue
        path = [i] + find_path(i, j) + [j]
        print(len(path), *path)
