import sys

input = sys.stdin.readline


def solve():
    N, M = map(int, input().split())

    nodes = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        nodes[a].append(b)

    connect = [0] * (N + 1)
    for i in range(1, N + 1):
        stack = [i]
        visited = set()
        while stack:
            cur = stack.pop()
            for next in nodes[cur]:
                if next in visited:
                    continue
                stack.append(next)
                visited.add(next)
        connect[i] += len(visited) + 1
        for node in visited:
            connect[node] += 1

    print(connect.count(N))


solve()
