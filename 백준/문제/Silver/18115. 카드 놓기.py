from collections import deque

N = int(input())
skill = list(map(int, input().split()))

card = deque()
for i in range(1, N + 1):
    if skill[-i] == 1:
        card.appendleft(i)
    elif skill[-i] == 2:
        tmp = card.popleft()
        card.appendleft(i)
        card.appendleft(tmp)
    else:
        card.append(i)

print(*card)
