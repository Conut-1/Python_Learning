def search(start, end):
    for i in range(start[0], end[0] + 1):
        for j in range(start[1], end[1] + 1):
            if i + 1 < end[0] + 1:
                dp[i + 1][j] += dp[i][j]
            if j + 1 < end[1] + 1:
                dp[i][j + 1] += dp[i][j]

N, M, K = map(int, input().split())

circle = ((K - 1) // M, (K - 1) % M)
dp = [[0] * M for _ in range(N)]
dp[0][0] = 1

if K == 0:
    search((0, 0), (N - 1, M - 1))
else:
    search((0, 0), circle)
    search(circle, (N - 1, M - 1))

print(dp[-1][-1])
