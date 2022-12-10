from collections import deque

def bfs(a, b):
    queue = deque()
    queue.append((a, 1))
    while queue:
        cur, count = queue.popleft()
        if cur == b:
            return count
        if cur > b:
            continue
        next = cur * 2
        queue.append((next, count + 1))
        next = int(str(cur) + "1")
        queue.append((next, count + 1))
    return -1

A, B = map(int, input().split())
print(bfs(A, B))
