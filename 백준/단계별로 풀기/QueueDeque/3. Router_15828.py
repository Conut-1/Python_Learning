import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
queue = deque()
while True:
    inst = int(input())
    if inst == -1:
        break
    if inst == 0:
        queue.popleft()
    elif len(queue) < N:
        queue.append(inst)

if len(queue):
    print(*queue)
else:
    print("empty")
