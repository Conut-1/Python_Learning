from collections import deque
import sys
input = sys.stdin.readline


def bfs(start):
    res = 0
    res_i = start
    while queue:
        cur, cur_cost = queue.popleft()
        if res < cur_cost:
            res_i = cur
            res = cur_cost
        for next, next_cost in tree[cur]:
            if visited[next] == 0:
                queue.append((next, cur_cost + next_cost))
                visited[next] = 1
    return res, res_i


N = int(input())
tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b, c = map(int, input().split())
    tree[a].append((b, c))
    tree[b].append((a, c))

visited = [0] * (N + 1)
queue = deque([(1, 0)])
visited[1] = 1
tmp, tmp_i = bfs(1)

visited = [0] * (N + 1)
queue = deque([(tmp_i, 0)])
visited[tmp_i] = 1
res, res_i = bfs(tmp_i)

print(res)
