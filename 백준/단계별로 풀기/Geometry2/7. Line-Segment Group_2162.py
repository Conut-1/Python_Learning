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

def ccw(pos_1, pos_2, pos_3):
    a = pos_1[0] * pos_2[1] + pos_2[0] * pos_3[1] + pos_3[0] * pos_1[1]
    b = pos_1[1] * pos_2[0] + pos_2[1] * pos_3[0] + pos_3[1] * pos_1[0]
    return a - b

def is_intersect(pos_1, pos_2, pos_3, pos_4):
    a = ccw(pos_1, pos_2, pos_3)
    b = ccw(pos_1, pos_2, pos_4)
    c = ccw(pos_3, pos_4, pos_1)
    d = ccw(pos_3, pos_4, pos_2)
    if a * b == 0 and c * d == 0:
        if pos_1 > pos_2:
            pos_1, pos_2 = pos_2, pos_1
        if pos_3 > pos_4:
            pos_3, pos_4 = pos_4, pos_3
        if pos_3 <= pos_2 and pos_1 <= pos_4:
            return 1
        return 0
    if a * b <= 0 and c * d <= 0:
        return 1
    return 0


N = int(input())
lines = []
for _ in range(N):
    x_1, y_1, x_2, y_2 = map(int, input().split())
    lines.append([(x_1, y_1), (x_2, y_2)])
parent = [-1] * N
for i in range(N):
    for j in range(N):
        if find(i) == find(j):
            continue
        if is_intersect(lines[i][0], lines[i][1], lines[j][0], lines[j][1]):
            union(i, j)

count = 0
for element in parent:
    if element < 0:
        count += 1
print(count)
print(-min(parent))
