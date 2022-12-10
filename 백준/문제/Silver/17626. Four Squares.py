n = int(input())

dp = [float("inf")] * (n + 1)
dp[0] = 0
x = 0
for i in range(1, n + 1):
    x = int(i ** 0.5)
    for j in range(1, x + 1):
        dp[i] = min(dp[i], 1 + dp[i - j ** 2])

print(dp[n])
