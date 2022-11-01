import sys
input = sys.stdin.readline

def find_res(n):
    for i in range(1, n + 1):
        if dp[i]:
            continue
        if i > 0:
            dp[i] += dp[i - 1]
        if i > 1:
            dp[i] += dp[i - 2]
        if i > 2:
            dp[i] += dp[i - 3]

T = int(input())
dp = [0] * 11
dp[1] = 1
dp[0] = 1
for _ in range(T):
    n = int(input())
    find_res(n)
    print(dp[n])
