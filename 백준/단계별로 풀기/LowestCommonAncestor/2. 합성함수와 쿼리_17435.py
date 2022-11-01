import sys
input = sys.stdin.readline

MAX_LOG_K = 19

def solve(n, x):
    cur = x
    for i in reversed(range(MAX_LOG_K + 1)):
        if (n & (1 << i)):
            cur = table[i][cur]

    return cur

m = int(input())
f = [0] + list(map(int, input().split()))

table = [[0] * (m + 1) for _ in range(MAX_LOG_K + 1)]
for i in range(1, m + 1):
    table[0][i] = f[i]

for k in range(1, MAX_LOG_K + 1):
    for i in range(1, m + 1):
        tmp = table[k - 1][i]

        table[k][i] = table[k - 1][tmp]

Q = int(input())
for _ in range(Q):
    n, x = map(int, input().split())
    print(solve(n, x))
