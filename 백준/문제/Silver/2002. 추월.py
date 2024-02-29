import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
in_order = deque([input().rstrip() for _ in range(n)])
out_order = [input().rstrip() for _ in range(n)]

overtake_set = set()
for out in out_order:
    if in_order[0] != out:
        overtake_set.add(out)
    else:
        in_order.popleft()
    while in_order and in_order[0] in overtake_set:
        in_order.popleft()

print(len(overtake_set))
