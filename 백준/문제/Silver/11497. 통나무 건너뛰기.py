import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    l = list(map(int, input().split()))

    l.sort()
    res = 0
    for i in range(n - 2):
        res = max(res, l[i + 2] - l[i])
    print(res)
