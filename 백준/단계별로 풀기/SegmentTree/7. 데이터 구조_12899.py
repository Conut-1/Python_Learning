import sys
import math
input = sys.stdin.readline

def update(node, diff):
    while node >= 1:
        tree[node] += diff
        node //= 2

def pop(node, index):
    while node < size:
        if tree[node * 2] < index:
            index -= tree[node * 2]
            node = node * 2 + 1
        else:
            node = node * 2
    print(node - size + 1)
    update(node, -1)

LIMIT = 2_000_000
N = int(input())
size = 2 ** math.ceil(math.log2(LIMIT))
tree = [0] * (2 * size)
for _ in range(N):
    mode, num = map(int, input().split())
    if mode == 1:
        update(size + num - 1, 1)
    else:
        pop(1, num)
