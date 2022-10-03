import sys
input = sys.stdin.readline


def inst_1(i, x):
    bulbs[i - 1] = x

def inst_2(l, r):
    for i in range(l, r + 1):
        if bulbs[i - 1] == 0:
            bulbs[i - 1] = 1
        else:
            bulbs[i - 1] = 0

def inst_3(l, r):
    for i in range(l, r + 1):
        bulbs[i - 1] = 0

def inst_4(l, r):
    for i in range(l, r + 1):
        bulbs[i - 1] = 1


N, M = map(int, input().split())
bulbs = list(map(int, input().split()))
for _ in range(M):
    inst, a, b = map(int, input().split())
    if inst == 1:
        inst_1(a, b)
    elif inst == 2:
        inst_2(a, b)
    elif inst == 3:
        inst_3(a, b)
    elif inst == 4:
        inst_4(a, b)

print(*bulbs)
