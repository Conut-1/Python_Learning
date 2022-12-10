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

def update(start, end, node, index, value):
    if index < start or index > end:
        return
    if start == end:
        tree[node][0], tree[node][1] = value, value
        return
    mid = (start + end) // 2
    update(start, mid, node * 2, index, value)
    update(mid + 1, end, node * 2 + 1, index, value)
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


T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    arr = [i for i in range(n)]
    tree = [[float("-inf"), float("inf")] for _ in range(n * 4)]
    init(0, n - 1, 1)
    for _ in range(k):
        q, a, b = map(int, input().split())
        if q == 1:
            sol = solve(0, n - 1, 1, a, b)
            if sol[0] == a and sol[1] == b:
                print("YES")
            else:
                print("NO")
        else:
            arr[a], arr[b] = arr[b], arr[a]
            update(0, n - 1, 1, a, arr[a])
            update(0, n - 1, 1, b, arr[b])
