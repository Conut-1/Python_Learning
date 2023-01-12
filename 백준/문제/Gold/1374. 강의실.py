import sys
import heapq
input = sys.stdin.readline

N = int(input())
lectures = [tuple(map(int, input().split())) for _ in range(N)]

room = [0]
lectures.sort(key=lambda x: (x[1], x[2]))
for lecture in lectures:
    if room[0] <= lecture[1]:
        heapq.heappop(room)
    heapq.heappush(room, lecture[2])

print(len(room))
