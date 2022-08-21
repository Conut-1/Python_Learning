import sys
input = sys.stdin.readline


t = int(input())
for i in range(t):
    n = int(input())
    files = list(map(int, input().split()))

    d = [[0] * n for _ in range(n)]
    for i in range(n - 1):
        d[i][i + 1] = files[i] + files[i + 1]
        for j in range(i + 2, n):
            d[i][j] = d[i][j - 1] + files[j]
    for v in range(2, n):
        for i in range(n - v):
            j = i + v
            d[i][j] += min([d[i][k] + d[k + 1][j] for k in range(i, j)])

    print(d[0][n - 1])

# import sys
# input = sys.stdin.readline


# def dp(start, end):
#     if d[start][end] != -1:
#         return d[start][end]
#     if start == end:
#         return 0

#     ans = float('inf')
#     s = sum(files[start:end + 1])
#     for i in range(start, end):
#         temp = dp(start, i) + dp(i + 1, end) + s
#         ans = min(ans, temp)
#         d[start][end] = ans

#     return ans

# t = int(input())
# for i in range(t):
#     n = int(input())
#     files = list(map(int, input().split()))
#     d = [[-1] * n for _ in range(n)]

#     print(d)
