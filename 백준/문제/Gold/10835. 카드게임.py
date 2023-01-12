import sys
sys.setrecursionlimit(10 ** 6)

def solve(x, y):
    if x >= N or y >= N:
        return 0

    if dp[x][y] != -1:
        return dp[x][y]

    if left[x] > right[y]:
        dp[x][y] = solve(x, y + 1) + right[y]
    else:
        discard_left = solve(x + 1, y) 
        discard_both = solve(x + 1, y + 1) 
        dp[x][y] = max(discard_left, discard_both)

    return dp[x][y]


N = int(input())
left = list(map(int, input().split()))
right = list(map(int, input().split()))

dp = [[-1] * (N) for _ in range(N)]
solve(0, 0)
print(dp[0][0])
