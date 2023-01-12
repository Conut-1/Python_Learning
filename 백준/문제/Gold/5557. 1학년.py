N = int(input())
numbers = list(map(int, input().split()))

dp = [[0] * (20 + 1) for _ in range(N)]
dp[0][numbers[0]] = 1

for i in range(1, N - 1):
    for value in range(20 + 1):
        if dp[i - 1][value]:
            if value + numbers[i] <= 20:
                dp[i][value + numbers[i]] += dp[i - 1][value]
            if value - numbers[i] >= 0:
                dp[i][value - numbers[i]] += dp[i - 1][value]

print(dp[N - 2][numbers[-1]])
