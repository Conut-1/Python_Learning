import sys
input = sys.stdin.readline


n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
m, k = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(m)]

res = [[0] * k for _ in range(n)]
for i in range(n * k):
    sum = 0
    for j in range(m):
        sum += a[i // k][j] * b[j][i % k]
    res[i // k][i % k] = sum

for line in res:
    print(*line)
