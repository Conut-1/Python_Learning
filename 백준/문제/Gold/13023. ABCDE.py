import sys
input = sys.stdin.readline

def dfs(cur, depth):
    global res

    if res == 1:
        return
    if depth == 5:
        res = 1
        return

    visited[cur] = 1
    for next in friends[cur]:
        if visited[next]:
            continue
        dfs(next, depth + 1)
    visited[cur] = 0


N, M = map(int,input().split())
friends = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

res = 0
visited = [0] * N
for i in range(N):
    if dfs(i, 1):
        res = 1
        break

print(res)
