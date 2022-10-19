N = int(input())
arr = [0]
for _ in range(N):
    arr.append(list(map(int, input().split())))

dp = [0] * (N + 2)
for i in range(N, 0, -1):
    dp[i] = dp[i + 1]
    if i + arr[i][0] - 1 > N:
        continue
    if dp[i] < arr[i][1] + dp[i + arr[i][0]]:
        dp[i] = arr[i][1] + dp[i + arr[i][0]]

print(dp[1])
