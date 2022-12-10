import sys
input = sys.stdin.readline

scenario = 1
while True:
    death = False
    o, w = map(int, input().split())
    if o == 0 and w == 0:
        break
    while True:
        act, size = input().split()
        if act == '#':
            if o // 2 < w < o * 2:
                print(scenario, ':-)')
            elif w <= 0:
                print(scenario, 'RIP')
            else:
                print(scenario, ':-(')
            break
        if w <= 0:
            continue
        if act == 'F':
            w += int(size)
        else:
            w -= int(size)
    scenario += 1
