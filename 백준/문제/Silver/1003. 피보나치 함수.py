import sys
input = sys.stdin.readline

def fibonacci(n):
    if dp[n][0] or dp[n][1]:
        return
    for i in range(n + 1):
        if dp[i][0] or dp[i][1]:
            continue
        dp[i][0] = dp[i - 1][0] + dp[i - 2][0]
        dp[i][1] = dp[i - 1][1] + dp[i - 2][1]

T = int(input())
dp = [[0] * 2 for _ in range(41)]
dp[0][0] = 1
dp[1][1] = 1
for _ in range(T):
    n = int(input())
    fibonacci(n)
    print(dp[n][0], dp[n][1])
