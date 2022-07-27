import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dict = {}
for pos in arr:
    if pos[1] in dict:
        dict[pos[1]].append(pos[0])
    else:
        dict[pos[1]] = [pos[0]]

key = sorted(dict.keys())
for k in key:
    pos_x = sorted(dict[k])
    for x in pos_x:
        print(x, k)
