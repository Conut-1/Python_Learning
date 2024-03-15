import sys
import heapq

input = sys.stdin.readline

n, h_centi, t = map(int, input().split())
h_giants = []
for _ in range(n):
    h_giant = int(input())
    h_giants.append((-h_giant, h_giant))
heapq.heapify(h_giants)

count = 0
for _ in range(t):
    __, h = heapq.heappop(h_giants)
    if h < h_centi:
        heapq.heappush(h_giants, (-h, h))
        break
    if h != 1:
        h //= 2
    heapq.heappush(h_giants, (-h, h))
    count += 1

_, h = heapq.heappop(h_giants)
if h < h_centi:
    print("YES")
    print(count)
else:
    print("NO")
    print(h)
