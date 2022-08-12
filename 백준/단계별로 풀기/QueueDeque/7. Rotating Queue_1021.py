from collections import deque

n, m = map(int, input().split())
target = list(map(int, input().split()))

queue = deque([i for i in range(1, n + 1)])
size = n
res = 0
for i in range(len(target)):
    count = 0
    while target[i] != queue[0]:
        count += 1
        queue.append(queue.popleft())
    queue.popleft()
    res += min(count, size - count)
    size -= 1

print(res)
