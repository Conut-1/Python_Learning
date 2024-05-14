import sys
import math

input = sys.stdin.readline

n, h_atk = map(int, input().split())
h_hp = 0
res = 0
for _ in range(n):
    t, a, h = map(int, input().split())
    if t == 1:
        h_hp += (math.ceil(h / h_atk) - 1) * a
        if h_hp > res:
            res = h_hp
    else:
        h_atk += a
        h_hp -= h
        if h_hp < 0:
            h_hp = 0

print(res + 1)
