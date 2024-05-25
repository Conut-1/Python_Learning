from operator import add, sub, mul, truediv
from collections import deque

s, t = map(int, input().split())

ops = {"*": mul, "+": add, "-": sub, "/": truediv}

res = -1
queue = deque()
check = set()
if s != t:
    queue.append((s, ""))
    check.add(s)
else:
    res = 0

while queue:
    cur, method = queue.popleft()
    if cur == t:
        res = method
        break
    if cur == 0:
        continue
    for op, op_func in ops.items():
        next = int(op_func(cur, cur))
        if next in check:
            continue
        if next > t:
            continue
        queue.append((next, method + op))
        check.add(next)

print(res)
