import sys

input = sys.stdin.readline

n = int(input())
conferences = [list(map(int, input().split())) for _ in range(n)]

count = [[0] * (n + 1) for _ in range(2)]
for i in range(1, len(conferences) + 1):
    count[0][i] = max(count[0][i - 1], count[1][i - 1] + conferences[i - 1][2])
    count[1][i] = max(count[0][i - 1], count[1][i - 1])

print(max(count[0][-1], count[1][-1]))
