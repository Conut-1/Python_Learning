import sys
input = sys.stdin.readline


def find(x):
    if parent[x] < 0:
        return x
    y = find(parent[x])
    parent[x] = y
    return y


def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return

    if parent[x] < parent[y]:
        parent[x] += parent[y]
        parent[y] = x
    else:
        parent[y] += parent[x]
        parent[x] = y


def solve():
    cities = list(map(int, input().split()))
    for city in cities[1:]:
        if find(cities[0]) != find(city):
            return "NO"
    return "YES"


N = int(input())
M = int(input())

parent = [-1] * (N + 1)
for i in range(N):
    arr = list(map(int, input().split()))
    for j in range(N):
        if arr[j] == 1:
            union(i + 1, j + 1)

print(solve())
