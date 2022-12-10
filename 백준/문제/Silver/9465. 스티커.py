import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    arr = [([0] + list(map(int, input().split()))) for _ in range(2)]
    dp = [[0] * (n + 1) for _ in range(2)]

    for i in range(1, n + 1):
        dp[0][i] = max(dp[1][i - 1] + arr[0][i], dp[0][i - 1])
        dp[1][i] = max(dp[0][i - 1] + arr[1][i], dp[1][i - 1])
    
    print(max(dp[0][-1], dp[1][-1]))
