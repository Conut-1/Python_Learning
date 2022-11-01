def find_res(n):
    for i in range(1, n + 1):
        if dp[i]:
            continue
        dp[i] = (dp[i - 1] + dp[i - 2] * 2) % 10007

n = int(input())

dp = [0] * 1001
dp[1] = 1
dp[2] = 3
find_res(n)
print(dp[n] % 10007)
