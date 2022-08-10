from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, target_idx = map(int, input().split())
    doc = list(map(int, input().split()))

    queue = deque()
    priority = [0] * 9
    for el in doc:
        priority[el - 1] += 1
        queue.append(el)

    priority_idx = 8
    count = 0
    while True:
        while priority[priority_idx] == 0:
            priority_idx -= 1
        while queue[0] != priority_idx + 1:
            queue.append(queue.popleft())
            target_idx = (target_idx + n - 1) % n
        queue.popleft()
        priority[priority_idx] -= 1
        count += 1
        n -= 1
        if target_idx == 0:
            print(count)
            break
        target_idx -= 1
