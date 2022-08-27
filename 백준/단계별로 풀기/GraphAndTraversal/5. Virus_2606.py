import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)


def dfs(r):
    visited[r] = 1
    for x in e[r]:
        if visited[x] == 0:
            dfs(x)


n = int(input())
m = int(input())
e = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    e[u].append(v)
    e[v].append(u)

for arr in e:
    arr.sort()

visited = [0] * (n + 1)
dfs(1)

count = 0
for status in visited[2:]:
    if status == 1:
        count += 1

print(count)
