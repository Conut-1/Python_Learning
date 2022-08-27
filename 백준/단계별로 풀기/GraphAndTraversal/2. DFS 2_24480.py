import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)


def dfs(r):
    global count

    visited[r - 1] = count
    count += 1
    for x in e[r - 1]:
        if visited[x - 1] == 0:
            dfs(x)


n, m, r = map(int, input().split())
e = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    e[u - 1].append(v)
    e[v - 1].append(u)

for arr in e:
    arr.sort(reverse=True)

visited = [0] * n
count = 1
dfs(r)

for i in visited:
    print(i)
