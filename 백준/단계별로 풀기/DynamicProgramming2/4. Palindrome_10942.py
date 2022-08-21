import sys
input = sys.stdin.readline


n = int(input())
arr = list(map(int, input().split()))

dp = [[0] * n for _ in range(n)]
for i in range(n):
    dp[i][i] = 1
for i in range(n - 1):
    if arr[i] == arr[i + 1]:
        dp[i][i + 1] = 1
for v in range(2, n):
    for i in range(n - v):
        j = i + v
        if dp[i + 1][j - 1] == 1 and arr[i] == arr[j]:
            dp[i][j] = 1

m = int(input())
for _ in range(m):
    s, e = map(int, input().split())

    print(dp[s - 1][e - 1])
