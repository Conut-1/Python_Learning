import sys
input = sys.stdin.readline

while 1:
    pos = list(map(int, input().split()))
    pos.sort()
    if pos[0] == 0:
        break
    if pos[0] ** 2 + pos[1] ** 2 == pos[2] ** 2:
        print("right")
    else:
        print("wrong")
