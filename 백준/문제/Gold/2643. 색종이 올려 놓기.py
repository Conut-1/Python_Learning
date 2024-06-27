import sys

input = sys.stdin.readline

N = int(input())
papers = []
for _ in range(N):
    a, b = map(int, input().split())
    if a > b:
        papers.append((a, b))
    else:
        papers.append((b, a))

papers.sort(reverse=True)

dp = [0] * N
for i in range(N):
    for j in range(i):
        if (
            papers[i][0] <= papers[j][0]
            and papers[i][1] <= papers[j][1]
            and dp[i] < dp[j]
        ):
            dp[i] = dp[j]
    dp[i] += 1

print(max(dp))
