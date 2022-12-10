import sys
input = sys.stdin.readline

def init(start, end, node):
    if start == end:
        tree[node] = arr[start]
        return
    mid = (start + end) // 2
    init(start, mid, node * 2)
    init(mid + 1, end, node * 2 + 1)

def update(start, end, node, left, right, diff):
    if left > end or right < start:
        return
    if left <= start and end <= right:
        lazy[node] += diff
        return
    mid = (start + end) // 2
    update(start, mid, node * 2, left, right, diff)
    update(mid + 1, end, node * 2 + 1, left, right, diff)

def get(start, end, node, index):
    if index < start or index > end:
        return
    if start == end:
        tree[node] += lazy[node]
        lazy[node] = 0
        print(tree[node])
        return
    mid = (start + end) // 2
    if lazy[node]:
        lazy[node * 2] += lazy[node]
        lazy[node * 2 + 1] += lazy[node]
        lazy[node] = 0
    get(start, mid, node * 2, index)
    get(mid + 1, end, node * 2 + 1, index)

N = int(input())
arr = list(map(int, input().split()))
tree = [0] * (N * 4)
lazy = [0] * (N * 4)
init(0, N - 1, 1)

M = int(input())
for _ in range(M):
    mode, *args = map(int, input().split())
    if mode == 1:
        update(0, N - 1, 1, args[0] - 1, args[1] - 1, args[2])
    else:
        get(0, N - 1, 1, args[0] - 1)
