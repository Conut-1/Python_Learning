import sys
input = sys.stdin.readline


def find(x):
    if parent[x] < 0:
        return x
    else:
        y = find(parent[x])
        parent[x] = y
        return y


def union(x, y):
    x = find(x)
    y = find(y)
    if (x == y):
        return
    if parent[x] < parent[y]:
        parent[x] += parent[y]
        parent[y] = x
    else:
        parent[y] += parent[x]
        parent[x] = y


N = int(input())
cost = []
parent = [-1] * (N + 1)
pos = []
for i in range(N):
    x, y, z = map(int, input().split())
    pos.append((x, y, z, i))

for i in range(3):
    pos.sort(key=lambda x:x[i])
    prev_pos = pos[0][3]
    for j in range(1, N):
        cur_pos = pos[j][3]
        cost.append((abs(pos[j][i] - pos[j - 1][i]), prev_pos, cur_pos))
        prev_pos = cur_pos
cost.sort()

res = 0
for i in range(len(cost)):
    d, a, b = cost[i]
    if find(a) == find(b):
        continue
    union(a, b)
    res += d
print(res)
