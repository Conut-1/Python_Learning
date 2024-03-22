import sys
import heapq


def solve():
    input = sys.stdin.readline

    n = int(input())

    classes = [tuple(map(int, input().split())) for _ in range(n)]
    classes.sort()

    res = 0
    t_heap = []
    for s, t in classes:
        while t_heap and t_heap[0] <= s:
            heapq.heappop(t_heap)
        res = max(res, len(t_heap) + 1)
        heapq.heappush(t_heap, t)

    print(res)


solve()
