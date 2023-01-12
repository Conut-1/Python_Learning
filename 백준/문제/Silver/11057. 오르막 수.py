N = int(input())
dp = [[0] * 10 for _ in range(N + 1)]

for i in range(10):
    dp[0][i] = 1

for i in range(1, N + 1):
    for j in range(10):
        dp[i][j] = sum(dp[i - 1][:j + 1]) % 10_007

print(dp[N][-1])
