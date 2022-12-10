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
    res.append(node - size + 1)
    update(node, -1)

N, K = map(int, input().split())
size = 2 ** math.ceil(math.log2(N))
tree = [0] * (2 * size)
for i in range(N):
    update(size + i, 1)

res = []
target = 1
while tree[1]:
    target += K - 1
    target = tree[1] if target % tree[1] == 0 else target % tree[1]
    pop(1, target)

print(f'<{(", ").join(map(str, res))}>')
