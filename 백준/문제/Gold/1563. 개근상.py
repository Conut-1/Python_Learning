N = int(input())

dp = [[[0] * 3 for _ in range(2)] for _ in range(N)]
dp[0][0][0] = 1
dp[0][0][1] = 1
dp[0][1][0] = 1

for i in range(1, N):
    dp[i][0][0] = sum(dp[i - 1][0]) % 1_000_000
    dp[i][0][1] = dp[i - 1][0][0]
    dp[i][0][2] = dp[i - 1][0][1]
    dp[i][1][0] = (sum(dp[i - 1][0]) + sum(dp[i - 1][1])) % 1_000_000
    dp[i][1][1] = dp[i - 1][1][0]
    dp[i][1][2] = dp[i - 1][1][1]

print((sum(dp[-1][0]) + sum(dp[-1][1])) % 1_000_000)
