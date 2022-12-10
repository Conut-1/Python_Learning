N = int(input())
p = list(map(int, input().split()))

maximum = 0
cur_height = p[0]
height = p[0]
for h in p:
    if h <= cur_height:
        height = h
    if h > height:
        maximum = max(maximum, h - height)
    cur_height = h

print(maximum)
