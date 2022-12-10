import sys
input = sys.stdin.readline

def init(start, end, node):
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    mid = (start + end) // 2
    tree[node] = init(start, mid, node * 2) + init(mid + 1, end, node * 2 + 1)
    return tree[node]

def sum(start, end, node, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return sum(start, mid, node * 2, left, right) + sum(mid + 1, end, node * 2 + 1, left, right)

def update(start, end, node, index, dif):
    if index < start or index > end:
        return
    tree[node] += dif
    if start == end:
        return
    mid = (start + end) // 2
    update(start, mid, node * 2, index, dif)
    update(mid + 1, end, node * 2 + 1, index, dif)

N, M, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
tree = [0] * (N * 4)
init(0, N - 1, 1)
for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        update(0, N - 1, 1, b - 1, c - arr[b - 1])
        arr[b - 1] = c
    if a == 2:
        print(sum(0, N - 1, 1, b - 1, c - 1))
