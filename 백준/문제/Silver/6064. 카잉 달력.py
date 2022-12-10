import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    m, n, x, y = map(int, input().split())
    f = 1
    while x <= m * n:
        if x % n == y % n:
            print(x)
            f = 0
            break
        x += m
    if f:
        print(-1)
