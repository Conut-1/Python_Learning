import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

res = float("inf")
for color in range(3):
    dp = [[float("inf")] * 3 for _ in range(N)]
    dp[0][color] = arr[0][color]
    for i in range(N - 1):
        dp[i + 1][0] = arr[i + 1][0] + min(dp[i][1], dp[i][2])
        dp[i + 1][1] = arr[i + 1][1] + min(dp[i][0], dp[i][2])
        dp[i + 1][2] = arr[i + 1][2] + min(dp[i][0], dp[i][1])
    for i in range(3):
        if i != color:
            res = min(res, dp[N - 1][i])

print(res)
