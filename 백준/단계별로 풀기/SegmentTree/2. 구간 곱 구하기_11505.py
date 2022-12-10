import sys
input = sys.stdin.readline

def init(start, end, node):
    if start == end:
        tree[node] = arr[start] % 1_000_000_007
        return tree[node]
    mid = (start + end) // 2
    tree[node] = init(start, mid, node * 2) * init(mid + 1, end, node * 2 + 1) % 1_000_000_007
    return tree[node]

def mul(start, end, node, left, right):
    if left > end or right < start:
        return 1
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return mul(start, mid, node * 2, left, right) * mul(mid + 1, end, node * 2 + 1, left, right) % 1_000_000_007

def update(start, end, node, index, new):
    if index < start or index > end:
        return
    if start == end:
        tree[node] = new % 1_000_000_007
        return
    mid = (start + end) // 2
    update(start, mid, node * 2, index, new)
    update(mid + 1, end, node * 2 + 1, index, new)
    tree[node] = tree[node * 2] * tree[node * 2 + 1] % 1_000_000_007

N, M, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
tree = [1] * (N * 4)
init(0, N - 1, 1)
for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        update(0, N - 1, 1, b - 1, c)
    if a == 2:
        print(mul(0, N - 1, 1, b - 1, c - 1))
