n = int(input())
arr = list(map(int, input().split()))

dp = []
for i in range(n):
    dp.append([0, 0])
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i][0] = max(dp[i][0], dp[j][0])
        if arr[i] < arr[j]:
            dp[i][1] = max(dp[i][1], dp[j][0], dp[j][1])
    dp[i][0] += 1
    dp[i][1] += 1

max_res = 0
for i in range(n):
    if dp[i][0] > max_res:
        max_res = dp[i][0]
    if dp[i][1] > max_res:
        max_res = dp[i][1]
print(max_res)
