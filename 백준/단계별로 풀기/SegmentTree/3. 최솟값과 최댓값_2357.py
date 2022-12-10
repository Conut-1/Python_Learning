import sys
input = sys.stdin.readline

def init(start, end, node):
    if start == end:
        tree[node][0], tree[node][1] = arr[start], arr[start]
        return
    mid = (start + end) // 2
    init(start, mid, node * 2)
    init(mid + 1, end, node * 2 + 1)
    tree[node][0] = min(tree[node * 2][0], tree[node * 2 + 1][0])
    tree[node][1] = max(tree[node * 2][1], tree[node * 2 + 1][1])

def solve(start, end, node, left, right):
    if left > end or right < start:
        return [float("inf"), float("-inf")]
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    x = solve(start, mid, node * 2, left, right)
    y = solve(mid + 1, end, node * 2 + 1, left, right)
    return [min(x[0], y[0]), max(x[1], y[1])]

N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]
tree = [[float("-inf"), float("inf")] for _ in range(N * 4)]
init(0, N - 1, 1)
for _ in range(M):
    a, b = map(int, input().split())
    print(*solve(0, N - 1, 1, a - 1, b - 1))
