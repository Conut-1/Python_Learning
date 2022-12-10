def fibonacci(n):
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

dp = [0] * 10001
dp[1] = 1
dp[2] = 1
n = int(input())
print(fibonacci(n))
