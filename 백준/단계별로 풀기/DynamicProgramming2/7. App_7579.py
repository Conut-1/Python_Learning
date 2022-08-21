n, m = map(int, input().split())
memories = list(map(int, input().split()))
costs = list(map(int, input().split()))

size = sum(costs)
cost_dp = [0] * (size + 1)
for memory, cost in zip(memories, costs):
    for i in range(size - cost, -1, -1):
        if cost_dp[i + cost] < cost_dp[i] + memory:
            cost_dp[i + cost] = cost_dp[i] + memory
for i in range(1, size + 1):
    if cost_dp[i] >= m:
        res = i
        break

print(i)
