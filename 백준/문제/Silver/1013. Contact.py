import sys
import re
input = sys.stdin.readline


T = int(input())
p = re.compile('^(100+1+|01)+$')
for _ in range(T):
    wave = input()
    m = p.match(wave)
    if m:
        print("YES")
    else:
        print("NO")
