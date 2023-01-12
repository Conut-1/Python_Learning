import sys
from math import gcd
input = sys.stdin.readline

def solve():
    a, b = map(int, input().split())
    arr = [[False] * (b + 1) for _ in range(b)]

    ans = 0

    for i in range(a, b + 1):
        for j in range(i):
            g = gcd(j, i)
            x, y = j // g, i // g
            if not arr[x][y]:
                arr[x][y] = True
                ans += 1

    print(ans)

solve()
