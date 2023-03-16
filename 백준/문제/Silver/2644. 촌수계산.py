import sys

input = sys.stdin.readline


def solve():
    visited[t_a] = 1
    stack = [(t_a, 0)]
    while stack:
        cur, dist = stack.pop()
        if cur == t_b:
            return dist

        for next in edges[cur]:
            if visited[next] == 1:
                continue
            visited[next] = 1
            next_dist = dist + 1
            stack.append((next, next_dist))

    return -1


N = int(input())
t_a, t_b = map(int, input().split())
M = int(input())

visited = [0] * (N + 1)
edges = [[] for _ in range(N + 1)]
for _ in range(M):
    x, y = map(int, input().split())

    edges[x].append(y)
    edges[y].append(x)

print(solve())
