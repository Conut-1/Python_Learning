import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dp_subtree_node(cur_node):
    dp[cur_node][1] = 1
    visited[cur_node] = 1
    for node in graph[cur_node]:
        if visited[node] == 1:
            continue
        dp_subtree_node(node)
        dp[cur_node][0] += dp[node][1]
        dp[cur_node][1] += min(dp[node][0], dp[node][1])

N = int(input())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
dp = [[0] * 2 for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dp_subtree_node(1)

print(min(dp[1][0], dp[1][1]))
