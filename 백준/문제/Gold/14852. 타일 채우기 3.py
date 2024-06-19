N = int(input())

dp = [[0] * 2 for _ in range(N + 1)]
dp[0][0] = 1
dp[1][0] = 2
if N > 1:
    dp[2][0] = 7

for i in range(3, N + 1):
    dp[i][1] = (dp[i - 3][0] + dp[i - 1][1]) % 1_000_000_007
    dp[i][0] = (dp[i - 1][0] * 2 + dp[i - 2][0] * 3 + 2 * dp[i][1]) % 1_000_000_007

print(dp[-1][0] % 1_000_000_007)
