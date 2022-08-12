from collections import deque
import sys
input = sys.stdin.readline

def ac():
    mode = 0
    res = []
    for inst in insts:
        if inst == "R":
            mode = (mode + 1) % 2
        elif inst == "D":
            if len(queue) == 0:
                return "error"
            elif mode == 0:
                queue.popleft()
            elif mode == 1:
                queue.pop()
    if mode == 0:
        while queue:
            res.append(queue.popleft())
    elif mode == 1:
        while queue:
            res.append(queue.pop())
    return f"[{','.join(map(str, res))}]"


t = int(input())
for _ in range(t):
    insts = input().rstrip()
    n = int(input())
    arr = list(map(int, input()[1:-2].replace(',', ' ').split()))
    queue = deque(arr)
    print(ac())
