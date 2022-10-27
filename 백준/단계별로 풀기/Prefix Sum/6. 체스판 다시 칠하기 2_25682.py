import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]

temp = 0
for i in range(N):
    color = "B" if i % 2 == 0 else "W"
    for j in range(M):
        board[i][j] = 1 if color != board[i][j] else 0
        color = "B" if color == "W" else "W"

prefix_sum = [[0] * (M + 1) for _ in range(N + 1)]
for i in range(N):
    for j in range(M):
        prefix_sum[i + 1][j + 1] = board[i][j] + prefix_sum[i][j + 1] + prefix_sum[i + 1][j] - prefix_sum[i][j]

minimum = K * K
for i in range(N - K + 1):
    for j in range(M - K + 1):
        count = prefix_sum[i + K][j + K] - prefix_sum[i + K][j] - prefix_sum[i][j + K] + prefix_sum[i][j]
        minimum = min(minimum, count, K * K - count)

print(minimum)
