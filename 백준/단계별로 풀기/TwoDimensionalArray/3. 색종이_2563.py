import sys
input = sys.stdin.readline

N = int(input())
arr = [[0] * 100 for _ in range(100)]

for _ in range(N):
    a, b = map(int, input().split())
    for i in range(a, a + 10):
        for j in range(b, b + 10):
            arr[i][j] = 1

area = 0
for line in arr:
    area += line.count(1)

print(area)
