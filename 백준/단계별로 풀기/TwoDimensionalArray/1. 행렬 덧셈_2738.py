import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr_a = [list(map(int, input().split())) for _ in range(N)]
arr_b = [list(map(int, input().split())) for _ in range(N)]

res = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        res[i][j] = arr_a[i][j] + arr_b[i][j]

for line in res:
    print(*line)
