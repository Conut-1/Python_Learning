import sys
input = sys.stdin.readline


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]
for i in range(n - 1):
    dp[i][i + 1] = arr[i][0] * arr[i][1] * arr[i + 1][1]

for v in range(2, n):
    for i in range(n - v):
        j = i + v
        dp[i][j] = min([dp[i][k] + dp[k + 1][j] + arr[i][0] * arr[k][1] * arr[j][1] for k in range(i, j)])

print(dp[0][-1])
