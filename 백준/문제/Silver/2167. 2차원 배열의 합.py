import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

prefix_sum = [[0] * (M + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, M + 1):
        prefix_sum[i][j] = arr[i - 1][j - 1] + prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1]

K = int(input())
for _ in range(K):
    i, j, x, y = map(int, input().split())
    print(prefix_sum[x][y] - prefix_sum[i - 1][y] - prefix_sum[x][j - 1] + prefix_sum[i - 1][j - 1])
