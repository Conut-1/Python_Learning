import sys
input = sys.stdin.readline

T = int(input())
k = int(input())
coins = [tuple(map(int, input().split())) for _ in range(k)]

coins.sort(reverse=True)
dp = [0] * (T + 1)
dp[0] = 1
for coin, n in coins:
    for i in range(T, -1, -1):
        for j in range(1, n + 1):
            if i - coin * j < 0:
                break
            dp[i] += dp[i - coin * j]

print(dp[-1])
