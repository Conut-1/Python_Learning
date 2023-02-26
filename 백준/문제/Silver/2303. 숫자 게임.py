from itertools import combinations
import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

highest_player = 0
max_score = 0
for i in range(N):
    score = 0
    comb = combinations(arr[i], 3)
    for c in comb:
        if score < sum(c) % 10:
            score = sum(c) % 10
    if score >= max_score:
        max_score = score
        highest_player = i + 1

print(highest_player)
