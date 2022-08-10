from collections import deque

n = int(input())
cards = [i for i in range(1, n + 1)]

queue = deque(cards)
while True:
    if len(queue) == 1:
        break
    queue.popleft()
    queue.append(queue.popleft())

print(queue[0])
