import sys
from math import gcd

input = sys.stdin.readline

N = int(input())

line = {}
res = 0
for i in range(N):
    a, b, c = map(int, input().split())
    if a < 0:
        a *= -1
        b *= -1
    gcd_res = gcd(a, b)
    a //= gcd_res
    b //= gcd_res
    if a == 0:
        key = "0,1"
    elif b == 0:
        key = "1,0"
    else:
        key = ",".join(map(str, [a, b]))
    if key not in line:
        line[key] = 0
    res += i - line[key]
    line[key] += 1

print(res)
