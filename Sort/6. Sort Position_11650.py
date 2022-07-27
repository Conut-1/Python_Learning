import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dict = {}
for pos in arr:
    if pos[0] in dict:
        dict[pos[0]].append(pos[1])
    else:
        dict[pos[0]] = [pos[1]]

key = sorted(dict.keys())
for k in key:
    pos_y = sorted(dict[k])
    for y in pos_y:
        print(k ,y)
