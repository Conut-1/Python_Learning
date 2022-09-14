N = int(input())
arr = list(map(int, input().split()))

dp = [[] for _ in range(N)]
for i in range(N):
    for j in range(i):
        if arr[i] > arr[j] and len(dp[i]) < len(dp[j]):
            dp[i] = dp[j].copy()
    dp[i].append(arr[i])

res_len = 0
res_idx = 0
for i in range(N):
    if len(dp[i]) > res_len:
        res_len = len(dp[i])
        res_idx = i

print(res_len)
print(*dp[res_idx])
