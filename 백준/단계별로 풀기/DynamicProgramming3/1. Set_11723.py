import sys
input = sys.stdin.readline

def add(s, num):
    s |= 1 << (num - 1)
    return s

def remove(s, num):
    s &= ~(1 << (num - 1))
    return s

def check(s, num):
    if s & (1 << (num - 1)):
        print(1)
    else:
        print(0)

def all():
    s = (1 << 20) - 1
    return s

def toggle(s, num):
    if s & (1 << (num - 1)):
        s &= ~(1 << (num - 1))
    else:
        s |= 1 << (num - 1)
    return s

def empty():
    return 0

M = int(input())
s = 0
for _ in range(M):
    inst = input().split()
    if inst[0] == "add":
        s = add(s, int(inst[1]))
    elif inst[0] == "remove":
        s = remove(s, int(inst[1]))
    elif inst[0] == "check":
        check(s, int(inst[1]))
    elif inst[0] == "toggle":
        s = toggle(s, int(inst[1]))
    elif inst[0] == "all":
        s = all()
    elif inst[0] == "empty":
        s = empty()
