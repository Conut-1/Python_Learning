import sys
input = sys.stdin.readline


def dfs(k, v):
    visited = [False] * (N + 1)
    stack = [(v, 1000000000)]

    while stack:
        cur, usado = stack.pop()
        if not visited[cur] and usado >= k:
            visited[cur] = True
            stack.extend(videos[cur])

    count = visited.count(True)
    return count - 1


N, Q = map(int, input().split())

videos = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    p, q, r = map(int, sys.stdin.readline().split())
    videos[p].append((q, r))
    videos[q].append((p, r))

for _ in range(Q):
    k, v = map(int, input().split())
    print(dfs(k, v))
