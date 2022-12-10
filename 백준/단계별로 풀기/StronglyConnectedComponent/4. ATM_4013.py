import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def find_scc(i):
    global id
    global scc_id

    id += 1
    visited[i] = id
    stack.append(i)

    result = visited[i]
    for next in graph[i]:
        if visited[next] == 0:
            result = min(result, find_scc(next))
        elif finished[next] == -1:
            result = min(result, visited[next])

    if result == visited[i]:
        cur_scc = []
        while True:
            t = stack.pop()
            cur_scc.append(t)
            finished[t] = scc_id
            if t == i:
                break
        scc.append(cur_scc)
        scc_id += 1

    return result

def bfs(s):
    queue = deque([s])
    while queue:
        cur = queue.popleft()
        for next in scc_graph[cur]:
            if dp[next] < dp[cur] + scc_money[next]:
                dp[next] = dp[cur] + scc_money[next]
                queue.append(next)

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

money = [0] + [int(input()) for _ in range(N)]

S, P = map(int, input().split())
restaurants = list(map(int, input().split()))

id = 0
scc_id = 0
scc = []
stack = []
visited = [0] * (N + 1)
finished = [-1] * (N + 1)
for i in range(1, N + 1):
    if visited[i] == 0:
        find_scc(i)

scc_money = [0] * len(scc)
scc_graph = [set() for _ in range(len(scc))]
for i in range(len(scc)):
    for node in scc[i]:
        scc_money[i] += money[node]
        for next in graph[node]:
            if finished[node] != finished[next]:
                scc_graph[i].add(finished[next])

dp = [0] * len(scc)
dp[finished[S]] = scc_money[finished[S]]
bfs(finished[S])

res = 0
for restaurant in restaurants:
    res = max(res, dp[finished[restaurant]])

print(res)
