import sys

input = sys.stdin.readline

n, q = map(int, input().split())
lands = set()
for _ in range(q):
    target = int(input())
    cur = target
    res = 0
    while cur != 0:
        if cur in lands:
            res = cur
        cur //= 2
    lands.add(target)
    print(res)
