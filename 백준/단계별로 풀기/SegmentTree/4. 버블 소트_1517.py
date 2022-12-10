import sys
input = sys.stdin.readline

def init(start, end, node):
    if start == end:
        tree[node] = 1
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

def update(start, end, node, index, value):
    if index < start or index > end:
        return
    if start == end:
        tree[node] = value
        return
    mid = (start + end) // 2
    update(start, mid, node * 2, index, value)
    update(mid + 1, end, node * 2 + 1, index, value)
    tree[node] = tree[node * 2] + tree[node * 2 + 1]

N = int(input())
arr = list(map(int, input().split()))
tree = [0] * (N * 4)

init(0, N - 1, 1)

arr_2 = []
for i in range(N):
    arr_2.append((arr[i], i))
arr_2.sort()

res = 0
for i in range(N):
    q = arr_2[i][1]
    res += sum(0, N - 1, 1, 0, q) - 1
    update(0, N - 1, 1, q, 0)
print(res)
