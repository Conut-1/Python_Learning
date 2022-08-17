import heapq
import sys
input = sys.stdin.readline


n = int(input())
min_heap = []
max_heap = []
for i in range(n):
    num = int(input())
    heapq.heappush(min_heap, num)
    if i % 2 == 0:
        num = heapq.heappop(min_heap)
        heapq.heappush(max_heap, (-num, num))
        num = heapq.heappop(max_heap)[1]
        heapq.heappush(min_heap, num)
        print(min_heap[0])
    else:
        num = heapq.heappop(min_heap)
        heapq.heappush(max_heap, (-num, num))
        print(max_heap[0][1])
