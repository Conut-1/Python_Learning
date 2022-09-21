from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    while queue:
        cur = queue.popleft()
        for next in tree[cur]:
            if parents[next] == 0:
                parents[next] = cur
                queue.append(next)


N = int(input())
tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

parents = [0 for _ in range(N + 1)]

queue = deque([1])
bfs()

for parent in parents[2:]:
    print(parent)
