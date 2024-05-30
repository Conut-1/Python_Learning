import sys


def solve():
    input = sys.stdin.readline

    D, P = map(int, input().split())
    dp = [0] * (D + 1)
    dp[0] = float("inf")

    for _ in range(P):
        l, c = map(int, input().split())
        for i in range(D, l - 1, -1):
            dp[i] = max(dp[i], min(dp[i - l], c))

    print(dp[-1])


solve()
