import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def make_tree(cur_node, parent_node):
    for node in graph[cur_node]:
        if node != parent_node:
            connect[cur_node].append(node)
            parent[node] = cur_node
            make_tree(node, cur_node)

def dp_subtree_node(cur_node):
    dp[cur_node][1] = w_arr[cur_node]
    for node in connect[cur_node]:
        dp_subtree_node(node)
        dp[cur_node][0] += max(dp[node][0], dp[node][1])
        dp[cur_node][1] += dp[node][0]

N = int(input())
w_arr = [0] + list(map(int, input().split()))
graph = [[] for _ in range(N + 1)]
connect = [[] for _ in range(N + 1)]
parent = [0] * (N + 1)
dp = [[0] * 2 for _ in range(N + 1)]
track = [0] * (N + 1)
for _ in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

make_tree(1, 0)
dp_subtree_node(1)

print(max(dp[1][0], dp[1][1]))

res = []
queue = deque()
queue.append(1)
while queue:
    cur_node = queue.popleft()
    if track[parent[cur_node]] == 0 and dp[cur_node][0] < dp[cur_node][1]:
        track[cur_node] = 1
        res.append(cur_node)
    for node in connect[cur_node]:
        queue.append(node)
res.sort()
print(*res)
