import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def init(start, end, node):
    if start == end:
        tree[node] = start
        return
    mid = (start + end) // 2
    init(start, mid, node * 2)
    init(mid + 1, end, node * 2 + 1)
    if h[tree[node * 2]] <= h[tree[node * 2 + 1]]:
        tree[node] = tree[node * 2]
    else:
        tree[node] = tree[node * 2 + 1]

def find_lowest_idx(start, end, node, left, right):
    if left > end or right < start:
        return -1
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    x = find_lowest_idx(start, mid, node * 2, left, right)
    y = find_lowest_idx(mid + 1, end, node * 2 + 1, left, right)
    if h[x] <= h[y]:
        return x
    else:
        return y

def find_area(start, end):
    global area

    if end < start:
        return
    if start == end:
        area = max(area, h[start])
        return
    idx = find_lowest_idx(0, n - 1, 1, start, end)
    find_area(start, idx - 1)
    find_area(idx + 1, end)

    area = max(area, h[idx] * (end - start + 1))

while True:
    test_case = list(map(int, input().split()))
    if test_case[0] == 0:
        break

    n, *h = test_case
    h.append(float("inf"))
    tree = [-1] * (n * 4)
    init(0, n - 1, 1)

    area = 0
    find_area(0, n - 1)

    print(area)
