import sys
from heapq import heapify, heappop, heappush

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k = int(input())
    files = list(map(int, input().split()))

    res = 0
    heapify(files)

    while len(files) != 1:
        file1 = heappop(files)
        file2 = heappop(files)
        res += file1 + file2
        heappush(files, file1 + file2)

    print(res)
