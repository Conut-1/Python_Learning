n = int(input())
arr = list(map(int, input().split()))

dp = [0] * (n + 1)
dp[2] = 1 + abs(arr[0] - arr[1])
for i in range(3, n + 1):
    min_power = -1
    for j in range(1, i):
        route_power = max(dp[j], (i - j) * (1 + abs(arr[i - 1] - arr[j - 1])))
        if min_power == -1:
            min_power = route_power
        else:
            min_power = min(route_power, min_power)
    dp[i] = min_power

print(dp[-1])
