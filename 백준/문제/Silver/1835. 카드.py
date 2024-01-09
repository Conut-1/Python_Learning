from collections import deque

n = int(input())
cards = deque([n])

for i in range(1, n):
    cards.appendleft(n - i)
    for _ in range((n - i) % (i + 1)):
        cards.appendleft(cards.pop())

print(" ".join(map(str, cards)))
